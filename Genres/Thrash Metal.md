**Thrash metal** is a subgenre of heavy metal music characterized by its aggressive tempo, fast guitar riffing, and high-energy drumming.

```dataviewjs
const genre = "Thrash Metal";
const pages = dv.pages(`"Artists"`).where(p => p.genre && p.genre.includes(genre));
const count = pages.length;

dv.paragraph(`**${count} artist${count !== 1 ? 's' : ''}** tagged with *${genre}*`);

if (count > 0) {
  dv.list(pages.sort(p => p.file.name).map(p => `[[${p.file.path}|${p.file.name}]]`));
}
```
