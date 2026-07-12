# Shock rock

Shock rock is a genre of rock music that incorporates theatrical, macabre, or provocative elements in live performances, often involving horror imagery, props, and elaborate stage shows. Pioneered by artists like Screaming Lord Sutch and Arthur Brown, the genre was defined by Alice Cooper in the early 1970s and later expanded by acts such as Kiss, Marilyn Manson, and GWAR.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
