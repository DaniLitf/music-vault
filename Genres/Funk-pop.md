# Funk-pop

**Funk-pop** is a genre blending funk rhythms and grooves with pop song structures and melodies.

```dataviewjs
// Automatically list artists with genre: "Funk-pop" in frontmatter
const genre = "Funk-pop";
const pages = dv.pages(`"Artists"`).where(p => {
  const g = p.genre;
  if (!g) return false;
  return Array.isArray(g) ? g.includes(genre) : g === genre;
});
dv.list(pages.sort(p => p.file.name).map(p => dv.fileLink(p.file.path)));
dv.paragraph(`**${pages.length} artist(s)** listed with genre: **${genre}**`);
```
