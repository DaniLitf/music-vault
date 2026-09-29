# Music Vault

An Obsidian vault mapping musicians' networks — with genre tagging for easy searching.

```dataviewjs
const c = f => dv.pages('"' + f + '"').length;
const a = c("Artists"), m = c("Members"), p = c("Producers"), s = c("Studios"), g = c("Genres");
dv.paragraph(`**Total:** ${a} artists + ${m} members + ${p} producers + ${s} studios + ${g} genres = ${a + m + p + s + g} pages`);
```

---

## All Artists

```dataview
LIST WITHOUT ID link(file.path, default(display_name, file.name))
FROM "Artists"
SORT default(display_name, file.name) ASC
```
