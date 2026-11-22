{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- get your hands on Loyd Georges' orb {% xfact 'agent_mission_seek_lg_orb' %}
- get your hands on the Panorbium Fortuna {% xfact 'agent_mission_find_panorbium_fortuna' %}
- investigate the Professor Voluto affair {% xfact 'agent_mission_investigate_voluto' %}

- your short-term objectives:

  - <{ orb_search_short_term_objectives }/>


<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- you have taken on the fictitious identity of {{character_properties.topaz.full_official_title}} {% xfact 'topaz_official_is_non_existent' as author %}
- you claim to work for {% symbol "Count Adamor" for "lg_remote_friend_lord_name" %}, a distant acquaintance of Loyd Georges who has gone on a cruise {% xfact 'topaz_pretends_working_for_count_adamor' as author %}
{% endif %}
- you are teamed up with agent Peridot
{% if standalone %}
- you know that Loyd Georges has discovered one of the Divine Orbs and hidden it away {% xfact 'lg_has_found_and_hidden_an_orb' %}
- you discovered that Loyd Georges had heavily involved Professor Loakim in his affairs {% xfact 'lg_gave_responsibilities_to_loakim' %}
- you attempted, as a duo, to abduct this Professor Loakim, alas without success {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- your colleague tried to burgle Loyd Georges' manor, but without success {% xfact 'peridot_robs_lg_manor_fail' %}
{% endif %}

{% if standalone %}
- "{{character_properties.amethyst.official_name}}" is in reality a Lordanian agent, the real bearer of the name is hospitalised for venereal diseases {% xfact 'amethyst_official_has_venereal_disease' %}
- it is a Masslavian agent with the pseudonym "Malachite" who recently triggered an Akarith riot in Doria {% xfact 'malachite_triggers_akarith_riot_in_dorian_dukedom' %}
{% endif %}

<{ peridot_and_topaz_meeting_with_lg_summary }/>


<{ title_last_minute_information }/>
==============================================

- Panorbium Fortuna: Prof. Loakim's deputy, **Ernest De Villeneuve**, is said to have brought it to Sabarim in a briefcase; in Nuxia, he bought a **brown canvas bag and a set of work overalls**; and apart from the guests and the couriers on horseback, only 3 delivery lorries made their way to the manor, between {% symbol "9:00 and 10:00" for "morning_delivery_trucks_time" %} {% xfact 'misc_panorbium_fortuna_brought_to_manor_in_bag' %}
- you have convincing *network traces* *(a document to write yourself, freely, before the evening)*, showing that a certain "Amethyst", of the Lordanian secret services, had tapped the phone of the patriarch of Ghek, from the vicinity of Salima. {% xfact 'amethyst_wiretaps_ghek_patriarch' %}
- a certain "Phonphonse" from the manor is trying to sell a "Chromia" pen that could be a spying device  {% xfact 'alphonse_has_found_library_spy_recorder' %}
- the famous {{character_properties.opal.official_name}} used to log in to a high-security web account with the login "Emerald", which appeared to be read-only  {% xfact 'opal_accesses_emerald_agent_web_account' %}
- in the event of an alliance with Akaris, the recognition sign with the Akariths would be "{% symbol "arms crossed over the chest" for "dorian_akarith_alliance_sign" %}" {% xfact "dorians_have_alliance_sign_with_akariths" %}



{% if standalone %}
<{ title_past_infractions }/>
===============================

Here are the deeds you have been guilty of during these first few weeks of operations:

- unlawful interception of communications (phone-tapping of people in Salima) {% xfact 'topaz_wiretaps_lg_and_friends' as author %}
- (failed) attempted abduction of Prof. Loakim, a friend of Loyd Georges {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- tax fraud (resale of gems from the auctions on the black market) {% xfact 'topaz_sells_gems_at_black_market' as author %}
- identity theft (see your official "cover") {% xfact 'topaz_is_undercover' as author %}
{% endif %}



