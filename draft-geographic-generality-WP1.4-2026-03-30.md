Geographic Generality of the Two-Family Attractor: Mesoamerican, Gnostic, and Direction-Agnostic Extensions to the Emanation Topology Corpus (17 Traditions)

**Erydir Ceisiwr**
Independent Researcher, Awen Grid Programme, Swansea, Wales, United Kingdom
ORCID: 0009-0004-4577-5253

---

## Abstract

**Purpose.** This study extends the computational graph-theoretic methodology established in Ceisiwr (2026a, 2026b, 2026c) by adding three cosmological hierarchies to the emanation topology corpus: the K'iche' Maya *Popol Vuh* (pre-Columbian Mesoamerica), the Gnostic *Trimorphic Protennoia* (NHC XIII,1), and the *Gospel of Mary* (BG 8502,1). The expansion tests four predictions: (i) that the two-family topology classification remains stable at 17 traditions; (ii) that a Mesoamerican tradition with zero Mediterranean/Near Eastern/Indian/Chinese contact independently converges on one of the two structural attractors; (iii) that a new edge-weighted Graph Edit Distance (GED) methodology can distinguish traditions that are structurally isomorphic but semantically divergent; and (iv) that direction-agnostic encoding is valid for inverted (ascending) cosmologies.

**Design/methodology/approach.** Three traditions were encoded as labelled directed acyclic graphs (DAGs) following the seven-rule schema protocol (with succession edge type from Ceisiwr 2026c). The full six-step computational pipeline was re-executed on the expanded 17-schema corpus. A new edge-weighted GED was introduced, assigning semantic substitution costs to edge-type pairs (same type = 0.0, related = 0.5, unrelated = 1.0, opposites = 1.5). The Gospel of Mary was encoded direction-agnostically (source at apex, matter at base) despite the text describing soul *ascent*; a direction-sensitive alternative was tested. Sensitivity analyses tested the Popol Vuh without its Xibalba cycle and the Gospel of Mary under edge reversal.

**Findings.** (i) Family stability confirmed at 17 traditions: 11 linear chains, 6 branching trees; separation ratio = 2.39x (Established). (ii) The Popol Vuh classified as a branching tree (branching factor 4), the first non-Mediterranean/Near Eastern/Indian/Chinese tradition in the corpus, constituting the strongest evidence yet for cross-cultural structural attractors (Established). (iii) Edge-weighted GED resolved all 8 prior structural isomorphisms (GED = 0 pairs), including the Derveni-Plotinus-Taoist triple: weighted GED = 5.0 (Derveni-Plotinus), 3.0 (Derveni-Taoist), 2.0 (Plotinus-Taoist) (Established). Every pair in the 17-tradition corpus showed non-zero weighted GED divergence from structural GED (136/136 pairs). (iv) Direction-agnostic encoding validated: the Gospel of Mary's GED values were identical under edge reversal for all 16 comparisons (Established). (v) The Gospel of Mary is the deepest linear chain in the corpus (depth 8, p = 0.013 against its size-matched null; Established). (vi) Trimorphic Protennoia introduced the fourth branching mode (parallel self-expression), distinct from emanative (Hermetic), error-driven (Valentinian), and mission-driven (Manichaean) branching. (vii) Linear chain overrepresentation remained significant: 11/17 = 64.7%, p < 0.0001 against the per-tradition null (Established). (viii) Sub-clustering within the linear-chain family yielded silhouette = 0.63 (strong), with compact chains (N <= 6, 5 members) and deep chains (N >= 7, 6 members including Gospel of Mary).

**Originality/value.** This is the third corpus expansion and the first to introduce a tradition from a geographically isolated civilisation. The Popol Vuh result constitutes the strongest evidence to date that the two-family attractor is not a regional Mediterranean/Asian diffusion pattern but a structurally independent phenomenon — an inference consistent with a pan-human constraint on hierarchical cosmological reasoning. The edge-weighted GED methodology provides a principled way to distinguish topological identity from semantic identity, resolving a limitation identified in Ceisiwr (2026c). The direction-agnostic validation extends the protocol's applicability to ascending, descending, and bidirectional cosmologies without loss of comparative power.

**Keywords:** emanation hierarchies; graph theory; Popol Vuh; Mesoamerican cosmology; Gnostic texts; Trimorphic Protennoia; Gospel of Mary; cross-cultural convergence; graph edit distance; edge-weighted GED; digital humanities; structural attractors; direction-agnostic encoding

---

## 1. Introduction

In Ceisiwr (2026a), we introduced a computational methodology for comparing cosmological emanation hierarchies across religious and philosophical traditions. Nine traditions were encoded as labelled directed acyclic graphs (DAGs) and compared using graph edit distance (GED), Weisfeiler-Leman kernels, and VF2 isomorphism testing against a null distribution of 7,000 random trees. The study identified a two-family topology (linear chains and branching trees), two exact structural isomorphisms between unrelated traditions, and a statistically significant overrepresentation of linear chains.

In Ceisiwr (2026b), the corpus was extended to 11 traditions with Proclean Neoplatonism and Suhrawardian Illuminationism, raising the isomorphism count to five and demonstrating family stability across intellectual lineages. In Ceisiwr (2026c), three further traditions -- Zoroastrian Bundahishn, Manichaean Realm of Light, and Derveni Orphic theogony -- extended the corpus to 14 schemas, introduced the sixth edge type (succession), revealed a triple isomorphism (Derveni-Plotinus-Taoist, GED = 0), and identified sub-clustering within the linear-chain family (silhouette = 0.68).

However, the 14-tradition corpus remained geographically constrained: all traditions originated in the Mediterranean, Near Eastern, Indian, or Chinese cultural zones -- regions with documented intellectual exchange. The two-family attractor could therefore be an artifact of diffusion rather than an independent structural constraint on cosmological reasoning. Additionally, all structural isomorphisms (GED = 0 pairs) remained unresolved at the semantic level: traditions like Derveni (succession) and Plotinus (emanation) use fundamentally different cosmological mechanisms yet appear identical under topology-only GED.

The present study addresses both limitations. We extend the corpus to 17 traditions by adding three schemas selected for distinct analytical contributions:

1. **Popol Vuh** (*K'iche' Maya*, pre-Columbian Mesoamerica; Christenson 2007, Tedlock 1985). A creation-by-trial cosmogony: three sequential attempts to create humanity, two of which fail catastrophically, interspersed with the Hero Twins' descent into and triumph over Xibalba (the Underworld). The Divine Triad speaks the world into being through creative utterance. This is the first tradition in the corpus from a civilisation with zero documented contact with any Mediterranean, Near Eastern, Indian, or Chinese cosmological tradition. If the Popol Vuh independently converges on one of the two structural attractors, the two-family classification cannot be attributed to cultural diffusion.

2. **Trimorphic Protennoia** (Nag Hammadi Codex XIII,1; Layton 1987, Robinson 1988, Turner 1990). A single divine figure (Protennoia/Barbelo/First Thought) descends three times in three simultaneous forms -- Voice, Speech, and Logos -- each penetrating deeper into materiality. Structurally, this is neither serial emanation (Plotinus), nor error-driven branching (Valentinian), nor mission-driven branching (Manichaean), but parallel self-expression of the same divine identity. It introduces a fourth mode of branching within the branching-tree family.

3. **Gospel of Mary** (BG 8502,1; King 2003, Tuckett 2007). The soul ascends through seven hostile Powers (psychological gatekeepers: Darkness, Desire, Ignorance, Zeal for Death, Kingdom of Flesh, Foolish Wisdom, Wrathful Wisdom) toward Silence/Rest. This is the only cosmology in the corpus where the direction of traversal is upward (ascent, not descent). It contains no Sophia, no Demiurge, no Aeons, and no Pleroma -- it is entirely psychological/experiential rather than cosmogonic. Including it forces a methodological decision: does direction matter for structural comparison? We adopt a direction-agnostic encoding (source at the apex, matter at the base) and validate it by showing that GED is invariant under edge reversal.

In addition to these three new schemas, we introduce a new analytical tool: **edge-weighted Graph Edit Distance**, which assigns semantic substitution costs to edge-type pairs. This resolves the limitation identified in Ceisiwr (2026c), where the Derveni-Plotinus-Taoist triple isomorphism (structural GED = 0) masked genuine cosmological differences.

### 1.1 Predictions

**Prediction 1 (Family stability).** The two-family classification will remain stable at 17 traditions with a separation ratio above 2.0x. The Popol Vuh and Trimorphic Protennoia will classify as branching trees; the Gospel of Mary will classify as a linear chain.

**Prediction 2 (Geographic generality).** The Popol Vuh, with no documented contact relevant to the cosmological structures under study, will independently converge on the branching-tree attractor — evidence that the two-family structure is not a diffusion artifact.

**Prediction 3 (Edge-weighted GED resolution).** The edge-weighted GED will resolve all 8 prior structural isomorphisms (GED = 0 pairs), assigning non-zero distances to pairs that use different edge types despite identical topology.

**Prediction 4 (Direction invariance).** The Gospel of Mary's GED values will be identical under direction-agnostic (descending) and direction-sensitive (ascending) encoding, validating the direction-agnostic protocol.

---

## 2. Methodology

### 2.1 Schema Encoding Protocol

All three traditions were encoded following the seven-rule DAG contract established in Ceisiwr (2026a), with the succession edge type from Ceisiwr (2026c). The six permitted edge types are: emanation, creation, fragmentation, contraction, reflection, and succession.

### 2.2 Popol Vuh Schema

**Primary sources:** Christenson, A. J. (2007) *Popol Vuh: The Sacred Book of the Maya*. Norman: University of Oklahoma Press; Tedlock, D. (1985) *Popol Vuh: The Definitive Edition of the Mayan Book of the Dawn of Life and the Glories of Gods and Kings*. New York: Simon & Schuster.

**Encoding (11 nodes, depth 6, branching tree, max branching factor 4):**

| Level | Node | Functional Role | Edge Type (from parent) |
|---|---|---|---|
| 0 | Divine Triad (Heart of Sky / Heart of Earth / Q'ukumatz) | source | -- |
| 1 | Creative Speech / Breath-Word | process | creation |
| 2 | Earth and Animals | matter | creation |
| 3 | Mud People (1st attempt -- fails) | matter | creation |
| 3 | Wooden People (2nd attempt -- destroyed) | matter | creation |
| 4 | Xibalba / Underworld Trial | fallen | fragmentation |
| 4 | Hero Twins (Hunahpu and Xbalanque) | process | contraction |
| 5 | Sun and Moon | intermediary | creation |
| 5 | Maize Discovery (Fox, Coyote, Parrot, Crow) | process | creation |
| 6 | Maize People (3rd attempt -- stable) | matter | creation |
| 6 | Maize Women / Humanity Established | matter | creation |

**Key encoding decisions.** (a) The Divine Triad is encoded as a single source node. Heart of Sky (Huracan), Heart of Earth, and Sovereign Plumed Serpent (Q'ukumatz/Kukulkan) act as a co-present creative unity, not a sequential emanation chain. This follows the same encoding logic applied to the Hermetic "All" and the Ishraq "Light of Lights" (Interpreted). (b) Three sequential creation attempts (Mud, Wood, Maize) are separate branches from Creative Speech, not nested levels, because each is a complete cosmological act that fails or succeeds independently. (c) The Hero Twin / Xibalba cycle is included as a side-branch (fragmentation from Wooden People destruction, contraction via Twin resurrection), because it is the mythic mechanism that redeems failed creation and enables the final Maize People. Removing it is tested in the sensitivity analysis (Section 3.4).

**Independence assessment: STRONG.** The K'iche' Maya civilisation had zero documented contact with Mediterranean, Near Eastern, Indian, or Chinese cosmological traditions. The Popol Vuh was transcribed in the mid-16th century from an older oral/pictographic tradition. Any structural convergence with corpus traditions must be attributed to independent cognitive or cosmological constraints rather than diffusion (Established).

**Alternative encodings.** (a) *Without Xibalba*: Remove Hero Twin cycle (3 nodes); tested in sensitivity analysis. (b) *Expanded triad*: Split Divine Triad into three separate source nodes (violates single-root DAG contract).

### 2.3 Trimorphic Protennoia Schema

**Primary sources:** Layton, B. (1987) *The Gnostic Scriptures*; Robinson, J. M. (1988) *The Nag Hammadi Library in English*, 3rd ed.; Turner, J. D. (1990) "Trimorphic Protennoia" in *Nag Hammadi Codices XI, XII, XIII*.

**Encoding (7 nodes, depth 4, branching tree, max branching factor 3):**

| Level | Node | Functional Role | Edge Type |
|---|---|---|---|
| 0 | Invisible Spirit | source | -- |
| 1 | Protennoia / Barbelo (First Thought) | first_emanation | emanation |
| 2 | First Descent: Voice (Phone) | intermediary | emanation |
| 2 | Second Descent: Speech (Phthongos) | intermediary | emanation |
| 2 | Third Descent: Logos / Christ | intermediary | emanation |
| 3 | Five Seals (Baptismal Illumination) | process | creation |
| 4 | Rescued Souls / Luminous Ones | soul | contraction |

**Key encoding decisions.** The three descents are the defining structural feature. Protennoia is the *same divine figure* at all three levels -- she does not emanate distinct beings but expresses herself in three simultaneous aspects (Voice awakens, Speech gives form, Logos liberates). Only the Logos descent leads to the Five Seals mechanism and soul rescue, producing an asymmetric branching tree. This is structurally distinct from all prior branching modes: emanative radiation (Hermetic), error-driven fall (Valentinian), and mission-driven evocation (Manichaean).

**Alternative encoding.** *Material World node*: Add an explicit Chaos/Material World node at the base that all three descents penetrate. Adds 1 node and 2 edges; does not change family classification.

### 2.4 Gospel of Mary Schema

**Primary sources:** King, K. L. (2003) *The Gospel of Mary of Magdala*; Tuckett, C. M. (2007) *The Gospel of Mary*; Berlin Gnostic Codex 8502,1.

**Encoding (9 nodes, depth 8, linear chain):**

| Level | Node | Functional Role | Edge Type |
|---|---|---|---|
| 0 | Silence / Rest (Anapausis) | source | -- |
| 1 | Power 7: Wrathful Wisdom | intermediary | emanation |
| 2 | Power 6: Foolish Wisdom | intermediary | emanation |
| 3 | Power 5: Kingdom of Flesh | intermediary | emanation |
| 4 | Power 4: Zeal for Death | intermediary | emanation |
| 5 | Power 3: Ignorance | intermediary | emanation |
| 6 | Power 2: Desire (Epithumia) | intermediary | emanation |
| 7 | Power 1: Darkness (Skotos) | intermediary | emanation |
| 8 | Material World / Body | matter | emanation |

**Direction-agnostic encoding rationale.** The text describes the soul's *ascent* through the seven Powers, with Silence/Rest as the destination and Material World as the starting point. However, the DAG protocol encodes cosmological hierarchy (source at apex, matter at base), not narrative direction. We adopt the convention that the *hierarchy* is encoded top-down regardless of the text's narrative direction. The topology of a linear chain is identical whether read top-down or bottom-up; we validate this empirically by showing that GED is invariant under edge reversal (Section 3.3).

**Alternative encoding.** *Direction-sensitive ascending*: Reverse all edges, change all edge types from emanation to contraction. Root becomes Material World; terminal node becomes Silence/Rest. Tested in sensitivity analysis.

### 2.5 Edge-Weighted Graph Edit Distance

Standard GED (Ceisiwr 2026a) treats all edge substitutions equally: replacing any edge type with any other costs 1.0. This conflates semantically related changes (emanation -> creation, both generative processes) with semantically opposed changes (creation -> fragmentation, generative vs. destructive). We introduce edge-weighted GED with a semantic substitution cost matrix:

| Substitution | Cost | Rationale |
|---|---|---|
| Same type (e.g. emanation -> emanation) | 0.0 | Identical |
| Related pair: emanation <-> creation | 0.5 | Both are generative processes |
| Related pair: fragmentation <-> contraction | 0.5 | Both involve structural collapse/gathering |
| Related pair: reflection <-> succession | 0.5 | Both involve return/displacement dynamics |
| Unrelated pairs (all others) | 1.0 | Default: no semantic overlap |
| Opposite pair: creation <-> fragmentation | 1.5 | Generative vs. destructive: maximum semantic distance |
| Opposite pair: emanation <-> contraction | 1.5 | Outflow vs. inflow: maximum semantic distance |

Node substitution costs remain unchanged: 0.0 if same functional_role, 1.0 otherwise.

This methodology extends the standard GED framework (which remains computed alongside the weighted version) without replacing it. Both structural GED and weighted GED are reported for all 136 pairs.

### 2.6 Computational Pipeline

The full six-step pipeline from Ceisiwr (2026a) was re-executed on the 17-schema corpus:

1. Schema loading and DAG contract validation (7 rules)
2. Topological invariant computation (30+ metrics per schema)
3. Null model generation (18,000 random DAG trees: 1,000 pooled + 1,000 per tradition stratified)
4. Statistical testing (6 formal tests: per-tradition extremity, depth convergence, chain frequency, Mann-Whitney, pairwise depth similarity, role sequence similarity)
5. Isomorphism and similarity testing (VF2, structural GED, role-labeled GED, **edge-weighted GED**, WL kernels, subgraph isomorphism, family clustering)
6. Figure generation (6 publication-ready figures, 300 DPI)

Additionally, a dedicated sensitivity analysis tested four alternative encodings:
- Suhrawardi branching alternative (from Ceisiwr 2026c)
- Zurvanite Bundahishn alternative (from Ceisiwr 2026c)
- Popol Vuh without Xibalba cycle (new)
- Gospel of Mary direction-sensitive ascending (new)

### 2.7 Software and Data Availability

All schemas, scripts, and outputs are available in the project repository: https://github.com/OwainGlyndwr1400/geographic-generality-emanation-cosmologies-wp1-4. The pipeline requires Python 3.10+, NetworkX, NumPy, SciPy, and matplotlib.

---

## 3. Findings

### 3.1 Family Classification and Stability (17 Traditions)

All 17 schemas loaded and passed the seven-rule DAG contract validation without error (Established).

**Family assignment:**

| Family | Count | Members |
|---|---|---|
| Linear chain | 11 | Plotinian, Taoist DDJ, Derveni Orphic, Bundahishn, Chaldean, Ishraq, Lurianic, Samkhya, Proclean, Sethian, **Gospel of Mary** |
| Branching tree | 6 | Hermetic, Genesis, Valentinian, Manichaean, **Popol Vuh**, **Trimorphic Protennoia** |

**Separation metrics:**

| Metric | WP 1.3 (14 schemas) | WP 1.4 (17 schemas) | Change |
|---|---|---|---|
| Linear chains | 10 | 11 | +1 (Gospel of Mary) |
| Branching trees | 4 | 6 | +2 (Popol Vuh, Trimorphic Protennoia) |
| Intra-chain mean GED | 2.76 | 3.20 | +0.44 |
| Intra-branch mean GED | 9.00 | 8.00 | -1.00 |
| Inter-family mean GED | 7.90 | 7.64 | -0.26 |
| Separation ratio | 2.87x | 2.39x | -0.48 |

The separation ratio decreased from 2.87x to 2.39x (Established). This is expected: we added two branching trees (expanding the branching family from 4 to 6 members, increasing its internal diversity) and one linear chain (Gospel of Mary at depth 8, which is more distant from the compact 5-node chains). The 2.39x ratio remains well above the 2.0x threshold that would indicate clear family separation (Established).

**Prediction 1 confirmed.** The two-family classification is stable at 17 traditions.

### 3.2 Geographic Generality: Popol Vuh

The Popol Vuh classified as a branching tree with max branching factor 4 (Creative Speech branches to Earth/Animals, Mud People, Wooden People, and Maize Discovery). This is the highest branching factor in the corpus, exceeding Genesis (6 at depth 1 but fewer downstream branches) in terms of mid-level branching complexity (Established).

Structurally, the Popol Vuh is the most distant tradition from the linear-chain family (mean GED to linear chains: 10.2). Within the branching-tree family, it clusters closest to Manichaean (GED = 8.0) and Trimorphic Protennoia (GED = 8.0), and most distant from Genesis (GED = 10.0) (Established).

The Popol Vuh's per-tradition extremity test (Test 1) shows that its depth (5) is *not* unusual for a random 11-node tree (null mean = 5.45, z = -0.34, p = 0.746), indicating that its depth is structurally typical for its size. What is unusual is its branching pattern: creation-by-trial (sequential failed attempts) rather than emanation or evocation (Interpreted).

The Popol Vuh also contributes the most diverse edge-type profile in the corpus: creation (7 edges), fragmentation (1), and contraction (1). No other tradition uses creation, fragmentation, *and* contraction edges. This is reflected in the weighted GED: Popol Vuh has the highest mean weighted GED to all other traditions (mean = 17.2), nearly double its mean structural GED (mean = 9.3) (Established).

**Prediction 2 confirmed.** The Popol Vuh independently converged on the branching-tree attractor despite no documented contact with any other corpus tradition's cultural sphere. This is the strongest evidence to date that the two-family attractor reflects a structural constraint independent of regional intellectual exchange.

### 3.3 Edge-Weighted GED: Resolving Structural Isomorphisms

The edge-weighted GED resolved all 8 prior structural isomorphisms (GED = 0 pairs):

| Pair | Structural GED | Weighted GED | Delta | Primary Edge-Type Difference |
|---|---|---|---|---|
| Derveni Orphic -- Plotinian | 0.0 | 5.0 | +5.0 | succession vs. emanation |
| Derveni Orphic -- Taoist DDJ | 0.0 | 3.0 | +3.0 | succession vs. emanation |
| Plotinian -- Taoist DDJ | 0.0 | 2.0 | +2.0 | reflection (Plotinian) absent in DDJ |
| Bundahishn -- Chaldean | 0.0 | 4.5 | +4.5 | creation-heavy vs. emanation-heavy |
| Ishraq -- Samkhya | 0.0 | 1.0 | +1.0 | Minor edge-type variation |
| Ishraq -- Lurianic | 0.0 | 7.5 | +7.5 | Different edge-type profiles |
| Lurianic -- Samkhya | 0.0 | 7.0 | +7.0 | contraction (Lurianic) vs. emanation |
| Proclean -- Sethian | 0.0 | 5.5 | +5.5 | fragmentation (Sethian) absent in Proclean |

The Derveni-Plotinus pair is the paradigmatic case. Both are 5-node linear chains (depth 4) with identical topology -- yet Derveni uses succession edges (theogonic displacement: Ouranos overthrown by Kronos, Kronos overthrown by Zeus) while Plotinus uses emanation edges (continuous overflow: the One pours into Nous, Nous into Soul). The weighted GED of 5.0 correctly reflects this fundamental cosmological difference (Established).

More broadly, every one of the 136 tradition pairs showed a non-zero delta between structural and weighted GED. The mean delta across all pairs was 4.5 edits (range: 1.0 to 15.0). The largest delta was Manichaean vs. Popol Vuh (structural GED = 8.0, weighted GED = 23.0, delta = 15.0), reflecting the extreme edge-type divergence between evocation-based (Manichaean) and creation/fragmentation-based (Popol Vuh) cosmologies (Established).

**Prediction 3 confirmed.** Edge-weighted GED resolves all structural isomorphisms and provides a principled semantic layer over topology-only comparison.

### 3.4 Direction Invariance: Gospel of Mary

The Gospel of Mary was encoded direction-agnostically (Silence/Rest as source at apex, Material World as terminal matter node at base) despite the text describing the soul's *ascent* through seven Powers. The direction-sensitive alternative (Material World as root, all edges reversed, edge types changed from emanation to contraction) was tested in the sensitivity analysis.

**Result:** All 16 GED comparisons between the Gospel of Mary and other traditions were identical under both encodings (Established). This is expected: reversing a linear chain produces an isomorphic DAG (the topology is symmetric). The edge-type change (emanation to contraction) does not affect structural GED (which ignores edge types), and the role-labeled GED is also invariant because the node roles (intermediary chain) remain the same regardless of direction.

**Direction-agnostic validation:** For topology comparison purposes, direction is irrelevant for linear chains. This extends the protocol to ascending, descending, and bidirectional cosmologies without requiring separate treatment (Established). Note: direction may matter for *branching* trees with asymmetric structures -- this remains to be tested in future work.

**Prediction 4 confirmed.** Direction-agnostic encoding is valid for the Gospel of Mary.

### 3.5 Gospel of Mary: Deepest Linear Chain

The Gospel of Mary (9 nodes, depth 8) is the deepest linear chain in the corpus, exceeding Proclean Neoplatonism and Sethian Gnosticism (both depth 7). Its depth is statistically unusual for a random 9-node tree: null mean depth = 4.63, z = 2.89, p = 0.013 (Established).

This is the first tradition in the corpus with *only* intermediary nodes between source and matter. All seven intermediate nodes are psychological gatekeepers (Powers), not cosmological tiers. The Gospel of Mary's functional-role profile -- one source, seven intermediaries, one matter -- is unique: no other tradition has such a high intermediary density (Established).

### 3.6 Trimorphic Protennoia: Fourth Branching Mode

The Trimorphic Protennoia classified as a branching tree (branching factor 3 at Protennoia/Barbelo) and introduced the fourth branching mode:

| Mode | Tradition | Mechanism |
|---|---|---|
| Emanative radiation | Hermetic | Source radiates multiple distinct emanations |
| Error-driven fall | Valentinian | Sophia's error creates Demiurge, splitting the Pleroma |
| Mission-driven evocation | Manichaean | Three parallel rescue missions dispatched |
| **Parallel self-expression** | **Trimorphic Protennoia** | **Same figure descends in three simultaneous forms** |

The parallel self-expression mode is structurally distinctive: the three descent nodes (Voice, Speech, Logos) at Level 2 are all the same divine figure (Protennoia/Barbelo), not distinct beings. Only the Logos descent continues to the Five Seals mechanism and soul rescue, producing an asymmetric branching tree rather than a symmetric star (Interpreted).

### 3.7 Statistical Tests (17-Schema Corpus)

| Test | Statistic | p-value | Significant? |
|---|---|---|---|
| Test 3: Linear chain frequency | 11/17 (64.7%) | < 0.0001 | Yes |
| Test 4: Mann-Whitney depth (real vs. null) | U, real mean = 5.18 vs. null mean = 3.96 | 0.0004 | Yes |
| Test 1: Gospel of Mary depth extremity | z = 2.89 | 0.013 | Yes |
| Test 2: Cross-corpus depth convergence | -- | 0.92 | No |
| Test 5: Pairwise depth similarity | -- | 0.95 | No |

Linear chain overrepresentation (Test 3) and real-schema depth above null (Test 4) remain highly significant at 17 traditions. Cross-corpus depth convergence (Tests 2 and 5) are not significant -- the corpus has enough depth variation (range: 2 to 8) that the traditions do not converge to a single depth. This is not a weakness; it reflects genuine structural diversity within the two-family framework (Interpreted).

### 3.8 Sensitivity Analysis

| Scenario | Chains | Trees | Separation Ratio |
|---|---|---|---|
| Primary (17 schemas) | 11 | 6 | 2.39x |
| Alt 1: Ishraq branching | 10 | 7 | 2.09x |
| Alt 2: Zurvanite Bundahishn | 10 | 7 | 2.12x |
| Alt 3: Popol Vuh without Xibalba | 11 | 6 | 2.24x |

All four scenarios maintain a separation ratio above 2.0x (Established). The Popol Vuh without-Xibalba alternative (Alt 3) still classifies as a branching tree because Creative Speech retains out-degree 4 (four creation branches) even without the Xibalba cycle. The branching structure comes from the creation-by-trial architecture, not the Hero Twin narrative (Established). The Xibalba cycle adds depth but not the fundamental branching pattern.

### 3.9 Sub-Clustering Within the Linear-Chain Family

The sub-clustering analysis from Ceisiwr (2026c) was updated for 11 linear chains:

| Sub-Cluster | Members | Mean Node Count | Intra-Cluster GED |
|---|---|---|---|
| Compact (N <= 6) | Derveni, Plotinian, Taoist, Bundahishn, Chaldean | 5.4 | 1.20 |
| Deep (N >= 7) | Ishraq, Lurianic, Samkhya, Proclean, Sethian, **Gospel of Mary** | 7.7 | 1.87 |

Inter-cluster mean GED: 4.53. Sub-cluster separation ratio: 3.78x. Mean silhouette score: 0.63 (strong clustering). The Gospel of Mary (N = 9) joins the deep sub-cluster and is its most extreme member (deepest chain in the corpus), which slightly reduces the silhouette from 0.68 (at 14 schemas) to 0.63 (at 17 schemas) (Established).

---

## 4. Discussion

### 4.1 Pan-Human Structural Attractors

The Popol Vuh result is the most significant finding of this study. Prior to WP 1.4, every tradition in the corpus originated from regions with some degree of documented intellectual exchange (Mediterranean, Near Eastern, Indian, Chinese). The two-family attractor could have been a Mediterranean/Asian cultural artifact -- a shared cognitive template transmitted through trade, translation, or religious contact.

The K'iche' Maya civilisation eliminates this explanation. There is no documented pathway by which Mediterranean emanation philosophy or Indian metaphysics could have reached pre-Columbian Mesoamerica. Yet the Popol Vuh independently converges on the branching-tree attractor, with a creation-by-trial architecture that uses creation, fragmentation, and contraction edges -- a unique edge-type profile found nowhere else in the corpus.

This suggests that the two-family structure (linear chain / branching tree) reflects a constraint inherent in hierarchical cosmological reasoning itself, not in any specific cultural tradition. At minimum, it is a pan-human structural invariant; at maximum, it points to a deeper cognitive or mathematical constraint on how humans conceptualise the origin and structure of reality (Interpreted).

### 4.2 Semantic Depth Beyond Topology

The edge-weighted GED methodology reveals that structural isomorphism (topology identity) is a necessary but not sufficient condition for cosmological equivalence. The Derveni-Plotinus pair is the paradigmatic case: both are 5-node linear chains, but succession (generational displacement through conflict) and emanation (non-diminishing overflow) are fundamentally different cosmological mechanisms. Treating them as identical (structural GED = 0) is correct at the topological level but misleading at the semantic level.

The weighted GED provides a principled middle ground between pure topology (which loses semantic information) and full textual analysis (which loses structural comparability). The 0.0 / 0.5 / 1.0 / 1.5 cost scale is deliberately coarse: it captures broad semantic relationships (generative vs. destructive, same-type vs. different-type) without attempting to encode the full richness of each tradition's cosmological vocabulary. We consider this coarseness a feature, not a limitation: fine-grained semantic costs would require tradition-specific expert judgment and reduce reproducibility (Interpreted).

### 4.3 Four Modes of Branching

The identification of four branching modes within the branching-tree family is a new analytical finding. Each mode produces a branching tree with different internal dynamics:

1. **Emanative radiation** (Hermetic): Source radiates multiple co-equal emanations. Symmetric branching.
2. **Error-driven fall** (Valentinian): A cosmic error (Sophia's overreach) generates a secondary creator (Demiurge), splitting the hierarchy. Asymmetric branching at a single crisis point.
3. **Mission-driven evocation** (Manichaean): The source deliberately dispatches multiple parallel rescue missions. Symmetric branching (three evocations).
4. **Parallel self-expression** (Trimorphic Protennoia): The same divine figure manifests simultaneously in multiple forms. Asymmetric branching (only one descent leads to soul rescue).

These four modes may represent a complete taxonomy of branching mechanisms in hierarchical cosmologies (Speculative). Testing this hypothesis requires additional branching traditions in future corpus expansions.

### 4.4 Limitations

1. **Edge-type cost assignment.** The related/unrelated/opposite categories for edge-type costs were assigned by the authors based on cosmological semantics. Alternative cost matrices could produce different weighted GED values. Sensitivity testing with permuted costs is planned for WP 1.5.

2. **Direction for branching trees.** Direction-agnostic encoding was validated for the Gospel of Mary (a linear chain), but branching trees with asymmetric structures may not be direction-invariant. This requires future testing.

3. **Corpus size.** At 17 traditions, the corpus remains relatively small for robust statistical inference. The binomial and permutation tests are appropriate for small samples, but some effects (e.g., depth convergence) may require 25+ traditions to reach significance.

4. **Single encoder.** All schemas were encoded by the same research team. Inter-encoder reliability testing is planned for WP 2.

---

## 5. Conclusion

The expansion of the emanation topology corpus to 17 traditions confirms the two-family attractor (linear chain / branching tree) with a separation ratio of 2.39x and extends it to a geographically isolated Mesoamerican tradition for the first time. The Popol Vuh's independent convergence on the branching-tree attractor constitutes the strongest evidence to date that the two-family structure is a pan-human structural invariant rather than a cultural diffusion artifact.

The edge-weighted GED methodology successfully resolves the limitation of structural isomorphism, distinguishing topologically identical traditions that use semantically different cosmological mechanisms. All 8 prior structural isomorphisms (GED = 0 pairs) are resolved, and all 136 tradition pairs show non-zero weighted GED divergence.

The direction-agnostic encoding is validated for linear chains (Gospel of Mary), extending the protocol to ascending, descending, and bidirectional cosmologies. The identification of four branching modes (emanative, error-driven, mission-driven, parallel self-expression) provides a preliminary taxonomy of branching mechanisms.

**Open questions for WP 1.5:**
- Does the compact/deep sub-clustering within linear chains reflect a deeper cognitive bifurcation?
- Can edge-weighted GED costs be empirically calibrated (e.g., through expert elicitation)?
- Will additional branching traditions (Enochian, Rig Vedic, Quranic Mi'raj) introduce new branching modes or converge on the existing four?
- Does direction matter for branching trees?

---

## References

Allberry, C. R. C. (ed.) (1938). *A Manichaean Psalm-Book. Part II.* Manichaean Manuscripts in the Chester Beatty Collection, Vol. II. Stuttgart: W. Kohlhammer.

Anklesaria, B. T. (trans.) (1956). *Zand-Akasih: Iranian or Greater Bundahishn.* Bombay.

Boyce, M. (with F. Grenet, Vol. III) (1975–1991). *A History of Zoroastrianism.* 3 vols. Leiden: Brill.

Bremmer, J. N. (2008). *Greek Religion and Culture, the Bible, and the Ancient Near East.* Jerusalem Studies in Religion and Culture 8. Leiden: Brill.

Ceisiwr, E. (2026a). "The Emanation Topology: A Graph-Theoretic Analysis of Cosmological Hierarchies Across Nine Traditions." Zenodo. DOI: [pending].

Ceisiwr, E. (2026b). "Proclean and Ishraqi Extensions to the Emanation Topology Corpus (11 Traditions)." Zenodo. https://doi.org/10.5281/zenodo.19305988

Ceisiwr, E. (2026c). "Zoroastrian, Manichaean, and Orphic Extensions to the Emanation Topology Corpus: Family Stability and Sub-Clustering at 14 Traditions." Zenodo. https://doi.org/10.5281/zenodo.19324327

Christenson, A. J. (trans.) (2007). *Popol Vuh: The Sacred Book of the Maya.* Norman: University of Oklahoma Press.

Gardner, I. & Lieu, S. N. C. (2004). *Manichaean Texts from the Roman Empire.* Cambridge University Press.

King, K. L. (2003). *The Gospel of Mary of Magdala: Jesus and the First Woman Apostle.* Santa Rosa, CA: Polebridge Press.

Kouremenos, T., Parassoglou, G. M., & Tsantsanoglou, K. (2006). *The Derveni Papyrus.* Studi e Testi per il Corpus dei Papiri Filosofici Greci e Latini 13. Florence: Olschki.

Layton, B. (1987). *The Gnostic Scriptures.* Garden City, NY: Doubleday.

Pasquier, A. (1983). *L'Évangile selon Marie (BG 1).* Bibliothèque copte de Nag Hammadi, Section «Textes» 10. Québec: Les Presses de l'Université Laval.

Robinson, J. M. (ed.) (1988). *The Nag Hammadi Library in English.* 3rd ed. San Francisco: Harper & Row.

Tedlock, D. (trans.) (1985). *Popol Vuh: The Definitive Edition of the Mayan Book of the Dawn of Life and the Glories of Gods and Kings.* New York: Simon & Schuster.

Tuckett, C. M. (2007). *The Gospel of Mary.* Oxford Early Christian Gospel Texts. Oxford: Oxford University Press.

Turner, J. D. (1990). "Trimorphic Protennoia." In *Nag Hammadi Codices XI, XII, XIII*, ed. C. W. Hedrick. Nag Hammadi Studies 28. Leiden: Brill.

West, M. L. (1983). *The Orphic Poems.* Oxford: Clarendon Press.

Zaehner, R. C. (1955). *Zurvan, a Zoroastrian Dilemma.* Oxford: Clarendon Press.
