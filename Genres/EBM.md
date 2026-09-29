# EBM

**Electronic body music (EBM)** is a genre that blends industrial music with electronic dance music, characterized by repetitive basslines, programmed drum machines, and shouted or distorted vocals.

```dataviewjs
// Automatically list artists with genre: "EBM" in frontmatter
const genre = "EBM";
const pages = dv.pages(`"Artists"`).where(p => {
  const g = p.genre;
  if (!g) return false;
  return Array.isArray(g) ? g.includes(genre) : g === genre;
});
dv.list(pages.sort(p => p.file.name).map(p => dv.fileLink(p.file.path)));
dv.paragraph(`**${pages.length} artist(s)** listed with genre: **${genre}**`);
```
