**Power metal** is a subgenre of heavy metal music typically combining traditional metal with melodic, anthemic vocals and fantasy-themed lyrics.

```dataviewjs
const genre = "Power Metal";
const pages = dv.pages(`"Artists"`).where(p => p.genre && p.genre.includes(genre));
const count = pages.length;

dv.paragraph(`**${count} artist${count !== 1 ? 's' : ''}** tagged with *${genre}*`);

if (count > 0) {
  dv.list(pages.sort(p => p.file.name).map(p => `[[${p.file.path}|${p.file.name}]]`));
}
```
