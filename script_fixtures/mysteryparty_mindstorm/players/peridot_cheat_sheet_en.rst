{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- get your hands on Loyd Georges' Orb {% fact 'agent_mission_seek_lg_orb' %}
- obtain a lease for the tar sands deposit {% fact 'agent_mission_obtain_mining_lease' %}
- convince the Akarith council of the doctrinal purity of the Dorians {% fact 'agent_mission_transfiliation_attempt' %} {% fact "peridot_must_answer_akarith_council" as author %}

- your short-term objectives:

  - <{ orb_search_short_term_objectives }/>


<{ title_major_recent_facts }/>
=========================================================

- you have taken on the identity of {{character_properties.peridot.full_official_title}}, with the agreement of the real person, who has stayed quietly in their shop {% fact 'peridot_official_was_bribed' %}{% fact 'peridot_official_is_still_in_shop' %}
- you are teamed up with agent Topaz
- you know that Loyd Georges has discovered one of the Divine Orbs and hidden it away {% fact 'lg_has_found_and_hidden_an_orb' %}
- your enquiries in the neighbourhood yielded nothing, apart from an endless conversation with Master Florent, apothecary and former apprentice of Master Bibine of Salima {% fact "peridot_talked_with_master_florent" as author %}
- you know from your partner that Loyd Georges had heavily involved Professor Loakim in his affairs {% fact 'lg_gave_responsibilities_to_loakim' %}
- you attempted, as a duo, to abduct this Professor Loakim, alas without success {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- a certain "Malachite" seems responsible for a recent burglary in a private warehouse in Alifir {% fact 'malachite&spinel_rob_alifir_warehouse' %}
- a certain "Spinel" spied on the telephone communications between Loyd Georges and Professor Loakim {% fact 'spinel_wiretaps_lg_and_friends' %}
- a certain "Amethyst" resold on the black market small artefacts from the auctions {% fact 'amethyst_sells_items_at_black_market' %}

{% macro peridot_and_topaz_meeting_with_lg_summary() %}
- the day before:

  - together with your partner, you met Loyd Georges at {% symbol "15:00" for "lg_meeting_time_for_peridot_topaz" %}, in his manor
  - wary at first, he ended up swallowing your tall tales, but alas taught you nothing you did not already know
  - you then spent a colourful evening at the {% symbol "Luxor Excelcis" for "peridot_topaz_alibi_club_name" %} club in Salima, still with your partner {% fact "peridot_topaz_alibi_is_strong" as author %}
{% endmacro %}
<{ peridot_and_topaz_meeting_with_lg_summary }/>


<{ title_last_minute_information }/>
==============================================

- two elegant people came out, the day before at around noon, through the basement window of the manor's pantry, before leaving the grounds by the main gate; one of them seemed to have lost something in their flight  {% fact 'amethyst_and_malachite_locked_in_pantry' %} {% fact 'amethyst_has_lost_thin_manor_parcel' %}
- you are carrying a sheet on "The Origin of Precious Stones"  {% hint "origins_of_precious_stones_for_peridot" is needed %}
- in the event of an alliance with Akaris, the recognition sign with the Akariths would be "{% symbol "arms crossed over the chest" for "dorian_akarith_alliance_sign" %}" {% fact "dorians_have_alliance_sign_with_akariths" %}


<{ title_past_infractions }/>
=============================

Here are the deeds you have been guilty of during these first few weeks of operations:

- (failed) attempted abduction of Prof. Loakim, a friend of Loyd Georges {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- (failed) attempted burglary of Loyd Georges' manor {% fact 'peridot_robs_lg_manor_fail' as author %}
- identity theft (for your official "cover") {% fact 'peridot_is_undercover' as author %}


Yodic Theology
=========================

<{ yodic_theology_simple_version }/>
