{% macro monolith_found_by_explorers() %}
Fortunately, at that very moment, Heliossarian archaeologists unearthed immemorial monoliths, recounting the first generations of the Maupertuis family. They mentioned, in enigmatic form, the creation of a library buried deep underground, in order to preserve the most powerful magic grimoires of that time. A few photos of these inscriptions leaked to the press, photos which you laboriously deciphered.
{% endmacro %}


{% macro portal_to_library_opened() %}
A few days later, as every year for centuries, a magic portal began to stir on the **{% symbol "winter solstice" for "astral_opening_date" %}**, in the cellar of an old neighbouring castle; a passage allowing one to reach, for a single day only, the Maupertuis secret archives. It was evidently through this spell that this family invited its magician vassals from all over the world to celebrate the new year, even though this tradition had clearly long been forgotten by the time the Maupertuis manor was burned.

It took you more than half a day to work out how this portal functions and to awaken it fully; you have less than **{% symbol "3½ h" for "library_outside_portal_remaining_time" %}** left to explore the premises when you materialise there. But to rummage through an old pile of books, that should be enough, shouldn't it?
{% endmacro %}


{% macro parcival_group_sheet() %}

Faction - The Parcival heirs
============================================

{# Parcival heir - You descend from a great lineage, and have either superhuman strength, or alchemical talents, or gifts of sight #}

The three of you all belong to the most recent generation of the Parcival family, living in the land of Slavinka. A family that has inherited, through its noble lineage, certain affinities with the esoteric world.
One of you thus specialises in the alchemical arts; another occasionally receives omens in the form of visions or voices; the last has developed impressive physical and sensory faculties by connecting with the invisible forces of Nature.

Recently, your little sister **{% symbol "Philomène" for "parcival_sick_child_name" %}** fell seriously ill. **{% symbol "Marbled degeneration" for "legacy_disease" %}**, an affliction that had struck your ancestors many times over the centuries. But one hope remained: it is known that your ancestress, Mérédice de Maupertuis, had been cured of it by her parents in her early childhood. This medicinal knowledge, amassed by her dynasty of healer-mages, has alas largely fallen into oblivion: their manor in {% symbol "Thelassar" for "events_region_name" %} was sacked by fanatics, a tragedy of which Mérédice was evidently the sole survivor. Traumatised, she had entirely rebuilt her life abroad, never seeking to recover the domain that was hers by right.{% fact "parcival_family_is_heir_of_maupertuis" %}

So you set off on the trail of the past, to find this fabulous **{% symbol "Rejuvenation Cocktail" for "parcival_disease_main_remedy_name" %}** that had saved your lineage.

The ruins of the Maupertuis manor, unsurprisingly, yielded no secrets. And time was beginning to run out; {% symbol "Philomène" for "parcival_sick_child_name" %} had only a few months left to live.

<{ monolith_found_by_explorers }/>

<{ portal_to_library_opened }/>

**Specifics**

<{ parcival_group_symbols }/>

{% endmacro %}
<{ parcival_group_sheet }/>
