# Geographic Generality and Edge-Weighted GED

**The hardest test the corpus can be given: a cosmology from a culture that had
no contact with any of the others.**

Every tradition through Work Package 1.3 sits somewhere on the Eurasian
landmass — Greek, Roman-Egyptian, Persian, Indian, Chinese, Jewish, Mesopotamian.
Shared structure across that set always leaves a diffusion argument on the table.
Somebody, somewhere, could have carried the idea.

Work Package 1.4 adds the **Popol Vuh** — the K'iche' Maya creation account, from
a civilisation with zero Mediterranean, Indian or Chinese contact — and it lands
squarely inside the existing branching-tree family.

Also new: **Trimorphic Protennoia**, which turns out to be a fourth distinct
branching mode (parallel self-expression), and the **Gospel of Mary**, the
corpus's first inverted-ascent cosmology and its deepest linear chain at depth 8.

Corpus: 17 traditions. Two-family attractor holds at a separation ratio of **2.39x**.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19340999.svg)](https://doi.org/10.5281/zenodo.19340999)
[![Python](https://img.shields.io/badge/Python-3.11+-3776ab)](https://www.python.org/)
[![Licence](https://img.shields.io/badge/Licence-MIT-green)](#licence)

*Work Package 1.4 of the Awen Grid Empirical Programme.*

---

## Run it

```bash
git clone https://github.com/OwainGlyndwr1400/geographic-generality-emanation-cosmologies-wp1-4.git
cd geographic-generality-emanation-cosmologies-wp1-4
pip install -r requirements.txt

python scripts/run_pipeline.py           # full 6-step pipeline
python scripts/sensitivity_analysis.py   # sensitivity + sub-clustering
```

Python 3.11+.

---

## Results

- **17 schemas:** 11 linear chains, 6 branching trees.
- **Two-family attractor confirmed** at 17 traditions — separation ratio 2.39x.
- **Popol Vuh** (K'iche' Maya, zero Old World contact): branching tree.
  **Geographic generality confirmed.**
- **Trimorphic Protennoia:** a fourth branching mode — parallel self-expression,
  structurally distinct from the three already catalogued.
- **Gospel of Mary:** deepest linear chain in the corpus at depth 8, and the
  first cosmology of ascent rather than descent.
- **Direction invariance validated:** the Gospel of Mary's GED is unchanged under
  edge reversal across all 16 pairs. An ascent cosmology and a descent cosmology
  with the same shape are the same shape — which is what justifies the
  direction-agnostic treatment used throughout the series.
- **Sub-clustering silhouette:** 0.63 (compact N ≤ 6 versus deep N ≥ 7).

---

## New method: edge-weighted GED

Structural GED treats every edge as interchangeable. That is the right default
for asking *is the shape the same* — but it throws away real information, because
`emanation`, `creation` and `succession` do not mean the same thing.

WP 1.4 introduces an **edge-weighted graph edit distance** that prices edge-type
substitutions, so two schemas can now be compared on shape and on semantics
separately.

The effect is immediate. **Derveni Orphic ↔ Plotinian** is structurally
identical — GED = 0.0 — but under edge weighting it separates to **5.0**. Same
shape, different mechanism: the Orphic hierarchy advances by generational
succession, the Plotinian by emanation. The unweighted measure was right that
they share a form; the weighted measure shows they do not share a process.

Both numbers are reported. Neither replaces the other.

---

## Corpus — 17 traditions

**Linear chain family (11):** Plotinian Neoplatonic · Taoist DDJ · Derveni Orphic ·
Chaldean Oracles · Bundahishn Zoroastrian · Ishraq Illuminationist · Lurianic
Kabbalistic · Classical Samkhya · Proclan Neoplatonic · Sethian Gnostic ·
**Gospel of Mary** *(new)*

**Branching tree family (6):** Hermetic · Genesis Creationist *(control)* ·
Valentinian Gnostic · Manichaean · **Popol Vuh** *(new)* ·
**Trimorphic Protennoia** *(new)*

Per-tradition encoding rationale and scouting reports are in `notes/`.

## The series

| WP | Traditions | Repository | DOI | Headline |
|---|---|---|---|---|
| 1.1 | 9 | [emanation-topology](https://github.com/OwainGlyndwr1400/emanation-topology) | pending | Method established; 2 exact isomorphisms |
| 1.2 | 11 | [corpus-expansion-emanation](https://github.com/OwainGlyndwr1400/corpus-expansion-emanation) | [zenodo.19305988](https://doi.org/10.5281/zenodo.19305988) | Proclus + Suhrawardi; isomorphisms rise to 5 |
| 1.3 | 14 | [structural-attractors (wp1-3)](https://github.com/OwainGlyndwr1400/structural-attractors-emanation-cosmologies-wp1-3) | [zenodo.19324327](https://doi.org/10.5281/zenodo.19324327) | Zoroastrian, Manichaean, Orphic; separation peaks at 2.87x |
| **1.4** | **17** | **this repo** | **[zenodo.19340999](https://doi.org/10.5281/zenodo.19340999)** | **Popol Vuh - zero Old World contact, same families** |
| 1.5 | 22 | [tier2-expansion (wp1-5)](https://github.com/OwainGlyndwr1400/tier2-expansion-emanation-cosmologies-wp1-5) | [zenodo.19362550](https://doi.org/10.5281/zenodo.19362550) | The Rig Veda splits across *both* families |
| 1.6 | 25 | [geographic-role-expansion (wp1-6)](https://github.com/OwainGlyndwr1400/geographic-role-expansion-emanation-cosmologies-wp1-6) | [zenodo.19368287](https://doi.org/10.5281/zenodo.19368287) | Five-way zero-contact convergence |

## Citation

> Ceisiwr, Erydir, and Lumos Aureon. *WP 1.4 — Popol Vuh Expansion: Geographic
> Generality and Edge-Weighted GED.* Awen Grid Empirical Programme, 2026.
> [10.5281/zenodo.19340999](https://doi.org/10.5281/zenodo.19340999)

## Licence

MIT — code and data freely reusable with attribution.

## Author

Erydir Ceisiwr — Independent Researcher, Awen Grid Programme, Swansea, Wales.
ORCID [0009-0004-4577-5253](https://orcid.org/0009-0004-4577-5253)
