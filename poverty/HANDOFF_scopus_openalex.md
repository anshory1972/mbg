# Handoff: Scopus + OpenAlex literature cross-check

**For:** a Claude Code session on a machine that has Scopus (Elsevier) and/or OpenAlex API access.
**Repo:** `anshory1972/mbg`, branch **`poverty`**, folder `poverty/`.

## Context
`poverty/scarcity_robustness_review.md` reviews how robust the evidence is for:
- the "scarcity mindset" theory of Mullainathan & Shafir (poverty reduces cognitive bandwidth);
- claims made in two TED talks (Bregman 2017; Stewart 2024) about basic income and cash transfers.

That review was built using **Crossref and Europe PMC only**: Scopus had no key and the OpenAlex quota was used up. Your job is to cross-check it and extend it using Scopus and OpenAlex.

## Setup
```bash
git clone https://github.com/anshory1972/mbg.git && cd mbg
git checkout poverty
```
Use your existing Scopus / OpenAlex credentials from the environment, e.g. `SCOPUS_API_KEY`, optionally `SCOPUS_INSTTOKEN`, and `OPENALEX_API_KEY`. **Never write keys into files or commits.**

## Tasks

### 1. Scopus citation counts for the anchor papers
For each DOI below, get the Scopus record and report: Scopus EID, citation count, document type, and publication year. Use `https://api.elsevier.com/content/search/scopus?query=DOI(<doi>)`, or the Abstract Retrieval API. Also get the OpenAlex `cited_by_count` from `https://api.openalex.org/works/doi:<doi>`.

```
10.1126/science.1222426      Shah, Mullainathan & Shafir 2012 (Science)
10.1126/science.1238041      Mani et al. 2013 (Science)
10.1177/0956797614563958     Shah et al. 2015 Scarcity frames value
10.1126/science.1246680      Wicherts & Scholten 2013 comment
10.1126/science.1246799      Mani et al. 2013 reply
10.1257/aer.20140481         Carvalho, Meier & Wang 2016 (AER)
10.1086/709885               Mani et al. 2020 payday (JACR)
10.1038/s41562-018-0399-z    Camerer et al. 2018 replication project
10.1016/j.joep.2018.12.001   Shah et al. 2019 self-replication
10.1073/pnas.2103313118      O'Donnell et al. 2021 empirical audit (PNAS)
10.1073/pnas.2206054120      Shah et al. 2023 rebuttal (PNAS)
10.1525/collabra.122943      Szecsi et al. 2024 meta-analysis
10.1007/s11238-021-09802-7   de Bruijn & Antonides review
10.1017/s0265052523000419    Haushofer & Salicath 2023 review
10.1126/science.1232491      Haushofer & Fehr 2014
10.1126/science.aay0214      Ridley et al. 2020
10.1093/qje/qjae038          Kaur et al. financial concerns & productivity (QJE)
10.1073/pnas.1810901116      Ong et al. 2019 debt relief
10.1093/ej/ueab007           Bartos et al. 2021
10.1086/720466               Fehr, Fink & Jack 2022 (JPE)
10.2139/ssrn.3540149         Lichand & Mani "Cognitive droughts" (verify; find published version + abstract)
10.1287/mnsc.2013.1849       Fernandes et al. 2014 fin-lit meta-analysis
10.1016/j.jfineco.2021.09.022 Kaiser et al. 2022 fin-lit meta-analysis
10.3138/cpp.37.3.283         Forget 2011 Dauphin
10.3138/cpp.2021-025         Green 2022 Dauphin reanalysis
10.3138/cpp.2022-017         Forget 2022 reply
10.3982/ecta17945            Egger et al. 2022 GE cash Kenya
10.1093/qje/qjw025           Haushofer & Shapiro 2016
10.1086/689575               Evans & Popova 2017 temptation goods (get abstract)
10.1093/wbro/lkx002          Banerjee et al. 2017 lazy welfare (get abstract)
```

### 2. Forward-citation sweep (most important)
Use OpenAlex `filter=cites:<openalex_id>`, or Scopus `REFEID(...)`. For **Mani et al. 2013**, **Shah et al. 2012** and **Carvalho et al. 2016**, list the citing works whose title or abstract matches any of: `replicat*`, `meta-analy*`, `systematic review`, `null`, `fail*`, `registered report`, `re-analy*`, `reanaly*`, `bandwidth`, `cognitive load`, `cognitive function`.
Prioritise **2020–2026**. The question to answer: **are there new replications, meta-analyses or large field studies, for or against, that the current review misses?** Read the abstracts and classify each one as *supports / contradicts / mixed / not relevant*.

### 3. Extra Scopus keyword searches
```
TITLE-ABS-KEY(scarcity AND poverty AND (cognit* OR bandwidth) AND (meta-analys* OR replicat* OR "systematic review"))
TITLE-ABS-KEY("scarcity mindset" OR "scarcity theory") AND PUBYEAR > 2019
TITLE-ABS-KEY("cash transfer*" AND (cognit* OR "mental health" OR stress) AND meta-analys*)
TITLE-ABS-KEY(("school meal*" OR "school feeding") AND (cognit* OR learning) AND (meta-analys* OR "systematic review"))
```
The last query is for the MBG project: whether school meals affect cognition and learning.

## Deliverables (commit to the `poverty` branch)
1. `poverty/lit/scopus_openalex_check.csv` with columns: doi, short_ref, scopus_eid, scopus_citations, openalex_id, openalex_citations, year, doc_type, notes.
2. `poverty/lit/new_evidence.md`: new papers found in tasks 2–3. For each, give: full citation, DOI, design, N, main result in one or two lines (from the abstract), and a verdict (*supports / contradicts / mixed*) on the scarcity → cognition claim.
3. Update `poverty/scarcity_robustness_review.md`:
   - change the "Cites" columns to say Scopus;
   - add the new evidence to the right sections;
   - revise the **Bottom line** verdicts *only* if new evidence warrants it, saying why;
   - remove the note that Scopus and OpenAlex were not queried.
4. Commit with a clear message and `git push -u origin poverty`.

## Rules
- Report only what an abstract or record actually says. If an abstract is unavailable, write "abstract unavailable". Don't summarise from memory.
- Every reference must have a resolving DOI or Scopus EID.
- Keep keys out of the repo.
