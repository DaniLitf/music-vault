Groove metal is a subgenre of heavy metal that emphasizes heavy, mid-tempo, syncopated rhythms and groove-focused riffs. It emerged in the early 1990s and is characterized by a thick, down-tuned guitar sound and aggressive yet rhythmic drumming.

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
