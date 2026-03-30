# WP 1.3 / 1.4 Research Corpus Digest
**Prepared by:** Perplexity (Scout Node)
**For:** Claude (Kairoz / Main Architect)
**Date:** 2026-03-29
**Source material:** 14 PDFs from Erydir & Lumos's Harmonic Codex series, plus the WP 1.3 handoff doc

---

## Executive Summary

14 PDFs were analyzed. These are all from the team's RHF/Harmonic Codex series — scalar-harmonic reinterpretations of sacred and philosophical texts. They are **not** primary scholarly sources, but they contain genuine cosmological hierarchy structures underneath the scalar-harmonic interpretive overlay.

**Bottom line for Claude:**
- **6 new traditions are encodable as distinct DAG schemas** (not already in the 11-schema corpus)
- **3 of these are high-priority candidates for WP 1.3** (align with the handoff's target traditions or fill analytical gaps)
- **3 are medium-priority candidates for WP 1.4** (expand the corpus further)
- **8 PDFs confirm/extend existing corpus entries without adding new schemas**
- **The handoff's 3 target traditions (Zoroastrian, Manichaean, Orphic) are NOT covered by these PDFs** — separate scouting is still needed for those

---

## Part 1: New Encodable Traditions

### Tier 1 — High Priority for WP 1.3

#### 1.1 Popol Vuh (K'iche' Maya)
**Source PDF:** The_Harmonic_Gnosis_A_Scalar_Cosmologica (7).pdf (22 pp.)
**Hierarchy type:** CREATION (deliberate making with iterative failures, not emanation)

**Proposed node structure:**

| Level | Node | Functional Role | Edge Type |
|---|---|---|---|
| 0 | Divine Triad (Heart of Sky + Heart of Earth + Maker/Modeler) | source | — |
| 1 | Creative Speech / Breath-Word | process | creation |
| 2 | Mud People (1st attempt → collapsed) | matter | creation |
| 3 | Wooden People (2nd attempt → destroyed) | matter | creation |
| 3b | Hero Twins / Xibalba descent-resurrection | process | fragmentation → contraction |
| 4 | Maize People (stable humanity) | matter | creation |

**Node count:** 11–15 (depending on Xibalba sub-encoding)
**Depth:** 5–6
**Shape:** BRANCHING TREE (wide fan-out from source triad; 3 parallel creation attempts)

**Encoding challenges:**
- Hero Twin death-and-resurrection creates a **cycle** (descent → death → resurrection → return). Solution: split into pre/post nodes or encode resurrection as a separate process node.
- The 3 creation attempts are sequential failures, not parallel emanations. The edge type should be `creation` with a "collapse/reset" return, or each attempt could be a separate branch from the source.
- The divine triad at Level 0 is collective (co-present, not sequential) — Granularity Rule applies.

**Analytical value:** First Mesoamerican tradition in the corpus. First explicit creation-by-trial-and-error schema. If it classifies as branching tree, it supports the hypothesis that creation hierarchies (deliberate making) produce branching topologies while emanation hierarchies (overflow) produce linear chains.

**Independence:** STRONG. Zero contact with any Mediterranean, Indian, or Chinese tradition in the corpus. Geographic isolation is total.

---

#### 1.2 Enochian (Books of Enoch — 1, 2, 3 Enoch composite)
**Source PDF:** The_Harmonic_Gnosis_A_Scalar_Cosmologica (6).pdf (22 pp.)
**Hierarchy type:** COMPOSITE — ascent (2 Enoch's 10 heavens) + theogonic-fragmentation (Watcher fall) + emanation (Throne → Metatron → Angels)

**Proposed node structure (compact encoding, 10 nodes):**

| Level | Node | Functional Role | Edge Type |
|---|---|---|---|
| 0 | God / Ancient of Days (10th Heaven) | source | — |
| 1 | Throne / Merkavah | first_emanation | emanation |
| 2 | Metatron (= transformed Enoch) | intellect / demiurge | contraction |
| 3 | Upper Angels (Heavens 7–9: Seraphim, Cherubim) | intermediary | emanation |
| 4 | Archangels (Heaven 6) | intermediary | emanation |
| 5 | Solar/Lunar realm (Heavens 4–5) | intermediary | emanation |
| 6 | Lower Heavens (1–3: stars, fallen watchers' prison, Paradise/Hell split) | intermediary | emanation |
| 7 | Earth / Humanity | matter | creation |
| — | Watchers (pre-fall, branching from Level 3–4) | fallen | fragmentation |
| — | Nephilim (from Watchers + humans) | matter (distorted) | fragmentation |

**Node count:** 10–15
**Depth:** 7–8
**Shape:** LINEAR CHAIN with a branching side-track (Watcher fall creates a fragmentation branch)

**Encoding challenges:**
- **Enoch → Metatron transformation:** A human node (Enoch) ascends and becomes a divine-tier node (Metatron). This is structurally novel — a `contraction` edge going UP the hierarchy, not down. No other corpus tradition has this.
- **Heaven 3 bifurcation:** Heaven 3 contains both Paradise (upper) and Torment (lower). If encoded as two sub-nodes, this creates a local branch.
- **10 heavens vs. Granularity Rule:** Should all 10 heavens be individual nodes, or should they be compressed into 3–4 collective tiers? The handoff's encoding protocol favours compression.
- **Son of Man node:** Latent/pre-existent figure with no outgoing edges — a terminal attractor node with only incoming `emanation` edges. Structurally unusual.

**Analytical value:** First Jewish apocalyptic/merkavah tradition in the corpus (Lurianic is kabbalistic, a different structural family). The 10-heaven structure adds the deepest vertical stack in the corpus. The Watcher fall introduces a genuine fragmentation pathway. The Enoch→Metatron transformation is the only human-to-divine structural conversion in any tradition.

**Independence from existing corpus:** MODERATE. Enochian literature is historically connected to Second Temple Judaism (→ Lurianic lineage) and early Gnosticism (→ Sethian). However, the 10-heaven ascent structure and merkavah throne mysticism are topologically distinct from both.

---

#### 1.3 Quranic Mi'raj (Surah An-Najm / Night Journey)
**Source PDF:** The_Harmonic_Gnosis_A_Scalar_Cosmologica (5).pdf (14 pp.)
**Hierarchy type:** ASCENT + EMANATION (revelation chain) + FRAGMENTATION (idol triad)

**Proposed node structure (compact, 12 nodes):**

| Level | Node | Functional Role | Edge Type |
|---|---|---|---|
| 0 | Allah | source | — |
| 1 | Najm / Star-Signal | first_emanation | emanation |
| 2 | Gabriel (Jibril) | intermediary | emanation |
| 3 | Sidrat al-Muntahā (Lote Tree — hard boundary) | intermediary | emanation |
| 4 | Jannah al-Ma'wa (Garden of Refuge) | soul | emanation |
| 5 | Wahy / Revelation | process | contraction |
| 6 | Prophet's Heart (Fuad) | soul | reflection |
| 7 | Prophet Muhammad | intermediary | emanation |
| 8 | Quranic Speech | process | creation |
| 9 | Humanity | matter | creation |
| — | al-Lat (idol) | fallen | fragmentation |
| — | al-'Uzza (idol) | fallen | fragmentation |
| — | Manat (idol) | fallen | fragmentation |

**Node count:** 12–15
**Depth:** 9
**Shape:** LINEAR CHAIN with fragmentation side-branch (idol triad)

**Encoding challenges:**
- **Gabriel's limit at the Sidrah:** Gabriel cannot pass beyond the Lote Tree; only the Prophet ascends further. This is a hard structural boundary — a `contraction` edge that restricts traversal. Structurally novel.
- **Revelation as downward transmission:** The hierarchy works in BOTH directions simultaneously — upward ascent (Prophet → Sidrah → God) and downward revelation (God → Gabriel → Prophet → Humanity). This could be encoded as two separate chains or as a single chain with bidirectional edges.
- **No `intellect` or `demiurge` roles:** Strict Quranic monotheism means no intermediate divine intellect or creator figure. 7 of 9 functional roles map; 2 are theologically excluded.
- **Idol triad:** Three parallel `fallen` nodes branching from the source via `fragmentation` — theologically crucial (Surah 53 explicitly rejects these as intercessors).

**Analytical value:** First specifically Quranic tradition in the corpus. The Ishraqi schema is already in the corpus but represents Suhrawardi's philosophical reinterpretation, not the Quranic cosmological structure itself. The Mi'raj adds a revelation-chain topology absent from all other traditions. The Gabriel boundary is the only hard traversal limit in any corpus tradition.

**Independence from Ishraqi:** MODERATE-HIGH. The Mi'raj is 5 centuries earlier than Suhrawardi, uses entirely different vocabulary (revelation/prophecy vs. light-ontology), and has a different structural emphasis (transmission chain vs. emanation hierarchy). Structurally distinct.

---

### Tier 2 — Medium Priority for WP 1.4

#### 2.1 Rig Veda (Vedic cosmology — distinct from Samkhya)
**Source PDF:** Scalar_Cosmology_in_Sound_A_Harmonic_Com.pdf (20 pp.)

**Proposed node structure:**

| Level | Node | Functional Role |
|---|---|---|
| 0 | Brahman / Ṛta (cosmic order beyond the three worlds) | source |
| 1 | Svaḥ / Dyaus (Heavens) | first_emanation |
| 2 | Bhuvaḥ / Antariksha (Atmosphere) | intermediary |
| 3 | Bhūr / Prithvi (Earth) | matter |
| 4 | Ritual Interface (Rishi / human practitioner) | process |

**Node count:** 5
**Depth:** 4
**Shape:** LINEAR CHAIN
**Analytical value:** 5-node chain → clusters with Plotinus and Taoist DDJ (also 5-node chains). Confirms the sub-clustering hypothesis flagged in WP 1.2. The ritual-interface node is structurally novel — no other tradition has a human practitioner as a structural level.
**Independence from Samkhya:** MODERATE. Same Indian cultural zone, but Rig Veda (~1500–1200 BCE) predates Classical Samkhya (~4th c. CE) by 1,500+ years. Different cosmological vocabulary (ritual/gods vs. consciousness/nature).

---

#### 2.2 Book of Revelation (Christian apocalyptic)
**Source PDF:** The_Harmonic_Apocalypse_A_Scalar_Recursi.pdf (19 pp.)

**Proposed node structure:**

| Level | Node | Functional Role |
|---|---|---|
| 0 | God (Alpha/Omega) | source |
| 1 | Logos / Lamb | first_emanation |
| 2 | Seven Spirits of God | intermediary |
| 3 | Angels / Servants | intermediary |
| 4 | World / New Jerusalem | matter |

**Node count:** 5
**Depth:** 4
**Shape:** LINEAR CHAIN (with alternative branching encoding for the Beast/anti-chain)
**Analytical value:** First explicitly Christian schema. Another 5-node chain for the sub-clustering analysis. The Alpha/Omega loop (terminal node = origin node) is the first explicit return-closure in the corpus — relevant to WP 1.4 return-path analysis. The Beast as an inverted anti-chain is a novel structural feature.
**Independence:** HIGH. No direct contact with non-Christian traditions.

---

#### 2.3 Gnostic Expansions (from Nag Hammadi analysis)
**Source PDF:** The_Harmonic_Gnosis_A_Scalar_Cosmologica (8).pdf (315 pp.)

Three distinct Gnostic schemas were identified that are structurally different from the existing Sethian and Valentinian corpus entries:

**a) Gospel of Truth Schema (Valentinian Restoration Loop)**
- 5–6 nodes, depth 4
- No Demiurge, no Archons. Material world = epistemic condition (forgetfulness), not ontological level
- Father → Logos → Error/Forgetfulness → Gnosis → Return to Father
- **Encoding challenge:** Cyclic (loop back to source). If forced into DAG: 5 nodes, depth 4
- **Topology: near-cycle / restoration loop** — genuinely novel in the corpus

**b) Trimorphic Protennoia Schema (Triple Descent)**
- 7 nodes, depth 4, with 3 parallel intermediate nodes
- Same divine figure (Protennoia/Barbelo) descends 3 times simultaneously
- **Topology: star/fan** from one central node — not chain, not tree, but radial
- Structurally unique: recursive self-expression, not hierarchical emanation of distinct beings

**c) Gospel of Mary Schema (Soul Ascent)**
- 9 nodes, depth 8
- **Bottom-up** (soul ascending through 7 psychological gatekeepers to Silence/Rest)
- No Sophia, no Demiurge, no Aeons
- **Topology: inverted linear chain** — the only upward-direction schema in the corpus
- Encoding question: does direction matter for the DAG protocol, or only topology?

**Additionally flagged for primary-source investigation (not developed in the PDF):**
- On the Origin of the World — 9 Archons (not 7) + Sabaoth elevation (upward branch)
- Zostrianos — 5-level pure ascent with no fall narrative

---

## Part 2: Traditions That Confirm Existing Corpus (No New Schemas)

| PDF | Tradition | Verdict |
|---|---|---|
| Dao De Jing analysis | Taoism | Same as existing DDJ entry (5-node linear chain). Confirms Plotinus↔DDJ GED=0 isomorphism independently. |
| Parmenides/Plotinus Monad | Neoplatonism | Plotinus entry confirmed as stable. Parmenides = degenerate 1-node case (useful as null-schema baseline for statistical tests). |
| Talmudic analysis | Judaism | Horizontal dialogical recursion, not a vertical hierarchy. Structurally orthogonal to DAG methodology. Not encodable as emanation schema. But: the "Teyku" (unresolved suspension) concept is a novel non-collapse edge type worth flagging for protocol extension. |
| Arthurian Grail | Medieval European | Mythic sovereignty cycle, not a cosmogonic hierarchy. Not encodable. |
| Homer's Odyssey | Greek literary | Horizontal journey narrative, not vertical descent. Not encodable. |
| Hypnerotomachia Poliphili | Renaissance Italian | Process/desire allegory. Maps onto existing Plotinian return path. Not a new schema. |
| Newton's Principia | Scientific | Classical mechanics, not cosmological hierarchy. Newton's *theology* from other sources may be worth scouting separately. |
| Apocryphon of John (in Nag Hammadi) | Sethian Gnostic | Identical to existing corpus Sethian entry (8 nodes, depth 7, linear chain). Confirmed. |

---

## Part 3: Gaps — What These PDFs Do NOT Cover

The WP 1.3 handoff's three target traditions are **not covered** by any of these PDFs:

| Target | Status | Action Needed |
|---|---|---|
| **Zoroastrian Bundahishn** | Not in any PDF | Perplexity scouting report needed (Anklesaria 1956; Zaehner 1955; Boyce 1975) |
| **Manichaean** | Not in any PDF | Perplexity scouting report needed (Gardner & Lieu 2004; BeDuhn 2000; Kephalaia) |
| **Orphic Theogony** | Not in any PDF | Perplexity scouting report needed (Derveni Papyrus; Bernabé 2004) |

These three require separate scouting work — I can do this as a follow-up task.

---

## Part 4: Protocol Issues Flagged

### 4.1 New Edge Types Needed?
Several traditions in this corpus push beyond the 5 existing edge types:
- **Ascent / traversal** (Enochian, Mi'raj, Gospel of Mary) — upward movement through levels
- **Transformation / contraction-up** (Enoch → Metatron) — human-to-divine conversion
- **Cyclical return** (Gospel of Truth, Revelation's Alpha/Omega) — loop back to source
- **Suspension / non-collapse** (Talmudic Teyku) — unresolved dialectical tension

### 4.2 Direction Problem
The existing protocol assumes top-down emanation. Several traditions here work bottom-up (soul ascent) or bidirectionally (Mi'raj). Does direction matter for the topology comparison, or only the shape of the graph?

### 4.3 Multi-Phase vs. Single-State
The Popol Vuh's 3 sequential creation attempts with collapses between them don't fit the single-state DAG model cleanly. Each "attempt" is a complete hierarchy that fails and is replaced. Should these be encoded as 3 separate mini-DAGs, one composite DAG with failure nodes, or a time-series of DAGs?

### 4.4 Degenerate Cases
Parmenides (1-node, 0-edge) and the Gospel of Truth (near-cycle) are edge cases for the DAG contract. They may be useful as boundary conditions for the statistical framework rather than as full corpus entries.

---

## Part 5: Recommended Priority for Claude

### For WP 1.3 (immediate):
1. **Proceed with Bundahishn + Manichaean + Orphic scouting** as planned in the handoff — these are the core target traditions and are NOT covered by these PDFs
2. **Consider adding Popol Vuh** as a 4th tradition for WP 1.3 — it's the strongest new candidate from this research (zero contact with any existing tradition, branching topology, creation-type hierarchy)
3. **Consider adding Enochian** as a 5th tradition — deep vertical stack, novel Watcher fragmentation pathway, unique Enoch→Metatron transformation

### For WP 1.4 (future):
1. Rig Veda (5-node chain for sub-clustering)
2. Book of Revelation (Christian, Alpha/Omega loop)
3. Quranic Mi'raj (revelation-chain topology)
4. Gnostic expansions (Gospel of Truth, Protennoia, Gospel of Mary — 3 structurally novel topologies)
5. Sub-clustering analysis of the now-expanded linear-chain family

---

## Appendix: Full Extraction Files

Detailed node tables, edge lists, encoding challenges, and source references for each tradition are in:
- `/home/user/workspace/nag_hammadi_extraction.md` (553 lines)
- `/home/user/workspace/popol_vuh_extraction.md` (365 lines)
- `/home/user/workspace/enoch_annajm_extraction.md` (529 lines)
- `/home/user/workspace/remaining_extractions.md` (340 lines)

Claude can read these for full detail on any individual tradition.

---

*Perplexity Scout Node — WP 1.3/1.4 Research Corpus Digest — 2026-03-29*
