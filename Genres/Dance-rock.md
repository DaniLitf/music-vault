# Dance-rock

**Dance-rock** is a genre blending rock music with dance beats, often incorporating funk and disco influences.

```dataviewjs
// Automatically list artists with genre: "Dance-rock" in frontmatter
const genre = "Dance-rock";
const pages = dv.pages(`"Artists"`).where(p => {
  const g = p.genre;
  if (!g) return false;
  return Array.isArray(g) ? g.includes(genre) : g === genre;
});
dv.list(pages.sort(p => p.file.name).map(p => dv.fileLink(p.file.path)));
dv.paragraph(`**${pages.length} artist(s)** listed with genre: **${genre}**`);
```
