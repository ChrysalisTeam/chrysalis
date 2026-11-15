{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

Votre principale tâche est de préserver Sabarim contre les nombreuses menaces extérieures et intérieures :

<{ obsidian_main_objectives_to_defend_sabarim }/>

**L'Affaire Voluto** garde aussi son importance ; en attendant d'obtenir des investigations sur le compte Anthropia du professeur, et peut-être de retrouver les enregistrements de surveillance de l'Académie d'Alifir, vous pouvez toujours voir du côté de ses anciens collègues : {% symbol "le docteur Marloff du département d'optique appliquée, le jeune physicien Waden Shaw, et le professeur Idn Gark du pôle Energies Nouvelles" for "voluto_suspicious_colleagues" %}. {% xfact "voluto_death_day_academy_recordings_disappeared" %} {% xfact 'agent_mission_investigate_voluto' %}


{% if standalone %}
<{ title_major_recent_facts }/>
=========================================================

- vous soupçonnez {{character_properties.opal.official_name}} d'avoir appartenu au gang des "Loups Rouges" par le passé, gang qui a volé les cierges d'or de la duchesse de Dorie, mère du Duc actuel ; il aurait par ailleurs, par le passé, rendu service aux services secrets sabarites sous la supervision de votre collègue "Le Docker"  {% xfact 'opal_was_in_red_wolves_gang' %} {% xfact "opal_has_friend_in_sabarith_spies_called_the_docker" as author %}
- d'après la presse, un certain "{{character_properties.malachite.official_name}}", a eu les deux jambes cassées la veille lors d'une attaque de mouflon, dans l’arrière-pays désertique de Sabarim...  {% xfact 'malachite_official_breaks_leg' %}
{% endif %}


<{ title_last_minute_information }/>
=========================================================

- vous avez sur vous un document des "Eléments de droit sabarite" {% xitem 'sabarith_law_summary_for_obsidian' is needed %} ainsi qu'un extrait de "Lexique akarite" {% xitem 'akarith_lexicon_for_obsidian' is needed %}
- Shark vous a empêché de garder votre arme pour la soirée, par prudence  {% xfact "obsidian_was_forbidden_by_shark_to_have_weapon" %}
- il semble que les tripots des bas-fonds de Sabarim servent aux akarites infiltrés, mais les consuls ne veulent pas y faire de remous {% xfact "akarith_use_sabarith_taverns_as_bases_and_consuls_know_it" %}
- vous avez appris que votre cousine {{character_properties.cynthia.official_name}}, journaliste, faisait partie de l'entourage proche de Loyd Georges  {% xfact "cynthia_and_obsidian_are_cousins" as author %}

