**{% symbol "La compromission ou la mort" for "dorian_sheet_motto" %}**

<{ title_your_intervention }/>
================================

Le service d'espionnage dorien, auquel vous appartenez, vous a envoyé enquêter sur les Loyd Georges, il y a plusieurs semaines de cela.

Votre nom de code est **Peridot** ; c’est notamment le pseudo que vous utilisez pour vous connecter à votre compte sur le réseau mondial, ou pour communiquer avec votre service d’espionnage.

Pour cette mission, vous avez pris l'identité de **{{character_properties.peridot.full_official_title}}** ; la personne détentrice du nom, quant à elle, s'est vue proposer une grasse somme d'argent en échange de son silence. La voilà heureuse comme tout, ses finances sont sauvées, et elle se fait discrète dans sa boutique. {% fact 'peridot_is_undercover' as author %}{% fact 'peridot_official_was_bribed' %}{% fact 'peridot_official_is_still_in_shop' %}

Vous travaillez en duo avec **Topaz**, un agent que vous connaissez bien, et utilisant de son côté l'identité fictive de **{{character_properties.topaz.full_official_title}}**. Vous avez ainsi tous deux participé à la première vente aux enchères de Loyd Georges, avec une certaine crédibilité. {% fact 'topaz_is_undercover' %}


<{ title_investigation_so_far }/>
============================================

Vous avez commencé votre petite enquête en vous promenant dans le hameau de Loyd Georges, près de Salima ; l'idée était de voir si les voisins, les commerçants, n'avaient pas des choses intéressantes à raconter. L'enquête s'est montrée peu fructueuse, Loyd Georges étant quelqu'un d'assez secret. Et le summum de l'inutilité a été atteint quand l'apothicaire du coin, Maître Florent – ravi d’avoir un public - vous a retenu pendant une bonne heure ; il vous a longuement raconté sa vie, depuis son apprentissage chez un certain Maître Bibine, rue de l'Arsenic à Salima, jusqu'à son installation ici, dans une bourgade perdue. Bref, l'énergumène vous a pompé la patience de toute une année. {% fact "peridot_talked_with_master_florent" as author %}

Heureusement, votre collègue a été plus chanceux, en découvrant (grâce à des écoutes téléphoniques) que le professeur Loakim, archéologue de l'Académie d'Alifir et ami de Loyd, était vraisemblablement très au courant des artefacts trouvés dans le temple enfoui. {% fact 'lg_gave_responsibilities_to_loakim' %}

{% macro dorian_failed_abduction() %}
Vous avez donc planifié, en duo avec votre collègue, et avec le support de mercenaires locaux, l'enlèvement du Pr Loakim. Mais la prompte intervention des forces de l'ordre sabarites a fait tourner en débacle cette opération ; heureusement que vous aviez bien couvert vos traces... {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
{% endmacro %}
<{ dorian_failed_abduction }/>

Vous avez par la suite tenté de cambrioler de nuit, seul, le manoir de Loyd Georges ; mais comme c'était à attendre, les sécurités en place étaient déjà bien trop sophistiquées, et vous avez dû abandonner. {% fact 'peridot_robs_lg_manor_fail' as author %}

Malgré ces échecs, vous avez pu déterminer, en recoupant les informations, ce qui vous importait le plus :

<{ loyd_georges_orb_certainties }/>


{% macro dorian_investigation_conclusion() %}
Bref, vous avancez laborieusement dans cette affaire Loyd Georges, et l'orbe divin reste un danger : il pourrait servir de prétexte aux chefs akarites pour déclencher une guerre "prophétique", rallier à leur cause les divers clans akarites (actuellement assez dubitatifs), et se bâtir un empire ; sans qu’il soit certain, pour l'instant, que la Dorie serait acceptée parmi leurs alliés. De plus, vous ne savez toujours pas comment ces orbes fonctionnent, ni l’étendue de leurs pouvoirs.

Mais vous continuez à tisser votre toile, et dès que Loyd Georges fera le moindre faux pas, vous n'en doutez (presque) pas, son orbe tombera sous votre contrôle.
{% endmacro %}
<{ dorian_investigation_conclusion }/>


<{ title_specific_information }/>
=============================

La nouvelle d'un cambriolage dans un entrepôt privé d'Alifir a attiré votre attention ; craignant un lien avec votre affaire, vous avez identifié le responsable du groupe mercenaire qui a réalisé l'exploit. En le faisant filer par un de vos mouchards, vous avez appris qu'il avait eu une conversation avec un certain "Malachite". {% fact 'malachite&spinel_rob_alifir_warehouse' %}

L'un de vos contacts à Salimacom (la compagnie de téléphone & web de Salima), vous a contacté pour vous apprendre qu'il avait trouvé une activité réseau curieuse lors d'un appel du professeur Loakim à Loyd Georges ; en utilisant un petit programme fait maison, il a pu tracer l'origine de l'étrange signal (horodaté "A827IZJ76") : le compte web d'un certain "Spinel". {% fact 'spinel_wiretaps_lg_and_friends' %}

Enfin, vous vous êtes promené au marché aux puces de Salima, et avez exposé votre identité "officielle" à un marchand. Il vous a alors a emmené dans son arrière-boutique, et vous a proposé de payer cash des artefacts et gemmes "de très grande qualité". Vous avez reconnu des pièces vendues par Loyd Georges durant ses enchères. Après avoir obtenu la coopération gracieuse du vendeur et de son receleur, grâce au chantage le plus éhonté ("ces objets appartiennent à M. Georges, qui est de mes amis, et je vous dénonce à la police si vous ne me dites pas qui vous les a fournies !"), vous avez finalement compris que ces pièces avaient été revendues via Pangeaweb par un certain "Amethyst", qui ne fait apparemment pas grand cas des lois commerciales du pays. {% fact 'amethyst_sells_items_at_black_market' %}


