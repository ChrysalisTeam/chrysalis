{{ current_player_id.upper() }}
##################################

<{ title_main_missions }/>
=============================================================

<{ lydia_objectives_summary }/>



<{ title_major_recent_facts }/>
=========================================================

{% if standalone %}
- your husband's strength has been abnormally declining for 1 year  {% xfact 'opal_has_become_ill_for_1_year' %}

- 6 months ago, you moved near Alifir, to enter the race for the Consulate of Alifir {% xfact 'opal_lydia_moved_to_alifir_villa_6_months_ago' as author %} {% xfact 'lydia_runs_for_alifir_consul_election' as author %}
{% endif %}

- your husband obtained permission to move in with the family at Loyd Georges' manor for the duration of the auctions, two weeks ago {% xfact "opal_lydia_temporarily_moved_to_lg_manor_2_weeks_ago" as author %}

{% if standalone %}
- your husband's financial empire is in imminent danger of bankruptcy, because of the collapse of the construction company {% symbol "LordaBild" for "opal_construction_contractor" %} {% xfact 'opal_lydia_family_faces_bankrupt' %}
{% endif %}

- you are about to take the place of Consul {% symbol "Mundlish Odalisc" for "lydia_adversary_name" %} thanks to an electoral campaign built around these themes:

{% filter indent(2) %}
<{ lydia_campaign_themes }/>
{% endfilter %}

{% if standalone %}
- your electoral opponent, Mundlish Odalisc, is trying to blackmail you over your husband's past, but it is hard to know whether it is a bluff {% xfact 'lydia_threatened_by_opponent_mundlish_odalisc' as author %}
{% endif %}

- you had gone away, with Khaal and your cousin **{% symbol "Isildis" for "lydia_cousin_name" %}**, for a {% symbol "thalassotherapy stay in the misty mountains (near the eastern border of Sabarim)" for "khaal_isildis_location" %}, even if it meant missing Loyd Georges' evening  {% xfact "lydia_was_out_of_manor_with_khaal_recently" as author %}

- you finally came back by airship in the early afternoon, on the day of the special evening, leaving Khaal and your cousin there.



<{ title_last_minute_information }/>
============================================

- you had become friendly with a journalist called "Cynthia", a friend of Loyd Georges passing through the manor; she has not repeated what you confided to her  {% xfact "cynthia_and_lydia_met_in_lg_manor" as author %}
