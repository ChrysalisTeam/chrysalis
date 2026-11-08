**{% symbol "Liberty or death" for "masslavian_sheet_motto" %}**

<{ title_your_intervention }/>
====================================

The Masslavian intelligence service, to which you belong, sent you to investigate Loyd Georges several weeks ago.

Your code name is **Malachite**; in particular, it is the handle you use to log in to your account on the world network, or to communicate with your intelligence service.

For this mission, you have taken, without his knowledge, the identity of **{{character_properties.malachite.full_official_title}}**. The real bearer of the name, a Masslavian patriot of the kind they no longer make, has stayed with the secret services along with his relatives, to advise you if need be, in particular on your supposed knowledge of the Yodic religion and its faithful. {% fact 'malachite_is_undercover' as author %} {% fact 'malachite_official_is_helping_secret_services' as author %} {% fact 'malachite_official_is_expert_in_yodic_history' %}

Teamed up with agent **Spinel**, whom you know well, you have settled into a shabby flat in Salima, above the premises of "Master Bibine, apothecary". You have thus taken part in Loyd Georges' auctions with a certain degree of credibility, and spied on the various participants. Spinel, for his part, is posing as **{{character_properties.spinel.full_official_title}}**. {% fact 'spinel_is_undercover' %}


<{ title_investigation_so_far }/>
=====================================

Thanks to your connections in the underworld, you have set up surveillance of Loyd Georges' postal communications. {% fact 'malachite_spies_on_lg_postal_mail' as author %} You thus learned that he had stored part of his archaeological loot in a private warehouse in Alifir. You and your accomplice hired the services of mercenaries to seize it, but you found the container empty. Either Loyd Georges had been tipped off, or spies from another faction had beaten you to it. {% fact 'malachite&spinel_rob_alifir_warehouse' as author %}

Your colleague then wanted to burgle Loyd Georges' manor, but the security systems had become too sophisticated, and he was nearly arrested. {% fact 'spinel_robs_lg_manor_fail' %}

Following these fruitless attempts, you decided, on your own, to manipulate a few Akarith faithful in order to trigger a riot in the capital of the Dukedom of Doria; relations between the Dorian government and the Order of the Akarith Judicators cooled somewhat after that. {% fact 'malachite_triggers_akarith_riot_in_dorian_dukedom' as author %}


{% macro masslavia_investigation_conclusion() %}

Despite the failures, you were able to determine, by cross-checking the information, what mattered most to you:

<{ loyd_georges_orb_certainties }/>

In short, you are making laborious progress in this Loyd Georges affair, and the Divine Orb remains a danger: it could serve as a pretext for the Akarith leaders to launch a "prophetic" war, rally the various Akarith clans (rather sceptical for the time being) to their cause, and build themselves an empire by crushing the surrounding countries - including your homeland. All the more so since you still do not know how this Orb works, nor the extent of its powers.

But you keep on weaving your web, and as soon as Loyd Georges makes the slightest misstep, you have (almost) no doubt about it, his Orb will fall under your control.

{% endmacro %}
<{ masslavia_investigation_conclusion }/>


<{ title_specific_information }/>
==================================

By hacking into the electronic mailboxes of other auction participants, you discovered that "{{character_properties.garnet.full_official_title}}" and "{{character_properties.amethyst.full_official_title}}" were in fact Lordanian spies, with the respective code names Garnet and Amethyst. Agents probably faithful to the Lordanian tradition, that is to say manipulating and betraying just about everyone depending on the balance of power, so that Lordania remains an undisputed power on the world stage. {% fact 'amethyst_is_undercover' %} {% fact 'garnet_is_undercover' %}

You remember rumours that went around the secret services: a Lordanian agent called "Emerald" is said to have been turned by the Akariths, and tasked with poisoning, on their behalf, a rich desecrator who also hailed from Lordania. But the affair is said to have ended with this "Emerald" poisoning himself, during an evening at a Dorian embassy. The Lordanians seem to want to avenge the death of this agent, without knowing the truth about this event. Life is decidedly ironic. {% fact 'opal_killed_emerald_agent' %}

The Masslavian services operating undercover in Sabarim are not really a match for their adversaries. So when they discovered that the cellar of the {% symbol "Café Bargarac in Alifir" for "akarith_sect_den_bar" %} served as a base for a small band of Akarith assassins, the "Purifiers", they did not attempt to attack it. At most they issued "safety advisories", because these fanatics only go after people who have desecrated Yodic sacred objects; and your superiors decided to wait for the end of the Loyd Georges operation, before mentioning it to the Sabarith State. {% fact 'misc_akarith_assassins_den_in_alifir_ignored_by_masslavians' %}

