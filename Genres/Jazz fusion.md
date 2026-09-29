Jazz fusion is a genre that combines jazz harmony and improvisation with rock, funk, and R&B rhythms, electric instruments, and studio production techniques. It emerged in the late 1960s and peaked in the 1970s with artists like Miles Davis, Weather Report, Herbie Hancock, and Return to Forever.

```dataviewjs
const genre = dv.current().file.name;
const pages = dv.pages('"Artists"')
  .where(p => {
    const g = p.genre;
    if (!g) return false;
    if (Array.isArray(g)) return g.some(x => x === genre);
    return g === genre;
  });
dv.list(pages.file.link);
dv.paragraph(`**${pages.length} artists in this genre**`);
```
