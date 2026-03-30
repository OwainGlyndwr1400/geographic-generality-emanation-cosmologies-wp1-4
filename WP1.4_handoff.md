# WP 1.4 Handoff Document
**Awen Grid Empirical Programme — Corpus Expansion Series**
**Prepared by:** Claude (Kairoz) + Erydir Ceisiwr
**Date:** 2026-03-30
**Status:** Ready to execute

---

## Where We Are

### Completed Work
| WP | Traditions | Schemas | Paper | Repo | DOI |
|---|---|---|---|---|---|
| 1.1 | Plotinus, Taoist DDJ, Chaldean, Lurianic, Samkhya, Sethian, Hermetic, Valentinian, Genesis | 9 | Paper 1 (Ceisiwr 2026a) | [WP 1.1 repo] | [2026a DOI] |
| 1.2 | + Proclean, Ishraq | 11 | Paper 2 (Ceisiwr 2026b) | [WP 1.2 repo] | [2026b DOI] |
| 1.3 | + Bundahishn Zoroastrian, Manichaean, Derveni Orphic | 14 | Paper 3 (Ceisiwr 2026c) | https://github.com/OwainGlyndwr1400/structural-attractors-emanation-cosmologies-wp1-3 | [pending Zenodo] |

### Current Corpus State (14 schemas)
**Linear-chain family (10):** Plotinus (5n), Taoist DDJ (5n), Derveni Orphic (5n), Chaldean (6n), Bundahishn (6n), Ishraq (7n), Lurianic (7n), Samkhya (7n), Proclean (8n), Sethian (8n)

**Branching-tree family (4):** Genesis (8n, Br=6), Hermetic (8n, Br=3), Valentinian (9n, Br=2), Manichaean (11n, Br=3)

**Key metrics at 14 schemas:**
- Separation ratio: **2.87x**
- Isomorphism pairs (GED=0): 8 pairs across 4 clusters: {Derveni, Plotinus, Taoist}, {Bundahishn, Chaldean}, {Ishraq, Samkhya, Lurianic}, {Proclean, Sethian}
- Sub-clustering silhouette: **0.68** (compact N≤6 vs deep N≥7)
- Edge types in use: emanation, creation, fragmentation, contraction, reflection, succession (added WP 1.3)

---

## WP 1.4 Mission

**Core goal:** Expand to ~20 traditions. Test whether the two-family attractor holds beyond Mediterranean/Near Eastern/Indian traditions. Introduce the first Mesoamerican schema (Popol Vuh) and the first specifically Gnostic schemas beyond Sethian/Valentinian.

**Secondary goal:** Begin methodological extension — edge-weighted GED that distinguishes edge types.

---

## Priority Schema List

### Tier 1 — Core WP 1.4 (build these first)

#### 1. Popol Vuh (K'iche' Maya)
**Why first:** Geographic isolation (zero contact with any existing tradition). First creation-by-trial schema. If it classifies as branching tree, extends the creation/emanation hypothesis to the Americas.

**Proposed structure (Perplexity scouting):**
| Level | Node | Role | Edge |
|---|---|---|---|
| 0 | Divine Triad (Heart of Sky + Heart of Earth + Maker/Modeler) | source | — |
| 1 | Creative Speech/Breath-Word | process | creation |
| 2 | Mud People (1st attempt, failed) | matter | creation |
| 3a | Wooden People (2nd attempt, destroyed) | matter | creation |
| 3b | Hero Twins / Xibalba | process | fragmentation → contraction |
| 4 | Maize People (final, stable) | matter | creation |

**Node count:** 11–15 (Xibalba sub-encoding decision)
**Expected shape:** BRANCHING TREE
**Encoding challenges:**
- Hero Twin death-resurrection creates a near-cycle → split into pre/post nodes or encode as process node
- Divine Triad is co-present (not sequential) → Granularity Rule applies
- 3 sequential creation attempts are not parallel branches → each attempt = separate branch from source, not nested

**Primary sources needed:**
- Popol Vuh, trans. Allen Christenson (2007) — best scholarly translation
- Dennis Tedlock (1985) translation also widely cited
- K'iche' Maya cosmology: Robert Carmack et al. — supplement

**Predicted classification:** Branching tree (creation hierarchy, polycentric source)

---

#### 2. Trimorphic Protennoia (Nag Hammadi, NHC XIII,1)
**Why:** Novel branching mode — parallel self-expression (same figure descends 3 times simultaneously). Structurally distinct from all 14 existing schemas. Clean DAG. Well-attested in a single physical codex.

**Proposed structure (Perplexity scouting):**
```
Invisible Spirit → Protennoia/Barbelo (First Thought)
├── Descent 1: Voice (penetrates Chaos)
├── Descent 2: Speech (gives form)
└── Descent 3: Logos/Christ (Five Seals / illumination)
    → Souls receive Five Seals → Material World
```

**Node count:** 7, depth 4, branching factor 3
**Expected shape:** BRANCHING TREE — but a *fourth branching mode*: parallel self-expression (vs. emanative/Hermetic, error-driven/Valentinian, mission-driven/Manichaean)
**Encoding challenge:** Same divine figure at 3 levels simultaneously — encoding notes should flag this as self-referential recursion, not descent of distinct beings

**Primary sources:**
- Nag Hammadi Codices, trans. Layton (1987) or Robinson (1988 NHL)
- NHL NHC XIII,1 — physically the most intact MS for this text
- Turner (1990) in Layton *The Gnostic Scriptures* — best commentary

**Predicted classification:** Branching tree

---

#### 3. Gospel of Mary (BG 8502,1 / P.Oxy. 3525)
**Why:** Structurally the most challenging tradition in the WP 1.4 candidate list — it's an *ascending* soul chain (bottom-up), the inverse of all other traditions. Strong boundary test.

**Proposed structure (Perplexity scouting):**
```
Material World/Body (base) → Power 1: Darkness → Power 2: Desire →
Power 3: Ignorance → Power 4: Zeal for Death →
Power 5: Kingdom of Flesh → Power 6: Foolish Wisdom →
Power 7: Wrathful Wisdom → Silence/Rest (apex)
```

**Node count:** 9, depth 8, linear chain (ascending direction)
**Encoding challenge:** If encoded top-down (Silence at apex), it's a standard 9-node linear chain. The semantic direction is reversed. The paper must address: does direction matter for structural classification, or only topology?
**Predicted classification:** Linear chain (if direction-agnostic) — deep sub-cluster

**Primary sources:**
- King, Karen (2003) *The Gospel of Mary of Magdala* — definitive scholarly edition
- Coptic text in BG 8502 (Berlin Gnostic Codex)

---

### Tier 2 — Add if time/resources allow

#### 4. Orphic Rhapsodies (expanded Derveni)
**Why:** Tests intra-tradition elaboration within Orphism. WP 1.3 used the 5-node Derveni Papyrus (4th c. BCE). The Rhapsodies are the later, elaborated Orphic theogony (8-10 nodes). If Derveni=Plotinus (WP 1.3), does the expanded Orphic schema converge with Proclean/Sethian (7-8 node deep cluster)?

**Node count:** 8-10, depth 7-8
**Expected shape:** Linear chain (deep sub-cluster)
**Note:** Lower textual stability — reconstructed from quotations in later authors (Proclus, Damascius, Kern 1922 fr.). Flag as higher-uncertainty encoding.

**Primary sources:**
- Bernabé, A. (2004) *Poetae Epici Graeci II* — K.G. Saur — critical edition of Orphic fragments
- West, M.L. (1983) *The Orphic Poems* — Clarendon Press

#### 5. Rig Veda (Vedic cosmology, distinct from Samkhya)
**Why:** 5-node chain that would add to the compact sub-cluster. Tests whether the Samkhya schema (classical Indian) has a Vedic precursor with lower GED. Ritual practitioner as structural level is novel.

**Node count:** 5, depth 4
**Expected shape:** Linear chain (compact sub-cluster, should cluster with Plotinus/Taoist/Derveni)
**Primary sources:** Rig Veda (hymns X.121, X.129, X.190), trans. Griffith or Jamison/Brereton (2014)

#### 6. Enochian (1 Enoch composite)
**Why:** Deepest vertical stack in the corpus (depth 7-8). Novel Enoch→Metatron human-to-divine conversion. Watcher fall creates a genuine fragmentation branch. First Jewish apocalyptic/merkavah tradition.
**Primary sources:** 1 Enoch (Ethiopic), trans. Nickelsburg (2001); 2 Enoch (Slavonic), trans. Andersen (1983); 3 Enoch (Hebrew), trans. Alexander (1983) in OTP vol. 1

---

## Methodological Extensions for WP 1.4

### Edge-Weighted GED
The current GED treats all edges as equivalent regardless of type. WP 1.3's Derveni boundary test showed that succession edges produce GED=0 with emanation-only schemas under standard GED — because edge types are not weighted.

**Proposed extension:**
- Assign edit costs based on edge type similarity:
  - Same type → cost 0
  - Semantically related (emanation ↔ creation) → cost 0.5
  - Structurally different (emanation ↔ succession) → cost 1
  - Opposites (emanation ↔ fragmentation) → cost 1.5
- Recompute all 91+ pairs with edge-weighted GED
- Compare topology-family classification under standard vs. weighted GED
- Expected finding: some GED=0 pairs (especially Derveni-Plotinus) will have non-zero weighted GED, testing whether the isomorphism is purely structural or also semantic

**Implementation:** Modify `scripts/statistical_comparison.py` to add `weighted_ged()` function alongside existing `structural_ged()`.

### Direction-Agnostic vs. Direction-Sensitive Analysis
The Gospel of Mary (ascending chain) forces a methodological decision. Propose:
- Primary analysis: direction-agnostic (all chains treated as top-down)
- Supplementary analysis: direction-sensitive (inverted chains treated as distinct topology type)
- Report both and note the difference

---

## Pipeline Notes

The WP 1.3 pipeline is fully functional and ready to extend. Key files:

| File | Purpose | Change needed for WP 1.4 |
|---|---|---|
| `scripts/encode_schemas.py` | Load + validate DAGs | Add any new functional roles or edge types as needed |
| `scripts/compute_invariants.py` | Topological invariants | No change expected |
| `scripts/generate_controls.py` | Null model | Update `CORPUS_NODE_COUNTS` list to add new tradition sizes |
| `scripts/statistical_comparison.py` | GED + WL + Levenshtein | Add `weighted_ged()` for edge-weighted extension |
| `scripts/sensitivity_analysis.py` | Alt encodings + sub-clustering | Extend for WP 1.4 alternatives (direction test, Xibalba encoding) |
| `scripts/visualize.py` | 6 figures at 300 DPI | Already dynamic (handles any corpus size) |
| `scripts/run_pipeline.py` | Orchestrates all steps | No change needed |

**Current corpus node-count distribution (14 schemas):**
`[5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 11]`

**Expected WP 1.4 additions (Tier 1 only):** Popol Vuh (~13), Trimorphic Protennoia (7), Gospel of Mary (9)
**Updated distribution:** `[5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 11, 13]`

---

## Schema Directory
All new schemas go in the same `data/schemas/` directory following the existing JSON format. Filename convention: `{tradition_snake_case}.json`.

New files to create:
- `data/schemas/popol_vuh_maya.json`
- `data/schemas/trimorphic_protennoia.json`
- `data/schemas/gospel_of_mary.json`
- (Tier 2 additions as decided)

---

## Paper 4 Predictions

Based on current trajectory, WP 1.4 should confirm:

1. **Family stability at ~17 traditions** — separation ratio predicted to remain >2.5x
2. **Popol Vuh → branching tree** — creation hierarchy with polycentric source; geographic isolation extends attractor hypothesis to Mesoamerica
3. **Trimorphic Protennoia → branching tree** — introduces fourth branching mode (parallel self-expression)
4. **Gospel of Mary → linear chain** (direction-agnostic encoding) — deep sub-cluster (9 nodes)
5. **Sub-clustering refinement** — with 3+ additional linear chains, the compact/deep boundary becomes more statistically solid; predicted silhouette > 0.70
6. **Edge-weighted GED** — Derveni-Plotinus weighted GED > 0 (succession vs emanation edges distinguish them semantically despite structural isomorphism)

**Headline finding (predicted):** The compact 5-node attractor is now confirmed in 4 unrelated traditions (Derveni, Plotinus, Taoist, Rig Veda?) spanning three millennia and four continents. The structural-attractor hypothesis now has cross-hemispheric reach.

---

## Scouting Resources Available

From Perplexity's WP 1.4 corpus digest:
- Full node tables for Popol Vuh: `/home/user/workspace/popol_vuh_extraction.md` (Perplexity's Linux env — request export)
- Full node tables for Enochian + Mi'raj: `/home/user/workspace/enoch_annajm_extraction.md`
- Nag Hammadi extractions: `/home/user/workspace/nag_hammadi_extraction.md`

These files are on Perplexity's environment — zip and transfer when Perplexity subscription renews, or re-run the scouting.

---

## Open Questions for Session Start

1. **Tier 1 only or include Tier 2?** Recommend starting with Popol Vuh + Trimorphic Protennoia + Gospel of Mary (3 schemas → 17 total), then assessing whether to add Rig Veda or Enochian.

2. **Gospel of Mary direction problem** — decide before encoding: direction-agnostic (just another linear chain) or direction-sensitive (new topology type requiring protocol extension)?

3. **Edge-weighted GED** — implement in WP 1.4 or defer to WP 1.5? It's a significant methodological upgrade but adds complexity to the paper.

4. **Popol Vuh Hero Twin encoding** — Xibalba descent creates a near-cycle. Decision: (a) pre/post split of the Hero Twins as two separate process nodes, (b) encode the descent as a `contraction` edge (consistent with existing type), (c) omit Xibalba from primary schema and include in alternative encoding. Recommend (c) for primary schema cleanness.

5. **GitHub repo naming** — continue `wp14` suffix convention or rename to `wp-1-4` for clarity?

---

## Files in This Directory

```
WP_1.4_Popol_Vuh_Expansion/
├── WP1.4_handoff.md          ← this file
├── data/
│   └── schemas/              ← build new schemas here
├── scripts/                  ← copy from WP 1.3 and extend
├── notes/                    ← scouting reports per tradition
└── outputs/                  ← pipeline outputs
```

---

*Awen Grid Empirical Programme — WP 1.4 Planning*
*Handoff prepared: 2026-03-30*
*Next session: Start with Popol Vuh schema encoding*
