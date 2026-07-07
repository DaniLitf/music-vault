# Glam metal

Glam metal (also known as hair metal or pop metal) is a subgenre of heavy metal combining the hard rock and heavy metal sound with elements of pop music and an androgynous visual aesthetic inspired by glam rock. It flourished on the Los Angeles Sunset Strip scene in the 1980s.

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
