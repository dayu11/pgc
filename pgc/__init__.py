"""pgc: programmatic, verifiable coding traces with computed decision policies.

Modules
- snapshot:  pinned read-only snapshot; capped deterministic tools (ls, grep, read, symbols)
- analysis:  static analysis of Python modules; the declared resolution semantics
- knowledge: what the agent has seen, parsed into typed facts; partial-knowledge resolver
- policy:    grounded action grammar, cap-aware observation model, contingency search
- render:    prose thoughts from the typed state delta
- runner:    the generate loop; trace format
- verify:    replay, world checks, plan adherence, certificate, calibration
- setter:    task generation with full access; skeletons and quotas
- prior:     count priors fit on held-out repositories
"""
