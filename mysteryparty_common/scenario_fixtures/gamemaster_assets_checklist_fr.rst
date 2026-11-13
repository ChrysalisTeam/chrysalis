Checklist des Objets du Jeu
================================

*Les objets non cruciaux pour le scénario sont marqués en italique.*

{% for section, section_item_structs in murder_party_items %}

{{section|dangerous_render}}

{% for section_item_struct in section_item_structs %}
- {% if not section_item_struct.item_is_important %}*{% endif%}{{section_item_struct.item_label|dangerous_render|trim}}{% if not section_item_struct.item_is_important %}*{% endif%}
{% endfor %}

{% endfor %}
