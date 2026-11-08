{{ current_player_id.upper() }}
##################################


<{ title_main_missions }/>
=============================================================

{% macro orb_search_short_term_objectives() %}for Loyd Georges' Orb, find the answer to his secret question ("{{ character_properties['loyd.georges'].secret_question }}"), and acquire artefacts well suited to geolocation by the World Scanner{% endmacro %}

- get hold of Loyd Georges' Orb {% fact 'agent_mission_seek_lg_orb' %}
- obtain a lease for the tar sands deposit {% fact 'agent_mission_obtain_mining_lease' %}

- retrieve from the Oberons the reports on the balance of military forces in Midolia, authenticate them, pass them on to us, then stay on the alert for anything related to this subject {% fact 'agent_mission_study_midolian_armies_balance' %} {% hint "heliossar_spy_reports_on_akaris_armament" is needed %}

{% macro lordanian_berserk_mission_summary() %}
- help Loyd Georges and {{character_properties.opal.official_name}} to be guinea pigs for the Berserk Elixir {% fact 'agent_mission_investigate_berserk_elixir' %} {% hint "berserk_elixir_advanced_ingredients_for_amethyst" is needed %} {# duo mission #}
{% endmacro %}
<{ lordanian_berserk_mission_summary }/>

- your short-term objectives:

  - <{ orb_search_short_term_objectives }/>



<{ title_major_recent_facts }/>
=========================================================

- you have borrowed, without his knowledge, the identity of {{character_properties.amethyst.full_official_title}}, who is being treated for a shameful disease  {% fact 'amethyst_official_has_venereal_disease' %}
- you are teamed up with agent Garnet, who recently lost his colleague "Emerald" in Doria (and inherited his fake identity) {% fact 'garnet_lost_colleague_emerald' %}
- you know that Loyd Georges has discovered one of the Divine Orbs and hidden it away {% fact 'lg_has_found_and_hidden_an_orb' %}
- you have unmasked the Dorian bidders as being the secret agents "Topaz" and "Peridot" working for Doria; their "official characters" are respectively "non-existent" and "still in his shop" {% fact 'topaz_official_is_non_existent' %} {% fact 'peridot_official_is_still_in_shop' %}

- the day before:

  - you offered a sealed bottle of blue digestive liqueur to Loyd Georges, during the interview at {% symbol "11:00" for "lg_meeting_time_for_amethyst" %}, but learned nothing from it {% fact 'amethyst_offers_liquor_to_lg' as author %}
  - then you disabled the surveillance cameras to explore the manor {% fact 'amethyst_disabled_surveillance_cameras' as author %}
  - you ran into {{character_properties.malachite.official_name}} hiding in the pantry {% fact 'amethyst_and_malachite_locked_in_pantry' as author %}
  - you retrieved a letter for Loyd Georges, but lost his thin brown parcel on your way out {% fact 'amethyst_has_stolen_manor_letter' as author %} {% fact 'amethyst_has_lost_thin_manor_parcel' as author %} {% hint "stolen_manor_letter_for_amethyst" is needed %}
  - after fruitless investigations, you went to bed very early on the {% symbol "8th floor of the SalimaGlobeCenter Hotel" for "amethyst_hostel_room" %} {% fact "amethyst_alibi_is_void" as author %}



<{ title_last_minute_information }/>
=============================================

You know some "Gems of Sabarith Law", such as the one about a romantic break-up preventing a police interrogation, or the one about wearing gloves always being allowed.{% fact 'amethyst_knows_misc_absurd_sabarim_laws' as author %}



<{ title_past_infractions }/>
======================================================

.. Here are the actions you have been guilty of during these first weeks of operations:

- desecration of Loyd Georges' family vault (Lordanian commando)  {% fact 'amethyst&garnet_open_lg_family_tomb' as author %}
- unlawful interception of communications (wiretapping of the patriarch of Ghek) {% fact 'amethyst_wiretaps_ghek_patriarch' as author %}
- computer hacking (Loyd Georges' secondary account) {% fact 'amethyst&garnet_crack_lg_2nd_web_account' as author %}
- tax fraud (resale of small artefacts on the black market) {% fact 'amethyst_sells_items_at_black_market' as author %}
- identity theft (see your official "cover") {% fact 'amethyst_is_undercover' as author %}

