Checklist des Objets du Jeu
================================

*Marquer avec un rond les objets préparés au début du jeu, et cocher ce rond lorsque les objets sont récupérés à la fin du jeu.*

{% for section, item_titles in murder_party_items %}

{{section}}

{% for item_title in item_titles %}
- {{item_title|dangerous_render}}
{% endfor %}

{% endfor %}
