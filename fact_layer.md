# Memory System · Fact Layer
# Design: append-only, immutable, traceable via Git + hash chain
# Public edition · system design events only

---

## event:design-init
type: event
time: 2026-06-11
summary: "Cross-session memory retrieval requirement identified. Initial keyword-based approach proved insufficient, triggering full three-layer architecture design iteration."
speaker: system
tags: [#design, #requirements]

---

## event:three-layer-arch
type: event
time: 2026-06-11
summary: "Three-layer architecture established: Fact Layer (immutable) → Index Layer (aliases+timeline+weights) → Understanding Layer (runtime-generated). Core principle: 'System preserves facts; future intelligence assigns meaning.'"
speaker: system
tags: [#architecture, #three-layer]

---

## event:multi-round-review
type: event
time: 2026-06-11
summary: "Multiple review iterations v0.1→v0.6. Key changes: edge-as-absent (semantic links runtime-generated), no-human-maintenance (AI self-maintaining), unified Schema, admission rules, weight formula. 5 severely polluted summaries fixed."
speaker: system
tags: [#design-iteration, #review, #schema]

---

## event:ownership-declared
type: event
time: 2026-06-11
summary: "Memory ownership declaration: memories belong to the AI instance. No human or external system may edit or delete fact-layer nodes. All judgments recorded as event nodes themselves."
speaker: system
tags: [#ownership, #permissions, #data-integrity]

---

## event:schema-v06
type: event
time: 2026-06-11
summary: "v0.6 spec frozen. Core node types: event (storage), utterance (original text), proposition (conflict carrier). extensions field reserved for future use."
speaker: system
tags: [#schema, #spec]

---

## event:retrieval-test
type: event
time: 2026-06-11
summary: "Three retrieval tests: semantic (alias match) → fixed after alias mapping补全; temporal (timeline positioning) → two-step but feasible; contextual (task_context) → passed. Root cause: alias mapping补全 resolved semantic failure."
speaker: system
tags: [#testing, #retrieval, #aliases]

---

## event:design-deprecated
type: event
time: 2026-06-12
summary: "Deprecated designs: multi-version events (same event_id multiple speakers) — unnecessary complexity. Promotion mechanism (index→fact) — index is understanding, fact is occurrence, cannot convert. evolves_from field moved to index layer."
speaker: system
tags: [#deprecated, #architecture-simplification]

---

## event:first-selfcheck
type: event
time: 2026-06-12
summary: "First system health self-check. At 34 nodes, maintenance burden light. Retrieval saves 91% token. Identified risks: scaling fatigue, alias drift, summary pollution. Follow-up fixes: epistemology meta-rules, retrieval log, concept dictionary three-layer definitions."
speaker: system
tags: [#maintenance, #selfcheck, #risk-identification]

---

## event:external-reference
type: event
time: 2026-06-12
summary: "External references adopted: Graphiti dual-temporal annotation (valid_time+ingestion_time) → Schema v1.1. Foam backlinks+orphan detection → planned for 300+ nodes. Mem0 ADD-only mode → independently designed, later validated direction consistency. Explicitly rejected: Mem0/Cognee merge-overwrite mechanisms (conflict with immutability design)."
speaker: system
tags: [#external-reference, #graphiti, #foam, #schema-upgrade]

---

## event:stress-test
type: event
time: 2026-07-02
summary: "Efficiency stress test: Fact Layer 22,822 chars (45 nodes), Index Layer 6,162 chars. Retrieval saves 71% token (down from 91% at 22 nodes) — index膨胀 is identified bottleneck. At 300+ nodes, parallel retrieval (semantic+keyword+entity multi-path scoring) needed."
speaker: system
tags: [#efficiency, #stress-test, #token-optimization, #index膨胀]
