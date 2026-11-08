Chrysalis: Descent - {{ name }}
##########################################################


Stats
=====================

.. list-table::
   :widths: 10 10
   :header-rows: 1

   * - Attribute
     - Value
   * - Constitution
     - {{ stats.constitution }}
   * - Agility
     - {{ stats.agility }}
   * - Observation
     - {{ stats.observation }}


Missions
=============

{{ missions }}


Skills
===============

{% for entry in abilities %}
- {{ entry }}
{% endfor %}



Equipment
============

Common:

{% for entry in common_equipments %}
- {{ entry }}
{% endfor %}


Specific:

{% for entry in equipments %}
- {{ entry }}
{% endfor %}
