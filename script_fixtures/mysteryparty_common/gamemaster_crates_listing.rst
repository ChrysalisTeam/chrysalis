.. CHECLIST DES OBJETS PAR RANGEMENT D'APPARTENANCE

{% for section, item_titles in murder_party_items_per_crate %}

{{section|dangerous_render}}
===================================================================================================================================

*Marquer avec des ronds les objets préparés au début du jeu, et cocher ces ronds lorsque les objets sont récupérés à la fin du jeu.*

{% for item_title in item_titles %}
- {{item_title|dangerous_render}}
{% endfor %}

.. raw:: pdf

    PageBreak

{% endfor %}
