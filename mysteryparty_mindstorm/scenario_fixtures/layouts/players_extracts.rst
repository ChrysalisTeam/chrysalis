{# Extracts of the character sheets for the gamemaster: the facts of these parts are attributed to each player #}
{% for p in player_names %}
{% if not loop.first %}

----------

{% endif %}


{{ p.capitalize() }}
#######################

{% with current_player_id=p, hide_anthropia_credentials=true %}
{% include "players/" ~ p ~ "_specific_abilities_" ~ language ~ ".rst" %}
{% include "common_anthropia_account_summary_displayer_" ~ language ~ ".rst" %}
{% endwith %}

{% endfor %}
