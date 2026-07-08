# Minneapolis sound

A subgenre of funk rock that emerged from the Minneapolis music scene in the late 1970s and early 1980s, characterized by its fusion of funk, R&B, new wave, synth-pop, and dance music. The sound was pioneered by Prince and his associates, most notably The Time, Jimmy Jam and Terry Lewis.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
