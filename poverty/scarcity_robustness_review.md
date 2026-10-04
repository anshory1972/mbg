# How robust is the evidence behind the TED talks? A literature check

*Compiled 2026-10-04. Searches and metadata come from the **Crossref** and **Europe PMC** APIs. Scopus needs an API key this environment doesn't have, and the anonymous OpenAlex quota was used up. Every DOI below was resolved through Crossref, and the summaries follow each paper's own abstract. "Cites" are Crossref counts, which usually run below Scopus or Google Scholar.*

## Bottom line

| Claim (from the talks) | Verdict | Why |
|---|---|---|
| Poverty causes **stress, anxiety, depression**, and cash relieves them | **Robust** | Causal reviews (Ridley et al. 2020, *Science*) and RCTs (Haushofer & Shapiro 2016). Haushofer & Salicath (2023): the income–well-being link is "robust … in correlational and causal analyses". |
| Scarcity causes **tunneling / attentional focus** and **over-borrowing** | **Moderately supported** | de Bruijn & Antonides (2022) review: the literature "predominantly confirms" it, with methodological caveats. Shah et al. (2019) self-replication: the attention and borrowing results held up. |
| Scarcity **lowers cognitive function** (the "bandwidth tax", "14 IQ points") | **Weak / contested** | Bayesian meta-analysis (Szecsi et al. 2024): "moderate evidence **against** the existence of the effect"; if it exists, g = 0.09. US payday RCT shows no cognitive effect (Carvalho et al. 2016). Haushofer & Salicath (2023): "the evidence is relatively weak". Some field studies do find effects (Kaur et al. 2024; Ong et al. 2019). |
| Scarcity **raises impatience and risk aversion** | **Mixed / inconclusive** | de Bruijn & Antonides: "not conclusive". Carvalho et al.: present bias only over money. Bartoš et al. (2021): poverty priming raises impatience. Fehr et al. (2022): scarcity makes choices *more* rational. |
| **Financial-literacy training doesn't work** (Bregman's "201 studies") | **Contested; newer evidence disagrees** | Fernandes et al. (2014): it explains 0.1% of the variance in behaviour, with weaker effects for low-income groups. Kaiser et al. (2022), a meta-analysis of **76 RCTs** with 160,000+ people, finds **positive, economically meaningful** effects. |
| **Dauphin / MINCOME** cut hospitalisations by 8.5% | **Contested** | Forget (2011) is the original. Green (2022) finds pre-existing downward trends in Dauphin and argues the data don't support the claim. Forget (2022) replies that the 1974–75 data are contaminated by the early announcement. |
| **Unconditional cash** works: consumption, assets, no "temptation" spending, no reduction in work, local multiplier | **Robust** | Egger et al. (2022, *Econometrica*): multiplier 2.5, minimal inflation. Haushofer & Shapiro (2016, *QJE*). Evans & Popova (2017). Banerjee et al. (2017). |

**What this means overall.** The *policy* conclusion both speakers reach, that unconditional cash beats paternalistic programmes, rests on solid RCT evidence. The *psychological mechanism* Bregman puts at the centre, scarcity cutting IQ, is the weakest link. Cash appears to work mainly because it relaxes **capital and liquidity constraints** and reduces **stress**, not because it restores lost IQ points. In a paper or talk, rest the argument on the cash evidence and present the bandwidth story as one possible channel that is still contested.

---

## 1. The core scarcity papers (what the talks rest on)

| Paper | Cites | Finding |
|---|---|---|
| Shah, Mullainathan & Shafir (2012), "Some consequences of having too little", *Science* 338. [10.1126/science.1222426](https://doi.org/10.1126/science.1222426) | 1,167 | Lab games: scarcity leads to focus, over-borrowing and fatigue. |
| Mani, Mullainathan, Shafir & Zhao (2013), "Poverty impedes cognitive function", *Science* 341. [10.1126/science.1238041](https://doi.org/10.1126/science.1238041) | 2,185 | NJ mall priming study plus Tamil Nadu sugarcane farmers before and after harvest. |
| Shah, Shafir & Mullainathan (2015), "Scarcity frames value", *Psych. Science*. [10.1177/0956797614563958](https://doi.org/10.1177/0956797614563958) | 361 | Scarcity makes people *less* susceptible to context effects, closer to economic rationality. |
| Mullainathan & Shafir (2013), *Scarcity: Why Having Too Little Means So Much* (book) | n/a | The general statement of the theory. |

## 2. Direct critiques, replications and replies (in sequence)

1. **Wicherts & Scholten (2013)**, Comment, *Science*. [10.1126/science.1246680](https://doi.org/10.1126/science.1246680). Re-analysing the mall data with income as a continuous variable instead of a rich/poor split "fails to corroborate" the result. They attribute the interaction to **ceiling effects** from short, easy tests.
   ↳ **Mani et al. (2013) reply**. [10.1126/science.1246799](https://doi.org/10.1126/science.1246799). The interaction holds with continuous income, there are no ceiling effects, and the farmer result survives allowing for learning effects.
2. **Dang, Xiao & Dewitte (2015)**, *Frontiers in Psychology*. [10.3389/fpsyg.2015.01037](https://doi.org/10.3389/fpsyg.2015.01037). The outcome measures (IQ, Stroop) are far from daily life, and low motivation could explain the results.
3. **Carvalho, Meier & Wang (2016)**, *AER* 106(2). [10.1257/aer.20140481](https://doi.org/10.1257/aer.20140481) (369 cites). An RCT among low-income US households, randomised to answer before or after payday. **No difference in cognitive function**, risk-taking or decision quality. Present bias appeared only for money choices, not effort choices. *The most direct test of Mani et al.'s mechanism, and it comes up null.*
   ↳ **Mani, Mullainathan, Shafir & Zhao (2020)**, *J. Assoc. Consumer Research*. [10.1086/709885](https://doi.org/10.1086/709885). Reply: payday swings are routine and anticipated, and the research design matters.
4. **Camerer et al. (2018)**, Social Science Replication Project, *Nature Human Behaviour*. [10.1038/s41562-018-0399-z](https://doi.org/10.1038/s41562-018-0399-z) (1,177 cites). 13 of 21 *Science*/*Nature* studies replicated. Shah et al. (2012) **failed** on the cognitive-fatigue result.
   ↳ **Shah, Mullainathan & Shafir (2018)**, *NHB*. [10.1038/s41562-018-0405-5](https://doi.org/10.1038/s41562-018-0405-5), and **(2019) "An exercise in self-replication"**, *J. Econ. Psych.* [10.1016/j.joep.2018.12.001](https://doi.org/10.1016/j.joep.2018.12.001). High-powered re-runs of all their studies. Similar effects across forms of scarcity, attentional shifts and over-borrowing look **more robust**. They found **no evidence** that scarcity-induced focus causes cognitive fatigue.
5. **O'Donnell et al. (2021)**, "Empirical audit and review … psychological consequences of scarcity", *PNAS* 118(44). [10.1073/pnas.2103313118](https://doi.org/10.1073/pnas.2103313118). 20 replications drawn from papers citing the seminal work: "some strong successes and other undeniable failures". *Correction* published 2022: [10.1073/pnas.2217321119](https://doi.org/10.1073/pnas.2217321119).
   ↳ **Shah, Mullainathan & Shafir (2023)**, "A scarcity literature mischaracterized with an empirical audit", *PNAS*. [10.1073/pnas.2206054120](https://doi.org/10.1073/pnas.2206054120). At least 10 of the 20 studies were mis-selected, mis-analysed or unfaithful to the originals.
6. **Szecsi et al. (2024)**, Bayesian meta-analysis, *Collabra: Psychology*. [10.1525/collabra.122943](https://doi.org/10.1525/collabra.122943). 14 effect sizes from 10 studies: **moderate evidence against** the effect, not robust to the choice of prior. If real, it is small: g = 0.09 [−0.03, 0.21]. The authors conclude the "evidence … is extremely limited".

## 3. Reviews

- **Haushofer & Fehr (2014)**, "On the psychology of poverty", *Science* 344. [10.1126/science.1232491](https://doi.org/10.1126/science.1232491) (1,349 cites). Poverty leads to stress and negative affect, which lead to short-sighted, risk-averse choices, forming a possible feedback loop.
- **Ridley, Rao, Schilbach & Patel (2020)**, "Poverty, depression, and anxiety: Causal evidence and mechanisms", *Science* 370. [10.1126/science.aay0214](https://doi.org/10.1126/science.aay0214) (1,034 cites). The causation runs **both ways**. Cash support and low-cost therapy both help.
- **de Bruijn & Antonides (2022)**, "Poverty and economic decision making: a review of scarcity theory", *Theory and Decision* 92. [10.1007/s11238-021-09802-7](https://doi.org/10.1007/s11238-021-09802-7) (209 cites). It tests three propositions:
  - (1) focus and neglect lead to over-borrowing: **mostly confirmed**;
  - (2) trade-off thinking makes consumption more consistent: **mostly confirmed**;
  - (3) lower bandwidth leads to more discounting and risk aversion: **not conclusive**.

  The theory is "original, coherent, and parsimonious" but "does not fully accord with the data and lacks some precision".
- **Haushofer & Salicath (2023)**, "The psychology of poverty: Where do we stand?", *Social Philosophy & Policy*. [10.1017/s0265052523000419](https://doi.org/10.1017/s0265052523000419). The income–well-being link is **robust**. On scarcity and stress driving decisions: "**the evidence is relatively weak**". Psychological interventions are small in absolute terms but large per dollar, compared with cash.
- **Dean, Schilbach & Schofield (2018)**, "Poverty and cognitive function", in Barrett, Carter & Chavas (eds.), *The Economics of Poverty Traps*, U. Chicago Press. [10.7208/chicago/9780226574448.003.0002](https://doi.org/10.7208/chicago/9780226574448.003.0002). An economics-side review of the possible channels.

## 4. Newer field evidence (mostly from development economics)

| Paper | Design | Result | Supports bandwidth? |
|---|---|---|---|
| **Kaur, Mullainathan, Oh & Schilbach (2024)**, *QJE*. [10.1093/qje/qjae038](https://doi.org/10.1093/qje/qjae038) | RCT: Indian piece-rate workers paid *earlier* | Output **+7% (0.11 SD)**, fewer careless mistakes, concentrated among the most constrained workers. Rules out nutrition and gift-exchange explanations. | **Yes**, the strongest field support. |
| **Ong, Theseira & Ng (2019)**, *PNAS*. [10.1073/pnas.1810901116](https://doi.org/10.1073/pnas.1810901116) | Quasi-experiment: Singapore one-off debt relief | Better cognitive function, less anxiety, less present bias | **Yes**, but not randomised. |
| **Bartoš, Bauer, Chytilová & Levely (2021)**, *Economic Journal*. [10.1093/ej/ueab007](https://doi.org/10.1093/ej/ueab007) | Priming poverty worries among Ugandan farmers | More impatience. Eye-tracking-style monitoring suggests it is *not* due to careless decisions. | Partly: preferences shift, but not via inattention. |
| **Fehr, Fink & Jack (2022)**, *JPE*. [10.1086/720466](https://doi.org/10.1086/720466) | Zambian farmers, 5,842 trading decisions | Constraints reduce endowment-effect bias. **Not mediated by cognitive performance**: scarcity makes people *more* rational. | **No** |
| **Carvalho, Meier & Wang (2016)**, *AER* | US payday RCT | No cognitive effect | **No** |
| Lichand & Mani (2020), "Cognitive droughts", SSRN [10.2139/ssrn.3540149](https://doi.org/10.2139/ssrn.3540149) | Rainfall shocks among Brazilian farmers | *(abstract not retrievable; working paper)* | Unverified |

**Pattern.** Field studies with **real, large, ongoing financial worries** (debt, wage timing) tend to find effects. Lab **priming** studies and **routine payday** variation tend not to. The mechanism may be real but smaller and more context-dependent than the "14 IQ points" headline implies.

## 5. Other claims made in the talks

**Financial education (Bregman)**
- Fernandes, Lynch & Netemeyer (2014), *Management Science*. [10.1287/mnsc.2013.1849](https://doi.org/10.1287/mnsc.2013.1849) (1,634 cites). This is the "201 studies" meta-analysis. Interventions explain **0.1%** of the variance in financial behaviour, effects are weaker in low-income samples, and they decay within about 20 months.
- **Kaiser, Lusardi, Menkhoff & Urban (2022)**, *J. Financial Economics*. [10.1016/j.jfineco.2021.09.022](https://doi.org/10.1016/j.jfineco.2021.09.022) (444 cites). 76 **RCTs**, N > 160,000: positive causal effects on knowledge *and* behaviour, "economically meaningful", and robust to publication bias.

  → Bregman's "almost no effect" relies on the older, partly correlational meta-analysis. The newer RCT-only evidence finds modest positive effects.

**Dauphin / MINCOME (Bregman)**
- Forget (2011), *Canadian Public Policy* 37(3). [10.3138/cpp.37.3.283](https://doi.org/10.3138/cpp.37.3.283). Hospitalisations −8.5%, especially for accidents, injuries and mental health; more adolescents continued to grade 12.
- **Green (2022)**, *CPP*. [10.3138/cpp.2021-025](https://doi.org/10.3138/cpp.2021-025). Dauphin was already trending down before treatment, and with short windows the data "do not support" the health-cost claim.
- Forget (2022), reply. [10.3138/cpp.2022-017](https://doi.org/10.3138/cpp.2022-017). The 1974–75 data are biased by the early announcement, and she stands by the original finding.

**Cash transfers (Stewart)**
- **Egger, Haushofer, Miguel, Niehaus & Walker (2022)**, *Econometrica*. [10.3982/ecta17945](https://doi.org/10.3982/ecta17945). Kenya: about $1,000 to 10,500 households in 653 villages, a shock worth more than 15% of local GDP. Large spillovers to non-recipients, **minimal price inflation**, local multiplier **2.5**. This is the source of Stewart's "$2.50 per $1".
- **Haushofer & Shapiro (2016)**, *QJE*. [10.1093/qje/qjw025](https://doi.org/10.1093/qje/qjw025) (761 cites). GiveDirectly RCT:
  - consumption rose from \$158 to \$193 PPP a month, and psychological well-being improved substantially;
  - **no overall effect on cortisol**;
  - monthly payments improved food security more, while lump sums went more into durables.
- **Evans & Popova (2017)**, "Cash transfers and temptation goods", *EDCC*. [10.1086/689575](https://doi.org/10.1086/689575). A review: cash does not increase spending on alcohol or tobacco.
- **Banerjee, Hanna, Kreindler & Olken (2017)**, "Debunking the stereotype of the lazy welfare recipient", *WBRO*. [10.1093/wbro/lkx002](https://doi.org/10.1093/wbro/lkx002). Seven RCTs show no systematic reduction in work.

*(The abstracts for Evans & Popova and Banerjee et al. were not available through the APIs. Their one-line summaries reflect their well-known headline findings and should be checked against the PDFs.)*

---

## 6. Implications for the MBG paper

1. **Don't build the argument on "scarcity lowers IQ".** If we bring in the psychology of poverty, cite Ridley et al. (2020) and Haushofer & Salicath (2023) for stress and well-being (robust), and Kaur et al. (2024) for productivity. Present cognitive bandwidth as a contested channel, citing Szecsi et al. (2024) and Carvalho et al. (2016).
2. **Egger et al. (2022) gives a direct contrast for the CGE results.** A cash shock worth more than 15% of local GDP in Kenya produced *minimal* inflation. Our model finds that MBG under protection pushes food CPI up 5.74pp. The difference makes sense: in-kind food procurement concentrates demand on one supply-constrained sector, while cash spreads it across goods. This supports adding a **cash-equivalent scenario**.
3. **Haushofer & Shapiro's monthly-versus-lump-sum result** (monthly payments improve food security more) is relevant to whether MBG's daily in-kind delivery has a food-security advantage over lump-sum cash.

## Method and reproducibility

- Search: Crossref `query.bibliographic` over about 30 queries covering meta-analysis, review, replication, comment and reply, payday, field evidence, and the other claims in the talks. Abstracts came from Crossref, then Europe PMC, then Semantic Scholar.
- One gap remains: **Scopus and OpenAlex were not queried.** To cross-check with them, add a `SCOPUS_API_KEY` or `OPENALEX_API_KEY` to the environment and re-run `poverty/lit/cr.py` / `abs.py`; this will also give citation counts that match Scopus.
- Raw abstracts are in `poverty/lit/abstracts_*.json`.
