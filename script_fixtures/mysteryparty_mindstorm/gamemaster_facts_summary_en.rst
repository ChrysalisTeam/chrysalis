Summary of facts and protagonists involved
==============================================

{% macro display_names(listing) %}{% for name, data in listing %}{% if not loop.first %},{% endif %} {% if not data['in_cheat_sheet'] %}*{% endif %}{{name}}{% if not data['in_cheat_sheet'] %}*{% endif %}{% endfor %}{% endmacro %}

.. list-table::
   :widths: 30 20 20
   :header-rows: 1

   * - Action or Fact
     - Author(s)
     - Witness(es)

{% for fact, authors, viewers in facts_summary %}
   * - {{fact}}
     - {{display_names(authors)}}
     - {{display_names(viewers)}}
{% endfor %}
