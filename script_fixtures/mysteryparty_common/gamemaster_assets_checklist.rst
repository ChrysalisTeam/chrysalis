Checklist des Objets du Jeu
================================

*Marquer avec des ronds les objets préparés au début du jeu, et cocher ces ronds lorsque les objets sont récupérés à la fin du jeu. Les objets importants pour le scénario sont mis en emphase ci-dessous.*

{% for section, section_item_structs in murder_party_items %}

{{section|dangerous_render}}

{% for section_item_struct in section_item_structs %}
- {% if not section_item_struct.item_is_important %}*{% endif%}{{section_item_struct.item_label|dangerous_render|trim}}{% if not section_item_struct.item_is_important %}*{% endif%}
{% endfor %}

{% endfor %}
