# Futurepop

**Futurepop** is a genre that emerged in the late 1990s, blending elements of synthpop, EBM, and electronic dance music with uplifting melodies, emotional vocals, and polished production.

```dataviewjs
// Automatically list artists with genre: "Futurepop" in frontmatter
const genre = "Futurepop";
const pages = dv.pages(`"Artists"`).where(p => {
  const g = p.genre;
  if (!g) return false;
  return Array.isArray(g) ? g.includes(genre) : g === genre;
});
dv.list(pages.sort(p => p.file.name).map(p => dv.fileLink(p.file.path)));
dv.paragraph(`**${pages.length} artist(s)** listed with genre: **${genre}**`);
```
