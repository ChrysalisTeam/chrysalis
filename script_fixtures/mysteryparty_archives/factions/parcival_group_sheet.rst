{% macro monolith_found_by_explorers() %}
Heureusement, à ce moment là, des archéologues héliossars ont mis au jour des monolithes immémoriaux, narrant les premières générations de la famille Maupertuis. Il y était mentionné, sous forme énigmatique, la création d'une bibliothèque enfouie loin sous terre, afin de conserver les plus puissants grimoires magiques de ce temps. Quelques photos de ces inscriptions ont fuité dans la presse, photos que vous avez laborieusement déchiffrées.
{% endmacro %}


{% macro portal_to_library_opened() %}
Quelques jours plus tard, comme chaque année depuis des siècles, un portail magique s'est amorcé lors du **{% symbol "solstice d'hiver" for "astral_opening_date" %}**, dans la cave d'un vieux château voisin ; un passage permettant de rejoindre, pour une journée seulement, les archives secrètes des Maupertuis. C'est visiblement par ce sortilège que cette famille invitait ses vassaux magiciens du monde entier à célébrer la nouvelle année, même si cette tradition était manifestement oubliée depuis longtemps quand le manoir des Maupertuis fut brûlé.

Il vous a fallu plus d'une demi-journée pour percer le fonctionnement de ce portail et le réveiller entièrement, il vous reste donc un peu plus de **{% symbol "3 heures" for "library_outside_portal_remaining_time" %}** pour explorer les lieux, lorsque vous vous y matérialisez. Mais pour fouiller un vieux tas de livres, cela devrait amplement suffire, n'est-ce pas ?
{% endmacro %}


{% macro parcival_group_sheet() %}

Faction - Les héritiers Parcival
============================================

{# Héritier Parcival - Vous descendez d'une grande lignée, et disposez soit d'une force surhumaine, soit de talents d'alchimie, soit de dons de voyance #}

Vous appartenez tous trois à la plus récente génération de la famille Parcival, vivant dans le pays de Slavinka. Une famille qui a hérité, par sa noble lignée, de certaines appétences avec le monde ésotérique.
L'un de vous est ainsi spécialisé dans les arts alchimiques ; l'autre reçoit ponctuellement des présages sous forme de visions ou de voix ; l'autre, enfin, a développé des facultés physiques et sensorielles impressionnantes en se connectant aux forces invisibles de la Nature.

Récemment, votre petite sœur {% symbol "Philomène" for "parcival_sick_child_name" %} est tombée gravement malade. La **{% symbol "dégénérescence marbrée" for "legacy_disease" %}**, un mal qui avait moult fois frappé vos ancêtres au fil des siècles. Mais un espoir subsistait : il est connu que votre aïeule, Mérédice de Maupertuis, en avait été guérie par ses parents dans sa tendre enfance. Ce savoir médicinal, engrangé par son ancestrale dynastie de mages-guérisseurs, est hélas largement tombé dans l'oubli : leur manoir de {% symbol "Thelassar" for "events_region_name" %} a été saccagé par des fanatiques, un drame dont Mérédice fut visiblement la seule rescapée. Traumatisée, elle avait entièrement refait sa vie à l'étranger, en ne cherchant jamais à récupérer le domaine qui lui revenait de droit.

Vous êtes donc partis sur les traces du passé, pour retrouver cette fabuleuse "Potion de Réjuvénation" qui avait sauvé votre lignée.

Les ruines du manoir des Maupertuis n'ont, sans surprise, livré aucun secret. Et le temps commençait à manquer ; {% symbol "Philomène" for "parcival_sick_child_name" %} n'en avait plus que pour quelques mois à vivre.

<{ monolith_found_by_explorers }/>

<{ portal_to_library_opened }/>

**Spécificités**

<{ parcival_group_symbols }/>

{% endmacro %}
<{ parcival_group_sheet }/>
