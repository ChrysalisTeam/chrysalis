
<{ context_details_lg_manor }/>


{# USELESS, NOW USE GUESTS GALLERY
Vous aurez aussi, bien évidemment, la compagnie des autres invités, pour la plupart des participants aux enchères  :

{% for name, value in character_properties|dictsort %}
{% if not value.is_npc %}
- {{value.full_official_title}}
{% endif %}
{% endfor %}
#}
