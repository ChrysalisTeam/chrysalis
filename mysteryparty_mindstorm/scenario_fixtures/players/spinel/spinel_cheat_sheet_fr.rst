{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

- mettre la main sur l'orbe de Loyd Georges {% xfact 'agent_mission_seek_lg_orb' %}
- mettre la main sur le Panorbium Fortuna {% xfact 'agent_mission_find_panorbium_fortuna' %}
- acheter le gisement de sables bitumineux {% xfact 'agent_mission_obtain_mining_lease' %}

- vos objectifs à court terme :

  - <{ orb_search_short_term_objectives }/>
  


<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- vous avez emprunté à son insu l'identité de {{character_properties.spinel.full_official_title}}, qui est parti randonner en Sabarim {% xfact 'spinel_official_does_trekking' %}
{% endif %}
- vous faites équipe avec l'agent Malachite, avec qui vous partagez un appartement de Salima, au dessus de chez "Maître Bibine, apothicaire".
{% if standalone %}
- vous savez que Loyd Georges a découvert l'un des orbes divins et l'a mis au secret {% xfact 'lg_has_found_and_hidden_an_orb' %}
- des fuites ont mis en lumière des conspirations akarites en Sabarim, et la pression qu'ils mettent sur les services secrets doriens {% xfact 'akariths_pressure_dorians_secret_services' %} {% xfact 'akariths_have_conspiracy_against_sabarim' %}
- vous savez que {{character_properties.opal.official_name}} a triché aux échecs contre Loyd Georges, afin de gagner des bouteilles de vieux vin {% xfact 'opal_cheats_at_chess_against_lg' %}
{% endif %}

- la veille :

  - vous vous rendez à l'entrevue avec Loyd Georges à {% symbol "16h" for "lg_meeting_time_for_spinel" %}
  - vous croisez l'inspecteur Shark dans la salle à manger, tandis qu'il part discuter avec le maître-coq {% xfact "spinel_encounters_shark_in_dining_room" as author %}
  - Loyd Georges vous déstabilise avec un interrogatoire de joaillerie, vous vous disputez
  - vous coupez court à l'entretien et partez en claquant la porte {% xfact 'loyd_georges_quarrelled_with_someone' as author %}
  - le soir, vous tentez de nouer contact, sans plus de succès, avec le gérant magouilleur de la taverne du {% symbol "Perroquet Baveur" for "malachite_spinel_alibi_tavern_name" %} {% xfact "spinel_alibi_is_illegal" as author %}



<{ title_last_minute_information }/>
==============================================

- vous présumez que {{character_properties.opal.official_name}} a un tatouage de gang lordanien sur le corps {% xfact 'opal_might_have_gang_tattoo' %}
- vous songez à créer des diversions avec votre compère, si cela était nécessaire pour agir tranquillement durant la soirée {% xfact "spinel_has_reviewed_formation_manuals" as author %}



{% if standalone %}
<{ title_past_infractions }/>
===============================

Voici les actions dont vous vous êtes rendu coupable durant ces premières semaines d'opérations :

- cambriolage (raté) d'un entrepôt privé d'Alifir, avec des mercenaires {% xfact 'malachite&spinel_rob_alifir_warehouse' as author %}
- cambriolage (raté) en solo du manoir de LG {% xfact 'spinel_robs_lg_manor_fail' as author %}
- interception illicite de communications (mise sur écoute du Pr Loakim et autres protagonistes) {% xfact 'spinel_wiretaps_lg_and_friends' as author %}
- usurpation d'identité (CF votre "couverture" officielle) {% xfact 'spinel_is_undercover' as author %}
{% endif %}


