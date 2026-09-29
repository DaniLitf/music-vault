# Street punk

Street punk is a working class-based punk subgenre that developed in the late 1970s and early 1980s, characterized by a raw, aggressive sound often incorporating Oi! and hardcore elements.

```dataviewjs
// Auto-generated: list all artists with this genre
const genre = "Street punk";
const pages = dv.pages('"Artists"')
  .where(p => {
    const g = p.genre;
    if (!g) return false;
    if (Array.isArray(g)) return g.includes(genre);
    return g === genre;
  });
dv.list(pages.file.link);
dv.paragraph(`**${pages.length} artists**`);
```
