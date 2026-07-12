# Anarcho-punk

Anarcho-punk (also known as anarchist punk) is a subgenre of punk rock that promotes anarchist politics. It emerged in the late 1970s and early 1980s, particularly in the United Kingdom, with bands like Crass, Conflict, and Subhumans.

```dataviewjs
// Auto-generated: list all artists with this genre
const genre = "Anarcho-punk";
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
