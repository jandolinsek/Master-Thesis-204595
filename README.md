# Master-Thesis-204595
Code used to analyse metagenomic and metatranscriptomic reads, to create tables and figures.

## Purpose
This repository contains the analysis code used in the thesis workflow. The goal is to keep the original structure and code while making the project easier to:
- share with supervisors and assessors,
- maintain and update over time,
- annotate consistently (including AI-assisted comments).

## How to use this repository
1. Keep analysis scripts and notebooks in their current locations (do not restructure unless required).
2. Store intermediate and final outputs in clearly named folders (for example by date, dataset, or analysis stage).
3. For each update, describe:
   - what changed,
   - why it changed,
   - which tables/figures are affected.

## Sharing with supervisors and assessors
When sharing a version of this project, include:
- this README,
- a short summary of the analysis run and key results,
- paths to the generated tables and figures.

## Updating guidance
- Prefer small, focused commits.
- Avoid changing code structure unless strictly needed.
- If you modify analysis logic, document assumptions and expected output changes near the edited code.

## AI-assisted commenting guidance
When using AI to add or improve comments, keep comments:
- factual (describe current behavior, not intended behavior),
- concise,
- local to the relevant block/function,
- consistent in style across files.

Use this short template when adding comments:
- **Input:** expected data/parameters
- **Process:** core transformation or analysis step
- **Output:** produced files/objects/metrics
- **Assumptions:** key constraints or biological/statistical assumptions
