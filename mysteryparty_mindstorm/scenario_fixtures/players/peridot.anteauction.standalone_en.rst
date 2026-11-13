**{% symbol "Compromise or death" for "dorian_sheet_motto" %}**

<{ title_your_intervention }/>
================================

The Dorian intelligence service, to which you belong, sent you to investigate Loyd Georges and his circle several weeks ago.

Your code name is **Peridot**; it is notably the pseudonym you use to log in to your account on the world network, or to communicate with your intelligence service.

For this mission, you have taken on the identity of **{{character_properties.peridot.full_official_title}}**; the holder of that name, for his part, was offered a fat sum of money in exchange for his silence. He is as happy as can be, his finances are saved, and he keeps a low profile in his shop. {% fact 'peridot_is_undercover' as author %}{% fact 'peridot_official_was_bribed' %}{% fact 'peridot_official_is_still_in_shop' %}

You work as a duo with **Topaz**, an agent you know well, who for his part uses the fictitious identity of **{{character_properties.topaz.full_official_title}}**. You both thus took part in Loyd Georges' first auction, with a degree of credibility. {% fact 'topaz_is_undercover' %}


<{ title_investigation_so_far }/>
============================================

You began your little investigation by strolling around Loyd Georges' hamlet, near Salima; the idea was to see whether the neighbours and shopkeepers had anything interesting to tell. The investigation proved rather fruitless, Loyd Georges being a fairly secretive man. And the height of uselessness was reached when the local apothecary, Master Florent – delighted to have an audience - held you up for a good hour; he told you his life story at length, from his apprenticeship with a certain Master Bibine, on Arsenic Street in Salima, to his settling here, in a godforsaken little town. In short, the character drained a whole year's worth of patience out of you. {% fact "peridot_talked_with_master_florent" as author %}

Fortunately, your colleague was luckier, discovering (thanks to phone taps) that Professor Loakim, an archaeologist at the Alifir Academy and a friend of Loyd's, most likely knew a great deal about the artefacts found in the buried temple. {% fact 'lg_gave_responsibilities_to_loakim' %}

{% macro dorian_failed_abduction() %}
You therefore planned, as a duo with your colleague, and with the support of local mercenaries, the abduction of Prof. Loakim. But the prompt intervention of Sabarith law enforcement turned this operation into a rout; a good thing you had covered your tracks well... {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
{% endmacro %}
<{ dorian_failed_abduction }/>

You subsequently tried to burgle Loyd Georges' manor by night, alone; but as was to be expected, the security systems in place were already far too sophisticated, and you had to give up. {% fact 'peridot_robs_lg_manor_fail' as author %}

Despite these failures, by cross-checking information you were able to determine what mattered most to you:

<{ loyd_georges_orb_certainties }/>


{% macro dorian_investigation_conclusion() %}
In short, you are making laborious progress in this Loyd Georges affair, and the Divine Orb remains a danger: it could serve as a pretext for the Akarith leaders to launch a "prophetic" war, rally the various Akarith clans (currently rather sceptical) to their cause, and build themselves an empire; without it being certain, for now, that Doria would be accepted among their allies. Moreover, you still do not know how these orbs work, nor the extent of their powers.

But you keep weaving your web, and as soon as Loyd Georges makes the slightest misstep, you have (almost) no doubt, his orb will fall under your control.
{% endmacro %}
<{ dorian_investigation_conclusion }/>


<{ title_specific_information }/>
=================================

News of a burglary in a private warehouse in Alifir caught your attention; fearing a link with your case, you identified the leader of the mercenary group that pulled off the feat. By having him tailed by one of your informers, you learned that he had had a conversation with a certain "Malachite". {% fact 'malachite&spinel_rob_alifir_warehouse' %}

One of your contacts at Salimacom (Salima's telephone & web company) got in touch to tell you he had found some curious network activity during a call from Professor Loakim to Loyd Georges; using a little home-made program, he was able to trace the origin of the strange signal (timestamped "A827IZJ76"): the web account of a certain "Spinel". {% fact 'spinel_wiretaps_lg_and_friends' %}

Finally, you strolled around the Salima flea market, and introduced yourself to a dealer under your "official" identity. He then took you to his back room, and offered to sell you, for cash, artefacts and gems "of very high quality". You recognised pieces sold by Loyd Georges during his auctions. After obtaining the gracious cooperation of the seller and his fence, through the most shameless blackmail ("these objects belong to Mr Georges, who is a friend of mine, and I'll report you to the police if you don't tell me who supplied them to you!"), you finally understood that these pieces had been resold via Pangeaweb by a certain "Amethyst", who apparently cares little for the country's commercial laws. {% fact 'amethyst_sells_items_at_black_market' %}


