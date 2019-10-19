
<{ title_previous_day }/>
==============================

Votre enquête piétinait depuis quelques jours, et vous étiez sur le point de provoquer une rencontre avec un agent adverse, pour faire bouger les choses, quand Loyd Georges vous propose un entretien en tête-à-tête, annonçant avoir des "informations importantes" à vous communiquer. **Vous vous rendez-donc au manoir, le jour venu, pour {% symbol "11h" for "lg_meeting_time_for_amethyst" %}.**

{% macro arrival_at_manor_with_butler() %}
Le lourd portail du parc s'ouvre lentement, puis claque dans votre dos. Un gendarme salimien bedonnnant sort à contre-coeur de sa large guérite, contrôle vos papiers, et vous fait passer à travers un détecteur d'armes. Le majordome de Loyd Georges, Rydji, vient alors à votre rencontre.

En entrant dans le magnifique Grand Hall du manoir, vous remarquez immédiatement la caméra qui surveille l'ensemble de la salle. Voilà qui ne simplifie jamais rien. Il ne semble pas y en avoir dans le petit hall, mais combien d'autres sont disséminées dans le château, voire le parc ?
{% endmacro %}
<{ arrival_at_manor_with_butler }/>

Vous rencontrez prestement Loyd Georges dans son bureau. Il semble tendu ! Vous faites de votre mieux pour le mettre à l’aise, et la bouteille de liqueur digestive que vous lui offrez est un pas dans le bon chemin ; c'est une liqueur étrangère qui a attiré votre œil dans la grande galerie marchande de Salima, car nantie d’une amusante couleur bleue, et d'un bouchon cacheté à la cire façon vieille époque. Loyd Georges promet de l’ouvrir en votre honneur pour le repas. {% fact 'amethyst_offers_liquor_to_lg' as author %}

Vous vous enquérez de ces fameuses "informations" qu'il a pour vous.
Après avoir maladroitement tenté de répondre à vos propres questions par d'autres questions (sur vos voyages, sur vos collections d'antiquités et pierreries...), le sir s'emmêle les pinceaux, et vous avoue qu’il n’a pas de révélation pour vous, mais qu’il voulait surtout savoir davantage à qui il avait affaire. Vous riez avec lui de ce qu’il ne s’y prend pas bien, ce à quoi il répond qu'en effet, une carrière dans la police sabarite aurait été une très mauvaise idée pour lui.

Vous cherchez alors à le faire parler sur ses récentes découvertes ; il vous narre rapidement son expédition et le mythe des orbes, mais il semble ignorer l'effet réel des orbes, s'il existe. Il avoue à demi-mot en avoir lui-même tenu un entre ses mains, mais vos tentatives pour le pousser dans ce sens ne font que le rendre méfiant...

Après cet entretien cordial mais peu fructueux, vers 11h45, Loyd Georges appelle le majordome pour qu'il vous raccompagne.
Vous remettez vos gants de cuir. Cet entretien est sur le point de vous laisser un goût amer. Vous n'avez pas pu vous introduire dans le manoir de nuit, à cause des dantesques protections du mur d'enceinte, et vous en ressortiriez aujourd'hui sans un seul indice tangible ? Que nenni ! Place à l'improvisation.

Le majordome vous refait traverser le parc jusqu'au poste de garde. Vous interpellez alors le gendarme de faction, clamant que "plus vous y pensez, plus vous êtes certain de l'avoir déjà vu quelque part ; n'étiez-vous pas ensemble à l'université ?". Le majordome repart vaquer à ses affaires, et vous maintenez pendant quelques minutes une discussion chaotique, que vous faites dériver sur les insondables subtilités des poteries prétectonnes de Kéroskia. A la fin, votre malheureux interlocuteur est avachi dans sa guérite, avec dans les yeux une unique supplique : "partez d'ici et fichez-moi la paix". Vous faites mine de vous être mis en retard, et sortez prestement en lui demandant d'ouvrir le portail. La lourde porte métallique se referme à nouveau, dans un grand fracas ; mais profitant d'être hors de vue du gendarme, vous êtes resté à l'intérieur, entre la guérite et le mur d'enceinte.

Précautionneusement, de bosquet en arbre, vous faites le tour du parc, pour revenir vers l'arrière du manoir ; la plupart des fenêtres sont voilées, voilà qui vous arrange bien. Pas de molosse en vue, non plus. Le vieil Alphonse fait des allers-retours pour étendre du linge, sur le porche arrière, en chantonnant des airs paillards. Un instant d'inattention de sa part, et vous voilà de nouveau dans le manoir.

Vous vous cachez dans le réduit, sous l'escalier en colimaçon du Grand Hall. Le vieux chien Bedou dormait tout à l'heure dans le hall secondaire, pourvu que cela dure.

12h sonne à l'horloge. A travers le mur, vous entendez Loyd Georges discuter, dans sa chambre, avec l'inspecteur Shark. Le policier harangue son hôte, le pousse à être plus direct et brutal avec les "suspects". Loyd Georges, déjà las, dit faire de son mieux. Puis un dialogue capture votre attention.

- Puis-je avoir l'identité de cet individu, qui parait-il, s'est grimé en éboueur, pour vous approcher tôt ce matin ?
- Qui vous a dit cela ?
- C'est mon rôle de tout savoir ; et de vous protéger, y compris contre vous-même.
- Cet "individu" m'apportait juste des nouvelles fraîches de mon ami le professeur Loakim, et il est reparti sans tarder. Il n'y a aucune malice à cela.
- Vous sous-estimez le pouvoir de corruption de vos ennemis. Vous a-t-il donné des objets, qui pourraient être piégés ? A-t-il été laissé seul dans le manoir, à un quelconque moment ?
- Non et non. Laissons de côté cet évènement inoffensif, qui nous fait perdre notre temps.

Le majordome entre alors dans le Grand Hall avec un nouveau visiteur, ce qui interrompe leur controverse. Impossible d'entendre la suite des échanges, maintenant qu'ils ont à nouveau lieu dans le bureau de Loyd Georges ; l'inspecteur semble être resté à écouter depuis la chambre, le fourbe.

Vous réfléchissez à vos prochains déplacements, lorsque vous avisez un petit écran encastré dans le mur. Chance, le terminal de contrôle des caméras du manoir. Vous repérez la position des **caméras ({% symbol "grand hall, bureau, bibliothèque, salle à manger, cuisine" for "videosurveillance_cameras_locations" %})**, et des habitants du lieu, avant de désactiver ce système. Voilà qui vous enlève une belle épine du pied. {% fact 'amethyst_disabled_surveillance_cameras' as author %}

Vous anticipez les déplacements des serviteurs dans le manoir. Vers 12h15, le majordome lance à Alphonse qu'il part en ville préparer la logistique de la soirée du lendemain, et qu'il lui confie donc la surveillance des visiteurs.
Un des participants aux enchères, **{{character_properties.opal.official_name}}**, passe à quelques pas de vous, en claudiquant sur sa canne.

Ne pouvant approcher des salles les plus intéressantes, vous montez à l'étage, et parcourez longuement la "collection" de Loyd Georges, un ramassis d'objets hétéroclites et de faible valeur : des chapeaux de cuir slavinkiens, d'énormes pachydermes en bois sculpté, de vieux grimoires de contes thélassars à moitié vermoulus, des armes et masques en bronze érodés... Le sol est bien balayé, mais sur les artefacts et les vitrines, la poussière a repris ses droits depuis longtemps. Aucun objet ne semble avoir été touché récemment, et aucune cachette apparente. Palsambleu.

En redescendant les escaliers, vers 12h45, vous avez une intuition. Le courrier serait-il passé ? Bingo ! La boite aux lettre du vestibule est mal refermée ; vous y trouvez deux brochures publicitaires, une lettre provenant d'une boite postale anonymisée, et un fin colis. Vous fourrez ces deux derniers plis dans votre poche.

Des bruits de pas dans le Grand Hall vous forcent à migrer vers la salle à manger, mais le vieil Alphonse continue sa route vers vous, et il y a du bruit en cuisine... vous vous réfugiez donc dans le spacieux garde-manger. En sautant vous cacher derrière les tonneaux de vin, vous vous retrouvez nez-à-nez avec un autre intrus. L'enchérisseur {{character_properties.malachite.official_name}}.

{% macro spies_locked_in_pantry() %}

{% fact 'amethyst_and_malachite_locked_in_pantry' as author %}

L'individu a l'air tout aussi ahuri que vous.

Dans cette situation hautement désagréable, une trêve tacite se met immédiatement en place. Vous restez 5 minutes en silence, côte à côte, à écouter les derniers préparatifs du repas de midi ; et à vous demander comment repartir sans encombre du manoir, le moment venu.

Tout s'accélère lorsqu'un museau canin gris vient fureter sous le porte du garde-manger. La voix d'Alphonse retentit.

- Bedou ! Laisse donc toute cette bouffe tranquille, maudit gourmet ! Ta gamelle t'attend dehors !

Le chien aboie frénétiquement en grattant contre la porte. Vous vous regardez quelques secondes, avec votre acolyte accidentel, avant de vous retourner vers le haut vasistas du garde-manger. En grimpant sur un coffre, vous cassez la sangle qui entrave son ouverture, sortez l'un après l'autre en quelques mouvements athlétiques, et le refermez juste avant que la porte ne s'ouvre.
{% endmacro %}
<{ spies_locked_in_pantry }/>

L'autre espion longe le mur à quatre pattes, en profitant de la protection d'une petite haie aux baies rouges ; il semble savoir ce qu'il fait, vous lui emboitez le pas. Aucune alerte n'a été déclenchée, mais ce n'est pas une raison pour trainer ici. Arrivé à l'avant du manoir, l'individu se remet debout, et prend le chemin du portail ; vous le rattrapez, et échangez des banalités avec lui, en travestissant votre voix, et en prenant garde à vous placer du côté opposé à la guérite.

{% macro spies_escape_from_manor() %}
Le gendarme vous ouvre sans même lever les yeux de son journal.
Sans un mot, sinon un petit soulevé de chapeau, vous partez chacun de votre côté ; avec un grand soulagement au fond de la poitrine.
{% endmacro %}
<{ spies_escape_from_manor }/>

Un soulagement incomplet toutefois. Le fin colis marron a dû tomber pendant votre escalade du vasistas. Mais vous retrouvez bien la lettre pliée au fond de votre poche, et son contenu vous laisse songeur. {% fact 'amethyst_has_stolen_manor_letter' as author %} {% fact 'amethyst_has_lost_thin_manor_parcel' as author %} {% hint "stolen_manor_letter_for_amethyst" is needed %}

Vous passez le reste de la journée à tenter, en vain, d'obtenir des informations sur l'orbe.
Vous rentrez vous coucher très tôt, dans votre petite chambre du {% symbol "8e étage de l'Hotel SalimaGlobeCenter" for "amethyst_hostel_room" %}.
{% fact "amethyst_alibi_is_void" as author %}

{% macro no_partner_communication_occurred_and_gala_planned() %}
Le lendemain, vous êtes accaparé par une foultitude de petites affaires à régler, et vous n'avez donc pas le temps de faire le point avec votre compère. Une grande soirée de gala est prévue le soir, pour relancer cette série d’enchères.
{% endmacro %}

{% macro pantry_spies_ending() %}
<{ no_partner_communication_occurred_and_gala_planned }/>Vous comptez bien en profiter pour soutirer à Loyd Georges quelques informations, et enquêter davantage auprès des autres enchérisseurs, dont votre "allié" involontaire du garde-manger. Cela sera-t-il suffisant pour tirer toute cette histoire d'orbes au clair ?
{% endmacro %}
<{ pantry_spies_ending }/>

