Summary of facts and protagonists involved
==============================================

{% macro display_names(listing) %}{% for name, data in listing %}{% if not loop.first %}, {% endif %}{{name}}{% endfor %}{% endmacro %}

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Action or Fact
     - Known by

{% for fact, knowers in aggregated_facts_summary %}
   * - {{fact}}
     - {{display_names(knowers)}}
{% endfor %}
