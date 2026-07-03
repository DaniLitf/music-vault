# House

A genre of electronic dance music characterized by a repetitive four-on-the-floor beat, synthesized basslines, and soulful vocal samples, originating in early-1980s Chicago clubs and evolving into numerous subgenres including deep house, acid house, and progressive house.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
