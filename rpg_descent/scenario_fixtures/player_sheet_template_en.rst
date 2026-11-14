{% set player = descent_rpg.players[current_player_id] %}
Chrysalis: Descent - {{ player.name }}
##########################################################


Stats
=====================

.. list-table::
   :widths: 10 10
   :header-rows: 1

   * - Attribute
     - Value
   * - Constitution
     - {{ player.stats.constitution }}
   * - Agility
     - {{ player.stats.agility }}
   * - Observation
     - {{ player.stats.observation }}


Missions
=============

{{ player.missions }}


Skills
===============

{% for entry in player.abilities %}
- {{ entry }}
{% endfor %}



Equipment
============

Common:

{% for entry in descent_rpg.common_equipments %}
- {{ entry }}
{% endfor %}


Specific:

{% for entry in player.equipments %}
- {{ entry }}
{% endfor %}
