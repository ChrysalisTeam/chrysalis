
################################
GAME MASTER'S MANUAL
################################

Fundamental principles of the game
#####################################

Pitch
=====

When night falls over the Maupertuis secret archives, three worlds come alive and intertwine: that of the living, that of books, and that of the dead.

Plunge into this den of art and magic, and break the curse that holds souls prisoner there.

*"The Secret Archives of the Maupertuis" is a mystery evening for 12 players, which lasts about 3-4 hours.*


Detailed concept
=====================

Several groups of adventurers have infiltrated an abandoned underground library, and find themselves trapped there by a mysterious power. At nightfall, the place comes to life, and fills with a multitude of beings, more or less benevolent, more or less enigmatic. Who are these strange characters, captives of the place as well - some phantom-like, others on the contrary far too alive?

This mystery evening puts the emphasis on a slightly unsettling, but above all bewitching atmosphere, in the manner of Pan's Labyrinth, Spirited Away, or Alice in Wonderland. Other possible references: Night at the Museum, the Vatican secret archives, the Cthulhu mythos... For costumes, the aesthetic is mainly somewhere between steampunk and occultism.

The players have one mission sheet per group, and only one or two specific abilities per person (this is not a novelistic game, where the players' personality and backstory are paramount). They are led to get to know one another, to talk with NPC actors brimming with services and secrets, and to solve simple puzzles (searching for items, opening locks, deciphering runes...).

For a good atmosphere, the idea is for the library to be plunged into darkness, lit only by a few lanterns carried by the players or set down next to the NPC actors. A smoke machine and spotlights can be used, in addition to loudspeakers, for even more immersion, or even a few choreographed "Sound & Light" moments.


Story of the game
===========================

{% macro common_npc_tragedy_knowledge() %}

The meeting of the Maupertuis and the Avatars
+++++++++++++++++++++++++++++++++++++++++++++++++++

*Knowledge shared by the Avatars and the phantoms, except the Thief.*

**The library curse began {% symbol "500 years" for "library_initial_events_timedelta" %} before the time of the game, that is to say it took place in the {% symbol "year 500" for "library_initial_events_year" %} of the {% symbol "Era of the Great Appeasement" for "current_era_name" %}. We are currently in the {% symbol "year 1000" for "current_events_year" %} of this era of prosperity.**

The child, **{% symbol "Octave" for "maupertuis_son" %} de Maupertuis**, met a tragic fate. Through his mother (**{% symbol "Isadora" for "maupertuis_mother" %}, née Guerlevan**) and his father (**{% symbol "Quirinius" for "maupertuis_father" %}**), he was descended from two great lineages of healer-mages. His parents died when the estate was attacked and razed by followers of the **god {% symbol "Bahamoot" for "god_of_diakons" %}**, on the orders of **{% symbol "Cardinal Tridentes" for "old_guru_name" %}**, during the {% symbol "Planetary Cataclysm" for "catastrophic_period" %}. {% symbol "Octave" for "maupertuis_son" %} was **{% symbol "10" for "maupertuis_son_age" %} years old** at the time. His sister, **{% symbol "Mérédice" for "maupertuis_daughter" %}**, who was **{% symbol "16 years old" for "maupertuis_daughter_age" %}**, disappeared during these events.

During the attack, {% symbol "Octave" for "maupertuis_son" %} had taken refuge in the underground archives, with his tutor **{% symbol "Master Parchemine" for "archivist_name" %}** (who did not practise magic). The magic portal linking the manor to this library (located very far below the surface) had been destroyed during the attack, but secondary portals remained, leading to ancient mages' castles - all in ruins - scattered across the planet. These portals had been enchanted for centuries to open on a single day each year, at the **{% symbol "winter solstice" for "astral_opening_date" %}**, for a shared celebration of the new year, even though this tradition had long since ceased to be observed.

The two survivors lived there alone for **{% symbol "15 months" for "octave_life_in_archives_delay" %}**, the tutor judging that {% symbol "Octave" for "maupertuis_son" %} was not yet ready to face the harshness of the outside world. They could not enter the library's "Forbidden Domain", guarded by a Beast, because Octave, unlike his sister, had not yet received the initiation allowing him to open the passage to this holy of holies. {% symbol "Master Parchemine" for "archivist_name" %} took on the role of archivist to pass the time, and began an inventory of the accessible "non-weird" books. {% fact "archivist_began_cataloging_books" %} Lonely, the child took refuge in reading fantasy novels, reading and re-reading his favourites, and forging an ever-stronger bond with the heroes of these works.

Under the influence of the magic saturating the place, and of Octave's insistent wishes, several imaginary characters actually became embodied in the library, thus becoming what are known as **"Avatars"**: an inventor, a druid, a duchess, a samurai, a knight, a biplane pilot...

The child and his new friends met at least one day each week in the library, to feast, play, build automatons, and learn a great many things about the rules governing each of the universes represented.
The Archivist soon discovered them, but had little choice but to accept the situation, while forbidding the Avatars to leave the library.

A few months later came the next **{% symbol "winter solstice" for "astral_opening_date" %}**. **The Arkon (paladin-exorcist) {% symbol "Valerias" for "arkon_name" %}**, of the Yodic religion (and more specifically of the Mithraite denomination), who resided in the **{% symbol "Rochesombre Monastery" for "common_monastery_name" %}**, sensed the presence of non-human souls. He infiltrated the secret library, and confronted the Archivist and the child, who were preparing to leave it.

These two finally agreed to stop putting humanity at risk with an unnatural mixing of the worlds, and to let the Arkon banish the Avatars from Earth for good; in return, the Arkon would take {% symbol "Octave" for "maupertuis_son" %} and the Archivist with him, to safety, in a welcoming country.

After heart-rending farewells, the imaginary characters each returned to their own universe, waiting for the ritual to close off their access to the world of humans.


The return of the Avatars
+++++++++++++++++++++++++++++++++

*This knowledge belongs to the Avatars alone.*

Some of the Avatars did indeed see the interdimensional passage close. But for three of them - **the Inventor {% symbol "Sir Jacques Vaucanson" for "inventor_name" %} (whom everyone calls {% symbol "Jacko" for "inventor_nickname" %}), the Druid {% symbol "Diviciacos" for "druid_name" %} and the Duchess {% symbol "Cassiopeia de Thiersonne" for "duchess_name" %}** - this was not the case. Their respective imaginary worlds remained connected to the world of the living.

When they came back to the library to find out what had happened, they found the pentacle still in place, a few traces of spells and fighting (softened by the magical protections of the furniture); and, to their horror, the Arkon's **skull-less skeleton** lying in a corner amid his weapons; as well as some ashes - probably those of the child and his tutor - in other spots.

Grief-stricken, these remaining Avatars created a makeshift **graveyard** for the remains of the deceased. They **argued fiercely** over what place to give the Arkon's bones, for while the Druid held him responsible for the massacre, the Duchess and the Inventor thought it could have been an accident, or the doing of some other entity. Giving the benefit of the doubt, they finally left all the remains together in the graveyard.

The Avatars then investigated the whole of the library's authorised floor, but in vain, as they knew far too little about this world's magic. They found only a few fake books and locked caskets, which they were unable to open. The passage to the Forbidden Domain, for its part, was still blocked by the age-old spell of the Maupertuis. And there was no way to reach the surface, even at a later {% symbol "winter solstice" for "astral_opening_date" %}. {% hint "beast_snack_as_moon_stones" is needed %}

The Duchess, in her own world, received from a soothsayer the revelation that the recently deceased were still prisoners of the library in the form of phantoms, but that on a forthcoming anniversary of the tragic event, this curse would be broken. Since then, every year, the Avatars gather for an **{% symbol "Otherworld Banquet" for "banquet_name" %}** in honour of the Maupertuis, awaiting the fulfilment of this crucial prophecy.

{% endmacro %}
<{ common_npc_tragedy_knowledge }/>


Plot background (SPOILER)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

One of the Avatars, the Druid with superhuman powers, had in fact become the great villain in his own universe; the child did not know this, having never found the last volume of the series. This former hero, wishing to take control of this universe as well, came back through said Volume, murdered the living during the ritual, then feigned surprise before the remaining imaginary characters, who came back later to find out what had happened.

Realising the scourge that threatened the world of humans, the Arkon had nevertheless managed, with his dying breath, to cast a spell on the traitor; a spell that trapped the entire library in a "black hole" of the spirit world: whether one is a real human or an imaginary character, one could henceforth enter it, but not leave, for as long as the traitor remained "alive". The three humans thus remained trapped as phantoms (spectres becoming embodied at times) in this place; as did the novel characters, who can however still come and go between the underground library and their own literary world.

Besides their own objectives, the players must therefore learn the difference between these various types of protagonists, and find a way to unmask and destroy the traitor, in order to bring the curse to completion and free the wandering souls.

Fundamental principles of the different worlds
==============================================

{% macro explanation_of_different_worlds() %}

The world of the living
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

It is an alternate history of our own world; everything that happens before 1908 is identical to ours, then a tectonic and climatic "great cataclysm" occurred, which turned everything upside down for centuries. Scientific laws and human psychology are identical to our world, with the addition of "magic".

- The living can see and hear the characters of the world of the dead as well as those of the world of books, and can touch the characters of the world of books.

- For a living person, any contact with a disembodied, wandering phantom is very dangerous. An embodied phantom, on the other hand, is harmless, and passes through the living without affecting them. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- The living are by default vulnerable to physical, magical and sacred attacks.

- The living are subject to the rules of the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}". {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

The world of the dead
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

It is represented by the humans or beasts who died in the library after its curse, and therefore cannot pass on to the afterlife.

- The dead can see and touch one another, but cannot harm each other. Embodied phantoms can "push back" their disembodied fellows.

- The dead can neither see, hear, nor sense the characters of the world of books.

- At no time can the dead interact with the objects of the living world. The only exception is the buffet, which is made up of dishes and drinks compatible with all worlds.

- When it touches a living person, any disembodied, wandering phantom injures them dangerously. An embodied phantom, on the other hand, is harmless, and passes through the living without affecting them. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- Only sacred attacks can reach the dead, not physical or magical attacks. But since at present they cannot escape the library, if they are injured, they invariably come back later, in a madder and more aggressive form.

- Phantoms are subject to **complex rules of wandering, embodiment and anchoring**, see the chapter on this subject.

- Phantoms are NOT subject to the rules of the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}". {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{# NOT YET - "Demonic" entities, also part of the world of the dead, could be invoked in this context. They would then have the same properties as phantoms, with more freedom, hostility, and magico-sacred powers. #}

The world of books
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The characters from the literary, imaginary world are solely novel heroes whom the child Octave brought to life because he admired them particularly. They are also called "\ **Avatars**\ ".

These characters are in the state their authors left them in at the end of their respective "stories", and not according to what the child knows/imagines about them. They do not age.

They each return to their parallel world through their books, whenever they wish. Time flows identically in all worlds, but in their books, the Avatars live in an "eternal present", where their situation is broadly unchanging, since their author has stopped writing.

- If the Avatars die in the real world, this is equivalent to a death in their imaginary world (a death subject to their own system of religious beliefs); they are then projected back there, and do not become phantoms in the real world.

- They can interact freely with the world of the living, its humans and animals, its objects and grimoires; **except with the "novels"**, which they cannot move, because these books carry an entire universe within them. {% fact "avatars_cannot_carry_novels" %}

- They can neither see, hear, nor sense the characters of the world of the dead, and have nothing to fear from their touch (whether in embodied phase or not).

- These Avatars wear their "typical" costumes and accessories from their novels, those they had when Octave involuntarily summoned them.

- They cannot bring back any other object or individual from/to their world of origin (not even decorative accessories). They are therefore, in all things, limited to what the Maupertuis library contains.

- They cannot go into the world of other Avatars, nor welcome living people or phantoms into their own world.

- They mostly retain the superpowers they possess in their own universe (regeneration, strength, spells...)

- They are vulnerable to physical and magical attacks, but the sacred (and the world of phantoms) does nothing to them, because their "transcendence" is not the same as that of humans.

{# but with risks of dangerous side effects, due to incompatibilities between the fundamental laws of the universes; in the present case, { % fact "avatar_abilities_are_randomly_hazardous" % } #}

- They are NOT subject to the rules of the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}", and may indeed cheerfully make fun of it, by swearing all sorts of far-fetched things. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

The world of automatons
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*The logistics assistants, photographers, and buffet servers would do well to belong to this world, for added atmosphere and a good freedom of action.*

With Octave's help, the "Inventor" Avatar had designed automatons able, for instance, to wait at table. These are purely mechanical entities, devoid of any consciousness and of any magical power. Some can speak and understand simple orders; other automatons are limited to very specific tasks such as serving food and drinks, or doing the cleaning. {% fact "inventor_has_built_androids" %}

To be more easily distinguished from the Avatars, besides their gait and speech, the automatons must wear **{% symbol "white ribbons" for "automaton_symbolic_cloth" %}** around their neck and wrists. {% hint "white_ribbon_cloth_for_automatons" is needed %}

They obey only the character (NPC actor or player) wearing a **wide silver bracelet called the {% symbol 'Dominion' for 'androids_command_bracelet_name' %}**. They respond to the wearer's orders as best they can, as long as these fall within their abilities, and do not directly contradict their innate rules of non-aggression and survival. *If in doubt about how to react to a difficult order, simulate the automaton's hesitation or incomprehension, and discreetly ask the Game Master.* {% fact "robots_obey_but_refuse_violence_or_sacrifice" %}

The robots see the living and the Avatars, but NOT the phantoms. They are visible to all.

They are generally slow and rigid in their movements. But they have **immense physical strength**, and can therefore move ULTRA-HEAVY objects on request. In a brawl, they would easily win against a human.

They are vulnerable to physical and magical attacks (except poisons, of course), but not to sacred attacks (e.g. from phantoms).
More precisely, they fear explosives and sword blows, but have little to fear from projectiles (bullets or arrows).

Possible typical roles (an automaton may switch roles during the game):

- Cleaner automaton (1 feather duster is available)
- Server automaton for drinks and dishes
- Butler automaton, who wants to take the players' coats and give them a tour of the authorised floor
- Singer automaton (a cappella, or plan for some instrumental music)
- Joker automaton (prepare 5-6 non-contemporary jokes to tell on request)
- Encyclopedic automaton (makes up a whole far-fetched speech when asked for information)
- Photographer automaton

Ideas for possible interactions for some automatons:

- They keep repeating a few stereotyped sentences to the players, even when irrelevant.
- They dust not only the shelves, but also the other characters.
- They carry lamps and follow the players who ask them to.

Typical lines:

- "Welcome to our humble abode"
- "Does Sir/Madam desire anything?"
- "Deign to taste these most costly sweetmeats"
- "Pray accept this delightfully quaffable beverage"
- "May I relieve you of your coat?"
- "I serve the Maupertuis lineage and it is an immense joy."
- "On your left, the tomb of the greeeeat Magus Mos Peratys, founder of the lineage..."

They may malfunction at times, until the Inventor Avatar or a player unjams them:

- They stutter, bump into walls and obstacles, get their arms stuck in one another's, or move oddly on the spot in "faulty gear" fashion...
- They may end up in a logical deadlock, constantly wanting to give way to another automaton: "No, no... After you... I wouldn't dream of it...".

Special role: **the sentinel automaton**, armed, which patrols the library to protect it against possible assailants (see its NPC sheet, and its scheduled interventions).

The automatons are NOT subject to the rules of the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}". {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{# NOPE NOT FOR NOW
  When, much later, the players manage to access the {% symbol "Thanatologue" for "book_of_the_dead" %}, it is POSSIBLE to trigger an intense soundtrack upon the first opening of this cursed grimoire.
  The serving automatons then become possessed, and limp towards the players, flailing their arms, and repeating "Death to the heretics!".
  The players must then avoid them until the end of the soundtrack; at that point, the automatons return to normal, and resume their usual tasks.
#}

The divine world
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The entities belonging to the "\ **divine**\ " - the NPC actor **the Ankou**, and the Game Master as the **renegade Djinn** - can see everyone and be seen by all, and are by default harmless to the various characters.

They are also immune to weapons and to the spells (including the {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %}) surrounding the library. {% fact "ankou_sees_all_and_is_harmless_for_all" %}

They are NOT subject to the rules of the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}". {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{% endmacro %}
<{ explanation_of_different_worlds }/>

Player teams
==================

It all begins when Heliossarian explorers (those present in the game), searching for the secrets of the Maupertuis, unearth monoliths covered in ancient inscriptions. Unfortunately for them, pictures of their find leak out, and make the rounds of the world press; a few groups of people turn out to be able to decipher it, and thus to understand how the portals leading to the Maupertuis library work, portals that are active at the coming **{% symbol "winter solstice" for "astral_opening_date" %}**. All these people hasten there on that date, for different reasons, without realising that they are thereby throwing themselves into the lion's den.

The Heliossarian explorers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These 3 adventurer-archaeologists are trying to protect their country, Heliossar, against the renewed appetite for conquest of their powerful neighbour, the Akarith Theocracy. They have learnt that the Akariths had got hold of a copy of the legendary {% symbol "Thanatologue" for "book_of_the_dead" %}, the Book of the Dead of a vanished civilisation, and had drawn from it a plan for an "inevitable" invasion of Heliossar. They are therefore searching for the copy that the Maupertuis, according to legend, possessed, in order to understand and above all thwart this plan of conquest.

Their abilities are oriented towards the physical and human sciences.

{% macro explorer_group_symbols() %}
The identifying garment of the Heliossarian explorers is a **beige belt** *(provided by the organisers)*.

Their motto is **"Knowledge is power"**, pointing the index finger towards the sky.
{% endmacro %}
<{ explorer_group_symbols }/>

The Parcival family
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These 3 brothers and sisters are the distant descendants of Mérédice de Maupertuis, Octave's sister, whom everyone believed to have died with her family, but who had in fact managed to escape and rebuild her life.

These Parcivals read in the autobiography of their ancestor Mérédice how her parents, healer-mages, had cured her of a great hereditary illness, marbled degeneration, thanks to a "{% symbol "Rejuvenation Cocktail" for "parcival_disease_main_remedy_name" %}". When their little sister fell ill in turn (she has only a few weeks left to live), they set out in search of the remedy, and their investigation led them to the buried archives of the former family estate.

Their abilities are oriented towards nature and magic.

{% macro parcival_group_symbols() %}

The coat of arms of the Parcival family is a **gnarled staff around which a single snake is coiled**.
{% fact "coat_of_arms_of_parcival_is_partial_caduceus" %}

Its identifying garment is a **royal-blue jabot** *(provided by the organisers)*.

Its motto is **"Noble of heart as of blood"**, with the fist clenched over the heart.
{% endmacro %}
<{ parcival_group_symbols }/>

The Diakons of {% symbol "Bahamoot" for "god_of_diakons" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These 3 monks officiate in the worship of the god {% symbol "Bahamoot" for "god_of_diakons" %}, which is deeply rooted in the region. The oracle of their monastery sensed that a soul drunk with hatred was in the ruins of the Maupertuis manor (this is the Beast), as well as wandering souls (the phantoms). They therefore go there to solve the problems, and protect the order of things.

{# **They also have orders to magically destroy the 3 "malefic" books contained in the Maupertuis Forbidden Domain, for fear that they fall into the wrong hands (the library cannot simply be burnt)?** NOPE #}

Their abilities are oriented towards theology and esotericism.

{% macro diakon_group_symbols() %}
The identifying garment of the Diakons of {% symbol "Bahamoot" for "god_of_diakons" %} is a **purple stole** (a scarf worn across the chest).

Unless specifically instructed otherwise, during rituals and processions, the Diakons keep their hands joined by the fingertips, palms apart, as if holding a globe between them; this is their prayer sign. When moving in procession, they drone a slow, guttural **"ohhhhm" sound**.

During rituals, they like to **proclaim their invocations loudly**, with emphasis.

Their motto is **"The dragon is our guide"**, to be professed with hands joined in prayer, once again.

{% endmacro %}
<{ diakon_group_symbols }/>

The Mirandian secret agents
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The autonomous island of Mirandia, and its strategic position at the centre of the Diorian Ocean, have aroused the greed of its neighbours. Trapped by economic plots, hopelessly in debt, the island is about to be annexed and sold to the highest bidder.

These 3 state agents have therefore moved heaven and earth to find the mythical (and "dangerous") treasure of the Maupertuis family, and thus save their homeland from bankruptcy.

Their abilities are oriented towards "technosteam gadgets".

{% macro spy_group_symbols() %}
The identifying garment of the Mirandian secret agents is an **emerald-green armband** *(provided by the organisers)*.

Their motto is **"Mirandia forever shall shine"**, with a military salute, hand against the temple.
{% endmacro %}
<{ spy_group_symbols }/>

NPC actors
==========

**These roles can be played as male or female, adapting names and titles where necessary.**

Octave de Maupertuis (the child)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_octave_character_summary() %}

- PHANTOM

- Traits: candour, spontaneity, enthusiasm, affection

- Octave does not know how he died, nor why he is a prisoner of this place, nor why he is anchored to a specific spot.

- Excited to learn that the players have met his tutor (the child already knew from the Ankou that he too is a prisoner as a phantom), and eager to see him again as soon as possible.

- Passionate about fantasy literature and other books.

- "My parents told me never to talk to strangers. So did {% symbol "Master Parchemine" for "archivist_name" %}. But I'm far too bored, so never mind"

{% endmacro %}
<{ phantom_octave_character_summary }/>

{# MEH
**A diary somewhere?**
**If he reaches the child's nook (with toy and plush), he gives more information?**
#}

{% symbol "Master Parchemine" for "archivist_name" %} (Octave's tutor and archivist )
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_archivist_character_summary() %}

- PHANTOM

- Traits: joviality, wisdom, benevolence, paternalism, meticulousness

- Wise and somewhat learned, but has very little knowledge of magic.

- He mainly taught Octave the humanities (sciences, letters...), leaving it to the parents to pass on their heritage as mages.

- He took advantage of their initial confinement in the library, following the sacking of the manor, to take on the role of archivist, and begin sorting the authorised floor. He simply took care not to handle the suspicious-looking grimoires. {% fact "archivist_began_cataloging_books" %}

- The tutor does not know how he died, nor why he is a prisoner of this place (he suspects a betrayal by the Arkon), nor why he is anchored to a specific spot.

- He kept a small **logbook** during their confinement, which must be somewhere in the library. {% fact "archivist_began_diary_during_confinement" %}

- Excited to learn that the players have met the child (the tutor already knew from the Ankou that he too is a prisoner as a phantom), and eager to see him again as soon as possible.

- Openly wonders whether it might be his unfinished work of inventorying and fully tidying the library that is holding him back in this world.

- Makes sure of the players' initial good will (potentially thanks to the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}"), then helps them by lavishing on them a great deal of advice, and information about the place.

{% endmacro %}
<{ phantom_archivist_character_summary }/>

{# MEH
**Weakness when facing villains: adores books: will do anything asked of him if a book is threatened**
**No longer knows how the library is arranged,**
**Can find the boy's borrowing record: this record lists the NPCs' books, in particular the volumes the villain comes from.**
#}

The Arkon {% symbol "Valerias" for "arkon_name" %} (the legendary paladin-exorcist)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_arkon_character_summary() %}

- PHANTOM

- Traits: wariness, sense of duty, good will, intelligence, sternness

- "Arkon" is a title designating a "knighthood blessed by the gods" in the so-called "Yodic" religions

- The Arkon remembers his death in single combat, and casting the curse on the library. He knows he is mystically bound to the area of his violent death.

- Both full of hope at seeing adventurers here, and at the same time worried that they will all end up, through his fault, dead and locked in like the others.

- Somewhat disillusioned to see that the pagan worship of the god {% symbol "Bahamoot" for "god_of_diakons" %} has ended up replacing his own (the Yodic faith of the Mithraite denomination), in the monastery on the surface

- Demands to be able to make his "{% symbol "mission confession" for "arkon_mission_confession" %}" to a prelate of the Yodic religion, and only in that case does he reveal everything he knows about the situation; only helps the players he trusts to carry out his mission of protecting humanity (and who are not simply going to lift the library's confinement, thereby destroying his efforts)

{% endmacro %}
<{ phantom_arkon_character_summary }/>


The Thief {% symbol "Fedore Pass'muraille" for "thief_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_thief_character_summary() %}

- PHANTOM

- Traits: greed, cunning, glibness, incredulity, distrust, alcoholism, vanity

- Story: 60 years after the curse fell upon the library, he infiltrated it, hoping to plunder its secrets; in particular the legendary **Maupertuis treasure**, and the mysterious **{% symbol "Fount of Knowledge" for "link_to_djinn_world" %}**. On the way, he picked up **only the Arkon's gladius**. {% fact "arkon_bag_disappeared_just_after_his_death" %} He managed to bypass the magic barrier blocking access to the Forbidden Domain, thanks to a **{% symbol 'teleportation astrolabe' for 'thief_teleportation_device_name' %}** (retrievable from his remains). But he was taken by surprise and killed by the Beast - still alive at that time - which guarded the place. {% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}

- The Thief is initially unaware that he is dead; he merely believes himself **trapped** in his little area (near the Beast's den) by the masters of the place. He therefore calls out to the players to **free** him from his anchoring, and to help him recover the equipment that someone *odiously* stole from him. This can give rise to a give-and-take negotiation.

- He continues to desire only material riches, which, alas, he can no longer pick up despite his attempts. Even if the players swear a "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}" to convince him that he is dead and that his priorities are illogical, he still shows doubts (perhaps these people have an immunity against the effects of this oath?).

- Following the Arkon's harangues, or even the Ankou's visits, he eventually realises that he is dead. But that changes nothing: after discussions with the players (some have information), he exults that the **"{% symbol "Pass'muraille Keep" for "thief_castle_name" %}"** has remained in his family ever since. He therefore glories in still being able to feed this pile of riches, even once dead, through his magic "{% symbol 'bottomless collection pouch' for 'thief_moneybox_name' %}". {% fact "arkon_and_ankou_try_to_persuade_thief_that_he_is_dead" %} {% fact "thief_heirs_still_benefit_from_his_treasure" %}

- He sells his information about the place dearly to the other explorers of this library, in exchange for gold and gemstones.

{% endmacro %}
<{ phantom_thief_character_summary }/>

The Ankou (the guide of souls, the "psychopomp")
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro god_ankou_character_summary() %}

- DIVINE (formerly a human phantom, but promoted by the gods)

- Traits: exasperation, outspokenness, colloquial language, sarcasm, good will,

- He is a dark but rather comical character, with little information to contribute but allowing dialogue to be created with the other NPC actors, and a link to be made with deceased ancestors.

- He only passes briefly through the library while doing his rounds, then can be "invoked" by the players to continue interacting.

- He informs the players that the phantoms are abnormally **prisoners** of this place, and cannot pass on to the afterlife; and that the players themselves are now locked in too.

- He wields cold irony ferociously, deadpan style; if for instance a Parcival dies, he asks them again what their initial mission was (saving their sick little sister), and whether they feel satisfied with the result.

- "What are you so freaked out about, you humans hiding behind the shelves! You think I can't see you? I'm not a psychopath, you should be thanking me instead, without me you'd look pretty silly trying to reach the kingdom of the dead! Come on out, as long as you don't come pawing at me, you've got nothing to fear from me! As if I'd give myself extra work by bumping off humans who've done nothing to me, in this place that's already cursed! And what did you come here for anyway, as if it wasn't already enough of a shambles!"

- "What do I look like, at the inter-spiritual meetings!? Every time I get ribbed, like <so, that Maupertuis business, still no progress?>. I've got a reputation to keep up, me! Phantoms squatting in a vault for centuries, it doesn't look good! Not to mention the critter upstairs! It's against the order of things, so let everyone pull their weight to figure out what's wrong!"

- During the final scene, on the other hand, he keeps quiet and lets the solemnity of the event take over; but he can, at the very end, throw in a "Hey guys, let's hurry it up now, I've got a group of Keroskian tourists who've just gone and petted some sabre sharks, so my day's not over yet!"

{% endmacro %}
<{ god_ankou_character_summary }/>

The Beast (the guardian ghoul of the Forbidden Domain)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_beast_character_summary() %}

- PHANTOM (formerly a "cave ghoul", enchanted by the Maupertuis so as not to need to feed)

- Traits: aggressive, sly, non-communicative

- Hired by Octave's parents to guard the most dangerous grimoires, in the Forbidden Domain

- The seal protecting the Forbidden Domain prevented the Beast itself from coming into the authorised area of the library

- Recognises no one as a friend (only Octave's parents and Mérédice had power over it; neither the tutor nor Octave would have been spared had they entered the Forbidden Domain)

- Died of old age more than a century after the library curse, and became even more ferocious from wandering aimlessly in the Forbidden Domain

- Has a genuine **addiction** to {% symbol "moon stones" for "phosphorescent_pebbles_name" %} (phosphorescent pebbles) {% fact "beast_is_addicted_to_moon_stones" %}

- Its species and characteristics must remain somewhat mysterious to the players, in order to heighten the anxiety, and force them to react quickly to find solutions when it appears.

- **The Maupertuis parents, questioned from the afterlife, can give pointers on how to neutralise it**

{% endmacro %}
<{ phantom_beast_character_summary }/>

The Druid {% symbol "Diviciacos" for "druid_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_druid_character_summary() %}

- NOVEL HERO (title "{% symbol "The Sorcerers of Chaos" for "druid_novel_name" %}", in {% symbol "3" for "druid_novel_volumes" %} Volumes)

- Traits: gentle, discreet, learned, friend of plants and beasts

- Built a little "jungle" nook with the plants of the place, where he taught the child harmony with nature

- He is the "real villain"

- In the first 2 volumes of his novel, he travels the world to defeat the dark sorcerers who control each continent. But in the 3rd volume, after killing the last sorcerer, he reveals his true nature and becomes the Guide of Gaia, who subjects the planet to a brutal "Back to Nature" utopia.

- He is very skilful, has magical powers, resists magic and poisons (as well as the sacred, of course), and regenerates his body very quickly when injured.

- He can use his **sea-blue blood**, with the help of the spirits of Nature, to heal all kinds of biological ailments (he must mime slashing his forearm in order to heal). {% fact "druid_can_well_heal_biological_injuries_with_his_blue_blood" %} {% hint "blue_blood_for_druid_healings" is needed %}

{# NOPE - **Knows about NECROMANCY?** #}

{% endmacro %}
<{ avatar_druid_character_summary }/>

The Inventor {% symbol "Sir Jacques Vaucanson" for "inventor_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_inventor_character_summary() %}

- NOVEL HERO (title "{% symbol "The Ballet of the Automatons" for "avatar_inventor_novel_name" %}", in a single Volume)

- Traits: extraversion, good manners, refined language, dynamism

- Designed the library's automatons

- He can cobble together a mechanical prosthesis to replace a lost limb {% fact "inventor_can_well_heal_missing_limbs" %}

{% endmacro %}
<{ avatar_inventor_character_summary }/>

The Duchess {% symbol "Cassiopeia de Thiersonne" for "duchess_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_duchess_character_summary() %}

- NOVEL HEROINE (title "{% symbol "The Pond Swans" for "avatar_duchess_novel_name" %}", in a single Volume)

- Traits: distinguished, sensitive, pious, protective, enterprising

- Is able to enter into synergy with other "seers"

- She can invoke her own gods, with the help of the {% symbol "initiates" for "ritualist_kind_name" %} present, to heal a sacred injury {% fact "duchess_can_well_heal_sacred_injuries" %}

{% endmacro %}
<{ avatar_duchess_character_summary }/>


Locations
=========

Lower floor (normal library)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- The Archivist's nook (facing the staircase)

- The child's nook

- The Arkon's nook

- The mini-jungle that the Druid and the child had created

- The magic dinner buffet of the four worlds

- The pentacle of the Arkon's unfinished ritual.

- The graveyard (rudimentary graves of the child, the Archivist and the Arkon)

- Various chests and objects scattered around the place, as well as "markers" placed on the floor by the Avatars during their fruitless investigations

Upper floor (Forbidden Domain)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*Access initially blocked for everyone.*

- The Thief's nook

- The Beast's den

- The chest with the {% symbol "Thanatologue" for "book_of_the_dead" %}

- The alchemy workshop

- The gemmology workshop

- Various traps and artefacts scattered among the shelves


.. raw:: pdf

   PageBreak


Course of the game
##########################################

Dangers and injuries
==========================

The different types of injuries
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro injury_types_knowledge() %}

The assaults an unlucky adventurer is liable to suffer fall into three categories: **physical, magical and sacred attacks**.

Physical attacks (cutting, blunt, piercing, toxic weapons...) and magical attacks (fire, ice or other spells, but also injuries resulting from magically bewitched objects...) must be parried by different means, but the resulting injuries are of the same nature: **biological**. The same medical care, the same potions, can therefore rescue the victims of these ailments.  {% fact "cursed_objects_give_magic_and_not_spiritual_injuries" %}

Sacred attacks, on the other hand, typically arising from contact with phantoms or demons, or with their cursed remains, cause injuries of a **spiritual** nature. Although the symptoms are close to those of biological ailments (tetany, blindness, unusable limb...), only the interventions of mystics can promptly repair the damage inflicted on the soul. Potions can also be useful in this case, but only by providing the celebrants with more energy and concentration for the performance of their blessing ritual. {% fact "potions_cannot_heal_spiritual_injuries" %} {% fact "cursed_skull_and_bones_give_sacred_injuries" %}

The distinction between these different types of injuries is not always obvious; for instance, the paralysis of a limb may be due to internal lesions just as much as to the attack of a spectre. Hence the need to investigate the circumstances that led to the observed disorders, in order to provide an appropriate remedy.

One point to note: just as "biological" injuries, even when healed, leave after-effects in the body, so "spiritual" injuries weaken the foundations of the soul.

**Suffering two injuries in a row, of whatever nature, therefore almost certainly leads to death.** {% fact "second_injury_sustained_is_always_fatal" %}

{% endmacro %}
<{ injury_types_knowledge }/>

In practice: the possible cases during the game
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro injury_cases_and_remedies() %}

A player can be harmed in the following cases:

- If they are touched by a phantom in disembodied phase (in spectral wandering): **sacred injury**. If they are attacked at length by the phantom Beast, or stand in a phantom's way instead of fleeing, it ends up killing them. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- If they touch a cursed object, such as a sounding skull or the bones that go with it {% fact "cursed_skull_and_bones_give_sacred_injuries" %}: **biological injury**. A pentacle, for its part, is NOT dangerous, except during a ritual. {% fact "pentacle_is_not_harmful_oustide_rituals" %}

- If they set off a physical or magical trap, that is to say knock a **jingle bell** to the floor (e.g. a thread stretched across an aisle) or trigger the chirp of a presence-detecting **cicada** (e.g. by opening a chest): **biological injury**.
 {% fact "cicada_or_minibell_sound_mean_injury" %}

- If they enter the tomb of the {% symbol "Magus Mos Peratys" for "maupertuis_dynasty_founder" %} without being a Parcival heir, and are touched by the Magus's mummy: **death**. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

- If they drink a dangerous potion, or are hit by an enemy spell, etc.: **biological injury**.

**Injuries translate into a penalty at the GM's discretion, depending on the situation: losing a limb or just the use of it, becoming mute, losing one's memory, becoming breathless and unable to run (in case of poisoning), or no longer being able to use certain abilities...**

**IMPORTANT: a second injury, whether of the same nature or not, sustained during the game, kills the player.** {% fact "second_injury_sustained_is_always_fatal" %}

{# NOPE
The players are supposed to look among themselves for ways to heal, thanks to magic potions and the Diakons' rituals, but these possibilities remain very limited.
#}

The players are, by themselves, very helpless in the face of the various injuries; they have NO abilities in this respect. {% fact "players_have_no_medecine_abilites" %}

**Healing by Avatars**: Depending on their type, injuries can be healed by some of the Avatars present. The Avatars must first leave the player with their injuries for a few minutes, long enough to "gather what is needed to heal them". Then they proceed with an operation or a ritual - **to be invented for the occasion**.

{# NOPE FORGET THAT FOR NOW
but beware, these interventions have **a 1 in 6 chance of failing dramatically** (then leading to the player's death - roll a die for it with the Game Master){ % fact "avatar_abilities_are_randomly_hazardous" % }.
#}

- The **Duchess** can invoke her own gods, with the help of the {% symbol "initiates" for "ritualist_kind_name" %} present, to repair a sacred injury (affecting the soul). {% fact "duchess_can_well_heal_sacred_injuries" %}
- The **Druid** can use his **sea-blue blood**, with the help of the spirits of Nature, to heal all kinds of biological ailments. {% fact "druid_can_well_heal_biological_injuries_with_his_blue_blood" %} {% hint "blue_blood_for_druid_healings" is needed %}
- The **Inventor** can cobble together a mechanical prosthesis to replace a lost limb. {% fact "inventor_can_well_heal_missing_limbs" %}

**If a player dies, they become a phantom**; they are however constantly embodied, and immediately free to move about, unlike the NPC phantoms. They nonetheless remain subject to the same barriers as all the protagonists ({% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %} encircling the library, {% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %} blocking access to the Forbidden Domain...). They can no longer handle objects (not even an abilities touch tablet), but they keep the knowledge they have acquired. Their phantom status allows them to access the trapped corridors and other places dangerous to the living without any problem.

With the right ritual from the {% symbol "Thanatologue" for "book_of_the_dead" %} grimoire, it is possible to **resurrect a player** as a **zombie** for a few hours; the player then recovers all their capabilities, but they must adopt the posture and speech of an "old-fashioned zombie" (e.g. they speak oddly, may stagger while walking, but cannot run...). {% fact "players_have_thanatologue_spell_to_summon_zombies" %}

{% endmacro %}
<{ injury_cases_and_remedies }/>


Events that pace the game
==========================

{% macro early_game_events() %}

Briefings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Before the game, group briefings and then a collective briefing take place with the players.
*See the detailed schedule sheet on this subject.*


The players' entrance
++++++++++++++++++++++++++++++++++

A speech by the Game Master introduces the start of the game.

Each group is then led, by an automaton, to a different spot on the lower floor of the library, with introductory music.

As a reminder, the library is holding its annual celebration today, as it has every year for 1000 years. The automatons (once designed by the Inventor and Octave) start bustling about to organise this celebration; some may initially be "switched off", seated or on the floor, waiting for the Inventor Avatar to turn them on.

At this point, the phantoms all move about in their disembodied form.

Some Avatars may already be present (for instance the Duchess praying in the graveyard, the Druid in his mini-jungle, the Inventor repairing an automaton), awaiting the opening of the buffet.


The opening of the Otherworld Buffet
++++++++++++++++++++++++++++++++++++++++++++

Lively music starts up, and the Inventor comes to the banquet, loudly calling on his friends from the imaginary world to join him in raising a toast to Octave and the Archivist, and in hoping together for the lifting of the curse.

The other Avatars converge, the players who were nearby get harangued too, and are swept up in this mixture of assorted declamations and dance moves, as the banquet opens.

The dishes on the buffet are supposed to be produced automatically by the enchanted table. Optionally, if it is not already visible, the laden buffet can be made to appear by means of a simple magic formula, which the Avatars know. {% fact "buffet_table_magically_generates_food" %}

Once the music is over, players and heroes get better acquainted around the buffet. It is assumed that, by design, these magic dishes are also accessible to the phantoms (embodied or not).


The first embodiment of the phantoms
++++++++++++++++++++++++++++++++++++++++++++++++

After a while, the gong sounds; the tutor-archivist becomes embodied, and calls the players to come to him. He is delighted to have visitors in this place - and perhaps, with them, a hope of resolving the curse. He answers the players' questions, and **tests their good intentions** with the "{% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}". He points out to them (again) the presence of the buffet, which for him **"activated on its own"** (as he cannot see the Avatars), on this anniversary date of the tragedy, as it does every 100 years

The other phantoms also become embodied (preferably a little later), each at their anchor point further away from the banquet.


The Spectral Bell frenzy
+++++++++++++++++++++++++++++++++++++++++++

A player will probably ring the service bell, out of curiosity, early in the game; as a phantom, one must react in accordance with the description of this mystical artefact, by switching to "{% symbol "spectral frenzy" for "phantom_frenzy_name" %}" mode, even if one is already in normal wandering.

{% endmacro %}
<{ early_game_events }/>


{% macro ankou_introduction_event() %}


The Ankou's passage through the library
++++++++++++++++++++++++++++++++++++++++++++++++++

The Ankou arrives by the stairs, and calls out to the players, telling them that they have no business being here, that he is not "the Beast", that he means them no harm, and finally that he is counting on them to help him solve the problem of these souls imprisoned in the place. He asks after his Spectral Bell, which must already have been stolen by the villain. Then he leaves.

{% endmacro %}
<{ ankou_introduction_event }/>

*The players can subsequently send questions to the Ankou, addressed to the deceased Maupertuis, but beware, the latter do not remember everything either.* {% fact "diakon_invoker_can_message_ankou" %}


The sentinel automaton's murderous madness
+++++++++++++++++++++++++++++++++++++++++++

{% macro automaton_sentinel_instructions() %}

{% fact "druid_turns_automaton_sentinel_into_prophet_killer" %}

From the very start of the adventure, this automaton patrols quite "mechanically" with a Nerf rifle, and challenges the players it comes across. It orders them to state their identity, and to swear (by Zarathustra) that they have no intention of harming the Maupertuis lineage. Then it continues its rounds, henceforth ignoring the players thus checked. {% hint 'nerf_gun_for_guard_automaton' is needed %}

Later, shortly after the opening of the Forbidden Domain, the Druid feels threatened by the various prophecies that gradually point to him. He therefore takes control of the sentinel automaton, through mushrooms/creepers infiltrating the central system of said machine (this is shown in-game, for instance, by fake plants around its neck or behind its mask).
{% hint "plants_around_head_of_automaton_hitman" is needed %}

The Druid sends the sentinel automaton to **assassinate** (with a bullet to the torso) two people:

- **The Oracle player**, who receives the visions
- **The Duchess NPC actor**, who helps her with this

The killer automaton seeks to frighten, or at most wound in the legs, the other protagonists, but no more; for the Druid is counting on them to remove the library curse. It is therefore particularly careful with the precious Diakons.

The automaton cannot retrieve its bullets, which naturally disintegrate on impact.
*These Nerf bullets must be of a different colour from the Parcivals' "darts"; make sure players do not pick them up, as that would make no sense in-game.* {% fact "nerf_bullets_and_arrows_need_different_colors" %}

Obviously, it **never aims at the head** of participants, for safety.

Faced with this automaton:

- All protagonists are vulnerable
- The Woodsman is protected, on the torso only, by the Arkon's armour; his {% symbol "Iridium" for "parcival_woodsman_arrows_metal" %} darts can slightly handicap the killer automaton, but hardly more, except for a perfect shot right to the heart, which would be fatal; he has already heard of this kind of mechanical chimera. {% fact "parcival_woodsman_knows_about_parasited_automatons" %}
- Going for a brawl is forbidden for safety reasons, but would in any case be suicidal given the physical strength of the automatons.
- The Diakons' spells are in theory unusable, as the automaton moves too much, for instance, to be put in stasis in a pentacle.
- If a protagonist possesses the {% symbol 'Dominion' for 'androids_command_bracelet_name' %}', the automatons' command bracelet, he can give orders to the killer automaton, and thus create a conflict that will confuse and slow it down (as the robot will oscillate between the order to kill, and the order not to).
- The best weapons for destroying the killer automaton are the Arkon's ULTRA-HEAVY {% symbol "gladius" for "arkon_weapon_name" %}, and explosives.

{% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}
{% hint "2_explosives_for_minesweeper" is needed %}

Once the killer automaton has been neutralised, or (in the worst case) has run out of bullets and self-destructs, the players can gather from it the clues to its strange contamination.
{% hint "plants_around_head_of_automaton_hitman" is needed %}

If the Druid is called upon to heal one of the automaton's two targets, he will naturally be **reluctant** to do so; but he will then have to choose between keeping a low profile and healing with his usual talent, or deliberately failing in his care, and then trying to justify it so as not to arouse too much suspicion.

{% endmacro %}
<{ automaton_sentinel_instructions }/>


The exploration of the founding Magus's tomb
++++++++++++++++++++++++++++++++++++++++++++++++

{% macro magus_zombie_instructions() %}

The players must find a way to teleport into the tomb of the {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %}, thereby bypassing the malefic seals protecting its entrance, in order to take magical artefacts from it.

The Magus's corpse lies stretched out there, in his golden papal alb.

If a non-Parcival is part of the teleported group (see their identifying garments), this triggers a curse: the Magus's mummy rises, and chases (walking slowly, like a zombie) the intruder, who must dodge it until the teleporter lets them out, on pain of death. The mummy then returns to its place. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %} {% fact "phantoms_are_persistent_but_zombies_are_transient" %}

When there is no non-Parcival in the tomb, the mummy does not move at all, but its mere presence is enough to unnerve the players, while they pinch its legendary ornaments.

{% endmacro %}
<{ magus_zombie_instructions }/>


The final battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

See the quest `Unmask and neutralise the villain`_ for an overview of the possible courses of this final episode.


The musical epilogue
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Have the players switch off their lanterns, to heighten the atmosphere.
A soundtrack is played, for a fairly choreographed scene.

The Ankou calls the finally freed phantoms to join him.

They have each put little wings on their backs: feathers for the Arkon, diodes for the Archivist, steampunk for Octave.

Octave is delighted to be reunited with his family soon, but turns back to hand out thanks, advice and farewells to each group of players, before running off.

The Archivist and the Arkon follow him solemnly.

The Beast may potentially reappear just to escape too, in a comical way, as may the Thief.

The automatons then guide the players to the library exit, before the teleportation portals close until the next {% symbol "winter solstice" for "astral_opening_date" %}.

Depending on whether or not the groups of players have made a commitment to the Arkon to protect/destroy the portals leading to this place, **this library will survive, or will self-destruct into the magma**, for lack of a magical link with the surface (it needs 2 of the 4 links so as not to collapse). {% fact "arkon_questions_groups_about_the future_of_maupertuis_archives" %}


Scheduling of prophecies and intuitions
++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro planning_of_prophecies() %}

**Give the Oracle only the content in italics, not the title or the context of these prophecies.**

- **Initial intuition about the adventurers** (at the end of the common introduction): This intuition, about the need for players to stand together, is already in the Oracle's character sheet. {% fact "parcival_oracle_has_initial_intuition_about_adventurers_solidarity" %}

- **Intuition about the Beast and the Magus** (at the Oracle's first meeting with the Duchess): *"You sense multiple wandering presences. One of them is filled with incomprehension and hatred. You also sense an ancient, sleeping one, both proud and vengeful, that seems to be calling you."*

- **Prophecy of the twin books of the Maupertuis father** (feather in the common Maupertuis chest): Simple vision, music "One Last Stand". {% hint 'feather_in_common_family_chest' is needed %}

- **Intuition about the Forbidden Domain** (when the players enter the forbidden floor): *"You feel the weight of centuries, of millennia of knowledge pouring down on you, knowledge that is a source of life, but also sometimes of death. However, you can sense it, Evil is far more rooted in the authorised floor than it is in the forbidden floor."*

- [OPTIONAL] **Prophecy about the wealth-generating mill** (feather on the board with the mill stereogram near the portraits): Simple vision, music "Here and Now (Seed's Theme)". {% hint 'optional_feather_on_stereogram_board' is needed %}

- **Prophecy of the anti-zombie Amplificans Ring** (feather in the Thanatologue): AUDIO prophecy, music "The Calling". TAKE CARE to keep the soundtrack in the Oracle's earpiece, and the music for the audience, in SYNC. {% hint 'feather_in_thanatologue' is needed %} If the Oracle player does not feel able to handle this audio prophecy, fall back on a simple vision, with the picture.

- **Cassandra's Prophecy**, as a video on the hologram pyramid, triggered by pouring the right potion on the right scary lenticular painting. {% hint "prophecy_hologram_for_scary_lenticular_painting" is needed %}

- **Prophecy of the Druid's lost 3rd Volume** (feather in the Arkon's satchel left by the villain): Simple vision, music "Broken Truth light (Delphi's Theme)". {% hint 'feather_in_arkon_bag' is needed %}

- **Prophecy of the Arkon's skull and the planetary danger** (lighting of the incense fountain): Partial vision as a DUO with the Duchess, music "Broken Truth heavy (Delphi's Theme)".

- **Intuition about the last battle** (shortly after the villain is unmasked, but ONLY if Cassandra's holographic prophecy has not been triggered via the scary lenticular portraits): *"You sense that the living present here are like ants standing before a bull; but that if all the ants join their efforts, they can build something to destroy their enemy. Beware however, in the final moments of a struggle, the best of friends can become the worst of adversaries, even unknowingly."* {% fact "parcival_oracle_has_fallback_intuition_about_last_battle" %}

{% endmacro %}
<{ planning_of_prophecies }/>


Quests and puzzle trails
============================

{#
OTHER IDEAS FOR ABILITIES AND PUZZLES

- Add textual riddles to find words (see Enigma Battle on the Clivra forum)
- Survival? Microfilms? QR Codes? Call to the knowledge switchboard?
- Restorer of erased texts (or that's redundant)? + gemmological analysis kit (meh)?
- Various fairly distinctive caskets and books are scattered among the normal books of the library; they must be found and then, for each, the corresponding key or code must be found. TO BE SPECIFIED

#}

Access the Forbidden Domain (useful to all)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A seal is visible in front of the stairs leading to the forbidden floor. When it is activated, a grimoire appears; it shows flippable squares on a panel (or an app on a touch tablet), {% hint "symbolic_enigma_puzzle_app" is needed %} which allow different combinations of symbol fragments to be created; the right complete pattern must be found to open the passage.

- The NPC actors indicate that the secret symbol of the Maupertuis family is needed to open the passage. {% fact "secret_family_symbol_needed_for_forbidden_zone" %} {% fact "npcs_know_about_secret_family_symbol_system" %}

- Octave has some memories of this system, even though he had not yet received his family's secret symbol, and had never gone alone into the Forbidden Domain (the Beast would in fact have attacked him in that case). {% fact "octave_would_have_been_attacked_by_beast_if_alone_in_forbidden_domain" %}

- The family symbol is a **UV message** in a booklet "Genealogy of the Maupertuis", {% hint "genealogy_book_with_uv_family_symbol" is needed %} which is hidden in the family's administrative briefcase. Octave and the Archivist had heard about this. {% hint "family_briefcase_protected_by_code" is needed %} {% fact "octave_and_archivist_know_about_secret_family_symbol_in_family_briefcase" %}
  This briefcase is protected by the code {% symbol "625-993" for "family_briefcase_code" %}, which is "whispered" by the fake book "{% symbol "Venture Prins" for "small_wooden_fake_book_name" %}". {% hint "family_briefcase_code_spoken_by_venture_prins_fake_book" is needed %}

- Octave and the Archivist know this fake book well, and have even, thanks to the code obtained, searched the administrative briefcase (dangerous because trapped) in the past. But in vain, alas. {% fact "octave_and_archivist_have_searched_family_briefcase" %} {% fact "octave_and_archivist_know_about_trap_of_family_briefcase" %}

- Both remember where they left the "{% symbol "Venture Prins" for "small_wooden_fake_book_name" %}"; they point out the relevant shelf to the players who ask, and the book is indeed there. {% fact "octave_and_archivist_know_about_venture_prins_book_location" %}
  A stethoscope, or even the help of an automaton, may be needed to hear the code broadcast within the wood of the book, and thus open the Maupertuis briefcase.

- The code of the administrative briefcase can also be requested from the deceased parents, later, via the Ankou, as a last resort.

Once the family symbol has been reproduced on the grimoire, a powerful sound is heard, and the passage to the Forbidden Domain is free to be crossed in both directions.


Neutralise the Maupertuis Beast (useful to all)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

When the library was cursed, the Beast that guarded the Forbidden Domain was trapped there, even after dying of old age. Having turned into an embittered phantom, it is more dangerous than ever.

The Beast attacks any living creature, and its attacks (hand-to-hand but "sacred") are quickly crippling and then lethal. It cannot see the characters from the books, and mostly ignores the phantoms, somewhat like a skittish dog. {% fact "beast_ignores_or_fears_other_phantoms" %}

Once access to the Forbidden Domain (usually protected by a powerful {% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %}) is open, the Beast is free to come out of it, and burst in among the players, if they do not take the initiative. Octave and the Archivist therefore encourage them to plan how to render it harmless for good. {% fact "octave_and_archivist_warn_players_about_beast_dangerousness" %}

To neutralise the Beast:

- The Beast detects the living who are within 3 m, but sees very poorly beyond that. It is therefore possible to walk around the Forbidden Domain while carefully avoiding it, but this remains very dangerous.
   {% fact "characters_know_how_the_beast_works_regarding_3m_sight" %}

- The Arkon had a suit of {% symbol "Mithril armour" for "arkon_armor_name" %} fully protecting the wearer from "sacred" attacks, that is to say those of creatures belonging to the kingdom of the dead. The players can find it in the graveyard, and the **sturdiest** of them all can put it on, to stand up to the Beast's attacks. {% hint "arkon_sacred_armor" is needed %}

- **The Exorcist** can drive the Beast away for a while with one of his incantations, or on the contrary draw it towards him at a slow pace. {% fact "diakon_exorcist_can_chase_away_beast_temporarily" %} {% fact "diakon_exorcist_can_attract_slowed_beast_temporarily" %}

- One of the Parcivals has bullets that can be **made sacred by the Exorcist**, and thus capable of "killing" the phantom Beast (that is to say turning it back into a randomly wandering spectre). But because of the curse that encloses the library, the Beast would in that case inevitably come back a little later, even more ferocious. {% fact "diakon_exorcist_can_bless_parcival_woodsman_arrows" %}

- The Beast's favourite treats were {% symbol "moon stones" for "phosphorescent_pebbles_name" %}; even though it can no longer eat them, it pounces on them whenever it comes across some. {% hint "beast_snack_as_moon_stones" is needed %} {% fact "beast_is_addicted_to_moon_stones" %}

- **The Invoker** knows a ritual capable of "freezing" an entity from the world of the dead for several days. He must draw the right pentacle, and make sure the Beast is lured onto it. Once this is done, the players are rid of it until the end of the game. {% fact "diakon_invoker_can_freeze_beast_for_days" %}

{# NOT YET - movable walls could be shifted to cage the Beast #}
{# NOPE - **The Alchemist** can find a potion capable of creating an {% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %} for one day on a #}




The remedy for marbled degeneration (Parcival family)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro parcival_group_main_quest() %}

**The Parcivals' main objective is to find a remedy for the illness of their little sister {% symbol "Philomène" for "parcival_sick_child_name" %}, {% symbol "marbled degeneration" for "legacy_disease" %}, since their ancestor Mérédice de Maupertuis had been cured of it here.**

- The Archivist remembers very well the illness of Mérédice de Maupertuis, and how the Maupertuis parents had sent him in person to fetch various highly specialised ingredients to create a {% symbol "Rejuvenation Cocktail" for "parcival_disease_main_remedy_name" %}. Luckily, during the inventory, he had found and put back in its place the recipe for this cocktail, and he points it out to the players (it is on the authorised floor). {% fact "archivist_knows_about_meredice_rejuvenation_cocktail_recipe_location" %}

- The {% symbol "Rejuvenation Cocktail" for "parcival_disease_main_remedy_name" %} requires mixing three potions: the Flexifying Elixir (harmless), the Clairvoyance Lotion (harmless), and the Pyrolitis Tincture (dangerous). {% hint "recipe_rejuvenation_cocktail" is needed %}

- The recipes for the first two potions are on the authorised floor; the Archivist had come across them, and had marked their location on the floor with **white crosses** (in tape). {% hint "recipe_flex_elixir" is needed %} {% hint "recipe_clarity_lotion" is needed %} {% hint "white_arrows_on_floor_towards_cure_recipes" is needed %} {% fact "archivist_has_marked_locations_of_rejuvenation_cocktail_subrecipes" %}

- These first two potions only call for ingredients that are easily accessible in the Parcival family's country, so they do not need to be made on site. But the help of the **Druid** is needed to recognise the obsolete names that designate certain ingredients in these recipes (or else question the Maupertuis parents from the afterlife). {% fact "druid_known_about_plants_and_gems" %} {% fact "parcival_alchemist_has_all_ingredients_for_flex_elixir_recipe" %} {% fact "parcival_alchemist_has_all_ingredients_for_clarity_lotion_recipe" %}

- The last potion, the Pyrolitis Tincture, which can also be used for hexes, has its recipe in the **Forbidden Domain**, which must therefore first be unlocked. A **{% symbol "Tracker Grimoire" for "frequency_scanner_book_name" %}** (a Bluetooth beacon scanner mobile app), which can be found on site in a chest, is used to locate recipes whose name is known, in this strange place (in addition, optionally, to the labels on the shelves). The Alchemist has heard of it. {% hint "radio_frequency_scanner_app_in_chest" is needed %} {% fact "parcival_alchemist_knows_about_frequency_scanner_book" %} {% hint "forbidden_zone_optional_labels_showing_tincture_shelf" is needed %} {% hint "recipe_pyrolitis_tincture" is needed %}

But the ingredients and the preparation method of this tincture are very complex, so one must make use of what had already been gathered by the Maupertuis family.

- One ingredient of the Tincture is in plain sight on the authorised floor; another in plain sight on the gemmology workbench; another on the alchemy workbench in the Forbidden Domain (but protected by a padlock to be picked); the last in a **toxic corridor** of the forbidden floor (this is an additional protection of the place). {% fact "one_corridor_is_toxic" %} {# Hint tags for this are in the clues document #}
  Walking down this last corridor means certain death. To retrieve the ingredient in question, one must either have recovered the anti-poison necklace elsewhere, or have been given control of an automaton and send it to fetch this ingredient (or simply ask the Inventor to act). {% hint "androids_command_silver_white_ribbon_bracelet_for_inventor" is needed %}

- Finally, a metal container with an **anti-explosion enchantment** is needed, which can be found among the alchemy tools (in the form of a small cylindrical copper cauldron with a handle). {% hint "enchanted_copper_cauldron_on_alchemy_table" is needed %}

- Once all the ingredients have been gathered (there is no need to actually prepare the potions), the family has succeeded in this mission, provided it can leave the place.

{% endmacro %}
<{ parcival_group_main_quest }/>


The Maupertuis treasure (Mirandian secret agents)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro spy_group_main_quest() %}

**The Mirandian secret agents' main objective is to find the treasure, the source of the Maupertuis' wealth, to save their small country from bankruptcy.**

They have found a fragment of Mérédice's diary, in which she describes in enigmatic language how, when a grimoire starts singing, thanks to changing symbols, something turns and riches appear. {% hint "meredice_diary_about_treasure_for_spy_group" is needed %}

An oracle triggered in the Forbidden Domain shows a paddle mill pouring riches into the river, surrounded by musical notes. {% hint "parcival_oracle_vision_about_water_mill" is needed %}
A stereogram on the wall also shows a coffee mill with a double hidden word of thanks {% hint "grinding_mill_stereogram_picture_with_magnetic_and_uv_code" is needed %}.

The players must understand that it is a **coffee mill** simply "hidden in plain sight", on the alchemist's workbench of the forbidden floor. {% hint "grinding_mill_with_enchantment" is needed %}

This mill, capable of generating precious stones out of nothing, actually requires a song from a magic grimoire in order to work.
Optionally, a seal on the forbidden floor must be activated to make this magic grimoire appear.
This work is protected by a code that changes every few days. {% hint "symbolic_cards_enigma_app" is needed %} {% fact "treasure_code_changes_magically" %}

The code is made up of symbols spread across 4 (indestructible) Maupertuis jewels. Only 3 jewels are enough to activate the song, as the last symbol can be found *relatively* quickly by trial and error on the singing grimoire's code.

The various jewels:

- The mother's brooch is on **Octave's grave**; he had worn it as a keepsake after finding it in the library; this brooch was almost all that remained in the child's ashes after the betrayal, so the Avatars laid it there as a sign of mourning. This object must guide the players in understanding the overall puzzle. {% hint "maupertuis_mother_jewel_on_octave_tomb" is needed %} {% fact "octave_carried_mother_jewel_after_her_death" %}

- The father's brooch is hidden in his key-protected magic book; this book was found by the heroes (who left a mark on the floor to point it out), but they did not know how to open it. The **magnetism and UV detectors** give a code, which is used to open ANOTHER magic book with a numeric code (also marked on the floor), which in turn contains the key to the first.
  {% hint "maupertuis_father_jewel_in_twin_books" is needed %} {% hint "parcival_oracle_vision_about_maupertuis_father_twin_books" is needed %}

- The brooch that was initially intended for Octave is in one of the N sealed mini-caskets, which are hidden in an initiation SEAL. This was a trial for Octave, who had to be able to "sense" the presence of the magic object before being entitled to it. The players must activate the seal, listen to the pre-recorded message of an automaton summarising the trial for them, then use the **metal detector** to guess which casket holds the object. Only a Maupertuis heir can actually trigger the resolution of this initiation. {% fact "octave_needed_to_pass_initiation_to_gain_his_jewel" %} {% fact "only_maupertuis_heirs_can_take_initiation" %} {% hint 'maupertuis_initiation_seal' is needed %} {% hint "maupertuis_son_jewel_in_nonmetal_tiny_chests" is needed %}  {# FIXME no more recorded message here, a letter instead!!! #}

- Mérédice's brooch, finally, was precisely the one the Thief had come to seek in the Forbidden Domain. He knows that it is in a metal box, in a corner of the library that has **collapsed**. He therefore sells this information dearly and reluctantly, knowing that he is no longer in a good position for the quest for the Maupertuis treasure. Octave also has a few less precise clues about where his sister kept her most precious belongings. {% hint "maupertuis_daughter_jewel_under_rubbles_beyond_alchemist_laboratory" is needed %}
  {% fact "thief_knows_about_location_of_maupertuis_daughter_jewel" %} {% fact "octave_has_hints_about_location_of_maupertuis_daughter_jewel" %}

Entering the right symbols into the singing grimoire triggers a victory melody, and one must then simulate that the mill, when turned, produces a batch of gems; limited in number per day (one batch every X hours), but sufficient for the secret agents' quest. {% hint 'jewels_set_for_grinding_mill_success' is needed %} {% fact 'spy_country_needs_500_kashes_per_day_for_3_years' %}

With the magic mill and the singing grimoire, the secret agents have succeeded in their mission, provided they can leave the place.

{% endmacro %}
<{ spy_group_main_quest }/>


The {% symbol "Thanatologue" for "book_of_the_dead" %} (Heliossarian explorers)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro explorer_group_main_quest() %}

**The Heliossarian explorers' main objective is to find the {% symbol "Thanatologue" for "book_of_the_dead" %}, a cursed grimoire, and above all, thanks to it, a way to counter the hexes and the invasion attempt of their enemies the Akariths.**

One of the rare copies of this mythical (and controversial) work has been kept by the Maupertuis lineage, in the "legendary chest" located in the **Forbidden Domain** - which Octave or the Archivist should point out to the explorer-archaeologists after checking their good will. For the safety of the world, both Maupertuis parents had to contribute their secret code to unlock this chest. {% hint "family_legendary_chest_protected_by_double_code" is needed %} {% fact "octave_and_archivist_know_about_thanatologue_location_and_double_code" %}

- **{% symbol "Quirinius" for "maupertuis_father" %} de Maupertuis had a poor memory**, he kept his codes in his personal notebook. The notebook is in one of his fake books (see above for how to open it). The secret code sought is in the form of a **square anamorphosis**. {% hint "quirinius_notebook_with_thanatologue_chest_code_as_anamorphosis_in_fake_book" is needed %}
  It is **{% symbol "723" for "maupertuis_father_thanatologue_chest_code" %}**. {% fact "dead_quirinius_does_not_remember_thanatologue_chest_code" %}

- **{% symbol "Isadora" for "maupertuis_mother" %} de Maupertuis hardly ever wrote anything down and memorised everything**, so she must be questioned from the afterlife to obtain her code. This is done by sending a message through the Ankou (and therefore through the **Invoker**). Alternatively, the **Thief** knows this code (which Octave's mother had also used for other caskets), and sells it very dearly; it can also be found in the Thief's wallet (lying in the Beast's den). {% fact "dead_isadora_remembers_thanatologue_chest_code" %} {% hint 'defunct_isadora_code_for_thanatologue_chest_code' is needed %} {% fact "diakon_invoker_can_message_ankou" %} {% fact "thief_knows_about_isadora_thanatologue_chest_code" %} {% hint 'thief_wallet_with_isadora_code_in_beast_nest' is needed %}
  This code is **{% symbol "159" for "maupertuis_mother_thanatologue_chest_code" %}**.

{% fact "maupertuis_mother_had_excellent_memory_but_not_father" %}

- The {% symbol "Thanatologue" for "book_of_the_dead" %} is indeed in the legendary chest, but that does not solve the problem. This book in fact teaches how to temporarily resurrect - in a semi-intelligent but obedient zombie form - recently dead people (by first drinking a **Potion of Authority**, which the Alchemist can easily make); and this would ensure victory for a horde of fanatical Akariths breaking into the Heliossarian technological defences. {% fact "akarith_army_is_much_more_numerous_and_mystic_than_heliossar_army" %} {% fact "players_have_thanatologue_spell_to_summon_zombies" %} {% hint "recipe_authority_potion" is needed %}
  The explorers must therefore find the countermeasure to this necromantic strategy. A **UV message** gives a clue to a solution, in the {% symbol "Thanatologue" for "book_of_the_dead" %}: the Akariths seek to target first and foremost the invokers of the opposing side, especially those wearing large jewels. {% hint "thanatologue_book_with_zombie_spell_and_uv_counterspell_hints" is needed %}

- The Arkon knows no miracle solution to a legion of zombies - other than fighting them one by one with blessed weapons. But he had heard of powerful ground enchantments, capable of preventing their initial "reanimation" from corpses. {% fact "arkon_has_clues_about_preventing_zombie_invocation_on_land" %}

- The Diakons know a simple ritual allowing a grave to be "dispelled" in advance, thus preventing a necromancer from raising an undead from it. But they do not know how to do this on the scale of a battlefield; that would require a legendary magical artefact. {% fact "diakon_invoker_has_spell_against_zombie_invocation_on_single_tomb" %}

- The Oracle has a vision/audio prophecy of a confrontation between a legion of undead, led by a dark grimoire, and a peaceful graveyard, enchanted by a ring topped with a symbol: **{% symbol "sun with a black whirl at its centre" for "amplificans_artefacts_symbol" %}**. {% hint "parcival_oracle_vision_about_necromancers_and_ring_amplificans" is needed %} {% hint "parcival_oracle_audio_about_necromancers_and_ring_amplificans" is needed %}

- The Arkon remembers this symbol, which is among other things that of the legendary **{% symbol "Amplificans Ring" for "ring_amplificans_name" %}**, which is said to have belonged to the founder of the Maupertuis lineage, the {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %}, but disappeared upon his death. He advises looking for traces of this in said Magus's tomb. {% fact "arkon_has_hints_about_ring_amplificans" %}

- An ultra-powerful magic barrier blocks access to the Magus's tomb, even though phantoms can bypass it; the only way to get in as a living person is clearly to teleport there. {% fact "magus_mos_peratys_tomb_is_extremly_well_sealed" %} {% fact "magus_mos_peratys_tomb_can_be_explored_by_free_phantoms" %}

- The powerful {% symbol 'teleportation astrolabe' for 'thief_teleportation_device_name' %} belonging to the Thief is on his remains, which are cursed because he "died in vice". {% hint 'thief_cursed_skeleton' is needed %} {% hint 'thief_teleportation_device_in_beast_nest' is needed %}

- The Thief demands a large sum of money to give the magic word allowing teleportation. Enough scattered riches must therefore be gathered for this, or the Maupertuis treasure used once it has been found. Alternatively, this formula can be found in encrypted form among the Thief's belongings. {% fact "thief_knows_teleportation_device_formula" %} {% hint 'thief_teleportation_device_encrypted_formula' is needed %}

- Only a Maupertuis heir can teleport peacefully into the tomb; anyone else triggers the awakening of the Magus in zombie form, and must therefore flee from him until they can teleport back outside. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

- If a person goes alone with the astrolabe into the Magus's tomb and is killed, the only way to recover the situation is to **zombify** them (thanks to the {% symbol "Thanatologue" for "book_of_the_dead" %}) so that they bring back the artefacts and the astrolabe.

- In the tomb, among other things, on the Magus's remains, is the {% symbol "Amplificans Ring" for "ring_amplificans_name" %}. {% hint 'ring_amplificans' is needed %}

- With the magic ring and the dispelling formula, the explorers have succeeded in their mission, as they have a few invokers in their army; provided they can leave the place, of course.

{% endmacro %}
<{ explorer_group_main_quest }/>


Unmask and neutralise the villain
+++++++++++++++++++++++++++++++++++++

{% macro quest_to_find_traitor_and_final_battle() %}

The accounts of the various phantoms agree on the fact that they died while the ritual was taking place. Suspicion should initially fall on the Arkon, especially from the Avatars (who were unable to see him afterwards as a phantom). But the Beast of the forbidden floor, or a possible curse linked to the ancestor {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %}, may also be suspected.

The Arkon, for his part, knows that he fought savagely against an assailant shrouded in darkness, who resisted physical, magical and sacred attacks well; and that he therefore cursed this attacker (and the library) as he succumbed.

Suspicion then turns to the Avatars, who were able to come and go between the worlds while the ritual was taking place, via various copies of their novels.

The remains of Octave and the Archivist cannot be found; it seems they were reduced to ashes. Only the bones (but **without the skull**) of the Arkon remain, which have indeed become indestructible. **The medical analysis of these bones** reveals signs of burning. {% hint "arkon_bones_having_traces_of_burning" is needed %}

In the Beast's den, among the Thief's remains, is the Arkon's **ULTRA-HEAVY {% symbol "gladius" for "arkon_weapon_name" %}**. This weapon can be analysed: it has traces of blue blood on its surface. Now, one of the novels about the Druid mentions that he has blue blood.
{% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}
{% fact "arkon_heavy_gladius_sword_has_blue_blood_traces" %}
{% fact "druid_novels_mention_his_blue_blood" %}

Several **oracles** are also delivered to steer the players.

- One shows a wooden, clawed hand threatening the world, as well as a skull beneath tree roots, making it possible to discover the Arkon's skull in the Druid's "indoor mini-jungle".
  {% hint "parcival_oracle_vision_about_skull_location_and_world_threat" is needed %} {% hint "arkon_skull_hidden_in_jungle_trees" is needed %}
  **The medical analysis of the skull** shows curare poisoning, which naturally casts suspicion on the Druid.  {% hint "arkon_skull_analysis_showing_curare_poisoning" is needed %}
- Another oracle shows a book bearing the number 3, wedged between evocations of "Zoology" and "Pastries". Volume 3 of the Druid's novel is hidden between these two shelves of books, indicated by labels on the furniture. {% hint "parcival_oracle_vision_about_location_of_chaos_novel_volume_three" is needed %} {% hint "authorized_zone_labels_showing_zoology_and_cooking_shelves" is needed %}
  Reading an **excerpt from Volume 3** shows that the Druid actually became a cruel and treacherous tyrant at the end of his own adventure. {% hint "chaos_novel_volume_three_between_zoology_and_cooking_shelves" is needed %}

The Druid initially denies all accusations, calling his accusers mad.
{# LATER **SIDE IDEA: during the game, the traitor murders one of the Avatars, who objected too strongly to the idea of removing the {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %} without having solved the investigation into the humans' deaths.** #}

But when the various conclusive clues are laid out before the other Avatars, they side with the players.
Typically, the Duchess will then go and confront the Druid, to intense music. {% fact "duchess_immediately_confronts_traitor_when_exposed" %}

He then changes his stance, owns up to his crime in the name of the Salvation of Pangea, and reminds everyone that he is far more powerful than all the participants put together. He therefore demands that everyone help him break the library curse, in exchange for their lives being spared in his future Haven of Nature.

He urges the players to hurry: he has all the time in the world, and now that he has access to the grimoires of the Forbidden Domain, he will eventually discover how to use this world's magic and break the library curse; but they have urgent missions to accomplish and must get out before the teleportation portals close, in a few hours' time.

The Druid warns that he will no longer move away from the pentacle of the Arkon's ritual, so that no one attempts to forcibly send him back to his world; and that he would sense it if another similar pentacle were created in the vicinity.

Typically, he then starts **reading grimoires** (including the {% symbol "Thanatologue" for "book_of_the_dead" %}), looking enthusiastic, not far from the pentacle. He really is on the trail of a **counter-spell** to cancel the {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %}. {% fact "druid_reads_near_pentacle_before_game_ending" %}

The traitor is immune to the usual attacks.
If the players assault him directly, he kills one of them (who becomes a phantom), then orders the others to keep searching for how to lift the curse.

But there are certain ways of getting at him:

{# NOPE for now - Either concoct a **magic self-combustion potion** and make him drink it, which will turn his magical power against him; this potion absolutely must be brought to him early enough, and by the automaton, so that he is not suspicious. #}
{# NOPE for now - Or reconstitute a banishing pentacle elsewhere TOO HARD, and use Volume 3 on it to expel the Druid from the world of humans (but beware, he must not see this, so he must be diverted if he comes to see what the players are doing).  #}

- Either bewitch a crossbow dart so that it becomes **unavoidably lethal**; this is a dark spell from the Thanatologue, the {% symbol "Sacrifice of Zarathustra" for "unavoidable_bullet_spell_name" %}, which requires the voluntary death of **three players** to create a "weapon that does not forgive". {% hint "unavoidable_bullet_spell_from_thanatologue" is needed %}
  The Alchemist can recreate darts thanks to a recipe found in the Forbidden Domain. {% fact "parcival_alchemist_can_create_iridium_arrows" %} {% hint "arrow_recipe_for_alchemist" is needed %}

- Or the most effective way: make a ritualist invulnerable to physical, toxic and magical attacks, then send him to destroy the otherworld corridors en masse thanks to one of his **rituals**, thereby walling the Avatars up in their respective worlds. {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

A holographic prophecy detailing this "invulnerable Diakon" procedure and its limits can be triggered by activating, with a Lotion of Revelation, one of the horrific portraits hanging on the wall; a recognisable portrait, as it reacts to the metal detector (the player who owns this tool has information about this).
{% hint "scary_lenticular_painting_with_metal_in_it" is needed %}
{% hint "prophecy_hologram_for_scary_lenticular_painting" is needed %}
{% fact "spy_sounder_knows_about_scary_lenticular_paintings" %}
{% fact "scary_lenticular_paintings_can_deliver_powerful_prophecy" %}
{% hint "potion_of_revelation_from_exorcist" is needed %}

- If this holographic prophecy is not found, an **intuition** of the Oracle can also evoke this battle plan, and warns against a counter-attack by the villain with the help of the phantoms. {% fact "parcival_oracle_has_fallback_intuition_about_last_battle" %}

Here is the "optimal" course of this final battle using an expulsion ritual:

- The players must gather **the {% symbol "Etheric Necklace of Stone Skin" for "etheric_stone_skin_necklace_name" %}, the {% symbol "Etheric Necklace of Vital Force" for "etheric_vital_force_necklace_name" %}, and the {% symbol "Etheric Necklace of Manaic Aura" for "etheric_manaic_aura_necklace_name" %}**, which are stored in various places in the library. {% hint "etheric_stone_skin_necklace" is needed %} {% hint "etheric_vital_force_necklace" is needed %} {% hint "etheric_manaic_aura_necklace" is needed %}

- For safety, the other Avatars must be urged by the Exorcist to each return to their world, otherwise they would be put in grave danger by the ritual. {% fact "diakon_exorcist_might_kill_remaining_avatars_with_expulsion_ritual" %}

- When the Exorcist begins his ritual, the Druid is at first confused, then, understanding what is happening, he attacks him by various means, but in vain.

- In desperation, the Druid will use the {% symbol "Spectral Bell" for "table_bell_name" %} to rally the spectres and thus endanger the ritualist; the latter does not have the build to don the Arkon's {% symbol "Mithril armour" for "arkon_armor_name" %} (which contains the {% symbol "Etheric Necklace of Blessing" for "etheric_benediction_necklace_name" %}), and thus protect himself from the spectres. {% fact "druid_finally_uses_table_bell_as_weapon" %}{% fact "etheric_benediction_necklace_is_in_arkon_sacred_armor" %} It is up to the other players to push back the spectres (with said Arkon's armour, with exorcisms...), without themselves getting attacked by the Druid.

- Once the ritual is complete, the Druid appears wounded; the Arkon then steps in to proclaim victory, and calls all the Diakons around him for a few final repetitions of the ritual incantation. He can break away from them at the end to proclaim: **"Per Horus et per Ra, per solem invictus, duceres {% symbol "Diviciacos" for "druid_name" %}, ACTA EST FABULA"**, authoritatively pointing out the centre of the pentacle to his adversary. The Druid is then drawn to the pentacle and dies there (https://fr.wikipedia.org/wiki/Per_Horus_et_per_Ra_et_per_Sol_Invictus_duceres).

- If the Diakon abandons the ritual for any reason, the Druid may "make an example" by killing one of the players, then repeats his orders to the survivors.

Whether the traitor is annihilated one way or another (cursed bullet or expulsion ritual), the curse comes to an end, and the epilogue can unfold. {% fact "traitor_death_ends_cursed_enclosure" %}

But if a player follows the Druid's orders and lifts the {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %}, or if everyone takes too long to act and the Druid finally breaks this curse himself (thanks to a formula supposedly found in a grimoire), then the Druid immediately escapes from the library.

In that case, the players can indeed go home, but with the bitterness of failure: having let a monster loose on their world. And the **remaining Avatars** (or those who came back having sensed the tragedy) can choose between being sent back, or staying to try to help this planet against the new peril.

{% endmacro %}
<{ quest_to_find_traitor_and_final_battle }/>


Finish the Avatar expulsion ritual (Diakons)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Avatars initially refuse to let anyone continue the ritual, begun by the Arkon and interrupted by the villain's betrayal, with a view to sending them home. Indeed, they do not want to leave until the phantoms have received justice and been freed. Added to this, initially, is the fear that the ritual itself caused these tragedies.

The pentacle and the ritual objects are still in place, as the traitor did not dare touch this sacred magic that he does not know, and moreover cannot, by nature, carry novels. {% fact "avatars_cannot_carry_novels" %}

It is only once the final battle plan is well established, or the villain already eliminated by some means, that the Avatars agree to return home and let the Exorcist's ritual send them back to their worlds for good.  {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

If a player attempts to forcibly send back the "good" Avatars, this will certainly cause a fair amount of chaos among the NPC actors as well as the players.


Remove the library's {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %} prematurely (trap)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The library's Enclosure can be removed prematurely by a ritual known to the Diakons, which requires the cooperation of at least **{% symbol "3 / 5 of the living" for "library_cursed_enclosure_opening_quota" %}** present, as well as **ingredients** easily accessible in the alchemist's workshop of the Forbidden Domain. {% fact "diakon_invoker_can_break_cursed_enclosure" %} But if this curse is destroyed in this way, the traitor escapes from the library, and it is a failure for everyone, as described above.

In the optimal outcome of the game, the library curse is automatically lifted upon the traitor's death, and this quest becomes moot. {% fact "traitor_death_ends_cursed_enclosure" %}

{# NOPE TOO MANY MISSIONS ALREADY

    Preserve the legendary grimoires (Diakons' bonus?)

    Most of the works in the library are copies of common books, or ones found since in other mystical places. But the {% symbol "Thanatologue" for "book_of_the_dead" %}, as well as two works (Necronomicon? Codex Vampiris?) must not fall into the hands of the impious who will probably end up finding this library in their turn.

    The two additional grimoires can be found thanks to *magnetism on a map of the library*, or by bribing the Thief.

    They must be useful to the players too, before they can be destroyed without regret. Or on the contrary they must be traps for overly bold readers...

#}


The Spiritual Orb, the Abyssal Vortex (trap) and the Fount of Knowledge (gift)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*This is an optional quest.*

In the Forbidden Domain, the players can find a tray with a switched-off plasma ball in the centre, designated as a {% symbol "Spiritual Orb" for "spiritual_orb_name" %}; 4 slots are drawn around it.

These slots each await a key object, which is an epoxy resin casting:

- a romantic crystal (a rose in a square-based pyramid)
- a marine crystal (a seashell in a triangular-based pyramid)
- a prickly crystal (a thistle in a cube)
- an innocent crystal (white flowers in a diamond)
{% hint 'spiritual_orb_key_square_base_pyramid' is needed %}
{% hint 'spiritual_orb_key_triangle_base_pyramid' is needed %}
{% hint 'spiritual_orb_key_cube_is_needed' is needed %}
{% hint 'spiritual_orb_key_diamond_is_needed' is needed %}

It is indicated, by a coat of arms (with a flame triad) that the Anthropologist knows, and by an excerpt from the Thanatologue, that by gathering these crystals and proclaiming a certain magic formula, one can open the **"Abyssal Vortex"**. {% fact "anthropologist_knows_about_fire_triad_emblem" %} {% hint 'abyssal_vortex_hint_in_thanatologue' is needed %}

The Avatars or Maupertuis phantoms know nothing about this, but the Arkon is wary of this little-known artefact. {% fact "arkon_does_not_know_about_spiritual_orb_magic" %}

It is in fact a communication channel to a demonic dimension. Once this channel is open (i.e. once the plasma ball is lit), the players who place a finger on it are contaminated by harmful influences too powerful for them. Depending on their character, they will have forfeits showing that their sanity has been damaged; always with a great deal of agitation and incoherent speech.

Examples of forfeits:
- the Oracle starts making preposterous predictions
- the Alchemist drinks one of his potions (non-lethal)
- others start using their metal detector or their UV lamp in vain, aimlessly...

This orb can also open passages to other strata of reality. In particular, the Thief knows the formula for opening a passage to the **{% symbol "Fount of Knowledge" for "link_to_djinn_world" %}**. If the players place a finger on the orb while it is connected to this world, they become bound to the **invisible world of the Djinns**, small, curious, invisible, harmless spirits who wander about everywhere. {% fact "phantom_thief_knows_formula_of_link_to_djinn_world" %}

The players can use this gift as a historical search engine, and ask the Game Master questions about the lore of this planet, about the main aspects of the Maupertuis' history. The Djinns do not know everything, have differing opinions, are sometimes wrong, but give generally instructive and useful information.

The **renegade Djinn**, played by the Game Master, was in fact cut off from communion with his fellows by the Arkon's frantic and dangerous invocations during the tragic fight; he is therefore searching for a magical artefact to be able to reconnect with his spirit world, which is none other than the {% symbol "Fount of Knowledge" for "link_to_djinn_world" %}.


Overview of participants' specific abilities
=============================================================

These roles can easily be reassigned or combined within a team, in case of changes in the players present. They come on top of the abilities common to all players (searching for objects, using keys, talking with NPC actors), which are also necessary to progress through the puzzles.

IMPORTANT: each role must have its **"moment of glory"** planned in the scenario - it is up to the player to know how to seize it.

{% macro summary_of_player_abilities() %}

{# CAUTION: DO NOT PUT ANY SPOILERS HERE, AS THE DRAGONS HAVE THIS INFORMATION TOO #}

Diakons of {% symbol "Bahamoot" for "god_of_diakons" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

They come to restore the natural order of things in the Maupertuis secret archives.

- Dispeller: recognises bewitchments on objects, removes negative ones, and knows the types of injuries
- Exorcist: knows how to attract or banish spirits, and bless weapons; knows about phantoms
- Invoker: knows how to perform complex magic rituals using pentacles or seals; owns a censer

Parcival family
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

They are searching for a remedy to save their sister.

- Woodsman: owns a crossbow and has Herculean strength; has a strong protective instinct, and knows various monsters
- Alchemist: knows how to make potions for various purposes; owns various ingredients and equipment
- Oracle: occasionally receives great visual or auditory revelations, as well as intuitions

Mirandian secret agents
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

They absolutely must find a source of wealth to save their country from bankruptcy.

- Minesweeper: knows how to secure traps/cave-ins, owns explosives and candles; knows mechanics well
- Sounder: knows how to detect metals and surface magnetic fields; senses the abnormal (archaeological, magical or divinatory) nature of artefacts
- Lockpicker: knows how to force certain padlocks, and open magnetic locks/anti-theft devices; carries ritual potions

Heliossarian explorer-archaeologists
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

They are seeking a cursed grimoire, in order to see through the schemes of a horde of invaders and counter them.

- Runologist: knows how to translate Akarith runes and recognise various secret codes; owns a magnifying glass and a stethoscope
- Unveiler: knows how to read invisible inks, and scientifically analyse objects
- Anthropologist: learned in human traditions, theologies, coats of arms, and market values; can sense the past of certain artefacts or places; knows about phantoms and the types of injuries

{% endmacro %}
<{ summary_of_player_abilities }/>


.. raw:: pdf

   PageBreak


The game universe
#############################

*This information is replicated in general summaries or relevant character sheets.*

{% macro common_lore_for_all() %}

Historical and geographical context
====================================

{# FIXME DEDUPLICATE THIS ONE DAY #}

The action takes place on the planet Pangea, in the **{% symbol "year 1000" for "current_events_year" %} of the {% symbol "Era of the Great Appeasement" for "current_era_name" %}**; the current level of development there is similar to our 20th century on Earth, but with a much smaller population.

In reality, the whole History of this planet, from prehistory up to the year 1900, is identical to ours. References to these periods of our world (Antiquity, Middle Ages, Renaissance...), to their cultural and artistic output, are therefore valid on Pangea, even if few people know them.

It was at the start of the 20th century that the two worlds diverged. While ours continued on its path towards the world wars, Pangea suffered a major tectonic and climatic upheaval, called the {% symbol "Planetary Cataclysm" for "catastrophic_period" %}, which torpedoed all human development for centuries.

The planet has at last emerged, with great difficulty, from this cataclysm, and humanity is taking off again.

The international currency is the **kash** (1 kash buys about 100 loaves of bread).


The {% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}
======================================================================

The Arkon Zarathustra is said to be at the origin of this very powerful planetary bewitchment, still in effect so long after it was set up - at the very beginning of the current era.

On Pangea, anyone who swears something **"By the {% symbol "Oath of Zarathustra" for "unbreakable_oath_name" %}"** is bound by the Heavens to honour their commitment, whatever their own beliefs.

In practice, any perjury will quickly be met with a painful punishment, ranging from infirmity to death, depending on the gravity of the lie. Furthermore, the forces of destiny would combine to fulfil the betrayed promise, in place of its author. Thus, when an eastern knight swore by Zarathustra that he would destroy a malefic well, but went back on his promise, legend has it that not only did he lose an arm in the following battle, but also that oxen left their path to dismantle the well themselves.

Though some people still play the sceptic on this subject, in practice there is no longer a single person who would risk abusing this oath; and except in a few serious cases, people usually prefer to swear on someone's head or on their own honour, which does not commit them to much.

Mystics agree that this oath applies only to *living* Pangeans; the deceased, deities and otherworldly entities are therefore said to use it at times to deceive humans. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}


Deities and alternative worlds
=============================================

Many beliefs coexist on Pangea, appearing and disappearing. Currently, the main deities worshipped are the **Yods** (an infinity within unity), **{% symbol "Bahamoot" for "god_of_diakons" %}** the cosmic dragon, and various Forces of Nature. Among the lesser deities are the Ankou, guide of the dead; as well as the **Djinns**, harmless, learned and invisible beings, who are spread across the whole planet. Rumour has it that many gods and goddesses, angels and demons, are in reality merely the inhabitants of very distant universes, or of other strata of reality.

.. raw:: pdf

   PageBreak

World map of Pangea
==============================

*Geography matters very little in this mystery evening; there is no need to learn these countries and cities.*

[BR]

.. image:: ../assets/pangea_world_map_v10_8bits-rotated.png
    :align: center
    :width: 2000px


{% endmacro %}
<{ common_lore_for_all }/>

.. raw:: pdf

   PageBreak

{% macro common_npc_lore_knowledge() %}

Knowledge of the characters of the Maupertuis era
============================================================

*Here is what all the Avatars and phantoms know, except the Thief; the latter knows a little about the old legends and the context of the sacking of the manor, but that is all. Deliver this information to the players when they question you about it on their own initiative.*


The {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This Magus lived {% symbol "3 centuries" for "mages_war_before_curse_timedelta" %} before the library curse, during the {% symbol "War of the Thirty Sorcerers" for "mages_war_name" %}.

A formidable mage, alchemist and duellist, he defeated all his adversaries. Legend has it that he was invulnerable to magic spells, and could make rain or hail fall on entire cities, whereas his invoker adversaries never affected more than a few ares of ground at a time.

To avoid any poisoning, he had learnt to generate food himself from mere rocks; knowledge that has survived among his descendants in the form of a magic banquet table, located in the library, which transmutes food on its own from the surrounding rocks. {% fact "buffet_table_magically_generates_food" %}

He created the Maupertuis family castle, the buried library, as well as the network of teleportation portals linking it to the domains of his vassals.

He died suddenly during great festivities, as he approached the age of 50, choking on a peach stone. He had not yet passed on his most important secrets to his heirs.

His relatives buried him hastily in a room adjoining the library, in his festive robe, without daring to risk triggering some curse by laying out his body. In particular, as proud as he was of his lineage, the Magus was equally **hateful** towards the "rabble" uninitiated in the magical arts, and legend has it that his grave still resonates with this feeling. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

Since then, each generation of Maupertuis has added its own layer of protections to his tomb, so that no **stranger** ever violates the burial place of this venerable forefather, nor any of the dangerous mysteries he took with him to the grave. To this day, no guild of mages on the planet would probably be capable of breaking so many accumulated bewitchments. But perhaps it is possible to get in by roundabout means, who knows? {% fact "magus_mos_peratys_tomb_is_extremly_well_sealed" %}

*Note: once freed from their anchoring, the phantoms CAN enter the tomb by passing through the walls surrounding it, which are not themselves protected by an {% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %} nor excluded from the {% symbol "Absolute Enclosure" for "library_cursed_enclosure_name" %} surrounding the entire library. They can therefore bring back some information about the contents of the tomb.* {% fact "magus_mos_peratys_tomb_can_be_explored_by_free_phantoms" %}


The etheric necklaces
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Legends speak of several magic necklaces forged by alchemists during this {% symbol "War of the Thirty Sorcerers" for "mages_war_name" %}, and lost shortly afterwards.
It is commonly accepted that the {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %} got hold of several of them. In particular, his drawling but thunderous diction at all his public appearances aroused more than one suspicion. {% fact "magus_mos_peratys_often_wore_manaic_aura_necklace" %}

**{% symbol "Etheric Necklace of Stone Skin" for "etheric_stone_skin_necklace_name" %}** (made of flat, oval, translucent bluish beads): Whoever wears this necklace around their neck becomes immune to physical weapons (blunt, piercing or cutting). In return, they walk and move their arms very slowly, like a golem.

**{% symbol "Etheric Necklace of Vital Force" for "etheric_vital_force_necklace_name" %}** (made of wooden beads): Whoever keeps this necklace around their neck becomes immune to everything that attacks the body from within: diseases, solid or liquid poisons, toxic vapours... In return, they can only breathe through the mouth (noisily), and can neither drink nor eat.

**{% symbol "Etheric Necklace of Manaic Aura" for "etheric_manaic_aura_necklace_name" %}** (made of a quartz on a fine golden chain): Whoever wears this necklace around their neck becomes immune to elemental spells (fire, ice, lightning...) and to malefic bewitchments of objects. In return, they can only speak very loudly and very slowly for as long as they wear it. "Sacred" damage (injuries from phantoms, demons...) is not prevented by this necklace. {% fact "etheric_manaic_aura_protects_from_magic_and_cursed_objects_too" %}

**{% symbol "Etheric Necklace of Blessing" for "etheric_benediction_necklace_name" %}** (made of Mithril rings before being melted into the Arkon's armour): Whoever keeps this necklace around their neck becomes impalpable on the spiritual plane, and can therefore no longer be injured by phantoms, demons, or curses. In return, this requires great physical strength, as this necklace is extremely heavy. {% fact "etheric_benediction_necklace_is_in_arkon_sacred_armor" %}


The magical decline
+++++++++++++++++++++++++++

In the following centuries, the "magical contrast", that is to say the phenomenal power of a few individuals compared to the rest of the population, diminished considerably. Hampered by a taste for secrecy and the limitations of an artisanal practice, the magical and esoteric arts were almost everywhere overtaken by military technologies; they survived mainly in their religious colouring, in connection with the world of the dead.

The great lineages of mages fell one after another, due to internal dissensions, or more or less justified popular aggression.
The Maupertuis lineage held out longer than the others, thanks to a favourable reputation due to its focus on medicinal care.

Since the fall of the family manor, even the buried library, though bristling with protective bewitchments (anti-fire, anti-flood, anti-breakage...), is gradually crumbling; some walls, entirely dispelled, have collapsed. But this process will take many more centuries; and some artefacts continue to preserve, in isolation, the powerful magical flows running through them.


The Forbidden Domain and the Beast
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Maupertuis Forbidden Domain, a floor of the library filled with dangerous secrets, has always been protected by **living monsters**, enchanted to do without food and live long. Pampered in exchange for their good services, these creatures were, from generation to generation, presented to the new Maupertuis heirs, who became their new masters. The identity of these creatures was deliberately hidden, for safety, so that only the Maupertuis heirs knew which species they belonged to.

At the time of the library curse, one guard monster remained, nicknamed "the Beast", in the Forbidden Domain; it probably met a grim fate (the phantoms sometimes hear its mournful cry, but the Avatars do not). It is said to have had the peculiarity of being very short-sighted, **not seeing much beyond 3 m**. {% fact "characters_know_how_the_beast_works_regarding_3m_sight" %}

The entrance to the Forbidden Domain has been protected, since the founding of the library, by an **{% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %}**. This legendary bewitchment spectacularly resists **physical and magical attacks, and can even block phantoms**; this last point is usually anecdotal, as spirits can usually bypass this blockade and pass through the walls (however, the phantoms have not seen any spectre of the Beast wandering on their side of the library). {% fact "beast_cannot_access_normal_zone_because_of_ultimate_seal" %} {% fact "phantoms_cannot_cross_some_fence_enchantments" %}

To temporarily open access to the Forbidden Domain, the **secret symbol of the Maupertuis**, passed down from generation to generation, must be reconstituted on a magic grimoire; access is then unlocked **for 12 hours**. {% fact "secret_family_symbol_needed_for_forbidden_zone" %} {% fact "npcs_know_about_secret_family_symbol_system" %}

Ultimately, among the protagonists of the tragedy, **only Octave had already entered** (accompanied by his parents) this Forbidden Domain. {% fact "only_octave_had_been_in_forbidden_domain" %}


The last Maupertuis household
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Maupertuis parents were very different and complementary; for instance, while {% symbol "Isadora" for "maupertuis_mother" %} had an excellent **memory** and never wrote anything down, {% symbol "Quirinius" for "maupertuis_father" %}, for his part, quickly forgot everything, and had to write down even his most sensitive secrets in notebooks, which he kept well hidden in the library. {% fact "maupertuis_mother_had_excellent_memory_but_not_father" %}

At the time of the attack on the manor, Mérédice de Maupertuis had already made great progress in the magical arts, and in particular - like her predecessors - in healing potions and gems. She regularly worked in the **alchemy and gemmology studies of the Forbidden Domain**. She in fact left most of her belongings in the library, for fear of losing them during her herbalism excursions in the surrounding area, or in case the manor was burgled.

Octave, for his part, had barely begun his apprenticeship, not least because he was distracted by his reading of novels and fantasy. He had therefore never gone alone into the forbidden floor (the Beast would in fact have attacked him in that case). {% fact "octave_would_have_been_attacked_by_beast_if_alone_in_forbidden_domain" %}

He was very soon due to undergo his **initiation called "dubbing"**, a ceremony that only works for heirs of the Maupertuis lineage: {% fact "only_maupertuis_heirs_can_take_initiation" %} {% fact "octave_would_have_been_attacked_by_beast_if_alone_in_forbidden_domain" %}

{% hint "maupertuis_initiation_instructions_for_octave" is needed %}
- Succeed in activating the **Initiation Seal** present on site
- Attempt to determine, solely through his sensitivity to magical auras, which small box, among a set, contained his **personal brooch**, and thus obtain this dynastic artefact {% fact "octave_needed_to_pass_initiation_to_gain_his_jewel" %}
- If successful, **receive the secret symbol** of the Maupertuis family; be presented to the Beast of the Forbidden Domain, and receive from it an oath of allegiance
- If unsuccessful, retry this ceremony in X months.

During his confinement in the library, Octave wore as a keepsake his **mother's brooch**, which he had found on site. {% fact "octave_carried_mother_jewel_after_her_death" %} {% hint 'maupertuis_mother_jewel_on_octave_tomb' is provided %}

In their childhood, Octave and his sister used to create treasure hunts - and other puzzles - for each other. Mérédice had created a particularly mischievous one to celebrate Octave's upcoming dubbing, by pinching his piggy bank full of savings. And she had placed the final riddle leading to this little treasure in the **{% symbol "Whispering Box" for "whispering_box" %} found at the bottom of a wooden chest.** {% hint "whispering_box_with_children_enigma_in_common_brown_chest" is needed %}; the family members used this magic box to leave each other messages, which they listened to by placing a finger on it. {# The players must use a stethoscope to read these messages #} Octave was never able to find his piggy bank, probably because it was hidden in the Forbidden Domain. {% fact "octave_moneybox_hidden_by_meredice_is_lost" %}


The {% symbol "Spectral Bell" for "table_bell_name" %} and the {% symbol "spectral frenzy" for "phantom_frenzy_name" %}
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If someone mentions a **table bell** (small, round and metallic) to you, you know nothing about it; you only know that it was **not visible** in the library during your lifetime (not even to the Thief), so someone must have brought it or taken it out of a hiding place.
The automatons, strangely, ignore the sound of this bell.

If someone presses the bell for the first time, the GM must trigger the unsettling soundtrack of the **{% symbol "spectral frenzy" for "phantom_frenzy_name" %}**. The phantoms then switch to their disembodied form, and rush towards the sound of the bell. Once near it, they wander left and right, not far off, distraught, until the end of the soundtrack, then go back to what they were doing before. {% fact "table_bell_triggers_spectral_frenzy" %}

Afterwards, the bell is supposed to be **temporarily drained** of its magic; the Avatars and phantoms can sense this and tell the players if they press the bell again. *Put black tape on it to show this.* {% fact "table_bell_is_only_usable_once" %}

*Mini-spoiler: It is in reality just a recall signal forgotten by the Ankou during a previous visit, but only the Ankou knows this.* {% fact "table_bell_belongs_to_ankou" %}

{% endmacro %}
<{ common_npc_lore_knowledge}/>



How phantoms work
==============================================

{% macro phantom_knowledge_article() %}

There is very little reliable knowledge about the world of the dead. Many exorcists and mystics attest, however, that sometimes, instead of floating freely towards the afterlife, the deceased can spend years or centuries wandering on Earth, for a wide variety of reasons.

Of the two phantom forms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

It is possible to communicate with a phantom when it is in an "embodied" phase. This is of course a misnomer, as the deceased remains unable to interact normally with the world of flesh and matter; they are nonetheless able to converse, reason, and remember their past life, even if their awareness of their situation can vary greatly. These privileged moments are the best way for an exorcist to understand what is holding a phantom on earth, in order to take corrective measures. These embodiment phases are more frequent and longer when living people are around.

The rest of the time, phantoms wander like aimless "spectres", deprived of most of their intelligence, and attracted to the living only when they come across them at close range. The degree of agitation of these ethereal, disembodied phantoms then depends in part on the weight of their earthly sins {% fact "phantoms_of_sinners_have_faster_specters" %}. But all of them can enter an intense "{% symbol "spectral frenzy" for "phantom_frenzy_name" %}", when they are touched by the waves of some magical or sacred ritual, or at certain significant moments of the day; their movements are then faster, and they seem to seek at all costs contact with the living or with a specific artefact.

Interestingly, phantoms retain a large part of their animal instincts, their likes and dislikes, even when in spectral wandering. {% fact "phantoms_always_keep_most_of_their_instinct" %}

It is established that phantoms can most often pass through walls and objects; however, as they are not entirely dematerialised, this requires extra effort from them, made worse when the place has been protected by magical bewitchments or sacred blessings. In practice, phantoms therefore often follow the same paths as humans. Note that some powerful enchantments can erect walls in the world of the living AND of the dead, thus also preventing the passage of embodied as well as disembodied phantoms. {% fact "phantoms_cannot_cross_some_fence_enchantments" %}


Of the dangerousness of wandering revenants
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Esoteric literature never ceases to warn against the dangerousness of phantoms when they are in their "spectral" phase.

Touching one of these wandering beings, psychically torn between the world of the living and that of the dead, indeed inflicts serious injuries on body and mind; harm that can easily lead to death. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

It is therefore essential not to touch (or let oneself be touched by) a "disembodied" phantom, unless wearing duly blessed protections.

On the other hand, embodied phantoms, endowed with reason, are entirely harmless, and pass through beings without affecting them.


Of spiritual chains
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Phantoms, generally speaking, do not stray far from the place where they once lived.

But people who died violently can find themselves as if anchored, imprisoned near the place of their fall, in the aura of a strange sacred light. They can only become embodied near this glow, although in spectral form they retain greater freedom - if one can call it that. {% fact "beings_dead_violently_are_anchored" %}

People - or even beasts - who died naturally do not seem to have this type of very localised bond, and it is rather unfinished tasks or curses that can hold them in the world of the living. {% fact "beings_dead_naturally_are_not_anchored" %}

Note that an anchored phantom will more often remain in spectral, wandering form than a phantom that is free to move about. {% fact "anchored_phantoms_turn_more_often_into_specters" %}


Of liberation rituals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Many sacred rituals make it possible to drive phantoms away, but it is inadvisable to use them without first analysing the situation, as it is rare for a phantom thus expelled to find, by luck, the way to the afterlife. The same goes for sacred weapons, which are merely primitive forms of exorcism, despite their great usefulness in certain delicate situations. Do not forget that a phantom thus mistreated, once it returns, will be even more disturbed and disembodied than before.

Many seers of the spirit world evoke the role of a "psychopomp", a guide of souls, who roams the Earth to bring phantoms back to the celestial paths. This would explain the sudden disappearance of deceased persons from places that had nonetheless been relentlessly haunted for years. But this enigmatic figure remains a subject of heated theological controversy.


Of the perils of bodily remains
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

People with heavy sins on their conscience, besides being quicker than others to become phantoms, can leave traces of this past in their mortal remains. Such a curse, which materialises as abnormal glows or sounds, can be very dangerous for an ill-advised gravedigger or grave robber; for it inflicts sacred injuries, if they directly touch the skull or bones of the deceased. {% fact "cursed_skull_and_bones_give_sacred_injuries" %}

Note that this spell can persist until well after the phantom's return to the kingdom of the dead, thus requiring the intervention of a Dispeller in due form.

{% endmacro %}
<{ phantom_knowledge_article }/>



Value of precious objects
======================================

{% macro treasures_value_summary() %}

You know the values of coins and gemstones well.

Here, for instance, is how precious items sold, at the best price, in the time of the Maupertuis.

- 1 silver- or bronze-coloured coin is worth 1 kash (whatever its size)
- 1 gold coin is worth 10 kashes in the big cities
- 1 small round diamond is worth 5 kashes in the trading centres of Keroskia
- 1 medium rectangular diamond is worth 10 kashes on the Nimouk market
- 1 large round or rectangular diamond is worth up to 20 kashes in the Axolian lands
- The colour (smoky or not) of diamonds has no impact on their value

Note that these values in kashes have remained broadly constant throughout the History of Pangea, up to the present day.
{% fact "precious_objects_have_kept_same_kash_value_along_history" %}

*Out-of-game NOTE*: As for precious jewels, their estimated value is written on a white label.

{% endmacro %}
<{ treasures_value_summary }/>
