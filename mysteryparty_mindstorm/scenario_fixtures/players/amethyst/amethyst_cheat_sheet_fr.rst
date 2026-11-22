{{ current_player_id.upper() }}
##################################


<{ title_main_missions }/>
=============================================================

{% macro orb_search_short_term_objectives() %}pour l'orbe de Loyd Georges, trouver la réponse à sa question secrète ("{{ character_properties['loyd.georges'].secret_question }}"), et acquérir des artefacts se prêtant bien à une géolocalisation par scanner mondial{% endmacro %}

- mettre la main sur l'orbe de Loyd Georges {% xfact 'agent_mission_seek_lg_orb' %}
- acheter le gisement de sables bitumineux, à un prix inférieur à ce qu'il vous rapportera : l'équivalent de **10 mégakashes** de bitume, ou 50% de plus avec un **Cœur de Fusion Thermocyclique** {% xfact 'agent_mission_obtain_mining_lease' %}

- récupérer auprès des obérons les rapports sur l'équilibre des forces militaires en Midolie, les authentifier, nous les transmettre, puis rester en alerte sur tout ce qui concerne ce sujet {% xfact 'agent_mission_study_midolian_armies_balance' %} {% xitem "heliossar_spy_reports_on_akaris_armament" is needed %}

{% macro lordanian_berserk_mission_summary() %}
- aider Loyd Georges et {{character_properties.opal.official_name}} à être cobayes de l'Élixir Berserk {% xfact 'agent_mission_investigate_berserk_elixir' %} {% xitem "berserk_elixir_advanced_ingredients_for_amethyst" is needed %} {# mission en duo #}
{% endmacro %}
<{ lordanian_berserk_mission_summary }/>

- vos objectifs à court terme :

  - <{ orb_search_short_term_objectives }/>
  


<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- vous avez emprunté à son insu l'identité de {{character_properties.amethyst.full_official_title}}, qui est en soin pour une maladie honteuse  {% xfact 'amethyst_official_has_venereal_disease' %}
- vous faites équipe avec l'agent Garnet, qui a perdu récemment son collègue "Emerald" en Dorie (et a hérité de sa fausse identité) {% xfact 'garnet_lost_colleague_emerald' %}
- vous savez que Loyd Georges a découvert l'un des orbes divins et l'a mis au secret {% xfact 'lg_has_found_and_hidden_an_orb' %}
- vous avez démasqué les enchérisseurs doriens comme étant des agents secrets "Topaz" et "Peridot" travaillant pour la Dorie ; leurs "personnages officiels" sont respectivement "inexistant" et "toujours dans sa boutique" {% xfact 'topaz_official_is_non_existent' %} {% xfact 'peridot_official_is_still_in_shop' %}
- en duo, pour approcher les artefacts de Loyd Georges, vous avez joué double jeu : vous avez dévoilé à la Dorie la couverture de l'agent masslave Marduk Pamuk, et donné à la Masslavie la localisation de la cache d'armes des doriens à Mastden {% xfact 'amethyst&garnet_unmask_masslavian_agent_in_dorian_dukedom' as author %} {% xfact 'amethyst&garnet_unmask_dorian_den_in_masslavia' as author %}
{% endif %}

- la veille :

  - vous avez offert une bouteille de liqueur digestive bleue cachetée à Loyd Georges, lors de l'entretien à {% symbol "11h" for "lg_meeting_time_for_amethyst" %}, mais n'y avez rien appris {% xfact 'amethyst_offers_liquor_to_lg' as author %}
  - puis vous avez désactivé les caméras de surveillance pour explorer le manoir {% xfact 'amethyst_disabled_surveillance_cameras' as author %}
  - à 12h, à travers un mur, vous avez entendu Shark questionner Loyd Georges sur un individu grimé en livreur, venu tôt le matin lui apporter des nouvelles de son ami le professeur Loakim
  - vous avez croisé {{character_properties.malachite.official_name}} caché dans le garde-manger {% xfact 'amethyst_and_malachite_locked_in_pantry' as author %}
  - vous avez récupéré une lettre pour Loyd Georges, mais perdu son fin colis marron en repartant {% xfact 'amethyst_has_stolen_manor_letter' as author %} {% xfact 'amethyst_has_lost_thin_manor_parcel' as author %} {% xitem "stolen_manor_letter_for_amethyst" is needed %}
  - après des investigations infructueuses, vous rentrez vous coucher très tôt au {% symbol "8e étage de l'Hotel SalimaGlobeCenter" for "amethyst_hostel_room" %} {% xfact "amethyst_alibi_is_void" as author %}



<{ title_last_minute_information }/>
=============================================

Vous connaissez des "Perles du Droit Sabarites", comme celle de la rupture amoureuse empêchant un interrogatoire de police, ou celle sur le port des gants toujours autorisé.{% xfact 'amethyst_knows_misc_absurd_sabarim_laws' as author %}



{% if standalone %}
<{ title_past_infractions }/>
======================================================

Voici les actions dont vous vous êtes rendu coupable durant ces premières semaines d'opérations :

- profanation du caveau familial de Loyd Georges (commando lordanien)  {% xfact 'amethyst&garnet_open_lg_family_tomb' as author %}
- interception illicite de communications (mise sur écoute du patriarche de Ghek) {% xfact 'amethyst_wiretaps_ghek_patriarch' as author %}
- piratage informatique (compte secondaire de Loyd Georges) {% xfact 'amethyst&garnet_crack_lg_2nd_web_account' as author %}
- fraude fiscale (revente de petits artefacts au marché noir) {% xfact 'amethyst_sells_items_at_black_market' as author %}
- usurpation d'identité (CF votre "couverture" officielle) {% xfact 'amethyst_is_undercover' as author %}
{% endif %}

