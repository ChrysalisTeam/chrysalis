
Fantôme - Octave de Maupertuis
##################################

Votre histoire
=======================

Votre profil
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

<{ phantom_octave_character_summary }/>


Un réveil inattendu
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Lorsque l'arkonte s'est immiscé dans la bibliothèque, vous avez fini par vous ranger à ses arguments.

Alors que vous prépariez vos affaires, le coeur lourd de devoir quitter pour toujours vos amis avatars, vous avez senti une vive brûlure dans votre dos.

{% macro maupertuis_phantoms_awakening() %}

Vous vous êtes réveillé un peu plus tard, la mémoire brouillée, le corps presque insensible. Le monde glissait entre vos doigts.
Grâce à votre bonne éducation, vous avez vite compris. Vous étiez devenu un fantôme.

Vous ne savez toujours pas ce qui s'est passé lors du rituel de l'Arkonte. Qui vous a attaqué ? L'arkonte ? La Bête ? Un intrus inattendu ? Une malédiction latente de la bibliothèque, peut-être en lien avec les pouvoirs insondables du fondateur de la dynastie Maupertuis, le {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %} ?

Ce genre de situation ne dure jamais éternellement. Donc vous attendez, en oscillant entre des moments de lucidité - dans lesquels vous êtes comme attaché à une petite zone lumineuse, et voyez passer au loin des spectres en errance - et d'étranges cauchemars où vous errez dans la bibliothèque, en proie à une rage surnaturelle.

{% endmacro %}
<{ maupertuis_phantoms_awakening }/>


Connaissances en commun avec l'Archiviste
==========================================

{% macro octave_and_archivist_common_knowledge_for_sheets() %}

IMPORTANT : La famille Maupertuis gardait quelques "paperasses administratives" dans une mallette noire, dans le domaine autorisé. Vous aviez entendu que le **symbole secret** de la famille, ouvrant l'accès au Domaine Interdit, s'y trouverait aussi dissimulé.
{% fact "octave_and_archivist_know_about_secret_family_symbol_infamily_briefcase" %}

Le code de cette valisette changeait automatiquement chaque jour, les chiffres actuels étaient **"murmurés par un livre factice {% symbol "Venture Prins" for "small_wooden_fake_book_name" %}"**. *Pensez à bien mémoriser la forme (épaisse en bois marron) et la localisation approximative de ce faux livre.*

Vous aviez en vain fouillé cette mallette, tous les deux, tout en prenant garde, car elle est **partiellement piégée** contre les intrus. {% fact "octave_and_archivist_know_about_venture_prins_book_location" %} {% fact "octave_and_archivist_have_searched_family_briefcase" %} {% fact "octave_and_archivist_know_about_trap_of_family_briefcase" %} {% hint 'trap_in_family_briefcase' is needed %}

Vous savez indiquer l'emplacement du boitier en bois à quiconque vous le demande **(voir Plan du Jeu)**.

Par ailleurs, vous avez entendu bien des choses, des parents Maupertuis, sur la dangerosité de **la Bête**, donc si les joueurs veulent ouvrir le passage vers le domaine interdit, vous les exhortez à avoir d'abord un plan pour la neutraliser, sous quelque forme qu'elle pointe le bout du museau. {% fact "octave_and_archivist_warn_players_about_beast_dangerousness" %}

Vous ne vous souvenez plus de l'espèce exacte à laquelle appartenait cette Bête. Juste que c'était une créature très griffue, et vivant habituellement dans des cavernes. {% fact "only_arkon_knows_things_about_beast_species" %}

Dans le temps, vous aviez entendu plusieurs fois les Maupertuis parler d'un **"Livre Yodique des Morts"**, le **{% symbol "Thanatologue" for "book_of_the_dead" %}**, qui serait l'un des grimoires les plus dangereux de la bibliothèque. Il était gardé dans un coffre du domaine interdit, verrouillé par **deux codes secrets**, chacun gardé par l'un des parents Maupertuis. {% fact "octave_and_archivist_know_about_thanatologue_location_and_double_code" %} {% hint 'family_legendary_chest_protected_by_double_code' is needed %}

Vous pouvez être tristes de réaliser, à un moment, que les diacres appartiennent précisément au culte de {% symbol "Bahamoot" for "god_of_diakons" %}, culte qui a fait saccager le manoir des Maupertuis jadis.

Octave avait un vieux livre d'enfance favori avec des animaux qui courent, en illusion d'optique (c'est utile pour l'énigme de la {% symbol "Boîte à Murmure" for "whispering_box" %} de Mérédice).

{% endmacro %}
<{ octave_and_archivist_common_knowledge_for_sheets }/>

Informations et instructions spécifiques
========================================

Vous avez gardé un esprit d'enfance, et vous interpellez parfois les joueurs de façon improbable, en leur racontant des anecdotes de votre relation enfance complice avec votre soeur, en leur demandant quel est leur livre ou leur reptile préféré, en leur demandant comment c'est "dehors" maintenant...

Si l'on vous apprend que votre soeur Mérédice a en réalité survécu aux persécutions qui ont détruit le manoir, vous êtes rempli d'enthousiasme ; mieux encore, si vous faites la rencontre de ses lointains descendants (vos piti-piti-piti...fillots), vous débordez d'affection et de gratitude envers eux.

Vous savez que votre soeur gardait ses affaires les plus précieuses dans son petit bureau d'études d'occultisme, dans le domaine interdit. Vous n'avez jamais vu ce bureau de vos yeux. Et en visitant le domaine en question, vous ne voyez rien qui ressemble à une telle chose ; peut-être derrière des éboulis ?
{% hint "maupertuis_daughter_jewel_under_rubbles_beyond_alchemist_laboratory" is needed %} {% fact "octave_has_hints_about_location_of_maupertuis_daughter_jewel" %}

L'archiviste vous a indiqué qu'il avait retrouvé, et bien classé, certaines vieilles recettes de potion qui avaient été utiles pour sauver votre soeur Mérédice dans son enfance. {% fact "archivist_knows_about_meredice_rejuvenation_cocktail_recipe_location" %} {% fact "archivist_has_marked_locations_of_rejuvenation_cocktail_subrecipes" %}

Si l'on vous parle du **trésor des Maupertuis**, vous savez que la famille disposait d'un artefact générateur de richesses, dans le domaine interdit. Le code magique pour l'utiliser change chaque jour, vous a-t-on dit. {% fact "treasure_code_changes_magically" %}

Si des joueurs cherchent un chaudron enchanté anti-abrasion, les guider finalement vers le chaudron en cuivre à anse, qui porte des marques d'envoûtement, dans l'étage interdit.

Lors de vos derniers préparatifs, vous aviez commencé à rassembler dans votre sac de voyage **un peu d'argent**, du moins celui qui n'avait pas été espièglement caché par votre soeur avant le drame. Si ce sac de voyage n'est plus trouvable, c'est soit que quelqu'un l'a volé, soit simplement qu'il a été enseveli sous un des **éboulis** survenus depuis. {% hint 'travel_bag_with_money_under_far_rubbles' is needed %} {% fact "octave_moneybox_hidden_by_meredice_is_lost" %}

Vous aviez aussi commencé un journal intime, au moment du départ, juste avant votre mort. {% hint 'octave_private_diary_on_his_tomb' is needed %}

{# ABORTED FOR NOW Vous aviez, tout petit, reçu de vos parents votre symbole secret personnel, une des clés nécessaire pour accéder au domain interdit des Maupertuis. Ce symbole ne vous a finalement pas servi, mais maintenant que vous êtes mort, il est étrangement apparu sur votre bras. -% fact "octave_has_secret_personal_symbol_on_arm" %- #}


Discours d'adieu aux joueurs
===================================

<{ octave_epilogue_speech }/>