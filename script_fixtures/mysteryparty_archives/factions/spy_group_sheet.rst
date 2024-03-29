
{% macro spy_group_sheet() %}

Faction - Les agents secrets mirandiens
============================================

{# Agent Secret - Vous êtes expert en déminage, ou en crochetage de serrure, ou en scanner magnétique de murs #}

Vous êtes des agents secrets de l'île de Mirandia, située au centre de l’océan diorique (île non visible sur la carte du monde).
L'un de vous est spécialisé dans le crochetage de serrures, et la lecture des champs magnétiques sur les objets ; l'autre dans la désactivation de pièges, et l'utilisation d'explosifs ; l'autre, enfin, dans la détection des métaux et la télécommunication.

Votre minuscule pays vivait en paix, jusqu'à ce que ses richesses minières et maritimes n'excitent la convoitise de ses puissants voisins. Victime de sombres complots économiques, Mirandia est désormais lourdement endettée, au risque d'être annexée par le plus offrant.

Votre pays doit désormais trouver de quoi rembourser **500 kashes par jour pendant 3 ans**, ce qui est énorme.
{% fact 'spy_country_needs_500_kashes_per_day_for_3_years' %}

En désespoir de cause, le prince mirandien vous a envoyé sur les traces d'un **trésor dynastique** ayant appartenu aux Maupertuis - une antique lignée de mages-guérisseurs qui avait toujours vécu dans l'aisance, sans jamais faire payer leurs services. Vos recherches vous ont mené jusqu'aux ruines de leur manoir, dans le pays de {% symbol "Thelassar" for "events_region_name" %}, manoir qui fut autrefois saccagé par des fanatiques. Vos chances de retrouver ces richesses devenaient bien minces.

<{ monolith_found_by_explorers }/>

<{ portal_to_library_opened }/>

**Spécificités**

<{ spy_group_symbols }/>

{% endmacro %}
<{ spy_group_sheet }/>
