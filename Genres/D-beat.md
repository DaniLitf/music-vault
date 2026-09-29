# D-beat

D-beat (also known as D-beat or Discrust) is a hardcore punk subgenre that originated in the early 1980s, named after and pioneered by the English band Discharge. It is characterised by fast, repetitive drum beats (the "D-beat"), heavily distorted guitars, and shouted political lyrics.

```dataviewjs
// Auto-generated: list all artists with this genre
const genre = "D-beat";
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
