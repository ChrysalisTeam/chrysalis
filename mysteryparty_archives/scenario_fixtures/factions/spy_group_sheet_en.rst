
{% macro spy_group_sheet() %}

Faction - The Mirandian secret agents
============================================

{# Secret agent - You are an expert in minesweeping, or in lockpicking, or in magnetic wall scanning #}

You are secret agents from the island of Mirandia, located in the middle of the Diorian Ocean (an island not shown on the world map).
One of you specialises in lockpicking, and in reading the magnetic fields on objects; another in disarming traps, and in the use of explosives; the last in metal detection and telecommunication.

Your tiny country lived in peace, until its mining and maritime riches aroused the greed of its powerful neighbours. The victim of dark economic plots, Mirandia is now heavily in debt, at risk of being annexed by the highest bidder.

Your country must now find the means to repay **500 kashes per day for 3 years**, which is enormous.
{% fact 'spy_country_needs_500_kashes_per_day_for_3_years' %}

As a last resort, the Mirandian prince sent you on the trail of a **dynastic treasure** that belonged to the Maupertuis - an ancient lineage of healer-mages who had always lived in comfort, without ever charging for their services. Your research led you to the ruins of their manor, in the land of {% symbol "Thelassar" for "events_region_name" %}, a manor that was once sacked by fanatics. Your chances of recovering these riches were becoming very slim.

<{ monolith_found_by_explorers }/>

<{ portal_to_library_opened }/>

**Specifics**

<{ spy_group_symbols }/>

{% endmacro %}
<{ spy_group_sheet }/>
