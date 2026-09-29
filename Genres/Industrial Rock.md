# Industrial Rock

A fusion genre that combines industrial music's mechanical and electronic elements with rock instrumentation and song structures. Emerged in the late 1980s with bands like Ministry, Nine Inch Nails, and KMFDM, blending distorted guitars with synthesizers, samples, and aggressive rhythms.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
