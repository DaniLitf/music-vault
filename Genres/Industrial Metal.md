# Industrial Metal

A fusion genre combining heavy metal with industrial music elements, characterized by synthesizers, drum machines, and distorted guitars.

```dataviewjs
dv.table(
  ["Artist", ""],
  dv.pages("#")
    .filter(p => p.genre && p.genre.includes("Industrial Metal"))
    .map(p => [p.display_name || p.file.name, ""])
    .sort()
)
```

**Total:** Automatically counted above via Dataview.
