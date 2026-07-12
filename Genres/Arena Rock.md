Arena rock is a style of rock music that emerged in the mid-1970s, characterized by anthemic choruses, heavy guitar riffs, and a larger-than-life sound designed to fill stadiums and arenas.

```dataviewjs
// Copy this section from the genre template directly
const genre = dv.current().file.name;
const artists = dv.pages('#artist').where(p => p.genre && p.genre.includes(genre));
dv.table(["Artist", "Genre"], artists.map(a => [a.file.link, a.genre]));
dv.paragraph(`**Total ${genre} artists: ${artists.length}**`);
```
