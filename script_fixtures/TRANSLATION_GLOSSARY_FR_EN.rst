#############################################
Translation Glossary - French to English
#############################################

.. This file is the single source of truth for translating the Chrysalis script
   fixtures (``*.rst`` Jinja2 templates) from French into English. Every English
   twin file (``*_en.rst``) must use the terms listed here. Add a row whenever a
   new recurring piece of jargon is translated, so that later translations stay
   consistent.

Conventions
===========

**Precedence**: a table row beats these general rules; the generated
"Jinja symbol display values" table at the end beats everything (see
**Symbol values** below). When a row lists several FR variants separated by
"/", the EN variants map to them in order.

**Spelling**: British English throughout (artefact, armour, colour, defence,
centre, mould, sulphur, grey, spectre, organiser, haemorrhage, ageing,
jewellery, tranquiliser, -ise/-isation verb endings, also in comments:
"CUSTOMISE"). "encyclopedia" and "program" (software) are acceptable British
forms. Exception: keep US spellings that already exist in file names or data
keys (e.g. ``duel_of_honor_rules.rst`` stays as a path, but the prose says
"duel of honour"; the macro ``wireline_fax`` stays although the prose says
"landline").

**Proper nouns**: invented names (Loyd Georges, Maupertuis, Rydji, Nazur,
Olloudios...) stay verbatim, including accents (Mérédice, Joséphine, Séléné).
Transparent French nicknames and titles are translated (la Bête = the Beast,
le Voleur = the Thief, Barbe Blonde = Blondbeard). Historical figures take their
standard English form (Vercingetorix, Julius Caesar, Zarathustra).

**Demonyms and adjectives** follow the code and file names, not the French
source: Akarith (never Akarite), Sabarith (never Sabarite), Lordanian,
Masslavian, Dorian, Yodic, Oberon, Heliossarian, Keroskian, Midolian,
Nalavutian, Salimian, Pangean.

**Role names** follow the file names: Dispeller, Exorcist, Invoker (Diakons);
Anthropologist, Runologist, Unveiler (Explorers); Alchemist, Oracle, Woodsman
(Parcival); Lockpicker, Minesweeper, Sounder (Spies); Dragons.

**Meta vocabulary**: "Game Master" / "GM" (maître de jeu, meneur de jeu, MJ);
"NPC" for a non-player character and "NPC actor" when the human performer is
meant (figurant); "player" (joueur/joueuse); "LARP" (GN); "murder party" for the
genre and "mystery game" / "mystery evening" for the subtitle wording;
"in-game" / "out-of-game" in prose, "IC" / "OOC" as abbreviations (RP / HRP).

**Puzzles**: "puzzle" for mechanical or visual enigmas, "riddle" for verbal ones.

**Capitalisation policy**:

- Capitalised: proper names of unique artefacts, places, institutions, events
  and named abilities/rituals (Divine Orb(s), Divine Tear(s), Sun of Atoms,
  Forbidden Domain, Otherworld Banquet / Otherworld Buffet, Yodic Book of the
  Dead, Thanatologue, Order of Tabellions, Bank of Salima, Weapon Blessing,
  Lightning Investigation); named orders, sects and factions (the Judicators,
  the Purifiers, the Red Wolves, the Diakons); role names (Dispeller,
  Lockpicker...); and character titles that stand in for a name when they
  designate that character (the Tabellion, the Beast, the Druid, the Arkon,
  the Archivist, the Curator, the Guide, the Reporter, the Hero, the Ancestral
  Tortoise, the Akarith Ambassador / the Ambassador); nicknames keep a capitalised article ("The Docker"); invented or
  title-like names of items and abilities stay capitalised in running text (the Leather Purse, the World
  Scanner, the Tectonic Canister, the Akarith Lexicon, "Elements/Gems of Sabarith Law"), whereas common nouns
  stay lowercase in prose (metal detector, magnetic unlocker, UV lamp, Herculean strength) and take a capital only
  as role-sheet ability headings. Bare "orb(s)" is lowercase in EN running text and headings, including "Loyd
  Georges' orb"; the capital is kept only inside names (Divine Orb(s), the Three Divine Orbs, Spiritual Orb,
  Alpha/Beta/Gamma Orb).
- Ranks and offices take a capital before a personal name (Archdeacon Menelas,
  Judicator Praeves, Captain Rodimir, Prof. Voluto) and are lowercase when
  generic or descriptive (the patriarch of Ghek, a consul, tabellions as a
  profession, an archdeacon); a fixed office title keeps its capital ("Consul
  of Alifir"). Generic functions stay lowercase even where the FR capitalises
  them ("an escrow agent" for "un Tiers de Confiance").
- Descriptive epithets and one-off bodies stay lowercase even where a FR line
  capitalises them: sacred orb (orbe sacré / saint orbe), the Akarith council /
  the great council, the misty mountains, cromlech (the stone circle or model;
  "the Cromlech" is the library-museum), the Magus's tomb, the museum's treasure
  in prose (only the rotation station is "the Treasure").
- Headings keep the case style of the matching row (Cromlech, Descent and
  Sentience headings are mostly Title Case, Archives and Mindstorm headings
  sentence case); ALL-CAPS FR headings stay all caps. Descent location names
  (Aquifer Cavern, Yodic Temple Cavern, Pagan Temple, Main Hall of the
  Pre-Yodic Temple...) are Title Case in headings and on the map but lowercase
  in running text ("the aquifer cavern"). "The Holy of Holies" (the sanctum of
  the Temple of Nazur, in Descent and in the Mindstorm Nazur mission) keeps its
  capitals everywhere; a figurative use stays lowercase ("this holy of holies"
  in the Archives GM manual).
- Pronouns: characters (roles, NPCs, the player as their character) follow the
  French source, gendered "he" / "she" as the FR writes them, with no
  neutralisation. Generic meta referents (the GM, "a player", "a participant")
  take singular "they" ("check with the GM when they come round"; "if a player
  dies, they become a phantom"). Non-human creatures whose FR "il" / "elle" is
  only grammatical (the Beast, the ghoul, the mummy, automatons, the monitor
  lizard) take "it"; a sapient or named creature that the FR treats as a person
  keeps the FR gender (the Ancestral Tortoise = "she").
- Coined lore terms that the FR writes as common nouns (bathar, polymony,
  transfiliation) follow the FR case: lowercase in running text, capitalised
  only where the FR capitalises them.

**Recurring renderings and false friends** (each has a row below; see also the
translator checklist for actuellement, éventuellement, important, assister,
déception, librairie...):

- religious "confession" = "denomination" (Mithraite denomination, Razulite
  denomination), never "confession" (except the Arkon's "mission confession",
  which is an act);
- "culte" (of a faith) = "worship" (the act) or "faith" (the religious body:
  "the Yodic faith", "a rival faith"), never "cult"; the one exception is the
  Descent zealots' graffiti, whose contempt "every cult devoted to the vile
  idols" deliberately keeps;
- "fantôme" = "phantom" (the Archives phantom NPCs: "the phantoms switch"); only
  Cromlech may say "ghost" for its druid's spectre; "fantomatique" =
  "phantom-like", never "ghostly";
- "portail de transplanage / téléportation" = "teleportation portal", never
  "apparition portal";
- "le sir / le sieur" = "the gentleman", never "the sir" ("ce triste sir" =
  "this sorry gentleman");
- "pastille" (sticker star) = "sticker";
- "téléphone filaire" = "landline";
- "disparition inquiétante" = "suspicious disappearance";
- "Etat des lieux" = "State of play";
- "livre d'or" = "guest book";
- "glaive" = "gladius"; "donjon" = "keep";
- "diacre" = "Diakon"; "confrère" between believers = "brother in the faith" or
  "fellow Diakon", never "fellow brother";
- "hors-jeu / hors-roleplay" = "out-of-game";
- "s'incarner" = "to become embodied";
- "défiance" = "distrust";
- "sensible à" (a danger, attacks) = "vulnerable to", never "sensitive to"
  (which stays for physical or perceptual sensitivity); "insensible à" =
  "immune to";
- "costume" (everyday men's clothing) = "suit"; "costume" stays only for
  theatrical or character costumes;
- "pays de X" = "the land of X" (the land of Akaris, the land of Balberith);
- "Anticiper" (GM schedule cue) = "Prepare for".

**Clock times and durations**: clock times use the 24-hour clock with a colon,
H:MM before 10:00 and HH:MM from 10:00 (no leading zero; this is what "HH:MM" in
the generated symbol table means), in prose and in symbol values alike (7:00,
9:00 and 10:00, 14:45, 20:00; ranges "8:00-10:00"); never "8 pm", "8am", "08:00"
or "20h". Two idiomatic exceptions only: a striking clock ("12h sonne à
l'horloge" = "The clock strikes twelve", or "12"), and a time the FR source
itself spells out in words ("10:00 in the morning" for
``heure_ouverture_du_cromlech_le_jour_j``). Durations are written
"3 hours", "a good hour", "15 min" (abbreviated "min", never "mn"); schedule
notation "H-45 min", "H+1:20"; "3h30" as a duration in tables = "3½ h".

**Typography**: French guillemets « » become straight double quotes "..."; no
space before : ; ? ! ; "n°" becomes "no."; "5mn" becomes "5 min"; "1er" becomes
"1st"; decimal commas become decimal points; thousands use a comma (2,000
kashes).

**Templating rules** (see also the translator checklist): Jinja tags, variable
names, filters, macros, lazy includes ``<{ name }/>`` and string literals that
are compared with data keys (``{% fact %}``, ``{% hint %}``, ``{% item %}``,
``{% xfact %}``, ``{% xitem %}``, ``{% if x == "..." %}``) stay untouched.
``{% include "x.rst" %}`` becomes ``{% include "x_en.rst" %}``. RST heading
underlines are re-sized to the translated title (titles containing a
``{% symbol %}`` tag are measured on the rendered text). Indentation, BOM and
line endings are preserved exactly.

**Symbol values**: ``{% symbol "value" for "key" %}`` prints "value" as prose,
and the sheet generator aborts if one key receives two different values
(compared after strip().lower()) across ALL rendered templates. The English
value of every key is therefore fixed by the generated table at the end of this
file: never edit a symbol value by hand; rewrite the sentence around the tag
instead. A value change goes through the ``CANON`` dict of
``normalize_symbols.py``, which rewrites every ``*_en.rst`` file at once.

Shared Pangea universe terms
=============================

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - costume (vêtement d'homme)
     - suit
     - False friend in everyday clothing: "des costumes et robes sobres" = "sober suits and dresses" (_common_game_rules). Keep "costume" for theatrical or character costumes ("pour les costumes" in the GM manuals, the Avatars' novel costumes, the "Druid's Spectre costume").
   * - sensible à (un danger, des attaques)
     - vulnerable to
     - False friend: exposed to harm = "vulnerable to" ("les vivants sont sensibles aux attaques" = "the living are vulnerable to attacks"; dragons_role). Keep "sensitive to" for physical or perceptual sensitivity (strong smells, magnetism, disturbances in the strata of existence) and "receptive to" for arguments; "insensible à" = "immune to" (attacks, weapons, spells) or "insensitive to" (pain).
   * - Académie d'Alifir
     - Alifir Academy
     - Scientific institution; never "Alifir's Academy".
   * - Akaris / Akarie / pays d'Akaris
     - Akaris / the land of Akaris
     - Theocratic country; FR variant "Akarie" also maps to "Akaris".
   * - akarite(s) / Akarites
     - Akarith / the Akariths
     - Adjective and demonym; capitalised.
   * - artefact
     - artefact
     - British spelling, never "artifact".
   * - Chrysalis (projet / univers)
     - Chrysalis (project / universe)
     - Project name; "Projet Chrysalis" = "Chrysalis Project".
   * - crossentar
     - crossentar
     - Yodic religious insignia; lowercase common noun, capitalised only in item titles.
   * - disparition inquiétante / signalement pour disparition inquiétante
     - suspicious disappearance / missing person report
     - Police term (Mindstorm radio spot and GM manual, Cromlech Reporter); never "worrying disappearance".
   * - Élixir Berserk
     - Berserk Elixir
     - Combat drug appearing in several games.
   * - Ère Tectonne / ère tectonne / prétectonne
     - Tectonic Era / pre-Tectonic
     - Pangean era name, capitalised in EN; FR spelling "tectonne" (the sources also write tectone / Tectone / ante-tectonne).
   * - figurant(e)
     - NPC actor
     - The human performer of a non-player character; "NPC" for the character itself.
   * - GN / jeu de rôle grandeur nature
     - LARP / live-action role-playing game
     - Meta.
   * - Héliossar / héliossar(e)
     - Heliossar / Heliossarian
     - Country / adjective.
   * - hors-jeu / HRP ; en jeu / RP
     - out-of-game / OOC ; in-game / IC
     - Meta. "hors-roleplay" (Archives and Mindstorm rules) is also "out-of-game" (row "hors-roleplay"); "OOC" / "IC" only as abbreviations.
   * - hors-roleplay
     - out-of-game
     - Meta (Archives and Mindstorm game rules, GM planning): same as "hors-jeu"; never "out-of-roleplay". One exception: the Vocabulary list of _common_game_rules glosses the abbreviation itself, '"HRP" (ou hors-roleplay) signifie "hors-jeu"' = '"OOC" (or out-of-character) means "out-of-game"', to avoid a circular definition.
   * - indice
     - clue
     - Meta.
   * - JDR / jeu de rôle
     - RPG / role-playing game
     - Meta.
   * - joueur / joueuse
     - player
     - Meta.
   * - kash / kashes / kilokash / mégakash
     - kash / kashes / kilokash / megakash
     - Pangea currency; lowercase; plurals "kashes", "kilokashes", "megakashes"; abbreviations "Mk" (megakash) and "¤" (kash) kept. Its value is game-dependent and follows each FR source: "1 kash buys 10 baguettes of bread" (Mindstorm context intro) but "about 100 loaves of bread" (Archives GM manual), an inconsistency in the FR sources, flagged to the author.
   * - Kéroskia / kéroskien
     - Keroskia / Keroskian
     - Continent / adjective; no accent in EN. Slavinka, Tieros Olim = countries in it.
   * - Larme(s) Divine(s)
     - Divine Tear(s)
     - Lore name of the Divine Orbs.
   * - Lordanie / lordanien
     - Lordania / Lordanian
     - Country / adjective.
   * - maître de jeu / maître du jeu / meneur de jeu / MJ
     - Game Master / GM
     - Meta; plural "GMs".
   * - Masslavie / masslave
     - Masslavia / Masslavian
     - Country / adjective.
   * - Midolie / midolien
     - Midolia / Midolian
     - Country / adjective.
   * - murder party / soirée-mystère / soirée mystère
     - murder party / mystery evening
     - Genre; the project is named "mystery party".
   * - Nazur / temple de Nazur
     - Nazur / the Temple of Nazur
     - Lost heretic city; verbatim.
   * - Orbe / Orbe Divin / Trois Orbes Divins
     - orb / Divine Orb / the Three Divine Orbs
     - Core lore; "it" in EN. Bare "orb(s)" lowercase ("the orbs", "Loyd Georges' orb"), capital only in Divine Orb(s), Spiritual Orb, Alpha/Beta/Gamma Orb.
   * - Pangéa / Pangée / pangéen(ne)
     - Pangea / Pangean
     - The world; no accent in EN.
   * - PNJ / personnage non joueur
     - NPC / non-player character
     - Meta.
   * - poing levé
     - raised fist
     - Out-of-game signal; "STOP" safe word kept.
   * - Sabarim / sabarite
     - Sabarim / Sabarith
     - Country / adjective.
   * - Salima / salimien
     - Salima / Salimian
     - City / adjective.
   * - sorceleur / Ordre des Sorceleurs
     - witcher / Order of Witchers
     - FR "sorceleur" is the official French for "witcher".
   * - Yods / yodisme / yodique / fidèles yodiques
     - the Yods / Yodism / Yodic / the Yodic faithful
     - Religion; capitalised; always plural "Yods".
   * - Zarathoustra / Serment de Zarathoustra
     - Zarathustra / Oath of Zarathustra
     - Standard EN spelling; "jurer par Zarathoustra" = "to swear by Zarathustra" (Archives).

Mystery Party: Archives (Les Archives Secrètes des Maupertuis)
===============================================================

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - 3h30 (symbol library_outside_portal_remaining_time)
     - 3½ h
     - Symbol value chosen per glossary convention; must match other batches.
   * - Accéder au domaine interdit
     - Access the Forbidden Domain
     - Quest heading.
   * - Action ou Fait
     - Action or Fact
     - Facts-summary table header.
   * - adoubement
     - dubbing
     - Maupertuis heirs' initiation ceremony (knighting metaphor).
   * - adresse mortuaire (« 42 rue d'Hadès »)
     - mortuary address ("42 Hades Street")
     - Needed by the Invoker's "Message to a Deceased".
   * - agents secrets mirandiens / Espions mirandiens / soldats mirandiens
     - Mirandian secret agents / Mirandian Spies / Mirandian soldiers
     - Faction (``spy_*`` files).
   * - Agitateur aluminique / Balance à plombs / Cristallisoir / Fioles jaugées en cristal
     - Aluminic stirrer / Weighted balance scale / Crystallising dish / Graduated crystal vials
     - Alchemist utensils.
   * - ailes (des fantômes)
     - wings (of the phantoms)
     - Epilogue costume (feathers / LEDs / steampunk).
   * - aimant magnétique (logo / symbole / étiquette)
     - "magnet" logo / "magnet" symbol / "magnet" label
     - Out-of-game marker of magnetic locks (Lockpicker, Sounder sheets).
   * - Alchémille / Chrysope / Joubarbe / Livèche / Sumac vénéneux / Digitale / Œil de triton
     - Lady's mantle / Lacewing / Houseleek / Lovage / Poison sumac / Digitalis / Eye of newt
     - Alchemist home ingredients. "Digitale" = "Digitalis", since the Druid reveals that the archaic "foxglove" (gant-de-renard) is the same plant. "Œil de triton" = the traditional "Eye of newt" (Macbeth), never "Newt's eye".
   * - alchimiste
     - Alchemist
     - Parcival role (canonical, parcival_alchemist).
   * - Amplificans / Bague Amplificans
     - Amplificans / Amplificans Ring
     - Legendary artefact family; verbatim.
   * - Analyse d'artefacts et de sépultures
     - Analysis of artefacts and burials
     - Unveiler sheet heading.
   * - ancrage / point d'ancrage / ancré / chaînes spirituelles
     - anchoring / anchor point / anchored / spiritual chains
     - Phantom mechanic.
   * - Ankou (l') / guide des âmes
     - the Ankou / guide of souls
     - Deity NPC (god_ankou); Breton name kept.
   * - anthropologue
     - Anthropologist
     - Explorer role (canonical).
   * - Anticiper (consigne de planning MJ)
     - Prepare for
     - GM schedule cue ("[Musique] Anticiper la Confession..." = "[Music] Prepare for the Confession..."); never "Anticipate".
   * - Aperçu des archives secrètes des Maupertuis
     - Overview of the Maupertuis secret archives
     - Section heading.
   * - Archives Secrètes des Maupertuis (Les) / archives secrètes des Maupertuis
     - The Secret Archives of the Maupertuis / the Maupertuis secret archives
     - Game title vs. running text.
   * - archiviste (l') / précepteur-archiviste
     - the Archivist / tutor-archivist
     - Phantom NPC (phantom_archivist).
   * - arkonte / l'arkonte Valerias / Arkonte yodique
     - Arkon / the Arkon Valerias / Yodic Arkon
     - Title (pl. Arkons), canonical from phantom_arkon.
   * - arme de poing (arbalète)
     - handheld weapon
     - NOT "handgun"; refers to the Woodsman's mini crossbow.
   * - "Armement qui blesses la chair, blesse aussi l'âme"
     - "Weaponry that wounds the flesh, wound the soul as well"
     - Weapon Blessing incantation.
   * - armure de Mithril
     - Mithril armour
     - Item.
   * - astrolabe de téléportation
     - teleportation astrolabe
     - Thief's item. Formula: "Astrolabe, carry me over there".
   * - atelier / établi / cabinet d'alchimie
     - alchemy workshop / alchemy workbench / alchemy study
     - Place (Forbidden Domain).
   * - atelier / établi de gemmologie
     - gemmology workshop / gemmology workbench
     - Place.
   * - attaques physiques / magiques / sacrées
     - physical / magical / sacred attacks
     - Injury mechanic.
   * - au-delà (l') / rejoindre l'au-delà
     - the afterlife / pass on to the afterlife
     - Lore.
   * - aube papale dorée
     - golden papal alb
     - Magus's burial robe.
   * - automate / androïde / automates serviteurs / Automate - …
     - automaton (pl. automatons) / android / servant automatons / Automaton - …
     - Sheet prefix.
   * - automate de garde / La Sentinelle de la Bibliothèque / automate tueur
     - sentinel automaton / the Library Sentinel / killer automaton
     - NPC (automaton_sentinel).
   * - automate de service / automates de service
     - serving automaton(s)
     - Table-service automatons (vs. "sentinel automaton").
   * - automate nettoyeur / serveur / majordome / chanteur / blagueur / encyclopédique / photographe
     - cleaner / server / butler / singer / joker / encyclopedic / photographer automaton
     - NPC extras' roles.
   * - Autres connaissances diverses
     - Other miscellaneous knowledge
     - Recurrent sheet heading (Anthropologist, Lockpicker).
   * - avatar(s) / Avatar - …
     - avatar(s) / Avatar - …
     - Novel heroes incarnated. Lowercase in running text, as in FR; capital only in headings, at sentence start and in the sheet prefix "Avatar - …".
   * - aventurine / oeil-de-tigre / clairvoyant minéral / arbre éternel / gant-de-renard
     - aventurine / tiger's eye / clairvoyant mineral / eternal tree / foxglove
     - Druid's archaic ingredient names.
   * - Axoliens (pays)
     - Axolian lands
     - Place.
   * - Bahamoot / diacres de Bahamoot / « Par Bahamoot… »
     - Bahamoot / Diakons of Bahamoot / "By Bahamoot…"
     - Cosmic dragon god; incantation opener.
   * - bande-son / bande son
     - soundtrack
     - GM meta; "lancer la bande-son" = "trigger the soundtrack".
   * - banquet d'outre-monde / buffet d'outre-monde / ouverture du buffet
     - Otherworld Banquet / Otherworld Buffet / buffet opening
     - Event.
   * - Barbe Blonde
     - Blondbeard
     - Duchess's corsair husband (pun on Blackbeard).
   * - bataille finale
     - final battle
     - Event / heading.
   * - batterie cubique (détecteur de métaux)
     - cubic battery
     - Sounder quest item.
   * - Béhémoth
     - Behemoth
     - Second dragon god.
   * - bénédiction / bénir / béni(te) / armes bénites
     - blessing / to bless / blessed / blessed weapons
     - Mechanic.
   * - Bénédiction d'arme
     - Weapon Blessing
     - Exorcist ritual (heading).
   * - Bénédiction de terrain anti-zombie
     - Anti-Zombie Ground Blessing
     - Invoker ritual (heading).
   * - Bête (la) / la Bête des Maupertuis / la Bête du Domaine Interdit
     - the Beast / the Maupertuis Beast / the Beast of the Forbidden Domain
     - Phantom NPC (phantom_beast).
   * - bibliothèque enfouie / souterraine
     - buried library / underground library
     - Place.
   * - blason / armoiries / héraldique
     - coat of arms / arms / heraldry
     - Anthropologist lore.
   * - blatte cendrée / oeil de tricératops / feuilles d'edelweiss
     - ash-grey cockroach / triceratops eye / edelweiss leaves
     - Invulnerability potion ingredients (complement glossary row).
   * - blessure biologique / spirituelle / sacrée / blessé
     - biological injury / spiritual injury / sacred injury / injured
     - Mechanic; "spirituelle" and "sacrée" are synonyms (spiritual injury = sacred injury).
   * - BOF / NOPE / A PRECISER (notes MJ dans les commentaires Jinja)
     - MEH / NOPE / TO BE SPECIFIED
     - Jinja-comment GM shorthand.
   * - Boîte à Murmures
     - Whispering Box
     - Mérédice's riddle box.
   * - brassard vert émeraude
     - emerald-green armband
     - Spies' identifying garment.
   * - broche
     - brooch
     - Treasure-quest jewels.
   * - buffet dinatoire magique des 4 mondes
     - magic dinner buffet of the four worlds
     - Place.
   * - bureau d'études d'occultisme (de Mérédice)
     - (Mérédice's) occult-studies study
     - Place in the Forbidden Domain, under rubble.
   * - cadenas transparent
     - transparent padlock
     - Lockpicker item.
   * - caducée
     - caduceus
     - Maupertuis coat of arms.
   * - Cajou / Pistache
     - Cashew / Pistachio
     - Dragon mouse names.
   * - carabine Nerf / balles Nerf
     - Nerf rifle / Nerf bullets
     - Sentinel automaton props.
   * - cardinal Tridentès
     - Cardinal Tridentes
     - Historical villain; accent dropped.
   * - cartouches de vapeur de cire pressurisée
     - pressurised wax vapour cartridges
     - UV lamp "batteries" (Unveiler).
   * - Cassandra / Prophétie de Cassandra
     - Cassandra / Cassandra's Prophecy
     - Hologram prophecy.
   * - Cassiopée de Thiersonne
     - Cassiopeia de Thiersonne
     - Duchess's name.
   * - ceinture beige
     - beige belt
     - Explorers' identifying garment.
   * - célébrant / officiant
     - celebrant / officiant
     - Ritual vocabulary.
   * - Charme d'esprit
     - Spirit Charm
     - Exorcist ritual (heading).
   * - chaudronnet cylindrique en cuivre
     - small cylindrical copper cauldron
     - Pyrolitis Tincture container.
   * - Chrysocolle / fluorite / lymphe de tarantule / jus de chrysanthrope / filtrat de marée lunaire / rosée d'éclair / seigle barbaquin
     - Chrysocolla / fluorite / tarantula lymph / Chrysanthrope juice / lunar tide filtrate / lightning dew / Barbaquin rye
     - Alchemist ingredients (invented names kept).
   * - cigale (cri de cigale)
     - cicada (cicada chirp)
     - Trap sound cue.
   * - cimetière
     - graveyard
     - Place.
   * - clairvoyance / voyant(e) / dons de voyance
     - clairvoyance / seer / gift of sight
     - Oracle/Duchess lore.
   * - cloches / gong
     - bells / gong
     - Sound cues switching phantom phases.
   * - clochette argentée / sonnette de table métallique
     - silver table bell / metal table bell
     - Physical descriptions of the Spectral Bell.
   * - Clochette Spectrale / clochette de table / clochette métallique / clochette de frénésie spectrale / clochette de service
     - Spectral Bell / table bell / metal table bell / spectral frenzy table bell / service bell
     - Ankou's item (symbol ``table_bell_name``). Bare "la clochette" = "the bell" or "the table bell"; never "small bell" or "handbell". See also "clochette argentée".
   * - Clôture Absolue / lever la Clôture
     - Absolute Enclosure / lift the Enclosure
     - Arkon's curse on the library.
   * - Cocktail de Réjuvénation
     - Rejuvenation Cocktail
     - Parcival quest potion.
   * - code secret / code à 3 lettres
     - secret code / 3-letter code
     - Puzzle meta.
   * - coffre légendaire
     - legendary chest
     - Holds the Thanatologue.
   * - coffret à bijoux (d'Isadora)
     - (Isadora's) jewellery box
     - Thief's backstory; code 159.
   * - coin de l'archiviste / de l'enfant / de l'arkonte / du voleur
     - the Archivist's nook / the child's nook / the Arkon's nook / the Thief's nook
     - Anchor points.
   * - collier anti-poison
     - anti-poison necklace
     - Item (toxic corridor).
   * - Collier éthérique d'aura manaïque / de bénédiction / de force vitale / de peau de pierre
     - Etheric Necklace of Manaic Aura / of Blessing / of Vital Force / of Stone Skin
     - Items; "les colliers éthériques" = "the etheric necklaces".
   * - compétence(s) spéciale(s) / Vos compétences
     - special ability / abilities; Your abilities
     - Recurrent sheet heading.
   * - COMPLEMENT D'INSTRUCTIONS - …
     - ADDITIONAL INSTRUCTIONS - …
     - Heading (complements).
   * - COMPLEMENTS DE BRIEFING POUR LES PARTICIPANTS
     - ADDITIONAL BRIEFINGS FOR PARTICIPANTS
     - Heading.
   * - Compléments des Figurants (document)
     - NPC Actors' Supplements
     - Document title referenced in briefings.
   * - complot anti-arkonte (Le)
     - The anti-Arkon conspiracy
     - Druid sheet heading.
   * - confession de mission
     - mission confession
     - Arkon ritual/speech.
   * - confession mithraïte / mithraïque
     - Mithraite denomination
     - Yodic religion branch. Both FR adjectives give "Mithraite"; a religious "confession" is a "denomination" (false friend), cf. "confession (razulite / taranite)".
   * - confrère (arkonte) / confrère diacre / vos confrères
     - brother in the faith (Arkon) / fellow Diakon / your fellow Diakons
     - The Anthropologist reveals himself to the Arkon as a "brother in the faith" (phantom_arkon_sheet); between Diakons "confrère" = "fellow Diakon". Never the redundant "fellow brother".
   * - Connaissance des bêtes dangereuses
     - Knowledge of dangerous beasts
     - Woodsman sheet heading.
   * - Connaissance des codes secrets / Kit d'observation-écoute
     - Knowledge of secret codes / Observation and listening kit
     - Runologist sheet headings.
   * - Connaissance des pentacles et sceaux
     - Knowledge of pentacles and seals
     - Invoker sheet heading.
   * - Connaissances en commun avec …
     - Knowledge shared with …
     - Sheet heading.
   * - Connaisseurs (en-tête de tableau)
     - Known by
     - Facts-summary table header (gamemaster_facts_summary).
   * - contre-sortilège
     - counter-spell
     - Magic.
   * - cordelette de chanvre / draps noirs / tissu noir / sacoche noire
     - hemp rope / black sheets / black cloth / black bag
     - Out-of-game markers for blocked passages and OOC items.
   * - corridor d'outre-monde
     - otherworld corridor
     - Inter-world link (Avatar books).
   * - corridor planétaire
     - planetary corridor
     - Teleportation system.
   * - corridor toxique
     - toxic corridor
     - Place.
   * - corridors éthériques
     - etheric corridors
     - Place (dead-ends).
   * - crâne sonore
     - sounding skull
     - Cursed object.
   * - cristal romantique / marin / piquant / innocent
     - romantic / marine / prickly / innocent crystal
     - Spiritual Orb keys.
   * - Crochetage de serrures / kit de crochetage
     - Lockpicking / lockpicking kit
     - Lockpicker ability / item.
   * - crocheteur
     - Lockpicker
     - Spy role (canonical).
   * - curare / flèche au curare
     - curare / curare arrow
     - Clue.
   * - Cyck du Clivra / CLIVRA
     - Cyck du Clivra / CLIVRA
     - Author of the alexandrine version; association name, verbatim.
   * - Dangers et blessures / Événements rythmant le jeu
     - Dangers and injuries / Events that pace the game
     - GM manual headings.
   * - déchus (Les) / dragons déchus
     - The Fallen / fallen dragons
     - 5th team sheet title (dragons_role).
   * - défiance
     - distrust
     - Character traits; false friend, never "defiance".
   * - dégénérescence marbrée
     - marbled degeneration
     - Parcival hereditary disease.
   * - démineur / déminage
     - Minesweeper / minesweeping
     - Spy role (canonical).
   * - Déroulement du jeu
     - Course of the game
     - GM manual heading.
   * - désenvoûtement / désenvoûter / dissiper
     - dispelling / to dispel
     - Mechanic.
   * - désenvoûteur
     - Dispeller
     - Diakon role (canonical).
   * - Détecteur de magnétisme / feuille de détection
     - Magnetism Detector / magnetic viewing film
     - Sounder ability / item.
   * - Détecteur de métaux
     - Metal Detector
     - Sounder item.
   * - Déverrouilleur magnétique / clé magnétique
     - Magnetic Unlocker / magnetic key
     - Lockpicker ability / item.
   * - devise / geste symbolique
     - motto / symbolic gesture
     - Faction symbols.
   * - dévoileur
     - Unveiler
     - Explorer role (canonical).
   * - diacre(s)
     - Diakon(s)
     - Canonical faction name; NOT "deacon".
   * - Discours d'adieu aux joueurs / Discours d'ouverture du buffet
     - Farewell speech to the players / Buffet opening speech
     - Sheet headings.
   * - Diviciacos
     - Diviciacos
     - Druid's name.
   * - divin (le) / Divinité - …
     - the divine / Deity - …
     - World category; sheet prefix.
   * - Divinités et mondes alternatifs / Carte du monde de Pangéa
     - Deities and alternative worlds / World map of Pangea
     - Lore headings.
   * - Djinn renégat Meujeuh / Meujeuh
     - renegade Djinn Geeyem / Geeyem
     - The GM's in-game persona (last_minute_instructions_for_participants). "Meujeuh" is "MJ" pronounced; rendered by the matching "G-M" pun "Geeyem".
   * - Djinn(s) / Djinn renégat
     - Djinn(s) / the renegade Djinn
     - GM's in-game persona.
   * - domaine autorisé / étage autorisé / étage du bas
     - authorised domain / authorised floor / lower floor
     - Place.
   * - domaine interdit / étage interdit / étage du haut
     - Forbidden Domain / forbidden floor / upper floor
     - Capitalise "Forbidden Domain" when named.
   * - Dominion (le)
     - the Dominion
     - Automaton command bracelet.
   * - Donjon des Pass'muraille
     - Pass'muraille Keep
     - "donjon" = keep, NOT dungeon.
   * - dragon(s) / dieux-dragons
     - dragon(s) / dragon gods
     - Dragons role.
   * - druide (le)
     - the Druid
     - Avatar NPC (avatar_druid), the villain.
   * - duchesse (la)
     - the Duchess
     - Avatar NPC (avatar_duchess).
   * - éboulis
     - rubble / rockfall(s)
     - Hiding places in the Forbidden Domain.
   * - éboulis rocheux
     - rockfall
     - Dynamite target (crumpled cardboard).
   * - élémentaire de feu
     - fire elemental
     - Druid's spell.
   * - Élixir Flexifiant
     - Flexifying Elixir
     - Sub-recipe.
   * - Encens prophétique / cône d'encens / fontaine d'encens
     - Prophetic Incense / incense cone / incense fountain
     - Alchemist recipe / prophecy trigger.
   * - encensoir / encensement / encenser
     - censer / censing / to cense
     - Invoker gear.
   * - enchantement anti-explosion
     - anti-explosion enchantment
     - Same container.
   * - Encyclopédie du monde des esprits
     - Encyclopedia of the Spirit World
     - Exorcist sheet heading.
   * - énigme / parcours d'énigmes / SOLUTIONS DES ÉNIGMES VISUELLES
     - puzzle / puzzle trail / SOLUTIONS TO THE VISUAL PUZZLES
     - "riddle" only for verbal riddles.
   * - entre-monde
     - in-between world
     - Djinn/dragon lore.
   * - envoûtement / envoûté / envoûter / enchantement
     - bewitchment / bewitched / to bewitch / enchantment (positive)
     - Dispeller mechanic.
   * - envoûtement dynastique / initiation dynastique
     - dynastic bewitchment / dynastic initiation
     - Octave's brooch trial (spy complement).
   * - envoûtement simple / complexe / légendaire
     - simple / complex / legendary bewitchment
     - Three levels.
   * - épilogue (musical)
     - (musical) epilogue
     - Event.
   * - Équipes de joueurs / Figurants (en-têtes)
     - Player teams / NPC actors
     - GM manual headings.
   * - ère du Grand Apaisement / an 1000
     - Era of the Great Appeasement / year 1000
     - Era name.
   * - errance (spectrale) / en errance / esprit errant / revenants errants
     - (spectral) wandering / wandering / wandering spirit / wandering revenants
     - Phantom phase.
   * - "Esprit errant, nous brisons les chaines qui te retiennent" / "Esprit errant, je restaure les chaines qui te retenaient"
     - "Wandering spirit, we break the chains that hold you" / "Wandering spirit, I restore the chains that held you"
     - Spiritual Anchor Release / Cancellation incantations.
   * - étiquette "ne pas toucher" (main barrée)
     - "do not touch" label (crossed-out hand)
     - Fragile decorative items.
   * - étoile autocollante dorée / argentée ; pastille
     - gold sticker star / silver sticker star; sticker
     - Out-of-game markers. "pastille" referring back to a sticker star = "sticker" (never "sticker dot"); only the round coloured tidying dots of game_rules are "round coloured sticker dots".
   * - étole violette
     - purple stole
     - Diakons' identifying garment.
   * - exorciste / exorcisme / Les rituels d'exorcisme
     - Exorcist / exorcism / Exorcism Rituals
     - Diakon role (canonical).
   * - explorateurs héliossars / explorateurs-archéologues
     - Heliossarian explorers / explorer-archaeologists
     - Faction (``explorer_*`` files).
   * - explosifs / bâtonnets de dynamite
     - explosives / sticks of dynamite
     - Minesweeper item.
   * - Expulsion d'esprit
     - Spirit Expulsion
     - Exorcist ritual (heading).
   * - Faction - …
     - Faction - …
     - Sheet title prefix.
   * - fantomatique
     - phantom-like / phantom (attributive)
     - GM manual, NPC sheets ("la Bête fantomatique" = "the phantom Beast", "âme fantomatique" = "phantom soul"); never "ghostly".
   * - fantôme / Fantôme - …
     - phantom / Phantom - …
     - Canonical (``phantom_*`` files), not "ghost".
   * - fantôme incarné / désincarné ; phase incarnée ; s'incarner
     - embodied / disembodied phantom; embodied phase; to become embodied
     - Phantom mechanic. "s'incarner" = "to become embodied" ("he becomes embodied", "they become embodied"), never "embody oneself". For Avatars/dragons use "incarnation".
   * - Fédore Pass'muraille
     - Fedore Pass'muraille
     - Thief's name; kept as proper noun.
   * - feuille de mémo (codes secrets) / tableau de correspondance (runes)
     - memo sheet / correspondence table
     - Runologist props.
   * - fiche de déroulement de quête
     - quest progression sheet
     - GM meta (NPC actors follow a group with it).
   * - fiche de figurant / fiche de mission / fiche de suivi / FICHE DE SUIVI POUR …
     - NPC sheet / mission sheet / tracking sheet / TRACKING SHEET FOR …
     - GM meta.
   * - fiche de planification des prophéties
     - prophecy schedule sheet
     - Duchess's GM handout.
   * - fil blanc / grelot
     - white thread / jingle bell
     - Trap materials.
   * - fiole / dose unique
     - vial / single dose
     - Potion rules.
   * - flash lumineux
     - light flash
     - Trap cue.
   * - flèches blanches (en scotch) / scotch blanc
     - white arrows (in tape) / white tape
     - Archivist's markers to the sub-recipes, made in-game of white tape on the floor; never "crosses", never phosphorescent paint.
   * - fléchette (d'arbalète) / fléchettes nerf / balles
     - dart (crossbow bolt) / Nerf darts / bullets
     - Woodsman ammo.
   * - folie meurtrière de l'automate de garde
     - the sentinel automaton's murderous madness
     - Event heading.
   * - Fond de l'intrigue (SPOILER)
     - Plot background (SPOILER)
     - GM heading.
   * - Force herculéenne
     - Herculean Strength
     - Woodsman ability heading.
   * - frénésie spectrale
     - spectral frenzy
     - Phantom mechanic.
   * - Fungal rouge (jus de)
     - red Fungal (juice)
     - Ingredient.
   * - fusil nerf
     - Nerf gun
     - Sentinel automaton's weapon.
   * - gage (sanction ludique)
     - forfeit
     - Abyssal Vortex mental-damage penalties.
   * - gants lumineux / voile
     - light-up gloves / veil
     - Phantom costume (wandering phase).
   * - Gardien des bois
     - Woodsman
     - Parcival role (canonical, parcival_woodsman).
   * - Généalogie des Maupertuis
     - Genealogy of the Maupertuis
     - Booklet.
   * - glaive (ULTRA-LOURD) de l'arkonte
     - the Arkon's (ULTRA-HEAVY) gladius
     - Short sword; NOT "glaive".
   * - goule des cavernes
     - cave ghoul
     - The Beast's species.
   * - Grand Sage
     - Great Sage
     - Kamilia shamanic lore.
   * - grimoire / grimoire maudit
     - grimoire / cursed grimoire
     - Generic.
   * - grimoire chantant / moulin à aube
     - singing grimoire / paddle mill
     - Treasure-mill activator (treasure quest vision).
   * - Grimoire Traceur
     - Tracker Grimoire
     - In-world name of the beacon-scanner app.
   * - Guerre des Trente Sorciers
     - War of the Thirty Sorcerers
     - Era event.
   * - Guide de Gaïa
     - Guide of Gaia
     - Druid's villain title.
   * - H-45mn / H+2mn / H+1h20
     - H-45 min / H+2 min / H+1:20
     - Schedule notation (minutes vs. hours:minutes).
   * - Havre de Nature
     - Haven of Nature
     - Druid's promise.
   * - héritiers Parcival / famille Parcival
     - Parcival heirs / Parcival family
     - Faction (``parcival_*`` files).
   * - héros / héroïne de roman
     - novel hero / novel heroine
     - Avatar category.
   * - Histoire du jeu
     - Story of the game
     - GM heading (backstory).
   * - Holistix
     - Holistix
     - Plant (purple bells).
   * - imposer les mains / imposition des mains
     - to lay one's hands on / laying on of hands
     - Dispeller / Exorcist ritual gesture.
   * - inamovible (coffrets, valises)
     - immovable
     - Game rules.
   * - incantation / formule magique
     - incantation / magic formula
     - Ritual vocabulary.
   * - Informations et instructions spécifiques
     - Specific information and instructions
     - Recurrent NPC sheet heading.
   * - initiation / Sceau d'initiation
     - initiation / Initiation Seal
     - Octave's dynastic trial.
   * - Initiations rituelles / Estimation des monnaies et gemmes / Connaissance des blasons
     - Ritual initiations / Appraisal of coins and gems / Knowledge of coats of arms
     - Anthropologist sheet headings.
   * - initié(s) / non-initié
     - initiate(s) / non-initiate
     - Anyone able to join a sacred ritual.
   * - Innovation rituelle / Récompense / Salvation / Herboristerie
     - Ritual Innovation / Reward / Salvation / Herbalism
     - Dragon abilities (headings).
   * - Inquisiteur-Exorciste
     - Inquisitor-Exorcist
     - Dispeller backstory.
   * - intuition
     - intuition
     - Oracle mechanic (vs. prophecy).
   * - inventeur (l')
     - the Inventor
     - Avatar NPC (avatar_inventor).
   * - invocateur / invocation / invoquer / arts invocatoires
     - Invoker / invocation / to invoke / invocatory arts
     - Diakon role (canonical).
   * - Iridium / Platine / Mithril
     - Iridium / Platinum / Mithril
     - Noble metals for blessing.
   * - Isadora (née Guerlevan) / Quirinius de Maupertuis
     - Isadora (née Guerlevan) / Quirinius de Maupertuis
     - Octave's parents.
   * - "J'implore que les Yods vous éclairent" / "Que je sois pour vous leur miroir"
     - "I beseech the Yods to enlighten you" / "May I be their mirror unto you"
     - Arkon greeting / reply.
   * - jabot bleu-royal
     - royal-blue jabot
     - Parcival identifying garment.
   * - Jacko
     - Jacko
     - Inventor's nickname.
   * - jeu de piste
     - treasure hunt
     - Maupertuis family backstory (GM manual).
   * - journal de bord / journal intime
     - logbook / diary
     - Archivist's / Octave's items.
   * - jurer par Zarathoustra
     - to swear by Zarathustra
     - Oath mechanic.
   * - Kahflu
     - Kahflu
     - Ceremonial drink.
   * - Kamilia (jungle de) / Shaman de la jungle de Kamilia
     - Kamilia Jungle / Shaman of the Kamilia Jungle
     - Place / Anthropologist title.
   * - L'entrée en scène des joueurs
     - The players' entrance
     - Event heading.
   * - L'univers du jeu / Contexte historico-géographique
     - The game universe / Historical and geographical context
     - Lore headings.
   * - La dernière maisonnée des Maupertuis
     - The last Maupertuis household
     - Lore heading.
   * - La survenue des révélations / révélations de type "visuel" / "auditif" / Les intuitions
     - The occurrence of revelations / Revelations of the "visual" / "auditory" type / Intuitions
     - Oracle sheet headings.
   * - lampe à ultraviolets / lampe UV / message UV
     - ultraviolet lamp / UV lamp / UV message
     - Unveiler item.
   * - message UV du portrait de Mérédice : "Adieu soeurette, qui mourra verra (signé Octave)"
     - UV message of Mérédice's portrait: "Farewell sis, time will kill (signed Octave)"
     - Pun on "qui vivra verra" / "time will tell" (checklist, optional UV message); an English UV prop must use this wording.
   * - Le ballet des automates
     - The Ballet of the Automatons
     - Inventor's novel title.
   * - Le déclin magique / contraste magique
     - The magical decline / magical contrast
     - Lore.
   * - Le fonctionnement des fantômes / Des deux formes fantomatiques / Des chaines spirituelles / Des rituels de libération / Des périls des restes corporels / De la dangerosité des revenants errants
     - How phantoms work / Of the two phantom forms / Of spiritual chains / Of liberation rituals / Of the perils of bodily remains / Of the dangerousness of wandering revenants
     - Phantom-article headings (archaic "Of ..." kept).
   * - Le reconnaissance des envoûtements d'artefacts / La suppression des envoûtements négatifs
     - Recognising artefact bewitchments / Removing negative bewitchments
     - Dispeller sheet headings.
   * - "Le savoir est pouvoir" / "Noble de coeur comme de sang" / "Le dragon est notre guide" / "Mirandia pour toujours brillera"
     - "Knowledge is power" / "Noble of heart as of blood" / "The dragon is our guide" / "Mirandia forever shall shine"
     - Faction mottos.
   * - Les cygnes d'étang
     - The Pond Swans
     - Duchess's novel title.
   * - Les ingrédients / ustensiles que vous possédez ; Les recettes que vous connaissez ; Quelques informations supplémentaires
     - The ingredients / utensils you own; The recipes you know; Some additional information
     - Alchemist sheet headings.
   * - Les sorciers du chaos / Tome 3
     - The Sorcerers of Chaos / Volume 3
     - Druid's novel.
   * - Libération d'ancrage spirituel / Annulation
     - Spiritual Anchor Release / Cancellation
     - Exorcist ritual (heading).
   * - licorne de nacre / trèfle à cinq feuilles
     - mother-of-pearl unicorn / five-leaf clover
     - Prophecy artefacts.
   * - Lieux
     - Locations
     - GM heading.
   * - lignée / dynastie Maupertuis
     - Maupertuis lineage / dynasty
     - Lore.
   * - livre d'or
     - guest book
     - Debriefing reminder (online comments). Two words in every game ("GUEST BOOK" in capitals).
   * - livre factice
     - fake book
     - Puzzle item.
   * - Livre Yodique des Morts
     - Yodic Book of the Dead
     - = the Thanatologue.
   * - livres jumeaux (du père Maupertuis)
     - twin books (of the Maupertuis father)
     - Treasure puzzle.
   * - Lotion / Potion de Révélation (aussi « Lotion de Restauration »)
     - Lotion of Revelation
     - Unify the three FR variants (Lotion / Potion de Révélation, Lotion de Restauration) as "Lotion of Revelation".
   * - Lotion de Clairvoyance
     - Clairvoyance Lotion
     - Sub-recipe.
   * - loupe et stéthoscope
     - magnifying glass and stethoscope
     - Runologist props.
   * - luminis
     - luminis
     - Minesweeper LED candles (invariable).
   * - lunettes de couleur / codes polychromatiques
     - coloured glasses / polychromatic codes
     - Anthropologist device.
   * - Mage Mos Peratys / mage / Mage Sombre / tombeau du mage
     - the Magus Mos Peratys / mage / the Dark Magus / the Magus's tomb
     - Founder NPC (phantom_magus). "the Magus's tomb" stays lowercase "tomb" (descriptive, not a place name).
   * - magiciens-guérisseurs / mages-guérisseurs
     - healer-mages
     - Maupertuis lineage.
   * - Main électrique (mode de déminage)
     - Electric hand (minesweeping mode)
     - Minesweeper briefing change.
   * - maisonnée Maupertuis
     - Maupertuis household
     - Lore.
   * - Maître Parchemine
     - Master Parchemine
     - Archivist's name.
   * - malédiction / maudit / malédiction de la bibliothèque
     - curse / cursed / the library curse
     - Core plot.
   * - maléfice / maléfique
     - hex / malefic
     - Magic.
   * - mallette administrative (noire)
     - (black) administrative briefcase
     - Puzzle item.
   * - malus
     - penalty
     - Injury mechanic.
   * - manoir des Maupertuis
     - Maupertuis manor
     - Place (razed).
   * - MANUEL DU MAITRE DE JEU
     - GAME MASTER'S MANUAL
     - Title.
   * - marasme planétaire / grand marasme
     - Planetary Cataclysm / the great cataclysm
     - Register-adjusted.
   * - marqueurs (hors-jeu)
     - (out-of-game) markers
     - Stickers, feathers, etc.
   * - Maupertuis (les)
     - the Maupertuis
     - Family name, invariable.
   * - Mère Nature / Harmonie Naturelle / Magie des Esprits
     - Mother Nature / Natural Harmony / Spirit Magic
     - Druid's creed.
   * - Mérédice de Maupertuis
     - Mérédice de Maupertuis
     - Keep accents.
   * - Message à un défunt / message spirituel
     - Message to a Deceased / spiritual message
     - Invoker ritual (heading).
   * - Mini-arbalète
     - Mini Crossbow
     - Woodsman ability heading / item.
   * - mini-jungle
     - mini-jungle
     - Place (Druid's).
   * - Mirandia / mirandien
     - Mirandia / Mirandian
     - Island country.
   * - mois pangéens : Septemaire / septemaire / octobaire / decembaire / februaire / junaire
     - Pangean months: Septemaire / septemaire / octobaire / decembaire / februaire / junaire
     - Coined month names in clue dates; verbatim, never translated.
   * - molettes à chiffres
     - numbered dials
     - Combination locks.
   * - moment de gloire
     - moment of glory
     - GM design meta.
   * - momie (du mage)
     - (the Magus's) mummy
     - Tomb trap.
   * - Monastère de Rochesombre
     - Rochesombre Monastery
     - Place.
   * - monde des vivants / des morts / des livres / des automates / monde divin
     - world of the living / world of the dead / world of books / world of automatons / divine world
     - Core lore (five worlds).
   * - monolithes
     - monoliths
     - Backstory.
   * - mort-vivant / zombie / zombifier
     - undead / zombie / to zombify
     - Necromancy.
   * - moulin à café / moulin magique / moulin boisé / Moulin au Trésor
     - coffee mill / magic mill / wooden mill / Treasure Mill
     - Spy quest artefact.
   * - nécromancien / nécromancie
     - necromancer / necromancy
     - Lore.
   * - niche de la Bête
     - the Beast's den
     - Place.
   * - Nimouk / Slavinka / Thelassar
     - Nimouk / Slavinka / Thelassar
     - Places.
   * - NOTE hors-jeu / hors-roleplay
     - Out-of-game note / out-of-game
     - Meta. "hors-roleplay" = "out-of-game" project-wide (Shared row "hors-roleplay"); never "out-of-roleplay".
   * - Notes hors-jeu : le déroulement des révélations
     - Out-of-game notes: how revelations unfold
     - Oracle sheet heading (macro prophecy_workflow_instructions).
   * - Nouvelle Ère
     - New Era
     - Lore.
   * - "Ô <nom du dieu>, toi qui résides au <adresse mortuaire>, réponds à notre quémande : <demande>."
     - "O <name of the god>, you who dwell at <mortuary address>, answer our plea: <request>."
     - Message to a Deceased incantation.
   * - "Ô sceau magique / Ô pentacle canonique, réveille-toi et écoute ma voix"
     - "O magic seal / O canonical pentacle, awaken and hear my voice"
     - Seal / pentacle activation incantation.
   * - océan diorique
     - Diorian Ocean
     - Place.
   * - Octave de Maupertuis (l'enfant)
     - Octave de Maupertuis (the child)
     - Phantom NPC (phantom_octave).
   * - oeillets de classeur blancs
     - white binder hole reinforcement rings
     - Out-of-game marker of magnetic locks.
   * - oracle (l') / oracle (vision)
     - the Oracle / oracle
     - Parcival role (canonical) vs. a delivered vision.
   * - orbe spirituel
     - Spiritual Orb
     - Artefact (plasma ball).
   * - ordre des choses
     - the order of things
     - Diakon motto-phrase.
   * - Ordre International de la Hiéraldique
     - International Order of Heraldry
     - Anthropologist lore.
   * - oreillette
     - earpiece
     - GM meta.
   * - organisateurs / orgas
     - organisers
     - Meta.
   * - ossements / dépouille / cendres
     - bones / remains / ashes
     - Clues.
   * - outre-monde / d'outre-monde
     - otherworld / otherworldly
     - Lore.
   * - "Ouvrez grandes vos oreilles, ouvrez grands vos yeux, car par la puissance pacificatrice de Bahamoot, voici que nous brisons les chaines impies qui emprisonnent cette matière !"
     - "Open wide your ears, open wide your eyes, for by the pacifying power of Bahamoot, behold, we break the unholy chains that imprison this matter!"
     - Dispeller incantation (complex bewitchment).
   * - paladin-exorciste
     - paladin-exorcist
     - Arkon's description.
   * - Paladium
     - Palladium
     - Noble metal of the Exorcist's Weapon Blessing (diakon_exorcist_role); FR typo corrected to "Palladium". Not the Mindstorm brotherhood "the Paladium", which keeps its in-world spelling.
   * - "Par Bahamoot, arrière, esprit errant" / "Par Bahamoot, lambine vers moi, esprit errant"
     - "By Bahamoot, begone, wandering spirit" / "By Bahamoot, dawdle towards me, wandering spirit"
     - Spirit Expulsion / Spirit Charm incantations.
   * - "Par Bahamoot, qu'en franchissant le seuil de l'éternité, j'emporte avec moi ce rempart contre-nature."
     - "By Bahamoot, may I, as I cross the threshold of eternity, take with me this unnatural rampart."
     - Absolute Enclosure Rupture incantation.
   * - "Par Bahamoot, qu'un repos sans rêve et sans fin berce cette dépouille mortuaire à tout jamais."
     - "By Bahamoot, may a dreamless and endless rest cradle these mortal remains for ever and ever."
     - Anti-Zombie Ground Blessing incantation.
   * - "Par Bahamoot, que se meuvent les cieux, qu'ils rejoignent la terre, que par ce mouvement de lumière, le fracas soit déchainé."
     - "By Bahamoot, may the heavens move, may they join the earth, may through this motion of light the thunderclap be unleashed."
     - Lightning Spell incantation.
   * - "Par Bahamoot, reste immobile."
     - "By Bahamoot, stay still."
     - Absolute Stasis incantation.
   * - "Par l'oiseau à trois têtes, reçois ma salutation" / "Par le serpent sans tête, reçois la mienne"
     - "By the three-headed bird, receive my greeting" / "By the headless snake, receive mine"
     - Kamilia shaman greeting / reply.
   * - "Par le soleil victorieux, Par le pouvoir des cieux, Portails disparaissez"
     - "By the victorious sun, By the power of the heavens, Portals, vanish"
     - Global Otherworld Corridor Rupture incantation.
   * - "Par le souffle sacré de Bahamoot, ô matière inerte, nous rompons les liens qui te lient aux strates ensorcelées"
     - "By the sacred breath of Bahamoot, O inert matter, we sever the bonds that bind you to the bewitched strata"
     - Dispeller incantation (simple bewitchment).
   * - Parcival
     - Parcival
     - Family name (not Percival).
   * - péché mignon
     - guilty pleasure
     - Spies' recurring phrase ("Et votre péché mignon, c'est…" = "And your guilty pleasure is…").
   * - pentacle / pentacle canonique
     - pentacle / canonical pentacle
     - Invoker mechanic.
   * - phase d'errance / passer en errance / repasser en incarné
     - wandering phase / switch to wandering / switch back to embodied
     - Phantom phase verbs.
   * - Philomène
     - Philomène
     - Parcival sick sister.
   * - Pierre anti-philosophale
     - Anti-Philosopher's Stone
     - Alchemist recipe.
   * - Pierre de lune (ingrédient alchimique du domicile Parcival)
     - Moonstone
     - Gem ingredient; distinct from the Beast's "moon stones" (phosphorescent pebbles).
   * - pierres de lune (galets phosphorescents)
     - moon stones (phosphorescent pebbles)
     - Beast's addiction.
   * - Pitch / Concept détaillé
     - Pitch / Detailed concept
     - GM manual headings.
   * - Plan du Jeu
     - Game Map
     - Referenced document.
   * - Planification des prophéties et intuitions
     - Scheduling of prophecies and intuitions
     - Event heading.
   * - PLANNING DETAILLÉ DU JEU / PLANNING DES PROPHETIES
     - DETAILED GAME SCHEDULE / PROPHECY SCHEDULE
     - Headings.
   * - plantes de la bibliothèque (symbol arkon_skull_location)
     - library plants
     - Symbol value; must match other batches.
   * - plumes colorées
     - coloured feathers
     - Prophecy triggers.
   * - portail de connaissances / catégorie « magie » / « analyse »
     - knowledge portal / "magic" / "analysis" category
     - Hint website.
   * - portail de transplanage / transplanage / portail de téléportation
     - teleportation portal / teleportation / teleportation portal
     - Both FR words name the same portal network: always "teleportation portal". Never "apparition" (in English an apparition is a ghost: false friend in a game full of phantoms).
   * - porte-voix à écho
     - echo megaphone
     - Inventor item.
   * - Potion d'Autorité
     - Potion of Authority
     - Zombie-command potion.
   * - Potion d'invulnérabilité
     - Potion of Invulnerability
     - Alchemist recipe.
   * - Potion de Charme et de Focus / Potion de Focus / Potion de Charme
     - Potions of Charm and of Focus / Potion of Focus / Potion of Charm
     - Exorcist support potions (diakon_exorcist_role, GM manual). The former "Philtre de Focus" of the Exorcist ritual is now "Potion de Focus" in FR too.
   * - Potion de Délieur de Langue
     - Tongue-Loosening Potion
     - Base of Potion of Authority.
   * - Potion de pestilence
     - Pestilence Potion
     - Alchemist recipe.
   * - Potion de vapeur de Thorium / vapeur de Thorium
     - Thorium vapour potion / Thorium vapour
     - Archives alchemy (checklist, Pyrolitis recipe clue): "vapour", never "steam".
   * - Potion de vieillissement accéléré / Potion de venin de serpent
     - Accelerated Ageing Potion / Snake Venom Potion
     - Enclosure-rupture ingredients.
   * - Potions dénichées / Bâtonnets d'explosifs / Réserve de luminis / Connaissance des mécaniques et des automates
     - Potions found / Sticks of explosives / Supply of luminis / Knowledge of mechanics and automatons
     - Spy sheet headings.
   * - précepteur
     - tutor
     - Archivist's original job.
   * - PREPARATION DES LIEUX
     - PREPARATION OF THE PREMISES
     - Schedule heading.
   * - Principes fondamentaux du jeu / des différents mondes
     - Fundamental principles of the game / of the different worlds
     - GM manual headings.
   * - prophétie / prophète / révélation (visuelle / auditive)
     - prophecy / prophet / (visual / auditory) revelation
     - Oracle mechanic.
   * - prothèse mécanique
     - mechanical prosthesis
     - Inventor healing.
   * - psychopompe
     - psychopomp
     - Ankou's title.
   * - puits « inutile »
     - the "useless" well
     - Dragon reward secret.
   * - Puzzle d'Ouverture du Domaine Interdit / Symboles d'Activation du Moulin au Trésor
     - Puzzle for Opening the Forbidden Domain / Activation Symbols of the Treasure Mill
     - Puzzle-solution headings.
   * - Pythie de Delphes
     - Pythia of Delphi
     - Oracle acting reference.
   * - quête / Quêtes et parcours d'énigmes
     - quest / Quests and puzzle trails
     - GM heading.
   * - quêteuse sans fond
     - bottomless collection pouch
     - Thief's magic moneybox.
   * - RECAPITULATIF DES DISCOURS DES FIGURANTS
     - SUMMARY OF NPC SPEECHES
     - Heading.
   * - règne / royaume des morts
     - kingdom of the dead
     - Ankou's speech, Beast section.
   * - Réminiscences mystiques
     - Mystic Reminiscences
     - Anthropologist ability heading.
   * - ressusciter
     - to resurrect
     - Thanatologue mechanic.
   * - Retour à la Nature (utopie)
     - "Back to Nature" utopia
     - Druid's novel ending.
   * - rituel / ritualiste / rituel d'expulsion / rituel de renvoi
     - ritual / ritualist / expulsion ritual / banishing ritual
     - Core mechanic.
   * - roman / Tome
     - novel / Volume
     - Avatars cannot carry novels.
   * - rubans blancs
     - white ribbons
     - Automaton marker.
   * - runes / Traducteur runique / runologue
     - runes / Runic Translator / Runologist
     - Explorer role (canonical).
   * - Rupture de Clôture Absolue
     - Absolute Enclosure Rupture
     - Invoker ritual (heading).
   * - Rupture globale de corridor d'outre-monde
     - Global Otherworld Corridor Rupture
     - Exorcist ritual (heading).
   * - sacoche porte-document
     - document satchel
     - Arkon's bag.
   * - sacré (le) / sacrée (attaque, arme, blessure)
     - the sacred / sacred (attack, weapon, injury)
     - Attack type.
   * - Sacrifice de Zarathoustra
     - Sacrifice of Zarathustra
     - Dark Thanatologue spell.
   * - salle ronde du briefing
     - round briefing room
     - Out-of-game start/end location.
   * - Salut de Pangéa
     - Salvation of Pangea
     - Druid's justification.
   * - salutation d'arkonte
     - Arkon's salutation
     - Recognition ritual between Arkon and Anthropologist.
   * - sanctuaire des Maupertuis
     - Maupertuis sanctuary
     - Synonym of the archives in player complements.
   * - sang bleu (comme la mer)
     - (sea-)blue blood
     - Druid clue.
   * - sceau (magique)
     - (magic) seal
     - Pentacle variant.
   * - Sceau de barrage absolu
     - Absolute Barrier Seal
     - Forbidden Domain lock.
   * - scène finale / Scènes théâtrales
     - final scene / Theatrical scenes
     - Event / rules heading.
   * - scientifique-dévoileur
     - scientist-Unveiler
     - Sounder sheet reference to the Explorer role.
   * - scientiste et maître-automaticien
     - scientist and master automaton-maker
     - Inventor's title.
   * - scotch noir
     - black tape
     - Out-of-game marker for sealed/anchored items (game rules).
   * - seau argenté
     - silver bucket
     - Used-items bucket.
   * - Serment de Zarathoustra / parjure
     - Oath of Zarathustra / perjury
     - Core lore.
   * - Sir Jacques Vaucanson
     - Sir Jacques Vaucanson
     - Inventor's name.
   * - soleil orné en son centre d'un tourbillon noir
     - sun with a black whirl at its centre
     - Amplificans symbol.
   * - solstice d'hiver
     - winter solstice
     - Portal opening date.
   * - sondeur
     - Sounder
     - Spy role (canonical).
   * - Sort de foudre
     - Lightning Spell
     - Invoker ritual (heading).
   * - sortilège / sort
     - spell
     - Magic.
   * - Source de Savoir
     - Fount of Knowledge
     - Link to the Djinn world.
   * - souris grises
     - grey mice
     - Dragons' bodies.
   * - Spécificités
     - Specifics
     - Faction sheet sub-heading.
   * - spectre / forme spectrale
     - spectre / spectral form
     - British spelling.
   * - Stase absolue
     - Absolute Stasis
     - Invoker ritual (heading).
   * - stéréogramme / anamorphose
     - stereogram / anamorphosis
     - Puzzle types.
   * - Stratège Défenseur
     - Defensive Strategist
     - Woodsman ability heading.
   * - strates de la réalité
     - strata of reality
     - Lore.
   * - Survol des compétences spécifiques des participants
     - Overview of participants' specific abilities
     - GM heading.
   * - symbole secret (de la famille Maupertuis)
     - secret (Maupertuis family) symbol
     - Forbidden Domain key.
   * - tableaux lenticulaires effrayants / pyramide hologramme
     - scary lenticular paintings / hologram pyramid
     - Prophecy device.
   * - tablette tactile
     - touch tablet
     - Out-of-game device.
   * - Teinture Pyrolitis
     - Pyrolitis Tincture
     - Dangerous sub-recipe.
   * - Terminal Web des indices
     - clue web terminal
     - Meta.
   * - Thanatologue (le)
     - the Thanatologue
     - Cursed grimoire.
   * - Théocratie akarite / runes akarites
     - Akarith Theocracy / Akarith runes
     - Adjective always "Akarith".
   * - thestral / wendigo / loup-garou / strige / dryade / spriggan / requins-sabres
     - thestral / wendigo / werewolf / strix / dryad / spriggan / sabre sharks
     - Woodsman bestiary.
   * - Thuriféraire (encenseur)
     - Thurifer (censer-bearer)
     - Invoker ability heading.
   * - tirelire / tirelire magique (du Voleur)
     - piggy bank / magic moneybox
     - Octave's lost savings = "piggy bank" (GM manual). The Thief's "sorte de tirelire magique" = "magic moneybox" (phantom_thief_sheet), the description of symbol ``thief_moneybox_name`` ("bottomless collection pouch"); "the moneybox" afterwards.
   * - tour de présentation
     - round of introductions
     - Pre-game ritual of the players.
   * - tout petits neveux / piti-piti-fillots
     - great-great-great-grandnephews and grandnieces
     - Ankou speech and Octave sheet; the childish "piti-piti-...fillots" keeps the same rendering.
   * - traître / méchant / Démasquer et neutraliser le méchant
     - traitor / villain / Unmask and neutralise the villain
     - Quest heading.
   * - trésor des Maupertuis
     - Maupertuis treasure
     - Spy quest.
   * - Trésor du Donjon des Pass'muraille
     - Treasure of the Pass'muraille Keep
     - Thief's hoard.
   * - triade de flammes
     - flame triad
     - Taboo emblem (Abyssal Vortex).
   * - triple longévité / bénédiction des leprechauns
     - triple longevity / blessing of the leprechauns
     - Dragons' "Reward" secret (useless well).
   * - tunique pourpre
     - purple tunic
     - Phantom costume marker.
   * - tuyaux de voleur (bons)
     - (good) thief's tips
     - Thief's paid clues heading.
   * - uchronie
     - alternate history
     - World-of-the-living description.
   * - ULTRA-LOURD
     - ULTRA-HEAVY
     - Item tag.
   * - Un réveil inattendu / L'envers du décor
     - An unexpected awakening / Behind the scenes
     - NPC sheet headings.
   * - "Unis nous resterons debout, divisés nous tomberons"
     - "United we shall stand, divided we shall fall"
     - Oracle's initial intuition (declaimed after the GM's intro speech).
   * - Valerias
     - Valerias
     - Arkon's name.
   * - Valeur des objets précieux
     - Value of precious objects
     - Heading (treasures_value_summary).
   * - Venture Prins (symbol small_wooden_fake_book_name)
     - Venture Prins
     - Fake wooden book; verbatim.
   * - verrins steamoforce / engrenages diphasiques / compresseurs néodymes / senseurs proprioceptifs
     - steamoforce jacks / diphasic gears / neodymium compressors / proprioceptive sensors
     - Minesweeper steampunk jargon.
   * - vêtement de reconnaissance
     - identifying garment
     - Faction symbol.
   * - vivants (les) / morts (les) / défunt
     - the living / the dead / the deceased
     - Lore.
   * - voleur (le)
     - the Thief
     - Phantom NPC (phantom_thief).
   * - Vortex Abyssal
     - Abyssal Vortex
     - Demonic dimension.
   * - Vos connaissances sur les différents types de blessures
     - Your knowledge of the different types of injuries
     - Recurrent heading.
   * - Vos connaissances sur les fantômes et autres esprits égarés
     - Your knowledge of phantoms and other lost spirits
     - Anthropologist sheet heading.
   * - Votre histoire / Votre profil / Votre histoire et votre mission
     - Your story / Your profile / Your story and your mission
     - Recurrent sheet headings.
   * - Votre plan de bataille / Votre préconnaissance des alliés / Votre connaissance des artefacts
     - Your battle plan / Your foreknowledge of your allies / Your knowledge of artefacts
     - Complement sheet headings.
   * - Votre sagesse draconique
     - Your draconic wisdom
     - Dragons sheet heading (the quotes section).
   * - Votre stratégie / Votre arrivée en jeu / Vos dernières bribes de pouvoir / Votre clairvoyance (sagesse) draconique
     - Your strategy / Your entry into the game / Your last scraps of power / Your draconic clairvoyance (wisdom)
     - Dragons sheet headings.
   * - votre vocation s'est rapidement imposée à vous / votre devoir s'est imposé à vous
     - your calling soon became clear to you / your duty became clear to you
     - Opener of the Diakon role sheets (Dispeller, Exorcist, Invoker) and of the Dragons sheet; never the calque "imposed itself on you".
   * - vouivre naine / queue de licorne / cristal de cardanium
     - dwarf wyvern / unicorn tail / cardanium crystal
     - Invulnerability potion ingredients.
   * - Zones de danger
     - Danger Zones
     - Minesweeper ability heading.

Mystery Party: Mindstorm (L'Affaire Loyd Georges)
=================================================

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - 11h / 12h / 12h30 / 12h45 / 17h / 18h / 22h / 22h40 (lg_meeting_time_for_*, evening_*_time, afternoon_lg_medecine_time, malachite_amethyst_encounter_time)
     - 11:00 / 12:00 / 12:30 / 12:45 / 17:00 / 18:00 / 22:00 / 22:40
     - Symbol values; 24-hour clock with colon.
   * - 145 route du Puy de la Fol, Hameau du Gisant, Alifir Sud
     - 145 Puy de la Fol Road, Hamlet of Le Gisant, South Alifir
     - Voluto's secret lab address (symbol "voluto_secret_lab_address").
   * - 15h / 16h20 / 10h45 (heures)
     - 15:00 / 16:20 / 10:45
     - Clock times on the 24-hour clock (H:MM / HH:MM, no leading zero, see Conventions), both in symbols and in prose (harmonised across player sheets).
   * - 18 mégakashes (opal_lydia_financial_needs)
     - 18 megakashes
     - Symbol value.
   * - 8e étage de l'Hotel SalimaGlobeCenter (amethyst_hostel_room)
     - 8th floor of the SalimaGlobeCenter Hotel
     - Symbol value.
   * - A la recherche de Matériaux de Construction / de Terres Rares / de Carburant
     - In search of Building Materials / Rare Earths / Fuel
     - Mission subtitles.
   * - Abonnement Rail Week-End Alifir-Faeran
     - Alifir–Faeran Weekend Rail Pass
     - Item; Alifir, Faeran verbatim.
   * - Académie de Belez
     - Belez Academy
     - Institution.
   * - Actes d'estimation / Actes d'huissier / Actes de vente
     - Appraisal deeds / Bailiff's deeds / Bills of sale
     - Tabellion abilities (headings of notary_sheet).
   * - Adjointe de police
     - Deputy police officer
     - Obsidian's cover job (Obsidian is female).
   * - aérodrome militaire géant d'Alifir
     - giant military aerodrome of Alifir
     - Place.
   * - Affaire Loyd Georges (L')
     - The Loyd Georges Affair
     - Standalone intro title; "Loyd Georges" verbatim (NOT "George").
   * - Affaire Voluto (L')
     - The Voluto Affair
     - Lore; Prof. Voluto verbatim.
   * - Agent secret / agents
     - Secret agent / agents
     - The spy players.
   * - Alphonse (le vieil Alphonse, Alph', Phonphonse)
     - Alphonse (old Alphonse, Alph', Phonphonse)
     - NPC servant; nicknames verbatim.
   * - Ambassadeur akarite
     - Akarith Ambassador
     - NPC (Archdeacon Menelas). A character title standing for the NPC: always capitalised, "the Akarith Ambassador" / "the Ambassador" (also "the Akarith Ambassador to Sabarim"), even where the FR writes "l'ambassadeur akarite" in lowercase.
   * - Amitié Numérique
     - Digital Friendship
     - Anthropia ability.
   * - An 1968 de la nouvelle ère
     - Year 1968 of the new era
     - Tabellion's birth year clue.
   * - Analphabète (caste des analphabètes)
     - Illiterate (the Illiterate caste)
     - Akarith society.
   * - Analyse biophysique (d'un objet)
     - Biophysical Analysis (of an object)
     - Anthropia ability.
   * - Analyseur Graphologico-Stylistique
     - Graphological-Stylistic Analyser
     - Specific ability.
   * - Annuaire
     - Directory
     - Anthropia contact directory.
   * - Anthropia (portail web Anthropia)
     - Anthropia (the Anthropia web portal)
     - Verbatim.
   * - antique téléphone-fax filaire (avec vidéo floue)
     - antique landline fax-phone (with blurry video)
     - Alphonse's paid service. "filaire" = "landline" (never "wireline"); the data keys ``wireline_fax`` and ``manor_has_wireline_phone_through_alphonse`` stay untouched.
   * - Apothicaire
     - Apothecary
     - Master Bibine's trade.
   * - appels du pied (de Rydji / d'Alphonse)
     - overtures (Rydji's / Alphonse's)
     - Planning label.
   * - Arbitre assermenté
     - Sworn referee
     - Duel of honour rules.
   * - Archidiacre
     - Archdeacon
     - Akarith clerical rank (Menelas, Baazel, Altos). Capitalised before a name ("Archdeacon Altos"). "l'archidiacre" without a name, standing for the calling NPC in yodic_council_interviews, is a character title: "the Archdeacon"; generic "an archdeacon" stays lowercase.
   * - Archidiacre Altos / Baazel
     - Archdeacon Altos / Baazel
     - Akarith council NPCs (phone calls).
   * - Argent standard
     - Standard cash
     - Possessions heading.
   * - Armure exosquelettique
     - Exoskeleton armour
     - Lore tech.
   * - Association de malfaiteurs
     - Criminal conspiracy
     - Judicial offence.
   * - AuBonPichet (taverne)
     - AuBonPichet (tavern)
     - Verbatim.
   * - Audition (du Grand Concile) / Auditions du Grand Concile akarite
     - Hearing (of the Great Council) / Hearings of the Akarith Great Council
     - Appointment title.
   * - Austrion
     - Austrion
     - Region (tar sands, the Duke's asylum); say "in / of Austrion" rather than an adjective.
   * - Authentification automatique
     - Automatic authentication
     - Anthropia mechanic.
   * - Authentification de document
     - Document Authentication
     - Specific ability (UV lamp).
   * - Aux Lucioles Salimiennes
     - Aux Lucioles Salimiennes
     - Café-theatre name, verbatim.
   * - Avant-enchères / après-enchères
     - Ante-auction / post-auction
     - Game mode labels.
   * - Axolie
     - Axolia
     - Region within striking range of Lordanian flying fortresses.
   * - Bague à tête de mort
     - Skull ring
     - Item.
   * - Baguette
     - Baguette
     - Currency sub-unit: 1 kash = 10 baguettes; verbatim.
   * - Bail minier / concession minière
     - Mining lease / mining concession
     - Mission mechanic.
   * - Balberith / pays de Balberith
     - Balberith / the land of Balberith
     - Blackmailing country (symbol ``waden_blackmailer_lady_country``) and home of the Kioctl Polytechnic Institute; verbatim. "le pays de Balberith" = "the land of Balberith", as "pays d'Akaris" = "the land of Akaris".
   * - Banque de Salima / Votre compte à la banque de Salima
     - Bank of Salima / Your account at the Bank of Salima
     - Institution.
   * - Baroudeur (Rodok) / vie de baroudeur
     - globetrotter (Rodok) / globetrotting life
     - Loyd Georges' adventuring friend in Mindstorm prose (opal_remedy_quest); name verbatim. "sa vie de baroudeur" (Loyd Georges, alphonse_sheet) = "his globetrotting life"; never "adventurer's life". In Descent the same FR word is the PC role "ranger" (role name).
   * - Basilique de Salima
     - Salima Basilica
     - Place.
   * - Bastet
     - Bastet
     - Loyd Georges' first pet.
   * - Bâthar
     - bathar
     - Akarith lore term for a non-Akarith (yodic_council_interviews, shark_previous_days); drop the circumflex. A common noun: lowercase, keeping the FR italics or quotes (a *bathar*, a "bathar"); capitalised only where the FR capitalises it.
   * - Bedou (berger angora)
     - Bedou (angora sheepdog)
     - Dog NPC.
   * - blanquette de veau (au laurier) / gratin de morue aux girolles
     - veal blanquette (with bay leaves) / cod gratin with chanterelles
     - The poisoned dishes.
   * - Blasphème (preuve de blasphème)
     - Blasphemy (proof of blasphemy)
     - Judicial/religious mechanic.
   * - Boîte aux lettres
     - Mailbox
     - GM meta ("LOT n à mettre dans la boîte aux lettres" = "LOT n to be placed in the mailbox").
   * - boîte postale (du hameau) / cabine télécom internationale
     - P.O. box (of the hamlet) / international telecom booth
     - Shark's dead drop.
   * - Boîte postale anonyme n°67
     - Anonymous P.O. box no. 67
     - Lore.
   * - bon cadeau pour un massage du crâne
     - gift voucher for a scalp massage
     - Hairdresser-masseur trigger.
   * - Bonbonne tectonne
     - Tectonic Canister
     - game_items.yaml item.
   * - "bouboule" (l'orbe)
     - "Roly-Poly" (the orb)
     - Waden's pet name for the orb in his Anthropia messages.
   * - bouilleurs de cru
     - home distillers
     - Tabellion's analogy for grandfathered privileges.
   * - Bourse de cuir
     - Leather Purse
     - game_items.yaml item. Capitalised in running text too ("the Leather Purse"), including the GM manual's FR typo "bourse de cuire".
   * - Bourses d'étude
     - Study grants
     - Rodimir negotiation demand.
   * - Brasserie du Purineur
     - the Purineur Brasserie
     - Place; never "Bar" (FR "bar le Purineur" too).
   * - Briefing initial / intermédiaire
     - Initial / mid-game briefing
     - Mentor phone briefings.
   * - Brigade criminologique
     - criminology squad
     - Shark's Manor search ability.
   * - Brouilleur d'ondes
     - Signal jammer
     - Item.
   * - Bulletin d'entretien-vérité
     - Truth-interview slip
     - Lie-detector paper ability.
   * - Bureau (du manoir)
     - Study
     - Manor room.
   * - Buste à 3 yeux
     - Three-eyed Bust
     - game_items.yaml item.
   * - Butin / Style / Déshonneur / Prison (enjeux)
     - Loot / Style / Dishonour / Prison (stakes)
     - Duel of honour stake types.
   * - Cab'
     - Cab
     - Lore vehicle.
   * - Cabine télécom
     - Telecom booth
     - Lore.
   * - cadre photo du chaton
     - kitten photo frame
     - Clue prop (Bastet).
   * - Café Bargarac d'Alifir
     - Café Bargarac in Alifir
     - Place; also the display value of symbol ``akarith_sect_den_bar``.
   * - caisse hors-jeu
     - out-of-game cash box
     - Tabellion deposit rule.
   * - Calepin Mémo
     - Memo Notebook
     - Item.
   * - Capitaine Rodimir / Négociation avec le Capitaine Rodimir
     - Captain Rodimir / Negotiation with Captain Rodimir
     - NPC; appointment title.
   * - Carte d'invitation magnétisée
     - Magnetised invitation card
     - Item.
   * - Carte pass dorée / carte passe / Crochetage par Carte Passe
     - Golden pass card / pass card / Pass-Card Lockpicking
     - Item; ability.
   * - cassette en plomb sous une latte de plancher (cynthia_proofs_hiding_place)
     - lead casket under a floorboard
     - Symbol value.
   * - Caution (2000 kashes)
     - Bail (2,000 kashes)
     - Judicial mechanic.
   * - cave de la maisonnette n°556, rue Latourbière, Faeran Sud
     - cellar of cottage no. 556, Latourbière Street, South Faeran
     - Waden's secret lab address (symbol "waden_secret_lab_address").
   * - Caveau familial (profanation du)
     - Family vault (desecration of the)
     - Judicial offence.
   * - Cazoar / Sablima (métropoles)
     - Cazoar / Sablima
     - Sabarith consulate metropolises; verbatim.
   * - Cazoar / Salima (métropoles)
     - Cazoar / Salima
     - Sabarith consulate metropolises.
   * - Central Téléphonique
     - Telephone Exchange
     - Anthropia feature.
   * - Ces dernières semaines / Ces derniers jours / Le jour du scrutin
     - The last few weeks / The last few days / Polling day
     - previous_days headings.
   * - Champignon aquatique bleu
     - Blue aquatic mushroom
     - Berserk ingredient.
   * - Champion (duel)
     - Champion
     - Duel of honour.
   * - chataignier / marronnier
     - sweet chestnut tree / horse chestnut
     - Treasure clue.
   * - Chenil
     - Kennel
     - Manor room.
   * - Chèvre angora d'Akarie / chèvre mohair de Kéroskia
     - Akarith angora goat / Keroskian mohair goat
     - Neighbour lore.
   * - chez lui, d'une hémorragie cérébrale consécutive à une chute
     - at home, of a cerebral haemorrhage following a fall
     - Symbol "physicist_death_circumstances".
   * - Ciboire
     - Ciborium
     - Item.
   * - Cierge d'or / Cierge Yodique
     - Golden candle / Yodic Candle
     - Items.
   * - Citations Yodiques
     - Yodic Quotes
     - Section heading.
   * - Clan (les 7 clans akarites)
     - Clan (the 7 Akarith clans)
     - Lore.
   * - Clef / code secret (coffre-fort)
     - Key / secret code (safe)
     - Safe mechanic.
   * - coalition midolienne anti-akarite
     - anti-Akarith Midolian coalition
     - Faction.
   * - Code de réinitialisation
     - reset code
     - Anthropia Purge ability.
   * - Code Pénal
     - Penal Code
     - Sabarith law.
   * - Codes de soumission
     - Submission codes
     - Press Disinformation ability.
   * - Coffre-fort
     - Safe
     - Item/location.
   * - Coiffeur-masseur
     - Hairdresser-masseur
     - NPC.
   * - Colis kéroskien
     - Keroskian parcel
     - Audio transcript lore.
   * - Collier de la reine
     - The Queen's Necklace
     - Lore item.
   * - Colonel Der'Ham, Chef des Services Secrets Doriens
     - Colonel Der'Ham, Head of the Dorian Secret Services
     - Signature of the Dorian mission.
   * - Combat (pierre-feuille-ciseaux / shi-fu-mi)
     - Combat (rock-paper-scissors)
     - Generic ability.
   * - Commissaire-priseur
     - Auctioneer
     - Tabellion role.
   * - Compétences génériques et conseils divers
     - Generic abilities and miscellaneous advice
     - Section heading.
   * - Compétences spéciales / spécifiques / Compétences Spéciales Numériques
     - Special abilities / specific abilities / Digital Special Abilities
     - Mechanic.
   * - Complot terroriste
     - Terrorist plot
     - Judicial offence.
   * - Compte Anthropia (identifiant ciblé)
     - Anthropia account (targeted username)
     - Anthropia Purge.
   * - Comte Adamor / Comte Blispin
     - Count Adamor / Count Blispin
     - NPCs.
   * - Concept de la soirée mystère / Détails des gameplays de la soirée / Les forces en présence / Le déroulement de la soirée
     - Concept of the mystery evening / Details of the evening's gameplay / The forces at play / The course of the evening
     - GM manual headings; "gameplay" is uncountable (no "gameplays").
   * - Concile akarite (Grand Concile)
     - Akarith council (great council)
     - A one-off religious council, not a standing institution: lowercase in running text ("the Akarith council", "the great council", "this council"); capitals only where the FR title capitalises (appointment title "Hearings of the Akarith Great Council").
   * - Confrérie des Obérons / obéron (nom et adj.)
     - Brotherhood of the Oberons / Oberon (noun and adj.)
     - Faction. FR: lowercase noun and adjective in running text ("les obérons", "le médiateur obéron"), capital only in the faction name "Confrérie des Obérons", in headings/titles and signatures; EN keeps "Oberon(s)" capitalised.
   * - Connaissance des Poisons
     - Knowledge of Poisons
     - Specific ability.
   * - consul / consulat
     - consul / consulate
     - Sabarith politics. Lowercase when generic ("the consuls", "a consul"); capitalised before a name ("Consul Mundlish Odalisc") and in the office title "Consul of Alifir" (see "Consulat d'Alifir"), as in the FR.
   * - Consul en exercice / favori(te)
     - incumbent consul / favourite
     - Election table.
   * - Consulat d'Alifir / consul d'Alifir / course au consulat
     - Consulate of Alifir / Consul of Alifir / race for the Consulate
     - Lydia's election.
   * - CONTRAINTE HORS-JEU
     - OUT-OF-GAME CONSTRAINT
     - GM instruction label.
   * - contrat / pacte de négociation (non-exclusif)
     - (non-exclusive) negotiation contract / commercial negotiation pact
     - Akarith Ambassador's offer to Lydia (Mission 1). "contrat de négociation" = "negotiation contract" (never "negotiating contract"); "pacte de négociation commerciale" = "commercial negotiation pact".
   * - Conversion monétaire et dépôt
     - Currency conversion and deposit
     - Section heading.
   * - Corne striée de chèvre
     - Ridged goat horn
     - Berserk ingredient.
   * - coup d'éclat divin
     - divine show of force
     - Akarith plot (spinel).
   * - Couverture
     - Cover (story)
     - Spy mechanic.
   * - Crochetage
     - Lockpicking
     - Ability.
   * - cryptorunes akarites modernes
     - modern Akarith cryptorunes
     - Cynthia hint.
   * - Cuisinier
     - Cook
     - Robb Barrow NPC.
   * - culte akarite
     - Akarith worship / the Akarith faith
     - Dorian mission. FR "culte" is neutral; never "cult" (pejorative in English).
   * - Culture Médicale
     - Medical Knowledge
     - Specific ability.
   * - Cœur de Fusion Thermocyclique
     - Thermocyclic Fusion Core
     - Lore tech.
   * - Dame Chance
     - Lady Luck
     - Idiom.
   * - Dame Clodynette
     - Lady Clodynette
     - NPC.
   * - Déchiffrement de messages codés
     - Decoding of Coded Messages
     - Opal ability.
   * - Défieur / défié
     - Challenger / challenged party
     - Duel of honour.
   * - Département de la Défense Sabarite
     - Sabarith Department of Defence
     - Institution; also symbol ``obsidian_employer_name`` (FR tag spells it "Defense").
   * - Dépêche Presse Mondiale
     - World Press Dispatch
     - Specific ability.
   * - Déroulement de l'enquête jusque-là
     - The investigation so far
     - Sheet title.
   * - Détecteur corporel
     - Body scanner
     - Item.
   * - détecteur de radiations / radioactivité / détecteur d'ondes
     - radiation detector / radioactivity detector / wave detector
     - Black-market item.
   * - Dhimmitude
     - Dhimmitude
     - Akarith status of non-believers; verbatim.
   * - Dictaphone-espion / Transcription d'enregistrement - Dictaphone espion
     - Spy dictaphone / Recording transcript - Spy dictaphone
     - Item.
   * - Digoxine / digitoxine
     - Digoxin / digitoxin
     - Cardiac toxins memo.
   * - Dilemme du prisonnier
     - Prisoner's dilemma
     - GM interrogation technique.
   * - Dirigeable
     - Airship
     - Lore vehicle.
   * - Distinction des objets RP/HRP / Apprentissage et suivi du scénario / Conseils de Jeu
     - Telling IC and OOC objects apart / Learning and following the scenario / Gameplay Advice
     - game_rules headings.
   * - Djinns de Sedes Sancta (Sollicitation des Djinns)
     - Djinns of Sedes Sancta (Consulting the Djinns)
     - Specific ability: a prepaid call putting three questions to a knowledge sect. "Sollicitation" = "Consulting", never "Summoning" (nothing is conjured).
   * - Dorien / dorienne; Duché dorien; Duc dorien; Dorie
     - Dorian; Dorian Dukedom; Dorian Duke; Doria
     - Faction.
   * - Drogue Zombifiante / zombifiant(e)
     - Zombifying Drug / zombifying
     - Lore drug.
   * - duc "grillé"
     - the Duke is "burnt"
     - Spy slang for exposed/compromised.
   * - Duc de Dorie
     - Duke of Doria
     - Title; "Duché Dorien" = "Dorian Dukedom".
   * - duchesse de Dorie / cierges d'or de la duchesse
     - Duchess of Doria / the Duchess's golden candles
     - Red Wolves theft lore.
   * - Duel d'honneur
     - Duel of honour
     - Generic mechanic (filename keeps "honor").
   * - Echelle des peines
     - Scale of penalties
     - Judicial.
   * - Eléments de droit sabarite
     - Elements of Sabarith Law
     - Document title.
   * - Elezie
     - Elezie
     - NPC blackmailer; verbatim.
   * - Élixir Berserk / Élixir militaire Berserk / Élixir salvateur Berserk
     - Berserk Elixir / Berserk Military Elixir / Berserk Life-saving Elixir
     - Mechanic/item.
   * - Elus des Yods / Fils Elu des Yods
     - Chosen of the Yods / Chosen Son of the Yods
     - Religious title.
   * - Emerald (agent lordanien)
     - Emerald
     - Dead Lordanian double agent, Garnet's former partner; code name verbatim.
   * - Emeute Akarite
     - Akarith Riot
     - Specific ability.
   * - Emilos Loakim / Pr Loakim
     - Emilos Loakim / Prof. Loakim
     - NPCs; verbatim.
   * - Enceinte externe électrifiée
     - Electrified outer fence
     - Manor lore.
   * - Enchères / ventes aux enchères / enchères montantes / descendantes
     - Auction(s) / ascending / descending auctions
     - "Les Ventes aux Enchères" = "The Auctions".
   * - Enjeu
     - Stake
     - Duel of honour.
   * - Enregistrement (transcription d')
     - Recording (transcript of)
     - Audio recordings.
   * - enregistreur audiophonique (en forme de stylo / de dictaphone)
     - audio recorder (shaped like a pen / a dictaphone)
     - Malachite's planted devices; also "spy pen" / "spy dictaphone".
   * - Entremetteur
     - Go-between
     - Oberon role.
   * - Entretien(s) / La journée des entretiens / Programme de la journée des entretiens
     - Interview(s) / The day of the interviews / Schedule of the interview day
     - Sheet title.
   * - équilibre de la terreur
     - balance of terror
     - Lydia vs. Odalisc.
   * - Ernest De Villeneuve
     - Ernest De Villeneuve
     - Prof. Loakim's deputy; verbatim.
   * - Eschatologie in-vivo / post-mortem
     - In-vivo / post-mortem eschatology
     - Akarith theology.
   * - Escouade Armée
     - Armed Squad
     - Obsidian ability.
   * - Etat des lieux
     - State of play
     - Heading inside the commented-out post-auction sections (``*.postauction.custom``); never "State of affairs". Its companion heading "Informations complémentaires - <Agent>" has its own row.
   * - Evènements et faits récents
     - Recent events and facts
     - Section heading.
   * - Expert en histoire yodique
     - expert in Yodic history
     - Malachite's cover identity.
   * - Expertise biophysique (d'un objet) / Service d'expertise biophysique
     - Biophysical appraisal (of an object) / Biophysical appraisal service
     - Auction ability (abilities.yaml matter_analysis); also for "analyse physique" when it means this ability. Distinct from the Anthropia ability "Analyse biophysique" = "Biophysical Analysis".
   * - Extrême-midolien
     - Far-Midolian
     - "fusion des peuples extrême-midoliens" = "merger of the Far-Midolian peoples".
   * - Faculté d'Imuo
     - Faculty of Imuo
     - Institution.
   * - Faits marquants des derniers jours
     - Highlights of the last few days
     - Sheet title.
   * - Fausse Preuve
     - Fake Evidence
     - Shark ability.
   * - Ferrets impériaux
     - Imperial studs
     - Lore item.
   * - Feuille antisèche
     - Cheat sheet
     - GM meta.
   * - Fiche de / du / de la … (titre de fiche PNJ)
     - Sheet of … (e.g. "Sheet of the servant Alphonse", "Sheet of the butler Rydji", "Sheet of the Tabellion of Salima", "Sheet of the Oberon Mediator", "Sheet of the Salimian Neighbour", "Sheet of the Akarith Ambassador to Sabarim")
     - NPC sheet titles.
   * - Fiche PNJ / fiche récapitulative
     - NPC sheet / summary sheet
     - GM meta.
   * - Flash-mob de fanatiques akarites
     - Flash mob of Akarith fanatics
     - Generic ability.
   * - Forteresse volante
     - Flying fortress
     - Lore vehicle.
   * - Fouille du manoir / Perquisition du manoir / Fouille du manoir #n
     - Manor search / Manor search #n
     - Mechanic.
   * - Fraude fiscale
     - Tax fraud
     - Judicial offence.
   * - Front des Affranchis
     - Freedmen's Front
     - Faction.
   * - Gala d'Ouverture
     - Opening Gala
     - Lore event.
   * - Garde armé
     - Armed guard
     - Mechanic.
   * - Garde-manger
     - Pantry
     - Manor room.
   * - Gardien des Traditions (Président)
     - Keeper of Traditions (President)
     - Sabarith political title.
   * - Gazette de Sabarim
     - Sabarim Gazette
     - Newspaper; also symbol ``cynthia_employer_name``.
   * - Gemmes
     - Gems
     - Valuables.
   * - GemmoKorps / LordaBild / GigAchat / Salimacom / PangeaTelecom / Septième Ciel
     - GemmoKorps / LordaBild / GigAchat / Salimacom / PangeaTelecom / Septième Ciel
     - Companies; verbatim.
   * - Gentil flic / méchant flic
     - Good cop / bad cop
     - GM technique.
   * - Géolocalisation des émetteurs/destinataires d'un appel ou d'un message informatique
     - Geolocation of the senders/recipients of a call or a computer message
     - Ability overview (all_specific_abilities_overview).
   * - Gestion de la soirée
     - Running the evening
     - GM heading.
   * - Gestionnaire de bien
     - estate manager
     - Lydia and Magnus's mentor.
   * - Gisement
     - Deposit
     - Mining lore.
   * - Gisement de sables bitumineux / carburant / terres rares / matériaux de construction (camps)
     - tar sands deposit / "fuel" / "rare earths" / "building materials" (sides)
     - Mining negotiation sides.
   * - Gîte Les Myrtilles
     - Les Myrtilles guesthouse
     - Place; also symbol ``garnet_rental_location``.
   * - glyphes sur le toit de la cabane de jardin
     - glyphs on the roof of the garden shed
     - Panorbium clue.
   * - Graissage de patte
     - Palm-greasing (bribe)
     - Generic ability.
   * - Grand concile / La décision du grand concile / haut-gradé du concile
     - great council / The great council's decision / high-ranking member of the council
     - Lowercase, see "Concile akarite".
   * - Grand Hall / petit hall / vestibule / réduit sous l'escalier en colimaçon
     - Great Hall / small hall / vestibule / cubbyhole under the spiral staircase
     - Manor rooms; capitalise "Great Hall" as a room name.
   * - grand hall, bureau, bibliothèque, salle à manger, cuisine (videosurveillance_cameras_locations)
     - great hall, study, library, dining room, kitchen
     - Symbol value.
   * - Grille rouillée
     - Rusty Grate
     - game_items.yaml item.
   * - grimoire mystique (Panorbium Fortuna)
     - mystical grimoire
     - GM manual heading 'The mystical grimoire "Panorbium Fortuna"'; see "Panorbium Fortuna".
   * - guérite / gendarme (salimien) de faction / poste de garde
     - sentry box / (Salimian) gendarme on duty / guard post
     - Manor gate.
   * - Hameau de Wiskons
     - Hamlet of Wiskons
     - Place.
   * - Haut Judicateur
     - High Judicator
     - Akarith rank.
   * - Haut-gradé akarite
     - high-ranking Akarith official
     - Council caller.
   * - haut-préfet salimien
     - Salimian high prefect
     - Malachite's bribery attempt.
   * - haute personnalité / hautes personnalités
     - prominent public figure / prominent public figures
     - Notary sheet ("as a prominent public figure of Sabarim"); plural in the Garnet cheat sheet and misc instructions ("prominent Lordanian public figures"). See also "personnalité (de Sabarim)".
   * - hauteurs de Kéroskia
     - Keroskia highlands
     - Origin of the Ambassador's skull ring (symbol tag text).
   * - HEURE 0:00 / DEBRIEFING
     - HOUR 0:00 / DEBRIEFING
     - Planning headings.
   * - Hommages
     - Tributes
     - End-of-game meta.
   * - homme en noir (manteau noir, chapeau haut de forme)
     - man in black (black coat, top hat)
     - Neighbour's clue.
   * - Hospice Central de Salima
     - Salima Central Hospice
     - Place.
   * - Hotel SalimaGlobeCenter
     - SalimaGlobeCenter Hotel
     - Place.
   * - Huis-clos
     - Closed-room setting
     - GM meta.
   * - Huissier
     - Bailiff
     - Tabellion role.
   * - Hydrolande (plateforme)
     - Hydroland (offshore platform)
     - Opal's autonomous offshore platform, put up for sale ("plate-forme maritime" = "offshore platform"); name anglicised, in quotes where the FR has them.
   * - Hymne sabarite (outrage à l')
     - Sabarith anthem (insult to the)
     - Judicial offence.
   * - Hypnotones
     - Hypnotones
     - Lore tech; verbatim.
   * - identité fictive / personnalité fictive / usurpation d'identité
     - fake identity / fictitious persona / identity theft
     - Spy cover vocabulary; "Identité fictive" and "usurpation d'identité" are also judicial offences (Sabarith law list).
   * - Imprimante 3D
     - 3D printer
     - Mission lore.
   * - Inculpé
     - Accused
     - Judicial.
   * - Indic'
     - Informant
     - Mission lore.
   * - infiltré(s) en Sabarim / en Thelassar (agents, fanatiques, zélotes)
     - undercover in Sabarim / in Thelassar
     - Agents, services, fanatics placed in a country ("des agents doriens infiltrés en Sabarim" = "Dorian agents undercover in Sabarim"; "the Masslavian services operating undercover in Sabarim"); never "infiltrated in". The attributive "les akarites infiltrés" = "the infiltrated Akariths"; the verb "s'infiltrer en X" = "to infiltrate X".
   * - Influence politique
     - Political influence
     - Section heading.
   * - Informations complémentaires - <Agent>
     - Additional information - <Agent>
     - Heading inside the post-auction sections.
   * - Informations diverses
     - Miscellaneous information
     - Sheet title.
   * - Informations diverses si enquête des joueurs
     - Miscellaneous information in case the players investigate
     - Shared manor-knowledge heading.
   * - Injonction de soin
     - Treatment order
     - Judicial penalty.
   * - Inspecteur Shark / Les mécaniques d'interrogatoire de l'inspecteur
     - Inspector Shark / The inspector's interrogation mechanics
     - PC.
   * - intendant de police de Salima / super-intendant de police
     - police superintendent of Salima / police superintendent
     - The same official: author of the letter answering Loyd Georges' complaint (GM manual) and the superior mentioned in the audio recordings.
   * - Interactions diverses
     - Miscellaneous interactions
     - Section heading.
   * - Interception des informations
     - Information Interception
     - Obsidian ability.
   * - Interception illicite de communications
     - Unlawful interception of communications
     - Judicial offence.
   * - Interrogatoire Booléen sous Transe
     - Boolean Interrogation under Trance
     - Specific ability.
   * - Intox Presse
     - Press Disinformation
     - Specific ability.
   * - Investigation Eclair
     - Lightning Investigation
     - Shark ability.
   * - Invités de Sir Loyd Georges (Les)
     - Sir Loyd Georges' Guests
     - Heading.
   * - Isildis
     - Isildis
     - Lydia's cousin; verbatim.
   * - jeu de dupes
     - game of deception / game of bluff
     - False friend: never "fool's game". "this game of deception" (Auction GM manual); "a game of bluff" where someone really bluffs (Mindstorm shark_misc_instructions).
   * - Jeu des bâtonnets
     - Game of sticks (Nim)
     - GM mini-game.
   * - Jeune scientiste
     - young scientist
     - Rydji/LG sofa talk (refers to Waden).
   * - Joute (annonce d'une lettre : "Je vous donne un F")
     - joust ("I give you an F")
     - Duel of honour word game; lowercase "joust" in running text ("the joust"). Example word adapted "abcès" -> "abscess". The rules check words against larousse.fr (a French dictionary): kept as is in EN; whether to cite an English dictionary is an author decision.
   * - Judicateur akarite / judicateur Praeves
     - Akarith Judicator / Judicator Praeves
     - Rank.
   * - juge d'instruction
     - examining magistrate
     - Shark's quasi-status.
   * - Juron akarite (Yod' Lash / Zort' / Sel'ha)
     - Akarith oath (Yod' Lash / Zort' / Sel'ha)
     - Verbatim.
   * - Justice de Sabarim (La)
     - Sabarim Justice
     - Document heading.
   * - Khaal (fils Magnus) / thalassothérapie du mont brumeux
     - Khaal / the thalassotherapy centre of the misty mountains
     - Magnus son's location; FR singular "mont brumeux" also = "misty mountains" (see "monts brumeux").
   * - Kioctl Institut Polytechnique
     - Kioctl Polytechnic Institute
     - Institution.
   * - Kit de piratage des cartes pass
     - pass-card hacking kit
     - Pass-Card Lockpicking.
   * - « L'âme audacieuse et secourable » (cynthia_sheet_motto)
     - "The bold and helpful soul"
     - Symbol value.
   * - L'héritage caché des Loyd
     - The hidden legacy of the Loyds
     - GM manual heading.
   * - L'histoire de l'inspecteur Shark
     - The story of Inspector Shark
     - Shark standalone heading.
   * - La compromission ou la mort / La liberté ou la mort / Le sens du devoir / La bête traquée / L'image d'un homme d'exception
     - Compromise or death / Liberty or death / A sense of duty / The hunted beast / The image of an exceptional man
     - Sheet mottos ({% symbol ... for "<x>_sheet_motto" %}) for Dorians, Masslavians, Shark, Waden, Opal.
   * - La journée de l'avant-veille
     - The day before yesterday
     - Sheet heading (opal_previous_days).
   * - « La liberté ou la mort » (masslavian_sheet_motto)
     - "Liberty or death"
     - Symbol value; Malachite/Spinel sheet motto.
   * - La Maisonnée de Sir Loyd Georges
     - Sir Loyd Georges' Household
     - Confirmed glossary entry (context_details).
   * - la Poste (moyen de contact générique)
     - the post
     - Generic means of contact, lowercase ("le téléphone ou la Poste" = "the telephone or the post", common_anthropia_account_summary_displayer). The named institutions are "Sabarim Postal Service" (Poste de Sabarim) and "Sabarith Post Office" (Poste Sabarite).
   * - « La renaissance de Sabarim » (lydia_sheet_motto)
     - "The rebirth of Sabarim"
     - Symbol value.
   * - laborantin
     - lab technician
     - Cynthia and Waden files ("laboratory assistant" is an acceptable variant).
   * - Laboratoire de biophysique de Belez
     - biophysics laboratory of Belez
     - Mummy analysis.
   * - Lampe UV
     - UV lamp
     - Item.
   * - Lanterne de pierre
     - Stone Lantern
     - game_items.yaml item.
   * - Laser Gigapulse
     - Gigapulse Laser
     - Lore tech.
   * - laurier (sauce) / blanquette de veau au laurier / laurier rose / énigme du laurier rose
     - bay leaf (bay leaves) / veal blanquette with bay leaves / oleander / the oleander riddle
     - "laurier" in the recipe = bay leaf; "laurier rose" = oleander, the poison (see "Laurier rose / oléandrine"). The confusion between the two is the plot.
   * - Laurier rose / oléandrine
     - Oleander / oleandrin
     - Cardiac toxins memo.
   * - Le Docker (de Le Docker)
     - The Docker (from The Docker)
     - NPC nickname. Keep the article capitalised as part of the nickname ("The Docker", "from The Docker"), even where the FR has a lowercase article ("le Docker").
   * - le docteur Marloff du département d'optique appliquée, le jeune physicien Waden Shaw, et le professeur Idn Gark du pôle Energies Nouvelles (voluto_suspicious_colleagues)
     - Doctor Marloff of the applied optics department, the young physicist Waden Shaw, and Professor Idn Gark of the New Energies division
     - Symbol value.
   * - Le Feu Sacré du Journalisme / L'envol politique
     - The Sacred Fire of Journalism / Taking flight in politics
     - Standalone sheet headings (Cynthia / Lydia).
   * - Le jour où tout déraille
     - The day everything goes off the rails
     - Sheet heading (opal_previous_days).
   * - Le lancement de la soirée / Exemple de speech introductif de l'inspecteur / Les mécaniques d'interrogatoire de l'inspecteur / Autres suggestions de comportement durant la soirée
     - Launching the evening / Example of the inspector's introductory speech / The inspector's interrogation mechanics / Other suggested behaviour during the evening
     - Shark GM-side headings (shark_misc_instructions).
   * - « Le salut de Sabarim » (obsidian_sheet_motto)
     - "The salvation of Sabarim"
     - Symbol value.
   * - Le secret des atomes / La trouvaille de Loyd Georges / Le chantage de Balberith / Ces derniers jours...
     - The secret of the atoms / Loyd Georges' find / The Balberith blackmail / These last few days...
     - Waden sheet headings.
   * - le sir / le sieur (Loyd Georges)
     - the gentleman
     - Author's playful idiom for Loyd Georges (and "le sieur X" for other men): always "the gentleman" ("le pauvre sir" = "the poor gentleman", "le sir de Salima" = "the gentleman of Salima"). Also for other men, ironic or pejorative ("ce triste sir" = "this sorry gentleman", e.g. Mundlish Odalisc, Malachite's official identity). Never "the sir" (not English). "Sir Loyd Georges" as a title keeps its capital.
   * - les bras croisés sur la poitrine
     - arms crossed over the chest
     - Symbol "dorian_akarith_alliance_sign".
   * - Les événements rythmant la soirée
     - The events punctuating the evening
     - Planning title.
   * - Les Ventes aux Enchères (programme) / Prix estimé du lot
     - The Auctions / Estimated lot price
     - common_auction_program.
   * - Lexique akarite
     - Akarith Lexicon
     - Document.
   * - Libre déplacement
     - Free Movement
     - Obsidian ability.
   * - Livre Sacré Yodique
     - Sacred Yodic Book
     - Auction lot F (sacred_book), the Akarith rune grimoire.
   * - Livres Sabarites
     - Sabarith Pounds
     - Currency.
   * - Lord Mac'Jolt
     - Lord Mac'Jolt
     - NPC.
   * - Lord-maire d'Ouram
     - Lord Mayor of Ouram
     - Title.
   * - Lordanie / lordanien
     - Lordania / Lordanian
     - Faction (Amethyst, Garnet); see the Shared row.
   * - Lot (Prix estimé du lot)
     - Lot (Estimated lot price)
     - Auction mechanic.
   * - Loups Rouges
     - Red Wolves
     - Faction.
   * - Loyauté de la preuve
     - Fairness of evidence
     - Sabarith law principle.
   * - Loyd Markis
     - Loyd Markis
     - Loyd Georges' father, explorer; verbatim.
   * - Luxor Excelcis
     - Luxor Excelcis
     - Place.
   * - Lydia Magnus / Khaal
     - Lydia Magnus / Khaal
     - Verbatim.
   * - Main dorée (la)
     - The Golden Hand
     - Lore.
   * - Maître Bibine / Maître Florent
     - Master Bibine / Master Florent
     - NPCs.
   * - maître-coq
     - head cook
     - Robb Barrow, as seen by Spinel.
   * - Mallette du tabellion
     - The Tabellion's briefcase
     - Item.
   * - Mandat (de négociation) sur papier / Nous, l'Etat Souverain de…
     - (Negotiating) mandate on paper / We, the Sovereign State of…
     - Mission mechanic.
   * - Manoir (de Sir Loyd Georges) / La Maisonnée de Sir Loyd Georges
     - Manor (of Sir Loyd Georges) / Sir Loyd Georges' Household
     - Setting.
   * - Marduk Pamuk / Mastden / Nimouk / Cazoar / Yumeimatchi / Balberith / Imuo
     - verbatim
     - Place and people names.
   * - Marloff (docteur) / Idn Gark (professeur) / pôle Energies Nouvelles
     - Doctor Marloff / Professor Idn Gark / New Energies division
     - Voluto's colleagues.
   * - Masslavie / masslave
     - Masslavia / Masslavian
     - Faction (Malachite, Spinel); see the Shared row.
   * - Médiateur obéron / Médiation des Obérons
     - Oberon mediator / Oberon Mediation
     - NPC + generic ability.
   * - Mémo pharmacologique des toxiques cardiaques
     - Pharmacological memo on cardiac toxins
     - Heading.
   * - Mentor / Points téléphoniques des invités avec leurs mentors
     - Mentor / Guests' phone check-ins with their mentors
     - External support NPC (lowercase "mentor" in running text); "point téléphonique" = "phone check-in". The FR heading reads "Points téléphonique".
   * - Mercenaires (Embauche de mercenaires)
     - Mercenaries (Mercenary Hiring)
     - Anthropia ability.
   * - Messagerie textuelle
     - Text messaging
     - Anthropia feature.
   * - Midolie / midolien; guerre midolienne
     - Midolia / Midolian; Midolian war
     - Country; "la guerre midolienne" (mentor briefings) = "the Midolian war", lowercase "war".
   * - Mise en examen
     - Indictment
     - Judicial.
   * - MISSION - La défense de Sabarim
     - MISSION - The defence of Sabarim
     - Obsidian mission heading.
   * - Mission / Quête / Vos quêtes
     - Mission / Quest / Your quests
     - "MISSION - …" headings stay uppercase.
   * - MISSION 1 : les gisements de sables bitumineux / MISSION 2 : les ventes aux enchères / Mission 3 : zizanie et coups de pouce / Mission 4 : une belle mort
     - MISSION 1: the tar sands deposits / MISSION 2: the auctions / Mission 3: discord and helping hands / Mission 4: a beautiful death
     - Ambassador mission headings.
   * - mission en duo
     - duo mission
     - Jinja comment in cheat sheets.
   * - Mme la Lord-maire d'Ouram
     - Her Honour the Lord Mayor of Ouram
     - The Lord Mayor is a woman.
   * - molosse / vieux chien Bedou
     - mastiff / the old dog Bedou
     - Oupaout is "the mastiff".
   * - Momie
     - Mummy
     - Mission lore.
   * - Mont Shina (sanctuaire immaculé)
     - Mount Shina (immaculate sanctuary)
     - Place.
   * - monts brumeux
     - misty mountains
     - Lowercase plural everywhere, including FR singular "mont brumeux"; "thalassothérapie des monts brumeux" = "thalassotherapy centre of the misty mountains"; same words in symbol ``khaal_isildis_location``.
   * - mot de passe (pour reconnaître un médiateur obéron)
     - password
     - Oberon first-contact rule (oberons_introduction): "utilisez notre mot de passe" = "use our password"; the password and countersign have their own row.
   * - Muguet
     - Lily of the valley
     - Cardiac toxins memo.
   * - Mundlish Odalisc / Isildis / Sylwie Lescusa / LordaBild / AIXJ726H
     - Mundlish Odalisc / Isildis / Sylwie Lescusa / LordaBild / AIXJ726H
     - Symbol values kept verbatim (Mundlish Odalisc is the incumbent Consul of Alifir, Lydia's rival); FR typo "Mundlish Odalisk" normalised to "Odalisc".
   * - mur d'enceinte / portail du parc / parc
     - perimeter wall / gate of the grounds / the grounds
     - Manor exterior.
   * - Murge de Salima (La)
     - La Murge de Salima
     - Tavern; verbatim.
   * - Nalavut / nalavutien
     - Nalavut / Nalavutian
     - Country; NOT "Navalut".
   * - navire-sondeur
     - survey ship
     - Hydroland lore.
   * - Nom de code
     - Code name
     - Spy mechanic (Amethyst, Garnet, Malachite, Spinel, Topaz, Peridot, Opal verbatim).
   * - Notaire
     - Notary
     - Tabellion role.
   * - Note Hautement Confidentielle
     - Highly Confidential Note
     - Document heading.
   * - Nouveau Départ
     - Fresh Start
     - Specific ability.
   * - Nuxia
     - Nuxia
     - City with informants; verbatim.
   * - Ombres nocturnes
     - Night Shadows
     - Lore faction.
   * - Opérations bancaires
     - Banking operations
     - Anthropia mechanic.
   * - Orbe (Orbes Divins, saint orbe, orbe sacré) / L'orbe de Loyd Georges
     - orb (Divine Orbs, sacred orb) / Loyd Georges' orb
     - Core lore. Bare "orb(s)" is lowercase everywhere in EN, headings included ("Loyd Georges' orb", "the orbs"); only "Divine Orb(s)", "Spiritual Orb" and "Alpha/Beta/Gamma Orb" are capitalised names; "saint orbe" and "orbe sacré" are both "sacred orb", lowercase (even FR "Orbe Sacré Akarite" = "Akarith sacred orb"). Never "holy orb".
   * - ordre des judicateurs (akarites)
     - Order of the (Akarith) Judicators
     - The Akarith politico-religious order as a named body (yodic_council_interviews, malachite.anteauction.standalone): capital "Order", with the article; "Akarith" only where the FR has "akarites". Plain "les judicateurs" = "the Judicators".
   * - Ordre des Tabellions
     - Order of Tabellions
     - Institution.
   * - Oreste et Pylade
     - Orestes and Pylades
     - Mythological friendship (peridot_previous_days).
   * - Origine des pierres précieuses (L')
     - The Origin of Precious Stones
     - Book title.
   * - Oupaout (molosse)
     - Oupaout (mastiff)
     - Dog NPC.
   * - Paladium
     - Paladium
     - Mysterious brotherhood that Spinel has joined (post-auction custom sheets of Malachite and Spinel); in-world name kept verbatim, with the article ("the Paladium"). Unrelated to the Archives noble metal, corrected there to "Palladium".
   * - Palsambleu / Que nenni
     - Zounds / Not a chance
     - Archaic interjections.
   * - Pangeaweb / Pangeanet / ChessCheat54
     - Pangeaweb / Pangeanet / ChessCheat54
     - Verbatim.
   * - Panorbium Fortuna
     - Panorbium Fortuna
     - Artefact (runic grimoire); verbatim.
   * - Papier détecteur de mensonge
     - Lie-detector paper
     - Specific ability.
   * - Parchemin Akarite
     - Akarith Scroll
     - game_items.yaml says "Akarite Scroll"; normalise to "Akarith".
   * - Pare-feu Médiatique
     - Media Firewall
     - Specific ability.
   * - Pas d'autres possessions
     - No other possessions
     - Possessions formula.
   * - Passage à la fouille du manoir #n
     - Moving on to manor search #n
     - Planning label.
   * - passerelle téléphonique « AlifirFront176 »
     - "AlifirFront176" telephone gateway
     - Spinel wiretap clue.
   * - Passif judiciaire (Votre)
     - Your criminal record
     - Sheet title.
   * - patriarche akarite de Ghek
     - Akarith patriarch of Ghek
     - Generic office: lowercase "the patriarch of Ghek". The FR typo "Gheck" (amethyst standalone) was fixed; "Ghek" matches the data key ``amethyst_wiretaps_ghek_patriarch``.
   * - Pénalités (judiciaires)
     - (Judicial) penalties
     - Mechanic.
   * - Perles du Droit Sabarite
     - Gems of Sabarith Law
     - Document title.
   * - Perquisition / fouille (par la police)
     - search (police)
     - "Perquisition du manoir" heading = "Manor search" (glossary).
   * - Perroquet Baveur
     - Drooling Parrot
     - Seedy tavern of the Malachite / Spinel alibi; display value of symbol ``malachite_spinel_alibi_tavern_name``, so the value carries no article ("the {% symbol %} tavern").
   * - personnalité (de Sabarim)
     - (Sabarim) public figure
     - Mining-lease mission briefings ("Une personnalité de Sabarim propose...") and planning labels ("Attack on a Salima public figure"); not "personality". "haute personnalité" has its own row.
   * - petite boite à mouchoir
     - small tissue box
     - Hiding place of the safe code (symbol tag text).
   * - Photographie
     - Photograph
     - Guest list column.
   * - piratage des communications postales
     - interception of postal communications
     - Malachite's past offence (malachite_cheat_sheet). "piratage" of mail = "interception", not "hacking"; computer or account "piratage" = "hacking" (see "Piratage informatique").
   * - Piratage informatique
     - Computer hacking
     - Judicial offence.
   * - Pistolet à 1 coup doré
     - Golden single-shot pistol
     - GM prop.
   * - PNJ-MR (ligne de planning) / PNJ Multi-Rôles (PNJ-MR)
     - [multi-role NPC] / multi-role NPCs
     - GM planning (gamemaster_planning_details): the label "[PNJ-MR]" = "[multi-role NPC]"; the two NPC actors who alternate between characters.
   * - Pôle obéron
     - Oberon hub
     - Oberon organisation.
   * - Polymonie
     - polymony
     - Akarith theology (coined term). Follows the FR case: lowercase in running text ("Regarding polymony"), capitalised only where the FR capitalises it.
   * - Portail web
     - Web portal
     - Anthropia.
   * - Poste de Sabarim
     - Sabarim Postal Service
     - Nazur mission.
   * - Poste Sabarite
     - Sabarith Post Office
     - Lost parcel.
   * - « Pour la gloire de la Lordanie... » (lordanian_sheet_motto)
     - "For the glory of Lordania..."
     - Symbol value; Amethyst/Garnet sheet motto.
   * - Précieux Chaudron (collection de pièces)
     - Precious Cauldron
     - Loyd Markis's hidden collection of ancient coins (23 megakashes), sought as a treasure; also the matching item. Capitalised name, in quotes in the GM manual.
   * - Presqu'îles de Wetfeet
     - Wetfeet Peninsulas
     - Place.
   * - Presse Hydraulique
     - Hydraulic Press
     - Lore tech.
   * - Principaux objectifs pour la soirée / Vos principaux objectifs
     - Main objectives for the evening / Your main objectives
     - Headings.
   * - Prof. Voluto / Schaladuk / Eusèbon
     - Prof. Voluto / Schaladuk / Eusebon
     - NPCs; drop accent on Eusebon.
   * - Profanateur
     - Desecrator
     - Religious offender.
   * - Professeur (Emilos) Loakim
     - Professor (Emilos) Loakim
     - Cynthia's father; verbatim.
   * - Prune rouge d'Akarie
     - Akarith red plum
     - Berserk ingredient.
   * - Purge Anthropia ("VOIDIFY")
     - Anthropia Purge ("VOIDIFY")
     - Specific ability.
   * - Purificateurs
     - Purifiers
     - Akarith assassin sect.
   * - Purificateurs akarites infiltrés / démantèlement
     - infiltrated Akarith Purifiers / dismantling
     - Sabarim sub-plot heading.
   * - Question secrète / réponse secrète
     - Secret question / secret answer
     - Mission mechanic.
   * - Rapport médical
     - Medical report
     - GM handout; planning label "rapport médical n" = "medical report n".
   * - Rapports d'espionnage héliossars
     - Heliossarian espionage reports
     - Mission lore.
   * - Rapports de vidéosurveillance du manoir / Rapports de Surveillance du Manoir
     - Manor CCTV reports / Manor Surveillance Reports
     - Anthropia ability; document title.
   * - rattachement (de la Dorie à l'Akarie)
     - annexation (of Doria to Akaris)
     - Political outcome.
   * - Récapitulatif des compétences spéciales (fiche hors-jeu)
     - Summary of special abilities (out-of-game sheet)
     - Oberon mediator reference.
   * - receleur / recel (illicite)
     - receiver of stolen goods / (illicit) receiving
     - Legal term (Auction GM manual): whoever illegally holds the items; never the bare "receiver", nor "fence" (reselling comes later).
   * - Rédac' chef
     - Editor-in-chief
     - Lore job.
   * - Redirection Téléphonique
     - Call Forwarding
     - Specific ability.
   * - Regard-Humaniste / CLIVRA
     - Regard-Humaniste / CLIVRA
     - Real-world association names; verbatim.
   * - RELANCES DE GAMEPLAYS
     - GAMEPLAY BOOSTS
     - Planning heading.
   * - Rendez-vous
     - Appointment
     - GM meta.
   * - Réquisition judiciaire
     - Judicial requisition
     - Sabarith law.
   * - réquisitionner (pour interrogatoire) / suspects réquisitionnés pour témoignages
     - to requisition (for questioning) / suspects requisitioned for testimony
     - Shark mechanic.
   * - réseau mondial
     - world network
     - Anthropia's in-world name for the net.
   * - Resorpa
     - Resorpa
     - Lore remedy; verbatim.
   * - Résumé des faits et protagonistes impliqués / Action ou Fait / Auteur(s) / Témoin(s)
     - Summary of facts and protagonists involved / Action or Fact / Author(s) / Witness(es)
     - Facts summary table.
   * - Résumés Doctrinaux
     - Doctrinal Summaries
     - Section heading.
   * - Rétrocaméra Manaïque
     - Manaic Retrocamera
     - Specific ability.
   * - Robb Barrow
     - Robb Barrow
     - NPC cook.
   * - Rodok
     - Rodok
     - LG's adventurer friend (symbol lg_adventurer_friend_name).
   * - Royaume de Suabel
     - Kingdom of Suabel
     - locations.yaml key is Kingdom_of_Suabel; use "Suabel" (the former FR spelling "Subael" was a typo).
   * - rubrique des chiens écrasés
     - miscellaneous news pages
     - Topaz standalone; the idiom, not "crushed dogs".
   * - Rue de l'Arsenic
     - Arsenic Street
     - Place.
   * - Rydji
     - Rydji
     - NPC butler.
   * - Sables bitumineux d'Austrion / bitume
     - Austrion tar sands / bitumen
     - Mission.
   * - sac en toile brune (et bleu de travail)
     - brown canvas bag (and a set of work overalls)
     - Panorbium Fortuna clue in the library.
   * - Sac militaire
     - Military duffel bag
     - Item.
   * - Saint Empire akarite
     - Holy Akarith Empire
     - Ambassador's rhetoric.
   * - Saint-des-saints
     - Holy of Holies
     - The sanctum of the Temple of Nazur (Nazur mission briefing), the same place as the Descent "Saint des Saints": capitalised as a place name. A figurative use stays lowercase (Archives GM manual "ce saint-des-saints" = "this holy of holies", said of the Forbidden Domain).
   * - Salima / salimien / Voisine Salimienne
     - Salima / Salimian / Salimian Neighbour
     - City. The former FR typo "Sablima" in sabarith_triumvirate was fixed in both FR and EN.
   * - Sas / Sas métallique / détecteur de haute technologie
     - airlock / metal airlock / high-tech detector
     - Manor entrance.
   * - Scanner corporel rayonnant
     - radiating body scanner
     - Voluto's official research.
   * - Scanner Mondial (Recherche par scanner mondial des clones d'un objet)
     - World Scanner (World-scanner search for clones of an object)
     - Anthropia ability. Capitalised in running text too ("the World Scanner", "geolocation by the World Scanner").
   * - Sceau du secret (sous le)
     - under the seal of secrecy
     - Spy officialese.
   * - Sceau infalsifiable (signature dans un cercle)
     - Tamper-proof seal (signature within a circle)
     - Mechanic.
   * - scène de bagarre dans la chambre de Loyd Georges
     - scene of a brawl in Loyd Georges' bedroom
     - Symbol "shark_vague_explanations_to_opal" (opal + shark sheets).
   * - scrutin / jour du scrutin / élections consulaires
     - vote / polling day / consular elections
     - Lydia's election.
   * - secret de l'instruction
     - investigative secrecy
     - Shark's legal pretext.
   * - Secret de Nazur (Le) / temple enfoui
     - The Secret of Nazur / buried temple
     - Mission.
   * - secrétaire en ébène
     - ebony writing desk
     - Study furniture.
   * - Sénateur
     - Senator
     - Sabarith politics.
   * - service d'espionnage (de Lordanie / de Masslavie)
     - (Lordanian / Masslavian) intelligence service
     - Spy sheets; "services secrets" = "secret services".
   * - Service express pour le duc dorien
     - Express service for the Dorian Duke
     - Appointment title.
   * - Services d'intelligence
     - Intelligence services
     - Sabarith politics.
   * - Serviteur / Données communes aux serviteurs du manoir
     - Servant / Shared data for the manor servants
     - NPC sheets.
   * - Serviteur doyen / doyen de collègue
     - Senior servant / senior colleague
     - Robb Barrow, Alphonse.
   * - Signe des Yods (bras croisés sur la poitrine)
     - Sign of the Yods (arms crossed over the chest)
     - Religious gesture.
   * - Sir Loyd Georges
     - Sir Loyd Georges
     - Host NPC; verbatim incl. final "s".
   * - Soirée / soirée spéciale / La journée de la soirée spéciale
     - Evening / special evening / The day of the special evening
     - Setting.
   * - soirée d'ambassade
     - embassy evening
     - The auction evening seen as a diplomatic event (amethyst_specific_abilities, weapons rule).
   * - Soleil des atomes / supernova atomique
     - Sun of Atoms / atomic supernova
     - Lore weapon; "Sun of Atoms" always capitalised (named device).
   * - sonnette d'appel des domestiques
     - servants' call bell
     - Garnet's evening intrusion.
   * - Soulèvement populaire
     - popular uprising
     - Rodimir appointment.
   * - soupirail
     - basement window
     - Peridot files.
   * - Soutiens extérieurs
     - supporters outside (the manor / the evening)
     - Mentors rule (game_rules, cheat-sheet footer): "superiors, mentors, family, friends...".
   * - SPOTS RADIO / MAILS
     - RADIO SPOTS / EMAILS
     - GM planning labels.
   * - Square Fleuri de Salima
     - Salima Flower Square
     - Place; also symbol ``malachite_alibi_location``.
   * - statuette kéroskienne à trois yeux
     - three-eyed Keroskian statuette
     - Cynthia's investigation (cf. Three-eyed Bust).
   * - statut avili
     - debased status
     - Transfiliation doctrine outcome.
   * - studio numéro 827 aux presqu'îles de Wetfeet (lieu-dit près d'Alifir) (cynthia_sabarim_home_address)
     - studio flat number 827 in the Wetfeet Peninsulas (a locality near Alifir)
     - Symbol value.
   * - Stylo-espion Chromia
     - Chromia spy pen
     - Item.
   * - Suggestion Mémorielle
     - Memory Suggestion
     - Specific ability.
   * - Sur le premier animal de Loyd Georges / Sur la date de naissance du Tabellion / Sur l'héritage caché de la famille Loyd / Sur l'affaire Loyd Georges / Sur les élections consulaires en cours / Sur les tripots clandestins de Salima / Sur votre élevage / Sur le mystérieux homme en noir
     - About Loyd Georges' first pet / About the Tabellion's date of birth / About the hidden legacy of the Loyd family / About the Loyd Georges affair / About the ongoing consular elections / About the illegal gambling dens of Salima / About your farm / About the mysterious man in black
     - "Sur …" NPC headings rendered as "About …".
   * - surcompression atomique / compresseur atomique
     - atomic overcompression / atomic compressor
     - Voluto's experiment (waden).
   * - Tabellion (Tabellion de Salima; Maestre Ramye Leydelass)
     - Tabellion (Tabellion of Salima; Maestre Ramye Leydelass)
     - NPC title verbatim: "the Tabellion" (capital T) whenever it designates the NPC; lowercase "tabellion(s)" only for the profession in general ("the privileges of tabellions"). Gloss "notary" on first use.
   * - tableaux des 4 saisons d'Arcimboldo / buste automnal
     - Arcimboldo's Four Seasons paintings / autumnal bust
     - Treasure clue.
   * - tatouage du "sapin rouge"
     - "red fir tree" tattoo
     - Red Wolves gang sign (opal/spinel).
   * - Télégraphe / pigeons voyageurs / coursiers
     - telegraph / carrier pigeons / couriers
     - Alternative communication means.
   * - Téléphone Basse-Fréquence
     - Low-Frequency Telephone
     - Specific ability.
   * - Téléphone-fax Filaire Sécurisé
     - Secure Landline Fax-Phone
     - Specific ability (macro ``wireline_fax``, name unchanged).
   * - Teneur (d'un interrogatoire)
     - Gist
     - Planning label for Shark's interrogation content.
   * - Tentacule de poulpe caverneux
     - Cave octopus tentacle
     - Berserk ingredient.
   * - terminal numérique
     - digital terminal
     - Manor web terminal.
   * - Terres rares
     - Rare earths
     - Mission resource.
   * - thalassothérapie dans les monts brumeux (près de la frontière Est de Sabarim) (khaal_isildis_location)
     - thalassotherapy stay in the misty mountains (near the eastern border of Sabarim)
     - Symbol value.
   * - Théologie Yodique
     - Yodic Theology
     - Section heading.
   * - tiers de confiance (devant Tiers de Confiance) / Tiers de confiance mondial / contrat parfait
     - escrow agent (before an escrow agent) / World escrow agent / perfect contract
     - Generic ability (players_generic_abilities, cheat-sheet footer, Obsidian and Rydji sheets). Lowercase "escrow agent" in running text, even where the FR capitalises "Tiers de Confiance"; "World escrow agent" is the sentence-case ability heading.
   * - Tisane / thé (signal de fin)
     - Herbal tea / tea (end signal)
     - GM meta.
   * - Traducteur de Runes Yodique / Traduction de runes akarites
     - Yodic Rune Translator / Akarith rune translation
     - Ability.
   * - Trésors Perdus de Midolie
     - Lost Treasures of Midolia
     - Auction: name of Loyd Georges' auctions and of their website; never "Oubliés"/"Forgotten".
   * - Traître atomique (Le)
     - The Atomic Traitor
     - Mission title.
   * - Transfiliation (dorienne)
     - (Dorian) transfiliation
     - Coined lore doctrine; verbatim. Follows the FR case: lowercase in running text and headings ("the doctrine of transfiliation", "MISSION - The Dorian transfiliation"), quotes kept where the FR has them; "transfilier" = "to transfiliate", "un transfilié en devenir" = "a transfiliate in the making".
   * - transfilié / transfilier
     - transfiliate (noun) / to transfiliate
     - Derivatives of "Transfiliation".
   * - tripot (clandestin) / tripot louche
     - (illegal) gambling den / shady den
     - Salima slums.
   * - Triumvirat de Consuls
     - Triumvirate of Consuls
     - Sabarith politics.
   * - Tubes Pneumatiques
     - Pneumatic Tubes
     - Specific ability / lore tech.
   * - Tunguska (cataclysme de)
     - Tunguska (cataclysm)
     - World history.
   * - Univers du Jeu (document)
     - Game Universe (document)
     - Rules.
   * - Université d'Omrh
     - University of Omrh
     - Institution.
   * - université de Cazoar / Georg Vidlaock / Vassil Becck
     - University of Cazoar / Georg Vidlaock / Vassil Becck
     - Malachite's alibi historians; verbatim.
   * - Uranium 234
     - Uranium-234
     - Lore.
   * - uriner sur un crossentar, le symbole sacré yodique (dorian_duke_profanation_act)
     - urinating on a crossentar, the sacred Yodic symbol
     - Symbol value.
   * - Vaches bouclées salimiennes
     - Salimian curly cattle
     - Neighbour lore.
   * - vasistas (du garde-manger)
     - (pantry) transom window
     - Pantry escape route.
   * - Venin de Najah royal
     - Royal Najah venom
     - Berserk ingredient.
   * - Vente Spéciale Privée / Les ventes privées / Ventes Privées d'Alphonse
     - Special Private Sale / Private sales / Alphonse's Private Sales
     - Heading. BEWARE: the Jinja literal ``"Ventes Privées d'Alphonse"`` in alphonse_special_sales.rst is a data key and must stay in French.
   * - Venture Prins (livre factice)
     - "Venture Prins" (fake book)
     - Verbatim in-game title.
   * - vidéographie
     - videograph
     - Pangea recording medium (Cynthia standalone).
   * - Vieille Voisine / vieille dame de Salima / doyenne du hameau
     - Old Neighbour / old lady of Salima / the hamlet's eldest resident
     - Multi-role NPC (old_neighbour_sheet). Capitalised only as an NPC label ("the NPCs Rydji, Alphonse and Old Neighbour", "[multi-role NPC]: Cook & Old lady of Salima"); lowercase in running text ("the old neighbour"). See also "Salima / salimien / Voisine Salimienne".
   * - Vigiles
     - security guards
     - Manor checkpoint.
   * - Vik Leydelass / Jiun Kaz'er / Ouidan Jelen / Marrow Dendeliev
     - Vik Leydelass / Jiun Kaz'er / Ouidan Jelen / Marrow Dendeliev
     - Consular candidates (Vik Leydelass and Ouidan Jelen become the new consuls); verbatim. Same for "Ginate Longchan"; for Baazel / Altos see "Archidiacre Altos / Baazel".
   * - Visa planétaire
     - Planetary visa
     - Lore.
   * - Vos compétences spécifiques
     - Your specific abilities
     - Sheet title.
   * - Vos identifiants web sur Anthropia
     - Your Anthropia web credentials
     - Heading.
   * - Vos Missions / Les délits que vous avez identifiés
     - Your Missions / The offences you have identified
     - Shark headings.
   * - Vos objectifs pour la soirée
     - Your objectives for the evening
     - Cynthia missions heading.
   * - Vos possessions / Vous portez sur vous :
     - Your possessions / You are carrying:
     - Sheet titles.
   * - Votre histoire / Votre parcours
     - Your story / Your background
     - Sheet titles.
   * - Votre intervention
     - Your intervention
     - Sheet title.
   * - Votre très particulière "façon d'être"
     - Your very peculiar "way of being"
     - Alphonse sheet heading.
   * - Vous avez pour l'instant accès, sur le portail web Anthropia, aux compétences spéciales suivantes :
     - On the Anthropia web portal, you currently have access to the following special abilities:
     - Sheet title.
   * - "Vous avez un fort joli nez" / "Vos sourcils le sont tout autant"
     - "You have a mighty pretty nose" / "Your eyebrows are just as pretty"
     - Oberon password and countersign.
   * - Xylitol
     - Xylitol
     - Lore substance.
   * - Zélotes akarites
     - Akarith zealots
     - Flash mob ability.

Mystery Party: Cromlech (Le Dernier Voeu des Druides) and common files
======================================================================

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - ablutions rituelles
     - ritual ablutions
     - Monthly rite the Curator performs on the artefacts.
   * - Accueil par l'inspecteur de police
     - Welcome by the Police Inspector
     - Game-flow heading.
   * - affaire (l')
     - the case
     - Police vocabulary; "témoins de l'affaire" = "witnesses in the case".
   * - agence de détectives (spécialisée dans le surnaturel)
     - detective agency (specialised in the supernatural)
     - Players' employer; "détectives privés" = "private detectives".
   * - agent d'accueil
     - receptionist
     - Guide's official occupation on the ID sheet.
   * - aiguille de la bobine Tesla / smartphone dans la porte
     - needle of the Tesla coil / smartphone in the door
     - Final-scene logistics.
   * - Alésia
     - Alesia
     - Anglicised, no accent.
   * - Andrea di Revel (Andréa)
     - Andrea di Revel
     - Proper noun; harmonise to "Andrea"; the Hero.
   * - Année de naissance
     - Year of birth
     - ID sheet field.
   * - « année de naissance renversée »
     - "birth year reversed"
     - Clue text; 1862 reversed gives chest code 2681.
   * - Archives secrètes des Maupertuis
     - the Secret Archives of the Maupertuis
     - Title of the Archives game, cited in the common rules.
   * - armement
     - weaponry
     - Generic term for the Roman arms.
   * - Armorique / armoricain
     - Armorica / Armorican
     - "Bretagne" = "Brittany", "breton" = "Breton".
   * - armure, casque et bouclier romains
     - Roman armour, helmet and shield
     - Canonical item name.
   * - artefacts antiques
     - ancient artefacts
     - British spelling "artefact".
   * - Artefacts cachés
     - Hidden Artefacts
     - Treasure document heading; Title Case like its siblings (Legionary's Equipment, Wooden Chest).
   * - article de journal
     - newspaper article
     - Handout given at game start.
   * - autel en pierre noire
     - black stone altar
     - Part of the cromlech model.
   * - av. J.-C.
     - BC
     - Dates; "52 av. J.-C" = "52 BC".
   * - Avis du public
     - Public reviews
     - Newspaper article heading.
   * - bandage sanglant au poignet
     - bloody wrist bandage
     - Canonical item name (for the Curator).
   * - bande son finale
     - final soundtrack
     - Final scene mechanic.
   * - barillet
     - cylinder
     - Revolver part.
   * - Bertrand du Guesclin
     - Bertrand du Guesclin
     - Historical; "chevalier breton" = "Breton knight".
   * - bête vengeresse
     - avenging beast
     - Andrea's coded message.
   * - bibliothèque-musée / musée-bibliothèque
     - library-museum
     - Harmonise both French forms.
   * - bobine Tesla
     - Tesla coil
     - Prop in the cromlech model.
   * - Bon amusement à tous !
     - Have fun, everyone!
     - Common rules closing line.
   * - bouc émissaire
     - scapegoat
     - Curator's fallback plan.
   * - Bourgmestre
     - Burgomaster
     - Period-flavoured title for the mayor.
   * - [BR] / [PAGEBREAK]
     - [BR] / [PAGEBREAK]
     - Layout markers, untouched.
   * - branche de houx
     - holly branch
     - Liturgical item.
   * - brassards pour les psykers
     - armbands for the psykers
     - Inventory item.
   * - Briefing des FIGURANTS
     - NPC ACTORS' Briefing
     - Game-flow heading.
   * - Briefing des JOUEURS hors-jeu
     - Out-of-game PLAYERS' Briefing
     - Game-flow heading.
   * - cabinet de curiosités
     - cabinet of curiosities
     - Newspaper article.
   * - cadenas (à 4 chiffres)
     - (4-digit) padlock
     - "pinces cassées" = "broken bolt cutters".
   * - Cadurques
     - Cadurci
     - Gaulish tribe; Latin plural.
   * - Caius Caninius Rebilus
     - Gaius Caninius Rebilus
     - Roman legate; standard English spelling.
   * - Camille du Guesclin
     - Camille du Guesclin
     - The Curator; gender-neutral first name.
   * - carrière d'avocat / reprendre sa carrière d'avocat
     - career as a lawyer / resume one's legal career
     - Curator's backstory, recurrent across sheets.
   * - cauchemars / sommeil agité / mauvaises ondes
     - nightmares / restless sleep / bad vibes
     - Omens among the Cromlech regulars.
   * - Ce que dit l'Histoire / Ce que dit la Légende
     - What History says / What Legend says
     - Siege document headings.
   * - Ce que vous savez sur le Conservateur / le Guide / le Reporter
     - What you know about the Curator / the Guide / the Reporter
     - Recurrent character-sheet headings.
   * - cercle de pierres
     - stone circle
     - Part of the cromlech model.
   * - cérémonie de remise des prix littéraires (concours Maurice Genevoix)
     - literary prize-giving ceremony (the Maurice Genevoix prize)
     - Curator's alibi.
   * - Checklist des Objets du Jeu
     - Game Props Checklist
     - Common file title.
   * - Checklist des objets par rangement d'appartenance
     - Props checklist by storage crate
     - Common crates-listing comment.
   * - chevalière
     - signet ring
     - Canonical item name (for the Guide).
   * - Chrysalis Forge
     - Chrysalis Forge
     - Association name, verbatim.
   * - clef / double des clefs / cordonnier
     - key / spare key / cobbler
     - Use "key" consistently.
   * - code du coffre / code du cryptex
     - chest code / cryptex code
     - Values "2681" and "secret" kept.
   * - coffre en bois avec cadenas à 4 chiffres
     - wooden chest with 4-digit padlock
     - Canonical item name.
   * - coffret (de bois) / coffrets imbriqués
     - (small) wooden chest / nested chests
     - Harmonise coffre/coffret to "chest".
   * - Coffret de bois
     - Wooden Chest
     - Treasure document heading (Title Case like its siblings); "chest" in prose, see "coffret (de bois) / coffrets imbriqués".
   * - Complément d'enquête #1 / #2 / #3
     - Investigation Update #1 / #2 / #3
     - Police report headings.
   * - Conciliabules finaux
     - Final Huddles
     - Game-flow heading.
   * - concours romanesque / lauréate / gerbe de fleurs
     - novel competition / winner / bouquet of flowers
     - Police report, ceremony scandal.
   * - connétable de France
     - Constable of France
     - Historical title.
   * - Conservateur (du musée / du Cromlech) / Gérant
     - Curator (of the museum / of the Cromlech) / Manager
     - Character; capital C as nickname.
   * - contact physique / baisemain
     - physical contact / hand-kiss
     - Safety rules.
   * - costume du spectre de druide
     - Druid's Spectre costume
     - Inventory item.
   * - coupe en argile pour ablutions rituelles
     - clay cup for ritual ablutions
     - Liturgical item.
   * - crâne électronique et/ou normal (pour le casque romain)
     - electronic and/or plain skull (for the Roman helmet)
     - Canonical item name.
   * - crépiter
     - to crackle
     - The model crackles during the final scene.
   * - Cromlech (le)
     - the Cromlech
     - Name of the library-museum; lowercase "cromlech" for the stone circle itself.
   * - Cromlech miniature / maquette de Cromlech
     - miniature cromlech / cromlech model
     - See "Cromlech model and magic portal".
   * - cryptex (contenant le parchemin médiéval) / mot de passe
     - cryptex (containing the medieval parchment) / password
     - Canonical item name.
   * - Datation approximative : il y a 150 ans
     - Approximate dating: 150 years ago
     - Treasure document.
   * - Debriefing
     - Debriefing
     - Game-flow heading.
   * - Découvrez le Cromlech de Lyon / le Cromlech de Lyon
     - Discover the Cromlech of Lyon / the Cromlech of Lyon
     - Newspaper article heading; "Cromlech lyonnais" also maps to "the Cromlech of Lyon".
   * - dénouement
     - ending
     - Final scene.
   * - « Dernier Voeu des Druides » (Le)
     - "The Druids' Last Wish"
     - Game title and legend name.
   * - Dernière bataille des Gaulois
     - The Gauls' Last Battle
     - Document title.
   * - Déroulement du jeu - FICHE MJ
     - Game Flow - GM SHEET
     - Sheet title.
   * - Description du trésor du musée
     - Description of the Museum Treasure
     - GM manual heading. In prose "le trésor du musée" stays lowercase ("the museum's treasure", "around the treasure"); only the rotation station is "the Treasure" / "the Museum Treasure".
   * - Descriptions des figurants
     - NPC Actor Descriptions
     - GM manual heading.
   * - Détectives du paranormal
     - Paranormal Detectives
     - Player sheet title; "joueurs-détectives" = "detective-players".
   * - Dies Irae
     - Dies Irae
     - Tesla coil tune, verbatim.
   * - dieu tutélaire / dieu-guerrier sanguinaire
     - tutelary god / bloodthirsty warrior god
     - Toutatis epithets.
   * - Disparu / disparition
     - Missing person / disappearance
     - ID sheet heading.
   * - divinités gauloises bénéfiques
     - benevolent Gaulish deities
     - Symbols on the stone circle.
   * - domaine inter-monde / monde parallèle / réalité parallèle
     - in-between realm / parallel world / parallel reality
     - Where the entity gestates.
   * - Drappès
     - Drappes
     - Gaulish chief, anglicised.
   * - druide / Druide
     - druid / the Druid
     - Capitalised when used as the character's name.
   * - Écho des Gones (L') - Numéro 165
     - L'Écho des Gones - Issue 165
     - Newspaper title verbatim.
   * - éclairs (phénomènes)
     - lightning flashes
     - Supernatural manifestation.
   * - Eden Schmitt
     - Eden Schmitt
     - The Guide; gender-neutral.
   * - effraction (aucune trace d')
     - (no sign of) forced entry
     - Police report.
   * - Eloi de Frontignan / Lilie Dupain / Gustave Bloch / Flavien
     - Eloi de Frontignan / Lilie Dupain / Gustave Bloch / Flavien
     - Minor names kept verbatim.
   * - Émile Loubet
     - Émile Loubet
     - French President in 1900.
   * - empreintes digitales
     - fingerprints
     - Police report.
   * - encensoir
     - censer
     - Liturgical item.
   * - enquête / mener l'enquête
     - investigation / to investigate
     - Core mechanic.
   * - entité divine (en gestation) / guerrier divin
     - (gestating) divine entity / divine warrior
     - Lore.
   * - entretien (simultané)
     - (simultaneous) interview
     - "Premier entretien simultané" = "First Simultaneous Interview".
   * - enveloppe non timbrée
     - unstamped envelope
     - Clue found by the Guide.
   * - Epasnactos
     - Epasnactus
     - Gaulish aristocrat, Latinised.
   * - Équipement de légionnaire / décurion / marques d'affrontement
     - Legionary's Equipment / decurion / battle marks
     - Treasure document.
   * - étiquettes d'indices
     - clue labels
     - Supernatural manifestation.
   * - étudiant reporter
     - student reporter
     - Character; sheet title "REPORTER".
   * - expert en archéologie
     - archaeology expert
     - Optional NPC.
   * - FAIRE DES PHOTOS
     - TAKE PHOTOS
     - GM reminder label.
   * - faussaire / indic
     - forger / informant
     - Analysed the gladius.
   * - fauteuil déplacé / poussé sur la tache
     - chair that had been moved / pushed over the stain
     - Key clue in several sheets.
   * - faux CV / faux diplômes
     - fake CV / forged diplomas
     - Guide's secret.
   * - fiche de personnage / FICHE MJ / FICHE PNJ
     - character sheet / GM SHEET / NPC SHEET
     - Meta vocabulary.
   * - Fiches d'Identité des Personnes Impliquées
     - Identity Sheets of Persons Involved
     - Police document title.
   * - figurant(e) / figurante d'ambiance
     - NPC actor / ambience extra
     - LARP meta: the human playing a non-player character.
   * - flaque / tache de sang (séché) / tache d'encre
     - pool / stain of (dried) blood / ink stain
     - Clues.
   * - flopée d'enquêteurs privés
     - flock of private investigators
     - Recurrent phrase (Curator, Guide sheets).
   * - Fonctionnement du jeu
     - How the Game Works
     - Heading.
   * - forces de l'ordre / forces de police
     - law enforcement / police forces
     - Police vocabulary.
   * - fourreau
     - scabbard
     - "le glaive n'est plus dans son fourreau" = "the gladius is no longer in its scabbard".
   * - gant noir
     - black glove
     - Hides the Curator's bandage.
   * - Gaulois / gaulois / gallo-romain / celte
     - Gauls / Gaulish / Gallo-Roman / Celtic
     - Noun / adjective.
   * - gendarmes / maréchaussée
     - gendarmes / the constabulary
     - Period flavour.
   * - glaive (antique / romain / gaulois)
     - (ancient / Roman / Gaulish) gladius
     - NOT "glaive" (a polearm in English).
   * - GONG de fin d'interrogatoire
     - end-of-interview GONG
     - Game mechanic.
   * - Gramophone Lettré (Le)
     - Le Gramophone Lettré
     - Newspaper name, verbatim.
   * - grand-maître du conservatoire / autrice dramatique Jeanne Lubeck
     - grand master of the conservatoire / the playwright Jeanne Lubeck
     - Curator's alibi guests; names verbatim.
   * - GREFFE / greffier.ère
     - CLERK'S OFFICE / clerk
     - Player role (note-taker); ALL-CAPS skill term like PSYCHISM and INTIMIDATION; never "CLERKING".
   * - grimoire (factice / scellé à couverture de bois / Celte)
     - grimoire (fake / sealed with wooden cover / Celtic)
     - Canonical item: "sealed grimoire with wooden cover".
   * - Grimoire Celte
     - Celtic Grimoire
     - Capitalised as the Curator names it.
   * - groupe sanguin
     - blood type
     - ID sheet field.
   * - groupes de joueurs (par affinité)
     - player groups (by affinity)
     - Game mechanic.
   * - guerre de Cent Ans
     - Hundred Years' War
     - Historical.
   * - Guide (du musée) / guide-bibliothécaire
     - (Museum) Guide / guide-librarian
     - Character; sheet title "MUSEUM GUIDE".
   * - habitués (du Cromlech)
     - regulars (of the Cromlech)
     - Patrons.
   * - Héros (le)
     - the Hero
     - Andrea; capital H as role name.
   * - Histoire complète (SPOILERS)
     - Full Story (SPOILERS)
     - GM manual heading.
   * - indice / indices-clés / piste
     - clue / key clues / lead
     - Core mechanic.
   * - informations policières
     - police information
     - Handouts between interviews.
   * - inspecteur.trice de police
     - Police Inspector
     - NPC supervising the game.
   * - Instructions pour tous les figurants
     - Instructions for all NPC actors
     - Shared include heading.
   * - INTERLUDE : Leçon d'Histoire du professeur Gustave Bloch
     - INTERLUDE: Professor Gustave Bloch's History Lesson
     - Heading.
   * - interrogatoire / rotation des interrogatoires / ordre de rotation
     - interrogation / interrogation rotation / rotation order
     - Mechanic.
   * - Intervention du druide / Intervention de l'inspecteur de police (à la moitié de l'entretien)
     - Druid's intervention / Police Inspector's intervention (halfway through the interview)
     - Game-flow sub-headings.
   * - INTIMIDATION / intimidateur.trice
     - INTIMIDATION / intimidator
     - Player role (one closed question per interview).
   * - invocation / maléfices / envoûtement / sortilège
     - invocation / dark sorcery / enchantment / spell
     - Lore.
   * - jeter un sort / imposer les mains
     - to cast a spell / to lay hands
     - Druid actions.
   * - jeu théâtral / jeu d'acteur
     - theatrical play / acting
     - Common rules.
   * - jeu-mystère / soirée mystère
     - mystery game / mystery evening
     - game_subtitle = "A 2-hour mystery game for all audiences".
   * - jour J (le) / Le jour du drame
     - the day of the crime / The Day of the Tragedy
     - Recurrent sheet heading.
   * - Jules César
     - Julius Caesar
     - Historical.
   * - la Faculté
     - the Faculty
     - Reporter's ID sheet.
   * - langage codé / message codé
     - simple code / coded message
     - Hero-Reporter communication.
   * - langue celte / langue incompréhensible / (en français) / en français approximatif / haranguer
     - Celtic tongue / unintelligible tongue / (in the players' (own) language) / in broken English / to harangue
     - Druid's speech. "(en français)" is a stage direction for the language the psykers understand: in EN, the language of the session (druid_spectre, game_flow).
   * - Le Trésor du Cromlech - FICHE PNJ
     - The Cromlech Treasure - NPC SHEET
     - Treasure document title.
   * - légat / légion
     - legate / legion
     - Siege document.
   * - lettre d'adieux (factice) / écrite de la main gauche
     - (fake) farewell letter / written with the left hand
     - Keep the euphemism, not "suicide note".
   * - lettre médiévale expliquant les runes du cromlech
     - medieval letter explaining the cromlech runes
     - Canonical item name.
   * - limbes
     - limbo
     - Druid's spiritual retreat.
   * - livre d'or
     - guest book
     - Debriefing reminder. Two words, as in the Archives table.
   * - LOGISTIQUE
     - LOGISTICS
     - Game-flow label.
   * - Lucterios
     - Lucterius
     - Gaulish chief, Latinised.
   * - M./Mme (devant un prénom épicène)
     - Mr/Mrs
     - Character sheet openers (Camille, Eden).
   * - main gauche (blessé à la) / gaucher
     - (wounded on the) left hand / left-handed
     - Key fact.
   * - maquette de Cromlech et de portail magique / maquette antique, fragile
     - Cromlech model and magic portal / fragile ancient model
     - Canonical item name.
   * - maquillages rapides
     - quick make-up
     - Final huddles.
   * - matériel liturgique
     - liturgical paraphernalia
     - Curator's office.
   * - menhir
     - menhir
     - Kept.
   * - mis en difficulté / décontenancé / coincé
     - put on the spot / thrown off balance / cornered
     - Interview behaviour vocabulary.
   * - monde des vivants
     - world of the living
     - Ending.
   * - Monstre (naissant)
     - (nascent) Monster
     - Capitalised as role name.
   * - Mythe de Cthulhu
     - Cthulhu Mythos
     - Standard English form.
   * - nappes et lanternes pour l'ambiance
     - tablecloths and lanterns for ambience
     - Inventory item.
   * - Nationalité / Adresse / Profession / Particularités
     - Nationality / Address / Occupation / Distinguishing features
     - ID sheet fields; street addresses kept verbatim.
   * - Note : 5/5
     - Rating: 5/5
     - Review headings.
   * - Note Finale
     - Final Note
     - Common rules heading.
   * - objets non cruciaux (pour le scénario)
     - non-crucial props (for the scenario)
     - "objet" = "prop" in prose, "item" in generated summaries.
   * - Objets Trouvés
     - Lost and Found
     - Where the Guide put the envelope.
   * - oeuf mystique
     - mystic egg
     - Lore.
   * - Olloudios / messager des dieux celtes
     - Olloudios / messenger of the Celtic gods
     - Druid's name, verbatim.
   * - oppidum / place forte
     - oppidum / stronghold
     - Siege document.
   * - panthéon celtique
     - Celtic pantheon
     - Lore.
   * - papier avec les symboles de la mythologie gauloise
     - paper with the symbols of Gaulish mythology
     - Canonical item name.
   * - papiers et stylos pour les greffiers
     - paper and pens for the clerks
     - Inventory item.
   * - « Par la Force de Toutatis » / « Par la Gloire de Jupiter »
     - "By the Might of Toutatis" / "By the Glory of Jupiter"
     - Final scene slogans.
   * - parchemin (médiéval / supplémentaire) / rouleaux de papyrus
     - (medieval / extra) parchment / papyrus scrolls
     - Items.
   * - Philippe du Guesclin / manoir / caves
     - Philippe du Guesclin / manor / cellars
     - Curator's father.
   * - phosphorescence
     - phosphorescence
     - Supernatural manifestation.
   * - pièces de musée / répliques fidèles
     - museum pieces / faithful replicas
     - Lore.
   * - pistolet / revolver
     - revolver
     - Harmonise to "revolver" (the source mentions a cylinder).
   * - portail magique / porte en bois / vidéo de Vortex
     - magic portal / wooden door / vortex video
     - Part of the cromlech model.
   * - possession démoniaque
     - demonic possession
     - Psykers' final state.
   * - potion de guérison (utilisée) / potion de régénération
     - (used) healing potion / regeneration potion
     - Canonical item: "used healing potion".
   * - Préambule
     - Preamble
     - Common rules heading.
   * - Premier / Deuxième / Troisième / Quatrième entretien simultané
     - First / Second / Third / Fourth Simultaneous Interview
     - Game-flow headings.
   * - Premier / Deuxième complément d'enquête ; Troisième et dernier complément d'enquête
     - First / Second Investigation Update; Third and Final Investigation Update
     - Game-flow headings (the police document uses "Investigation Update #n").
   * - présentoir en verre
     - glass display case
     - Guide's rejected idea.
   * - professeur Gustave Bloch
     - Professor Gustave Bloch
     - Interlude NPC.
   * - PSYKISME / psyker / dons de spiritisme
     - PSYCHISM / psyker / spiritualist gifts
     - Player role; "psyker" kept.
   * - Quercy
     - Quercy
     - Region, verbatim.
   * - rangement (d'appartenance) / caisse / BOX
     - storage crate / crate / BOX
     - Common crates listing. The "@CODES" crate identifiers (e.g. "@EXTERNE-SACS-GEANTS") stay verbatim in EN: build_archives_pdfs.py parses them, and they match the French labels of the real crates.
   * - rapport d'analyse (du glaive)
     - analysis report (of the gladius)
     - Investigation update.
   * - Rapport d'enquête initial
     - Initial Investigation Report
     - Police document heading.
   * - Règles de Jeu et Conseils - Important
     - Game Rules and Advice - Important
     - Common rules title.
   * - Règles de sécurité / Sécurité physique et émotionnelle / Respect du matériel
     - Safety Rules / Physical and emotional safety / Care of props
     - Recurrent headings.
   * - reliques sacrées du peuple gaulois / âme du peuple celte
     - sacred relics of the Gaulish people / soul of the Celtic people
     - Druid's lie.
   * - Reporter (le/la)
     - the Reporter
     - Character; Ryan Parker.
   * - Respect de l'immersion / période de flottement
     - Respecting Immersion / lull
     - Common rules heading.
   * - Résumé de la situation
     - Situation Summary
     - Player sheet heading.
   * - rituel (druidique / magique / sacré) / formules druidiques
     - (druidic / magic / sacred) ritual / druidic incantations
     - Lore.
   * - Rôles spéciaux
     - Special Roles
     - Player sheet heading.
   * - runes (gravées sur les portants en pierre)
     - runes (carved on the standing stones)
     - Cromlech model.
   * - Ryan Parker
     - Ryan Parker
     - The Reporter.
   * - Salle des Antiquités / salle des artefacts / salle du Trésor
     - Antiquities Room / artefacts room / Treasure Room
     - Prefer "Treasure Room"; "Antiquities Room" only in the police report.
   * - scène d'empoignade
     - scuffle scene
     - Safety rules.
   * - Scène finale / FIN DU JEU
     - Final Scene / END OF GAME
     - Heading.
   * - Sculpture de Cromlech / Datation approximative
     - Cromlech Sculpture / Approximate dating
     - Treasure document heading.
   * - secousses sismiques, remontées de lave
     - seismic tremors, lava upwellings
     - Italian omens.
   * - Sénons
     - Senones
     - Gaulish tribe.
   * - senseur télépathique
     - telepathic sensor
     - Andrea's bracelet / Guide's ring.
   * - Siège d'Uxellodunum (Le)
     - The Siege of Uxellodunum
     - Document title.
   * - "signe des centurions" (bras croisés sur la poitrine) / "signe des druides" (forme de menhir)
     - "Centurions' Sign" (arms crossed over the chest) / "Druids' Sign" (menhir shape)
     - Final scene gestures, described identically in all sheets; capitalised "Centurions' Sign" / "Druids' Sign" (in quotes where the FR has them).
   * - Sommaire
     - Contents
     - GM manual TOC title.
   * - spectre (du druide) / fantôme
     - spectre (of the druid) / ghost
     - Sheet title "DRUID'S SPECTRE"; "a Druid's spectre" in prose. Cromlech only: "fantôme" may be "ghost" here, whereas the Archives game always says "phantom".
   * - Suspect #1 / #2 / #3
     - Suspect #1 / #2 / #3
     - ID sheet headings.
   * - Synopsis
     - Synopsis
     - GM manual heading.
   * - tablette noire de défixion
     - black curse tablet (defixio)
     - Canonical item name.
   * - tatouages-éclair
     - lightning-bolt tattoos
     - Make-up for possessed psykers.
   * - témoin / coincer un témoin / mis en difficulté / divaguer
     - witness / to corner a witness / put on the spot / to ramble
     - Core mechanic.
   * - toge en lin
     - linen toga
     - Curator's ritual garb.
   * - touche-à-tout
     - jack-of-all-trades
     - Guide's (and Curator's) temperament.
   * - Toutatis
     - Toutatis
     - God's name, verbatim.
   * - Trésor (du musée / antique)
     - (Museum / ancient) Treasure
     - Capital T only as the 4th rotation station ("the Treasure", "the Museum Treasure"); lowercase in running prose ("the museum's treasure").
   * - Uxellodunum
     - Uxellodunum
     - Verbatim.
   * - Vercingétorix
     - Vercingetorix
     - Anglicised.
   * - vérifier des faits
     - to check facts
     - Inspector's offer.
   * - Vieux Lyon
     - Vieux Lyon
     - Setting, December 1900. Keep the French district name (usual in English guidebooks and the UNESCO listing); never "Old Lyon".
   * - Vocabulaire
     - Vocabulary
     - Common rules heading.
   * - Vos actions au long de l'enquête
     - Your actions during the investigation
     - Druid's Spectre sheet heading.
   * - Votre histoire / Votre passé
     - Your Story / Your Past
     - Character sheet headings.
   * - Votre rôle dans le dénouement
     - Your role in the ending
     - Druid's Spectre sheet heading.
   * - zombies (psykers)
     - zombies (psykers)
     - Final huddles.

Chrysalis: Descent (The Temple of Nazur) and Chrysalis: Sentience
=================================================================

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - 1/3 de chance, 1/6 de chance
     - 1-in-3 chance, 1-in-6 chance
     - Probability notation.
   * - 5mn / 20mn / 3h30
     - 5 min / 20 min / 3½ h
     - Time notation.
   * - académies étrangères
     - foreign academies
     - Lore (science monopolies).
   * - affaire des éboulis / explosion sulfureuse
     - the rockfall affair / sulphur explosion
     - Sentience plot key. British spelling "sulphur".
   * - agilité
     - Agility
     - Attribute (1–5); also = Attack value. Capitalise as sheet field.
   * - « Ainsi finit tout culte voué aux infâmes idoles »
     - "Thus ends every cult devoted to the vile idols"
     - Pagan Temple graffiti.
   * - akarite(s) / akarite ancien
     - Akarith / Old Akarith
     - Adjective and demonym, capitalised, invariable plural. Never "Akarite".
   * - aller-retour
     - round trip
     - Porter logistics.
   * - amoncellement / empilement d'objets
     - heap of objects / pile of objects
     - Holy of Holies element. Use "heap" consistently.
   * - ancienne écurie
     - old stable
     - Night rendezvous place.
   * - animal de compagnie (des magiciens)
     - familiar
     - Sentience: magicians' pets (toucan, dwarf bear, tortoise). Plain "pet" acceptable in villagers' speech.
   * - animaux « sapiens »
     - "sapient" animals / the sapients
     - Sentience core concept; keep quotation marks on first uses.
   * - apothicaire Colbert / archiviste
     - Colbert the apothecary / archivist
     - Sentience NPC; also runs the telegraph office.
   * - apporteuse d'affaire
     - business introducer
     - Joséphine's intended role with Minéralys.
   * - arbalète compacte (grappin, carreaux, soporifiques)
     - compact crossbow (grapnel, bolts, tranquiliser bolts)
     - Ranger equipment. "carreau d'arbalète" = "crossbow bolt".
   * - arche centrale / arche de pierre (du temple yodique)
     - the central ark / the stone ark
     - A shrine-like detachable object, not an architectural arch. Always "ark".
   * - archéologue (Pr Sylvius)
     - archaeologist (Prof. Sylvius)
     - PC role. British spelling throughout (archaeologist, artefact, defence, colour, mould, sulphur).
   * - artefact exceptionnel
     - exceptional artefact
     - Core mechanic. Always "artefact", never "artifact".
   * - artefact super méga exceptionnel
     - super-mega-exceptional artefact
     - Tongue-in-cheek; keep playful tone (Divine Tear).
   * - artificier confirmé
     - seasoned demolitions expert
     - Butler skill.
   * - Astuce
     - Tip
     - GM note label.
   * - attaque / défense (valeur d'ATTAQUE / DÉFENSE)
     - Attack / Defence (ATTACK value / DEFENCE value)
     - Combat mechanic.
   * - aubergiste Hannibal Monir / Rose / auberge
     - Hannibal Monir the innkeeper / Rose / the inn
     - Sentience NPCs.
   * - autochtones
     - the locals
     - Akarith inhabitants.
   * - automate d'alarme
     - alarm automaton
     - Witcher gadget.
   * - bande-son / son de l'orbe / chant de l'orbe / sifflement / vrombissement
     - soundtrack / the orb sound / the orb's song / strange whistling / humming
     - Multimedia cue.
   * - baril / tonnelet de poudre noire
     - powder keg / small keg
     - Trap near canal.
   * - baroudeur(se) (Rodok)
     - ranger (Rodok)
     - PC role (data key "protector"). Never "adventurer"/"backpacker". In Mindstorm prose Rodok is a "globetrotter" (see that table).
   * - Bartzar
     - Bartzar
     - Akarith warrior statue name; verbatim.
   * - bâton de dynamite
     - stick of dynamite
     - 1 kg dry black powder ≈ 1 stick.
   * - battue / perquisition
     - manhunt / search
     - Final night.
   * - bestiaire
     - bestiary
     - Slideshow content.
   * - bézoar
     - bezoar
     - Sentience; witcher antidote stone.
   * - blessure
     - wound
     - Narrative damage; no HP system.
   * - bonbonne
     - demijohn
     - Heap item with red plum liqueur deposit.
   * - bourgmestre (Honoré des Hautvents)
     - burgomaster (Honoré des Hautvents)
     - Sentience antagonist. Unify spelling "Hautvents".
   * - boyau souterrain (sans oxygène)
     - underground duct (airless)
     - Canal exit.
   * - brancard (téléscopique) / demi-brancard
     - (telescopic) stretcher / half a stretcher
     - Common equipment.
   * - Briefing des joueurs
     - Player briefing
     - Section heading.
   * - butin / marché noir
     - loot / black market
     - Butler objective.
   * - cadavre recroquevillé / naturellement momifié
     - curled-up corpse / naturally mummified
     - Holy of Holies.
   * - calice d'argent
     - silver chalice
     - Booby-trapped chest item.
   * - camion tout-terrain / camp de base
     - off-road truck / base camp
     - Logistics.
   * - campement de chasse
     - hunting camp
     - Witcher's nap spot.
   * - canal / évacuation du canal
     - canal / canal outlet
     - Aquifer Cavern; always "canal", not "channel".
   * - caractéristiques / Caractéristique / Valeur
     - attributes / Attribute / Value
     - Stat block term and sheet table headers.
   * - Caractéristiques des personnages
     - Character attributes
     - Game System heading.
   * - Carbone14
     - carbon-14 dating
     - Science lore.
   * - caverne aquifère
     - Aquifer Cavern
     - Location heading; "Cavern" for the big rooms, "cave" generically. "sous-caverne" = "sub-cavern". Descent location names are Title Case in headings and on the map, lowercase in running text ("the aquifer cavern").
   * - caverne du temple yodique
     - Yodic Temple Cavern
     - Location heading (Title Case); lowercase in running text ("the Yodic temple cavern").
   * - cérémonie de crémation / obsèques
     - cremation ceremony / funeral
     - Sentience scene 3.
   * - champignons rosés / champignons aquatiques bleus
     - pinkish mushrooms / blue water mushrooms
     - Flora.
   * - chance (la "chance")
     - "luck"
     - Dice philosophy.
   * - chatière en métal (coulissante)
     - sliding metal hatch
     - Main hall.
   * - chauve-souris phosphorescentes / luminescentes amphibies
     - amphibious luminescent bats
     - Unify adjective.
   * - Chlamydes / serpents-requins
     - Chlamydes / shark-snakes
     - Creature; sing. "Chlamyde".
   * - Chrysalis:Descent / Chrysalis:Sentience / MANUEL du JDR CHRYSALIS:DESCENT
     - Chrysalis: Descent / Chrysalis: Sentience / CHRYSALIS: DESCENT RPG MANUAL
     - Titles.
   * - chute de Nazur
     - the fall of Nazur
     - Dating reference.
   * - clef en laiton / clef de la pagode
     - brass key / the pagoda key
     - Corpse item.
   * - coffre en bois (piégé) / dispositif de mise à feu
     - (booby-trapped) wooden chest / firing mechanism
     - Trap.
   * - coffre-fort / coffret métallique
     - safe / metal casket
     - Sentience: Joséphine's safe at the Town Hall (see "Hôtel de Village").
   * - Colère des Yods
     - the Wrath of the Yods
     - Thunder, per locals. Plural "Yods".
   * - colline extérieure
     - The Hill Outside
     - Location heading (Title Case); lowercase in running text ("the hill outside").
   * - combat / Combats possibles
     - fight / Possible Fights
     - Section heading.
   * - combinaison spéléologique / bouteille de plongée / lunettes de vision nocturne
     - caving suit / diving tank / night-vision goggles
     - Equipment.
   * - Compagnie des Rocheuses
     - the Rockies Company
     - Sentience mining corporation.
   * - compétences / Compétences communes
     - skills / Common abilities
     - Sheet section (yaml key "abilities"); Sentience "Compétences communes" are powers.
   * - Compétences / Equipements / Communs : / Spécifiques : (feuille de personnage Descent)
     - Skills / Equipment / Common: / Specific:
     - Player sheet template headings (yaml keys abilities / common_equipments / equipments).
   * - Compétences communes des animaux « sapiens »
     - Common abilities of the "sapient" animals
     - Opening heading.
   * - confession (razulite / taranite)
     - denomination (Razulite / Taranite)
     - Religious schism. "confession" is a false friend.
   * - Congrès Trisannuel des Prodiges
     - the Triennial Congress of Wonders
     - Sentience lore.
   * - constitution
     - Constitution
     - Attribute.
   * - Contexte de l'expédition
     - Expedition background
     - Section heading.
   * - convois (exemples de convois)
     - hauls (example hauls)
     - Porter loads.
   * - corbeau postal
     - messenger raven
     - Sentience.
   * - cornes rabotées
     - filed-down horns
     - Goat skull.
   * - corniche
     - ledge
     - Aquifer cavern.
   * - corridor inondé / cuvette
     - flooded corridor / dip
     - East corridor.
   * - coups de théâtre
     - dramatic twists
     - Sentience heading.
   * - cristaux sulfureux / huile de roche
     - sulphur crystals / rock oil
     - Sentience industrial lore.
   * - crypte
     - crypt
     - Monitor lizard's lair.
   * - dalle
     - flagstone
     - Trap trigger.
   * - Dé 6 / Dé à 6 faces / D6
     - D6 / six-sided die
     - Both games use a single D6.
   * - Délais
     - Time costs
     - Quick Reference heading.
   * - Déroulement d'une partie / Le déroulement du jeu
     - How a session unfolds / How the game unfolds
     - Section headings.
   * - diamants incrustés
     - inlaid diamonds
     - In fresco.
   * - diaporama / diapositives / mode manuel
     - slideshow / slides / manual mode
     - GM media cues.
   * - dommages (narratifs)
     - (narrative) damage
     - Mechanic.
   * - Druide Galien / ours nain
     - the Druid Galien / dwarf bear
     - Sentience NPC and familiar.
   * - éboulis / éboulé / semi-éboulis
     - rubble / collapsed / partial rubble
     - Tunnels ("collapsed tunnel", "rockfall").
   * - échec critique (fumble)
     - critical failure (fumble)
     - Descent: a 6. Sentience: a 1.
   * - Écran de Jeu
     - GM screen
     - GM material.
   * - efficacité double
     - double potency
     - Elixir with spectrometer dosing.
   * - église monothéiste / temple néopaïen
     - monotheistic church / neo-pagan temple
     - Historical summary.
   * - Élixir Berserk / Quête de l'Élixir Berserk / Recette
     - Berserk Elixir / The Berserk Elixir Quest / Recipe
     - Ranger's personal quest (also exists in Mindstorm).
   * - Émile le tanneur
     - Émile the tanner
     - Sentience.
   * - Enchanteresse Dorina / toucan à bec vert
     - the Enchantress Dorina / green-billed toucan
     - Sentience.
   * - énigme / Enigme lumineuse / énigme teaser
     - puzzle / The Light Puzzle / teaser puzzle
     - "puzzle" for mechanical ones, "riddle" for textual riddles.
   * - Enquête archéologique / Enquête naturaliste
     - Archaeological investigation / Naturalist investigation
     - Quick-reference headings.
   * - Equipements (Communs / Spécifiques)
     - Equipment (Common / Specific)
     - Sheet headings; "equipment" uncountable.
   * - espèce inconnue / faits scientifiques nouveaux
     - unknown species / new scientific facts
     - Naturalist objectives.
   * - essais et erreurs
     - trial and error
     - Idiom.
   * - êtres de l'air / de la terre / de l'eau
     - the beings of the air / of the earth / of the water
     - Lever riddle.
   * - Exemple de déroulement minuté
     - Sample timeline
     - Heading.
   * - feuille de personnage / fiche de personnage
     - character sheet
     - Generic.
   * - fidèles / impies / hérétiques
     - the faithful / the impious / heretics
     - Religious vocabulary.
   * - fidèles serviteurs / porteurs
     - faithful servants / porters
     - Two NPCs in their fifties. Always "porters".
   * - « Filtre de l'Orthodoxie »
     - "Filter of Orthodoxy"
     - Engraved on well grate.
   * - fiole en or
     - gold vial
     - Contains Berserk Elixir.
   * - flambeau / torches en bois / lampe frontale / spot lumineux
     - torch (flame) / wooden torches / headlamp / spotlight
     - Light sources.
   * - fresque murale
     - wall fresco
     - Unify "fresco".
   * - fronton
     - pediment
     - Pagan Temple.
   * - fumigène urticant
     - irritant smoke grenade
     - Butler equipment.
   * - galerie du fond
     - rear gallery
     - Main hall.
   * - garde-frontières / garnison
     - border guards / garrison
     - Escape context.
   * - gemmes basiques / libres / violettes / pierreries
     - basic gems / loose gems / purple gems / precious stones
     - Purple gems are fake. "sans valeur" → "worthless".
   * - géodes lumineuses / mini-géodes
     - glow-geodes / mini-geodes
     - Common equipment.
   * - gîte / antre / nid
     - lair / nest
     - Monitor lair; yeti nest.
   * - graffitis
     - graffiti
     - Uncountable in EN.
   * - grille de fer (lourde, rouillée)
     - heavy rusty iron grate
     - Well cover.
   * - grimoire de vie / journal intime
     - Grimoire of Life / diary
     - Sentience MacGuffin.
   * - guano brun (radioactif)
     - brown guano (radioactive)
     - Resource.
   * - guetteur / guet
     - lookout
     - Left on hilltop.
   * - hallebarde
     - halberd
     - Well bottom.
   * - hélice de bateau rouillée / cierge liturgique / poteries / crânes
     - rusty boat propeller / liturgical candle / pottery / skulls
     - Heap contents.
   * - « Hérétiques, faites demi-tour avant que les Yods ne vous noient dans le feu »
     - "Heretics, turn back before the Yods drown you in fire"
     - Aquifer Cavern graffiti.
   * - Hibou
     - Owl
     - Sentience PC.
   * - Hôtel de Village
     - Town Hall
     - Sentience: the village institution where Joséphine has her office; capitalised. FR "Hôtel de ville" also = "Town Hall".
   * - IMPORTANT - Briefing des joueurs
     - IMPORTANT - Player briefing
     - Heading.
   * - inception
     - inception
     - Owl ability.
   * - indice(s)
     - clue(s)
     - Generic.
   * - initiative / effet de surprise
     - initiative / surprise
     - Combat.
   * - JDR / jeu de rôle / jeu de rôle d'aventure-enquête exploratoire / boosté au multimédia
     - RPG / role-playing game / exploratory adventure-investigation RPG / multimedia-enhanced
     - Generic.
   * - jet de dé / faire moins ou égal
     - die roll / roll equal to or under (the attribute)
     - Descent resolution.
   * - jets de difficulté variable
     - rolls of variable difficulty
     - Sentience resolution.
   * - Joséphine des Hautvents / Fénelon, notaire
     - Joséphine des Hautvents / Fénelon the notary
     - Sentience.
   * - kit d'analyse gemmologique / trousse médicale et antipoison / kit d'archéologie
     - gemmological kit / first-aid and antidote kit / archaeology kit
     - Equipment.
   * - kit espionnage / kit de micros / console d'écoute
     - spy kit / microphone kit / listening console
     - Ranger equipment.
   * - L'alchimiste est morte
     - The Alchemist Is Dead
     - Scenario subtitle.
   * - lanterne de pierre
     - stone lantern
     - Well puzzle.
   * - larme divine
     - the Divine Tear
     - Singular artefact (= the orb).
   * - Le sorceleur est en route vers le village / … est acclamé par les villageois à son retour / … fait son discours et sème la discorde / Les villageois interrompent les obsèques de l'alchimiste / La soirée amène des coups de théâtre
     - The witcher is on his way to the village / … is cheered by the villagers on his return / … makes his speech and sows discord / The villagers interrupt the alchemist's funeral / The evening brings dramatic twists
     - Scene headings 1-4.
   * - leviers / vannes / pistons en bois / grand levier isolé
     - levers / sluice gates / wooden plungers / large lone lever
     - Water puzzle.
   * - lézardes
     - fissures
     - Ceiling/wall cracks (not lizards!).
   * - lichens / gaz dangereux / toxique
     - lichens / toxic gas
     - Hazard.
   * - Lieux et actions possibles / Gameplays communs à tout le jeu
     - Locations and Possible Actions / Gameplay Common to the Whole Game
     - Headings.
   * - lingot d'or
     - gold ingot
     - Orb's pedestal.
   * - liqueur de prune rouge
     - red plum liqueur
     - Elixir ingredient.
   * - « Lorsque la Lueur de la Foi traverse le Tamis de la Doctrine, se manifeste la Gloire des Yods »
     - "When the Glow of Faith passes through the Sieve of Doctrine, the Glory of the Yods is revealed"
     - Fresco inscription.
   * - « Lumière des fidèles »
     - "Light of the Faithful"
     - Lantern engraving.
   * - machine à écrire
     - typewriter
     - Sentience clue.
   * - mâchoire métallique (ensanglantée)
     - (bloodied) metal jaw
     - Sentience planted weapon.
   * - majordome (Rydji)
     - butler (Rydji)
     - PC role; avoid "majordomo".
   * - masque de survie / masque à gaz / masque de protection bactério-chimique
     - survival mask / gas mask / bio-chemical protective mask
     - Same item under three names.
   * - mèche / mèche à explosif / vieille mèche
     - fuse / blasting fuse / old slow fuse
     - Not "wick"; not "detonating fuse" (real det cord is far faster): "100 m of blasting fuse (burn rate 5 m/s)".
   * - Médias d'accompagnement
     - Supporting media
     - Heading.
   * - méta-jeu
     - metagaming
     - Briefing note.
   * - mode nomade
     - nomadic mode
     - Slideshow on a tablet.
   * - moisissures / infection pulmonaire / oedème à la gorge / trachéotomie
     - mould / lung infection / throat oedema / tracheotomy
     - Hazards.
   * - monolithe
     - monolith
     - Balanced stalagmite.
   * - mousquet / katana / faux / machette longue
     - musket / katana / scythe / long machete
     - Weapons.
   * - nappes phréatiques
     - water table
     - Geology.
   * - naturaliste (Dr Physh)
     - naturalist (Dr Physh)
     - PC role.
   * - Nazur / Nazuron / « Le temple de Nazur » / ancienne capitale hérétique
     - Nazur / the River Nazuron / "The Temple of Nazur" / former heretic capital
     - Proper nouns verbatim.
   * - nyctalopie / œil aiguisé et serres acérées / envol silencieux
     - night vision / keen eye and sharp talons / silent flight
     - Owl abilities.
   * - observation
     - Observation
     - Attribute.
   * - orage
     - thunderstorm
     - Weather cover.
   * - ordre de marche
     - marching order
     - Party formation.
   * - Ordre des Sorceleurs / sorceleur (Abélard)
     - Order of Witchers / witcher (Abélard)
     - Sentience; lowercase common noun.
   * - ouïe fine et odorat fin
     - keen hearing and keen sense of smell
     - Wombat trait.
   * - Ouistiti
     - Marmoset
     - Sentience PC.
   * - Pacte de Sang
     - Blood Pact
     - Sentience core lore.
   * - pagode (petite, en terre séchée)
     - small dried-clay pagoda
     - Locked container.
   * - parchemins roulés / parchemins sacrés / livres saints du yodisme
     - rolled scrolls / sacred scrolls / Yodic holy books
     - Pagoda contents.
   * - parvis / tunnel de procession pré-yodique / plateforme en pierre taillée
     - forecourt / pre-Yodic processional tunnel / cut-stone platform
     - Arrival point.
   * - paysan akarite / zélote akarite
     - Akarith peasant / Akarith zealot
     - Enemies.
   * - pèlerinage annuel des fidèles yodiques
     - annual pilgrimage of the Yodic faithful
     - Background.
   * - Péripéties envisageables
     - Possible complications
     - Heading.
   * - personnages prétirés
     - pre-generated characters (pregens)
     - RPG jargon.
   * - pièces de monnaie percées / débris de bateaux
     - pierced coins / boat wreckage
     - Bait on ledge.
   * - piège (pieux sur ressort)
     - trap (spring-loaded spikes)
     - Trap.
   * - pierres tombales dressées
     - standing gravestones
     - Resource.
   * - piolet / pioche
     - ice axe / pickaxe
     - Tools.
   * - pions / plans (ou artworks)
     - tokens / maps (or artwork)
     - GM material.
   * - pistage
     - tracking
     - Sentience scene 1.
   * - poche ventrale / bouclier cartilagineux / salive infectée / nuisible
     - belly pouch / cartilaginous rump shield / septic saliva / vermin
     - Wombat traits.
   * - point radio / opérateur télécom / émetteur-récepteur radio
     - radio check-in / radio operator / radio transceiver
     - Briefing rule.
   * - poissons nacrés / poissons aveugles du puits
     - pearly fish / blind well-fish
     - Not "pearl fish".
   * - polyglotte / psychologue / réminiscence
     - polyglot / psychologist / reminiscence
     - Sapient abilities.
   * - pont couvert de poix
     - pitch-covered bridge
     - Fire trap.
   * - portique d'entrée / loge / insigne religieux
     - entrance portico / niche / religious insignia
     - Where the crossentar sits.
   * - poste télégraphique / « répondeur » / message de statut
     - telegraph office / "answering machine" / status message
     - Sentience; keep quotation marks.
   * - poudre noire
     - black powder
     - Explosive.
   * - présage néfaste
     - ill omen
     - Owl trait.
   * - Présentation rapide du jeu / Présentation de l'univers / Scénario de la session
     - Quick Game Overview / Setting Overview / Session Scenario
     - Headings.
   * - Prologue – à lire en entier aux joueurs / Prélude / Synopsis / Le fond secret de l'affaire (pour le MJ) / Le vrai fond de l'affaire
     - Prologue – read in full to the players / Prelude / Synopsis / The Secret Behind the Affair (GM only) / The Real Truth of the Matter
     - Sentience headings.
   * - prophétie razulite / runes sacrées akarites / message runique
     - Razulite prophecy / Akarith sacred runes / runic message
     - Lore.
   * - « puants singes glabres »
     - "stinking hairless apes"
     - Forged letter wording.
   * - puits (creusé dans la colline) / puits (Saint des Saints)
     - shaft (blasted into the hill) / well (Holy of Holies)
     - Two different objects; distinguish.
   * - racines d'arbres
     - tree roots
     - Depth clue.
   * - raie-pieuvre-caméléon terrestre
     - land ray-octopus-chameleon
     - One hybrid creature.
   * - Rapatriement des éléments intéressants
     - Hauling Back the Finds
     - Heading.
   * - râtelier
     - torch rack
     - Furniture.
   * - razulite / taranite / Sul'Razul / Sul'Taran / devises razulites
     - Razulite / Taranite / Sul'Razul / Sul'Taran / Razulite mottoes
     - Yodic denominations; capitalise.
   * - Récapitulatifs
     - Quick Reference
     - Section behind GM screen.
   * - renfoncement hexagonal
     - hexagonal recess
     - Well bottom.
   * - Répartition des rôles
     - Role assignment
     - Heading.
   * - Résumé historique
     - Historical summary
     - Heading.
   * - réussite / succès / réussite exceptionnelle
     - success / exceptional success
     - Dice.
   * - Sabarite / pays de Sabarite / noblesse sabarite
     - Sabarim / the land of Sabarim / Sabarith nobility
     - Country = Sabarim; adjective = Sabarith.
   * - Saint des Saints
     - Holy of Holies
     - Location.
   * - Saint des Saints du Temple Yodique
     - Holy of Holies of the Yodic Temple
     - Location heading.
   * - Salle principale du temple (pré-)yodique
     - Main Hall of the Pre-Yodic Temple
     - Heading; keep "Pre-" (the building predates Yodism and was only later taken over by the Razulites). Lowercase in running text.
   * - scoop archéologique
     - archaeological scoop
     - Archaeologist mission.
   * - Séléné / Sylvorann
     - Séléné / Sylvorann
     - Alchemist and village; verbatim with accents.
   * - simulacre
     - pretence
     - Joséphine/Abélard sham conversation.
   * - Société Minéralys
     - the Minéralys Company
     - Sentience; keep accent.
   * - socle pour des feux rituels
     - plinth for ritual fires
     - Recess beside temple.
   * - somnifère (légers somnifères)
     - sedative (mild sedatives)
     - Drug.
   * - « Souffrance et mort aux impies »
     - "Suffering and death to the impious"
     - Graffiti.
   * - source thermale / moulins solaires
     - hot spring / solar mills
     - Sentience.
   * - spectromètre de masse / sonar / détecteur de radioactivité / détecteur de métaux
     - mass spectrometer / sonar / radiation detector / metal detector
     - Gear.
   * - Statistiques
     - Stats
     - Sheet header.
   * - statue de guerrier (akarite) / statues païennes
     - (Akarith) warrior statue / pagan statues
     - Artefacts.
   * - Symbole de la Force
     - Symbol of Strength
     - Fresco engraving.
   * - Système de jeu
     - Game System
     - Heading.
   * - table basse
     - low table
     - Not "coffee table".
   * - télépathie / communiquer télépathiquement / télépathie rayonnante
     - telepathy / communicate telepathically / radiating telepathy
     - Sapient abilities.
   * - temple païen
     - Pagan Temple
     - Location heading (Title Case); lowercase in running text ("the pagan temple").
   * - théocratie yodique fanatisée
     - fanatical Yodic theocracy
     - Akaris description.
   * - torchis
     - cob
     - Temple windows.
   * - Tortue ancestrale (PNJ)
     - Ancestral Tortoise (NPC)
     - "tortoise", not "turtle". A named NPC: always capitalised, "the Ancestral Tortoise", also in running text; the short form "la tortue" = "the Tortoise" (capitalised), as it designates the same character.
   * - tour / chaumière de l'alchimiste
     - the alchemist's tower / cottage
     - Same dwelling, two words.
   * - traces de vandalisme
     - traces of vandalism
     - Teaser puzzle.
   * - treuil multi-filins
     - multi-cable winch
     - At shaft top.
   * - Trouvailles revendables ou exceptionnelles
     - Resaleable or Exceptional Finds
     - Heading.
   * - tunnel vers l'extérieur
     - Tunnel to the Outside
     - Heading (Title Case); lowercase in running text.
   * - varan impérial / varan royal / varan
     - imperial monitor (lizard) / monitor lizard
     - Unify "imperial monitor" ("varan royal" too). Bare "le varan" = "the monitor lizard" (master_script, also in lists of beasts); "the monitor" alone only right after "imperial monitor" in the same passage.
   * - vidéo d'introduction
     - intro video
     - Multimedia cue.
   * - ville « maudite et vouée à l'interdit »
     - city "cursed and placed under interdict"
     - Nazur epithet.
   * - Wombat (marsupial fouisseur)
     - Wombat (burrowing marsupial)
     - Sentience PC.
   * - yéti forestier
     - forest yeti
     - Creature.

Alternate reality game: Auction (the Pychronia web game)
=========================================================

.. Terms coined while translating ``alternate_reality_game_auction/**/*_fr.yaml``
   into ``*_en.yaml``. Run ``docs/check_fixture_translations.py`` after any
   change: both languages must keep the same keys, identifiers, file paths and
   game markup. Secret answers (``secret_answer``) and hidden-clue categories
   are translated, since players deduce them from English texts.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Français
     - English
     - Notes
   * - Âge de l'Equilibre Universel
     - Age of Universal Balance
     - Mythical era (encyclopedia).
   * - airain hyper-condensé
     - hyper-condensed bronze
     - Arkon's gladius.
   * - archimage
     - archmage
     - Lowercase in prose.
   * - Bataille de Wigwir
     - Battle of Wigwir
     - Capitalised as an event name; the GM manual also says "the battle of Wigwir" in running text.
   * - bouboule
     - Roly-Poly
     - Nickname (news messages).
   * - Central Obéron
     - Oberon Central
     - Signature.
   * - Centre d'Etudes de Belez
     - Belez Study Centre
     - Biophysics signature.
   * - Centre Scanner (à Alifir)
     - Scanner Centre (in Alifir)
     - World Scan help page.
   * - cérémonie finale / cérémonie de remise des prix
     - final ceremony / prize-giving ceremony
     - Alifir Academy events.
   * - chant de l'orbe / chant des orbes
     - song of the orb / song of the orbs
     - Lowercase.
   * - cimetière animal du Père Huche (Salima Sud)
     - Père Huche pet cemetery (South Salima)
     - Location in player messages.
   * - Citadelle Nuageuse
     - Cloud Citadel
     - Seat of the Akarith Judicators' councils.
   * - conciergerie centrale de Faeran
     - central concierge desk in Faeran
     - Waden's pick-up point.
   * - Congrégation pour l'Orthodoxie
     - Congregation for Orthodoxy
     - Akarith department.
   * - continent mécréant
     - the infidel continent
     - Akarith view of other lands.
   * - Défi d'Échecs
     - Chess Challenge
     - Ability and GM manual heading.
   * - désert de sel / salar / banquise de sel
     - salt desert / salar / salt pack ice
     - Geography (encyclopedia).
   * - Détecteur Manaïque
     - Manaic Detector
     - Paladium product.
   * - Doyen des Fidèles Akarites
     - Dean of the Akarith Faithful
     - Bishop Baazel's signature.
   * - Doyenne(s) (d'Alifir) / muses-doyennes
     - Dean(s) (of Alifir) / muse-deans
     - Lowercase "the deans" in prose; capitalised in signatures and before a name (Aiode, Melete, Mneme).
   * - Duc Dorien / Empire Akarite
     - the Dorian Duke / the Akarith Empire
     - Auction ARG term.
   * - empreinte manaïque / manaïque
     - manaic imprint / manaic
     - Extends "Rétrocaméra Manaïque".
   * - Enchères mono-tour au (deuxième) meilleur offrant
     - Single-round auctions, (second-)highest bid wins
     - Auction rules page.
   * - enquêteur du temps
     - investigator of time
     - Loyd Georges about himself.
   * - Ère Stable
     - Stable Era
     - Calendar era.
   * - État Parlementaire de Masslavie
     - Parliamentary State of Masslavia
     - Auction ARG term.
   * - Faction mottos: « Liberté, honneur, robustesse » / « Grandeur, Largesse, Délicatesse » / « Opulence, Indépendance, Puissance » / « Foi, Pureté, Divinité » / « Loi, Ordre, Sécurité »
     - "Freedom, honour, fortitude" / "Grandeur, Largesse, Finesse" / "Opulence, Independence, Power" / "Faith, Purity, Divinity" / "Law, Order, Security"
     - Super-faction mottos.
   * - Fédération Lordanienne
     - Lordanian Federation
     - Auction ARG term.
   * - Flash Info
     - Newsflash
     - News subject prefix.
   * - Force et Honneur
     - Strength and Honour
     - Sign-off.
   * - Gemmes pratiques pour faire l'appoint / gemmes piégées
     - handy gems for topping up a payment / trap gems
     - GM hints on auction gems.
   * - Géolocalisation Numérique
     - Digital Geolocation
     - GeoIP service.
   * - Grand Colloque (de l'Académie d'Alifir)
     - Grand Colloquium
     - Academy event; never "Symposium".
   * - Grand Concile Secret (akarite)
     - (Akarith) Grand Secret Council
     - Auction ARG term.
   * - Grand Conseil (akarite) / Grand Conseil Nalavutien
     - Great Council / Great Nalavutian Council
     - Auction ARG term.
   * - Grand Hibou Céleste
     - Great Celestial Owl
     - Nalavutian deity.
   * - Grand Inquisiteur
     - Grand Inquisitor
     - Akarith rank.
   * - Grand Mandataire
     - Grand Mandatary
     - Heliossarian head of state.
   * - Grimoire Sacré Akarite / grimoire-clé
     - Sacred Akarith Grimoire / key grimoire
     - Auction ARG term.
   * - Guerres Midoliennes / guerre midolienne
     - Midolian Wars / Midolian war
     - Auction ARG term.
   * - guilde des voleurs
     - thieves' guild
     - Lowercase.
   * - Harmonies Jungliennes
     - Jungle Harmonies
     - Claudia Pason's album; the track list keeps the French map labels in brackets, since the jungle map image is French.
   * - historique télécom
     - telecom history
     - UI-related wording.
   * - Hymne X
     - X anthem
     - Eg. "Masslavian anthem".
   * - Hôtel Impérial d'Alifir
     - Alifir Imperial Hotel
     - Auction ARG term.
   * - Imprimeries Tridimensionnelles de Kioctl
     - Kioctl Three-Dimensional Printing Works
     - Auction ARG term.
   * - judicateur suprême Arthanas / Messagers des Yods
     - Supreme Judicator Arthanas / Messengers of the Yods
     - Rank before a name; epithet of the Judicators.
   * - Jungle de Kamilia: Lisière Ouest aux Oiseaux / Pic de l'Aiguille Noire / Mont Eventé / Caverne du Géant Invisible / Vallée du Souffle / Ruisseau des 1000 Branches / Plateau de Kupoutac / Rivière Cascadante / Ruisseau Rutilant / Ruisseau Vaseux / Roc du Babouin / Butte des Arbres Secs
     - Kamilia Jungle: Western Edge of the Birds / Black Needle Peak / Windswept Mount / Cavern of the Invisible Giant / Valley of the Breath / Brook of the 1000 Branches / Kupoutac Plateau / Cascading River / Glittering Brook / Muddy Brook / Baboon Rock / Dry Trees Mound
     - Places of the Jungle Harmonies clue; they must match the labels of images/world_maps/kamilia_jungle_map_en.jpg (generated by docs/translate_kamilia_jungle_map.py). Always "1000 Branches", never "100".
   * - Justice et Vérité
     - Justice and Truth
     - Paladium sign-off.
   * - kit de mise sur écoute / kit de confidentialité / mise sur écoute
     - wiretapping kit / privacy kit / wiretapping
     - Wiretapping ability.
   * - la main des dieux
     - the hand of the gods
     - Prof. Losslass's nickname.
   * - « Les vieilleries de Joji »
     - "Joji's Old Curios"
     - Shop in Baynon.
   * - Lettre de Mission X
     - Mission Letter - X
     - Letterhead.
   * - Ligue Bancaire Pangéenne
     - Pangean Banking League
     - Escrow page.
   * - Livres Sabarites Certifiées
     - Certified Sabarith Pounds
     - Currency wording.
   * - Lolo
     - Lolo
     - Emilos's nickname for Loyd Georges.
   * - marché informel
     - informal market
     - Black market self-designation.
   * - marées yodiques
     - Yodic tides
     - Historical period.
   * - maître des enchères
     - auctioneer
     - Auction rules.
   * - Maître Izdouvraj (huissier)
     - Master Izdouvraj (bailiff)
     - Chess Challenge.
   * - Merveilleux Zélote Bartzar
     - Marvellous Zealot Bartzar
     - Auction ARG term.
   * - messageries Microcosme
     - Microcosm inboxes
     - Auction ARG term.
   * - mi-moniale / mi-monesse
     - semi-nun
     - The Judicators' courtesans.
   * - Mielleries à l'Ancienne
     - Traditional Honeyworks
     - Company in Cazoar.
   * - module djinnique
     - Djinnic module
     - Auction ARG term.
   * - Mont Olysho / colline Brumerre
     - Mount Olysho / Brumerre Hill
     - Auction ARG term.
   * - montagnes nacrées
     - pearly mountains
     - Axolia.
   * - nourrissons d'Eiode / Fils d'Eiode
     - Infants of Eiode / Sons of Eiode
     - Auction ARG term.
   * - Objets d'Enchères (page)
     - Auction Items
     - UI page name.
   * - orbe polaire
     - polar orb
     - Lowercase.
   * - panier à crabes
     - nest of vipers
     - Idiom.
   * - Panthéon Éternel (de l'Académie)
     - Eternal Pantheon
     - Auction ARG term.
   * - passe-murs éthérés
     - ethereal wall-walkers
     - Seal list.
   * - phonodistance
     - long-distance phone
     - Auction ARG term.
   * - puk(s)
     - puk(s)
     - Oberon slang for hired thugs; verbatim, lowercase.
   * - Race élue des Yod(s)
     - Chosen Race of the Yods
     - Auction ARG term.
   * - Rapport synthétique X - Affaire Loyd Georges
     - X summary report - The Loyd Georges affair
     - Letterhead.
   * - Sanctuaire des Yods (Zorzas)
     - Sanctuary of the Yods
     - Auction ARG term.
   * - Scan Mondial (section / service)
     - World Scan
     - UI label; distinct from "Scanner Mondial" = World Scanner item.
   * - sciences technomanaïques
     - technomanaic sciences
     - The GM manual also says "technomagical".
   * - Service OmniVision
     - the OmniVision Service
     - Manor surveillance.
   * - Services des Renseignements Généraux (X) / Services de police Généraux Sabarites
     - (X) General Intelligence Services / Sabarith General Police Services
     - Letterheads.
   * - Télécoms Pangéennes
     - Pangean Telecoms
     - Wiretapping help.
   * - Télévisualisation (2D/3D)
     - televisualisation
     - Slideshow pages.
   * - Thélassare(s)
     - Thelassarian(s)
     - Demonym, by analogy with Heliossarian.
   * - {{ titre_officiel }} / {{NUMERO_GAMEMASTER}} / {{ PRIX }} / {{ JOUEUR }} / {{ nom_du_module }}
     - {{ official_title }} / {{GAMEMASTER_NUMBER}} / {{ PRICE }} / {{ PLAYER }} / {{ module_name }}
     - Placeholders that the game master fills in by hand are translated; ``{{ character_properties... }}`` variables stay verbatim.
   * - Traducteur de Runes (de l'Académie)
     - Rune Translator
     - Device; "Yodic Rune Translator" for the ability.
   * - transpondeur Lasulis / lentilles de Barzow
     - Lasulis transponder / Barzow lenses
     - Waden's equipment request.
   * - vieille branche / les anciens
     - old bean / old-timers
     - Familiar address (Emilos, Waden).
   * - Votre rectitude
     - Your Rectitude
     - Loyd Georges mocking Dean Melete.

Jinja symbol display values
===========================

.. Display values of ``{% symbol "value" for "key" %}`` tags. The sheet
   generator aborts when one key is given two different values across the
   rendered templates, so every ``*_en.rst`` file must use exactly the English
   value listed here (case-insensitive). Clock times are written HH:MM (24-hour).
   This table is generated from the fixture files by the merge script.

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Symbol key
     - Français
     - English
   * - ``afternoon_lg_medecine_time``
     - 18h
     - 18:00
   * - ``afternoon_opal_departure_time``
     - 14h45
     - 14:45
   * - ``akarith_ambassador_skull_ring_origin``
     - hauteurs de Kéroskia
     - Keroskia highlands
   * - ``akarith_sect_coded_message``
     - MO NOUS COUVRE - LIVRAISON OK – 17 TAVERNES AUBONPICHET SOUMISES SUR 1238
     - MO IS COVERING US - DELIVERY OK – 17 AUBONPICHET TAVERNS SUBDUED OUT OF 1238
   * - ``akarith_sect_den_bar``
     - Café Bargarac d'Alifir
     - Café Bargarac in Alifir
   * - ``alphonse_alibi_bar``
     - La Murge de Salima
     - La Murge de Salima
   * - ``amethyst``
     - 11h
     - 11:00
   * - ``amethyst_hostel_room``
     - 8e étage de l'Hotel SalimaGlobeCenter
     - 8th floor of the SalimaGlobeCenter Hotel
   * - ``amplificans_artefacts_symbol``
     - soleil orné en son centre d'un tourbillon noir
     - sun with a black whirl at its centre
   * - ``analysis_code_androids_command_bracelet``
     - fzk
     - fzk
   * - ``analysis_code_arkon_gladius``
     - xep
     - xep
   * - ``analysis_code_arkon_skull``
     - srf
     - srf
   * - ``analysis_code_thief_bones``
     - jsb
     - jsb
   * - ``analysis_code_thief_wallet``
     - yal
     - yal
   * - ``analysis_code_three_tombs``
     - ltx
     - ltx
   * - ``analysis_portal_hint_category``
     - analyse
     - analysis
   * - ``androids_command_bracelet_name``
     - Dominion
     - Dominion
   * - ``archivist_name``
     - Maître Parchemine
     - Master Parchemine
   * - ``arkon_armor_name``
     - armure de Mithril
     - Mithril armour
   * - ``arkon_mission_confession``
     - confession de mission
     - mission confession
   * - ``arkon_name``
     - Valerias
     - Valerias
   * - ``arkon_skull_location``
     - plantes de la bibliothèque
     - library plants
   * - ``arkon_weapon_name``
     - glaive
     - gladius
   * - ``arrivée_conservateur_à_cérémonie_le_jour_j``
     - 10h
     - 10:00
   * - ``arrivée_conservateur_au_cromlech_le_jour_j``
     - 7h
     - 7:00
   * - ``astral_opening_date``
     - solstice d'hiver
     - winter solstice
   * - ``auction_process_instructions``
     - Les lots de gemmes sont vendus en enchères descendantes, tandis que les artefacts le sont en enchères montantes normales.
     - Gem lots are sold by descending auction, while artefacts are sold by normal ascending auction.
   * - ``automaton_symbolic_cloth``
     - rubans blancs
     - white ribbons
   * - ``avatar_duchess_novel_name``
     - Les cygnes d'étang
     - The Pond Swans
   * - ``avatar_inventor_novel_name``
     - Le ballet des automates
     - The Ballet of the Automatons
   * - ``banquet_name``
     - banquet d'outre-monde
     - Otherworld Banquet
   * - ``bewitchment_portal_hint_category``
     - magie
     - magic
   * - ``book_of_the_dead``
     - Thanatologue
     - Thanatologue
   * - ``candle_batteries_name``
     - cartouches de vapeur de cire pressurisée
     - pressurised wax vapour cartridges
   * - ``catastrophic_period``
     - marasme planétaire
     - Planetary Cataclysm
   * - ``code_du_cryptex``
     - secret
     - secret
   * - ``common_monastery_name``
     - Monastère de Rochesombre
     - Rochesombre Monastery
   * - ``current_era_name``
     - ère du Grand Apaisement
     - Era of the Great Appeasement
   * - ``current_events_year``
     - an 1000
     - year 1000
   * - ``cynthia_employer_name``
     - Gazette de Sabarim
     - Sabarim Gazette
   * - ``cynthia_friend_name``
     - Sylwie Lescusa
     - Sylwie Lescusa
   * - ``cynthia_proofs_hiding_place``
     - cassette en plomb sous une latte de plancher
     - lead casket under a floorboard
   * - ``cynthia_sabarim_home_address``
     - studio numéro 827 aux presqu'îles de Wetfeet (lieu-dit près d'Alifir)
     - studio flat number 827 in the Wetfeet Peninsulas (a locality near Alifir)
   * - ``cynthia_sheet_motto``
     - L'âme audacieuse et secourable
     - The bold and helpful soul
   * - ``délai_analyse_du_glaive_antique``
     - un mois
     - one month
   * - ``délai_arrivée_du_guide_au_cromlech``
     - 1 an
     - 1 year
   * - ``délai_arrivee_du_héros``
     - trois mois
     - three months
   * - ``délai_arrivée_du_reporter_au_cromlech``
     - 6 mois
     - 6 months
   * - ``délai_attente_heros_par_reporter_le_jour_j``
     - une bonne heure
     - a good hour
   * - ``délai_attente_police_par_reporter_le_jour_j``
     - 1h
     - 1 hour
   * - ``délai_début_secousses_sismiques_italiennes``
     - 1 an
     - 1 year
   * - ``délai_guide_a_donné_clefs_au_héros``
     - un mois
     - one month
   * - ``délai_mort_père_du_conservateur``
     - 15 mois
     - 15 months
   * - ``dorian_akarith_alliance_sign``
     - les bras croisés sur la poitrine
     - arms crossed over the chest
   * - ``dorian_duke_profanation_act``
     - uriner sur un crossentar, le symbole sacré yodique
     - urinating on a crossentar, the sacred Yodic symbol
   * - ``dorian_sheet_motto``
     - La compromission ou la mort
     - Compromise or death
   * - ``druid_name``
     - Diviciacos
     - Diviciacos
   * - ``druid_novel_name``
     - Les sorciers du chaos
     - The Sorcerers of Chaos
   * - ``druid_novel_volumes``
     - 3
     - 3
   * - ``duchess_name``
     - Cassiopée de Thiersonne
     - Cassiopeia de Thiersonne
   * - ``etheric_benediction_necklace_name``
     - Collier éthérique de bénédiction
     - Etheric Necklace of Blessing
   * - ``etheric_manaic_aura_necklace_name``
     - Collier éthérique d'aura manaïque
     - Etheric Necklace of Manaic Aura
   * - ``etheric_stone_skin_necklace_name``
     - Collier éthérique de peau de pierre
     - Etheric Necklace of Stone Skin
   * - ``etheric_vital_force_necklace_name``
     - Collier éthérique de force vitale
     - Etheric Necklace of Vital Force
   * - ``evening_alarm_deactivation_time``
     - 22h
     - 22:00
   * - ``evening_dinner_time_dog_bedou``
     - 19h
     - 19:00
   * - ``evening_garnet_escape_time``
     - 22h40
     - 22:40
   * - ``evening_intrusion_time_garnet``
     - 22h
     - 22:00
   * - ``evening_opal_return_time``
     - 21h30
     - 21:30
   * - ``events_region_name``
     - Thelassar
     - Thelassar
   * - ``family_briefcase_code``
     - 625-993
     - 625-993
   * - ``first_alarm_deactivation_time``
     - 12h
     - 12:00
   * - ``frequency_scanner_book_name``
     - grimoire traceur
     - Tracker Grimoire
   * - ``garnet_rental_location``
     - gîte Les Myrtilles
     - Les Myrtilles guesthouse
   * - ``god_of_diakons``
     - Bahamoot
     - Bahamoot
   * - ``hamlet_near_mlg_manor``
     - Hameau de Wiskons
     - Hamlet of Wiskons
   * - ``heure_ouverture_du_cromlech_le_jour_j``
     - 10h du matin
     - 10:00 in the morning
   * - ``hint_website_name``
     - portail de connaissances (présent sur place)
     - knowledge portal (available on site)
   * - ``inventor_name``
     - Sir Jacques Vaucanson
     - Sir Jacques Vaucanson
   * - ``inventor_nickname``
     - Jacko
     - Jacko
   * - ``khaal_isildis_location``
     - thalassothérapie dans les monts brumeux (près de la frontière Est de Sabarim)
     - thalassotherapy stay in the misty mountains (near the eastern border of Sabarim)
   * - ``kitchen_cook_inspector_meeting_time``
     - 16h
     - 16:00
   * - ``legacy_disease``
     - dégénérescence marbrée
     - Marbled degeneration
   * - ``lg_adventurer_friend_name``
     - Rodok
     - Rodok
   * - ``lg_bank_account_number``
     - AIXJ726H
     - AIXJ726H
   * - ``lg_close_friend_lord_name``
     - Comte Blispin
     - Count Blispin
   * - ``lg_enemy_lord_name``
     - Lord Mac'Jolt
     - Lord Mac'Jolt
   * - ``lg_expedition_end_ago``
     - 6 semaines
     - 6 weeks
   * - ``lg_first_pet_name``
     - Bastet
     - Bastet
   * - ``lg_meeting_end_for_malachite``
     - 12h30
     - 12:30
   * - ``lg_meeting_time_for_amethyst``
     - 11h
     - 11:00
   * - ``lg_meeting_time_for_garnet``
     - 17h
     - 17:00
   * - ``lg_meeting_time_for_malachite``
     - 12h
     - 12:00
   * - ``lg_meeting_time_for_peridot_and_topaz``
     - 15h
     - 15:00
   * - ``lg_meeting_time_for_peridot_topaz``
     - 15h
     - 15:00
   * - ``lg_meeting_time_for_spinel``
     - 16h
     - 16:00
   * - ``lg_remote_friend_lord_name``
     - Comte Adamor
     - Count Adamor
   * - ``lg_vault_secret_code``
     - 603-109 (six sans Troie...sang neuf)
     - 603-109 (sick-oh-free... won-oh-nine)
   * - ``lg_vault_secret_code_location``
     - petite boite à mouchoir
     - small tissue box
   * - ``library_cursed_enclosure_name``
     - Clôture Absolue
     - Absolute Enclosure
   * - ``library_cursed_enclosure_opening_quota``
     - 3 / 5 des vivants
     - 3 / 5 of the living
   * - ``library_initial_events_timedelta``
     - 500 ans
     - 500 years
   * - ``library_initial_events_year``
     - an 500
     - year 500
   * - ``library_outside_portal_remaining_time``
     - 3h30
     - 3½ h
   * - ``link_to_demonic_space``
     - Vortex Abyssal
     - Abyssal Vortex
   * - ``link_to_djinn_world``
     - Source de Savoir
     - Fount of Knowledge
   * - ``lordanian_sheet_motto``
     - Pour la gloire de la Lordanie...
     - For the glory of Lordania...
   * - ``lydia_adversary_name``
     - Mundlish Odalisc
     - Mundlish Odalisc
   * - ``lydia_cousin_name``
     - Isildis
     - Isildis
   * - ``lydia_sheet_motto``
     - La renaissance de Sabarim
     - The rebirth of Sabarim
   * - ``mages_war_before_curse_timedelta``
     - 3 siècles
     - 3 centuries
   * - ``mages_war_name``
     - Guerre des Trente Sorciers
     - War of the Thirty Sorcerers
   * - ``magic_code_enchanted_cauldron``
     - adp
     - adp
   * - ``magic_code_etheric_benediction_necklace``
     - bst
     - bst
   * - ``magic_code_etheric_manaic_aura_necklace``
     - pyw
     - pyw
   * - ``magic_code_etheric_stone_skin_necklace``
     - arx
     - arx
   * - ``magic_code_etheric_vital_force_necklace``
     - hfv
     - hfv
   * - ``magic_code_forbidden_domain_seal``
     - bte
     - bte
   * - ``magic_code_grinding_mill``
     - ecz
     - ecz
   * - ``magic_code_mos_peraty_tomb``
     - kxp
     - kxp
   * - ``magic_code_ring_amplificans``
     - duy
     - duy
   * - ``magic_code_spectral_table_bell``
     - vbr
     - vbr
   * - ``malachite_alibi_location``
     - Square Fleuri de Salima
     - Salima Flower Square
   * - ``malachite_amethyst_encounter_time``
     - 12h45
     - 12:45
   * - ``malachite_spinel_alibi_tavern_name``
     - Perroquet Baveur
     - Drooling Parrot
   * - ``masslavian_sheet_motto``
     - La liberté ou la mort
     - Liberty or death
   * - ``maupertuis_daughter``
     - Mérédice
     - Mérédice
   * - ``maupertuis_daughter_age``
     - 16 ans
     - 16 years old
   * - ``maupertuis_dynasty_founder``
     - Mage Mos Peratys
     - Magus Mos Peratys
   * - ``maupertuis_father``
     - Quirinius
     - Quirinius
   * - ``maupertuis_father_blue_fake_book_code``
     - 425
     - 425
   * - ``maupertuis_father_thanatologue_chest_code``
     - 723
     - 723
   * - ``maupertuis_mother``
     - Isadora
     - Isadora
   * - ``maupertuis_mother_thanatologue_chest_code``
     - 159
     - 159
   * - ``maupertuis_son``
     - Octave
     - Octave
   * - ``maupertuis_son_age``
     - 10
     - 10
   * - ``morning_delivery_trucks_time``
     - 9h et 10h
     - 9:00 and 10:00
   * - ``morning_opal_wake_up_time``
     - 10h45
     - 10:45
   * - ``most_dangerous_radioactive_material``
     - Uranium 234
     - Uranium-234
   * - ``nom_du_conservateur``
     - Camille du Guesclin
     - Camille du Guesclin
   * - ``nom_du_dieu_sanguinaire``
     - Toutatis
     - Toutatis
   * - ``nom_du_guide``
     - Eden Schmitt
     - Eden Schmitt
   * - ``nom_du_héros``
     - Andrea di Revel
     - Andrea di Revel
   * - ``nom_du_musee``
     - Cromlech
     - Cromlech
   * - ``nom_du_reporter``
     - Ryan Parker
     - Ryan Parker
   * - ``nom_du_spectre``
     - Olloudios
     - Olloudios
   * - ``noon_meal_time_lg_opal``
     - 13h15
     - 13:15
   * - ``noon_meal_time_servants``
     - 14h
     - 14:00
   * - ``noon_opal_lydia_call_time``
     - 12h30
     - 12:30
   * - ``notary_birth_date_day_month``
     - 24 novembre
     - 24 November
   * - ``notary_birth_date_year``
     - 1968
     - 1968
   * - ``notary_name``
     - Maestre Ramye Leydelass
     - Maestre Ramye Leydelass
   * - ``oberon_introduction_title``
     - La médiation des Obérons
     - Oberon Mediation
   * - ``obsidian_employer_name``
     - Département de la Défense Sabarite
     - Sabarith Department of Defence
   * - ``obsidian_sheet_motto``
     - Le salut de Sabarim
     - The salvation of Sabarim
   * - ``octave_life_in_archives_delay``
     - 15 mois
     - 15 months
   * - ``old_guru_name``
     - cardinal Tridentès
     - Cardinal Tridentes
   * - ``opal_construction_contractor``
     - LordaBild
     - LordaBild
   * - ``opal_lydia_financial_needs``
     - 18 mégakashes
     - 18 megakashes
   * - ``opal_sheet_motto``
     - L'image d’un homme d’exception
     - The image of an exceptional man
   * - ``parcival_disease_main_remedy_name``
     - Cocktail de Réjuvénation
     - Rejuvenation Cocktail
   * - ``parcival_sick_child_name``
     - Philomène
     - Philomène
   * - ``parcival_woodsman_arrows_metal``
     - Iridium
     - Iridium
   * - ``pere_du_conservateur``
     - Philippe du Guesclin
     - Philippe du Guesclin
   * - ``peridot_topaz_alibi_club_name``
     - Luxor Excelcis
     - Luxor Excelcis
   * - ``phantom_charm_cooldown``
     - 10 minutes
     - 10 minutes
   * - ``phantom_eviction_cooldown``
     - 10 minutes
     - 10 minutes
   * - ``phantom_frenzy_name``
     - frénésie spectrale
     - spectral frenzy
   * - ``phosphorescent_pebbles_name``
     - pierres de lune
     - moon stones
   * - ``physicist_death_circumstances``
     - chez lui, d'une hémorragie cérébrale consécutive à une chute
     - at home, of a cerebral haemorrhage following a fall
   * - ``physicist_discovery_claims``
     - des découvertes révolutionnaires dans le domaine militaire
     - revolutionary discoveries in the military field
   * - ``potion_de_guerison``
     - potion de régénération
     - regeneration potion
   * - ``ring_amplificans_name``
     - Bague Amplificans
     - Amplificans Ring
   * - ``ritualist_kind_name``
     - initiés
     - initiates
   * - ``sabarim_revolution_leader_name``
     - Capitaine Rodimir
     - Captain Rodimir
   * - ``shark_sheet_motto``
     - Le sens du devoir
     - A sense of duty
   * - ``shark_vague_explanations_to_opal``
     - scène de bagarre dans la chambre de Loyd Georges
     - scene of a brawl in Loyd Georges' bedroom
   * - ``small_wooden_fake_book_name``
     - Venture Prins
     - Venture Prins
   * - ``spiritual_orb_name``
     - orbe spirituel
     - Spiritual Orb
   * - ``standard_pentacle_description``
     - pentacle canonique (étoile à 5 branches dans un cercle)
     - canonical pentacle (5-pointed star in a circle)
   * - ``table_bell_name``
     - Clochette Spectrale
     - Spectral Bell
   * - ``teleportation_system_name``
     - corridor planétaire
     - planetary corridor
   * - ``thief_castle_name``
     - Donjon des Pass’muraille
     - Pass'muraille Keep
   * - ``thief_moneybox_name``
     - quêteuse sans fond
     - bottomless collection pouch
   * - ``thief_name``
     - Fédore Pass’muraille
     - Fedore Pass'muraille
   * - ``thief_teleportation_device_cooldown``
     - 30 secondes
     - 30 seconds
   * - ``thief_teleportation_device_name``
     - astrolabe de téléportation
     - teleportation astrolabe
   * - ``thief_teleportation_device_simultaneous_limit``
     - 3 personnes
     - 3 people
   * - ``ultimate_seal_name``
     - Sceau de barrage absolu
     - Absolute Barrier Seal
   * - ``unavoidable_bullet_spell_name``
     - Sacrifice de Zarathoustra
     - Sacrifice of Zarathustra
   * - ``unbreakable_oath_name``
     - Serment de Zarathoustra
     - Oath of Zarathustra
   * - ``videosurveillance_cameras_locations``
     - grand hall, bureau, bibliothèque, salle à manger, cuisine
     - great hall, study, library, dining room, kitchen
   * - ``voluto_secret_lab_address``
     - 145 route du Puy de la Fol, Hameau du Gisant, Alifir Sud
     - 145 Puy de la Fol Road, Hamlet of Le Gisant, South Alifir
   * - ``voluto_suspicious_colleagues``
     - le docteur Marloff du département d'optique appliquée, le jeune physicien Waden Shaw, et le professeur Idn Gark du pôle Energies Nouvelles
     - Doctor Marloff of the applied optics department, the young physicist Waden Shaw, and Professor Idn Gark of the New Energies division
   * - ``waden_blackmailer_lady_country``
     - Balberith
     - Balberith
   * - ``waden_blackmailer_lady_name``
     - Elezie
     - Elezie
   * - ``waden_blackmailing_start_ago``
     - 15 jours
     - 15 days
   * - ``waden_secret_lab_address``
     - dans la cave de la maisonnette n°556, rue Latourbière, Faeran Sud. Il est situé en face d'un Centre Commercial GigAchat, et à 50m d'un îlot de cabines PangeaTelecom
     - in the cellar of cottage no. 556, Latourbière Street, South Faeran. It stands opposite a GigAchat Shopping Centre, and 50 m from a cluster of PangeaTelecom booths
   * - ``waden_sheet_motto``
     - La bête traquée
     - The hunted beast
   * - ``waden_voluto_cooperation_end_ago``
     - 2 mois
     - 2 months
   * - ``waden_voluto_cooperation_start_ago``
     - 8 mois
     - 8 months
   * - ``whispering_box``
     - Boîte à Murmures
     - Whispering Box
   * - ``(empty key)``
     - 16h / 17h
     - 16:00 / 17:00
