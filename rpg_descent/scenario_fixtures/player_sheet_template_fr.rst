{% set player = descent_rpg.players[current_player_id] %}
Chrysalis:Descent - {{ player.name }}
##########################################################


Statistiques
=====================

.. list-table::
   :widths: 10 10
   :header-rows: 1

   * - Caractéristique
     - Valeur
   * - Constitution
     - {{ player.stats.constitution }}
   * - Agilité
     - {{ player.stats.agility }}
   * - Observation
     - {{ player.stats.observation }}


Missions
=============

{{ player.missions }}


Compétences
===============

{% for entry in player.abilities %}
- {{ entry }}
{% endfor %}



Équipements
============

Communs :

{% for entry in descent_rpg.common_equipments %}
- {{ entry }}
{% endfor %}


Spécifiques :

{% for entry in player.equipments %}
- {{ entry }}
{% endfor %}
