# HackUTD 2026 Expert Kit (drop-in)

Copy everything in this folder into the ROOT of the hackathon repo:

    cp -R ~/Documents/HackUTD-2026-Kit/. ~/path/to/your-repo/

That adds:
- CLAUDE.md / AGENTS.md  the always-loaded cheat sheet (Claude Code / other agent tools)
- decisions/             10 decision guides (the cheat sheet routes agents here)
- domains/               21 deeper references
- agents/ and .claude/agents/judge-critic.md   the skeptical-judge reviewer agent

If the repo already has a CLAUDE.md, paste this one's content into it instead of overwriting.
Fill in section 6 "Event specifics" of CLAUDE.md (and AGENTS.md) with sponsor tracks and deadlines.
Everything here is written in our own words and safe for a public repo.

Optional search tool (works on this Mac only; the book database stays private):
    claude mcp add expert-library -- ~/Documents/HackUTD-2026-Expert-KB/.venv/bin/python -I ~/Documents/HackUTD-2026-Expert-KB/kb/search/search.py --mcp
