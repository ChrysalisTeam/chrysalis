
<{ diakon_group_sheet }/>

Your abilities
====================================

<{ diakon_sheet_intro }/>

But your vocation soon imposed itself on you: Exorcist, that is, the one who knows the world of spirits and its rules, and has various rituals at his disposal to counter it.

Refer to **the article in the appendix** for a detailed description of the world of the dead; knowledge that you will be able to teach theatrically to your allies during the game, when the subject comes up.


Exorcism Rituals
+++++++++++++++++++++++++++++++++++++++++++++++

Your rituals require artefacts, gestures, invocations, and sometimes the use of potions in support of your psychic strength.

*Out-of-game note: feel free to simulate the exhaustion that the most demanding of these exorcism rituals cause you, even collapsing to your knees after one of them.*

You had brought in your pockets some **Potions of Charm and of Focus** for your usual rituals; you also had **one dose of Lotion of Revelation**, entrusted to you with mysterious insistence by the oracle of the monastery.
However, through carelessness, you **dropped** them at some point - hard to tell whether it was before or after the leap through the teleportation portal. Confound it. But perhaps you will find something on site to restock, anyway.
{% hint 'potion_of_focus_from_exorcist' is needed %} {% hint 'potion_of_charm_from_exorcist' is needed %} {% hint "potion_of_revelation_from_exorcist" is needed %} {% fact "diakon_exorcist_lost_potions_bag_found_by_lockpicker" %}
{% macro phantom_related_spells() %}


Weapon Blessing
-----------------------------------------

You are able to bless a handheld weapon, or a piece of ammunition (arrow, bullet...), so that it has a hold on the entities of the world of the dead.
Weapons thus made sacred cannot of course really injure or kill beings that are already dead; but through the mystical impacts they inflict, they can drive off aggressive phantoms, and weaken their link to the world of the living; this latter effect condemns them to spend a greater proportion of their time in spectral form, between two embodiments. {% fact "diakon_exorcist_can_bless_parcival_woodsman_arrows" %}

This blessing only works on noble metals: **Palladium, Iridium, Platinum, or Mithril**.

Ritual:

- Take a sip of Potion of Focus {% hint "potion_of_focus_from_exorcist" is needed %}
- Lay your hands on the handheld weapon or the ammunition presented
- Proclaim **"Weaponry that wounds the flesh, wound the soul as well"** {# (or else the Latin version: "Tu et caro dolet, et anima nocere") #}


Spirit Expulsion
-----------------------------------------

You are able to drive off a creature of the world of the dead, to make it leave a possessed body, or simply to send it far away from you; this systematically makes it revert to spectral, disembodied form, if it was not already in it (but only for a few minutes). The spirit thus driven off will flee at random, avoiding the place it was driven from, yet without being able to cross the possible spiritual barriers that usually hold it back when it is a spectre. {% fact "diakon_exorcist_can_chase_away_beast_temporarily" %}

As this exorcism is psychically exhausting for you, you can only perform it once every **{% symbol "10 minutes" for "phantom_eviction_cooldown" %}**. It affects only one spirit per invocation.

Ritual:

- Raise your arms to the sky, palms facing the phantom
- Shout **"By {% symbol "Bahamoot" for "god_of_diakons" %}, begone, wandering spirit"** {# (or else the Latin version: "Vade retro, mali spiritus OUDATED") #}


Spirit Charm
-----------------------------------------

You are able to charm a creature of the world of the dead, whether it is in embodied or spectral form; it does not change form, but it is irresistibly drawn towards you for 30 seconds, while moving particularly slowly. This does not, however, allow it to pass through the obstacles that would usually block it. {% fact "diakon_exorcist_can_attract_slowed_beast_temporarily" %}

As this exorcism is psychically exhausting for you, you can only perform it once every **{% symbol "10 minutes" for "phantom_charm_cooldown" %}**. It affects only one spirit per invocation.

Ritual:

- Take a sip of Potion of Charm {% hint "potion_of_charm_from_exorcist" is needed %}
- Cross your arms over your heart
- Shout **"By {% symbol "Bahamoot" for "god_of_diakons" %}, dawdle towards me, wandering spirit"** {# (or else the Latin version: "Venite ad me errantes spiritu") #}


Spiritual Anchor Release
-----------------------------------------

If you come across a phantom stuck in a small area - typically the place of its violent death - while it is in embodied form, this ritual lets you free it from this invisible chain. Like all phantoms, it will nonetheless remain subject thereafter to the constraints of a possible {% symbol "Absolute Barrier Seal" for "ultimate_seal_name" %}, or other magic wall, raised in its path. {% fact "phantoms_cannot_cross_some_fence_enchantments" %}

Ritual:

- Gather **2 other {% symbol "initiates" for "ritualist_kind_name" %}**, besides yourself, in a circle around the embodied phantom
- All three of you stand with your arms stretched out horizontally
- Proclaim all together **"Wandering spirit, we break the chains that hold you"**, three times in a row

According to mystical literature, a phantom thus freed from its spiritual chains will shift into its spectral form far less often. {% fact "anchored_phantoms_turn_more_often_into_specters" %}

**Cancellation**: any of the initiates who took part in the ritual can, as long as the phantom has not passed on to the afterlife, restore the invisible chain that tied it to a specific spot. One simply has to hold out open palms towards the embodied phantom, and proclaim **"Wandering spirit, I restore the chains that held you"**. The phantom will then return to its original anchoring location. This cancellation has been used in the past to curb phantoms that had become too talkative or indiscreet. {% fact "diakons_can_all_anchor_phantoms" %}

{% endmacro %}
<{ phantom_related_spells }/>


Global Otherworld Corridor Rupture
------------------------------------------

You are able to cut the bridges that exist between disjoint worlds, such as the portals that some sorcerers open towards the world of spirits, or towards other parallel worlds. {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

The greatest mystics are able to perform this rupture selectively, breaking only one corridor - attached to a specific object - at a time. But your exorcism is somewhat cruder, and will annihilate all the inter-world attachment points located within a radius of 100 paces around you.

Ritual:

- Use an activated {% symbol "canonical pentacle (5-pointed star in a circle)" for "standard_pentacle_description" %}
- Place at the centre of this pentacle as many objects attached to otherworld corridors as possible (cursed talismans, Avatar books...)
- The presence of additional {% symbol "initiates" for "ritualist_kind_name" %} around the pentacle is advisable, but not essential
- Stretch your right arm towards the portal, fingers spread wide
- Proclaim this incantation on a loop: **"By the victorious sun, By the power of the heavens, Portals, vanish"** for at least **30 seconds**
- It is important to remain perfectly **still** during the incantation, otherwise the pentacle may be destabilised (it briefly goes out) and this delays the completion of the ritual

Beware, this exorcism only works smoothly if all the entities that came into this world through one of the corridors present have **returned** to their world, or failing that are placed **inside** the pentacle. Otherwise, the ritualist will meet with mystical resistance, and the invocation will not be resolved after the usual time. If the officiant then continues his invocation for **a further 30 seconds**, this will force the completion of the ritual, but with the dramatic consequence of **"killing"** the said otherworld entities still present; whatever that means in concrete terms, so unnatural is this situation.
{% fact "diakon_exorcist_might_kill_remaining_avatars_with_expulsion_ritual" %}

{# WRONG Note that it is possible, in a single invocation, to break several otherworld corridors at once, but to do so the objects linked to each of these corridors must be placed in the pentacle, and above all there must be as many Diakons taking part in the ritual gestures and incantations as there are corridors to close.
 OUTDATED proclaim "Portal to other worlds, I conjure you, close your threshold forever" repeatedly for 30 seconds, arms raised (or else the Latin version: "Porta ad alios mundos, sigillum tuum limen") #}



Your knowledge of the different types of injuries
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You know that there are different types of injuries, sometimes natural, sometimes supernatural, but the teaching you were supposed to attend on this subject was postponed time and again... so much so that for now you are reduced to calling upon your fellow Diakons whenever someone around you gets injured by a wandering spirit. The height of irony for an exorcist!



Encyclopedia of the Spirit World
===================================================================

<{ phantom_knowledge_article }/>


