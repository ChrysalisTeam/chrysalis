**{% symbol "For the glory of Lordania..." for "lordanian_sheet_motto" %}**

<{ title_your_intervention }/>
=================================

The Lordanian intelligence service, to which you belong, sent you to investigate Loyd Georges several weeks ago.

Your code name is **Garnet**; in particular, it is the pseudonym you use to log in to your account on the world network, or to communicate with your intelligence service.

For this mission, you have taken on the identity of **{{character_properties.garnet.full_official_title}}**, a fictitious persona often used by the Lordanian secret services because it has been patiently built up: fake entry in the civic register, bank account activity, etc. You therefore took part in Loyd Georges' auctions with a certain degree of credibility. {% fact 'garnet_is_undercover' as author %} {% fact 'garnet_official_is_fictional_identity' as author %}

Taking on this persona has stirred up a recent wound in you. For years, you were used to working as a duo with agent **"Emerald"**. Back then, he was the one who took on the identity of "{{character_properties.garnet.official_name}}". But he died recently, during a tragic reception organised by the Akarith embassy in Doria. You remember your frantic run through the streets of Nimouk, searching for a dose of adrenaline to restart his heart, which was inexorably slowing down. You promise yourself, clenching your fists, never to lose a comrade again... but also to do in the stranger who poisoned him, if you are ever lucky enough to find him. {% fact 'garnet_lost_colleague_emerald' as author %}

Before you had come to terms with all this, you were asked to build a new team with agent **Amethyst**. You know him well, having taken part with him in several strategic studies on Midolia, and you enjoy his company. Amethyst, for his part, is posing as **{{character_properties.amethyst.full_official_title}}**. {% fact 'amethyst_is_undercover' %}


<{ title_investigation_so_far }/>
======================================

{% macro loyd_georges_orb_certainties() %}
**Loyd Georges has found one of the mythical Akarith Divine Orbs, has hidden it outside his manor, and has said nothing about it either to his household or to his friends, to avoid any leak.** {% fact 'lg_has_found_and_hidden_an_orb' %}
{% endmacro %}{# inserted later #}

{% macro garnet_inquiry_so_far() %}
In trying to get hold of Loyd Georges' artefacts, you have been led, as a duo with your partner, to play a double or even triple game; even if it meant revealing to Doria the cover of a Masslavian agent (we will not be seeing Marduk Pamuk in Doria again for a long time...){% fact 'amethyst&garnet_unmask_masslavian_agent_in_dorian_dukedom' as author %}; or giving Masslavia the location of the Dorians' weapons cache in Mastden (Masslavia){% fact 'amethyst&garnet_unmask_dorian_den_in_masslavia' as author %}; or even fraudulently breaking into a secondary computer account of Loyd Georges, which was unfortunately rather sparse. {% fact 'amethyst&garnet_crack_lg_2nd_web_account' as author %}

These operations were not useless, since you were able to retrace Loyd Georges' movements upon his return from the expedition. By cross-referencing his digital notes with the information pilfered here and there, you were able to determine what mattered most to you:

<{ loyd_georges_orb_certainties }/>

Following a bold hunch, you and your partner led a Lordanian commando in an assault on Loyd Georges' magnificent family vault, in the crypt of the Salima Basilica. You drew a blank, and the incident made the front page of the newspapers... {% fact 'amethyst&garnet_open_lg_family_tomb' as author %}

In short, you are making laborious progress in this Loyd Georges affair, and the Divine Orb remains a danger: it could serve as a pretext for the Akarith leaders to launch a "prophetic" war, rally the various Akarith clans (rather sceptical for the time being) to their cause, and build themselves an empire capable of rivalling Lordania; unless this regional conflict ruins Midolia, which would rather be good news for your homeland. What is certain is that you still do not know how this orb works, nor the extent of its powers.

In any case, you keep on weaving your web, and as soon as Loyd Georges makes the slightest misstep, you have (almost) no doubt about it, his orb will fall under your control.

{% endmacro %}

<{ garnet_inquiry_so_far }/>

Note: you had personally tried to hire a pickpocket, to relieve Loyd Georges of his notes, but it seems that faced with the media hype around this affair, the delinquent got cold feet... {% fact 'garnet_attempts_lg_pickpocketing' as author %}


<{ title_specific_information }/>
==================================

In the course of your investigation, you have been able to observe the intrigues of several participants in Loyd Georges' auctions.

Such as the so-called {{character_properties.spinel.full_official_title}}, who has wiretapped Loyd Georges and scholars from the Alifir Academy. The trail is easy to find, provided one thinks of looking at the system's event logs, on the "AlifirFront176" telephone gateway. {% fact 'spinel_wiretaps_lg_and_friends' %}

A certain "{{character_properties.topaz.official_name}}", for his part, met up with a minor henchman of a big mafia, on the evening of the first auction, to resell at a better price - and without paying taxes to Sabarim - the few lots of gems he had bought. {% fact 'topaz_sells_gems_at_black_market' %}









