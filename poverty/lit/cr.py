import requests,sys,json,time
H={"User-Agent":"lit-review (mailto:arief.yusuf@gmail.com)"}
def search(q,rows=12,filt=None):
    p={"query.bibliographic":q,"rows":rows,"select":"DOI,title,author,issued,container-title,is-referenced-by-count,type","mailto":"arief.yusuf@gmail.com"}
    if filt:p["filter"]=filt
    r=requests.get("https://api.crossref.org/works",params=p,headers=H,timeout=60).json()
    for it in r["message"]["items"]:
        a=it.get("author",[{}]);au=(a[0].get("family","?") if a else "?")+(" et al." if len(a)>1 else "")
        y=it.get("issued",{}).get("date-parts",[[None]])[0][0]
        print(f'{it.get("is-referenced-by-count",0):>6} | {y} | {au} | {(it.get("title") or ["?"])[0][:110]} | {(it.get("container-title") or [""])[0][:40]} | {it["DOI"]}')
for q in sys.argv[1:]:
    print("\n### ",q); search(q); time.sleep(1)
