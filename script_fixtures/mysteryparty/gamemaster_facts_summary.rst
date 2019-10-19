Résumé des faits et protagonistes impliqués
==============================================

{% macro display_names(listing) %}{% for name, data in listing %}{% if not loop.first %},{% endif %} {% if not data['in_cheat_sheet'] %}*{% endif %}{{name}}{% if not data['in_cheat_sheet'] %}*{% endif %}{% endfor %}{% endmacro %}

.. list-table::
   :widths: 30 20 20
   :header-rows: 1

   * - Action ou Fait
     - Auteur(s)
     - Témoin(s)

{% for fact, authors, viewers in facts_summary %}
   * - {{fact}}
     - {{display_names(authors)}}
     - {{display_names(viewers)}}
{% endfor %}
