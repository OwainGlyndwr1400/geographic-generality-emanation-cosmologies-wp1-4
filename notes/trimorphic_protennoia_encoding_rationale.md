# Trimorphic Protennoia — Encoding Rationale

**Schema:** `data/schemas/trimorphic_protennoia.json`
**Source:** Nag Hammadi Codex XIII,1
**Encoded:** 2026-03-30
**Encoder:** Claude (Kairoz) + Erydir-Ceisiwr

---

## The Fourth Branching Mode: Parallel Self-Expression

Trimorphic Protennoia introduces a structural pattern not found in any of the 14 existing schemas. To understand why, it helps to name the other three branching modes explicitly:

1. **Emanative / Serial (Plotinus, Proclus, Hermetic):** The divine cascades downward through a hierarchy of successively lesser hypostases. Each level is a distinct ontological entity. The chain is serial and non-reversing at the level of identity.

2. **Error-Driven Branching (Valentinian Gnostic):** A fall or mistake — Sophia's desire, a premature act of will — generates a branch into matter. The branching is caused by defect, not design. Rescue is necessary precisely because something went wrong.

3. **Mission-Driven Branching (Manichaean):** A deliberate divine intervention sends an emissary into the lower world to retrieve trapped light. The emissary is a distinct figure, not the source itself. The mission is planned, not reactive.

4. **Parallel Self-Expression (Trimorphic Protennoia — this schema):** A single divine figure — Protennoia, First Thought, Barbelo — descends three times in three forms without ceasing to be the same identity. Voice, Speech, and Logos are not distinct emanations, not errors, not separate emissaries. They are the same being expressing itself in three simultaneous modes of self-disclosure, each penetrating deeper into materiality. This is not a cascade, not a fall, not a mission — it is a trifold self-revelation.

This is why the three descent nodes (descent_voice, descent_speech, descent_logos) share level 2 and all branch from the single protennoia node. They are co-equal expressions of the same identity, not a chain.

---

## Structural Challenge: Same Divine Figure at Three Levels

The primary encoding challenge is that Protennoia is simultaneously:
- The first emanation of the Invisible Spirit (level 1 node)
- The agent of all three descents (parent of level 2 nodes)
- The implicit subject even within the descended forms

A naive encoding might try to create three separate "Protennoia" nodes for each descent. This was rejected because it misrepresents the theology: the text repeatedly asserts that Voice, Speech, and Logos are the same "I" speaking. The Voice says "I am Protennoia." The Speech says "I am Protennoia." The Logos says "I am Protennoia."

The solution adopted here is a single protennoia node with three outgoing emanation edges — one per descent form. This correctly encodes the branching structure while preserving the unity of identity. The edges share the same relationship type (emanation) rather than using distinct types, because each descent is an equal act of self-expression, not a hierarchical progression of ontological distance from the source.

---

## Five Seals as Process Node

The Five Seals (five_seals node) are encoded as a **process** node with functional_role "process" — distinct from all other functional roles in the schema (source, first_emanation, intermediary, soul). This choice reflects their nature in the text: they are not a divine hypostasis, not a soul, not an emanated being. They are a **mechanism** — the baptismal rite through which liberation is accomplished.

The edge from descent_logos to five_seals uses relationship "creation" (Logos enacts the rite), and the edge from five_seals to souls_rescued uses relationship "contraction" (souls are gathered/contracted back from dispersal in matter). This follows the existing pipeline's edge vocabulary while precisely capturing the functional distinction between the rite's administration and its effect.

---

## Alternative Encoding Considered

Turner (1990) emphasises that all three descents penetrate the same material realm — progressively deeper, but into the same chaos. This suggests an alternative encoding: add an explicit Material World / Chaos node at level 3 with edges from descent_voice and descent_speech pointing into it, and then from material_world to five_seals (or souls_rescued).

This alternative is documented in the schema's alternative_encodings field. It was not adopted for the primary encoding because:
- It adds structural complexity (8 nodes, 8 edges) without changing the tradition's family classification
- The primary text's emphasis is on the descending subject (Protennoia), not the descended-into object (Chaos)
- The existing 6-edge DAG already correctly encodes the causal chain: source → first thought → three descent forms → rite → rescued souls

The alternative remains available for future comparative analysis or if Turner's material-realm emphasis becomes the focus of a subsequent paper.

---

## Source References

- **Layton, B. (1987).** *The Gnostic Scriptures.* Doubleday. — Provides the foundational English translation and theological context for Protennoia as Barbelo/First Thought.
- **Robinson, J. M., ed. (1988).** *The Nag Hammadi Library in English*, 3rd ed. Harper & Row. — Primary source for all passage references in the schema (pages 35-50 of the codex).
- **Turner, J. D. (1990).** Trimorphic Protennoia. In *Nag Hammadi Codices XI, XII, XIII.* Brill. — Scholarly commentary used for the alternative encoding note regarding the material world as shared target.

---

## DAG Properties

| Property | Value |
|---|---|
| Nodes | 7 |
| Edges | 6 |
| Depth | 4 |
| Max branching factor | 3 (at protennoia node) |
| Shape | branching_tree |
| Root | invisible_spirit |
| Is DAG | true |
| All connected | true |
