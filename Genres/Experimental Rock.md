Experimental rock is a subgenre of rock music that pushes the boundaries of conventional composition, instrumentation, and song structure, often incorporating elements from diverse musical traditions and avant-garde techniques.

```dataviewjs
// Copy this section from the genre template directly
const genre = dv.current().file.name;
const artists = dv.pages('#artist').where(p => p.genre && p.genre.includes(genre));
dv.table(["Artist", "Genre"], artists.map(a => [a.file.link, a.genre]));
dv.paragraph(`**Total ${genre} artists: ${artists.length}**`);
```
