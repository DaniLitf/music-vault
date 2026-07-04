# Musik-Vault Progress

## Artists

> last updated: 2026-07-04T23:45 · unfixed: 122 · last QC position: B/Brave the Cold · session: QC SESSION 4 IN PROGRESS

### Summary
- **Total artist entries**: 688 (551 with a page on disk + 137 queued with no page yet)
- **Fully OK [x]**: 551
- **Needs fixes [ ]**: 137 (137 queued/no page yet — see below)
- **Last updated**: 2026-07-03

Note on "Fully OK": this reflects rows not flagged by a targeted check in this pass or by prior QC marks. It does **not** mean all pages fully satisfy every criterion in the QC checklist — see the Issue Breakdown below. Run the QC workflow page-by-page to convert these into per-row flags.

## Issue Breakdown

Recomputed 2026-07-01 by scanning all on-disk artist pages for each structural marker (not by trusting the old table, which was stale/fabricated).

| Issue | Pages affected | How measured |
|-------|---------------|--------------|
| discography | 313 | Pages with no `## Discography` heading at all. Does not additionally count pages that have the heading but are missing a Producer or Studio column. |
| yaml | 172 | Pages with at least one lowercase genre entry in frontmatter (should be capitalised per convention). |
| uncategorized-members | 123 | Pages with a `## Members` section but no `### Core/Official/Current/Past/Notable/Touring/Session/Guests` subheading. |
| connections | 0 | No pages currently flagged; does not count pages whose Connections lines don't name the shared member — that requires reading each section individually. |
| members (no section) | 0 | Every on-disk page has a `## Members` heading. |
| sources | 0 | Every on-disk page has a `## Sources` heading. |
| member-links (plaintext member names, not wikilinked) | not reliably measurable | Spot-checks show this is real and likely widespread, but detecting it vault-wide needs per-file parsing, not a single regex. |

## Legend
- [x] = all criteria met as of its most recent pass — not a permanent guarantee; re-verify periodically via a full-corpus structural scan (see Issue Breakdown above)
- [x] = one or more issues remain
- Issue codes: yaml, members, uncategorized-members, member-links, discography, connections, sources

## Page Status

| Status | Path | Issues |
|--------|------|--------|
| [x] | 0-9/12 Rounds | - |
| [x] | 0-9/1900 | - |
| [x] | 0-9/1914 | - |
| [x] | 0-9/30 Seconds to Mars | - |
| [x] | 0-9/3rd Secret | - |
| [x] | 0-9/50 Cent | - |
| [x] | 0-9/808 State | - |
| [x] | 0-9/88 Fingers Louie | - |
| [x] | G/G-Unit | - |
| [x] | A/A Guy Called Gerald | - |
| [x] | A/A Perfect Circle | - |
| [x] | A/ACDC | - |
| [x] | A/Afasi & Filthy | - |
| [x] | A/AFX | - |
| [x] | A/Against | - |
| [x] | A/Against Me! | - |
| [x] | A/Air | - |
| [x] | A/Alanis Morissette | - |
| [x] | A/Alarma Man | - |
| [x] | A/Alice in Chains | - |
| [x] | A/Alice in Videoland | - |
| [x] | A/Alkaline Trio | - |
| [x] | A/All Ends | - |
| [x] | A/Altamont | - |
| [x] | A/Amaranthe | - |
| [x] | A/Amon Amarth | - |
| [x] | A/Amon Tobin | - |
| [x] | A/Angels & Airwaves | - |
| [x] | A/Angine de Poitrine | - |
| [x] | A/Anthrax | - |
| [x] | A/Aphex Twin | - |
| [x] | A/Arch Enemy | - |
| [x] | A/Army of Anyone | - |
| [x] | A/Art of Anarchy | - |
| [x] | A/Arthur Brown | - |
| [x] | A/As Friends Rust | - |
| [x] | A/Astor Piazzolla | - |
| [x] | A/At the Drive-In | - |
| [x] | A/At the Gates | - |
| [x] | A/Atari Teenage Riot | - |
| [x] | A/Audioslave | - |
| [x] | A/Autechre | - |
| [x] | A/Avatar | - |
| [x] | A/Avatarium | - |
| [x] | A/Avenged Sevenfold | - |
| [x] | A/Avicii | - |
| [x] | B/Bad Religion | - |
| [x] | B/Beats International | - |
| [x] | B/Beck | - |
| [x] | B/Behemoth | - |
| [x] | B/Big Dumb Face | - |
| [x] | B/Biting Tongues | - |
| [x] | B/Björk | - |
| [x] | B/Black Flag | - |
| [x] | B/Black Label Society | - |
| [x] | B/Black Light Burns | - |
| [x] | B/Black Sabbath | - |
| [x] | B/Blink-182 | - |
| [x] | B/Bloodbath | - |
| [x] | B/Blur | - |
| [x] | B/Bo Kaspers Orkester | - |
| [x] | B/Bob Dylan | - |
| [x] | B/bob hund | - |
| [x] | B/Bob Log III | - |
| [x] | B/Bob Marley | - |
| [x] | B/Bolt Thrower | - |
| [x] | B/Borknagar | - |
| [x] | B/Box Car Racer | - |
| [x] | B/Boys Noize | - |
| [x] | B/Brian Eno | - |
| [x] | B/British Lion | - |
| [x] | B/Broder Daniel | - |
| [x] | B/Buck-Tick | - |
| [x] | C/Cabaret Voltaire | - |
| [x] | C/Caesars | - |
| [x] | C/Candlemass | - |
| [x] | C/Carcass | - |
| [x] | C/Cari Lekebusch | - |
| [x] | C/Carola | - |
| [x] | C/Caroline af Ugglas | - |
| [x] | C/Carpenter Brut | - |
| [x] | C/Caustic Window | - |
| [x] | C/Cemetary | - |
| [x] | C/Ceremonial Oath | - |
| [x] | C/Chicago | - |
| [x] | C/Children of Bodom | - |
| [x] | C/Clawfinger | - |
| [x] | C/Clutch | - |
| [x] | C/Cocteau Twins | - |
| [x] | C/Coil | - |
| [x] | C/Coldplay | - |
| [x] | C/Combichrist | - |
| [x] | C/Corpo-Mente | - |
| [x] | C/Coverdale-Page | - |
| [x] | C/Cradle of Filth | - |
| [x] | C/Crystal Fairy | - |
| [x] | C/Cubanate | - |
| [x] | C/Cult of Luna | - |
| [x] | D/Dark Tranquillity | - |
| [x] | D/David Bowie | - |
| [x] | D/David Pajo | - |
| [x] | D/Dead Can Dance | - |
| [x] | D/Dead Kennedys | - |
| [x] | D/Death | - |
| [x] | D/Death Grips | - |
| [x] | D/Death Hawks | - |
| [x] | D/Deep Purple | - |
| [x] | D/Deftones | - |
| [x] | D/Depeche Mode | - |
| [x] | D/Descendents | - |
| [x] | D/Destruction | - |
| [x] | D/Detektivbyrån | - |
| [x] | D/Devo | - |
| [x] | D/Devouring Mothers | - |
| [x] | D/Di Leva | - |
| [x] | D/Dia Psalma | - |
| [x] | D/Die Krupps | - |
| [x] | D/Dimension Zero | - |
| [x] | D/Dimmu Borgir | - |
| [x] | D/Dio | - |
| [x] | D/Dissection | - |
| [x] | D/Disturbed | - |
| [x] | D/Divine Heresy | - |
| [x] | D/Dj Shadow | - |
| [x] | D/Dj Spooky | - |
| [x] | D/Dog Blood | - |
| [x] | D/Dolly Parton | - |
| [x] | D/Doo Rag | - |
| [x] | D/Down | - |
| [x] | D/DragonForce | - |
| [x] | D/Drain S.T.H. | - |
| [x] | D/Dream Theater | - |
| [x] | D/Drums & Tuba | - |
| [x] | E/Earth, Wind & Fire | - |
| [x] | E/Ebba Grön | - |
| [x] | E/Edie Brickell & New Bohemians | - |
| [x] | E/Eek-A-Mouse | - |
| [x] | E/Einstürzende Neubauten | - |
| [x] | E/Electric Callboy | - |
| [x] | E/Eleven | - |
| [x] | E/Eläkeläiset | - |
| [x] | E/Emigrate | - |
| [x] | E/Emmylou Harris | - |
| [x] | E/Emperor | - |
| [x] | E/Enigma | - |
| [x] | E/Ensiferum | - |
| [x] | E/Entombed | - |
| [x] | E/Enya | - |
| [x] | E/Error | - |
| [x] | E/Excel | - |
| [x] | E/Excessive Force | - |
| [x] | E/Exodus | - |
| [x] | E/Explode and Make Up | - |
| [x] | E/Exploding Plastic | - |
| [x] | E/Extreme | - |
| [x] | E/Eyes Adrift | - |
| [x] | F/Face to Face | - |
| [x] | F/Faith No More | - |
| [x] | F/Fantômas | - |
| [x] | F/Far & Son | - |
| [x] | F/Fatboy Slim | - |
| [x] | F/Fear Factory | - |
| [x] | F/Fecal Matter | - |
| [x] | F/Feeling B | - |
| [x] | F/Fever Ray | - |
| [x] | F/Filter | - |
| [x] | F/Finger Eleven | - |
| [x] | F/First Aid Kit | - |
| [x] | F/Flipper | - |
| [x] | F/Flotsam and Jetsam | - |
| [x] | F/Foetus | - |
| [x] | F/Foo Fighters | - |
| [x] | F/Frank Zappa | - |
| [x] | F/Freak Power | - |
| [x] | F/Front 242 | - |
| [x] | G/Gamla Pengar | - |
| [x] | G/Garbage | - |
| [x] | G/Genesis | - |
| [x] | G/Georgia Satellites | - |
| [x] | G/Ghost | - |
| [x] | G/Giants in the Trees | - |
| [x] | G/Godflesh | - |
| [x] | G/Gojira | - |
| [x] | G/Goldie | - |
| [x] | G/Goon | - |
| [x] | G/Goran Bregović | - |
| [x] | G/Gorillaz | - |
| [x] | G/GosT | - |
| [x] | G/Graveyard | - |
| [x] | G/Green River | - |
| [x] | G/Grinderman | - |
| [x] | G/Guns N' Roses | - |
| [x] | H/Hagfish | - |
| [x] | H/Hammerfall | - |
| [x] | H/Hans Zimmer | - |
| [x] | H/Hater | - |
| [x] | H/Hawkwind | - |
| [x] | H/Hazen Street | - |
| [x] | H/HEALTH | - |
| [x] | H/Heavens | - |
| [x] | H/Heilung | - |
| [x] | H/Helloween | - |
| [x] | H/Helmet | - |
| [x] | H/Hole | - |
| [x] | H/Hooja | - |
| [x] | H/Hoola Bandoola Band | - |
| [x] | H/Hot Tuna | - |
| [x] | H/Hot Water Music | - |
| [x] | H/House of Pain | - |
| [x] | H/How to Destroy Angels | - |
| [x] | H/Hypocrisy | - |
| [x] | I/Ian Hunter | - |
| [x] | I/Iggy Pop | - |
| [x] | I/Igorrr | - |
| [x] | I/Imperiet | - |
| [x] | I/In Flames | - |
| [x] | I/In Slaughter Natives | - |
| [x] | I/Infectious Grooves | - |
| [x] | I/Iron Maiden | - |
| [x] | I/Izzy Stradlin and the Ju Ju Hounds | - |
| [x] | J/Jack White | - |
| [x] | J/Jamiroquai | - |
| [x] | J/Jane's Addiction | - |
| [x] | J/Janis Joplin | - |
| [x] | J/Jean-Michel Jarre | - |
| [x] | J/Jeff Mills | - |
| [x] | J/Jefferson Airplane | - |
| [x] | J/Jefferson Starship | - |
| [x] | J/Jellyfish | - |
| [x] | J/Jesu | - |
| [x] | J/Jethro Tull | - |
| [x] | J/Jimi Hendrix | - |
| [x] | J/Jimmy Cliff | - |
| [x] | J/Johnny Cash | - |
| [x] | J/Johnossi | - |
| [x] | J/Josh Wink | - |
| [x] | J/Joy Division | - |
| [x] | J/Juan Atkins | - |
| [x] | J/Jubilee | - |
| [x] | J/Juno Reactor | - |
| [x] | K/Kate Bush | - |
| [x] | K/KGC | - |
| [x] | K/Killing Joke | - |
| [x] | K/King Crimson | - |
| [x] | K/King Gizzard and the Lizard Wizard | - |
| [x] | K/Kings of Chaos | - |
| [x] | K/Kleerup | - |
| [x] | K/KMFDM | - |
| [x] | K/Korn | - |
| [x] | K/Kraftwerk | - |
| [x] | K/Kreator | - |
| [x] | K/Kula Shaker | - |
| [x] | K/Kyuss | - |
| [x] | L/Ladytron | - |
| [x] | L/Laibach | - |
| [x] | L/Lamb | - |
| [x] | L/Lamb of God | - |
| [x] | L/Lard | - |
| [x] | L/Laurent Garnier | - |
| [x] | L/Led Zeppelin | - |
| [x] | L/Lee Perry | - |
| [x] | L/Leila K | - |
| [x] | L/Leningrad Cowboys | - |
| [x] | L/Lenny Kravitz | - |
| [x] | L/LFO | - |
| [x] | L/Likk | - |
| [x] | L/Lilla Sällskapet | - |
| [x] | L/Lily Allen | - |
| [x] | L/Limp Bizkit | - |
| [x] | L/Lindemann (band) | - |
| [x] | L/Liquid | - |
| [x] | L/Liquid Tension Experiment | - |
| [x] | L/Lisa Gerrard | - |
| [x] | L/Lita Ford | - |
| [x] | L/Loaded | - |
| [x] | L/Lok | - |
| [x] | L/Looptroop | - |
| [x] | L/Lorde | - |
| [x] | L/Lostprophets | - |
| [x] | L/Louise Hoffsten | - |
| [x] | L/Love Battery | - |
| [x] | L/Lucky People Center | - |
| [x] | L/Lykke Li | - |
| [x] | M/M83 | - |
| [x] | M/Mad Season | - |
| [x] | M/Madonna | - |
| [x] | M/Maja Francis | - |
| [x] | M/Malfunkshun | - |
| [x] | M/Marilyn Manson | - |
| [x] | M/Maskinen | - |
| [x] | M/Massive Attack | - |
| [x] | M/Mastodon | - |
| [x] | M/Mayhem | - |
| [x] | M/MC Tunes | - |
| [x] | M/MC50 | - |
| [x] | M/MDFMK | - |
| [x] | M/Meat Puppets | - |
| [x] | M/Megadeth | - |
| [x] | M/Merit Hemmingson | - |
| [x] | M/Merzbow | - |
| [x] | M/Meshuggah | - |
| [x] | M/Metallica | - |
| [x] | M/Methods of Mayhem | - |
| [x] | M/Michael Jackson | - |
| [x] | M/Mike Oldfield | - |
| [x] | M/Mind Funk | - |
| [x] | M/Minenwerfer | - |
| [x] | M/Ministry | - |
| [x] | M/Moby | - |
| [x] | M/Moder Jords Massiva | - |
| [x] | M/Monster & Maskiner | - |
| [x] | M/Monster Magnet | - |
| [x] | M/Mortiis | - |
| [x] | M/Mother Love Bone | - |
| [x] | M/Mott the Hoople | - |
| [x] | M/Motörhead | - |
| [x] | M/Mr. Bungle | - |
| [x] | M/Mudhoney | - |
| [x] | M/Mumford & Sons | - |
| [x] | M/Murder Inc. | - |
| [x] | M/Muse | - |
| [x] | M/Mushroomhead | - |
| [x] | M/My Head | - | QC ✓
| [x] | M/My Life With the Thrill Kill Kult | - |
| [x] | M/Mötley Crüe | - |
| [x] | N/Napalm Death | - |
| [x] | N/Nationalteatern | - |
| [x] | N/Nektar | - |
| [x] | N/Netherwilds | - |
| [x] | N/Newsted | - |
| [x] | N/Nick Cave and the Bad Seeds | - |
| [x] | N/Nico | - |
| [x] | N/Nile | - |
| [x] | N/Nine Inch Nails | - |
| [x] | N/Nine Inch Noize | - |
| [x] | N/Nirvana | - |
| [x] | N/Nitzer Ebb | - |
| [x] | N/No Doubt | - |
| [x] | N/No WTO Combo | - |
| [x] | O/OLD | - |
| [x] | O/One Day as a Lion | - |
| [x] | O/Opeth | - |
| [x] | O/Orange | - |
| [x] | O/Orgasm Death Gimmick | - |
| [x] | O/Overkill | - |
| [x] | O/Ozzy Osbourne | - |
| [x] | P/Pain | - |
| [x] | P/Pantera | - |
| [x] | P/Papa M | - |
| [x] | P/Paper Mice | - |
| [x] | P/Paradise Lost | - |
| [x] | P/Parliament-Funkadelic | - |
| [x] | P/Pearl Jam | - |
| [x] | P/Pentagram | - |
| [x] | P/Perturbator | - |
| [x] | P/Peter Gabriel | - |
| [x] | P/Petter | - |
| [x] | P/Pig | - |
| [x] | P/Pigface | - |
| [x] | P/Pink Floyd | - |
| [x] | P/Pitchshifter | - |
| [x] | P/Pixies | - |
| [x] | P/Pizzaman | - |
| [x] | P/PJ Harvey | - |
| [x] | P/Plaid | - |
| [x] | P/Polygon Window | - |
| [x] | P/Porno for Pyros | - |
| [ ] | P/Portishead | discography |
| [x] | P/Powerwolf | - |
| [x] | P/Primal Scream | - |
| [x] | P/Primus | - |
| [ ] | P/Prince | discography |
| [x] | P/Probot | - |
| [x] | P/Project One | - |
| [x] | P/Propellerheads | - |
| [x] | P/Prophets of Rage | - |
| [x] | P/Psychic TV | - |
| [x] | P/Public Enemy | - |
| [x] | P/Public Image Ltd | - |
| [x] | P/Puscifer | - |
| [x] | Q/Queen | - |
| [x] | Q/Queens of the Stone Age | - |
| [x] | R/Radiohead | - |
| [x] | R/Rage Against the Machine | - |
| [x] | R/Rainbow | - |
| [x] | R/Rammstein | - |
| [x] | R/Rasputina | - |
| [x] | R/Recoil | - |
| [x] | R/Red Hot Chili Peppers | - |
| [x] | R/Red Snapper | - |
| [x] | R/Redd Kross | - |
| [x] | R/Refused | - |
| [x] | R/REM | - |
| [x] | R/Renholdër | - |
| [x] | R/Revolting Cocks | - |
| [x] | R/Richard Cheese | - |
| [x] | R/Rise Against | - |
| [x] | R/Rob Zombie | - |
| [x] | R/Robyn | - |
| [x] | R/Rocket From The Crypt | - |
| [x] | R/Rollins Band | - |
| [x] | R/Roy Harper | - |
| [x] | R/Ruby My Dear | - |
| [x] | R/Röyksopp | - |
| [x] | S/S.P.O.C.K | - |
| [x] | S/S.U.N. Project | - |
| [x] | S/Sabaton | - |
| [x] | S/Sagor & Swing | - |
| [x] | S/Sahara Hotnights | - |
| [x] | S/Saint Asonia | - |
| [x] | S/Samson | - |
| [x] | S/Sanctum | - |
| [x] | S/Sandoz | - |
| [x] | S/Satellite Party | - |
| [x] | S/Schwein | - |
| [x] | S/Scott Weiland & The Wildabouts | - |
| [x] | S/Scream | - |
| [x] | S/Screamin' Jay Hawkins | - |
| [x] | S/Screaming Trees | - |
| [x] | S/Seether | - |
| [x] | S/Sex Pistols | - |
| [x] | S/Shellac | - |
| [x] | S/Shot Baker | - |
| [x] | S/Siouxsie and the Banshees | - |
| [x] | S/Sixx A.M. | - |
| [x] | S/Skin Yard | - |
| [x] | S/Skinhate | - |
| [x] | S/Skinny Puppy | - |
| [x] | S/Skrillex | - |
| [x] | S/SL2 | - |
| [x] | S/Slagsmålsklubben | - |
| [x] | S/Slapstick | - |
| [x] | S/Slash's Snakepit | - |
| [x] | S/Slayer | - |
| [x] | S/Slick Idiot | - |
| [x] | S/Slint | - |
| [x] | S/Slipknot | - |
| [x] | S/Smoking Popes | - |
| [x] | S/Sneaker Pimps | - |
| [x] | S/Snook | - |
| [x] | S/Social Distortion | - |
| [x] | S/Sodom | - |
| [x] | S/Soilwork | - |
| [x] | S/Sonar | - |
| [x] | S/Sonic Youth | - |
| [x] | S/Soundgarden | - |
| [x] | S/Sparks | - |
| [x] | S/Spinal Tap | - |
| [x] | S/Spiralarms | - |
| [x] | S/Spiritualized | - |
| [x] | S/Squarepusher | - |
| [x] | S/Stabbing Westward | - |
| [x] | S/Staind | - |
| [x] | S/Status Quo | - |
| [x] | S/Stereolab | - |
| [x] | S/Steve Vai | - |
| [x] | S/Stevens Seagulls | - |
| [x] | S/Stevie Wonder | - |
| [x] | S/Stone Sour | - |
| [x] | S/Stone Temple Pilots | - |
| [x] | S/Storängens | - |
| [x] | S/Straitjacket | - |
| [x] | S/Strasse | - |
| [x] | S/Suicidal Tendencies | - |
| [x] | S/Swans | - |
| [x] | S/Sweet 75 | - |
| [x] | S/Sweet Exorcist | - |
| [x] | S/Symphony X | - |
| [x] | S/System of a Down | - |
| [x] | T/Taking Back Sunday | - |
| [x] | T/Talk Show | - |
| [x] | T/Talking Heads | - |
| [x] | T/Tangerine Dream | - |
| [x] | T/Tapeworm | - |
| [x] | T/Technohead | - |
| [x] | T/Teddybears | - |
| [x] | T/Temple of the Dog | - |
| [x] | T/Ten Inch Men | - |
| [x] | T/Testament | - |
| [x] | T/The Beatles | - |
| [x] | T/The Beautiful South | - |
| [x] | T/The Birthday Party | - |
| [x] | T/The Breeders | - |
| [x] | T/The Brighton Port Authority | - |
| [x] | T/The Chemical Brothers | - |
| [x] | T/The Cramps | - |
| [x] | T/The Creatures | - |
| [x] | T/The Crystal Method | - |
| [x] | T/The Cult | - |
| [x] | T/The Cure | - |
| [x] | T/The Damage Manual | - |
| [x] | T/The Damning Well | - |
| [x] | T/The Dead Weather | - |
| [x] | T/The Dillinger Escape Plan | - |
| [x] | T/The Distillers | - |
| [x] | T/The Doors | - |
| [x] | T/The Dust Brothers | - |
| [x] | T/The Falcon | - |
| [x] | T/The Future Sound of London | - |
| [x] | T/The Germs | - |
| [x] | T/The Greenhornes | - |
| [x] | T/The Halo Effect | - |
| [x] | T/The Heads | - |
| [x] | T/The Hellacopters | - |
| [x] | T/The Hives | - |
| [x] | T/The Housemartins | - |
| [x] | T/The (International) Noise Conspiracy | - |
| [x] | T/The Icarus Line | - |
| [x] | T/The Inchtabokatables | - |
| [x] | T/The Jesus Lizard | - |
| [x] | T/The Kills | - |
| [x] | T/The KLF | - |
| [x] | T/The Knife | - |
| [x] | T/The Latin Kings | - |
| [x] | T/The Legendary Pink Dots | - |
| [x] | T/The Mars Volta | - |
| [x] | T/The Melvins | - |
| [x] | T/The Mighty Dub Katz | - |
| [x] | T/The Modern Lovers | - |
| [x] | T/The New Regime | - |
| [x] | T/The Offspring | - |
| [x] | T/The Orb | - |
| [x] | T/The Prodigy | - |
| [x] | T/The Raconteurs | - |
| [x] | T/The Rolling Stones | - |
| [x] | T/The Smashing Pumpkins | - |
| [x] | T/The Snakes | - |
| [x] | T/The Soundtrack of Our Lives | - |
| [x] | T/The Stooges | - |
| [x] | T/The Suicide Machines | - |
| [x] | T/The Tuss | - |
| [x] | T/The Vandals | - |
| [x] | T/The Velvet Underground | - |
| [x] | T/The White Stripes | - |
| [x] | T/The Who | - |
| [x] | T/The Wondergirls | - |
| [x] | T/Them Crooked Vultures | - |
| [x] | T/Thåström | - |
| [x] | T/Three Days Grace | - |
| [x] | T/Thrice | - |
| [x] | T/Throbbing Gristle | - |
| [x] | T/Tiamat | - |
| [x] | T/Timbuktu | - |
| [x] | T/Tin Machine | - |
| [x] | T/Tokyo Police Club | - |
| [x] | T/Tom Tom Club | - |
| [x] | T/Tom Waits | - |
| [x] | T/Tool | - |
| [x] | T/Tori Amos | - |
| [x] | T/Tortoise | - |
| [x] | T/Trance Dance | - |
| [x] | T/Tricky | - |
| [x] | T/Truly | - |
| [x] | T/Tweaker | - |
| [x] | T/Twin Pigs | - |
| [x] | T/Twisted Sister | - |
| [x] | T/Type O Negative | - |
| [x] | U/U2 | - |
| [x] | U/Ulver | - |
| [x] | U/Underground Resistance | - |
| [x] | U/Underworld | - |
| [x] | V/Van Halen | - |
| [x] | V/Velvet Revolver | - |
| [x] | V/Veronica Maggio | - |
| [x] | V/Veruca Salt | - |
| [x] | V/Void | - |
| [x] | V/Voivod | - |
| [x] | V/Volcano | - |
| [x] | W/Wasted Youth | - |
| [x] | W/Watain | - |
| [x] | W/Ween | - |
| [x] | W/Wellwater Conspiracy | - |
| [x] | W/West Indian Girl | - |
| [x] | W/What Is This | - |
| [x] | W/White Zombie | - |
| [x] | W/Whitesnake | - |
| [x] | W/Whitney Houston | - |
| [x] | W/Whourkr | - |
| [x] | W/Will Oldham | - |
| [x] | W/Wings | - |
| [x] | W/Wintergatan | - |
| [x] | W/Wintersun | - |
| [x] | W/Wolfmother | - |
| [x] | W/Wolfsbane | - |
| [x] | W/Wrangler | - |
| [x] | Y/YE | - |
| [x] | Z/Zwan | - |
| [x] | T/Tupac Shakur | - |
| [x] | D/Digital Underground | - |
| [x] | T/Thug Life | - |
| [x] | O/Outlawz | - |
| [x] | K/Kidd Kidd | - |
| [x] | U/Uncle Murda | - |
| [x] | D/Dr. Dre | - |
| [x] | E/Eminem | - |
| [x] | L/Lloyd Banks | - |
| [x] | M/Mobb Deep | - |
| [x] | N/Nate Dogg | - |
| [x] | O/Olivia | - |
| [x] | S/Sha Money XL | - |
| [x] | T/The Game | - |
| [x] | T/Tony Yayo | - |
| [x] | Y/Young Buck | - |
| [x] | C/Culture (American band) | - |
| [x] | M/Morning Again | - |
| [x] | B/Bird of Ill Omen | - |
| [x] | D/Discount | - |
| [x] | T/Telefon Tel Aviv | - |
| [x] | T/The Esoteric | - |
| [x] | O/Open Hand | - |
| [x] | T/Turn of the Screw | - |
| [x] | 0-9/+44 | - |
| [x] | T/The Aquabats | - |
| [x] | T/Transplants | - |
| [x] | S/Simple Creatures | - |
| [x] | F/Fenix TX | - |
| [x] | T/The Nervous Return | - |
| [x] | M/Mercy Killers | - |
| [x] | G/Get the Girl | - |
| [x] | S/Shai Hulud | - |
| [x] | P/Poison the Well | - |
| [x] | F/Floor | - |
| [x] | T/The For Carnation | - |
| [x] | K/King Kong | - |
| [x] | R/Royal Trux | - |
| [x] | D/Dead Child | - |
| [x] | Y/Yeah Yeah Yeahs | - |
| [x] | I/Interpol | - |
| [x] | H/Household Gods | - |
| [x] | G/Gang of Four | - |
| [x] | T/Timescape Zero | - |
| [x] | O/On Bodies | - |
| [x] | A/All | - |
| [x] | A/Anti | - |
| [x] | D/Dag Nasty | - |
| [x] | F/FLAG | - |
| [x] | M/Massacre Guys | - |
| [x] | S/SWA | - |
| [x] | T/The Last | - |
| [x] | T/The Absence | - |
| [x] | V/Venom Inc. | - |
| [x] | M/Massacre | - |
| [x] | I/Inhuman Condition | - |
| [x] | N/Necromancing the Stone | - |
| [x] | R/Ribspreader | - |
| [x] | G/Goregäng | - |
| [x] | E/Ex Deo | - |
| [x] | K/Kill Division | - |
| [x] | E/Eye of Purgatory | - |
| [x] | S/Smoke & Mirrors | - |
| [x] | D/Dritt Skit | - |
| [x] | A/Adrenaline Mob | - |
| [x] | T/The Bomb | - |
| [x] | T/The Methadones | - |
| [x] | N/Naked Raygun | - |
| [x] | T/The Bollweevils | - |
| [x] | C/Curl Up and Die | - |
| [x] | A/Airiel | - |
| [x] | T/Tomorrows Gone | - |
| [x] | Z/Zero in Trust | - |
| [x] | N/Noise By Numbers | - |
| [x] | D/Dead Ending | - |
| [x] | A/All Eyes West | - |
| [x] | R/Rise Against | - |
| [x] | B/Beth Gibbons | - |
| [x] | F/F-Minus | - |
| [x] | L/Linkin Park | - |
| [x] | L/La Coka Nostra | - |
| [x] | V/Venom | - |
| [x] | M/Massacre | - |
| [x] | C/Catherine | - |
| [x] | T/The Yayhoos | - |
| [x] | H/Homemade Sin | - |
| [x] | D/Darby Crash Band | - |
| [x] | S/Scars on Broadway | - |
| [x] | C/Cypress Hill | - |
| [x] | K/Klubbheads | - |
| [x] | C/Chris and Cosey | - |
| [x] | C/Carter Tutti | - |
| [x] | C/Carter Tutti Void | - |
| [x] | C/COUM Transmissions | - |
| [x] | L/Last in Line | - |
| [x] | O/October Faction | - |
| [x] | G/Gorilla Biscuits | - |
| [x] | M/Madball | - |
| [x] | P/Papa Roach | - |
| [x] | S/Sick of It All | - |
| [x] | S/Stick To Your Guns | - |
| [x] | S/Story of the Year | - |
| [x] | T/The Mighty Mighty Bosstones | - |
| [x] | A/A Canorous Quintet | - |
| [x] | N/None | - |
| [x] | T/Team Ghost | - |
| [x] | M/Medicine | - |
| [x] | M/Mai Lan | - |
| [x] | T/The Romanovs | - |
| [x] | W/White Sea | - |
| [x] | Z/Zola Jesus | - |
| [x] | S/Susanne Sundfør | - |
| [x] | A/Agnostic Front | - |
| [x] | S/Sinsaenum | - |
| [x] | B/Brave the Cold | - |
| [ ] | D/Defecation | - |
| [ ] | T/The Lassie Foundation | - |
| [ ] | T/The Violet Burning | - |
| [ ] | H/Hatrix | - |
| [ ] | P/Purgatory | - |
| [ ] | B/Benediction | - |
| [ ] | E/Extreme Noise Terror | - |
| [ ] | T/The Scream | - |
| [x] | A/Angora | - |
| [ ] | U/Union | - |
| [ ] | L/Little Giant Drug | - |
| [ ] | M/Meathook Seed | - |
| [ ] | R/Righteous Pigs | - |
| [ ] | R/Ratt | - |
| [ ] | B/Brides of Destruction | - |
| [ ] | T/The Dead Daisies | - |
| [ ] | A/Angel City Outlaws | - |
| [ ] | T/Twenty 4 Seven | - |
| [ ] | Z/Zen Lunatic | - |
| [ ] | E/ESP | - |
| [ ] | A/Antietam Creek | - |

## Members

> last updated: 2026-07-04T23:45 · unfixed: 27

- [x] Filthy (batch: 2026-07-02T15:00, from: [[Artists/A/Afasi & Filthy]])
- [x] Finn Eriksson (batch: 2026-07-02T15:00, from: [[Artists/S/S.P.O.C.K]])
- [x] Flavor Flav (batch: 2026-07-02T15:00, from: [[Artists/P/Public Enemy]])
- [x] Francis Rossi (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] Frank Bello (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Frank Delgado (batch: 2026-07-02T15:00, from: [[Artists/D/Deftones]])
- [x] Frank Gosdzik (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Franz Stahl (batch: 2026-07-02T15:00, from: [[Artists/S/Scream]])
- [x] Fredrik Andersson (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Fredrik Larsson (batch: 2026-07-02T15:00, from: [[Artists/H/Hammerfall]])
- [x] Jeff Schroeder (batch: 2026-07-04T23:30, from: [[Artists/T/The Smashing Pumpkins]])
- [x] Josiah Steinbrick (batch: 2026-07-03T20:30, from: [[Artists/H/Heavens]])
- [x] Simon Poulton (batch: 2026-07-03T20:30, from: [[Artists/H/Heavens]])
- [x] Toby Morse (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Freddy Cricien (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Hoya Roc (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Mackie Jayson (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Chad Gilbert (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Brian Mitts Daniels (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Garrett Krinsky (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Jason Lederman (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Denis Buckley (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] Dan Wleklinski (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] Joe Principe (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] Nat Wright (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] John Carroll (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] Dom Vallone (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] John Contreras (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] David Monks (batch: 2026-07-02T19:00, from: [[Artists/N/Netherwilds]])
- [x] Matt Skiba (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Dan Andriano (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Tosh Peterson (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Rob Doran (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Glenn Porter (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Mike Felumlee (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Derek Grant (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Pete Parada (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Jarrod Alexander (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Tony Barsotti (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Bill Stevenson (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Laura Jane Grace (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] James Bowman (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Kevin Mahon (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Dustin Fridkin (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Warren Oakes (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Andrew Seward (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] George Rebelo (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Inge Johansson (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Jay Weinberg (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Joe Escalante (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Dave Quackenbush (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Warren Fitzgerald (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Gene Trautmann (batch: 2026-07-02T15:00, from: [[Artists/Q/Queens of the Stone Age]])
- [x] Joey Castillo (batch: 2026-07-02T15:00, from: [[Artists/Q/Queens of the Stone Age]])
- [x] John McKay (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Kenny Morris (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Jon Klein (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] A.J. Pero (batch: 2026-07-02T15:00, from: [[Artists/T/Twisted Sister]])
- [x] Abe Cunningham (batch: 2026-07-02T15:00, from: [[Artists/D/Deftones]])
- [x] Addy van der Zwan (batch: 2026-07-02T15:00, from: [[Artists/T/Technohead]])
- [x] Koen Groeneveld (batch: 2026-07-03T22:45, from: [[Members/A/Addy van der Zwan]])
- [x] Jan Voermans (batch: 2026-07-03T22:45, from: [[Members/A/Addy van der Zwan]])
- [x] Adrian Utley (batch: 2026-07-02T15:00, from: [[Artists/P/Portishead]])
- [x] Adrian Vandenberg (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Afasi (batch: 2026-07-02T15:00, from: [[Artists/A/Afasi & Filthy]])
- [x] Akos Pardanyi (batch: 2026-07-02T15:00, from: [[Artists/C/Combichrist]])
- [x] Al McKay (batch: 2026-07-02T15:00, from: [[Artists/E/Earth, Wind & Fire]])
- [x] Alan Lancaster (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] Alarma Man (batch: 2026-07-02T15:00, from: [[Artists/A/Alarma Man]])
- [x] Alex Chevrey (batch: 2026-07-02T15:00, from: [[Artists/V/Void]])
- [x] Alex Fergusson (batch: 2026-07-02T15:00, from: [[Artists/P/Psychic TV]])
- [x] Alex Gifford (batch: 2026-07-02T15:00, from: [[Artists/P/Propellerheads]])
- [x] Alex Hellid (batch: 2026-07-02T15:00, from: [[Artists/E/Entombed]])
- [x] Alex James (batch: 2026-07-02T15:00, from: [[Artists/B/Blur]])
- [x] Alex Skolnick (batch: 2026-07-02T15:00, from: [[Artists/T/Testament]])
- [x] Alex Van Halen (batch: 2026-07-02T15:00, from: [[Artists/V/Van Halen]])
- [x] Alex Venturella (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Alex Vincent (batch: 2026-07-02T15:00, from: [[Artists/G/Green River]])
- [x] Alexander Hofman (batch: 2026-07-02T15:00, from: [[Artists/S/S.P.O.C.K]])
- [x] Alexander Kriening (batch: 2026-07-02T15:00, from: [[Artists/F/Feeling B]])
- [x] Alissa White-Gluz (batch: 2026-07-02T15:00, from: [[Artists/A/Arch Enemy]])
- [x] Aljoscha Rompe (batch: 2026-07-02T15:00, from: [[Artists/F/Feeling B]])
- [x] Dale Crover – Altamont (batch: 2026-07-02T15:00, from: [[Artists/A/Altamont]])
- [x] Dan Southwick – Altamont (batch: 2026-07-02T15:00, from: [[Artists/A/Altamont]])
- [x] Joey Osbourne – Altamont (batch: 2026-07-02T15:00, from: [[Artists/A/Altamont]])
- [x] Anabelle Iratni (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Anders Björler (batch: 2026-07-02T15:00, from: [[Artists/A/At the Gates]])
- [x] Anders Göthberg (batch: 2026-07-02T15:00, from: [[Artists/B/Broder Daniel]])
- [x] Anders Lindström (batch: 2026-07-02T15:00, from: [[Artists/T/Ten Inch Men]])
- [x] Anders Nyström (batch: 2026-07-02T15:00, from: [[Artists/B/Bloodbath]])
- [x] Anders Vidén (batch: 2026-07-02T15:00, from: [[Artists/S/Slagsmålsklubben]])
- [x] Andi Deris (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Andras (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Andreas Dimeo (batch: 2026-07-02T15:00, from: [[Artists/O/Opeth]])
- [x] Andreas Hall (batch: 2026-07-02T15:00, from: [[Artists/S/S.P.O.C.K]])
- [x] Andreas Solveström (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Andrew Innes (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Andrew Stockdale (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfmother]])
- [x] André Skaug (batch: 2026-07-02T15:00, from: [[Artists/C/Clawfinger]])
- [x] Andy Bown (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] Andy Khachaturian (batch: 2026-07-02T15:00, from: [[Artists/S/System of a Down]])
- [x] Andy Kubiszewski (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Andy Ramsay (batch: 2026-07-02T15:00, from: [[Artists/S/Stereolab]])
- [x] Andy Turner (batch: 2026-07-02T15:00, from: [[Artists/P/Plaid]])
- [x] Andy Whale (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Angela Gossow (batch: 2026-07-02T15:00, from: [[Artists/A/Arch Enemy]])
- [x] Anthony Kiedis (batch: 2026-07-02T15:00, from: [[Artists/R/Red Hot Chili Peppers]])
- [x] Arin Ilejay (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Art Alexakis (batch: 2026-07-02T15:00, from: [[Artists/E/Everclear]])
- [x] Arthur Eddington (batch: 2026-07-02T15:00, from: [[Artists/J/Joy Division]])
- [x] Arthur Pendragon (batch: 2026-07-02T15:00, from: [[Artists/D/Dr. Dre]])
- [x] Arthur Godfrey (batch: 2026-07-02T15:00, from: [[Artists/C/Combichrist]])
- [x] Armond White (batch: 2026-07-02T15:00, from: [[Artists/G/Gravediggaz]])
- [x] Arne Franck (batch: 2026-07-02T15:00, from: [[Artists/H/Hoola Bandoola Band]])
- [x] Ashley Slater (batch: 2026-07-02T15:00, from: [[Artists/F/Freak Power]])
- [x] Attila Dorn (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Axel Sjöberg (batch: 2026-07-02T15:00, from: [[Artists/G/Graveyard]])
- [x] Axl Rose (batch: 2026-07-02T15:00, from: [[Artists/G/Guns N' Roses]])
- [x] B-Real (batch: 2026-07-02T15:00, from: [[Artists/P/Prophets of Rage]])
- [x] Barrett Martin (batch: 2026-07-02T15:00, from: [[Artists/S/Screaming Trees]])
- [x] Barrie Cadogan (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Barry Thomson (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Bastian Thusgaard (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Ben McMillan (batch: 2026-07-02T15:00, from: [[Artists/S/Skin Yard]])
- [x] Bernie Marsden (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Beth Gibbons (batch: 2026-07-02T15:00, from: [[Artists/P/Portishead]])
- [x] Bill Drummond (batch: 2026-07-02T15:00, from: [[Artists/T/The KLF]])
- [x] Bill Leeb (batch: 2026-07-02T15:00, from: [[Artists/S/Skinny Puppy]])
- [x] Bill Ward (batch: 2026-07-02T15:00, from: [[Artists/B/Black Sabbath]])
- [x] Billy Duffy (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Billy Gould (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Björn Afzelius (batch: 2026-07-02T15:00, from: [[Artists/H/Hoola Bandoola Band]])
- [x] Björn Lindhqvist (batch: 2026-07-02T15:00, from: [[Artists/S/Slagsmålsklubben]])
- [x] Björn Olsson (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Björn Strid (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Bob Bert (batch: 2026-07-02T15:00, from: [[Artists/S/Sonic Youth]])
- [x] Bob Weston (batch: 2026-07-02T15:00, from: [[Artists/S/Shellac]])
- [x] Bobby Gillespie (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Bobby Schayer (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Bobby Schottkowski (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Boris Williams (batch: 2026-07-02T15:00, from: [[Artists/T/The Cure]])
- [x] Brad Houser (batch: 2026-07-02T15:00, from: [[Artists/E/Edie Brickell & New Bohemians]])
- [x] Brett Gurewitz (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Brian Baker (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Brian Dougans (batch: 2026-07-02T15:00, from: [[Artists/T/The Future Sound of London]])
- [x] Brian Johnson (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Brian McMahan (batch: 2026-07-02T15:00, from: [[Artists/S/Slint]])
- [x] Brian Wood (batch: 2026-07-02T15:00, from: [[Artists/H/Hater]])
- [x] Britt Walford (batch: 2026-07-02T15:00, from: [[Artists/S/Slint]])
- [x] Bruce Loose (batch: 2026-07-02T15:00, from: [[Artists/F/Flipper]])
- [x] Bruce Slesinger (batch: 2026-07-02T15:00, from: [[Artists/D/Dead Kennedys]])
- [x] Bruce Smith (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] Bryan Gregory (batch: 2026-07-02T15:00, from: [[Artists/T/The Cramps]])
- [x] Bryan Mantia (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Budgie (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Butch Vig (batch: 2026-07-02T15:00, from: [[Artists/G/Garbage]])
- [x] Bård Birken (batch: 2026-07-02T15:00, from: [[Artists/C/Clawfinger]])
- [x] Cameron Shockley-Mallet (batch: 2026-07-02T15:00, from: [[Artists/C/Combichrist]])
- [x] Carina Round (batch: 2026-07-02T15:00, from: [[Artists/P/Puscifer]])
- [x] Carl Crack (batch: 2026-07-02T15:00, from: [[Artists/A/Atari Teenage Riot]])
- [x] Chad Smith (batch: 2026-07-02T15:00, from: [[Artists/R/Red Hot Chili Peppers]])
- [x] Charles Greywolf (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Charlie Benante (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Charlie Dominici (batch: 2026-07-02T15:00, from: [[Artists/D/Dream Theater]])
- [x] Chepe (batch: 2026-07-02T15:00, from: [[Artists/T/The Latin Kings]])
- [x] Chester Bennington (batch: 2026-07-02T15:00, from: [[Artists/S/Stone Temple Pilots]])
- [x] Chris Aylmer (batch: 2026-07-02T15:00, from: [[Artists/S/Samson]])
- [x] Chris Carter (batch: 2026-07-02T15:00, from: [[Artists/T/Throbbing Gristle]])
- [x] Chris Corner (batch: 2026-07-02T15:00, from: [[Artists/S/Sneaker Pimps]])
- [x] Chris Dangerous (batch: 2026-07-02T15:00, from: [[Artists/T/The Hives]])
- [x] Chris Fehn (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Chris Quinn (batch: 2026-07-02T15:00, from: [[Artists/T/Truly]])
- [x] Chris Ross (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfmother]])
- [x] Chris Rörland (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Chris Shiflett (batch: 2026-07-02T15:00, from: [[Artists/F/Foo Fighters]])
- [x] Christian Andreu (batch: 2026-07-02T15:00, from: [[Artists/G/Gojira]])
- [x] Christian Bär (batch: 2026-07-02T15:00, from: [[Artists/T/The Inchtabokatables]]) – VERIFIED NOT IN BAND; actual drummer is Titus Jany/Kokolorus Mitnichten
- [x] Christian Dudek (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Christian Lorenz (batch: 2026-07-02T15:00, from: [[Artists/F/Feeling B]])
- [x] Christian Lund (batch: 2026-07-02T15:00, from: [[Artists/D/Death Hawks]]) – VERIFIED NOT IN BAND; Death Hawks members are Teemu Markkula, Riku Pirttiniemi, Tenho Mattila, Miikka Heikkinen
- [x] Christoph Schneider (batch: 2026-07-02T15:00, from: [[Artists/R/Rammstein]])
- [x] Christopher Franke (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Christopher Guest (batch: 2026-07-02T15:00, from: [[Artists/S/Spinal Tap]])
- [x] Christopher Hall (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Christopher Juul (batch: 2026-07-02T15:00, from: [[Artists/H/Heilung]])
- [x] Chuck D (batch: 2026-07-02T15:00, from: [[Artists/P/Prophets of Rage]])
- [x] Chuck Dukowski (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Chuck Mosley (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Claude Coleman Jr. (batch: 2026-07-02T15:00, from: [[Artists/W/Ween]])
- [x] Claude Schnell (batch: 2026-07-02T15:00, from: [[Artists/D/Dio]])
- [x] Cliff Evans (batch: 2026-07-02T15:00, from: [[Artists/C/Crystal Fairy]])
- [x] Cliff Williams (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Corpo-Mente (batch: 2026-07-02T15:00, from: [[Artists/C/Corpo-Mente]])
- [x] Cosey Fanni Tutti (batch: 2026-07-02T15:00, from: [[Artists/T/Throbbing Gristle]])
- [x] Cozy Powell (batch: 2026-07-02T15:00, from: [[Artists/R/Rainbow]])
- [x] Craig Jones (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Cronos (batch: 2026-07-02T15:00, from: [[Artists/P/Probot]])
- [x] D'arcy Wretzky (batch: 2026-07-02T15:00, from: [[Artists/T/The Smashing Pumpkins]])
- [x] Dan Baird (batch: 2026-07-02T15:00, from: [[Artists/G/Georgia Satellites]])
- [x] Daniel Bressanutti (batch: 2026-07-02T15:00, from: [[Artists/F/Front 242]])
- [x] Daniel Firth (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Daniel House (batch: 2026-07-02T15:00, from: [[Artists/S/Skin Yard]])
- [x] Daniel Löble (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Daniel Mbinga (batch: 2026-07-02T15:00, from: [[Artists/S/Snook]])
- [x] Daniel Mullback (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Daniel Mÿhr (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Dansen (batch: 2026-07-02T15:00, from: [[Artists/D/Dia Psalma]])
- [x] Darby Crash (batch: 2026-07-02T15:00, from: [[Artists/T/The Germs]])
- [x] Daron Malakian (batch: 2026-07-02T15:00, from: [[Artists/S/System of a Down]])
- [x] Darren Emerson (batch: 2026-07-02T15:00, from: [[Artists/U/Underworld]])
- [x] Darrin Mooney (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Dave Abbruzzese (batch: 2026-07-02T15:00, from: [[Artists/P/Pearl Jam]])
- [x] Dave Aju (batch: 2026-07-02T15:00, from: [[Artists/R/Red Snapper]])
- [x] Dave Alexander (batch: 2026-07-02T15:00, from: [[Artists/T/The Stooges]])
- [x] Dave Coutts (batch: 2026-07-02T15:00, from: [[Artists/T/Talk Show]])
- [x] Dave Dreiwitz (batch: 2026-07-02T15:00, from: [[Artists/W/Ween]])
- [x] Dave Elitch (batch: 2026-07-02T15:00, from: [[Artists/T/The Mars Volta]])
- [x] Dave Evans (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Dave Hewitt (batch: 2026-07-02T15:00, from: [[Artists/G/Georgia Satellites]])
- [x] Dave Krusen (batch: 2026-07-02T15:00, from: [[Artists/P/Pearl Jam]])
- [x] Dave Ogilvie (batch: 2026-07-02T15:00, from: [[Artists/S/Skinny Puppy]])
- [x] Dave Quackenbush (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Dave Rowntree (batch: 2026-07-02T15:00, from: [[Artists/B/Blur]])
- [x] David Andersson (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] David Coverdale (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] David Larsson (batch: 2026-07-02T15:00, from: [[Artists/G/Gamla Pengar]])
- [x] David Lovering (batch: 2026-07-02T15:00, from: [[Artists/P/Pixies]])
- [x] David Wallin (batch: 2026-07-02T15:00, from: [[Artists/P/Pain]])
- [x] David Wm. Sims (batch: 2026-07-02T15:00, from: [[Artists/T/The Jesus Lizard]])
- [x] Dean DeLeo (batch: 2026-07-02T15:00, from: [[Artists/A/Army of Anyone]])
- [x] Denny Seiwell (batch: 2026-07-02T15:00, from: [[Artists/W/Wings]])
- [x] Derek Sherinian (batch: 2026-07-02T15:00, from: [[Artists/D/Dream Theater]])
- [x] Derrick McKenzie (batch: 2026-07-02T15:00, from: [[Artists/J/Jamiroquai]])
- [x] Dez Cadena (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Dino Jelusick (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] DJ Ashba (batch: 2026-07-02T15:00, from: [[Artists/S/Sixx A.M.]])
- [x] DJ Lethal (batch: 2026-07-02T15:00, from: [[Artists/L/Limp Bizkit]])
- [x] DJ Lord (batch: 2026-07-02T15:00, from: [[Artists/P/Prophets of Rage]])
- [x] Doggge (batch: 2026-07-02T15:00, from: [[Artists/T/The Latin Kings]])
- [x] Don Bolles (batch: 2026-07-02T15:00, from: [[Artists/T/The Germs]])
- [x] Doogie White (batch: 2026-07-02T15:00, from: [[Artists/R/Rainbow]])
- [x] Doug Grean (batch: 2026-07-02T15:00, from: [[Artists/S/Scott Weiland & The Wildabouts]])
- [x] Dr. Matt Destruction (batch: 2026-07-02T15:00, from: [[Artists/T/The Hives]])
- [x] Dregen (batch: 2026-07-02T15:00, from: [[Artists/T/The Hellacopters]])
- [x] Duke Erikson (batch: 2026-07-02T15:00, from: [[Artists/G/Garbage]])
- [x] Dwayne Goettel (batch: 2026-07-02T15:00, from: [[Artists/S/Skinny Puppy]])
- [x] Ebbot Lundberg (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Ed Handley (batch: 2026-07-02T15:00, from: [[Artists/P/Plaid]])
- [x] Ed Simons (batch: 2026-07-02T15:00, from: [[Artists/T/The Chemical Brothers]])
- [x] Eddie Ojeda (batch: 2026-07-02T15:00, from: [[Artists/T/Twisted Sister]])
- [x] Edgar Froese (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Edward Ka-Spel (batch: 2026-07-02T15:00, from: [[Artists/T/The Legendary Pink Dots]])
- [x] Elize Ryd (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Eloy Casagrande (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Eric Dover (batch: 2026-07-02T15:00, from: [[Artists/S/Slash's Snakepit]])
- [x] Eric Erlandson (batch: 2026-07-02T15:00, from: [[Artists/H/Hole]])
- [x] Eric Kretz (batch: 2026-07-02T15:00, from: [[Artists/S/Stone Temple Pilots]])
- [x] Eric Peterson (batch: 2026-07-02T15:00, from: [[Artists/T/Testament]])
- [x] Erik Danielsson (batch: 2026-07-02T15:00, from: [[Artists/W/Watain]])
- [x] Erik Drost (batch: 2026-07-02T15:00, from: [[Artists/T/The Legendary Pink Dots]])
- [x] Ethan Buckler (batch: 2026-07-02T15:00, from: [[Artists/S/Slint]])
- [x] Exploding Plastic (batch: 2026-07-02T15:00, from: [[Artists/E/Exploding Plastic]])
- [x] F.M. Einheit (batch: 2026-07-02T15:00, from: [[Artists/E/Einstürzende Neubauten]])
- [x] Falk Maria Schlegel (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Far & Son (batch: 2026-07-02T15:00, from: [[Artists/F/Far & Son]])
- [x] Faust (batch: 2026-07-02T15:00, from: [[Artists/E/Emperor]])
- [x] Filthy (batch: 2026-07-02T15:00, from: [[Artists/A/Afasi & Filthy]])
- [x] Finn Eriksson (batch: 2026-07-02T15:00, from: [[Artists/S/S.P.O.C.K]])
- [x] Flavor Flav (batch: 2026-07-02T15:00, from: [[Artists/P/Public Enemy]])
- [x] Francis Rossi (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] Frank Bello (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Frank Delgado (batch: 2026-07-02T15:00, from: [[Artists/D/Deftones]])
- [x] Frank Gosdzik (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Franz Stahl (batch: 2026-07-02T15:00, from: [[Artists/S/Scream]])
- [x] Fredrik Andersson (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Fredrik Larsson (batch: 2026-07-02T15:00, from: [[Artists/H/Hammerfall]])
- [x] Fredrik Sandsten (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Frédéric Leclercq (batch: 2026-07-02T15:00, from: [[Artists/D/DragonForce]])
- [x] G.C. Green (batch: 2026-07-02T15:00, from: [[Artists/G/Godflesh]])
- [x] Garry Cobain (batch: 2026-07-02T15:00, from: [[Artists/T/The Future Sound of London]])
- [x] Gary Lee Conner (batch: 2026-07-02T15:00, from: [[Artists/S/Screaming Trees]])
- [x] Gary Mounfield (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Gavin Ward (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Gee Anzalone (batch: 2026-07-02T15:00, from: [[Artists/D/DragonForce]])
- [x] Geezer Butler (batch: 2026-07-02T15:00, from: [[Artists/B/Black Sabbath]])
- [x] Gene Trautmann (batch: 2026-07-02T15:00, from: [[Artists/Q/Queens of the Stone Age]])
- [x] Geoff Barrow (batch: 2026-07-02T15:00, from: [[Artists/P/Portishead]])
- [x] Allen Stiritz (batch: 2026-07-02T15:00, from: [[Artists/W/Wasted Youth]])
- [x] Gian Pyres (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Gilby Clarke (batch: 2026-07-02T15:00, from: [[Artists/S/Slash's Snakepit]])
- [x] Ginger Fish (batch: 2026-07-02T15:00, from: [[Artists/R/Rob Zombie]])
- [x] Glen Matlock (batch: 2026-07-02T15:00, from: [[Artists/S/Sex Pistols]])
- [x] Glenn Hughes (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Glenn McClelland (batch: 2026-07-02T15:00, from: [[Artists/W/Ween]])
- [x] Goon (batch: 2026-07-02T15:00, from: [[Artists/G/Goon]]) – LA-based indie rock band, artist page updated
- [x] Graham Bonnet (batch: 2026-07-02T15:00, from: [[Artists/R/Rainbow]])
- [x] Graham Coxon (batch: 2026-07-02T15:00, from: [[Artists/B/Blur]])
- [x] Greg Christian (batch: 2026-07-02T15:00, from: [[Artists/T/Testament]])
- [x] Greg Edwards (batch: 2026-07-02T15:00, from: [[Artists/P/Puscifer]])
- [x] Greg Ginn (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Greg Graffin (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Greg Hetson (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Günter Schulz (batch: 2026-07-02T15:00, from: [[Artists/S/Slick Idiot]])
- [x] Hannes van Dahl (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Harry Shearer (batch: 2026-07-02T15:00, from: [[Artists/S/Spinal Tap]])
- [x] Henrik Berggren (batch: 2026-07-02T15:00, from: [[Artists/B/Broder Daniel]])
- [x] Henrik Englund Wilhemsson (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Henrik Sandelin (batch: 2026-07-02T15:00, from: [[Artists/A/Avatar]])
- [x] Henry Ranta (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Hillel Slovak (batch: 2026-07-02T15:00, from: [[Artists/R/Red Hot Chili Peppers]])
- [x] Hiro Yamamoto (batch: 2026-07-02T15:00, from: [[Artists/S/Soundgarden]])
- [x] Hooja (batch: 2026-07-02T15:00, from: [[Artists/H/Hooja]])
- [x] Howlin' Pelle Almqvist (batch: 2026-07-02T15:00, from: [[Artists/T/The Hives]])
- [x] Hugh Whitaker (batch: 2026-07-02T15:00, from: [[Artists/T/The Housemartins]])
- [x] Håkan Jonsson (batch: 2026-07-02T15:00, from: [[Artists/W/Watain]])
- [x] Ian Astbury (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Ian Person (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Inferno (batch: 2026-07-02T15:00, from: [[Artists/B/Behemoth]])
- [x] Isaiah "Ikey" Owens (batch: 2026-07-02T15:00, from: [[Artists/T/The Mars Volta]])
- [x] Ivan de Prume (batch: 2026-07-02T15:00, from: [[Artists/W/White Zombie]])
- [x] J. Yuenger (batch: 2026-07-02T15:00, from: [[Artists/W/White Zombie]])
- [x] Jack Endino (batch: 2026-07-02T15:00, from: [[Artists/S/Skin Yard]])
- [x] Jack Gibson (batch: 2026-07-02T15:00, from: [[Artists/E/Exodus]])
- [x] Jah Wobble (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] Jake E. (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] James Kottak (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] James Michael (batch: 2026-07-02T15:00, from: [[Artists/S/Sixx A.M.]])
- [x] James Williamson (batch: 2026-07-02T15:00, from: [[Artists/T/The Stooges]])
- [x] Jamie Miller (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Jamie Stewart (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Janis Joplin (batch: 2026-07-02T15:00, from: [[Artists/J/Janis Joplin]])
- [x] Janne Parviainen (batch: 2026-07-02T15:00, from: [[Artists/E/Ensiferum]])
- [x] Jarboe (batch: 2026-07-02T15:00, from: [[Artists/S/Swans]])
- [x] Jase Edwards (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfsbane]])
- [x] Jason Cooper (batch: 2026-07-02T15:00, from: [[Artists/T/The Cure]])
- [x] Jason Finn (batch: 2026-07-02T15:00, from: [[Artists/S/Skin Yard]])
- [x] Jason Pierce (batch: 2026-07-02T15:00, from: [[Artists/S/Spiritualized]])
- [x] Jason Rullo (batch: 2026-07-02T15:00, from: [[Artists/S/Symphony X]])
- [x] Jay Bentley (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Jay Jay French (batch: 2026-07-02T15:00, from: [[Artists/T/Twisted Sister]])
- [x] Jay Kay (batch: 2026-07-02T15:00, from: [[Artists/J/Jamiroquai]])
- [x] Jay Lane (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Jay Ziskrout (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Jean-Luc De Meyer (batch: 2026-07-02T15:00, from: [[Artists/F/Front 242]])
- [x] Jean-Michel Jarre (batch: 2026-07-02T15:00, from: [[Artists/J/Jean-Michel Jarre]])
- [x] Jean-Michel Labadie (batch: 2026-07-02T15:00, from: [[Artists/G/Gojira]])
- [x] Jeff Friedl (batch: 2026-07-02T15:00, from: [[Artists/P/Puscifer]])
- [x] Jeff Hanneman (batch: 2026-07-02T15:00, from: [[Artists/S/Slayer]])
- [x] Jeff Hateley (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfsbane]])
- [x] Jeff Loomis (batch: 2026-07-02T15:00, from: [[Artists/A/Arch Enemy]])
- [x] Jeff Mills (batch: 2026-07-02T15:00, from: [[Artists/J/Jeff Mills]])
- [x] Jennie Bomb (batch: 2026-07-02T15:00, from: [[Artists/S/Sahara Hotnights]])
- [x] Jeremy Brown (batch: 2026-07-02T15:00, from: [[Artists/S/Scott Weiland & The Wildabouts]])
- [x] Jesus Mendez Jr. (batch: 2026-07-02T15:00, from: [[Artists/N/Newsted]])
- [x] Jim Kimball (batch: 2026-07-02T15:00, from: [[Artists/T/The Jesus Lizard]])
- [x] Jim Macpherson (batch: 2026-07-02T15:00, from: [[Artists/T/The Breeders]])
- [x] Jim O'Rourke (batch: 2026-07-02T15:00, from: [[Artists/S/Sonic Youth]])
- [x] Jim Sclavunos (batch: 2026-07-02T15:00, from: [[Artists/G/Grinderman]])
- [x] Jim Sellers (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Jim Ward (batch: 2026-07-02T15:00, from: [[Artists/A/At the Drive-In]])
- [x] Jimmy "The Rev" Sullivan (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Jimmy Cauty (batch: 2026-07-02T15:00, from: [[Artists/T/The KLF]])
- [x] Jo Bench (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Joacim Cans (batch: 2026-07-02T15:00, from: [[Artists/H/Hammerfall]])
- [x] Joakim Hedestedt (batch: 2026-07-02T15:00, from: [[Artists/C/Clawfinger]])
- [x] Joakim Lindbäck (batch: 2026-07-02T15:00, from: [[Artists/S/Slagsmålsklubben]])
- [x] Joakim Nilsson (batch: 2026-07-02T15:00, from: [[Artists/G/Graveyard]])
- [x] Jochen Arbeit (batch: 2026-07-02T15:00, from: [[Artists/E/Einstürzende Neubauten]])
- [x] Jocke Wallgren (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Joe Duplantier (batch: 2026-07-02T15:00, from: [[Artists/G/Gojira]])
- [x] Joe Escalante (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Joe Lynn Turner (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Joe Satriani (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Joel Ekman (batch: 2026-07-02T15:00, from: [[Artists/S/Stone Sour]])
- [x] Joey Belladonna (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Joey Castillo (batch: 2026-07-02T15:00, from: [[Artists/Q/Queens of the Stone Age]])
- [x] Johan Andreassen (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Johan DeFarfalla (batch: 2026-07-02T15:00, from: [[Artists/O/Opeth]])
- [x] Johan Eriksson (batch: 2026-07-02T15:00, from: [[Artists/S/S.P.O.C.K]])
- [x] Johan Hegg (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Johan Håkansson (batch: 2026-07-02T15:00, from: [[Artists/B/Broder Daniel]])
- [x] Johan Jøllby (batch: 2026-07-02T15:00, from: [[Artists/S/Slagsmålsklubben]])
- [x] Johan Liiva (batch: 2026-07-02T15:00, from: [[Artists/A/Arch Enemy]])
- [x] Johan Reinholdz (batch: 2026-07-02T15:00, from: [[Artists/D/Dark Tranquillity]])
- [x] Johan Söderberg (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Johanna Asplund (batch: 2026-07-02T15:00, from: [[Artists/S/Sahara Hotnights]])
- [x] Johanna Öst (batch: 2026-07-02T15:00, from: [[Artists/T/The Wondergirls]])
- [x] Johannes Eckerström (batch: 2026-07-02T15:00, from: [[Artists/A/Avatar]])
- [x] Johannes Schmoelling (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] John Alfredsson (batch: 2026-07-02T15:00, from: [[Artists/A/Avatar]])
- [x] John Bush (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] John Dolmayan (batch: 2026-07-02T15:00, from: [[Artists/S/System of a Down]])
- [x] John Edwards (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] John King (batch: 2026-07-02T15:00, from: [[Artists/T/The Dust Brothers]])
- [x] John Lydon (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] John McBain (batch: 2026-07-02T15:00, from: [[Artists/H/Hater]])
- [x] John McKay (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] John Otto (batch: 2026-07-02T15:00, from: [[Artists/L/Limp Bizkit]])
- [x] John Sykes (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] John Tempesta (batch: 2026-07-02T15:00, from: [[Artists/W/White Zombie]])
- [x] John Weiffenbach (batch: 2026-07-02T15:00, from: [[Artists/V/Void]])
- [x] Johnny A. Carter (batch: 2026-07-02T15:00, from: [[Artists/P/Pitchshifter]])
- [x] Johnny Christ (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Jon Brännström (batch: 2026-07-02T15:00, from: [[Artists/R/Refused]])
- [x] Jon Dupree (batch: 2026-07-02T15:00, from: [[Artists/V/Void]])
- [x] Jon Hudson (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Jon Klein (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Jon Lord (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Jon Votta (batch: 2026-07-02T15:00, from: [[Artists/A/Art of Anarchy]])
- [x] Jonas Björler (batch: 2026-07-02T15:00, from: [[Artists/A/At the Gates]])
- [x] Jonas Jarlsby (batch: 2026-07-02T15:00, from: [[Artists/A/Avatar]])
- [x] Jonas Lindqvist (batch: 2026-07-02T15:00, from: [[Artists/B/Broder Daniel]])
- [x] Jonas Renkse (batch: 2026-07-02T15:00, from: [[Artists/B/Bloodbath]])
- [x] Jonas Stålhammar (batch: 2026-07-02T15:00, from: [[Artists/A/At the Gates]])
- [x] Jonathan Donais (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Jonny Mattock (batch: 2026-07-02T15:00, from: [[Artists/S/Spiritualized]])
- [x] Joram Metekohy (batch: 2026-07-02T15:00, from: [[Artists/P/Project One]])
- [x] Josephine Forsman (batch: 2026-07-02T15:00, from: [[Artists/S/Sahara Hotnights]])
- [x] Josephine Wiggs (batch: 2026-07-02T15:00, from: [[Artists/T/The Breeders]])
- [x] Josh Rand (batch: 2026-07-02T15:00, from: [[Artists/S/Stone Sour]])
- [x] Juan Alderete (batch: 2026-07-02T15:00, from: [[Artists/T/The Mars Volta]])
- [x] Jukka Koskinen (batch: 2026-07-02T15:00, from: [[Artists/W/Wintersun]])
- [x] Kai Hahto (batch: 2026-07-02T15:00, from: [[Artists/W/Wintersun]])
- [x] Kai Hansen (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Kai Uwe Faust (batch: 2026-07-02T15:00, from: [[Artists/H/Heilung]])
- [x] Kalle Gustafsson Jerneholm (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Karl Willetts (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Keith Levene (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] Keith Morris (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Kelley Deal (batch: 2026-07-02T15:00, from: [[Artists/T/The Breeders]])
- [x] Kelli Dayton (batch: 2026-07-02T15:00, from: [[Artists/S/Sneaker Pimps]])
- [x] Ken Jordan (batch: 2026-07-02T15:00, from: [[Artists/T/The Crystal Method]])
- [x] Ken Sandin (batch: 2026-07-02T15:00, from: [[Artists/T/The Hellacopters]])
- [x] Kenney Jones (batch: 2026-07-02T15:00, from: [[Artists/T/The Who]])
- [x] Kenny Morris (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Kenny Withrow (batch: 2026-07-02T15:00, from: [[Artists/E/Edie Brickell & New Bohemians]])
- [x] Kent Stax (batch: 2026-07-02T15:00, from: [[Artists/S/Scream]])
- [x] Kevin Moore (batch: 2026-07-02T15:00, from: [[Artists/D/Dream Theater]])
- [x] Kevin Ratajczak (batch: 2026-07-02T15:00, from: [[Artists/E/Electric Callboy]])
- [x] Kevin Rutmanis (batch: 2026-07-02T15:00, from: [[Artists/T/The Melvins]])
- [x] Kim Deal (batch: 2026-07-02T15:00, from: [[Artists/P/Pixies]])
- [x] Kim Pettersson (batch: 2026-07-02T15:00, from: [[Artists/O/Opeth]])
- [x] King Diamond (batch: 2026-07-02T15:00, from: [[Artists/P/Probot]])
- [x] Kjetil Haraldstad (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Koen Groeneveld (batch: 2026-07-02T15:00, from: [[Artists/T/Technohead]])
- [x] Kransen (batch: 2026-07-02T15:00, from: [[Artists/D/Dia Psalma]])
- [x] Kris Weston (batch: 2026-07-02T15:00, from: [[Artists/T/The Orb]])
- [x] Kristen Pfaff (batch: 2026-07-02T15:00, from: [[Artists/H/Hole]])
- [x] Kurt Glori (batch: 2026-07-02T15:00, from: [[Artists/E/Excessive Force]])
- [x] Larry Dunn (batch: 2026-07-02T15:00, from: [[Artists/E/Earth, Wind & Fire]])
- [x] Larry LaLonde (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Larry Mullen Jr. (batch: 2026-07-02T15:00, from: [[Artists/U/U2]])
- [x] Lee Ranaldo (batch: 2026-07-02T15:00, from: [[Artists/S/Sonic Youth]])
- [x] Leeroy Thornhill (batch: 2026-07-02T15:00, from: [[Artists/T/The Prodigy]])
- [x] Les (batch: 2026-07-02T15:00, from: [[Artists/B/Behemoth]])
- [x] Les Claypool (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Liam Howe (batch: 2026-07-02T15:00, from: [[Artists/S/Sneaker Pimps]])
- [x] Likk (batch: 2026-07-02T15:00, from: [[Artists/L/Likk]])
- [x] Lime (batch: 2026-07-02T15:00, from: [[Artists/S/SL2]])
- [x] Lina Ericsson (batch: 2026-07-02T15:00, from: [[Artists/T/The Wondergirls]])
- [x] Lindsay Schoolcraft (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Lorna Doom (batch: 2026-07-02T15:00, from: [[Artists/T/The Germs]])
- [x] Louie Clemente (batch: 2026-07-02T15:00, from: [[Artists/T/Testament]])
- [x] Lu Edmonds (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] Luc Van Acker (batch: 2026-07-02T15:00, from: [[Artists/R/Revolting Cocks]])
- [x] Lucia Cifarelli (batch: 2026-07-02T15:00, from: [[Artists/S/Schwein]])
- [x] Lux Interior (batch: 2026-07-02T15:00, from: [[Artists/T/The Cramps]])
- [x] Lætitia Sadier (batch: 2026-07-02T15:00, from: [[Artists/S/Stereolab]])
- [x] M. Shadows (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Mac McNeilly (batch: 2026-07-02T15:00, from: [[Artists/T/The Jesus Lizard]])
- [x] Mackan (batch: 2026-07-02T15:00, from: [[Artists/D/Dia Psalma]])
- [x] Magnus Björklund (batch: 2026-07-02T15:00, from: [[Artists/R/Refused]])
- [x] Magnus Höggren (batch: 2026-07-02T15:00, from: [[Artists/R/Refused]])
- [x] Malcolm Young (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Malin Ekholm (batch: 2026-07-02T15:00, from: [[Artists/T/The Wondergirls]])
- [x] Marc Hudson (batch: 2026-07-02T15:00, from: [[Artists/D/DragonForce]])
- [x] Marc Reign (batch: 2026-07-02T15:00, from: [[Artists/D/Destruction]])
- [x] Marek Šmerda (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Maria Andersson (batch: 2026-07-02T15:00, from: [[Artists/S/Sahara Hotnights]])
- [x] Maria Franz (batch: 2026-07-02T15:00, from: [[Artists/H/Heilung]])
- [x] Mario Duplantier (batch: 2026-07-02T15:00, from: [[Artists/G/Gojira]])
- [x] Mark Arm (batch: 2026-07-02T15:00, from: [[Artists/G/Green River]])
- [x] Mark Brzezicki (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Mark Clayden (batch: 2026-07-02T15:00, from: [[Artists/P/Pitchshifter]])
- [x] Mark Deutrom (batch: 2026-07-02T15:00, from: [[Artists/T/The Melvins]])
- [x] Mark Eliopulos (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Mark Evans (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Mark Mendoza (batch: 2026-07-02T15:00, from: [[Artists/T/Twisted Sister]])
- [x] Mark Pickerel (batch: 2026-07-02T15:00, from: [[Artists/S/Screaming Trees]])
- [x] Markus Grosskopf (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Markus Toivonen (batch: 2026-07-02T15:00, from: [[Artists/E/Ensiferum]])
- [x] Martijn de Kleer (batch: 2026-07-02T15:00, from: [[Artists/T/The Legendary Pink Dots]])
- [x] Martin Duffy (batch: 2026-07-02T15:00, from: [[Artists/P/Primal Scream]])
- [x] Martin Hederos (batch: 2026-07-02T15:00, from: [[Artists/T/The Soundtrack of Our Lives]])
- [x] Martin Henriksson (batch: 2026-07-02T15:00, from: [[Artists/D/Dark Tranquillity]])
- [x] Martin Kearns (batch: 2026-07-02T15:00, from: [[Artists/B/Bolt Thrower]])
- [x] Martin Larsson (batch: 2026-07-02T15:00, from: [[Artists/A/At the Gates]])
- [x] Martin Watson (batch: 2026-07-02T15:00, from: [[Artists/S/Sweet Exorcist]])
- [x] Martyn P. Casey (batch: 2026-07-02T15:00, from: [[Artists/G/Grinderman]])
- [x] Mary Hansen (batch: 2026-07-02T15:00, from: [[Artists/S/Stereolab]])
- [x] Mat Mitchell (batch: 2026-07-02T15:00, from: [[Artists/P/Puscifer]])
- [x] Mats Häll (batch: 2026-07-02T15:00, from: [[Artists/G/Gamla Pengar]])
- [x] Mats Persson (batch: 2026-07-02T15:00, from: [[Artists/T/Ten Inch Men]])
- [x] Matt Chamberlain (batch: 2026-07-02T15:00, from: [[Artists/E/Edie Brickell & New Bohemians]])
- [x] Matt Lukin (batch: 2026-07-02T15:00, from: [[Artists/T/The Melvins]])
- [x] Matthew Greywolf (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Mattias Hellberg (batch: 2026-07-02T15:00, from: [[Artists/D/Death Hawks]])
- [x] Max Cavalera (batch: 2026-07-02T15:00, from: [[Artists/P/Probot]])
- [x] Melissa Auf der Maur (batch: 2026-07-02T15:00, from: [[Artists/T/The Smashing Pumpkins]])
- [x] Melvin Gibbs (batch: 2026-07-02T15:00, from: [[Artists/R/Rollins Band]])
- [x] Michael Anthony (batch: 2026-07-02T15:00, from: [[Artists/V/Van Halen]])
- [x] Michael Devin (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Michael Kiske (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Michael Lepond (batch: 2026-07-02T15:00, from: [[Artists/S/Symphony X]])
- [x] Michael McKean (batch: 2026-07-02T15:00, from: [[Artists/S/Spinal Tap]])
- [x] Michael Pinnella (batch: 2026-07-02T15:00, from: [[Artists/S/Symphony X]])
- [x] Michael Romeo (batch: 2026-07-02T15:00, from: [[Artists/S/Symphony X]])
- [x] Michael Weikath (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Mick Harvey (batch: 2026-07-02T15:00, from: [[Artists/T/The Birthday Party]])
- [x] Mick Thomson (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Micke Dahlén (batch: 2026-07-02T15:00, from: [[Artists/C/Clawfinger]])
- [x] Micky Moody (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Mikael Hedlund (batch: 2026-07-02T15:00, from: [[Artists/H/Hypocrisy]])
- [x] Mikael Niklasson (batch: 2026-07-02T15:00, from: [[Artists/D/Dark Tranquillity]])
- [x] Mikael Wiehe (batch: 2026-07-02T15:00, from: [[Artists/H/Hoola Bandoola Band]])
- [x] Mikael Åström (batch: 2026-07-02T15:00, from: [[Artists/D/Death Hawks]])
- [x] Mike Banks (batch: 2026-07-02T15:00, from: [[Artists/U/Underground Resistance]])
- [x] Mike Bordin (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Mike Dimkich (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Mike Riggs (batch: 2026-07-02T15:00, from: [[Artists/R/Rob Zombie]])
- [x] Mike Simpson (batch: 2026-07-02T15:00, from: [[Artists/T/The Dust Brothers]])
- [x] Mike Smith (batch: 2026-07-02T15:00, from: [[Artists/L/Limp Bizkit]])
- [x] Mike Starr (batch: 2026-07-02T15:00, from: [[Artists/A/Alice in Chains]])
- [x] Mike Watt (batch: 2026-07-02T15:00, from: [[Artists/T/The Stooges]])
- [x] Montego Joe (batch: 2026-07-02T15:00, from: [[Artists/T/Tom Tom Club]])
- [x] Morten Løwe Sørensen (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Mustis (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Myles Heskett (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfmother]])
- [x] N.U. Unruh (batch: 2026-07-02T15:00, from: [[Artists/E/Einstürzende Neubauten]])
- [x] Natasha Shneider (batch: 2026-07-02T15:00, from: [[Artists/E/Eleven]])
- [x] Nate Mendel (batch: 2026-07-02T15:00, from: [[Artists/F/Foo Fighters]])
- [x] Neil Turbin (batch: 2026-07-02T15:00, from: [[Artists/A/Anthrax]])
- [x] Nic Endo (batch: 2026-07-02T15:00, from: [[Artists/A/Atari Teenage Riot]])
- [x] Nicholas Barker (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Nicholaus Arson (batch: 2026-07-02T15:00, from: [[Artists/T/The Hives]])
- [x] Nick Barker (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Nick Knox (batch: 2026-07-02T15:00, from: [[Artists/T/The Cramps]])
- [x] Nick Simper (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Niels van Hoorn (batch: 2026-07-02T15:00, from: [[Artists/T/The Legendary Pink Dots]])
- [x] Nigel Preston (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Nils Molin (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Ola Flink (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Ola Frick (batch: 2026-07-02T15:00, from: [[Artists/T/Ten Inch Men]])
- [x] Olavi Mikkonen (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Oliver Riedel (batch: 2026-07-02T15:00, from: [[Artists/R/Rammstein]])
- [x] Olle Nyberg (batch: 2026-07-02T15:00, from: [[Artists/H/Hoola Bandoola Band]])
- [x] Olof Dreijer (batch: 2026-07-02T15:00, from: [[Artists/T/The Knife]])
- [x] Olof Mörck (batch: 2026-07-02T15:00, from: [[Artists/A/Amaranthe]])
- [x] Orion (batch: 2026-07-02T15:00, from: [[Artists/B/Behemoth]])
- [x] Orvar Säfström (batch: 2026-07-02T15:00, from: [[Artists/E/Entombed]])
- [x] Oskar Bergenheim (batch: 2026-07-02T15:00, from: [[Artists/G/Graveyard]])
- [x] Oskar Lindgren (batch: 2026-07-02T15:00, from: [[Artists/S/Snook]])
- [x] Oskar Montelius (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Page Hamilton (batch: 2026-07-02T15:00, from: [[Artists/H/Helmet]])
- [x] Pat Smear (batch: 2026-07-02T15:00, from: [[Artists/F/Foo Fighters]])
- [x] Patrick Codenys (batch: 2026-07-02T15:00, from: [[Artists/F/Front 242]])
- [x] Patrik Hansson (batch: 2026-07-02T15:00, from: [[Artists/S/Sanctum]])
- [x] Patrik Nystedt (batch: 2026-07-02T15:00, from: [[Artists/T/Ten Inch Men]])
- [x] Patty Schemel (batch: 2026-07-02T15:00, from: [[Artists/H/Hole]])
- [x] Paul Bostaph (batch: 2026-07-02T15:00, from: [[Artists/S/Slayer]])
- [x] Paul Cook (batch: 2026-07-02T15:00, from: [[Artists/S/Sex Pistols]])
- [x] Paul Gray (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Paul Haslinger (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Paul Hinojos (batch: 2026-07-02T15:00, from: [[Artists/A/At the Drive-In]])
- [x] Paul Landers (batch: 2026-07-02T15:00, from: [[Artists/F/Feeling B]])
- [x] Paul Masvidal (batch: 2026-07-02T15:00, from: [[Artists/D/Death]])
- [x] Paul Samson (batch: 2026-07-02T15:00, from: [[Artists/S/Samson]])
- [x] Paula P-Orridge (batch: 2026-07-02T15:00, from: [[Artists/P/Psychic TV]])
- [x] Pelle Forsberg (batch: 2026-07-02T15:00, from: [[Artists/W/Watain]])
- [x] Pete Finestone (batch: 2026-07-02T15:00, from: [[Artists/B/Bad Religion]])
- [x] Peter Baumann (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Peter Gordeno (batch: 2026-07-02T15:00, from: [[Artists/D/Depeche Mode]])
- [x] Peter Pedersen (batch: 2026-07-02T15:00, from: [[Artists/H/Hoola Bandoola Band]])
- [x] Peter Stahl (batch: 2026-07-02T15:00, from: [[Artists/S/Scream]])
- [x] Peter Wichers (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Phil Calvert (batch: 2026-07-02T15:00, from: [[Artists/T/The Birthday Party]])
- [x] Phil Knight (batch: 2026-07-02T15:00, from: [[Artists/T/The Legendary Pink Dots]])
- [x] Phil Rudd (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Phil Winter (batch: 2026-07-02T15:00, from: [[Artists/W/Wrangler]])
- [x] Pierre von Känel (batch: 2026-07-02T15:00, from: [[Artists/T/The Inchtabokatables]])
- [x] Piggy D. (batch: 2026-07-02T15:00, from: [[Artists/R/Rob Zombie]])
- [x] Pjäsen (batch: 2026-07-02T15:00, from: [[Artists/D/Dia Psalma]])
- [x] Poison Ivy (batch: 2026-07-02T15:00, from: [[Artists/T/The Cramps]])
- [x] Pontus Norgren (batch: 2026-07-02T15:00, from: [[Artists/H/Hammerfall]])
- [x] Porl Thompson (batch: 2026-07-02T15:00, from: [[Artists/T/The Cure]])
- [x] Pär Hansson (batch: 2026-07-02T15:00, from: [[Artists/R/Refused]])
- [x] Pär Sundström (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Ralph Johnson (batch: 2026-07-02T15:00, from: [[Artists/E/Earth, Wind & Fire]])
- [x] Randy DeLay (batch: 2026-07-02T15:00, from: [[Artists/G/Georgia Satellites]])
- [x] Randy Rhoads (batch: 2026-07-02T15:00, from: [[Artists/O/Ozzy Osbourne]])
- [x] Rasmus Ehrnborn (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Ray Luzier (batch: 2026-07-02T15:00, from: [[Artists/A/Army of Anyone]])
- [x] Raymond Herrera (batch: 2026-07-02T15:00, from: [[Artists/F/Fear Factory]])
- [x] Reb Beach (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Rich Conte (batch: 2026-07-02T15:00, from: [[Artists/O/Overkill]])
- [x] Richard Christy (batch: 2026-07-02T15:00, from: [[Artists/D/Death]])
- [x] Rick Parfitt (batch: 2026-07-02T15:00, from: [[Artists/S/Status Quo]])
- [x] Rick Smith (batch: 2026-07-02T15:00, from: [[Artists/U/Underworld]])
- [x] Rikard Edlund (batch: 2026-07-02T15:00, from: [[Artists/G/Graveyard]])
- [x] Rikard Sundén (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Ritchie Blackmore (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Rob Brown (batch: 2026-07-02T15:00, from: [[Artists/A/Autechre]])
- [x] Rob Harris (batch: 2026-07-02T15:00, from: [[Artists/J/Jamiroquai]])
- [x] Robert Dahlqvist (batch: 2026-07-02T15:00, from: [[Artists/T/The Hellacopters]])
- [x] Robert DeLeo (batch: 2026-07-02T15:00, from: [[Artists/A/Army of Anyone]])
- [x] Robert Hood (batch: 2026-07-02T15:00, from: [[Artists/U/Underground Resistance]])
- [x] Robert Roth (batch: 2026-07-02T15:00, from: [[Artists/T/Truly]])
- [x] Robo (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Rod Evans (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Roddy Bottum (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Roel van Helden (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Roger O'Donnell (batch: 2026-07-02T15:00, from: [[Artists/T/The Cure]])
- [x] Ron Asheton (batch: 2026-07-02T15:00, from: [[Artists/T/The Stooges]])
- [x] Ron Mael (batch: 2026-07-02T15:00, from: [[Artists/S/Sparks]])
- [x] Ron Reyes (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Ron Thal (batch: 2026-07-02T15:00, from: [[Artists/A/Art of Anarchy]])
- [x] Rowland S. Howard (batch: 2026-07-02T15:00, from: [[Artists/T/The Birthday Party]])
- [x] Roy Mayorga (batch: 2026-07-02T15:00, from: [[Artists/S/Stone Sour]])
- [x] Rudi Moser (batch: 2026-07-02T15:00, from: [[Artists/E/Einstürzende Neubauten]])
- [x] Russell Allen (batch: 2026-07-02T15:00, from: [[Artists/S/Symphony X]])
- [x] Russell Mael (batch: 2026-07-02T15:00, from: [[Artists/S/Sparks]])
- [x] Sal Abruscato (batch: 2026-07-02T15:00, from: [[Artists/T/Type O Negative]])
- [x] Salla (batch: 2026-07-02T15:00, from: [[Artists/T/The Latin Kings]])
- [x] Sam Rivers (batch: 2026-07-02T15:00, from: [[Artists/L/Limp Bizkit]])
- [x] Sami Hinkka (batch: 2026-07-02T15:00, from: [[Artists/E/Ensiferum]])
- [x] Sammy Hagar (batch: 2026-07-02T15:00, from: [[Artists/V/Van Halen]])
- [x] Sandra Lauer (batch: 2026-07-02T15:00, from: [[Artists/E/Enigma]])
- [x] Sascha Gerstner (batch: 2026-07-02T15:00, from: [[Artists/H/Helloween]])
- [x] Sascha Konietzko (batch: 2026-07-02T15:00, from: [[Artists/S/Schwein]])
- [x] Scott Asheton (batch: 2026-07-02T15:00, from: [[Artists/T/The Stooges]])
- [x] Scott Firth (batch: 2026-07-02T15:00, from: [[Artists/P/Public Image Ltd]])
- [x] Scott Garrett (batch: 2026-07-02T15:00, from: [[Artists/T/The Cult]])
- [x] Scott Kirkland (batch: 2026-07-02T15:00, from: [[Artists/T/The Crystal Method]])
- [x] Scott Stapp (batch: 2026-07-02T15:00, from: [[Artists/A/Art of Anarchy]])
- [x] Sean Booth (batch: 2026-07-02T15:00, from: [[Artists/A/Autechre]])
- [x] Sean Finnegan (batch: 2026-07-02T15:00, from: [[Artists/V/Void]])
- [x] Sean Kinney (batch: 2026-07-02T15:00, from: [[Artists/A/Alice in Chains]])
- [x] Sean Reinert (batch: 2026-07-02T15:00, from: [[Artists/D/Death]])
- [x] Sergio Vega (batch: 2026-07-02T15:00, from: [[Artists/D/Deftones]])
- [x] Serj Tankian (batch: 2026-07-02T15:00, from: [[Artists/S/System of a Down]])
- [x] Shannon Hamm (batch: 2026-07-02T15:00, from: [[Artists/D/Death]])
- [x] Sharlee D'Angelo (batch: 2026-07-02T15:00, from: [[Artists/A/Arch Enemy]])
- [x] Shavo Odadjian (batch: 2026-07-02T15:00, from: [[Artists/S/System of a Down]])
- [x] Shawn Crahan (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Shirley Manson (batch: 2026-07-02T15:00, from: [[Artists/G/Garbage]])
- [x] Sid Vicious (batch: 2026-07-02T15:00, from: [[Artists/S/Sex Pistols]])
- [x] Sid Wilson (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Sim Cain (batch: 2026-07-02T15:00, from: [[Artists/R/Rollins Band]])
- [x] Skeeter Thompson (batch: 2026-07-02T15:00, from: [[Artists/S/Scream]])
- [x] Slipmatt (batch: 2026-07-02T15:00, from: [[Artists/S/SL2]])
- [x] Sofia Lundberg (batch: 2026-07-02T15:00, from: [[Artists/T/The Wondergirls]])
- [x] Stan Cullimore (batch: 2026-07-02T15:00, from: [[Artists/T/The Housemartins]])
- [x] Stefan Schwarzmann (batch: 2026-07-02T15:00, from: [[Artists/D/Destruction]])
- [x] Stefan Wittke (batch: 2026-07-02T15:00, from: [[Artists/T/The Inchtabokatables]])
- [x] Steve "Danger" Ellett (batch: 2026-07-02T15:00, from: [[Artists/W/Wolfsbane]])
- [x] Steve "Fuzz" Kmak (batch: 2026-07-02T15:00, from: [[Artists/D/Disturbed]])
- [x] Steve DePace (batch: 2026-07-02T15:00, from: [[Artists/F/Flipper]])
- [x] Steve Di Giorgio (batch: 2026-07-02T15:00, from: [[Artists/T/Testament]])
- [x] Steve DiGiorgio (batch: 2026-07-02T15:00, from: [[Artists/D/Death]])
- [x] Steve Jones (batch: 2026-07-02T15:00, from: [[Artists/S/Sex Pistols]])
- [x] Steve Jordan (batch: 2026-07-02T15:00, from: [[Artists/T/The Rolling Stones]])
- [x] Steve Marker (batch: 2026-07-02T15:00, from: [[Artists/G/Garbage]])
- [x] Steve Morse (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Steve Shelley (batch: 2026-07-02T15:00, from: [[Artists/S/Sonic Youth]])
- [x] Steve Souza (batch: 2026-07-02T15:00, from: [[Artists/E/Exodus]])
- [x] Steve Turner (batch: 2026-07-02T15:00, from: [[Artists/G/Green River]])
- [x] Steven Scales (batch: 2026-07-02T15:00, from: [[Artists/T/Tom Tom Club]])
- [x] Steven Severin (batch: 2026-07-02T15:00, from: [[Artists/S/Siouxsie and the Banshees]])
- [x] Steven Shane McDonald (batch: 2026-07-02T15:00, from: [[Artists/T/The Melvins]])
- [x] Stuart Anstis (batch: 2026-07-02T15:00, from: [[Artists/C/Cradle of Filth]])
- [x] Stuart Toolin (batch: 2026-07-02T15:00, from: [[Artists/P/Pitchshifter]])
- [x] Stuart Zechman (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Stéfane Funèbre (batch: 2026-07-02T15:00, from: [[Artists/P/Powerwolf]])
- [x] Sven Karlsson (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Sven Plaggemeier (batch: 2026-07-02T15:00, from: [[Artists/T/The Inchtabokatables]])
- [x] Sylvain Coudret (batch: 2026-07-02T15:00, from: [[Artists/S/Soilwork]])
- [x] Synyster Gates (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Tanya Donelly (batch: 2026-07-02T15:00, from: [[Artists/T/The Breeders]])
- [x] Taylor Hawkins (batch: 2026-07-02T15:00, from: [[Artists/F/Foo Fighters]])
- [x] Ted Falconi (batch: 2026-07-02T15:00, from: [[Artists/F/Flipper]])
- [x] Ted Lundström (batch: 2026-07-02T15:00, from: [[Artists/A/Amon Amarth]])
- [x] Teemu Mäntysaari (batch: 2026-07-02T15:00, from: [[Artists/W/Wintersun]])
- [x] Terminator X (batch: 2026-07-02T15:00, from: [[Artists/P/Public Enemy]])
- [x] Terry Balsamo (batch: 2026-07-02T15:00, from: [[Artists/L/Limp Bizkit]])
- [x] Thighpaulsandra (batch: 2026-07-02T15:00, from: [[Artists/S/Spiritualized]])
- [x] Thomas Fehlmann (batch: 2026-07-02T15:00, from: [[Artists/T/The Orb]])
- [x] Thomas Mark (batch: 2026-07-02T15:00, from: [[Artists/T/The Inchtabokatables]])
- [x] Thomas Pridgen (batch: 2026-07-02T15:00, from: [[Artists/T/The Mars Volta]])
- [x] Thorsten Quaeschning (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Thunderstick (batch: 2026-07-02T15:00, from: [[Artists/S/Samson]])
- [x] Tim Alexander (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Tim Gane (batch: 2026-07-02T15:00, from: [[Artists/S/Stereolab]])
- [x] Tim Yeung (batch: 2026-07-02T15:00, from: [[Artists/D/Divine Heresy]])
- [x] Tim Öhrström (batch: 2026-07-02T15:00, from: [[Artists/A/Avatar]])
- [x] Tobias Egervall (batch: 2026-07-02T15:00, from: [[Artists/D/Death Hawks]])
- [x] Todd Brashear (batch: 2026-07-02T15:00, from: [[Artists/S/Slint]])
- [x] Todd Huth (batch: 2026-07-02T15:00, from: [[Artists/P/Primus]])
- [x] Todd Trainer (batch: 2026-07-02T15:00, from: [[Artists/S/Shellac]])
- [x] Tom Angelripper (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Tom Chant (batch: 2026-07-02T15:00, from: [[Artists/R/Red Snapper]])
- [x] Tom Hunting (batch: 2026-07-02T15:00, from: [[Artists/E/Exodus]])
- [x] Tom Rowlands (batch: 2026-07-02T15:00, from: [[Artists/T/The Chemical Brothers]])
- [x] Tommy Aldridge (batch: 2026-07-02T15:00, from: [[Artists/W/Whitesnake]])
- [x] Tommy Black (batch: 2026-07-02T15:00, from: [[Artists/S/Scott Weiland & The Wildabouts]])
- [x] Tommy Bolin (batch: 2026-07-02T15:00, from: [[Artists/D/Deep Purple]])
- [x] Tommy Clufetos (batch: 2026-07-02T15:00, from: [[Artists/R/Rob Zombie]])
- [x] Tommy Johansson (batch: 2026-07-02T15:00, from: [[Artists/S/Sabaton]])
- [x] Tommy Vext (batch: 2026-07-02T15:00, from: [[Artists/D/Divine Heresy]])
- [x] Tony Hajjar (batch: 2026-07-02T15:00, from: [[Artists/A/At the Drive-In]])
- [x] Tony Laureano (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Tony Scaglione (batch: 2026-07-02T15:00, from: [[Artists/S/Slayer]])
- [x] Tracy Pew (batch: 2026-07-02T15:00, from: [[Artists/T/The Birthday Party]])
- [x] Trance Dance (batch: 2026-07-02T15:00, from: [[Artists/T/Trance Dance]])
- [x] Travis Neal (batch: 2026-07-02T15:00, from: [[Artists/D/Divine Heresy]])
- [x] Truls Mörck (batch: 2026-07-02T15:00, from: [[Artists/G/Graveyard]])
- [x] Twin Pigs (batch: 2026-07-02T15:00, from: [[Artists/T/Twin Pigs]])
- [x] Tyron Downie (batch: 2026-07-02T15:00, from: [[Artists/T/Tom Tom Club]])
- [x] Uffe Cederlund (batch: 2026-07-02T15:00, from: [[Artists/E/Entombed]])
- [x] Ulf Nyberg (batch: 2026-07-02T15:00, from: [[Artists/R/Refused]])
- [x] Vadim Pruzhanov (batch: 2026-07-02T15:00, from: [[Artists/D/DragonForce]])
- [x] Van Conner (batch: 2026-07-02T15:00, from: [[Artists/S/Screaming Trees]])
- [x] Vigilante Carlstroem (batch: 2026-07-02T15:00, from: [[Artists/T/The Hives]])
- [x] Vince Votta (batch: 2026-07-02T15:00, from: [[Artists/A/Art of Anarchy]])
- [x] Volcano (batch: 2026-07-02T15:00, from: [[Artists/V/Volcano]])
- [x] Vortex (batch: 2026-07-02T15:00, from: [[Artists/D/Dimmu Borgir]])
- [x] Walter Flakus (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Warren Fitzgerald (batch: 2026-07-02T15:00, from: [[Artists/T/The Vandals]])
- [x] Wes Burt-Martin (batch: 2026-07-02T15:00, from: [[Artists/E/Edie Brickell & New Bohemians]])
- [x] Will Heggie (batch: 2026-07-02T15:00, from: [[Artists/C/Cocteau Twins]])
- [x] Will Shatter (batch: 2026-07-02T15:00, from: [[Artists/F/Flipper]])
- [x] Will White (batch: 2026-07-02T15:00, from: [[Artists/P/Propellerheads]])
- [x] Willem Rebergen (batch: 2026-07-02T15:00, from: [[Artists/P/Project One]])
- [x] William DuVall (batch: 2026-07-02T15:00, from: [[Artists/A/Alice in Chains]])
- [x] Yva Las Vegass (batch: 2026-07-02T15:00, from: [[Artists/S/Sweet 75]])
- [x] Zacky Vengeance (batch: 2026-07-02T15:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Zak Starkey (batch: 2026-07-02T15:00, from: [[Artists/T/The Who]])
- [x] Zenny Bomb (batch: 2026-07-02T15:00, from: [[Artists/C/Combichrist]])
- [x] ZP Theart (batch: 2026-07-02T15:00, from: [[Artists/D/DragonForce]])
- [x] Øystein Brun (batch: 2026-07-02T15:00, from: [[Artists/B/Borknagar]])
- [x] Dan Clements (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Shaun Ross (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Greg Cerwonka (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Damon DeLaPaz (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Evan Warech (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Rickey Pallamino (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Greg Saenz (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Brandon Rudley (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Max Asher (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Vic Caruso (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Alex Barreto (batch: 2026-07-02T05:00, from: [[Artists/E/Excel]])
- [x] Jake Duzsik (batch: 2026-07-02T05:00, from: [[Artists/H/HEALTH]])
- [x] John Famiglietti (batch: 2026-07-02T05:00, from: [[Artists/H/HEALTH]])
- [x] BJ Miller (batch: 2026-07-02T05:00, from: [[Artists/H/HEALTH]])
- [x] Jupiter Keyes (batch: 2026-07-02T05:00, from: [[Artists/H/HEALTH]])
- [x] Dave Silva (batch: 2026-07-02T05:00, from: [[Artists/M/My Head]])
- [x] George Clinton (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Bootsy Collins (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Eddie Hazel (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Garry Shider (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Michael Hampton (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Fred Wesley (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Maceo Parker (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Billy Bass Nelson (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Cordell Mosson (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Ray Davis (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Fuzzy Haskins (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Calvin Simon (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Grady Thomas (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Junie Morrison (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Tiki Fulwood (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Jerome Brailey (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Glenn Goins (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Jimmy Page (batch: 2026-07-02T05:00, from: [[Artists/R/Roy Harper]])
- [x] Etty Lau Farrell (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] Nuno Bettencourt (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] Carl Restivo (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] Kevin Figueiredo (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] Nick Perri (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] John Frusciante (batch: 2026-07-02T05:00, from: [[Artists/S/Satellite Party]])
- [x] Aaron Lewis (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Johnny April (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Jon Wysocki (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Sal Giancarelli (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Fred Durst (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Jeramie Kling (batch: 2026-07-01T22:00, from: [[Artists/O/Overkill]])
- [x] Mathias Lodmalm (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Zrinko Culjak (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Juha Sievers (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Christian Saarinen (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Anton Hedberg (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Markus Nordberg (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Thomas Josefsson (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Mattias Borgh (batch: 2026-07-02T01:00, from: [[Artists/C/Cemetary]])
- [x] Marcus Sjöberg (batch: 2026-07-01T23:00, from: [[Artists/W/Wintergatan]])
- [x] David Zandén (batch: 2026-07-01T23:00, from: [[Artists/W/Wintergatan]])
- [x] Evelina Hägglund (batch: 2026-07-01T23:00, from: [[Artists/W/Wintergatan]])
- [x] Julia Jonas (batch: 2026-07-01T23:00, from: [[Artists/W/Wintergatan]])
- [x] Anders Molin (batch: 2026-07-01T23:00, from: [[Artists/D/Detektivbyrån]])
- [x] Jon Ekström (batch: 2026-07-01T23:00, from: [[Artists/D/Detektivbyrån]])
- [x] Denis Bélanger (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Michel Langevin (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Denis D'Amour (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Jean-Yves Thériault (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Daniel Mongrain (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Dominic Laroche (batch: 2026-07-01T22:00, from: [[Artists/V/Voivod]])
- [x] Eric Knutson (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Kelly David-Smith (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Michael Gilbert (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Steve Conley (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Ken Mary (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Bill Bodily (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Michael Spencer (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Jason Bittner (batch: 2026-07-01T22:00, from: [[Artists/F/Flotsam and Jetsam]])
- [x] Jesus Mendez Jr. (batch: 2026-07-01T22:00, from: [[Artists/N/Newsted]])
- [x] Jessie Farnsworth (batch: 2026-07-01T22:00, from: [[Artists/N/Newsted]])
- [x] Mike Mushok (batch: 2026-07-01T22:00, from: [[Artists/N/Newsted]])
- [x] James Hetfield (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Lars Ulrich (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Dave Mustaine (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Cliff Burton (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Jason Newsted (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Ron McGovney (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Ian Hunter (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Mick Ralphs (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Verden Allen (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Overend Watts (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Dale Griffin (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Luther Grosvenor (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Morgan Fisher (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Dave Brock (batch: 2026-07-01T20:00, from: [[Artists/H/Hawkwind]])
- [x] Nik Turner (batch: 2026-07-01T20:00, from: [[Artists/H/Hawkwind]])
- [x] Simon King (batch: 2026-07-01T20:00, from: [[Artists/H/Hawkwind]])
- [x] Del Dettmar (batch: 2026-07-01T20:00, from: [[Artists/H/Hawkwind]])
- [x] Robert Calvert (batch: 2026-07-01T20:00, from: [[Artists/H/Hawkwind]])
- [x] Marcus Jidell (batch: 2026-07-01T20:00, from: [[Artists/A/Avatarium]])
- [x] Carl Westholm (batch: 2026-07-01T20:00, from: [[Artists/A/Avatarium]])
- [x] Jennie-Ann Smith (batch: 2026-07-01T20:00, from: [[Artists/A/Avatarium]])
- [x] Lars Sköld (batch: 2026-07-01T20:00, from: [[Artists/A/Avatarium]])
- [x] Mats Rydström (batch: 2026-07-01T20:00, from: [[Artists/A/Avatarium]])
- [x] Johan Edlund (batch: 2026-07-01T20:00, from: [[Artists/T/Tiamat]])
- [x] Sven Roger Öjersson (batch: 2026-07-01T20:00, from: [[Artists/T/Tiamat]])
- [x] Jack White (batch: 2026-07-01T00:00, from: [[Artists/T/The White Stripes]])
- [x] Richard Taylor (batch: 2026-07-01T00:00, from: [[Artists/B/British Lion]])
- [x] David Hawkins (batch: 2026-07-01T00:00, from: [[Artists/B/British Lion]])
- [x] Graeme Leslie (batch: 2026-07-01T00:00, from: [[Artists/B/British Lion]])
- [x] Pete DiStefano (batch: 2026-07-01T00:00, from: [[Artists/P/Porno for Pyros]])
- [x] Mark Watrous (batch: 2026-07-01T00:00, from: [[Artists/T/The Raconteurs]])
- [x] Tinna Karlsdotter (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Joseph Skansås (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Emma Gelotte (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Michael Håkansson (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Fredrik Johansson (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Peter Mårdklint (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Anders Janfalk (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Jonna Sailon (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Alexander Ridha (batch: 2026-07-01T16:00, from: [[Artists/N/Nine Inch Noize]])
- [x] Rico Nasty (batch: 2026-07-01T16:00, from: [[Artists/N/Nine Inch Noize]])
- [x] Reeves Gabrels (batch: 2026-07-01T17:00, from: [[Artists/T/Tin Machine]])
- [x] Tony Sales (batch: 2026-07-01T17:00, from: [[Artists/T/Tin Machine]])
- [x] Hunt Sales (batch: 2026-07-01T17:00, from: [[Artists/T/Tin Machine]])
- [x] Kevin Armstrong (batch: 2026-07-01T17:00, from: [[Artists/T/Tin Machine]])
- [x] Eric Schermerhorn (batch: 2026-07-01T17:00, from: [[Artists/T/Tin Machine]])
- [x] Mick Ronson (batch: 2026-07-01T18:00, from: [[Artists/D/David Bowie]])
- [x] Trevor Bolder (batch: 2026-07-01T18:00, from: [[Artists/D/David Bowie]])
- [x] Woody Woodmansey (batch: 2026-07-01T18:00, from: [[Artists/D/David Bowie]])
- [x] Ben Weinman (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Dimitri Minakakis (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Adam Doll (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Chris Pennie (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Brian Benoit (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Greg Puciato (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Gil Sharone (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] James Love (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Billy Rymer (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Kevin Antreassian (batch: 2026-07-02T09:00, from: [[Artists/T/The Dillinger Escape Plan]])
- [x] Craig Fox (batch: 2026-07-02T09:00, from: [[Artists/T/The Greenhornes]])
- [x] Mark Watrous (batch: 2026-07-02T09:00, from: [[Artists/T/The Greenhornes]])
- [x] Jamie Hince (batch: 2026-07-02T09:00, from: [[Artists/T/The Kills]])
- [x] Christian Gabel (batch: 2026-07-02T09:00, from: [[Artists/T/Thåström]])
- [x] Tore Ylwizaker (batch: 2026-07-02T09:00, from: [[Artists/U/Ulver]])
- [x] Jørn H. Sværen (batch: 2026-07-02T09:00, from: [[Artists/U/Ulver]])
- [x] Daniel O'Sullivan (batch: 2026-07-02T09:00, from: [[Artists/U/Ulver]])
- [x] Louiche Mayorga (batch: 2026-07-02T09:00, from: [[Artists/A/Against]])
- [x] Grant Estes (batch: 2026-07-02T09:00, from: [[Artists/A/Against]])
- [x] Amery Smith (batch: 2026-07-02T09:00, from: [[Artists/A/Against]])
- [x] Kevin Guercio (batch: 2026-07-02T09:00, from: [[Artists/A/Against]])
- [x] Gary Cherone (batch: 2026-07-02T09:00, from: [[Artists/E/Extreme]])
- [x] Pat Badger (batch: 2026-07-02T09:00, from: [[Artists/E/Extreme]])
- [x] Paul Geary (batch: 2026-07-02T09:00, from: [[Artists/E/Extreme]])
- [x] Mike Mangini (batch: 2026-07-02T09:00, from: [[Artists/E/Extreme]])
- [x] Kate Bush (batch: 2026-07-02T09:00, from: [[Artists/K/Kate Bush]])
- [x] Adam Gontier (batch: 2026-07-02T09:00, from: [[Artists/S/Saint Asonia]])
- [x] Cale Gontier (batch: 2026-07-02T09:00, from: [[Artists/S/Saint Asonia]])
- [x] Cody Watkins (batch: 2026-07-02T09:00, from: [[Artists/S/Saint Asonia]])
- [x] Rich Beddoe (batch: 2026-07-02T09:00, from: [[Artists/S/Saint Asonia]])
- [x] Corey Lowery (batch: 2026-07-02T09:00, from: [[Artists/S/Saint Asonia]])
- [x] Joakim Thåström (batch: 2026-07-02T13:00, from: [[Artists/E/Ebba Grön]])
- [x] Gunnar Ljungstedt (batch: 2026-07-02T13:00, from: [[Artists/E/Ebba Grön]])
- [x] Lennart Eriksson (batch: 2026-07-02T13:00, from: [[Artists/E/Ebba Grön]])
- [x] Anders Sjöholm (batch: 2026-07-02T13:00, from: [[Artists/E/Ebba Grön]])
- [x] Christian Falk (batch: 2026-07-02T13:00, from: [[Artists/I/Imperiet]])
- [x] Per Hägglund (batch: 2026-07-02T13:00, from: [[Artists/I/Imperiet]])
- [x] Fred Asp (batch: 2026-07-02T13:00, from: [[Artists/I/Imperiet]])
- [x] Scott Anderson (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] James Black (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] Rick Jackett (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] Sean Anderson (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] Steve Molella (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] Rob Gommerman (batch: 2026-07-02T13:00, from: [[Artists/F/Finger Eleven]])
- [x] Peter Gabriel (batch: 2026-07-02T13:00, from: [[Artists/P/Peter Gabriel]])
- [x] Shaun Morgan (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Dale Stewart (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] John Humphrey (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Johan Greyling (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Dave Cohoe (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Nick Oshiro (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Pat Callahan (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Troy McLawhorn (batch: 2026-07-02T13:00, from: [[Artists/S/Seether]])
- [x] Neil Sanderson (batch: 2026-07-02T13:00, from: [[Artists/T/Three Days Grace]])
- [x] Brad Walst (batch: 2026-07-02T13:00, from: [[Artists/T/Three Days Grace]])
- [x] Barry Stock (batch: 2026-07-02T13:00, from: [[Artists/T/Three Days Grace]])
- [x] Matt Walst (batch: 2026-07-02T13:00, from: [[Artists/T/Three Days Grace]])
- [x] Nicolas Godin (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Jean-Benoît Dunckel (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Brian Reitzell (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Roger Manning Jr. (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Brian Kehew (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Jason Falkner (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] James Rotondi (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Dave Palmer (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Earl Harvin (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Vincent Taurelle (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Steve Jones (drummer) (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Alex Thomas (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Tom DeLonge (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] David Kennedy (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Ilan Rubin (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Matt Rubano (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Atom Willard (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Ryan Sinn (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Matt Wachter (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Eddie Breckenridge (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Aaron Rubin (batch: 2026-07-02T16:00, from: [[Artists/A/Angels & Airwaves]])
- [x] Jared Leto (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Shannon Leto (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Solon Bixler (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Kevin Drake (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Tim Kelleher (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Braxton Olita (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Tomo Miličević (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] 50 Cent (batch: 2026-07-02T17:13, from: [[Artists/0-9/50 Cent]])
- [x] Tupac Shakur (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Lloyd Banks (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Tony Yayo (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Young Buck (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] The Game (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Kidd Kidd (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Uncle Murda (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Damien Moyal (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Timothy Kirkpatrick (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Joseph Simmons (guitarist) (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] James Glayat (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Henry Olmino (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Jeronimo Gomez (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Matthew Crum (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Stephen Looker (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Gordon Tarpley (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Jason Dooley (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Jason Black (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Kaleb Stewart (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Peter Bartsocas (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Christopher Beckham (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Guillermo Amador (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Alexander Vernon (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Zachary Swain (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Thomas Rankine (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Adam D'Zurilla (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Joshua Williams (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Chad Darby (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Michael Lipscomb (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Richard Thurston (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Ryan Mahon (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Scott Borland (batch: 2026-07-02T22:51, from: [[Artists/B/Big Dumb Face]])
- [x] Kyle Weeks (batch: 2026-07-02T22:51, from: [[Artists/B/Big Dumb Face]])
- [x] Greg Isabelle (batch: 2026-07-02T22:51, from: [[Artists/B/Big Dumb Face]])
- [x] Chris Gibbs (batch: 2026-07-02T22:51, from: [[Artists/B/Big Dumb Face]])
- [x] Josh Eustis (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Nick Annis (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Marshall Kilpatric (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Sean Fetterman (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Dennis Sanders (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Dylan Taylor (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] John Bates (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Mark Hoppus (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Travis Barker (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Scott Raynor (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Mike Krull (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Brooks Wackerman (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Shane Gallagher (batch: 2026-07-02T23:42, from: [[Artists/0-9/+44]])
- [x] Craig Fairbaugh (batch: 2026-07-02T23:42, from: [[Artists/0-9/+44]])
- [x] Carol Heller (batch: 2026-07-02T23:42, from: [[Artists/0-9/+44]])
- [x] Anthony Celestino (batch: 2026-07-02T23:56, from: [[Artists/B/Box Car Racer]])
- [x] George Rios (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Andrew Logan (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] José Martinez (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Shane Post (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] José Flores (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Nahuel Gauna (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Denny Carmassi (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Ricky Phillips (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Jorge Casas (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Lester Mendez (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Guy Pratt (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Brett Tuggle (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] John Harris (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] John Sambataro (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Tommy Funderburk (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] David Pajo (batch: 2026-07-03T04:12, from: [[Artists/D/David Pajo]])
- [x] John Wylie (batch: 2026-07-03T04:30, from: [[Artists/C/Culture (American band)]])
- [x] Mark Mitchell (batch: 2026-07-03T04:30, from: [[Artists/C/Culture (American band)]])
- [x] Louie Long (batch: 2026-07-03T04:30, from: [[Artists/C/Culture (American band)]])
- [x] Milo Aukerman (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Karl Alvarez (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Stephen Egerton (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Frank Navetta (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Tony Lombardo (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Ray Cooper (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Doug Carrion (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] David Nolte (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Cecilia Loera (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Dave Smalley (batch: 2026-07-03T05:30, from: [[Artists/A/All]])
- [x] Scott Reynolds (batch: 2026-07-03T05:30, from: [[Artists/A/All]])
- [x] Chad Price (batch: 2026-07-03T05:30, from: [[Artists/A/All]])
- [x] Greg Ginn (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Keith Morris (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Chuck Dukowski (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Raymond Pettibon (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Bryan Migdol (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Jim Dearmen (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Spot [member] (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Robo (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Ron Reyes (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Emil Johnson (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Chuck Biscuits (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Kira Roessler (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Anthony Martinez (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] C'el Revuelta (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Mike Vallely (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Gregory Moore (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Dave Klein (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Tyler Smith (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Brandon Pertzborn (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Isaias Gil (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Joseph Noval (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Harley Duggan (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Austin Sears (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Matt Baxter (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Charles Wiley (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Max Zanelly (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] David Rodriguez (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Bryce Weston (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Jeff Dean (batch: 2026-07-03T09:30, from: [[Artists/E/Explode and Make Up]])
- [x] Pete Mittler (batch: 2026-07-03T09:30, from: [[Artists/E/Explode and Make Up]])
- [x] Mike Pinaud (batch: 2026-07-03T09:30, from: [[Artists/E/Explode and Make Up]])
- [x] Tim Den (batch: 2026-07-03T09:30, from: [[Artists/E/Explode and Make Up]])
- [x] Trever Keith (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Scott Shiflett (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Danny Thompson (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Dennis Hill (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Matt Riddle (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Rob Kurth (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Chad Yaro (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Jose Medeles (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Chris Cresswell (batch: 2026-07-03T20:45, from: [[Artists/H/Hot Water Music]])
- [x] Chris Wollard (batch: 2026-07-03T20:45, from: [[Artists/H/Hot Water Music]])
- [x] Chuck Ragan (batch: 2026-07-03T20:45, from: [[Artists/H/Hot Water Music]])
- [x] George Rebelo (batch: 2026-07-03T20:45, from: [[Artists/H/Hot Water Music]])
- [x] Jason Black (batch: 2026-07-03T20:45, from: [[Artists/H/Hot Water Music]])
- [x] Christian Dudek (batch: 2026-07-02T15:00, from: [[Artists/S/Sodom]])
- [x] Christian Lorenz (batch: 2026-07-02T15:00, from: [[Artists/F/Feeling B]])
- [x] Christian Lund (batch: 2026-07-02T15:00, from: [[Artists/D/Death Hawks]])
- [x] Christoph Schneider (batch: 2026-07-02T15:00, from: [[Artists/R/Rammstein]])
- [x] Christopher Franke (batch: 2026-07-02T15:00, from: [[Artists/T/Tangerine Dream]])
- [x] Christopher Guest (batch: 2026-07-02T15:00, from: [[Artists/S/Spinal Tap]])
- [x] Christopher Hall (batch: 2026-07-02T15:00, from: [[Artists/S/Stabbing Westward]])
- [x] Christopher Juul (batch: 2026-07-02T15:00, from: [[Artists/H/Heilung]])
- [x] Chuck D (batch: 2026-07-02T15:00, from: [[Artists/P/Public Enemy]])
- [x] Chuck Dukowski (batch: 2026-07-02T15:00, from: [[Artists/B/Black Flag]])
- [x] Chuck Mosley (batch: 2026-07-02T15:00, from: [[Artists/F/Faith No More]])
- [x] Claude Coleman Jr. (batch: 2026-07-02T15:00, from: [[Artists/W/Ween]])
- [x] Claude Schnell (batch: 2026-07-02T15:00, from: [[Artists/D/Dio]])
- [x] Cliff Evans (batch: 2026-07-02T15:00, from: [[Artists/C/Crystal Fairy]])
- [x] Cliff Williams (batch: 2026-07-02T15:00, from: [[Artists/A/ACDC]])
- [x] Corpo-Mente (batch: 2026-07-02T15:00, from: [[Artists/C/Corpo-Mente]])
- [x] Cosey Fanni Tutti (batch: 2026-07-02T15:00, from: [[Artists/T/Throbbing Gristle]])
- [x] Cozy Powell (batch: 2026-07-02T15:00, from: [[Artists/R/Rainbow]])
- [x] Craig Jones (batch: 2026-07-02T15:00, from: [[Artists/S/Slipknot]])
- [x] Cronos (batch: 2026-07-02T15:00, from: [[Artists/V/Venom]])
- [x] Everlast (batch: 2026-07-03T21:00, from: [[Artists/H/House of Pain]])
- [x] Danny Boy (batch: 2026-07-03T21:00, from: [[Artists/H/House of Pain]])
- [x] DJ Lethal (batch: 2026-07-03T21:00, from: [[Artists/H/House of Pain]])
- [x] Mitch Harris (batch: 2026-07-03T14:32, from: [[Artists/N/Napalm Death]]) – QC ✓
- [x] Anthony Gonzalez (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Nicolas Fromageau (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Morgan Kibby (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Loïc Maurin (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Kaela Sinclair (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Joe Berry (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Jordan Lawlor (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Ian Young (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Pierre-Marie Maulini (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Zola Jesus (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Brad Laner (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Susanne Sundfør (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Mai Lan (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Kenny Becker (batch: 2026-07-03T18:36, from: [[Artists/G/Goon]])
- [x] Andy Polito (batch: 2026-07-03T18:36, from: [[Artists/G/Goon]])
- [x] Dillon Peralta (batch: 2026-07-03T18:36, from: [[Artists/G/Goon]])
- [x] Tamara Simons (batch: 2026-07-03T18:36, from: [[Artists/G/Goon]])
- [x] Matt Bellamy (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Dominic Howard (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Chris Wolstenholme (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Steve Felton (batch: 2026-07-03T23:45, from: [[Artists/M/Mushroomhead]])
- [x] Jeffrey Hetrick (batch: 2026-07-03T23:45, from: [[Artists/M/Mushroomhead]])
- [x] Ryan Farrell (batch: 2026-07-03T23:45, from: [[Artists/M/Mushroomhead]])
- [x] Mark Greenway (batch: 2026-07-03T14:32, from: [[Artists/N/Napalm Death]])
- [x] Shane Embury (batch: 2026-07-03T14:32, from: [[Artists/N/Napalm Death]])
- [x] Mitch Harris (batch: 2026-07-03T14:32, from: [[Artists/N/Napalm Death]])
- [ ] Danny Herrera (batch: 2026-07-03T14:32, from: [[Artists/N/Napalm Death]])
- [ ] Chad Channing (batch: 2026-07-03T14:45, from: [[Artists/N/Nirvana]])
- [ ] Randy Rhoads (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Jimmy Marchiano (batch: 2026-07-04T23:45, from: [[Artists/A/Angora]])
- [ ] Frank Scimeca (batch: 2026-07-04T23:45, from: [[Artists/A/Angora]])
- [ ] Robert Iezzi (batch: 2026-07-04T23:45, from: [[Artists/A/Angora]])

## Producers

> last updated: 2026-07-04T11:45 · unfixed: 19

- [x] George Clinton (batch: 2026-07-02T05:00, from: [[Artists/P/Parliament-Funkadelic]])
- [x] Terry Date (batch: 2026-07-02T05:00, from: [[Artists/S/Staind]])
- [x] Paul Curcio (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Flemming Rasmussen (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Bob Rock (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Rick Rubin (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Greg Fidelman (batch: 2026-07-01T21:00, from: [[Artists/M/Metallica]])
- [x] Roberto Laghi (batch: 2026-07-01T15:00, from: [[Artists/A/All Ends]])
- [x] Boys Noize (batch: 2026-07-01T16:00, from: [[Artists/N/Nine Inch Noize]])
- [x] Tony Visconti (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Ken Scott (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Nile Rodgers (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Gus Dudgeon (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Harry Maslin (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Brian Eno (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [x] Reeves Gabrels (batch: 2026-07-01T17:00, from: [[Artists/D/David Bowie]])
- [ ] Jacob Hellner (batch: 2026-07-04T21:15, from: [[Artists/R/Rammstein]])
- [ ] Olsen Involtini (batch: 2026-07-04T21:15, from: [[Artists/R/Rammstein]])
- [x] Guy Stevens (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] David Bowie [producer] (batch: 2026-07-01T20:00, from: [[Artists/M/Mott the Hoople]])
- [x] Nicolas Godin (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Jean-Benoît Dunckel (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Nigel Godrich (batch: 2026-07-02T15:15, from: [[Artists/A/Air]])
- [x] Bob Ezrin (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Brian Virtue (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Josh Abraham (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Steve Lillywhite (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Jared Leto [producer] (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Shannon Leto [producer] (batch: 2026-07-02T16:15, from: [[Artists/0-9/30 Seconds to Mars]])
- [x] Rob McGregor (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] J. Robbins (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Butch Vig (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Marc Hudson (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Laura Jane Grace [producer] (batch: 2026-07-02T17:00, from: [[Artists/A/Against Me!]])
- [x] Matt Allison (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Joe McGrath (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Jerry Finn (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Bill Stevenson [producer] (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Jason Livermore (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Cameron Webb (batch: 2026-07-02T18:00, from: [[Artists/A/Alkaline Trio]])
- [x] Dan Wleklinski [producer] (batch: 2026-07-02T20:00, from: [[Artists/0-9/88 Fingers Louie]])
- [x] Dr. Dre [producer] (batch: 2026-07-02T17:13, from: [[Artists/0-9/50 Cent]])
- [x] Eminem [producer] (batch: 2026-07-02T17:13, from: [[Artists/0-9/50 Cent]])
- [x] Shock G (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Big D the Impossible (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Stretch (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Easy Mo Bee (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Tony Pizarro (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Johnny J (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Daz Dillinger (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] DJ Quik (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] QDIII (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Hurt-M-Badd (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Swizz Beatz (batch: 2026-07-02T17:43, from: [[Artists/T/Tupac Shakur]])
- [x] Hi-Tek (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Scott Storch (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Ron Browz (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Red Spyda (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Tha Bizness (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Rick Rock (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Polow da Don (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] Don Cannon (batch: 2026-07-02T21:00, from: [[Artists/G/G-Unit]])
- [x] James Paul Wisner (batch: 2026-07-02T22:43, from: [[Artists/A/As Friends Rust]])
- [x] Wes Borland [producer] (batch: 2026-07-02T22:51, from: [[Artists/B/Big Dumb Face]])
- [x] Danny Lohner [producer] (batch: 2026-07-02T23:12, from: [[Artists/B/Black Light Burns]])
- [x] Mark Trombino (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] John Feldmann (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Otis Barthoulameu (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Travis Barker [producer] (batch: 2026-07-02T23:22, from: [[Artists/B/Blink-182]])
- [x] Mark Hoppus [producer] (batch: 2026-07-02T23:42, from: [[Artists/0-9/+44]])
- [x] Jeremy Staska (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Marek Stycos (batch: 2026-07-03T03:43, from: [[Artists/B/Bird of Ill Omen]])
- [x] Mike Fraser (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] David Coverdale [producer] (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] Jimmy Page [producer] (batch: 2026-07-03T03:53, from: [[Artists/C/Coverdale-Page]])
- [x] David Pajo [producer] (batch: 2026-07-03T04:12, from: [[Artists/D/David Pajo]])
- [x] Spot (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] David Tarling (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] Stephen Egerton [producer] (batch: 2026-07-03T04:45, from: [[Artists/D/Descendents]])
- [x] John Hampton (batch: 2026-07-03T05:30, from: [[Artists/A/All]])
- [x] Donnell Cameron (batch: 2026-07-03T08:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Mudrock (batch: 2026-07-03T08:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Mike Elizondo (batch: 2026-07-03T08:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Joe Barresi (batch: 2026-07-03T08:00, from: [[Artists/A/Avenged Sevenfold]])
- [x] Greg Ginn [producer] (batch: 2026-07-03T09:15, from: [[Artists/B/Black Flag]])
- [x] Tom Petta (batch: 2026-07-03T09:30, from: [[Artists/E/Explode and Make Up]])
- [x] Jim Goodwin (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Chad Blinman (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] Thom Wilson (batch: 2026-07-03T13:00, from: [[Artists/F/Face to Face]])
- [x] John Silver (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Mick Barnard (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Ronnie Caryl (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Tim Renwick (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Gary Wallis (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Roger Taylor (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Nir Zidkyahu (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Howard Benson (batch: 2026-07-03T19:45, from: [[Artists/H/Hazen Street]])
- [x] Anthony Drennan (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Ben Lovett (batch: 2026-07-03T20:30, from: [[Artists/H/Heavens]])
- [x] DJ Muggs (batch: 2026-07-03T21:00, from: [[Artists/H/House of Pain]])
- [x] Daniel Pearce (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Patrick Smyth (batch: 2026-07-03T14:00, from: [[Artists/G/Genesis]])
- [x] Andy Sturmer (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Roger Manning (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Jason Falkner (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Chris Manning (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Tim Smith (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Eric Dover (batch: 2026-07-03T22:50, from: [[Artists/J/Jellyfish]])
- [x] Tony Bevilacqua (batch: 2026-07-03T23:20, from: [[Artists/J/Jubilee]])
- [x] Jenni Tarma (batch: 2026-07-03T23:20, from: [[Artists/J/Jubilee]])
- [x] Troy Petrey (batch: 2026-07-03T23:20, from: [[Artists/J/Jubilee]])
- [x] Michael Shuman (batch: 2026-07-03T23:20, from: [[Artists/J/Jubilee]])
- [x] Ian Watkins (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Lee Gaze (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Mike Lewis (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Stu Richardson (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Jamie Oliver (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Mike Chiplin (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] DJ Stepzak (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Luke Johnson (batch: 2026-07-03T23:55, from: [[Artists/L/Lostprophets]])
- [x] Anthony Gonzalez (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Nicolas Fromageau (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Ken Thomas (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Ewan Pearson (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Morgan Kibby (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Antoine Gaillet (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Justin Meldal-Johnsen (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Joseph Trapanese (batch: 2026-07-03T18:57, from: [[Artists/M/M83]])
- [x] Irv Gotti (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Chris Gotti (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Ja Rule (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Ashanti (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Charli Baltimore (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Lloyd (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Vanessa Carlton (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Vita (batch: 2026-07-03T21:15, from: [[Artists/M/Murder Inc.]])
- [x] Rich Costey (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] John Leckie (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Paul Reeve (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] David Bottrill (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] John Cornfield (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Adrian Bushby (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Tommaso Colliva (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Mutt Lange (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Shellback (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Timbaland (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Gaius Chow (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Fred Ball (batch: 2026-07-03T21:30, from: [[Artists/M/Muse]])
- [x] Jason Popson (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Waylon Reavis (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Tom Schmitz (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Rick Thomas (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Steve Rauckhorst (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Scott Beck (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] John Sekula (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Richie Moore (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Joe Kilcoyne (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Joe Lenkey (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Jack Kilcoyne (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Marko Vukcevich (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Daniel Fox (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Robert Godsey (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Tommy Church (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Tom Shaffner (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Joe Gaal (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Aydin Kerr (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [ ] Simon Kanaris (batch: 2026-07-03T23:55, from: [[Artists/M/Mushroomhead]])
- [x] Tommy Lee (batch: 2026-07-03T13:15, from: [[Artists/M/Mötley Crüe]])
- [ ] Mick Mars (batch: 2026-07-03T13:15, from: [[Artists/M/Mötley Crüe]])
- [ ] Vince Neil (batch: 2026-07-03T13:15, from: [[Artists/M/Mötley Crüe]])
- [x] John Corabi (batch: 2026-07-03T13:15, from: [[Artists/M/Mötley Crüe]])
- [ ] Max Norman (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Bob Daisley (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Ron Nevison (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Roy Thomas Baker (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Keith Olsen (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Duane Baron (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] John Purdell (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Michael Beinhorn (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Tim Palmer (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Kevin Churko (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Andrew Watt (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Louis Bell (batch: 2026-07-04T00:00, from: [[Artists/O/Ozzy Osbourne]])
- [ ] Peter Tägtgren (batch: 2026-07-04T14:32, from: [[Artists/P/Pain]])
- [ ] Gary Smith (batch: 2026-07-04T19:15, from: [[Artists/P/Pixies]])
- [ ] Gil Norton (batch: 2026-07-04T19:15, from: [[Artists/P/Pixies]])
- [ ] Tom Dalgety (batch: 2026-07-04T19:15, from: [[Artists/P/Pixies]])
- [ ] Chris Cornell (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Matt Cameron (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Ben Shepherd (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Jason Everman (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Kim Thayil (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Hiro Yamamoto (batch: 2026-07-04T22:00, from: [[Artists/S/Soundgarden]])
- [ ] Logan Mader (batch: 2026-07-04T11:45, from: [[Artists/B/Brave the Cold]])
