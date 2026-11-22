{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- get your hands on Loyd Georges' orb {% xfact 'agent_mission_seek_lg_orb' %}
- buy the tar sands deposit, at a price lower than what it will bring you: the equivalent of **20 megakashes** of whole tar sands, or 50% more with a **Thermocyclic Fusion Core** {% xfact 'agent_mission_obtain_mining_lease' %}
- convince the Akarith council of the doctrinal purity of the Dorians {% xfact 'agent_mission_transfiliation_attempt' %} {% xfact "peridot_must_answer_akarith_council" as author %}

- your short-term objectives:

  - <{ orb_search_short_term_objectives }/>


<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- you have taken on the identity of {{character_properties.peridot.full_official_title}}, with the agreement of the real person, who has stayed quietly in his shop {% xfact 'peridot_official_was_bribed' %}{% xfact 'peridot_official_is_still_in_shop' %}
{% endif %}
- you are teamed up with agent Topaz
{% if standalone %}
- you know that Loyd Georges has discovered one of the Divine Orbs and hidden it away {% xfact 'lg_has_found_and_hidden_an_orb' %}
- your enquiries in the neighbourhood yielded nothing, apart from an endless conversation with Master Florent, apothecary and former apprentice of Master Bibine of Salima {% xfact "peridot_talked_with_master_florent" as author %}
- you know from your partner that Loyd Georges had heavily involved Professor Loakim in his affairs {% xfact 'lg_gave_responsibilities_to_loakim' %}
- you attempted, as a duo, to abduct this Professor Loakim, alas without success {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- a certain "Malachite" seems responsible for a recent burglary in a private warehouse in Alifir {% xfact 'malachite&spinel_rob_alifir_warehouse' %}
- a certain "Spinel" spied on the telephone communications between Loyd Georges and Professor Loakim {% xfact 'spinel_wiretaps_lg_and_friends' %}
- a certain "Amethyst" resold on the black market small artefacts from the auctions {% xfact 'amethyst_sells_items_at_black_market' %}
{% endif %}

{% macro peridot_and_topaz_meeting_with_lg_summary() %}
- the day before:

  - together with your partner, you met Loyd Georges at {% symbol "15:00" for "lg_meeting_time_for_peridot_and_topaz" %}, in his manor
  - wary at first, he ended up swallowing your tall tales, but alas taught you nothing you did not already know
  - you then spent a colourful evening at the {% symbol "Luxor Excelcis" for "peridot_topaz_alibi_club_name" %} club in Salima, still with your partner {% xfact "peridot_topaz_alibi_is_strong" as author %}
{% endmacro %}
<{ peridot_and_topaz_meeting_with_lg_summary }/>


<{ title_last_minute_information }/>
==============================================

- two elegant people came out the day before, shortly before 13:00, through the transom window of the manor's pantry, before leaving the grounds by the main gate; one of them seemed to have lost something in their flight  {% xfact 'amethyst_and_malachite_locked_in_pantry' %} {% xfact 'amethyst_has_lost_thin_manor_parcel' %}
- you are carrying a sheet on "The Origin of Precious Stones"  {% xitem "origins_of_precious_stones_for_peridot" is needed %}
- in the event of an alliance with Akaris, the recognition sign with the Akariths would be "{% symbol "arms crossed over the chest" for "dorian_akarith_alliance_sign" %}" {% xfact "dorians_have_alliance_sign_with_akariths" %}


{% if standalone %}
<{ title_past_infractions }/>
=============================

Here are the deeds you have been guilty of during these first few weeks of operations:

- (failed) attempted abduction of Prof. Loakim, a friend of Loyd Georges {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- (failed) attempted burglary of Loyd Georges' manor {% xfact 'peridot_robs_lg_manor_fail' as author %}
- identity theft (for your official "cover") {% xfact 'peridot_is_undercover' as author %}
{% endif %}


Yodic Theology
=========================

<{ yodic_theology_simple_version }/>
