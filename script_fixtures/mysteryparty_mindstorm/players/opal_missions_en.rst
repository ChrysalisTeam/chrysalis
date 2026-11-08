


{% include "missions/berserk_elixir_recipe/opal_remedy_quest_en.rst" %} {# BEFORE MAIN OBJECTIVES #}


<{ title_main_missions }/>
=========================================

{% macro magnus_parents_must_protect_family() %}
Protect your family
    Between the Akarith fanatics and your political adversaries, your loved ones are in danger. You will therefore have to defend them, at any cost.
{% endmacro %}


{% macro opal_main_objectives() %}

<{ magnus_parents_must_protect_family }/>

Save your health and Loyd Georges'
    Your last hope seems to lie in this famous "Berserk Elixir"; you hope that Rydji and {% symbol "Rodok" for "lg_adventurer_friend_name" %} will be able to put you on its trail... {% fact "opal_knows_about_berserk_elixir" as author %}

Help solve the crime against Loyd Georges
    You have only moderate confidence in the remaining skills of the ageing Inspector Shark, so you fully intend to investigate a little on the side, perhaps through his deputy police officer. Especially since, in the absence of a culprit, they might end up accusing you!

Defend Loyd Georges' Orb
    This archaeological wonder has taken a back seat because of recent events, but you feel it your duty to protect Loyd Georges' Orb, so valiantly recovered, against foreign agents. Only, you do not even know where he hid it...

Tackle the Akarith "Purifiers"
    You bear a serious grudge against this sect that made an attempt on your life, and perhaps on Loyd Georges'. So if the opportunity arises...

{% endmacro %}

<{ opal_main_objectives }/>





{% if not standalone %}
{% include "missions/nazur_secrets/specific_mission_briefing_en.rst" %}
{% endif %}

