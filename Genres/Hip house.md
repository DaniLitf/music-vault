# Hip house

Hip house (also called house rap) is a musical genre that fuses the rhythms and production styles of house music with the vocal delivery and song structures of hip-hop, emerging in the late 1980s. It typically features rapped verses over four-on-the-floor house beats.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
