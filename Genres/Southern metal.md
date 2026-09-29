Southern metal is a subgenre of heavy metal music that incorporates elements of southern rock, blues rock, and hard rock. It typically features blues-influenced guitar riffs, groovy rhythms, and a raw, organic production style.

```dataviewjs
const genre = dv.current().file.name;
const artists = dv.pages('"Artists"')
  .where(p => p.genre && p.genre.some(g => g.path ? g.path.includes(genre) : g === genre));

dv.paragraph(`**${artists.length} artist(s) with the genre "${genre}"**`);

if (artists.length > 0) {
  dv.table(["Artist", "Genres"],
    artists.sort(p => p.file.name)
      .map(p => [p.file.link, p.genre])
  );
}
```
