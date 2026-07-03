# Industrial

A genre of music that draws on harsh, mechanical, and transgressive themes, emerging from the late 1970s post-punk and experimental scenes. Characterised by repetitive rhythms, distorted sounds, tape loops, and provocative aesthetics, pioneered by artists like Throbbing Gristle and Cabaret Voltaire.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
