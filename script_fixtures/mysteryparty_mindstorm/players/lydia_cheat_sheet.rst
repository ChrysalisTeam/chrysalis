{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

<{ lydia_objectives_summary }/>



<{ title_major_recent_facts }/>
=========================================================

- les forces de votre mari déclinent anormalement depuis 1 an  {% fact 'opal_has_become_ill_for_1_year' %}

- il y a 6 mois, vous avez déménagé près d'Alifir, pour vous lancer dans la course au consulat d'Alifir {% fact 'opal_lydia_moved_to_alifir_villa_6_months_ago' as author %} {% fact 'lydia_runs_for_alifir_consul_election' as author %}

- votre mari a obtenu d'aménager en famille dans le manoir de Loyd Georges pour la durée des enchères, il y a deux semaines {% fact "opal_lydia_temporarily_moved_to_lg_manor_2_weeks_ago" as author %}

- l'empire financier de votre mari est en danger imminent de banqueroute, à cause de la faillite de la société de construction {% symbol "LordaBild" for "opal_construction_contractor" %} {% fact 'opal_lydia_family_faces_bankrupt' %}

- vous êtes sur le point de prendre la place du consul {% symbol "Mundlish Odalisc" for "lydia_adversary_name" %} grâce à une campagne électorale axée sur ces thèmes :

{% filter indent(2) %}
<{ lydia_campaign_themes }/>
{% endfilter %}

- votre adversaire électoral, Mundlish Odalisk, cherche à vous faire chanter quant au passé de votre mari, mais difficile de savoir si ce n'est pas du bluff {% fact 'lydia_threatened_by_opponent_mundlish_odalisc' as author %}

- vous étiez partie, avec Khaal et votre cousine **{% symbol "Isildis" for "lydia_cousin_name" %}**, pour une {% symbol "thalassothérapie dans les monts brumeux (près de la frontière Est de Sabarim)" for "khaal_isildis_location" %}, quitte à manquer la soirée de Loyd Georges  {% fact "lydia_was_out_of_manor_with_khaal_recently" as author %}

- vous êtes finalement rentrée par dirigeable en début d'après-midi, le jour de la soirée spéciale, en laissant Khaal et votre cousine là-bas.



<{ title_last_minute_information }/>
============================================

- vous aviez sympathisé avec une journaliste appelée "Cynthia", amie de Loyd Georges de passage au manoir ; elle n'a pas ébruité vos confidences  {% fact "cynthia_and_lydia_met_in_lg_manor" as author %}
