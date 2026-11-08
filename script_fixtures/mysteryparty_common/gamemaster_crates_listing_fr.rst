.. CHECKLIST DES OBJETS PAR RANGEMENT D'APPARTENANCE

{% for section, item_qualified_labels in murder_party_items_per_crate %}

{{section|dangerous_render}}
===================================================================================================================================

{% for item_label, item_is_important in item_qualified_labels %}
- {% if not item_is_important%}*{% endif%}{{item_label|dangerous_render|trim}}{% if not item_is_important %}*{% endif%}
{% endfor %}

.. raw:: pdf

    PageBreak

{% endfor %}
