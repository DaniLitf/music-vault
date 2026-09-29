# Death metal

**Death metal** is an extreme subgenre of heavy metal music that typically employs heavily distorted guitars, tremolo picking, deep growling vocals, blast beat drumming, and complex song structures.

```dataviewjs
// Automatically list artists with genre: "Death metal" in frontmatter
const genre = "Death metal";
const pages = dv.pages(`"Artists"`).where(p => {
  const g = p.genre;
  if (!g) return false;
  return Array.isArray(g) ? g.includes(genre) : g === genre;
});
dv.list(pages.sort(p => p.file.name).map(p => dv.fileLink(p.file.path)));
dv.paragraph(`**${pages.length} artist(s)** listed with genre: **${genre}**`);
```
