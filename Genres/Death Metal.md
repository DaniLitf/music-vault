# Death metal

An extreme heavy metal subgenre that emerged in the mid-1980s, characterised by heavily distorted guitars, deep growling vocals, blast beat drumming, and lyrics focused on violence, death, horror, and the occult.

```dataviewjs
// Auto-generated: list all artists with this genre
const genre = "Death metal";
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
