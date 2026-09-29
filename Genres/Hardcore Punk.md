# Hardcore punk

Hardcore punk (often abbreviated as hardcore) is a punk rock music genre and subculture that originated in the late 1970s. It is generally faster, harder, and more aggressive than other forms of punk rock.

```dataviewjs
// Auto-generated: list all artists with this genre
const genre = "Hardcore punk";
const pages = dv.pages('"Artists"')
  .where(p => {
    const g = p.genre;
    if (!g) return false;
    if (Array.isArray(g)) return g.includes(genre);
    return g === genre;
  });
dv.list(pages.file.link);
dv.paragraph(`**${pages.length} artists**`);
```
