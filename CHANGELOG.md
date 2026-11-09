# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-09

First public release.

### Added
- Seven modes: headline, experience, full profile review (skills, Featured, gaps), keyword map,
  Unique Value Proposition, elevator pitch and About section, run together by default.
- Profile audit: metrics that appear only in About, duplicate roles and skills, expired
  certifications, location and title mismatches, thin current role, weak skill tags.
- LinkedIn limits built in: 220-character headline, 2,600-character About (260-word cap),
  2,000 characters per role, 100 skills; Featured accepts posts, articles, links and media only.
- A fill-in loop: placeholders for missing facts, then a clean final version from the user's answers.
- Optional Apply mode for AIs with a signed-in browser: edits one section at a time, keeps
  "Notify network" off, confirms deletions and posts first.
- Three distributions generated from one source: Claude Code skill and agent (plugin), Claude.ai
  skill zip, and a paste-in prompt for ChatGPT, Gemini and others.
- `scripts/build.py` and a CI check that keep the three copies identical.
- `docs/USAGE.md` with ready-to-copy requests for everyday tasks and common situations, and
  `docs/EXAMPLE.md` with a fictional before-and-after.

[1.0.0]: https://github.com/arunmenon1807/linkedin-optimizer/releases/tag/v1.0.0
