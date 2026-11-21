# Case-insensitive tracking-loop rejection

## Context

A tracking destination can point back to a tracking endpoint. URL path case differences can hide `/t/` loops.

## Decision

Compare the destination path case-insensitively when rejecting `/t/` destinations.

## Consequences

Regression checks must cover uppercase `/T/` and mixed-case variants without weakening other destination validation.
