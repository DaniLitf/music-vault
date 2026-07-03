# Thrash Metal

An aggressive, fast-tempo metal subgenre combining the speed and aggression of hardcore punk with the complexity of NWOBHM, pioneered in the early-to-mid 1980s by the American "Big Four" (Metallica, Megadeth, Slayer, Anthrax) and the German "Teutonic" scene (Kreator, Destruction, Sodom).

```dataviewjs
const genre = dv.current().file.name;
const name = p => p.display_name ?? p.file.name;
const pages = dv.pages('"Artists"')
	.where(p => Array.isArray(p.genre) ? p.genre.includes(genre) : p.genre === genre)
	.sort(name);
dv.paragraph(`Bands in the vault with genre **${genre}** (${pages.length}):`);
dv.list(pages.map(p => dv.fileLink(p.file.path, false, name(p))));
```
