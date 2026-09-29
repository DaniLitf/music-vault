# Crust punk

Anarchist-influenced punk subgenre that emerged in the mid-1980s, combining hardcore punk with heavy metal elements. Known for its raw, abrasive sound, dual vocalists, and politically charged lyrics.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
