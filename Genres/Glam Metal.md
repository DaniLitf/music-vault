# Glam Metal

A commercially-oriented heavy metal subgenre from the 1980s combining flashy visual style with catchy hooks, guitar virtuosity, and power ballads.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
