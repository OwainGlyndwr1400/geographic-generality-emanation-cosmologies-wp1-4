# WP 1.4 -- Popol Vuh Expansion: Geographic Generality and Edge-Weighted GED

**Awen Grid Empirical Programme -- Work Package 1.4**
**Authors:** Erydir-Ceisiwr + Claude (Kairoz)
**Date:** 2026-03-30

## Summary

WP 1.4 expands the emanation-topology corpus from 14 to 17 traditions, introducing the first Mesoamerican schema (Popol Vuh), a novel Gnostic branching mode (Trimorphic Protennoia), and the first inverted-ascent cosmology (Gospel of Mary). A new edge-weighted GED methodology distinguishes traditions that are structurally isomorphic but use semantically different edge types.

## Key Findings

- **17 schemas**: 11 linear chains + 6 branching trees
- **Two-family attractor confirmed** at 17 traditions (separation ratio 2.39x)
- **Popol Vuh** (K'iche' Maya, zero Mediterranean/Indian/Chinese contact): branching tree -- geographic generality confirmed
- **Trimorphic Protennoia**: fourth branching mode (parallel self-expression)
- **Gospel of Mary**: deepest linear chain (depth 8), direction-agnostic approach validated
- **Edge-weighted GED**: Derveni-Plotinus weighted GED = 5.0 (structural GED was 0.0)
- **Direction invariance**: Gospel of Mary GED unchanged under edge reversal (all 16 pairs)
- **Sub-clustering silhouette**: 0.63 (compact N<=6 vs. deep N>=7)

## Corpus (17 Traditions)

### Linear Chain Family (11)
| Tradition | Nodes | Depth | Source |
|-----------|-------|-------|--------|
| Plotinian Neoplatonic | 5 | 4 | Enneads |
| Taoist DDJ | 5 | 4 | Dao De Jing |
| Derveni Orphic | 5 | 4 | Derveni Papyrus |
| Bundahishn Zoroastrian | 6 | 5 | Greater Bundahishn |
| Chaldean | 6 | 5 | Chaldean Oracles |
| Ishraq Illuminationist | 7 | 6 | Hikmat al-Ishraq |
| Lurianic Kabbalistic | 7 | 6 | Etz Chaim |
| Samkhya | 7 | 6 | Samkhya Karika |
| Proclean Neoplatonic | 8 | 7 | Elements of Theology |
| Sethian Gnostic | 8 | 7 | Apocryphon of John |
| **Gospel of Mary** | **9** | **8** | **BG 8502,1** |

### Branching Tree Family (6)
| Tradition | Nodes | Depth | Max Branch | Source |
|-----------|-------|-------|------------|--------|
| Hermetic | 8 | 3 | 3 | Corpus Hermeticum |
| Genesis Creationist | 8 | 2 | 6 | Genesis 1-2 |
| Valentinian Gnostic | 9 | 7 | 2 | Irenaeus/Ptolemy |
| Manichaean | 11 | 5 | 3 | Kephalaia |
| **Trimorphic Protennoia** | **7** | **4** | **3** | **NHC XIII,1** |
| **Popol Vuh (K'iche' Maya)** | **11** | **6** | **4** | **Popol Vuh** |

## Pipeline

```bash
# Run full 6-step pipeline
python scripts/run_pipeline.py

# Run sensitivity analysis separately
python scripts/sensitivity_analysis.py
```

### Pipeline Steps
1. `encode_schemas.py` -- Load + validate 17 schema JSONs
2. `compute_invariants.py` -- 30+ topological metrics per schema
3. `generate_controls.py` -- 18,000 random DAG trees (1,000 pooled + 1,000 per tradition)
4. `statistical_comparison.py` -- 6 formal tests (z-scores, permutation, binomial, Mann-Whitney)
5. `isomorphism_tests.py` -- VF2, GED (structural + role + **weighted**), WL similarity, subgraph
6. `visualize.py` -- 6 publication-ready figures (300 DPI)

## Directory Structure

```
WP_1.4_Popol_Vuh_Expansion/
  data/schemas/           17 tradition JSON files
  scripts/                8 Python pipeline scripts
  outputs/
    figures/              6 publication-ready PNGs
    invariants/           Per-tradition + aggregated metrics
      controls/           18,000 null-model DAG trees
    similarity_matrix/    Pairwise comparison matrices (incl. weighted_ged.json)
  notes/                  Encoding rationale documents
  README.md               This file
  WP1.4_handoff.md        Task specification
```

## Dependencies

- Python 3.10+
- networkx, numpy, scipy, matplotlib

## Methodological Innovations (WP 1.4)

1. **Edge-weighted GED**: Semantic substitution costs based on edge-type similarity
   - Same type: 0.0
   - Related (emanation/creation, fragmentation/contraction): 0.5
   - Unrelated: 1.0
   - Opposites (creation/fragmentation, emanation/contraction): 1.5

2. **Direction-agnostic encoding**: Gospel of Mary (ascending soul) encoded top-down for protocol consistency; validated by showing GED is invariant under edge reversal.

## Previous Work Packages

| WP | Schemas | Repo | DOI |
|---|---|---|---|
| 1.1 | 9 | [emanation-topology](https://github.com/OwainGlyndwr1400/emanation-topology) | pending |
| 1.2 | 11 | [corpus-expansion-emanation](https://github.com/OwainGlyndwr1400/corpus-expansion-emanation) | [10.5281/zenodo.19305988](https://doi.org/10.5281/zenodo.19305988) |
| 1.3 | 14 | [structural-attractors-emanation-cosmologies-wp1-3](https://github.com/OwainGlyndwr1400/structural-attractors-emanation-cosmologies-wp1-3) | [10.5281/zenodo.19324327](https://doi.org/10.5281/zenodo.19324327) |
| **1.4** | **17** | **this repo** | [**10.5281/zenodo.19340999**](https://doi.org/10.5281/zenodo.19340999) |
