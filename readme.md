# About This Vault

## Purpose

This vault exists to map connections between musicians by tracing who played with whom across bands, projects, and collaborations. Every artist page lists its members; every member page lists their associated artists. Discography tables link albums to their producers and recording studios. Together these form a dense network graph of musical relationships, visible in Obsidian's Graph View.

**Primary goal:** Discover links between artists through shared members, collaborations, producers, and studios.

**Secondary goal:** Find new bands through genres. Each genre page gathers every artist tagged with that genre, making it easy to explore similar music.

All conventions, workflows, and quality rules for maintaining the vault live in [[CLAUDE]] — AI agents load it automatically; humans can read it there too.

---

## Folder Structure

```
music-vault/
├── Artists/          # Band and solo artist pages
│   ├── A/ … Z/      # Subfolders by first letter of page name
│   └── 0-9/         # Names starting with a digit
├── Members/          # Individual musician pages
│   ├── A/ … Z/      # Same subfolder convention
│   └── 0-9/
├── Producers/        # Record producer pages
│   ├── A/ … Z/      # Same subfolder convention
│   └── 0-9/
├── Studios/          # Recording studio pages
│   ├── A/ … Z/      # Same subfolder convention
│   └── 0-9/
├── Genres/           # Genre listing pages (flat, no subfolders)
├── Templates/        # Page templates for AI agent use
├── about.md          # This file
├── CLAUDE.md         # Agent instructions: conventions, workflows, checklists
├── Index.md          # Root index with counts
├── incomming.md      # Inbox for raw artist/member/producer/studio names
└── progress.md       # Artist, member, and producer progress checklists
```

---

## Graph View Tips

- **Filter by folder:** In the Filters panel, use `path:Producers/`, `path:Studios/`, or `path:Members/` to toggle those node types on or off without removing them from the vault.
- **Colour by folder:** In the Groups panel, create a group per folder path and assign each a distinct colour (e.g. Artists = blue, Members = green, Producers = orange, Studios = purple).
- **Find hubs:** Producers or studios that appear as highly-connected nodes reveal artists who share a sonic lineage even when they share no members.
