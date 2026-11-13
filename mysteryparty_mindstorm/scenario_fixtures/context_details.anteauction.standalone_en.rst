
<{ context_details_lg_manor }/>


{# USELESS, NOW USE GUESTS GALLERY
You will also, of course, have the company of the other guests, most of them participants in the auctions:

{% for name, value in character_properties|dictsort %}
{% if not value.is_npc %}
- {{value.full_official_title}}
{% endif %}
{% endfor %}
#}
