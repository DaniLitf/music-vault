**Speed metal** is a subgenre of heavy metal music that emerged in the early 1980s, characterized by fast tempos, aggressive riffing, and an emphasis on speed.

```dataviewjs
const genre = "Speed Metal";
const pages = dv.pages(`"Artists"`).where(p => p.genre && p.genre.includes(genre));
const count = pages.length;

dv.paragraph(`**${count} artist${count !== 1 ? 's' : ''}** tagged with *${genre}*`);

if (count > 0) {
  dv.list(pages.sort(p => p.file.name).map(p => `[[${p.file.path}|${p.file.name}]]`));
}
```
