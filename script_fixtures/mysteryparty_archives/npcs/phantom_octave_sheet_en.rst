
Phantom - Octave de Maupertuis
##################################

Your story
=======================

Your profile
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

<{ phantom_octave_character_summary }/>


An unexpected awakening
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

When the Arkon intruded into the library, you eventually came round to his arguments.

As you were packing your things, your heart heavy at having to leave your avatar friends forever, you felt a sharp burning in your back.

{% macro maupertuis_phantoms_awakening() %}

You woke up a little later, your memory blurred, your body almost numb. The world was slipping through your fingers.
Thanks to your good education, you quickly understood. You had become a phantom.

You still do not know what happened during the Arkon's ritual. Who attacked you? The Arkon? The Beast? An unexpected intruder? A latent curse of the library, perhaps linked to the unfathomable powers of the founder of the Maupertuis dynasty, the {% symbol 'Magus Mos Peratys' for 'maupertuis_dynasty_founder' %}?

This kind of situation never lasts forever. So you wait, oscillating between moments of lucidity - in which you are as if bound to a small lit area, and see wandering spectres pass by in the distance - and strange nightmares in which you roam the library, in the grip of a supernatural rage.

{% endmacro %}
<{ maupertuis_phantoms_awakening }/>


Knowledge shared with the Archivist
==========================================

{% macro octave_and_archivist_common_knowledge_for_sheets() %}

IMPORTANT: The Maupertuis family kept some "administrative paperwork" in a black briefcase, in the authorised domain. You had heard that the family's **secret symbol**, opening access to the Forbidden Domain, was also hidden there.
{% fact "octave_and_archivist_know_about_secret_family_symbol_infamily_briefcase" %}

The code of this small case changed automatically every day. The current digits were **whispered by a fake book, {% symbol "Venture Prins" for "small_wooden_fake_book_name" %}**. *Make sure you memorise the shape (thick, made of brown wood) and the approximate location of this fake book.*

You had searched this briefcase in vain, the two of you, while taking care, because it is **partially trapped** against intruders. {% fact "octave_and_archivist_know_about_venture_prins_book_location" %} {% fact "octave_and_archivist_have_searched_family_briefcase" %} {% fact "octave_and_archivist_know_about_trap_of_family_briefcase" %} {% hint 'trap_in_family_briefcase' is needed %}

You can point out the location of the wooden box to anyone who asks you **(see Game Map)**.

Moreover, you heard many things, from the Maupertuis parents, about the dangerousness of **the Beast**, so if the players want to open the passage to the Forbidden Domain, you urge them to first have a plan to neutralise it, in whatever form it shows the tip of its snout. {% fact "octave_and_archivist_warn_players_about_beast_dangerousness" %}

You no longer remember the exact species this Beast belonged to. Just that it was a very clawed creature, usually living in caves. {% fact "only_arkon_knows_things_about_beast_species" %}

Back in the day, you had heard the Maupertuis speak several times of a **"Yodic Book of the Dead"**, the **{% symbol "Thanatologue" for "book_of_the_dead" %}**, said to be one of the most dangerous grimoires in the library. It was kept in a chest in the Forbidden Domain, locked by **two secret codes**, each kept by one of the Maupertuis parents. {% fact "octave_and_archivist_know_about_thanatologue_location_and_double_code" %} {% hint 'family_legendary_chest_protected_by_double_code' is needed %}

You may be sad to realise, at some point, that the Diakons belong precisely to the cult of {% symbol "Bahamoot" for "god_of_diakons" %}, the cult that had the Maupertuis manor sacked long ago.

Octave had an old favourite childhood book with running animals, as an optical illusion (this is useful for the puzzle of Mérédice's {% symbol "Whispering Box" for "whispering_box" %}).

{% endmacro %}
<{ octave_and_archivist_common_knowledge_for_sheets }/>

Specific information and instructions
========================================

You have kept a childlike spirit, and you sometimes accost the players in unlikely ways, telling them anecdotes about your close childhood relationship with your sister, asking them what their favourite book or reptile is, asking them what it is like "outside" now...

If you are told that your sister Mérédice actually survived the persecutions that destroyed the manor, you are filled with enthusiasm; better still, if you meet her distant descendants (your great-great-great...grandnephews and nieces), you overflow with affection and gratitude towards them.

You know that your sister kept her most precious belongings in her small occult-studies study, in the Forbidden Domain. You have never seen this study with your own eyes. And when visiting the domain in question, you see nothing resembling such a thing; perhaps behind some rubble?
{% hint "maupertuis_daughter_jewel_under_rubbles_beyond_alchemist_laboratory" is needed %} {% fact "octave_has_hints_about_location_of_maupertuis_daughter_jewel" %}

The Archivist told you that he had found, and properly filed, certain old potion recipes that had been useful in saving your sister Mérédice in her childhood. {% fact "archivist_knows_about_meredice_rejuvenation_cocktail_recipe_location" %} {% fact "archivist_has_marked_locations_of_rejuvenation_cocktail_subrecipes" %}

If someone talks to you about the **Maupertuis treasure**, you know that the family had a wealth-generating artefact, in the Forbidden Domain. The magic code to use it changes every day, you were told. {% fact "treasure_code_changes_magically" %}

During your final preparations, you had started gathering **a little money** in your travel bag, at least the money that had not been mischievously hidden by your sister before the sacking of the Maupertuis manor. If this travel bag can no longer be found, either someone stole it, or it was simply buried under one of the **rockfalls** that have occurred since; you do not know where. {% hint 'travel_bag_with_money_under_far_rubbles' is needed %} {% fact "octave_moneybox_hidden_by_meredice_is_lost" %}

You had also started a diary, at the time of departure, just before your death. {% hint 'octave_private_diary_on_his_tomb' is needed %}

{# ABORTED FOR NOW As a small child, you had received from your parents your personal secret symbol, one of the keys needed to access the Maupertuis Forbidden Domain. This symbol was ultimately of no use to you, but now that you are dead, it has strangely appeared on your arm. -% fact "octave_has_secret_personal_symbol_on_arm" %- #}


Farewell speech to the players
===================================

<{ octave_epilogue_speech }/>