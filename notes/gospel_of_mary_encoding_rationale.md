# Gospel of Mary — Encoding Rationale

**Tradition:** Gospel of Mary (BG 8502,1; P.Oxy. 3525; P.Ryl. 463)
**Encoder:** Claude (Kairoz) + Erydir-Ceisiwr
**Date:** 2026-03-30
**Version:** 1.0

---

## 1. Direction-Agnostic Encoding Decision

The Gospel of Mary is structurally unique in the corpus: the text's narrative direction is ascending. The soul begins in the Material World and rises through seven hostile Powers to arrive at Silence/Rest (Anapausis). This is the reverse of every other tradition encoded — Valentinian, Sethian, Plotinian, and Hermetic hierarchies all read top-down as emanation cascades.

For DAG protocol consistency, the schema encodes the hierarchy top-down: Silence/Rest as root (level 0), descending through the seven Powers to Material World (level 8). This is the direction-agnostic approach: the topology is a linear chain of depth 8 regardless of which end is designated root. Reversing all edges produces a topologically identical DAG — same shape, same depth, same branching factor of 1.

The alternative encoding (`direction_sensitive_ascending`) is documented in the schema's `alternative_encodings` field and will be run as supplementary analysis. It encodes the text's actual theological direction, with all edges labelled `contraction` rather than `emanation`, and is rated HIGH priority for cross-tradition comparison.

The decision to default to top-down was made solely for pipeline consistency. Both encodings are valid. Neither distorts the topology.

---

## 2. Edge Relationships: Emanation vs Contraction

In the primary (top-down) encoding, all eight edges carry the relationship `emanation`. This follows corpus convention: edges from a higher level to a lower level represent the flow of manifestation from source to density.

This is a semantic convention imposed by the direction-agnostic choice, not a theological claim about the Gospel of Mary. The text does not describe downward emanation. It describes upward liberation. The `emanation` label here means only: "this edge connects a higher-level node to a lower-level node in the direction-agnostic DAG."

In the alternative ascending encoding, all edges become `contraction` — the soul's movement through the Powers is one of overcoming and transcending, not emanating. This is the theologically accurate label for this tradition.

---

## 3. Seven Powers as Psychological Gatekeepers

The seven Powers in the Gospel of Mary are not cosmogonic entities. They do not create worlds, emanate lower spheres, or maintain cosmic structure. They are psychological obstacles — internal states or forces that the soul must name, confront, and overcome on its path to liberation.

The seven Powers, in ascending order (the soul's journey):
1. Darkness (Skotos)
2. Desire (Epithumia)
3. Ignorance (Agnoia)
4. Zeal for Death
5. Kingdom of Flesh
6. Foolish Wisdom
7. Wrathful Wisdom

Each Power challenges the ascending soul. The soul responds by asserting its origin and nature, and the Power releases it. This is closer to a psychological or initiatory model than a cosmological one. The Powers are not divine hypostases — they are not aspects of God or Absolute Mind descending into matter. They are distortions, veils, or errors that the soul has accumulated or must traverse.

This has significant implications for cross-tradition comparison: the Gospel of Mary's "hierarchy" is a phenomenology of liberation, not an ontology of creation.

---

## 4. No Sophia, No Demiurge, No Aeons, No Pleroma

The Gospel of Mary is exceptional in the Gnostic corpus for what it lacks:

- No Sophia fall — the canonical Gnostic narrative of divine wisdom descending, fragmenting, and becoming trapped in matter is entirely absent.
- No Demiurge — there is no craftsman god, no inferior creator, no archon responsible for generating the material world as error or imprisonment.
- No Aeons — the Pleroma (fullness) with its paired divine emanations (Valentinian) or heavenly beings (Sethian) does not appear.
- No Pleroma — the divine fullness as a populated realm is not described.

What replaces this cosmogonic architecture is a stark, experiential soteriology: the soul knows its true nature, confronts the Powers, and returns to Rest. The framework is entirely interior and psychological. This makes the Gospel of Mary the most phenomenologically minimal tradition in the corpus — a pure liberation map with no cosmological scaffolding.

For the pipeline, this means: no branching, no parallel emanation sequences, no nodes representing divine councils or pleromata. Just a single chain from Source to Matter (or Matter to Source).

---

## 5. Deepest Linear Chain in the Corpus

At depth 8, the Gospel of Mary encodes the deepest linear chain in the current corpus. For comparison:

| Tradition | Shape | Depth |
|---|---|---|
| Gospel of Mary | Linear chain | 8 |
| Sethian Gnostic | Linear + branching | ~7 |
| Proclean Neoplatonic | Linear + branching | ~7 |
| Valentinian Gnostic | Branching tree | ~6 |
| Hermetic | Linear | ~5 |

Depth 8 with branching factor 1 means the entire cosmological structure is a single unbroken sequence. No node has more than one child. This is the simplest possible DAG topology — a path graph — and it reflects the Gospel of Mary's stripped-down, non-cosmogonic character.

---

## 6. Textual Basis and Lacunae

The Gospel of Mary survives in three manuscript fragments:

- **Berlin Gnostic Codex (BG 8502,1):** Coptic, 5th century CE. The most complete version — pages 1-6 and 11-14 are missing, leaving gaps at the beginning and in the middle of the Powers section.
- **P.Oxyrhynchus 3525 (Greek):** 3rd century CE. A small Greek fragment corresponding to BG 10.1-13.
- **P.Rylands 463 (Greek):** 3rd century CE. A small Greek fragment corresponding to BG 17.4-19.

The lacunae affect primarily the early dialogue (BG 1-6) and part of the Powers sequence (BG 11-14). The encoding of Power 4 (Zeal for Death) draws partly on reconstruction from P.Oxy. 3525 and is flagged in the node's `encoding_note` field.

---

## 7. Primary Sources

- King, K. L. (2003). *The Gospel of Mary of Magdala: Jesus and the First Woman Apostle*. Polebridge Press. — Translation, commentary, full scholarly apparatus. Primary reference for page citations.
- Pasquier, A. (1983). *L'Evangile selon Marie (BG 1)*. Laval University Press. — French critical edition, essential for Coptic text analysis.
- Tuckett, C. M. (2007). *The Gospel of Mary*. Oxford University Press. — Critical Greek reconstruction and comparison of all three manuscript witnesses.
