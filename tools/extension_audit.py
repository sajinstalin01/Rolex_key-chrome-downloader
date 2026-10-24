#!/usr/bin/env python3
"""Offline heuristic audit of an unpacked Chrome/Chromium extension."""
import argparse, hashlib, json, re
from pathlib import Path
HIGH={"debugger","nativeMessaging","management","proxy","webRequestBlocking"}
MED={"cookies","history","clipboardRead","clipboardWrite","downloads","webNavigation"}
TEXT={".js",".html",".htm",".json"}
def main():
    p=argparse.ArgumentParser(description="Audit an unpacked browser extension locally")
    p.add_argument("folder",type=Path,help="Extension root containing manifest.json")
    p.add_argument("--json",action="store_true",help="Output JSON")
    a=p.parse_args(); root=a.folder.resolve(); mf=root/"manifest.json"
    if not mf.is_file(): p.error("manifest.json not found")
    try: m=json.loads(mf.read_text(encoding="utf-8"))
    except Exception as e: p.error(f"Invalid manifest JSON: {e}")
    findings=[]
    def add(level,message): findings.append({"level":level,"message":message})
    perms=set(m.get("permissions",[])+m.get("optional_permissions",[]))
    hosts=m.get("host_permissions",[])+m.get("optional_host_permissions",[])
    if any(x=="<all_urls>" or "://*/*" in x for x in hosts): add("high","Broad host access declared")
    for x in sorted(perms & HIGH): add("high",f"Powerful permission: {x}")
    for x in sorted(perms & MED): add("medium",f"Sensitive permission: {x}")
    csp=m.get("content_security_policy",{})
    if isinstance(csp,str) and "unsafe-eval" in csp: add("high","CSP contains unsafe-eval")
    if isinstance(csp,dict) and "unsafe-eval" in csp.get("extension_pages",""): add("high","CSP contains unsafe-eval")
    refs=[]
    for k in ("options_page","devtools_page"):
        if isinstance(m.get(k),str): refs.append(m[k])
    for k in ("action","browser_action","page_action"):
        v=m.get(k,{})
        if isinstance(v,dict):
            refs.extend(v[x] for x in ("default_popup",) if isinstance(v.get(x),str))
            if isinstance(v.get("default_icon"),str): refs.append(v["default_icon"])
            elif isinstance(v.get("default_icon"),dict): refs.extend(v["default_icon"].values())
    if isinstance(m.get("background"),dict) and isinstance(m["background"].get("service_worker"),str): refs.append(m["background"]["service_worker"])
    for c in m.get("content_scripts",[]): refs.extend(c.get("js",[])); refs.extend(c.get("css",[]))
    for x in sorted(set(refs)):
        if not (root/x).is_file(): add("medium",f"Referenced file missing: {x}")
    inspected=0
    for f in root.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in TEXT or f.stat().st_size>2_000_000: continue
        inspected+=1; s=f.read_text(encoding="utf-8",errors="replace"); rel=str(f.relative_to(root))
        if re.search(r"\beval\s*\(|\bnew\s+Function\s*\(",s): add("medium",f"{rel}: dynamic-code pattern; review manually")
        if re.search(r"fetch\s*\(|XMLHttpRequest|WebSocket",s) and "http" in s: add("medium",f"{rel}: network request pattern; verify destinations")
        if len(s)>12000 and re.search(r"atob\s*\(|String\.fromCharCode|\\x[0-9a-f]{2}",s,re.I): add("medium",f"{rel}: encoding/obfuscation indicators")
    report={"name":m.get("name","(unnamed)"),"version":m.get("version","(missing)"),"manifest_version":m.get("manifest_version"),"file_count":sum(x.is_file() for x in root.rglob("*")),"text_files_inspected":inspected,"manifest_sha256":hashlib.sha256(mf.read_bytes()).hexdigest(),"findings":findings,"disclaimer":"Heuristic static analysis only; not a malware verdict or guarantee of safety."}
    if not findings: report["findings"]=[{"level":"low","message":"No listed heuristic matched."}]
    if a.json: print(json.dumps(report,indent=2))
    else:
        print(f"{report['name']} v{report['version']} · Manifest V{report['manifest_version']}")
        print(f"Files: {report['file_count']} · Text files inspected: {inspected}")
        print(f"manifest.json SHA-256: {report['manifest_sha256']}")
        for f in report["findings"]: print(f"[{f['level'].upper()}] {f['message']}")
        print(report["disclaimer"])
if __name__=="__main__": main()
