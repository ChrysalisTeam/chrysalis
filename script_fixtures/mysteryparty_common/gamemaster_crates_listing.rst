.. CHECKLIST DES OBJETS PAR RANGEMENT D'APPARTENANCE

{% for section, item_titles in murder_party_items_per_crate %}

{{section|dangerous_render}}
===================================================================================================================================

{% for item_title in item_titles %}
- {{item_title|dangerous_render}}
{% endfor %}

.. raw:: pdf

    PageBreak

{% endfor %}
