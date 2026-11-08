{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- mettre la main sur l'orbe de Loyd Georges {% fact 'agent_mission_seek_lg_orb' %}
- obtenir un bail pour le gisement de sables bitumineux {% fact 'agent_mission_obtain_mining_lease' %}
- convaincre le concile akarite de la pureté doctrinale des doriens {% fact 'agent_mission_transfiliation_attempt' %} {% fact "peridot_must_answer_akarith_council" as author %}

- vos objectifs à court terme :

  - <{ orb_search_short_term_objectives }/>


<{ title_major_recent_facts }/>
=========================================================

- vous avez pris l'identité de {{character_properties.peridot.full_official_title}}, avec l'accord de la vraie personne qui est restée en toute discrétion dans sa boutique {% fact 'peridot_official_was_bribed' %}{% fact 'peridot_official_is_still_in_shop' %}
- vous faites équipe avec l'agent Topaz
- vous savez que Loyd Georges a découvert l'un des orbes divins et l'a mis au secret {% fact 'lg_has_found_and_hidden_an_orb' %}
- vos recherches dans le voisinage n'ont rien donné, hormis avec une interminable discussion avec Maitre Florent, apothicaire et ancien apprenti de Maître Bibine de Salima {% fact "peridot_talked_with_master_florent" as author %}
- vous savez par votre compère que le professeur Loakim était fortement impliqué par Loyd Georges {% fact 'lg_gave_responsibilities_to_loakim' %}
- vous avez tenté, en duo, d'enlever ce professeur Loakim, hélas sans succès {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- une certain "Malachite" semble responsable d'un récent cambriolage dans un entrepôt privé d'Alifir {% fact 'malachite&spinel_rob_alifir_warehouse' %}
- un certain "Spinel" a espionné les communications téléphoniques entre Loyd Georges et le professeur Loakim {% fact 'spinel_wiretaps_lg_and_friends' %}
- un certain "Amethyst" a revendu au marché noir des petits artefacts provenant des enchères {% fact 'amethyst_sells_items_at_black_market' %}

{% macro peridot_and_topaz_meeting_with_lg_summary() %}
- la veille :

  - vous avez, avec votre compère, rencontré Loyd Georges à {% symbol "15h" for "lg_meeting_time_for_peridot_topaz" %}, dans son manoir
  - d'abord méfiant, il a fini par ingurgiter vos bobards, mais ne vous a hélas rien appris que vous ne sachiez déjà
  - vous avez ensuite passé une soirée haute en couleur au club {% symbol "Luxor Excelcis" for "peridot_topaz_alibi_club_name" %} de Salima, toujours avec votre compère {% fact "peridot_topaz_alibi_is_strong" as author %}
{% endmacro %}
<{ peridot_and_topaz_meeting_with_lg_summary }/>


<{ title_last_minute_information }/>
==============================================

- deux personnes élégantes sont sorties, la veille vers midi, par le soupirail du garde-manger du manoir, avant de quitter le parc par le grand portail ; l'une d'elle semblait avoir perdu quelque chose dans sa fuite  {% fact 'amethyst_and_malachite_locked_in_pantry' %} {% fact 'amethyst_has_lost_thin_manor_parcel' %}
- vous avez sur vous une fiche sur "L'origine des pierres précieuses"  {% hint "origins_of_precious_stones_for_peridot" is needed %}
- en cas d'alliance avec l'Akarie, le signe de reconnaissance avec les akarites serait "{% symbol "les bras croisés sur la poitrine" for "dorian_akarith_alliance_sign" %}" {% fact "dorians_have_alliance_sign_with_akariths" %}


<{ title_past_infractions }/>
=============================

Voici les actions dont vous vous êtes rendu coupable durant ces premières semaines d'opérations :

- tentative (ratée) d'enlèvement du Pr Loakim, ami de Loyd Georges {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- tentative (ratée) de cambriolage du manoir de Loyd Georges {% fact 'peridot_robs_lg_manor_fail' as author %}
- usurpation d'identité (pour votre "couverture" officielle) {% fact 'peridot_is_undercover' as author %}


Théologie Yodique
=========================

<{ yodic_theology_simple_version }/>
