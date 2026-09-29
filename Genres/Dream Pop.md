Dream pop is a subgenre of alternative rock and indie rock that emphasizes atmospheric soundscapes, ethereal vocals, and lush, textural instrumentation.

```dataviewjs
// Copy this section from the genre template directly
const genre = dv.current().file.name;
const artists = dv.pages('#artist').where(p => p.genre && p.genre.includes(genre));
dv.table(["Artist", "Genre"], artists.map(a => [a.file.link, a.genre]));
dv.paragraph(`**Total ${genre} artists: ${artists.length}**`);
```
