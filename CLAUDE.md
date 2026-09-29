# Agent Instructions

Operating manual for AI agents working in this vault. For the vault's purpose and how to browse it, see [[readme]].

---

## Core Conventions

Read this section before starting any work. These rules apply across all workflows.

### Subfolder Convention

All artist, member, producer, and studio pages go under a single-letter subfolder matching the first character of the page title, uppercase.

| First character | Subfolder | Example path |
|---|---|---|
| A–Z | Same letter | `Artists/A/AFX.md`, `Members/K/Kanye West.md` |
| 0–9 | `0-9/` | `Artists/0-9/12 Rounds.md` |
| Accented (Å, Ö, etc.) | Base Latin letter | `Members/A/Joakim Åhlund.md` (Å → A) |
| Other symbols | `0-9/` | — |

Wikilinks must always include the subfolder:
- `[[Artists/A/Aphex Twin]]` — not `[[Artists/Aphex Twin]]`
- `[[Members/R/Richard D. James]]` — not `[[Members/Richard D. James]]`
- `[[Producers/R/Rick Rubin]]` — not `[[Producers/Rick Rubin]]`
- `[[Studios/A/Abbey Road Studios]]` — not `[[Studios/Abbey Road Studios]]`

Genre pages stay flat in `Genres/` (no subfolders).

### Aliases vs Name Changes (One Page Per Name)

**Name change (same entity, rebranding):** One artist page. List former names in `also_known_as:`.
- Drain → Drain S.T.H. → one page: `Artists/D/Drain S.T.H.md` with `also_known_as: Drain`
- Caesars Palace → Caesars → one page: `Artists/C/Caesars.md` with `also_known_as: Caesars Palace, Twelve Caesars`

**Parallel alias (different creative projects, same person):** Separate artist page per alias.
- Aphex Twin, AFX, Polygon Window, Caustic Window → four pages, each in `Artists/`
- The shared member page (`Members/R/Richard D. James.md`) is the hub — it lists all aliases in `also_known_as:` and links to them via `## Associated Artists`

**Rule of thumb:** Same timeline, same discography, same members? → one page with `also_known_as:`. Separate discographies for different styles under the same person? → separate artist pages.

#### Solo Artist / Alias Page Setup

**Single identity (e.g. Kleerup):**
1. Create `Artists/K/Kleerup.md`
2. Create `Members/K/Kleerup.md`
3. On the artist page, Members section says: `{Artist} is a solo artist. See [[Members/K/Kleerup]] for biography.`
4. The member page links back via `## Associated Artists`

**Multiple aliases (e.g. Aphex Twin + AFX + Polygon Window):**
1. Create one `Members/R/Richard D. James.md` — this is the hub
2. Create one artist page per alias: `Artists/A/Aphex Twin.md`, `Artists/A/AFX.md`, etc.
3. On each alias artist page, Members section lists: `[[Members/R/Richard D. James]] – alias`
4. Alias artist pages keep Connections minimal; all real collaborations go on the member page
5. The member page's `## Associated Artists` lists every alias AND every band/project the person played with

### Core Rule: Get ALL Members

**Every single name listed in a band's Members section gets its own `Members/` page.** No exceptions. The whole purpose of this vault is connections — a plain-text name is invisible to the graph. Converting it to `[[Members/N/Name]]` creates the link. This applies to:

- Current and past members
- Touring musicians and session contributors
- Notable guests
- Anyone explicitly listed as playing with the band

If a band has 50+ contributors, create all 50+ member pages. Each page can be brief (2+ sentences) but must exist.

### Frontmatter Conventions

- **All frontmatter keys use underscores** (`real_name:`, `also_known_as:`, `birth_date:`, `death_date:`) — never spaces
- `also_known_as:` on **artist pages**: name changes only (see Aliases vs Name Changes above). On **member pages**: all stage names, pseudonyms, and aliases. Never list the birth name here — that goes in `real_name:`
- `real_name:` contains the musician's legal birth name. If the page title is already the birth name, leave this empty
- Genres: capitalised, match the exact genre page name (e.g. `Trip hop` not `trip-hop`). Genre names are case-sensitive
- Dates: `YYYY-MM-DD` format (use `YYYY` if only year is known)
- `nationality:` uses demonyms (American, British, Swedish, Ukrainian)
- Death dates: add to existing member pages when discovered
- `display_name:` — optional key on artist pages, set only when the true name can't be used as a filename (e.g. `AC/DC`, `R.E.M.`); Dataview listings (Index, genre pages) display it instead of the filename.

---

## Templates

Templates live in `Templates/`. **[[Artists/P/Pigface.md]] is the canonical reference for a fully quality-checked artist page** regarding members and connections — use it as the model when creating or refining any artist page.

**Artist page** (`Templates/artist-template.md`):
- YAML frontmatter: `genre:` list (capitalised), `also_known_as:` per the alias rules above, optional `display_name:`, optional `festivals:` commented out
- Bold summary line: `**Genre / style from City, Country. Active YEAR–present.**`
- Short description paragraph (2-3 sentences)
- `## Discography` with sub-sections for every release type: `### Studio Albums`, `### EPs`, `### Singles`, `### Live Albums`, `### Compilations`, `### Remix Albums`, `### Splits` — include all known releases
- `## Members` section — ALL members as `[[Members/N/Name]]` wiki links with role and years. Categorize into: `### Core / Official Members`, `### Current Touring Band`, `### Past Touring & Session Members`, `### Notable Guests`
- `## Connections` — **every line must explain which shared member(s) create the link.** Format: `- [[Artists/B/Band Name]] – Member Name (explanation)`. For multi-member connections: `- [[Artists/B/Band Name]] – Member1, Member2 (explanation)`
- `## Sources` — at least Wikipedia + one more source
- Solo artist pattern: `{Artist} is a solo artist. See [[Members/N/Name]] for biography.`

**Member page** (`Templates/member-template.md`):
- YAML frontmatter: `real_name:`, `also_known_as:`, `birth_date: YYYY-MM-DD`, `death_date: YYYY-MM-DD`, `nationality:`
- Bold summary line: `**Role. Born DATE.**`
- 2-3 sentence biography covering career and notable contributions
- `## Associated Artists` — bullet list of `[[Artists/B/Band]] – role (years)`. For a solo musician with multiple aliases, list each alias here
- `## Biography` section (optional, for extended text)
- `## Sources` — at least Wikipedia

**Producer page** (`Templates/producer-template.md`):
- YAML frontmatter: `real_name:`, `also_known_as:`, `birth_date:`, `death_date:`, `nationality:`
- Bold summary line: `**Record producer. NATIONALITY.**`
- 2-3 sentence biography covering style, signature productions, and significance
- `## Associated Projects` — bullet list of `[[Artists/X/Name]] – *Album Title* (YEAR)` for every vault album they produced
- `## Sources` — at least Wikipedia
- If the producer is also a musician, they may also have a `Members/` page — link to it in the bio

**Studio page** (`Templates/studio-template.md`):
- YAML frontmatter: `location:` (City, Country), `active_years:` (YYYY–present or YYYY–YYYY)
- Bold summary line: `**Recording studio. CITY, COUNTRY.**`
- 2-3 sentence description covering history, notable equipment/acoustics, and cultural significance
- `## Albums Recorded Here` — bullet list of `[[Artists/X/Name]] – *Album Title* (YEAR)` for every vault album recorded there
- `## Sources` — at least Wikipedia

**Genre page** (`Templates/genre-template.md`):
- One-line description of the genre
- A standard `dataviewjs` block (copy it verbatim from the template) that automatically lists and counts all artists whose `genre:` frontmatter matches the page's filename — never write a manual artist list or count
- No YAML frontmatter needed. When creating a new genre page, the filename must exactly match the genre name used in artist frontmatter (case-sensitive); the list and count then maintain themselves

---

## Workflows

### Workflow 1: New Artist

**This workflow applies every time a new artist is added, regardless of source.**

1. **Take the next artist** — from the `## Artists` section of `progress.md` in alphabetical order (skip entries marked `[x]`), from `incomming.md`, or named directly by the user.
2. **Research** — open Wikipedia, fetch the full page, note members, discography, genres, notable events. Cross-reference at least one more source (AllMusic, Discogs, Bandcamp, official site).
3. **Check individual members** — for obscure members, search AllMusic, Discogs, and Bandcamp separately.
4. **Create all pages** — artist, member (ALL of them), and any new genre pages needed. Place each in the correct letter subfolder per the Subfolder Convention.
5. **For every album in the discography:**
   - Check if a producer page exists; create or update it.
   - Check if a studio page exists; create it as a stub if missing, or update it. Studios are **not** queued — they are only deepened via the manually-triggered Workflow 5.
6. **Check connections** — for every band linked in `## Connections` or in a member's `## Associated Artists`, check if it is in `progress.md`. If missing, add it to the `## Artists` section (see Queue Entry Format below).
7. **Add all members encountered** to the `## Members` section of `progress.md` if not already listed. Use a single shared batch stamp for all items added in this run (see Queue Entry Format). Inline-created member pages are stubs — their queue entry stays **unchecked** until processed via Workflow 2.
8. **Add all producers encountered** to the `## Producers` section of `progress.md` if not already listed, using the same batch stamp. Inline-created producer pages are stubs — their queue entry stays **unchecked** until processed via Workflow 3.
9. **Genre pages are created inline only** — they are never queued.
10. **Update the `last updated` / unfixed count in `progress.md`.** Do not add totals, summaries, or page counts to `progress.md` — `Index.md` computes those automatically via Dataview and must not be edited.
11. **Mark the artist as complete** in `progress.md`.

### Workflow 2: New Member

**This workflow applies every time a new member is processed.**

1. **Pick the next unchecked member** from the `## Members` section of `progress.md`, oldest batch first. Skip entries marked `[x]`.
2. **Research** — open Wikipedia, AllMusic, Discogs; note full name, birth date, nationality, all bands and projects they have been part of.
3. **Create or update the member page** in the correct `Members/` subfolder, matching the member template (frontmatter, bold summary line, 2+ sentence biography).
4. **Build or update `## Associated Artists`** — every band and project links to an artist page with role and years.
5. **For every artist linked in `## Associated Artists`:**
   - If the artist page exists: update its `## Members` section to include this member in the correct category (core, touring, session, or guest).
   - If the artist page does not exist: add it to the `## Artists` section of `progress.md`, **unchecked** (see Queue Entry Format).
6. **Run the Member quality gate checklist**, then mark the member as complete in `progress.md`.

### Workflow 3: New Producer

**This workflow applies every time a new producer is processed.**

1. **Pick the next unchecked producer** from the `## Producers` section of `progress.md`, oldest batch first. Skip entries marked `[x]`.
2. **Research** — open Wikipedia, AllMusic, Discogs; note full name, birth date, nationality, all albums and artists they have worked with.
3. **Create or update the producer page** in the correct `Producers/` subfolder, matching the producer template (frontmatter, bold summary line, 2+ sentence biography).
4. **Build or update `## Associated Projects`** — every album links to an artist page with album title and year.
5. **For every artist linked in `## Associated Projects`:**
   - If the artist page exists: update its discography table to include this producer in the Producer column.
   - If the artist page does not exist: add it to the `## Artists` section of `progress.md`, **unchecked**, with a batch stamp (see Queue Entry Format).
6. **If the producer is also a musician:** verify a `Members/` page exists and link to it from the bio. Add to `## Members` in `progress.md` (**unchecked**, batch-stamped) if not already listed.
7. **Run the Producer quality gate checklist**, then mark the producer as complete in `progress.md`.

### Workflow 4: Quality Check (QC)

**Run this workflow to verify and refine existing artist pages against the canonical template ([[Artists/P/Pigface.md]]).**

0. **Sort the `## Artists` table** in `progress.md` alphabetically by path (fold appended rows at the bottom into place). Do this once at the start of a QC run, not per page. `## Members` and `## Producers` are batch-ordered and are never re-sorted.
1. **Resume from the `last QC position`** recorded in the `## Artists` header of `progress.md`, or wherever the user directs. This is a separate cursor from the batch-stamped Members/Producers queues — it tracks alphabetical QC progress specifically. After finishing a page, advance the cursor to the next path in alphabetical order, whether or not the page needed fixes.
2. **Read the current artist page** and compare against the canonical template: frontmatter (`genre:` list, capitalised), bold summary line (genre/location/active-years pattern), discography tables for every release type, and Members section categorised into core/official, current touring, past touring/session, and notable guests.
3. **For every member in the Members section:**
   - Verify a member page exists and is up to date; create if missing and add to `## Members` in `progress.md` (**unchecked**, batch-stamped).
   - Verify the member page links back to this artist in `## Associated Artists`; update if missing.
   - Verify this member appears in the correct member category on the artist page.
4. **Rebuild or add the Connections section** — every line links to another artist page and explains which shared member(s) create the link. Format: `- [[Artists/B/Band Name]] – Member Name (explanation)`.
5. **For every album in the discography:**
   - Verify a producer page exists and is up to date; create if missing and add to `## Producers` in `progress.md` (**unchecked**, batch-stamped).
   - Verify the producer page lists this album in `## Associated Projects`; update if missing.
   - Verify a studio page exists; create it as a stub if missing. Studios are **not** queued.
   - Verify the studio page lists this album in `## Albums Recorded Here`; update if missing.
6. **Verify every genre** in the frontmatter has a corresponding genre page; create any missing genre pages inline (genres are never queued). Genre pages list artists automatically via Dataview — just verify the frontmatter genre name exactly matches the genre page filename.
7. **Verify Sources section** exists with at least Wikipedia plus one more source.
8. **Run the Artist quality gate checklist**, then mark the artist as complete in `progress.md`.

### Workflow 5: New Studio (Manual Trigger Only)

**This workflow is NEVER run automatically. Studios are created as stubs during the artist and QC workflows but are only deepened when the user explicitly asks to process a studio (or studios). There is no studio queue in `progress.md`.**

1. **Take the studio named by the user** (or, if the user asks to process all studios, iterate over existing stub pages in `Studios/`).
2. **Research** — open Wikipedia, official site, AllMusic, Discogs; note location, active years, history, notable equipment/acoustics, and significant recordings.
3. **Create or update the studio page** in the correct `Studios/` subfolder, matching the studio template (frontmatter, bold summary line, 2+ sentence description).
4. **Build or update `## Albums Recorded Here`** — every vault album links to its artist page with title and year.
5. **For every artist linked:** verify the album's discography row on the artist page lists this studio in the Studio column; update if missing.
6. **Run the Studio quality gate checklist.**

---

## Handling incomming.md

`incomming.md` is a lightweight inbox. The user drops raw artist, member, producer, or studio names into the matching section, one per line, with no formatting or research — that's the agent's job during processing.

**When told to "handle incomming" (or "handle the incoming queue"):**

1. Work through the file **one item at a time** — never batch-process several entries in parallel.
2. Process the `## Artists` section first, top to bottom, running each name through **Workflow 1: New Artist**. Remove the line once its workflow completes.
3. Once `## Artists` is empty, process `## Members`, running each through **Workflow 2: New Member**.
4. Once `## Members` is empty, process `## Producers`, running each through **Workflow 3: New Producer**.
5. **Stop before touching `## Studios`.** Studio pages are only deepened via Workflow 5 (manual-trigger only) — ask the user for confirmation before creating or updating any studio page from this section.

If a name already has a page in the vault (as an artist, member, or producer page), that's not a skip — it means the existing page needs updating. Run the same workflow against the existing page (treat it like a QC pass: verify frontmatter, biography, links, discography, etc. are current), then remove the line. Never create a duplicate page, and never remove a line without either creating or updating the corresponding page.

---

## progress.md Structure

`progress.md` has three queues, but they are not identical in format: `## Artists` is a **status table** (existing artists get QC'd in place, so each row needs a path and a free-text issue list, not just a checkbox), while `## Members` and `## Producers` are **checkbox lists** (new members/producers are discrete, one-shot additions with a clear source and batch). (Studios and genres are never queued — see Workflows 1 and 5.) `progress.md` tracks **work status only** — total page counts live in `Index.md`, not here.

The Artists queue looks like:

```
## Artists

> last updated: 2026-07-01T00:00 · unfixed: 18 · last QC position: A/All Ends

| Status | Path | Issues |
|--------|------|--------|
| [x] | A/ACDC | - |
| [ ] | P/Pink Floyd | connections |
```

`last QC position` is the path Workflow 4 will resume from next. A row's `[x]` reflects the checks performed during its most recent pass — not a permanent guarantee. Structural criteria can drift (new checks get added, templates change), so treat old `[x]` marks as provisional and periodically re-run a full-corpus structural scan (as documented in `progress.md`'s Issue Breakdown) rather than trusting them indefinitely.

The Members and Producers queues each start with a status line showing when it was last touched and how many entries remain unchecked, followed by checkbox entries:

```
## Members
> last updated: 2026-06-30T14:32 · unfixed: 12

- [ ] Member Name (batch: 2026-06-30T14:32, from: [[Artists/D/Drain S.T.H]])
- [x] Other Member (batch: 2026-06-28T09:10, from: [[Artists/P/Pigface]])
```

### Queue Entry Format

Every Members/Producers queue entry follows:

```
- [ ] {Name} (batch: {YYYY-MM-DDTHH:MM}, from: {source page or "manual"})
```

- **batch** — a single shared timestamp applied to every item added in one workflow run. All members and producers discovered while processing one artist share that artist's batch stamp. This groups additions so they can be processed together and traced back to their origin.
- **from** — the page that caused this entry to be added, or `manual` if the user added it directly.
- New entries are **always unchecked** (`[ ]`). Mark `[x]` only after the item has been fully processed via its own workflow.
- **Append, don't sort:** new entries always go at the **end of their section** — never insert alphabetically. This keeps additions cheap. Sorting is a separate maintenance step done at the start of a QC run (see Workflow 4 and Running the Queue).

The Artists queue uses its own row format instead: `| [ ] or [x] | {subfolder}/{Name} | {issue codes, comma-separated, or "-"} |`. A row is added the same way — unchecked, with the correct subfolder path, **appended as the last row of the table** — whenever a workflow discovers an artist not already listed.

### Running the Queue

- **Ordering:** `## Members` and `## Producers` are processed **oldest batch first** (ascending batch timestamp), then alphabetically within a batch. This keeps the vault breadth-first and prevents newer discoveries from starving older ones. Since new entries are appended, file order already approximates batch order — no re-sorting needed. The `## Artists` table has no batch stamps — it is processed **alphabetically by path**, even though appended rows may sit unsorted at the bottom of the table between QC runs.
- **"Run queue" (general):** process all sections using the ordering above.
- **"Run {queue} queue":** restrict to one section (e.g. only `## Members`).
- After processing any item, update that queue's `last updated` timestamp and decrement its `unfixed` count.

When any workflow discovers a new artist, member, or producer not already listed, add it to the correct queue (unchecked, batch-stamped) before continuing. Never remove entries — only mark them complete.

---

## Research Standards

- Open Wikipedia and read the full article. For non-English artists, use the native-language Wikipedia (e.g. sv.wikipedia.org, fr.wikipedia.org, de.wikipedia.org) and cross-reference with Last.fm, Discogs, or Metal Archives
- Cross-reference at least two sources for member lists — Wikipedia member sections are often incomplete
- For birth dates: Wikipedia infoboxes are the first stop; if missing, try AllMusic or Discogs artist pages
- For obscure members: search AllMusic, Discogs, and Bandcamp individually — a member who doesn't appear in Wikipedia may have a full AllMusic page
- For touring/session members: band official sites and live setlist archives (setlist.fm) often have more complete rosters than Wikipedia
- Record every source used in the `## Sources` section, not just Wikipedia

---

## Quality Gate Checklists

Use these as a final scan before marking work complete.

### Artist (Workflows 1 and 4)
- [ ] Artist page has `## Sources` with actual citations
- [ ] Every member has a page (no plaintext names in Members section)
- [ ] Every member bio is at least 2 sentences
- [ ] Member pages use standard frontmatter (`real_name:`, `also_known_as:`, `birth_date:`, `death_date:`, `nationality:`)
- [ ] Every member page links back to this artist in `## Associated Artists`
- [ ] Producer pages exist for every producer linked in discography tables
- [ ] Every producer page lists the relevant album in `## Associated Projects`
- [ ] Studio pages exist (at least as stubs) for every studio linked in discography tables
- [ ] Every studio page lists the relevant album in `## Albums Recorded Here`
- [ ] Genre pages exist for every genre in frontmatter (exact, case-sensitive filename match — lists/counts are automated via Dataview)
- [ ] Connections section exists and every line explains which shared member(s) create the link
- [ ] New members added to `## Members` in `progress.md` (unchecked, batch-stamped)
- [ ] New producers added to `## Producers` in `progress.md` (unchecked, batch-stamped)
- [ ] New artists discovered added to `## Artists` in `progress.md` (unchecked, batch-stamped)
- [ ] `progress.md` queue `last updated` / unfixed counts updated
- [ ] Artist marked complete in `progress.md`

### Member (Workflow 2)
- [ ] Member page exists in correct `Members/` subfolder
- [ ] YAML frontmatter has `real_name:`, `also_known_as:`, `birth_date:`, `death_date:`, `nationality:`
- [ ] Bold summary line follows role/born-date pattern
- [ ] Biography is at least 2 sentences
- [ ] `## Associated Artists` lists all known bands and projects as wikilinks
- [ ] Every linked artist page has been updated to include this member in the correct category
- [ ] Missing artist pages added to `## Artists` in `progress.md`
- [ ] Member marked complete in `progress.md`

### Producer (Workflow 3)
- [ ] Producer page exists in correct `Producers/` subfolder
- [ ] YAML frontmatter has `real_name:`, `also_known_as:`, `birth_date:`, `death_date:`, `nationality:`
- [ ] Bold summary line follows record producer/nationality pattern
- [ ] Biography is at least 2 sentences
- [ ] `## Associated Projects` lists all vault albums as wikilinks with title and year
- [ ] Every linked artist page has been updated with this producer in the discography table
- [ ] Missing artist pages added to `## Artists` in `progress.md`
- [ ] If also a musician: `Members/` page exists and is linked from bio; added to `## Members` in `progress.md` (unchecked, batch-stamped)
- [ ] Producer marked complete in `progress.md`

### Studio (Workflow 5 — manual only)
- [ ] Studio page exists in correct `Studios/` subfolder
- [ ] YAML frontmatter has `location:` and `active_years:`
- [ ] Bold summary line follows recording studio/city-country pattern
- [ ] Description is at least 2 sentences
- [ ] `## Albums Recorded Here` lists all vault albums as wikilinks with title and year
- [ ] Every linked artist page lists this studio in the relevant discography row

---

## Vault Statistics

`Index.md` is **fully automated via Dataview** — it computes all page-type counts (Artists, Members, Producers, Studios, Genres, and the total) and renders the alphabetical artist list live. **Never edit `Index.md`**; new pages appear in it automatically when created in the correct folder.

`progress.md` tracks only work status (last-updated timestamp and unfixed count per queue), never totals.
