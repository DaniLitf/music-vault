# Extreme metal

Extreme metal encompasses aggressive, fast, and distorted forms of heavy metal including subgenres like death metal, grindcore, black metal, and thrash metal.

```dataviewjs
const artists = dv.pages('"Artists"')
  .where(p => p.genre && p.genre.includes('Extreme metal'));
dv.table(["Artist", "Genres"], 
  artists.map(p => [
    p.file.link(),
    p.genre.join(', ')
  ]));
dv.paragraph(`**Total: ${artists.length} artists**`);
```
