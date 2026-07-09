A genre of music that originated in Jamaica in the late 1960s, characterised by a distinctive rhythm style marked by offbeat accents, syncopated bass lines, and themes of spirituality, social justice, and love.

```dataviewjs
// Group artists by genre, then count and list them
const genre = dv.current().file.name;
const pages = dv.pages('"Artists"')
  .where(p => {
    const g = p.genre;
    if (!g) return false;
    if (Array.isArray(g)) return g.includes(genre);
    return g === genre;
  })
  .sort(p => p.file.name);

dv.paragraph(`**Artists in genre: ${pages.length}**`);

if (pages.length > 0) {
  // Group by first-letter subfolder
  const grouped = {};
  for (const p of pages) {
    const pathParts = p.file.path.split('/');
    const subfolder = (pathParts.length >= 3) ? pathParts[1] : '?';
    if (!grouped[subfolder]) grouped[subfolder] = [];
    grouped[subfolder].push(p.file.link);
  }

  for (const letter of Object.keys(grouped).sort()) {
    dv.header(3, letter);
    dv.list(grouped[letter].sort((a, b) => {
      const nameA = (a.display || a.path || '').toString();
      const nameB = (b.display || b.path || '').toString();
      return nameA.localeCompare(nameB);
    }));
  }
}
```
