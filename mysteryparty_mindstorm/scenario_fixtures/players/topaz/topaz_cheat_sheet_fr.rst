{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- mettre la main sur l'orbe de Loyd Georges {% xfact 'agent_mission_seek_lg_orb' %}
- mettre la main sur le Panorbium Fortuna {% xfact 'agent_mission_find_panorbium_fortuna' %}
- investiguer l'affaire du professeur Voluto {% xfact 'agent_mission_investigate_voluto' %}

- vos objectifs à court terme :

  - <{ orb_search_short_term_objectives }/>


<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- vous avez pris l'identité fictive de {{character_properties.topaz.full_official_title}} {% xfact 'topaz_official_is_non_existent' as author %} 
- vous prétendez travailler pour le {% symbol "Comte Adamor" for "lg_remote_friend_lord_name" %}, lointaine connaissance de Loyd Georges partie en croisière {% xfact 'topaz_pretends_working_for_count_adamor' as author %}
{% endif %}
- vous faites équipe avec l'agent Peridot
{% if standalone %}
- vous savez que Loyd Georges a découvert l'un des orbes divins et l'a mis au secret {% xfact 'lg_has_found_and_hidden_an_orb' %}
- vous avez découvert que le professeur Loakim était fortement impliqué par Loyd Georges {% xfact 'lg_gave_responsibilities_to_loakim' %}
- vous avez tenté, en duo, d'enlever ce professeur Loakim, hélas sans succès {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- votre collègue a tenté de cambrioler le manoir de Loyd Georges, mais sans succès {% xfact 'peridot_robs_lg_manor_fail' %}
{% endif %}

- le fameux homme d'affaires "{{character_properties.opal.official_name}}" a étrangement accès à un compte web de haute sécurité, mais "gelé", ayant pour identifiant "Emerald". {% xfact 'opal_accesses_emerald_agent_web_account' %}
{% if standalone %}
- "{{character_properties.amethyst.official_name}}" est en réalité un agent lordanien, le vrai porteur du nom est hospitalisé pour maladies vénériennes {% xfact 'amethyst_official_has_venereal_disease' %}
- c'est un agent masslave de pseudonyme "Malachite" qui a récemment déclenché une émeute akarite en Dorie {% xfact 'malachite_triggers_akarith_riot_in_dorian_dukedom' %}
{% endif %}

<{ peridot_and_topaz_meeting_with_lg_summary }/>


<{ title_last_minute_information }/>
==============================================

- vous avez des *traces réseau* probantes [écrivez ce document freestyle], montrant qu'un certain "Amethyst", des services secrets lordaniens, avait mis sur écoute le patriarche de Ghek, depuis les environs de Salima. {% xfact 'amethyst_wiretaps_ghek_patriarch' %}
- un certain "Phonphonse" du manoir cherche à vendre un stylo "Chromia" qui pourrait être un système d'espionnage  {% xfact 'alphonse_has_found_library_spy_recorder' %}
- le fameux {{character_properties.opal.official_name}} se connectait autrefois à un compte web de haute sécurité ayant pour identifiant "Emerald", et semblant en lecture seule  {% xfact 'opal_accesses_emerald_agent_web_account' %}
- en cas d'alliance avec l'Akarie, le signe de reconnaissance avec les akarites serait "{% symbol "les bras croisés sur la poitrine" for "dorian_akarith_alliance_sign" %}" {% xfact "dorians_have_alliance_sign_with_akariths" %}



{% if standalone %}
<{ title_past_infractions }/>
===============================

Voici les actions dont vous vous êtes rendu coupable durant ces premières semaines d'opérations :

- interception illicite de communications (mise sur écoute de gens de Salima) {% xfact 'topaz_wiretaps_lg_and_friends' as author %}
- tentative (ratée) d'enlèvement du Pr Loakim, ami de Loyd Georges {% xfact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- fraude fiscale (revente de gemmes des enchères au marché noir) {% xfact 'topaz_sells_gems_at_black_market' as author %}
- usurpation d'identité (CF votre "couverture" officielle) {% xfact 'topaz_is_undercover' as author %}
{% endif %}



