Chrysalis:Descent - {{ name }}
##########################################################


Statistiques
=====================

.. list-table::
   :widths: 10 10
   :header-rows: 1

   * - Caractéristique
     - Valeur
   * - Constitution
     - {{ stats.constitution }}
   * - Agilité
     - {{ stats.agility }}
   * - Observation
     - {{ stats.observation }}


Missions
=============

{{ missions }}


Compétences
===============

{% for entry in abilities %}
- {{ entry }}
{% endfor %}



Equipements
============

Communs :

{% for entry in common_equipments %}
- {{ entry }}
{% endfor %}


Spécifiques :

{% for entry in equipments %}
- {{ entry }}
{% endfor %}
