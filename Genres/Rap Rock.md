A fusion of rap and rock music combining hip-hop rhythms and beats with rock instrumentation and songwriting.

```dataviewjs
const artists = dv.pages('"Artists"')
  .where(p => p.genre && p.genre.includes('Rap Rock'));
const count = artists.length;

dv.header(2, `${count} Artist${count === 1 ? '' : 's'}`);
dv.list(artists.sort(a => a.file.name).map(a => dv.fileLink(a.file.name, false, a.display_name || a.file.name)));
```
