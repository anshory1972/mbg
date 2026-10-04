import requests,re,html,time,sys,json
H={"User-Agent":"lit-review (mailto:arief.yusuf@gmail.com)"}
def clean(t): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t or ''))).strip()
def get(doi):
    a=None
    try:
        m=requests.get(f"https://api.crossref.org/works/{doi}",headers=H,timeout=60).json()["message"]
        a=clean(m.get("abstract"))
    except Exception as e: pass
    if not a:
        r=requests.get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",params={"query":f'DOI:"{doi}"',"resultType":"core","format":"json"},timeout=60).json()
        res=r.get("resultList",{}).get("result",[])
        if res: a=clean(res[0].get("abstractText"))
    if not a:
        for k in range(3):
            r=requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",params={"fields":"abstract,tldr"},timeout=60)
            if r.status_code==200:
                j=r.json(); a=j.get("abstract") or ((j.get("tldr") or {}).get("text")); break
            time.sleep(4*(k+1))
    return a
out={}
for d in sys.argv[1:]:
    a=get(d); out[d]=a
    print(f"\n=== {d}\n{(a or 'NO ABSTRACT')[:1800]}"); time.sleep(1)
json.dump(out,open("abstracts_%d.json"%int(time.time()),"w"),indent=1)
