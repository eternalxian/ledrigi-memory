# Memory System · Index Layer
# Rebuildable, overridable. version: 1

## Timeline

2026-06-11  event:design-init
2026-06-11  event:three-layer-arch
2026-06-11  event:multi-round-review
2026-06-11  event:ownership-declared
2026-06-11  event:schema-v06
2026-06-11  event:retrieval-test
2026-06-12  event:design-deprecated
2026-06-12  event:first-selfcheck
2026-06-12  event:external-reference
2026-07-02  event:stress-test

## Weight Ranking

importance:5
  event:ownership-declared
  event:three-layer-arch

importance:4
  event:multi-round-review
  event:schema-v06
  event:design-init

## Concept Mapping

architecture:
  children: [event:design-init, event:three-layer-arch, event:schema-v06]

data-integrity:
  children: [event:ownership-declared]

iteration-testing:
  children: [event:multi-round-review, event:retrieval-test, event:stress-test]

deprecated:
  children: [event:design-deprecated]

maintenance:
  children: [event:first-selfcheck, event:external-reference]

## Aliases

architecture -> event:three-layer-arch
schema -> event:schema-v06
ownership -> event:ownership-declared
testing -> event:retrieval-test
efficiency -> event:stress-test
token -> event:stress-test
deprecated -> event:design-deprecated
reference -> event:external-reference
dual-temporal -> event:external-reference
design -> event:design-init
review -> event:multi-round-review
selfcheck -> event:first-selfcheck
