# Exospection
[![FlightSpection](https://img.shields.io/badge/Powered%20by-FlightSpection-blue)](https://github.com/sciencedelicmetatech/flightspection)

**The Three External Anchors for Complete Agent Memory Integrity**

Raell's Stack Theorem proves that a complete agent-memory integrity system requires **six independent external anchors**. FlightSpection provides three (write-time, temporal, read-side). Exospection provides the remaining three.

## The Three Services

| Service | Question | Answer Type |
| :--- | :--- | :--- |
| **Authority** | Is this record still approved? | Signed bit (Certificate) |
| **Causal** | Where did this record come from? | Signed trace (Certificate) |
| **Norm** | Is this record allowed here? | Signed policy (Proposer) |

Without these three anchors, the stack is mathematically incomplete. A record can be intact, current, and faithfully delivered and still be revoked, causally misattributed, or contextually inappropriate.

## Architecture
```text
[ L1: Recallspection ]  <- 3 Anchors (AGMI L4)
          |
[ FlightSpection ]      <- The Bridge (Refuses on Tamper)
          |
[ Exospection ]         <- 3 Anchors (This Repo)