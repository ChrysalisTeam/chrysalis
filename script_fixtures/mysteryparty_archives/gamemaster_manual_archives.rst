
################################
MANUEL DU MAITRE DE JEU
################################

Principes fondamentaux du jeu
#####################################

Pitch
=====

Lorsque la nuit tombe sur les archives secrètes des Maupertuis, trois mondes s’animent et se croisent : celui des vivants, celui des livres, et celui des morts.

Plongez dans cet antre d’art et de magie, et brisez la malédiction qui y maintient les âmes prisonnières.

*"Les Archives Secrètes Des Maupertuis" est une soirée-mystère pour 12 joueurs, qui se joue en 3-4h environ.*


Concept détaillé
=====================

Plusieurs groupes d'aventuriers se sont infiltrés dans une bibliothèque souterraine abandonnée, et s’y retrouvent piégés par un mystérieux pouvoir. A la nuit tombée, ces lieux prennent vie, et se peuplent d'une multitude d'êtres plus ou moins bienveillants, plus ou moins énigmatiques. Qui sont ces étranges personnages, captifs des lieux eux aussi - certains fantomatiques, d’autres au contraire bien trop vivants ?

Cette soirée-mystère met l'accent sur une ambiance légèrement angoissante, mais plus encore envoûtante, à la façon d'un Labyrinthe de Pan, d'un Voyage de Chihiro, ou d'un Alice au Pays des Merveilles. Autres références possibles : la Nuit au Musée, les archives secrètes du Vatican, le mythe de Cthulhu… Pour les costumes, on se place principalement dans une esthétique entre le steampunk et l'occultisme.

Les joueurs ont une feuille de mission par groupe, et seulement une ou deux compétences spécifiques par personne (ce n'est pas un jeu romanesque, où le caractère et le passif des joueurs sont primordiaux). Ils sont amenés à faire connaissance les uns avec les autres, à discuter avec des figurants regorgeant de services et de secrets, et à résoudre des énigmes simples (recherche d'objets, ouverture de serrures, déchiffrement de runes...).

Pour une bonne atmosphère, l’idée est que la bibliothèque soit plongée dans le noir, seulement éclairée par quelques lanternes portées par les joueurs ou posées à côté des figurants. Une machine à fumée et des spots lumineux peuvent être utilisés, en plus d'enceintes sonores, pour encore plus d'immersivité, voire quelques moments chorégraphiés façon “Son & Lumière”.


Histoire du jeu
===========================

{% macro common_npc_tragedy_knowledge() %}

La rencontre des Maupertuis et des Avatars
+++++++++++++++++++++++++++++++++++++++++++++++++++

*Connaissances communes aux avatars et aux fantômes, sauf le voleur.*

**La malédiction de la bibliothèque a débuté {% symbol "500 ans" for "library_initial_events_timedelta" %} avant le temps du jeu, c'est-à-dire qu'elle a eu lieu en l'{% symbol "an 500" for "library_initial_events_year" %} de l'{% symbol "ère du Grand Apaisement" for "current_era_name" %}. Nous sommes actuellement en l'{% symbol "an 1000" for "current_events_year" %} de cette ère de prospérité.**

L'enfant, **{% symbol "Octave" for "maupertuis_son" %} de Maupertuis**, a connu une destinée tragique. Il est issu, par sa mère (**{% symbol "Isadora" for "maupertuis_mother" %}, née Guerlevan**) et son père (**{% symbol "Quirinius" for "maupertuis_father" %}**) de deux grandes lignées de magiciens-guérisseurs. Ses parents sont morts lorsque le domaine a été attaqué et rasé par des fidèles du **dieu {% symbol "Bahamoot" for "god_of_diakons" %}**, sur ordre du **{% symbol "cardinal Tridentès" for "old_guru_name" %}**, lors du {% symbol "marasme planétaire" for "catastrophic_period" %}. {% symbol "Octave" for "maupertuis_son" %} avait alors **{% symbol "10" for "maupertuis_son_age" %} ans**. Sa soeur, **{% symbol "Mérédice" for "maupertuis_daughter" %}**, qui avait **{% symbol "16 ans" for "maupertuis_daughter_age" %}**, a disparu durant ces évènements.

{% symbol "Octave" for "maupertuis_son" %} s'était réfugié lors de l'attaque dans les archives souterraines, avec son précepteur **{% symbol "Maître Parchemine" for "archivist_name" %}** (ne pratiquant pas la magie). Le portail magique reliant le manoir à cette bibliothèque (située très loin sous la surface) avait été détruit lors de l'attaque, mais il restait des portails secondaires vers d'anciens châteaux de magiciens - tous en ruines - répartis sur la planète. Ces portails étaient enchantés depuis des siècles pour s'ouvrir une journée par an uniquement, lors du **{% symbol "solstice d'hiver" for "astral_opening_date" %}**, pour une célébration commune de la nouvelle année, même si cette tradition n'était plus respectée depuis longtemps.

Les deux survivants ont vécu là seuls **{% symbol "15 mois" for "octave_life_in_archives_delay" %}** durant, le précepteur estimant qu'{% symbol "Octave" for "maupertuis_son" %} n'était pas encore prêt pour affronter la rudesse du dehors. Ils n'ont pas pu se rendre dans le "domaine interdit" de la bibliothèque, gardé par une Bête, car Octave n'avait pas encore reçu l'initiation lui permettant d'ouvrir le passage vers ce saint-des-saints, contrairement à sa soeur. {% symbol "Maître Parchemine" for "archivist_name" %} s'est improvisé archiviste pour passer le temps, et a commencé un inventaire des livres "non bizarres" accessibles. {% fact "archivist_began_cataloging_books" %} Esseulé, l'enfant s’est réfugié dans la lecture de romans fantastiques, lisant et relisant ses préférés, et liant une connivence de plus en plus forte avec les héros de ces oeuvres.

Sous l’action de la magie imbibant les lieux, et des souhaits lancinants d’Octave, plusieurs personnages imaginaires se sont réellement incarnés dans la bibliothèque, devenant ainsi ce que l'on appelle des **"avatars"** : un inventeur, un druide, une duchesse, une samuraï, un chevalier, un pilote de biplan...

L'enfant et ses nouveaux amis se retrouvaient au moins un jour chaque semaine dans la bibliothèque, pour festoyer, jouer, fabriquer des automates, et apprendre moult choses sur les règles régissant chacun des univers représentés.
L’archiviste les a vite découverts, mais il a bien dû accepter la situation, tout en interdisant aux avatars de sortir de la bibliothèque.

Quelques mois plus tard a eu lieu le **{% symbol "solstice d'hiver" for "astral_opening_date" %}** suivant. **L’arkonte (paladin-exorciste) {% symbol "Valerias" for "arkon_name" %}**, de religion yodique (et plus particulièrement de confession mithraïte), qui résidait dans le **{% symbol "Monastère de Rochesombre" for "common_monastery_name" %}**, a senti la présence des âmes non-humaines. Il s’est infiltré dans la bibliothèque secrète, et a confronté l’archiviste et l’enfant qui s'apprêtaient à en partir.

Ceux-ci ont finalement accepté de ne plus faire courir de risque à l’humanité avec un mélange contre-nature des mondes, et de laisser l’arkonte renvoyer définitivement les avatars hors de la Terre ; en retour, l’arkonte amènerait avec lui {% symbol "Octave" for "maupertuis_son" %} et l'archiviste, en sécurité, dans un pays accueillant.

Après des adieux déchirants, les personnages imaginaires sont chacun retournés dans leur univers, en attendant que le rituel fermme leur accès au monde des humains.


Le retour des Avatars
+++++++++++++++++++++++++++++++++

*Ces connaissances sont propres uniquement aux avatars.*

Certains des avatars ont effectivement vu le passage interdimensionnel se refermer. Mais pour trois d'entre eux - **l'inventeur {% symbol "Sir Jacques Vaucanson" for "inventor_name" %} (que tout le monde appelle {% symbol "Jacko" for "inventor_nickname" %}), le druide {% symbol "Diviciacos" for "druid_name" %} et la duchesse {% symbol "Cassiopée de Thiersonne" for "duchess_name" %}** - cela n'a pas été le cas. Leurs mondes imaginaires respectifs restaient connectés au monde des vivants.

Lorsqu'ils sont revenus dans la bibliothèque s'enquérir de la situation, ils ont trouvé le pentacle toujours en place, quelques traces de sortilèges et de combat (atténuées par les protections magiques du mobilier) ; horreur, le **squelette sans crâne** de l'arkonte gisait dans un coin au milieu de ses armes ; ainsi que quelques cendres - probablement de l'enfant et de son précepteur - à d'autres endroits.

Éplorés, ces avatars subsistants ont créé un **cimetière improvisé** pour les restes défunts. Ils ont **vivement débattu** de la place à accorder aux ossements de l'arkonte, car **autant le druide le tenait pour responsable du massacre, autant la duchesse et l'inventeur pensaient que cela pouvait être un accident, ou l'action d'une autre entité**. Au bénéfice du doute, ils ont finalement laissé toutes les dépouilles ensemble au cimetière.

Les avatars ont ensuite investigué l'ensemble de l'étage autorisé de la bibliothèque, mais en vain, les connaissances en magie de ce monde leur manquant trop. Ils n'ont trouvé que quelques livres factices et coffrets verrouillés, qu'ils n'étaient pas capables d'ouvrir. Le passage vers le domaine interdit, de son côté, était toujours bloqué par le sortilège immémorial des Maupertuis. Et impossible de rejoindre la surface, même lors d'un {% symbol "solstice d'hiver" for "astral_opening_date" %} suivant. {% hint "beast_snack_as_moon_stones" is needed %}

La duchesse a, dans son propre monde, reçu d'un devin la révélation que les récents défunts étaient toujours prisonniers de la bibliothèque sous forme de fantômes, mais que lors d'un prochain anniversaire de l'évènement tragique, cette malédiction serait brisée. Depuis, tous les ans, les avatars se réunissent pour un **{% symbol "banquet d'outre-monde" for "banquet_name" %}** en l'honneur des Maupertuis, dans l'attente de la réalisation de cette cruciale prophétie.

{% endmacro %}
<{ common_npc_tragedy_knowledge }/>


Fond de l’intrigue (SPOILER)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

L'un des avatars, le duide aux pouvoirs surhumains, était en fait devenu le grand méchant dans son univers ; l’enfant ne le savait pas, n’ayant jamais retrouvé le dernier tome de la série. Cet ancien héros, désirant prendre le contrôle de cet univers aussi, est revenu par ledit Tome, a assassiné les vivants pendant le rituel, puis a joué la surprise vis-à-vis des personnages imaginaires restants, revenus plus tard s’enquérir de la situation.

Réalisant le fléau qui menaçait le monde des humains, l’arkonte avait cependant réussi, dans son dernier souffle, à jeter un sortilège sur le traître ; un sortilège qui a piégé la bibliothèque entière dans un "trou noir" du monde spirituel : que l'on soit véritable humain ou personnage imaginaire, on pourrait désormais y entrer, mais pas en sortir, aussi longtemps que le traître serait "en vie". Les trois humains sont donc restés piégés en tant que fantômes (spectres s’incarnant par moments) dans ces lieux ; de même que les personnages de roman, qui peuvent cependant toujours aller et venir entre la bibliothèque souterraine et leur propre monde littéraire.

Outre leurs propres objectifs, les joueurs doivent donc apprendre la différence entre ces différents types de protagonistes, et trouver le moyen de démasquer et détruire le traître, pour finaliser la malédiction et libérer les âmes errantes.

Principes fondamentaux des différents mondes
============================================

{% macro explanation_of_different_worlds() %}

Le monde des vivants
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

C’est une uchronie de notre propre monde ; tout ce qui se passe avant 1908 y est identique au nôtre, puis s’est produit un “grand marasme” tectonique et climatique qui a tout chamboulé pendant des siècles. Les lois scientifiques, la psychologie des humains, sont identiques à notre monde, avec en plus la présence de “magie”.

- Les vivants peuvent voir et entendre aussi bien les personnages du monde des morts que des livres, et peuvent toucher les personnages du monde des livres.

- Pour un vivant, tout contact avec un fantôme désincarné, en errance, est très dangereux. Un fantôme incarné, en revanche, est sans danger, et passe à travers les vivants sans les impacter. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- Les vivants sont par défaut sensibles aux attaques physiques, magiques et sacrées.

- Les vivants sont soumis aux règles du “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

Le monde des morts
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Il est représenté par les humains ou bêtes qui sont morts dans la bibliothèque après sa malédiction, et ne peuvent donc rejoindre l’au-delà.

- Les morts peuvent se voir et se toucher mutuellement, mais ne peuvent se nuire entre eux. Les fantômes incarnés peuvent “repousser” leurs congénères désincarnés.

- Les morts ne peuvent ni voir, ni entendre, ni sentir les personnages du monde des livres.

- À aucun moment les morts ne peuvent interagir avec les objets du monde vivant. Seule exception, le buffet est composé de plats et boissons compatibles avec tous les mondes.

- Lorsqu'il touche un vivant, tout fantôme désincarné, en errance, le blesse dangereusement. Un fantôme incarné, en revanche, est sans danger, et passe à travers les vivants sans les impacter. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- Seules des attaques sacrées peuvent atteindre les morts, pas les attaques physiques ni magiques. Mais puisque présentement ils ne peuvent pas s'échapper de la bibliothèque, s'ils sont blessés, ils reviennent systématiquement plus tard, sous une forme plus folle et agressive.

- Les fantômes sont soumis à des **règles complexes d'errance, d'incarnation et d'ancrage**, voir le chapitre à ce sujet.

- Les fantômes ne sont PAS soumis aux règles du “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{# NOT YET - Des entités “démoniaques”, faisant elles aussi partie du monde des morts, pourraient être invoquées dans ce contexte. Elles auraient alors les mêmes propriétés que les fantômes, avec davantage de liberté, d’hostilité, et de pouvoirs magico-sacrés. #}

Le monde des livres
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les personnages issus du monde littéraire, imaginaire, sont uniquement des héros de romans auxquels l’enfant Octave a donné vie parce qu’il les admirait particulièrement. On les appelle aussi ”\ **avatars**\ ”.

Ces personnages sont dans l’état où leurs auteurs les avaient laissés à la fin de leurs “histoires” respectives, et non selon ce que l’enfant sait/imagine d’eux. Ils ne vieillissent pas.

Ils retournent chacun dans leur monde parallèle via leurs livres, lorsqu’ils le désirent. Le temps s’écoule identiquement dans tous les mondes, mais dans leurs livres, les avatars vivent un “éternel présent”, où leur situation est globalement immuable, puisque leur auteur a cessé son travail d'écriture.

- Si les avatars meurent dans le monde réel, cela équivaut à une mort dans leur monde imaginaire (une mort soumise à leur propre système de croyances religieuses) ; ils y sont alors reprojetés, et ne deviennent pas des fantômes dans le monde réel.

- Ils peuvent interagir librement avec le monde des vivants, ses humains et animaux, ses objets et grimoires ; **sauf avec les "romans"**, qu’il ne peuvent déplacer car ces livres portent en eux un univers entier. {% fact "avatars_cannot_carry_novels" %}

- Ils ne peuvent ni voir, ni entendre, ni sentir les personnages du monde des morts, et ne craignent pas leur toucher (en phase incarnée ou non).

- Ces avatars portent leurs costumes et accessoires “typiques” de leurs romans, ceux qu'ils avaient quand Octave les a, involontairement, invoqués.

- Ils ne peuvent ramener aucun autre objet ou individu depuis/vers leur monde d’origine (pas mêmes des accessoires décoratifs). Ils sont donc, en toutes choses, limités à ce que la bibliothèque des Maupertuis contient.

- Ils ne peuvent pas aller dans le monde d'autres avatars, ni accueillir dans leur propre monde des vivants ou des fantômes.

- Ils conservent majoritairement les super-pouvoirs qu’ils possèdent dans leur propre univers (régénération, force, sorts…)

- Ils sont sensibles aux attaques physiques et magiques, mais le sacré (et le monde des fantômes) ne leur fait rien car leur "transcendance" n'est pas la même que les humains.

{# mais avec des risques d'effets de bord dangereux, à cause d'incompatibilités entre les lois fondamentales des univers ; dans le cas présent, { % fact "avatar_abilities_are_randomly_hazardous" % } #}

- Ils ne sont PAS soumis aux règles du “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”, et peuvent d'ailleurs s'en moquer allègrement, en jurant toutes sortes de choses farfelues. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

Le monde des automates
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*Les assistants logistiques, photographes, et servants du buffet, ont intérêt à faire partie de ce monde-là pour un surcroît d'ambiance et une bonne liberté d'action.*

Avec l'aide d'Octave, l'avatar "inventeur" avait conçu des automates pouvant, par exemple, faire le service de la table. Il s’agit d’entités purement mécaniques, dénuées de toute conscience et de tout pouvoir magique. Certains peuvent parler et comprendre des ordres simples ; d'autres automates sont limités à des tâches très précises comme servir les mets et boissons, ou faire le ménage. {% fact "inventor_has_built_androids" %}

Pour être plus facilement distingués des avatars, outre leurs démarches et paroles, les automates doivent porter des **{% symbol "rubans blancs" for "automaton_symbolic_cloth" %}** autour du cou et des poignets. {% hint "white_ribbon_cloth_for_automatons" is needed %}

Ils obéissent uniquement au personnage (figurant ou joueur) portant un **bracelet large argenté appelé le {% symbol 'Dominion' for 'androids_command_bracelet_name' %}**. Ils répondent du mieux possible à ses ordres, tant qu'ils sont dans leurs compétences, et ne contredisent pas frontalement leurs règles innées de non-agression et de survie. *En cas de doute sur comment réagir à un ordre difficile, simuler l'hésitation ou l'incompréhension de l'automate, et demander discrètement au maître de jeu.* {% fact "robots_obey_but_refuse_violence_or_sacrifice" %}

Les robots voient les vivants et les avatars, mais PAS les fantômes. Ils sont visibles par tous.

Ils sont globalement lents et rigides dans leurs mouvements. Mais ils disposent d'une **immmense force physique**, et peuvent donc déplacer des objets de type ULTRA-LOURD à la demande. En cas d'empoignade, ils gagneraient facilement contre un humain.

Ils sont sensibles aux attaques physiques et magiques (hormis les poisons bien sûr), mais pas aux attaques sacrées.
Plus précisément, ils craignent les explosifs et les coups d'épée, mais peu les projectiles (balles ou flèches).

Rôles typiques possibles (un automate peut en changer en cours de partie) :

- Automate nettoyeur (1 plumeau est disponible)
- Automate serveur de boissons et de plats
- Automate majordome, qui veut enlever leurs manteaux aux joueurs et leur faire visiter l'étage autorisé
- Automate chanteur (a cappella, ou prévoir une musique instrumentale)
- Automate blagueur (prévoir 5-6 blagues non-contemporaines à raconter sur demande)
- Automate encyclopédique (invente tout un discours farfelu quand on lui demande une information)
- Automate photographe

Idées d'interactions possibles pour certains automates :

- Ils répètent toujours quelques phrases stéréotypées aux joueurs, même hors de propos.
- Ils font la poussière non seulement sur les étagères, mais aussi sur les autres personnages.
- Ils portent des lampes et suivent les joueurs qui le leur demandent.

Paroles typiques :

- "Soyez le bienvenu dans notre humble demeure"
- "Monsieur/madame désire-t-il/elle quelque chose ?"
- "Daignez goûter ces douceurs fort onéreuses"
- "Je vous prie d'accepter cette boisson gouleyante à souhait"
- "Puis-je vous débarrasser de votre manteau ?"
- "Je sers la lignée des Maupertuis et c'est une immense joie."
- "A votre gauche le tombeau du graaaaand mage Mos Peratys, fondateur de la lignée..."

Ils peuvent dysfonctionner par moment, jusqu'à ce que l'avatar inventeur ou un joueur ne les débloque :

- Ils bégaient, butent contre les murs et obstacles, se coincent les bras les uns dans les autres, ou bougent bizarrement sur place façon "engrenage défectueux"...
- Ils peuvent se retrouver dans une impasse logique, en voulant constamment céder la priorité à un autre automate : "Mais non... Après vous... Je n'en ferais rien...".

Rôle spécial : **l'automate de garde**, armé, qui patrouille dans la bibliothèque pour la protéger contre de possibles assaillants (voir sa fiche de figurant, et ses interventions programmées).

Les automates ne sont PAS soumis aux règles du “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{# NOPE NOT FOR NOW
  Lorsque, bien plus tard, les joueurs arrivent à accéder au {% symbol "Thanatologue" for "book_of_the_dead" %}, il est POSSIBLE de déclencher une bande-son intense lors de la première ouverture de ce grimoire maudit.
  Les automates de service deviennent alors possédés, et claudiquent vers les joueurs, en battant des bras, et en ressassant "Mort aux hérétiques !".
  Les joueurs doivent alors les éviter jusqu'à la fin de la bande-son ; à ce moment-là, les automates redeviennent normaux, et reprennent leurs tâches habituelles.
#}

Le monde divin
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les entités faisant partie du “\ **divin**\ ” - le figurant **l’Ankou**, et le maître de jeu en **Djinn renégat** - peuvent voir tout le monde et être vues de tous, et sont par défaut sans danger pour les différents personnages.

Ils sont également insensibles aux armes et aux sortilèges (dont la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %}) entourant la bibliothèque. {% fact "ankou_sees_all_and_is_harmless_for_all" %}

Ils ne sont PAS soumis aux règles du “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}

{% endmacro %}
<{ explanation_of_different_worlds }/>

Équipes de joueurs
==================

Tout débute lorsque des explorateurs héliossars (ceux présents dans le jeu), à la recherche des secrets des Maupertuis, exhument des monolithes couverts d'inscriptions antiques. Hélas pour eux, des images de leur trouvaille fuitent, et font le tour de la presse mondiale ; quelques groupes de personnes se révèlent capables de la déchiffrer, et de comprendre ainsi le fonctionnement des portails menant à la bibliothèque des Maupertuis, portails actifs lors du **{% symbol "solstice d'hiver" for "astral_opening_date" %}** qui arrive. Tous ces gens s’y rendent prestement à cette date, pour des raisons différentes, sans réaliser qu’ils se jettent ainsi dans la gueule du loup.

Les explorateurs héliossars
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ces 3 aventuriers-archéologues tentent de préserver leur pays, Héliossar, contre les nouvelles envies de conquête de leur puissant voisin, la Théocratie akarite. Ils ont appris que les akarites avaient mis la main sur une copie du légendaire {% symbol "Thanatologue" for "book_of_the_dead" %}, le Livre des Morts d’une civilisation disparue, et en avaient tiré un plan pour une invasion “inéluctable” d’Héliossar. Ils recherchent donc l'exemplaire que les Maupertuis, d’après la légende, possédaient, afin de comprendre et surtout parer ce plan de conquête.

Leurs compétences sont orientées vers les sciences physiques et humaines.

{% macro explorer_group_symbols() %}
Le vêtement de reconnaissance des explorateurs héliossars est une **ceinture beige** *(fournie par les organisateurs)*.

Leur devise est **"Le savoir est pouvoir"**, en pointant l'index vers le ciel.
{% endmacro %}
<{ explorer_group_symbols }/>

La famille Parcival
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ces 3 frères et soeurs sont les lointains descendants de Mérédice de Maupertuis, la soeur d’Octave que tout le monde croyait morte avec sa famille, mais qui avait en réalité pu s’échapper et refaire sa vie.

Ces Parcival ont lu dans l’autobiographie de leur ancêtre Mérédice comment ses parents, magiciens-guérisseurs, l’avaient soignée d’un grand mal héréditaire, la dégénérescence marbrée, grâce à un "{% symbol "Cocktail de Réjuvénation" for "parcival_disease_main_remedy_name" %}". Lorsque leur petite soeur commune est tombée malade à son tour (il ne lui reste que quelques semaines à vivre), ils sont partis en quête du remède, et leur enquête les a menés jusqu’aux archives enfouies de l'ancien domaine familial.

Leurs compétences sont orientées vers la nature et la magie.

{% macro parcival_group_symbols() %}

Le blason de la famille Parcival est un **bâton noueux autour duquel un unique serpent est enroulé**.
{% fact "coat_of_arms_of_parcival_is_partial_caduceus" %}

Son vêtement de reconnaissance est un **jabot bleu-royal** *(fourni par les organisateurs)*.

Sa devise est **"Noble de coeur comme de sang"**, le poing fermé sur le coeur.
{% endmacro %}
<{ parcival_group_symbols }/>

Les diacres de {% symbol "Bahamoot" for "god_of_diakons" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ces 3 moines officient pour le culte du dieu {% symbol "Bahamoot" for "god_of_diakons" %}, très ancré dans la région. L’oracle de leur monastère a senti qu’une âme ivre de haine se trouvait dans les ruines du manoir Maupertuis (il s’agit de la Bête), ainsi que des âmes errantes (les fantômes). Ils s’y rendent donc pour résoudre les problèmes, et protéger l’ordre des choses.

{# **Ils ont aussi ordre de détruire magiquement les 3 livres “maléfiques” que contient le domaine interdit des Maupertuis, de peur qu’ils ne tombent en de mauvaises mains (la bibliothèque ne peut pas juste être brûlée). ?** NOPE #}

Leurs compétences sont orientées vers la théologie et l’ésotérisme.

{% macro diakon_group_symbols() %}
Le vêtement de reconnaissance des diacres de {% symbol "Bahamoot" for "god_of_diakons" %} est une **étole violette** (écharpe portée en travers du torse).

Sauf instructions spécifiques, lors des rituels et des processions, les diacres gardent les mains jointes par les pointes des doigts, les paumes éloignées l'une de l'autre, comme s'ils enserraient un globe entre elles ; c'est leur signe de prière. Lors de leurs déplacements en procession, ils ânonnent un **son "ôôôôhm"** lent et guttural.

Lors des rituels, ils aiment **clamer bien fort** leurs invocations, avec emphase.

Leur devise est **"Le dragon est notre guide"**, à professer les mains jointes en prière, là encore.

{% endmacro %}
<{ diakon_group_symbols }/>

Les agents secrets mirandiens
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

L’île autonome de Mirandia, et son positionnement stratégique au centre de l’océan diorique, ont attiré les convoitises de ses voisins. Piégée par des complots économiques, surendettée, l’île est sur le point d’être annexée et vendue au plus offrant.

Ces 3 agents étatiques ont donc remué ciel et terre pour retrouver le mythique (et “dangereux”) trésor de la famille Maupertuis, et sauver ainsi leur patrie de la faillite.

Leurs compétences sont orientées vers les “gadgets technosteam”.

{% macro spy_group_symbols() %}
Le vêtement de reconnaissance des agents secrets mirandiens est un **brassard vert émeraude** *(fourni par les organisateurs)*.

Leur devise est **"Mirandia pour toujours brillera"**, avec un salut militaire la main contre la tempe.
{% endmacro %}
<{ spy_group_symbols }/>

Figurants
=========

**Ces rôles peuvent être joués au masculin comme au féminin, en adaptant les noms et titres si nécessaire.**

Octave de Maupertuis (l’enfant)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_octave_character_summary() %}

- FANTÔME

- Traits : candeur, spontanéité, enthousiasme, affection

- Octave ne sait pas comment il est mort, ni pourquoi il est prisonnier de ce lieu, ni pourquoi il est ancré à un endroit précis.

- Excité d’apprendre que les joueurs ont croisé son précepteur (l’enfant savait déjà par l’Ankou qu’il est prisonnier en fantôme aussi), et désireux de le revoir au plus vite.

- Passionné de littérature fantastique et autres livres.

- “Mes parents m’ont dit de ne jamais parler à des inconnus. {% symbol "Maître Parchemine" for "archivist_name" %} aussi. Mais je m’ennuie trop, alors tant pis”

{% endmacro %}
<{ phantom_octave_character_summary }/>

{# BOF
**Journal intime quelque part ?**
**S'il arrive au coin enfant (avec jouet et peluche) il donne davantage d’informations ?**
#}

{% symbol "Maître Parchemine" for "archivist_name" %} (le précepteur d'Octave et archiviste )
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_archivist_character_summary() %}

- FANTÔME

- Traits : jovialité, sagesse, bienveillance, paternalisme, méticulosité

- Sage et un peu érudit, mais a très peu de connaissances en magie.

- Il enseignait principalement à Octave ses humanités (sciences, lettres...), laissant aux parents le soin de transmettre leur héritage de magiciens.

- Il a tiré profit de leur enfermement initial dans la bibliothèque, suite au saccage du manoir, pour s'improviser archiviste, et commencer à trier l'étage autorisé. Il prenait juste soin de ne pas manipuler les grimoires aux allures louches. {% fact "archivist_began_cataloging_books" %}

- Le précepteur ne sait pas comment il est mort, ni pourquoi il est prisonnier de ce lieu (soupçonne une trahison de l’arkonte), ni pourquoi il est ancré à un endroit précis.

- Il a tenu un petit **journal de bord** pendant leur enfermement, qui doit se trouver quelque part dans la bibliothèque. {% fact "archivist_began_diary_during_confinement" %}

- Excité d’apprendre que les joueurs ont croisé l’enfant (le précepteur savait déjà par l’Ankou qu’il est prisonnier en fantôme aussi), et désireux de le revoir au plus vite.

- Se demande ouvertement si ce n’est pas son oeuvre d’inventaire et rangement complet de la bibliothèque, inachevée, qui le retient dans ce monde.

- S’assure de la bonne volonté initiale des joueurs (potentiellement grâce au “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}”), puis les aide en leur prodiguant énormément de conseils, et d’informations sur les lieux.

{% endmacro %}
<{ phantom_archivist_character_summary }/>

{# BOF
**Faiblesse face aux méchants : adore les livres : fera tout ce qu’on lui demande si on menace un livre**
**Ne sait plus comment est rangée la bibliothèque,**
**Peut retrouver la fiche des emprunts du garçon : cette fiche liste les livres des figurants notamment les tomes dont est issu le méchant.**
#}

L’arkonte {% symbol "Valerias" for "arkon_name" %} (le paladin-exorciste légendaire)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_arkon_character_summary() %}

- FANTÔME

- Traits : méfiance, sens du devoir, bonne volonté, intelligence, sévérité

- "Arkonte" est un titre désignant une "chevalerie bénie par les dieux" dans les religions dites "yodiques"

- L’arkonte se souvient de sa mort en combat singulier, et d'avoir jeté la malédiction sur la bibliothèque. Il sait être attaché mystiquement à la zone de sa mort violente.

- À la fois plein d'espoir en voyant des aventuriers ici, et en même temps inquiet qu'ils ne terminent tous, par sa faute, morts et enfermés comme les autres.

- Un peu désabusé de voir que le culte païen du dieu {% symbol "Bahamoot" for "god_of_diakons" %} a finalement remplacé le sien (le culte yodique de confession mithraïte), dans le monastère à la surface

- Exige de pouvoir faire sa “{% symbol "confession de mission" for "arkon_mission_confession" %}” à un prélat de la religion yodique, et uniquement dans ce cas il livre tout ce qu’il sait sur la situation ; n’aide que les joueurs en qui il a confiance pour mener à bien sa mission de protection de l’humanité (et qui ne vont pas simplement lever le confinement de la bibliothèque, en détruisant ainsi ses efforts)

{% endmacro %}
<{ phantom_arkon_character_summary }/>


Le voleur {% symbol "Fédore Pass’muraille" for "thief_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_thief_character_summary() %}

- FANTÔME

- Traits : convoitise, roublardise, bagout, incrédulité, défiance, alcoolisme, vanité

- Histoire : 60 ans après que la malédiction se soit abattue sur la bibliothèque, il s’est infiltré dedans, espérant en piller les secrets ; en particulier le légendaire **trésor des Maupertuis**, et la mystérieuse **{% symbol "Source de Savoir" for "link_to_djinn_world" %}**. Il a ramassé au passage **uniquement le glaive** de l'arkonte. {% fact "arkon_bag_disappeared_just_after_his_death" %} Il a réussi à contourner la barrière magique bloquant l’accès au Domaine Interdit, grâce à un **{% symbol 'astrolabe de téléportation' for 'thief_teleportation_device_name' %}** (récupérable sur sa dépouille). Mais il s’est fait tuer par surprise par la Bête - toujours vivante à ce moment-là - qui gardait les lieux. {% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}

- Le voleur n’a initialement pas conscience qu’il est mort ; il se croit juste **piégé** dans sa petit zone (à proximité de la niche de la Bête) par les maîtres des lieux. Il interpelle donc les joueurs pour qu'on le **libére** de son ancrage, et qu'on l'aide à retrouver les équipements que quelqu'un lui a *odieusement* volés. Cela peut donner lieu à une négociation, donnant-donnant.

- Il continue à ne désirer que les richesses matérielles, qu'il ne peut hélas plus prendre en main malgré ses tentatives. Même si les joueurs font un “{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}” pour le convaincre qu'il est mort et que ses priorités sont illogiques, il est manifeste encore des doutes (peut-être ces personnes ont-elles une immunité contre les effets de ce serment ?).

- Suite aux harangues de l'arkonte, voire aux visites de l’Ankou, il finit par réaliser qu'il est mort. Mais cela ne change rien : après discussions avec les joueurs (certains ont des informations), il exulte que le **"{% symbol "Donjon des Pass’muraille" for "thief_castle_name" %}"** soit resté depuis toujours dans sa famille. Il se glorifie donc de pouvoir encore alimenter cet amoncellement de richesse, même une fois mort, via sa magique "{% symbol 'quêteuse sans fond' for 'thief_moneybox_name' %}". {% fact "arkon_and_ankou_try_to_persuade_thief_that_he_is_dead" %} {% fact "thief_heirs_still_benefit_from_his_treasure" %}

- Il monnaie chèrement ses informations sur les lieux aux autres explorateurs de cette bibliothèque, contre de l’or et des pierreries.

{% endmacro %}
<{ phantom_thief_character_summary }/>

L’Ankou (le guide des âmes, le “psychopompe”)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro god_ankou_character_summary() %}

- DIVIN (anciennement fantôme humain, mais promu par les dieux)

- Traits : exaspération, franc-parler, langage familier, sarcasme, bonne volonté,

- C’est un personnage sombre mais plutôt comique, ayant peu d’informations à apporter mais permettant de créer du dialogue avec les autres figurants, et de faire le lien avec des ancêtres défunts.

- Il ne passe que brièvement dans la bibliothèque en faisant sa tournée, puis peut être “invoqué” par les joueurs pour continuer à interagir.

- Il informe les joueurs que les fantômes sont anormalement **prisonniers** de ce lieu, et ne peuvent rejoindre l'au-delà ; et que les joueurs eux-mêmes sont, désormais, enfermés aussi.

- Il manie férocement l'ironie à froid, façon "pince-sans-rire" ; si par exemple un Parcival meurt, il lui redemande quelle était sa mission initiale (sauvez sa petite soeur malade), et s'il se sent satisfait du résultat.

- “Pourquoi vous flippez, là, les humains qui vous cachez derrière les rayons ! Vous croyez que je ne vous vois pas ? Je ne suis pas un psychopathe, vous devriez plutôt me remercier, sans moi vous auriez l’air fin pour rejoindre le royaume des morts ! Allez sortez, tant que vous ne venez pas me tripoter, vous n’avez rien à craindre de moi ! Comme si j’allais me rajouter du travail supplémentaire en butant des humains qui ne m’ont rien fait, dans ce lieu qui est déjà maudit ! Mais qu’est-ce que vous êtes venus faire ici d'ailleurs, comme si c’était pas déjà assez le boxon !”

- “J’ai l’air de quoi moi, aux réunions inter-spirituelles !? À chaque fois je me fais charrier, genre <alors cette affaire Maupertuis, ça avance toujours pas ?>. J’ai une réputation à tenir moi ! Des fantômes qui squattent un caveau pendant des siècles, ça fait tache ! Sans parler de la bestiole là-haut ! C’est contre l’ordre des choses, donc que chacun y mette du sien pour comprendre ce qui cloche !”

- Pendant la scène finale, en revanche, il se tait et laisse la solennité de l’évènement s’imposer ; mais il peut, tout à la fin, lancer un “Hé les gars on se dépêche maintenant, j'ai un groupe de touristes kéroskiens qui vient d’aller caresser des requins-sabres, donc j’ai pas fini ma journée !”

{% endmacro %}
<{ god_ankou_character_summary }/>

La Bête (la goule gardienne du Domaine Interdit)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro phantom_beast_character_summary() %}

- FANTÔME (anciennement une "goule des cavernes", enchantée par les Maupertuis pour ne pas avoir besoin de se nourrir)

- Traits : agressive, sournoise, non-communiquante

- Engagée par les parents d’Octave pour garder les grimoires les plus dangereux, dans le Domaine interdit

- Le sceau protégeant le Domaine Interdit l'empêchait elle-même de venir dans la zone autorisée de la bibliothèque

- Ne reconnaît personne comme ami (seuls les parents d’Octave et Mérédice avaient pouvoir sur elle, ni le précepteur ni Octave n’auraient été épargnés s’ils avaient pénétré dans le domaine interdit)

- Morte de vieillesse plus d'un siècle après la malédiction de la bibliothèque, et devenue encore plus féroce à force d’errer sans but dans le domaine interdit

- A une véritable **addiction** pour les {% symbol "pierres de lune" for "phosphorescent_pebbles_name" %} (galets phosphorescents) {% fact "beast_is_addicted_to_moon_stones" %}

- Son espèce et ses caractéristiques doivent rester un peu mystèrieuses pour les joueurs, afin d’augmenter l’angoisse, et de les forcer à réagir vite pour trouver des solutions, lorsqu’elle apparaît.

- **Les parents Maupertuis, interrogés depuis l’au-delà, peuvent donner des indications sur comment la neutraliser**

{% endmacro %}
<{ phantom_beast_character_summary }/>

Le druide {% symbol "Diviciacos" for "druid_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_druid_character_summary() %}

- HEROS DE ROMAN (titre “{% symbol "Les sorciers du chaos" for "druid_novel_name" %}”, en {% symbol "3" for "druid_novel_volumes" %} Tomes)

- Traits : doux, discret, érudit, ami des plantes et des bêtes

- A construit un petit coin “jungle” avec les plantes du lieu, où il enseignait à l’enfant l’harmonie avec la nature

- C’est lui le “vrai méchant”

- Dans les 2 premiers tomes de son roman, il parcourt le monde pour défaire les sombres magiciens qui contrôlent chaque continent. Mais dans le 3e tome, après avoir tué le dernier sorcier, il révèle sa vraie nature et devient le Guide de Gaïa, qui soumet la planète à une utopie brutale de “Retour à la Nature”.

- Il est très habile, a des pouvoirs magiques, résiste à la magie et aux poisons (ainsi qu’au sacré bien sûr), et régénère très vite son corps en cas de blessure.

- Il peut utiliser son **sang bleu comme la mer**, avec l'aide des esprits de la Nature, pour soigner tous types de maux biologiques (il doit simuler qu'il s'entaille l'avant-bras pour soigner). {% fact "druid_can_well_heal_biological_injuries_with_his_blue_blood" %} {% hint "blue_blood_for_druid_healings" is needed %}

{# NOPE - **S’y connait en NECROMANCIE?** #}

{% endmacro %}
<{ avatar_druid_character_summary }/>

L’inventeur {% symbol "Sir Jacques Vaucanson" for "inventor_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_inventor_character_summary() %}

- HEROS DE ROMAN (titre “{% symbol "Le ballet des automates" for "avatar_inventor_novel_name" %}”, en 1 seul Tome)

- Traits : extraversion, bonnes manières, langage châtié, dynamisme

- A conçu les automates de la bibliothèque

- Il peut bricoler une prothèse mécanique pour remplacer un membre perdu {% fact "inventor_can_well_heal_missing_limbs" %}

{% endmacro %}
<{ avatar_inventor_character_summary }/>

La duchesse {% symbol "Cassiopée de Thiersonne" for "duchess_name" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro avatar_duchess_character_summary() %}

- HEROINE DE ROMAN (titre "{% symbol "Les cygnes d'étang" for "avatar_duchess_novel_name" %}", en 1 seul Tome)

- Traits : distinguée, sensible, pieuse, protectrice, entreprenante

- Est capable d'entrer en synergie avec d'autres "voyants"

- Elle peut invoquer ses propres dieux, avec l'aide des {% symbol "initiés" for "ritualist_kind_name" %} présents, pour guérir une blessure sacrée {% fact "duchess_can_well_heal_sacred_injuries" %}

{% endmacro %}
<{ avatar_duchess_character_summary }/>


Lieux
=====

Etage du bas (bibliothèque normale)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Le coin de l’archiviste (face à l’escalier)

- Le coin de l’enfant

- Le coin de l’arkonte

- La mini-jungle que le druide et l’enfant avaient créée

- Le buffet dinatoire magique des 4 mondes

- Le pentacle du rituel inachevé de l’arkonte.

- Le cimetière (tombes rudimentaires de l’enfant, de l’archiviste et de l’arkonte)

- Différents coffres et objets répartis dans les lieux, ainsi que des “marqueurs” mis au sol par les avatars lors de leurs investigations infructueuses

Etage du haut (domaine interdit)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*Accès initialement bloqué pour tous.*

- Le coin du voleur

- La niche de la Bête

- Le coffre avec le {% symbol "Thanatologue" for "book_of_the_dead" %}

- L’atelier d’alchimie

- L’atelier de gemmologie

- Différents pièges et artefacts répartis entre les rayonnages


.. raw:: pdf

   PageBreak


Déroulement du jeu
##########################################

Dangers et blessures
==========================

Les différents types de blessures
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro injury_types_knowledge() %}

Les agressions qu'un aventurier malchanceux est susceptible de subir se classent en trois catégories : **attaques physiques, magiques et sacrées**.

Les attaques physiques (armes tranchantes, contondantes, perçantes, toxiques...), et les attaques magiques (sortilèges de feu, de glace, ou autres, mais aussi blessures résultant d'objets magiquement envoûtés...) doivent être parées avec des moyens différents, mais les blessures résultantes sont d'une même nature : **biologique**. Les mêmes soins médicaux, les mêmes potions, peuvent donc secourir les victimes de ces maux.  {% fact "cursed_objects_give_magic_and_not_spiritual_injuries" %}

En revanche, les attaques sacrées, typiquement issues de contacts avec des fantômes ou démons, ou avec leurs dépouilles maudites, causent des blessures de nature **spirituelle**. Quoique les symptômes soient proches de maux biologiques (tétanie, cécité, membre inutilisable...), seules les interventions de mystiques peuvent réparer promptement les dommages infligés à l'âme. Les potions aussi peuvent être utiles dans ce cas, mais uniquement en fournissant aux célébrants davantage d'énergie et de concentration pour la réalisation de leur rituel de bénédiction. {% fact "potions_cannot_heal_spiritual_injuries" %} {% fact "cursed_skull_and_bones_give_sacred_injuries" %}

La distinction entre ces différents types de blessures n'est pas toujours évidente ; par exemple, la paralysie d'un membre peut être due à des lésions internes tout comme à l'attaque d'un spectre. D'où la nécessité d'investiguer les circonstances ayant mené aux troubles constatés, afin de fournir un remède approprié.

Un point d'attention : de même que les blessures "biologiques", même soignées, laissent des séquelles dans le corps, de même les blessures "spirituelles" fragilisent les fondements de l'âme.

**Subir deux blessures d'affilée, de quelques natures que ce soit, mène donc presque certainement à la mort.** {% fact "second_injury_sustained_is_always_fatal" %}

{% endmacro %}
<{ injury_types_knowledge }/>

Concrètement : les cas possibles durant le jeu
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro injury_cases_and_remedies() %}

Un joueur peut être atteint dans les cas suivants :

- S’il se fait toucher par un fantôme en phase désincarnée (en errance spectrale) : **blessure sacrée**. S'il se fait attaquer durablement par la Bête fantôme, ou fait obstacle à un fantôme au lieu de s'enfuir, cela finit par le tuer. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

- S’il touche un objet maudit, comme un crâne sonore ou les ossements qui sont avec {% fact "cursed_skull_and_bones_give_sacred_injuries" %} : **blessure biologique**. Un pentacle, lui, n'est PAS dangereux, hormis durant un rituel. {% fact "pentacle_is_not_harmful_oustide_rituals" %}

- S’il déclenche un piège physique ou magique, c'est-à-dire fait tomber un **grelot** par terre (ex. fil tendu dans une allée) ou déclenche le cri d'une **cigale** à détecteur de présence (ex. en ouvrant un coffre) : **blessure biologique**.
 {% fact "cicada_or_minibell_sound_mean_injury" %}

- S'il pénètre dans le tombeau du {% symbol "Mage Mos Peratys" for "maupertuis_dynasty_founder" %} sans être un héritier Parcival, et se fait toucher par la momie du mage : **mort**. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

- S'il boit une potion dangereuse, ou reçoit un sortilège ennemi etc. : **blessure biologique**.

**Les blessures se traduisent par un malus à la discrétion du MJ, suivant la situation : perdre un membre ou juste son usage, devenir muet, perdre la mémoire, devenir essoufflé et ne plus pouvoir courir (en cas d'empoisonnement), ou ne plus pouvoir utiliser certaines compétences...**

**IMPORTANT : une deuxième blessure, de même nature ou non, subie durant le jeu, tue le joueur.** {% fact "second_injury_sustained_is_always_fatal" %}

{# NOPE
Les joueurs sont censés chercher entre eux les moyens de se soigner, grâce aux potions magiques et aux rituels des diacres, mais ces possibilités restent très limitées.
#}

Les joueurs sont par eux-mêmes très démunis face aux diverses blessures, ils n'ont PAS de compétences en ce sens. {% fact "players_have_no_medecine_abilites" %}

**Guérisons par des avatars** : Les blessures peuvent, en fonction de leur type, être guéries par certains des avatars présents. Les avatars doivent d'abord laisser le joueur avec ses blessures pendant quelques minutes, le temps de "rassembler ce qu'il faut pour le soigner". Puis ils procèdent à une opération ou un rituel - **à inventer pour l'occasion**.

{# NOPE FORGET THAT FOR NOW
mais attention ces interventions ont **1 chance sur 6 d'échouer dramatiquement** (menant alors à la mort du joueur - tirer cela au dé avec le maître de jeu){ % fact "avatar_abilities_are_randomly_hazardous" % }.
#}

- La **duchesse** peut invoquer ses propres dieux, avec l'aide des {% symbol "initiés" for "ritualist_kind_name" %} présents, pour réparer une blessure sacrée (touchant l'âme). {% fact "duchess_can_well_heal_sacred_injuries" %}
- Le **druide** peut utiliser son **sang bleu comme la mer**, avec l'aide des esprits de la Nature, pour soigner tous types de maux biologiques. {% fact "druid_can_well_heal_biological_injuries_with_his_blue_blood" %} {% hint "blue_blood_for_druid_healings" is needed %}
- L'\ **inventeur** peut bricoler une prothèse mécanique pour remplacer un membre perdu. {% fact "inventor_can_well_heal_missing_limbs" %}

**Si un joueur meurt, il devient un fantôme** ; il est cependant constamment incarné, et immédiatement libre de ses mouvements, contrairement aux fantômes figurants. Il reste cependant soumis aux mêmes barrières que l'ensemble des protagonistes ({% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %} encerclant la bibliothèque, {% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %} bloquant l'accès au domaine interdit...). Il ne peut plus manipuler d’objets (pas même une tablette tactile de compétences), mais il garde ses connaissances acquises. Son statut de fantôme lui permet d'accéder sans problème aux corridors piégés et autres lieux dangereux pour les vivants.

Avec le bon rituel du grimoire {% symbol "Thanatologue" for "book_of_the_dead" %}, il est possible de **ressusciter un joueur** à l’état de **zombie** pour quelques heures ; le joueur retrouve alors toutes ses capacités, mais il doit adopter une posture et un langage de "zombie à l’ancienne” (ex. il parle bizarrement, peut marcher en titubant, mais ne peut pas courir...). {% fact "players_have_thanatologue_spell_to_summon_zombies" %}

{% endmacro %}
<{ injury_cases_and_remedies }/>


Événements rythmant le jeu
==========================

{% macro early_game_events() %}

Briefings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Avant le jeu, des briefings par groupe puis collectif ont lieu avec les joueurs.
*Voir la fiche de planning détaillé, à ce sujet.*


L’entrée en scène des joueurs
++++++++++++++++++++++++++++++++++

Un discours du maître de jeu introduit le début du jeu.

Chaque groupe est ensuite amené, par un automate, dans un endroit différent de l’étage du bas de la bibliothèque, avec une musique introductive.

Pour rappel, la bibliothèque a aujourd'hui sa fête annuelle, comme chaque année depuis 1000 ans. Les automates (autrefois conçus par l'inventeur et Octave) commencent à s'activer pour organiser cette fête ; certains peuvent être initialement "désactivés", assis ou au sol, en attendant que l'avatar Inventeur ne les allume.

Les fantômes se déplacent à ce moment tous sous leur forme désincarnée.

Certains avatars peuvent déjà être présents (par exemple la duchesse en prière au cimetière, le druide dans sa mini-jungle, l'inventeur réparant un automate), dans l'attente de l'ouverture du buffet.


L’ouverture du buffet d'outre-monde
++++++++++++++++++++++++++++++++++++++++++++

Une musique entraînante se déclenche, et l’inventeur vient au banquet, appelant à grands cris ses amis du monde imaginaire à le rejoindre pour porter un toast à Octave et l'archiviste, et espérer ensemble la levée de la malédiction.

Les autres avatars convergent, les joueurs qui étaient proches se font haranguer aussi, et sont entrainés dans ce mélange de déclamations diverses et de mouvements de danse, en ouverture du banquet.

Les mets du buffet sont supposés être automatiquement produits par la table enchantée. Optionnellement, s'il n'est pas déjà visible, on peut faire apparaître le buffet garni par une formule magique simple, que les avatars connaissent. {% fact "buffet_table_magically_generates_food" %}

Une fois la musique finie, joueurs et héros font plus ample connaissance autour du buffet. Il est assumé que, à dessein, ces mets magiques sont aussi accessibles aux fantômes (incarnés ou non).


La première incarnation des fantômes
++++++++++++++++++++++++++++++++++++++++++++++++

Après un moment, le gong résonne ; le précepteur-archiviste s’incarne, et appelle les joueurs à venir à lui. Ils se montre ravi d’avoir de la visite dans ces lieux - et peut-être avec eux un espoir de résolution de la malédiction. Il répond aux questions des joueurs, et **teste leurs bonnes intentions** avec le "{% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}". Il leur (re)signale la présence du buffet, qui pour lui s'est **"activé tout seul"** (car il ne voit pas les avatars), en cette date anniversaire du drame, comme tous les 100 ans

Les autres fantômes s'incarnent aussi (de préférence un peu après), chacun à son point d'attache plus loin du banquet.


La frénésie de la clochette spectrale
+++++++++++++++++++++++++++++++++++++++++++

Un joueur sonnera probablement la clochette de service, par curiosité, en début de jeu ; en tant que fantôme, il faudra réagir conformément à la description de cet artefact mystique, en passant en mode "{% symbol "frénésie spectrale" for "phantom_frenzy_name" %}", y compris si l'on est déjà en errance normale.

{% endmacro %}
<{ early_game_events }/>


{% macro ankou_introduction_event() %}


Le passage de l'Ankou dans la bibliothèque
++++++++++++++++++++++++++++++++++++++++++++++++++

L'Ankou arrive par les escaliers, et interpelle les joueurs sur le fait qu’ils n’ont rien à faire ici, qu’il n’est pas “la Bête”, qu’il ne leur veut pas de mal, puis finalement qu’il compte sur eux pour l'aider à résoudre le problème de ces âmes prisonnières des lieux. Il s'enquiert de la présence de sa clochette spectrale, qui doit déjà avoir été dérobée par le méchant. Puis il repart.

{% endmacro %}
<{ ankou_introduction_event }/>

*Les joueurs peuvent par la suite envoyer des questions à l'Ankou à l'adresse des défunts Maupertuis, mais attention, ceux-ci ne se souviennent pas de tout non plus.* {% fact "diakon_invoker_can_message_ankou" %}


La folie meutrière de l'automate de garde
+++++++++++++++++++++++++++++++++++++++++++

{% macro automaton_sentinel_instructions() %}

{% fact "druid_turns_automaton_sentinel_into_prophet_killer" %}

Dès le début de l'aventure, cet automate patrouille bien "mécaniquement" avec une carabine Nerf, et interpelle les joueurs qu'il croise. Il les somme de décliner leur identité, et de jurer (par Zarathoustra) qu'ils n'ont aucune intention de s'en prendre à la lignée des Maupertuis. Puis il continue sa ronde, en ignorant désormais les joueurs ainsi contrôlés. {% hint 'nerf_gun_for_guard_automaton' is needed %}

Plus tard, peu après l'ouverture du Domaine Interdit le druide se sent menacé par les différentes prophéties qui le désignent peu à peu. Il prend donc le contrôle de l'automate de garde, par des champignons/lianes s'infiltrant dans le système central de ladite machine (cela est matérialisé en jeu, par exemple, par de faux végétaux autour de son cou ou derrière son masque).
{% hint "plants_around_head_of_automaton_hitman" is needed %}

Le druide envoie l'automate de garde pour **assassiner** (par une balle dans le torse) deux personnes :

- **La joueuse Oracle**, qui reçoit les visions
- **La figurante Duchesse**, qui l'aide à cela

L'automate tueur cherche à effrayer, ou à la rigueur blesser aux jambes, les autres protagonistes, mais pas plus ; car le druide compte sur eux pour supprimer la malédiction de la bibliothèque. Il se montre donc particulièrement prudent envers les précieux diacres.

L'automate ne peut pas récupérer ses balles, qui se désagrègent naturellement à l'impact.
*Ces balles nerf doivent avoir une couleur différente des "fléchettes" des Parcival ; veiller à ce que des joueurs n'en récupèrent pas, car cela n'aurait pas de sens en jeu.* {% fact "nerf_bullets_and_arrows_need_different_colors" %}

Il ne vise évidemment **jamais la tête** des participants, par sécurité.

Face à cet automate :

- Tous les protagonistes sont vulnérables
- Le Gardien des Bois est protégé, au torse seulement, par l'armure de l'arkonte ; ses fléchettes d'{% symbol "Iridium" for "parcival_woodsman_arrows_metal" %} peuvent légèrement handicaper l'automate tueur, mais guère plus, hormis un coup parfait en plein coeur, qui serait fatal ; il a déjà entendu parler de ce genre de chimères mécaniques. {% fact "parcival_woodsman_knows_about_parasited_automatons" %}
- Aller à l'empoignade est proscrit par sécurité, mais serait de toute façon suicidaire étant donnée la force physique des automates.
- Les sortilèges des diacres sont en théorie inutilisables, car l'automate bouge trop, par exemple, pour être mis en stase dans un pentacle.
- Si un protagoniste possède le {% symbol 'Dominion' for 'androids_command_bracelet_name' %}', le bracelet de commandement des automates, il peut donner des ordres à l'automate tueur, et ainsi créer un conflit qui va le confondre et le ralentir (car le robot oscillera entre l'ordre de tuer, et celui de ne pas le faire).
- Les meilleures armes pour détruire l'automate tueur sont le {% symbol "glaive" for "arkon_weapon_name" %} ULTRA-LOURD de l'arkonte, et les explosifs.

{% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}
{% hint "2_explosives_for_minesweeper" is needed %}

Une fois que l'automate tueur a été neutralisé, ou (en pire cas) n'a plus de balles et s'autodétruit, les joueurs peuvent récolter dessus les indices de son étrange contamination.
{% hint "plants_around_head_of_automaton_hitman" is needed %}

Si le druide est appelé pour soigner une des deux cibles de l'automate, il sera naturellement **réticent** à le faire ; mais il devra alors choisir entre faire profil bas et soigner avec son talent habituel, ou échouer volontairement dans ses soins, et tenter alors de le justifier pour ne pas éveiller trop de soupçons.

{% endmacro %}
<{ automaton_sentinel_instructions }/>


L'exploration du tombeau du mage fondateur
++++++++++++++++++++++++++++++++++++++++++++++++

{% macro magus_zombie_instructions() %}

Les joueurs doivent trouver le moyen de se téléporter dans le tombeau du {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %}, en contournant ainsi les sceaux maléfiques qui protègent son entrée, pour y prendre des artefacts magiques.

Le cadavre du mage git allongé là, dans l'aube papale dorée.

Si un non-Parcival fait partie du groupe des téléportés (voir leurs habits de reconnaissance), cela déclenche une malédiction : la momie du mage se lève, et pourchasse (en marchant lentement, comme un zombie) l'intrus, qui doit l'esquiver jusqu'à ce que le téléporteur lui permette de sortir, sous peine de mourir. La momie retourne ensuite à sa place. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %} {% fact "phantoms_are_persistent_but_zombies_are_transient" %}

Lorsqu'il n'y pas de non-Parcival dans le tombeau, la momie ne bouge absolument pas, mais sa simple présence suffit à stresser les joueurs, tandis qu'ils lui piquent ses ornements légendaires.

{% endmacro %}
<{ magus_zombie_instructions }/>


La bataille finale
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Voir la quête `Démasquer et neutraliser le méchant`_ pour un aperçu des déroulements possibles de cet épisode final.


L’épilogue musical
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Faire éteindre aux joueurs leurs lanternes, pour augmenter l’ambiance.
Une bande-son est jouée, pour une scène assez chorégraphiée.

L’Ankou appelle les fantômes enfin libérés à le rejoindre.

Ils ont chacun mis des petites ailes dans le dos : plumes pour l'arkonte, diodes pour l'archiviste, steampunk pour Octave.

Octave est ravi de retrouver bientôt sa famille, mais se retourne pour distribuer des remerciements, conseils et adieux à chaque groupe de joueurs, avant de partir en courant.

L’archiviste et l’arkonte le suivent avec solennité.

La Bête peut potentiellement reparaître juste pour s'échapper elle aussi, de façon comique, de même que le voleur.

Les automates guident ensuite les joueurs vers la sortie de la bibliothèque, avant que les portails de transplanage ne se referment jusqu'au prochain {% symbol "solstice d'hiver" for "astral_opening_date" %}.

Selon que les groupes de joueurs ont, ou non, pris l'engagement auprès de l'arkonte de protéger/détruire les portails menant à ce lieu, **cette bibliothèque subsistera, ou s'autodétruira dan le magma**, faute de lien magique avec la surface (elle a besoin de 2 des liens sur les 4 pour ne pas s'effondrer). {% fact "arkon_questions_groups_about_the future_of_maupertuis_archives" %}


Planification des prophéties et intuitions
+++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro planning_of_prophecies() %}

**Donner à l'oracle uniquement le contenu en italique, pas le titre ou le contexte de ces prophéties.**

- **Intuition initiale sur les aventuriers** (à la fin de l'introduction commune) : Cette intuition, sur la nécessité de rester solidaires entre joueurs, est déjà dans la fiche de personnage de l'Oracle. {% fact "parcival_oracle_has_initial_intuition_about_adventurers_solidarity" %}

- **Intuition sur la Bête et le Mage** (lors de la première rencontre de l'oracle avec la duchesse) : *"Vous sentez de multiples présences errantes. L'une d'elles est remplie d'incompréhension et de haine. Vous sentez aussi une vieille ancienne endormie, à la fois fière et vengeresse, qui semble vous appeler."*

- **Prophétie des livres jumeaux du père Maupertuis** (plume dans le coffre commun des Maupertuis) : Vision simple, musique "One Last Stand". {% hint 'feather_in_common_family_chest' is needed %}

- **Intuition sur le domaine interdit** (lorsque les joueurs entrent dans l'étage interdit) : *"Vous sentez se déverser sur vous le poids de siècles, de millénaires de connaissances qui sont sources de vie, mais aussi parfois de mort. Cependant, vous le sentez, le Mal est bien plus ancré dans l'étage autorisé, qu'il ne l'est dans l'étage interdit."*

- **Prophétie sur le moulin générateur de richesses** (plume sur le tableau avec stéréogramme de moulin près des portraits) : Vision simple, musique "Here and Now (Seed's Theme)". {% hint 'feather_on_stereogram_board' is needed %}

- **Prophétie de la bague Amplificans anti-zombies** (plume dans le Thanatologue) : Prophétie AUDIO, musique "The Calling". ATTENTION à bien garder la bande-son de l'oreillette de l'Oracle, et la musique pour le public, en SYNCHRONISATION. {% hint 'feather_in_thanatologue' is needed %} Si le joueur Oracle ne se sent pas capable de gérer cette prophétie audio, repasser sur une simple vision, avec l'image.

- **Prophétie du 3e Tome égaré du druide** (plume dans la sacoche de l'arkonte déposée par le méchant) : Vision simple, musique "Broken Truth light (Delphi's Theme)". {% hint 'feather_in_arkon_bag' is needed %}

- **Prophétie du crâne de l’arkonte et du danger planétaire** (allumage de la fontaine d'encens) : Vision partielle en DUO avec la duchesse, musique "Broken Truth heavy (Delphi's Theme)".

- **Intuition sur la dernière bataille** (peu après que le méchant est démasqué, mais UNIQUEMENT si la prophétie holographique de Cassandra n'a pas été déclenchée via les portraits lenticulaires effrayants) : *"Vous sentez que les vivants présents sont comme des fourmis qui se tiennent face à un taureau ; mais que si toutes les fourmis joignent leurs efforts, elles peuvent bâtir de quoi détruire leur ennemie. Attention cependant, dans les derniers instants d'une lutte, les meilleurs amis peuvent devenir les pires adversaires, même à leur insu."* {% fact "parcival_oracle_has_fallback_intuition_about_last_battle" %}

{% endmacro %}
<{ planning_of_prophecies }/>


Quêtes et parcours d’énigmes
============================

{#
AUTRE IDEES DE COMPETENCES ET ENIGMES

- Mettre des énigmes textuelles pour trouver des mots (voir Enigma Battle sur le forum du Clivra)
- Survie ? Microfilms ? QR Codes ? Appel au central des connaissances ?
- Restaurateur de textes effacés (ou ça fait doublon) ? + kit d’analyse gemmologique (bof) ?
- Différents coffrets et livres assez caractéristiques sont disséminés parmi les livres normaux de la bibliothèque, il faut les trouver puis pour chacun trouver la clé ou le code correspondant. A PRECISER

#}

Accéder au domaine interdit (utile à tous)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Un sceau est visible devant les escaliers menant à l'étage interdit. Lorsqu'il est activé, un grimoire apparait ; il montre des carrés retournables sur un panneau (ou une application sur tablette tactile), {% hint "symbolic_enigma_puzzle_app" is needed %} qui permettent de créer différentes combinaisons de bouts de symboles ; il faut trouver le bon motif entier pour ouvrir le passage.

- Les figurants indiquent qu'il faut le symbole secret de la famille Maupertuis pour pouvoir ouvrir le passage. {% fact "secret_family_symbol_needed_for_forbidden_zone" %} {% fact "npcs_know_about_secret_family_symbol_system" %}

- Octave a quelques souvenirs de ce système, même s’il n’avait pas encore reçu le symbole secret de sa famille, et n’était jamais allé seul dans le domaine interdit (la Bête l'aurait d'ailleurs attaqué dans ce cas). {% fact "octave_would_have_been_attacked_by_beast_if_alone_in_forbidden_domain" %}

- Le symbole de la famille est en **message UV** dans un livret “Généalogie des Maupertuis”, {% hint "genealogy_book_with_uv_family_symbol" is needed %} qui est dissimulé dans la mallette administrative de la famille. Octave et l'archiviste avaient entendu parler de cela. {% hint "family_briefcase_protected_by_code" is needed %} {% fact "octave_and_archivist_know_about_secret_family_symbol_in_family_briefcase" %}
  Cette mallette est protégée par le code {% symbol "625-993" for "family_briefcase_code" %}, qui est "murmuré" par le livre factice "{% symbol "Venture Prins" for "small_wooden_fake_book_name" %}". {% hint "family_briefcase_code_spoken_by_venture_prins_fake_book" is needed %}

- Octave et l'archiviste connaissent bien ce livre factice, et ont même, grâce au code obtenu, fouillé la mallette administrative (dangereuse car piégée) par le passé. Mais en vain, hélas. {% fact "octave_and_archivist_have_searched_family_briefcase" %} {% fact "octave_and_archivist_know_about_trap_of_family_briefcase" %}

- Tous deux se souviennent où ils ont laissé le "{% symbol "Venture Prins" for "small_wooden_fake_book_name" %}" ; ils indiquent le rayon concerné aux joueurs qui le demandent, et le livre s'y trouve bien. {% fact "octave_and_archivist_know_about_venture_prins_book_location" %}
  Il peut falloir un stéthoscope, voire l'aide d'un automate, pour entendre le code diffusé dans le bois du livre, et ainsi ouvrir la mallette des Maupertuis.

- Le code de la mallette administrative peut aussi être demandé aux parents défunts, plus tard, via l’Ankou, en pire cas.

Une fois le symbole de la famille reproduit sur le grimoire, un son puissant se fait entendre, et le passage vers le domaine interdit est libre pour passer dans les deux sens.


Neutraliser la Bête des Maupertuis (utile à tous)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Lors de la malédiction de la bibliothèque, la Bête qui gardait le domaine interdit y a été piégée, même une fois morte de vieillesse. Devenue fantomatique et aigrie, elle est plus dangereuse que jamais.

La Bête attaque toute créature vivante et ses attaques (au corps à corps mais “sacrées”) sont rapidement handicapantes puis létales. Elle ne peut voir les personnages des livres, et ignore majoritairement les fantômes, un peu comme une chienne effarouchée. {% fact "beast_ignores_or_fears_other_phantoms" %}

Une fois que l’accès au domaine interdit (habituellement protégé par un puissant {% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %}) est ouvert, la Bête est libre d’en sortir, et de faire irruption parmi les joueurs, si ceux-ci ne prennent pas les devants. Octave et l'archiviste les encouragent donc à planifier de quoi la mettre hors d’état de nuir durablement. {% fact "octave_and_archivist_warn_players_about_beast_dangerousness" %}

Pour neutraliser la Bête :

- La Bête détecte les vivants qui se trouvent à moins de 3m, mais voit très mal au-delà. Il est donc possible de se promener dans le domaine interdit en l’évitant soigneusement, mais cela reste très dangereux.
   {% fact "characters_know_how_the_beast_works_regarding_3m_sight" %}

- L’arkonte avait une {% symbol "armure de Mithril" for "arkon_armor_name" %} protégeant intégralement le porteur des attaques “sacrées”, c'est-à-dire celles des créatures appartenant au royaume des morts. Les joueurs peuvent la trouver au cimetière, et le **plus costaud** de tous peut la revêtir, pour tenir tête aux attaques de la Bête. {% hint "arkon_sacred_armor" is needed %}

- **L’exorciste** peut faire fuir la Bête pendant quelque temps avec une de ses incantations, ou au contraire l'attirer à lui à rythme lent. {% fact "diakon_exorcist_can_chase_away_beast_temporarily" %} {% fact "diakon_exorcist_can_attract_slowed_beast_temporarily" %}

- L’un des Parcival a des balles qui peuvent être **rendues sacrées par l’exorciste**, et donc capables de “tuer” la Bête fantomatique (c'est-à-dire la retransformer en spectre errant aléatoirement). Mais à cause de la malédiction qui clôture la bibliothèque, la Bête reviendrait forcément dans ce cas un peu plus tard, encore plus féroce. {% fact "diakon_exorcist_can_bless_parcival_woodsman_arrows" %}

- La Bête avait pour friandises favorites des {% symbol "pierres de lune" for "phosphorescent_pebbles_name" %} ; même s'il ne peut plus les manger, il se jette dessus quand il en croise. {% hint "beast_snack_as_moon_stones" is needed %} {% fact "beast_is_addicted_to_moon_stones" %}

- **L’invocateur** connait un rituel capable de “geler” pour plusieurs jours une entité du monde des morts. Il lui faut tracer le bon pentacle, et s’assurer que la Bête soit attirée dessus. Une fois cela fait, les joueurs en sont débarrassés jusqu’à la fin du jeu. {% fact "diakon_invoker_can_freeze_beast_for_days" %}

{# NOT YET - murs amovibles pourraient être déplacés pour encager la Bête #}
{# NOPE - **L'alchimiste** peut trouver une potion capable de réaliser un {% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %} pendant une journée sur u #}




Le remède contre la dégénérescence marbrée (famille Parcival)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro parcival_group_main_quest() %}

**Les Parcival ont pour principal objectif de trouver un remède contre la maladie de leur petite soeur {% symbol "Philomène" for "parcival_sick_child_name" %}, la {% symbol "dégénérescence marbrée" for "legacy_disease" %}, car leur ancêtre Mérédice de Maupertuis en avait été guérie ici.**

- L'archiviste se souvient très bien de la maladie de Mérédice de Maupertuis, et comment les parents Maupertuis l'avaient envoyé en personne quérir différents ingrédients très pointus pour créer un {% symbol "Cocktail de Réjuvénation" for "parcival_disease_main_remedy_name" %}. Chance, il avait retrouvé et rangé à sa place, lors de l'inventaire, la recette de ce cocktail, et l'indique aux joueurs (elle est dans l'étage autorisé). {% fact "archivist_knows_about_meredice_rejuvenation_cocktail_recipe_location" %}

- Le {% symbol "Cocktail de Réjuvénation" for "parcival_disease_main_remedy_name" %} demande de mélanger trois potions : l'Elixir Flexifiant (inoffensif), la Lotion de Clairvoyance (inoffensive), et la Teinture Pyrolitis (dangereuse). {% hint "recipe_rejuvenation_cocktail" is needed %}

- Les deux premières potions ont leurs recettes à l'étage autorisé ; l'archiviste les avait croisées, et avait marqué leur emplacement avec des **flèches blanches tracées au sol**, grâce à une peinture phosphorescente trouvée sur place. {% hint "recipe_flex_elixir" is needed %} {% hint "recipe_clarity_lotion" is needed %} {% hint "white_arrows_on_floor_towards_cure_recipes" is needed %} {% fact "archivist_has_marked_locations_of_rejuvenation_cocktail_subrecipes" %}

- Ces deux premières potions ne font appel qu'à des ingrédients facilement accessibles dans le pays de la famille Parcival, elles n’ont donc pas besoin d’être réalisées sur place. Mais il faut l’aide du **druide** pour reconnaître les noms désuets qui désignent certains ingrédients, dans ces recettes (ou bien interroger les parents Maupertuis depuis l’au-delà). {% fact "druid_known_about_plants_and_gems" %} {% fact "parcival_alchemist_has_all_ingredients_for_flex_elixir_recipe" %} {% fact "parcival_alchemist_has_all_ingredients_for_clarity_lotion_recipe" %}

- La dernière potion, la Teinture Pyrolitis, qui peut aussi servir à des maléfices, a sa recette dans le **domaine interdit**, qu'il faut donc d'abord débloquer. Un **{% symbol "grimoire traceur" for "frequency_scanner_book_name" %}** (une application mobile de scanner de balises bluetooth), trouvable sur place, est utilisé pour localiser les recettes dont on connait le nom, dans cet étrange endroit (en plus, optionnellement, des étiquettes sur les rayonnages). L'alchimiste en a entendu parler. {% hint "radio_frequency_scanner_app_in_chest" is needed %} {% fact "parcival_alchemist_knows_about_frequency_scanner_book" %} {% hint "forbidden_zone_optional_labels_showing_tincture_shelf" is needed %} {% hint "recipe_pyrolitis_tincture" is needed %}

Mais les ingrédients et le mode de préparation de cette teinture sont très complexes, il faut donc profiter de ce qui avait déjà été rassemblé par la famille Maupertuis.

- Un ingrédient de la Teinture est en évidence à l’étage autorisé ; un autre en évidence sur l'établi de gemmologie ; un autre sur l'établi d'alchimie dans le domaine interdit (mais protégé par un cadenas à crocheter) ; le dernier dans un **corridor toxique** de l’étage interdit (c'est une protection supplémentaire du lieu). {% fact "one_corridor_is_toxic" %} {# Hint tags for this are in the clues document #}
  Se promener dans ce dernier corridor, c'est la mort assurée. Pour récupérer l'ingrédient concerné, il faut soit avoir récupéré le collier anti-poison ailleurs, soit avoir reçu le contrôle d'un automate et l'envoyer chercher cet ingrédient (ou juste demander à l'inventeur d'agir). {% hint "androids_command_silver_white_ribbon_bracelet_for_inventor" is needed %}

- Enfin, il faut un récipient métallique avec **enchantement anti-explosion**, qui se trouve dans les outils d’alchimie (sous forme d’un chaudronnet cylindrique en cuivre avec anse). {% hint "enchanted_copper_cauldron_on_alchemy_table" is needed %}

- Une fois tous les ingrédients rassemblés (pas besoin de préparer effectivement les potions), la famille a réussi cette mission, à condition qu’elle puisse quitter les lieux.

{% endmacro %}
<{ parcival_group_main_quest }/>


Le trésor des Maupertuis (agents secrets mirandiens)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro spy_group_main_quest() %}

**Les agents secrets mirandiens ont pour principal objectif de trouver le trésor, la source de richesse des Maupertuis, pour sauver leur petit pays de la faillite.**

Ils ont retrouvé un morceau du journal de Mérédice, où elle décrit en langage énigmatique comment lorsqu'un grimoire se met à chanter, grâce à des symboles changeants, quelque chose tourne et les richesses apparaissent. {% hint "meredice_diary_about_treasure_for_spy_group" is needed %}

Un oracle déclenché dans le domaine interdit montre un moulin à aube déversant des richesses dans le fleuve, entouré de notes de musiques. {% hint "parcival_oracle_vision_about_water_mill" is needed %}
Un stéréogramme au mur montre par ailleurs un moulin à café avec un double mot caché de remerciement {% hint "grinding_mill_stereogram_picture_with_magnetic_and_uv_code" is needed %}.

Les joueurs doivent comprendre qu’il s’agit d’un **moulin à café** simplement “caché à la vue de tous”, sur l’établi d’alchimiste de l’étage interdit. {% hint "grinding_mill_with_enchantment" is needed %}

Ce moulin, capable de générer des pierres précieuses à partir de rien, nécessite en réalité un chant issu d'un grimoire magique, pour fonctionner.
Optionnellement, il faut activer un sceau dans l'étage interdit pour faire apparaître ce grimoire magique.
Cet ouvrage est protégé par un code qui change tous les quelques jours. {% hint "symbolic_cards_enigma_app" is needed %} {% fact "treasure_code_changes_magically" %}

Le code est constitué de symboles répartis entre 4 bijoux (indestructibles) des Maupertuis. 3 bijoux seulement suffisent à activer la chanson, car le dernier symbole peut se trouver *relativement* rapidement par essai et erreur sur le code du grimoire chantant.

Les différents bijoux :

- La broche de la mère de famille se trouve sur la **tombe d’Octave**, qui l’avait portée en souvenir après l'avoir retrouvée dans la bibliothèque ; cette broche était quasiment tout ce qui restait dans les cendres de l’enfant après la trahison, les avatars l’ont donc déposée là en signe de deuil. Cet objet doit guider les joueurs dans la compréhension de l’énigme globale. {% hint "maupertuis_mother_jewel_on_octave_tomb" is needed %} {% fact "octave_carried_mother_jewel_after_her_death" %}

- La broche du père de famille est cachée dans son livre magique protégé par clef ; ce livre a été trouvé par les héros (qui ont laissé une marque au sol pour le désigner), mais ils n’ont su comment l’ouvrir. Le **détecteur de magnétisme et d'UV** donnent un code, qui sert à ouvrir un AUTRE livre magique à code numérique (lui aussi marqué au sol), contenant lui la clef du premier.
  {% hint "maupertuis_father_jewel_in_twin_books" is needed %} {% hint "parcival_oracle_vision_about_maupertuis_father_twin_books" is needed %}

- La broche qui était initialement destinée à Octave se trouve dans un des N mini-coffrets scellés, qui sont cachés dans un SCEAU d'initiation. Il s’agissait d’une épreuve pour Octave, qui devait être capable de “sentir” la présence de l’objet magique avant d’y avoir droit. Les joueurs doivent activer le sceau, écouter le message pré-enregistré d'un automate qui leur résume l'épreuve, puis utiliser le **détecteur de métal** pour deviner le coffret qui a l’objet. Seul un héritier Maupertuis peut effectivement déclencher la résolution de cette initiation. {% fact "octave_needed_to_pass_initiation_to_gain_his_jewel" %} {% fact "only_maupertuis_heirs_can_take_initiation" %} {% hint 'maupertuis_initiation_seal' is needed %} {% hint "maupertuis_son_jewel_in_nonmetal_tiny_chests" is needed %}

- La broche de Mérédice, enfin, était précisément celle que le voleur venait chercher dans le domaine interdit. Il sait qu'elle se trouve dans une boite en métal, dans un recoin de la bibliothèque qui s'est **effondré**. Il vend donc cette information chèrement et à contrecoeur, en sachant qu'il n'est plus en bonne posture pour la quête du trésor des Maupertuis. Octave a aussi quelques indices, moins précis, sur l'endroit où sa soeur gardait ses biens les plus précieux. {% hint "maupertuis_daughter_jewel_under_rubbles_beyond_alchemist_laboratory" is needed %}
  {% fact "thief_knows_about_location_of_maupertuis_daughter_jewel" %} {% fact "octave_has_hints_about_location_of_maupertuis_daughter_jewel" %}

Rentrer les bons symboles dans le grimoire chantant déclenche une mélodie de victoire, et il faut alors simuler que le moulin, lorsqu’on le tourne, produit un lot de gemmes ; en nombre limité par jour (un lot toutes les X heures), mais suffisant pour la quête des agents secrets. {% hint 'jewels_set_for_grinding_mill_success' is needed %}

Avec le moulin magique et le grimoire chantant, les exZplorateurs ont réussi leur mission, à condition qu’ils puissent quitter les lieux.

{% endmacro %}
<{ spy_group_main_quest }/>


Le {% symbol "Thanatologue" for "book_of_the_dead" %} (explorateurs héliossars)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{% macro explorer_group_main_quest() %}

**Les explorateurs héliossars ont pour principal objectif de trouver le {% symbol "Thanatologue" for "book_of_the_dead" %}, un grimoire maudit, et surtout, grâce à lui, un moyen de contrer les maléfices et la tentative d'invasion de leurs ennemis les akarites.**

Un des rares exemplaires de cet ouvrage mythique (et controversé) a été conservé par la lignée des Maupertuis, dans le "coffre légendaire" situé dans le **domaine interdit** - ce qu'Octave ou l'archiviste devrait indiquer aux explorateurs-archéologues après avoir vérifié leur bonne volonté. Pour la sécurité du monde, les deux parents de Maupertuis devaient apporter leur code secret pour déverrouiller ce coffre. {% hint "family_legendary_chest_protected_by_double_code" is needed %} {% fact "octave_and_archivist_know_about_thanatologue_location_and_double_code" %}

- **{% symbol "Quirinius" for "maupertuis_father" %} de Maupertuis avait peu de mémoire**, il gardait ses codes dans son carnet de notes personnelles. Celui-ci est dans un de ses livres factices (voir ci-dessus pour son mode d’ouverture). Le code secret recherché est sous forme d'une **anamorphose en carré**. {% hint "quirinius_notebook_with_thanatologue_chest_code_as_anamorphosis_in_fake_book" is needed %}
  Il vaut **{% symbol "723" for "maupertuis_father_thanatologue_chest_code" %}**. {% fact "dead_quirinius_does_not_remember_thanatologue_chest_code" %}

- **{% symbol "Isadora" for "maupertuis_mother" %} de Maupertuis ne notait presque jamais rien et mémorisait tout**, il faut donc la questionner depuis l'au-delà pour obtenir son code. Cela se fait en envoyant un message par l’intermédiaire de l’Ankou (et donc de l’\ **invocateur**). En alternative, le **voleur** connait ce code (que la mère d'Octave avait aussi utilisé pour d’autres coffrets), et le vend très cher ; on peut aussi le trouver dans le portefeuille du voleur (gisant dans la niche de la Bête). {% fact "dead_isadora_remembers_thanatologue_chest_code" %} {% hint 'defunct_isadora_code_for_thanatologue_chest_code' is needed %} {% fact "diakon_invoker_can_message_ankou" %} {% fact "thief_knows_about_isadora_thanatologue_chest_code" %} {% hint 'thief_wallet_with_isadora_code_in_beast_nest' is needed %}
  Ce code est **{% symbol "159" for "maupertuis_mother_thanatologue_chest_code" %}**.

{% fact "maupertuis_mother_had_excellent_memory_but_not_father" %}

- Le {% symbol "Thanatologue" for "book_of_the_dead" %} se trouve bien dans le coffre légendaire, mais cela ne résout pas le problème. Ce livre enseigne en effet comment ressusciter temporairement - sous une forme zombie semi-intelligente mais obéissante - des gens morts récemment (en buvant d’abord une **Potion d'Autorité**, que l’alchimiste sait facilement fabriquer); et cela assurerait la victoire à une horde d’akarites fanatiques rentrant dans les défenses technologiques héliossares. {% fact "akarith_army_is_much_more_numerous_and_mystic_than_heliossar_army" %} {% fact "players_have_thanatologue_spell_to_summon_zombies" %} {% hint "recipe_authority_potion" is needed %}
  Les agents secrets doivent donc trouver la contre-mesure à cette stratégie nécromancienne. Un **message UV** donne un indice sur une solution, dans le {% symbol "Thanatologue" for "book_of_the_dead" %} : les akarites cherchent à viser en priorité les invocateurs du camp adverse, surtout ceux portant de grands bijoux. {% hint "thanatologue_book_with_zombie_spell_and_uv_counterspell_hints" is needed %}

- L’arkonte ne connaît pas de solution miracle à une légion de zombies - à part les combattre un à un avec des armes bénites. Mais il avait entendu parler de puissants enchantements de terrain, capables d’empêcher leur “réanimation” initiale à partir de cadavres. {% fact "arkon_has_clues_about_preventing_zombie_invocation_on_land" %}

- Les diacres connaissent un rituel simple permettant de “désenvouter” par avancer une tombe, et éviter ainsi qu’un nécromancien n'en tire un mort-vivant. Mais ils ne savent pas faire cela à l’échelle d’un champ de bataille, cela nécessiterait un artefact magique légendaire. {% fact "diakon_invoker_has_spell_against_zombie_invocation_on_single_tomb" %}

- L’oracle a une prophétie vision/audio d’une opposition entre une légion de morts-vivants, dirigés par un grimoire sombre, et un cimetière tranquille, enchanté par une bague surmontée d'un symbole : **{% symbol "soleil orné en son centre d'un tourbillon noir" for "amplificans_artefacts_symbol" %}**. {% hint "parcival_oracle_vision_about_necromancers_and_ring_amplificans" is needed %} {% hint "parcival_oracle_audio_about_necromancers_and_ring_amplificans" is needed %}

- L’arkonte se souvient de ce symbole, qui est entre autres celui de la légendaire **{% symbol "Bague Amplificans" for "ring_amplificans_name" %}**, qui aurait appartenu au fondateur de la lignée des Maupertuis, le {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %}, mais a disparu à sa mort. Il conseille de chercher des traces de cela dans le tombeau dudit mage. {% fact "arkon_has_hints_about_ring_amplificans" %}

- Une barrière magique ultra-puissante bloque l'accès au Tombeau du mage, même si les fantômes peuvent eux la contourner ; le seul moyen d'y pénétrer en tant que vivant, c'est manifestement de s'y téléporter. {% fact "magus_mos_peratys_tomb_is_extremly_well_sealed" %} {% fact "magus_mos_peratys_tomb_can_be_explored_by_free_phantoms" %}

- Le puissant {% symbol 'astrolabe de téléportation' for 'thief_teleportation_device_name' %} appartenant au voleur est sur sa dépouille, qui est maudite car il est "mort dans le vice". {% hint 'thief_cursed_skeleton' is needed %} {% hint 'thief_teleportation_device_in_beast_nest' is needed %}

- Le voleur demande une grosse somme d'argent pour donner le mot magique permettant de se téléporter. Il faut donc rassembler assez de richesses éparpillées pour cela, ou utiliser le trésor des Maupertuis une fois celui-ci trouvé. En alternative, cette formule est trouvable sous forme chiffrée dans les affaires du voleur. {% fact "thief_knows_teleportation_device_formula" %} {% hint 'thief_teleportation_device_encrypted_formula' is needed %}

- Seul un héritier des Maupertuis peut se téléporter tranquillement dans le tombeau, toute autre personne y déclenche le réveil du mage sous forme zombie, et doit donc le fuir jusqu'à pouvoir se retéléporter à l'extérieur. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

- Si une personne se rend seule avec l'astrolabe dans le tombeau du mage et est tuée, le seul moyen de rétablir la situation est de la **zombifier** (grâce au {% symbol "Thanatologue" for "book_of_the_dead" %}) pour qu'elle ramène les artefacts et l'astrolabe.

- Dans le tombeau se trouve entre autres, sur la dépouille du mage, la {% symbol "Bague Amplificans" for "ring_amplificans_name" %}. {% hint 'ring_amplificans' is needed %}

- Avec la bague magique et la formule du désenvoûtement, les explorateurs ont réussi leur mission, car ils ont quelques invocateurs dans leur armée ; à condition qu’ils puissent quitter les lieux, bien sûr.

{% endmacro %}
<{ explorer_group_main_quest }/>


Démasquer et neutraliser le méchant
+++++++++++++++++++++++++++++++++++++

{% macro quest_to_find_traitor_and_final_battle() %}

Les récits des différents fantômes concordent sur le fait qu’ils sont morts alors que se déroulait le rituel. Les soupçons doivent viser initialement l’arkonte, surtout de la part des avatars (qui n’ont pu le voir ensuite en tant que fantôme). Mais la Bête de l'étage interdit, ou une possible malédiction liée à l'ancêtre {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %}, peuvent aussi être suspectées.

L’arkonte, lui, sait qu’il s’est battu sauvagement avec un agresseur entouré de ténèbres, qui résistait bien aux attaques physiques, magiques et sacrées ; et qu’il a donc maudit cet attaquant (et la bibliothèque) en succombant.

Les soupçons se portent donc ensuite sur les avatars, qui pouvaient aller et venir entre les mondes pendant que le rituel se déroulait, via différents exemplaires de leurs romans.

Les restes d’Octave et de l’Archiviste sont introuvables, il semble qu’ils aient été réduits en cendres. Seuls restent les ossements (mais **sans le crâne**) de l’arkonte, qui sont en effet devenus indestructibles. **L’analyse médicale de ces ossements** révèle des signes de brûlure. {% hint "arkon_bones_having_traces_of_burning" is needed %}

Dans la niche de la Bête, parmi les restes du voleur, se trouve le **{% symbol "glaive" for "arkon_weapon_name" %} ULTRA-LOURD** de l'arkonte. Cette arme est analysable : elle possède des traces de sang bleu à sa surface. Hors, un des romans concernant le druide mentionne qu'il a le sang bleu.
{% hint "arkon_heavy_gladius_sword_stolen_by_thief" is needed %}
{% fact "arkon_heavy_gladius_sword_has_blue_blood_traces" %}
{% fact "druid_novels_mention_his_blue_blood" %}

Plusieurs **oracles** sont aussi délivrés pour aiguiller les joueurs.

- L’un montre une main boisée et griffue menaçant le monde, ainsi qu'un crâne sous des racines d’arbres, permettant de découvrir le crâne de l'arkonte dans la “mini jungle d’intérieur” du druide.
  {% hint "parcival_oracle_vision_about_skull_location_and_world_threat" is needed %} {% hint "arkon_skull_hidden_in_jungle_trees" is needed %}
  **L’analyse médicale du crâne** montre un empoisonnement au curare, ce qui fait naturellement suspecter le druide.  {% hint "arkon_skull_analysis_showing_curare_poisoning" is needed %}
- Un autre oracle montre un livre portant le chiffre 3, coincé entre des évocations de "Zoologie" et de "Patisseries". Le Tome 3 du roman du Druide est caché entre ces deux rayonnages de livres, indiqués par des étiquettes sur les meubles. {% hint "parcival_oracle_vision_about_location_of_chaos_novel_volume_three" is needed %} {% hint "authorized_zone_labels_showing_zoology_and_cooking_shelves" is needed %}
  La lecture d’un **extrait du Tome 3** montre que le druide est en réalité devenu un tyran cruel et déloyal à la fin de sa propre aventure. {% hint "chaos_novel_volume_three_between_zoology_and_cooking_shelves" is needed %}

Le druide nie initialement toutes les accusations, en traitant ses accusateurs de fous.
{# LATER **IDEE ANNEXE : le traitre assassine pendant le jeu un des avatars, qui s’opposait trop fort à l’idée de supprimer la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %} sans avoir résolu l’enquête de la mort des humains.** #}

Mais lorsque les différents indices probants sont exposés aux autres avatars, ceux-ci se rangent derrière les joueurs.
Typiquement, la duchesse va alors aller confronter le druide, sur une musique intense. {% fact "duchess_immediately_confronts_traitor_when_exposed" %}

Celui-ci change alors de posture, assume son crime au nom du Salut de Pangéa, et rappelle qu'il est bien plus puissant que tous les participants rassemblés. Il exige donc de tous de l'aider à briser la malédiction de la bibliothèque, en échange de la vie sauve dans son futur Havre de Nature.

Il exhorte les joueurs à se dépêcher : lui a tout son temps, et maintenant qu’il a accès aux grimoires du domaine interdit, il finira bien par découvrir comment utiliser la magie de ce monde et briser la malédiction de la bibliothèque ; mais eux ont des missions urgentes à accomplir et doivent ressortir avant que les portails de transplanage ne se referment, d'ici quelques heures.

Le druide prévient qu'il ne s'éloignera plus du pentacle du rituel de l'arkonte, afin que personne ne tente de le renvoyer de force dans son monde ; et qu'il sentirait si un autre pentacle similaire était créé dans les environs.

Typiquement, il se met alors à **lire des grimoires** (dont le {% symbol "Thanatologue" for "book_of_the_dead" %}), l'air enthousiaste, non loin du pentacle. Il est réellement sur la piste d'un **contre-sortilège** pour annuler la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %}. {% fact "druid_reads_near_pentacle_before_game_ending" %}

Le traître est insensible aux attaques usuelles.
Si les joueurs l'agressent directement, il en tue un (qui devient un fantôme), puis ordonne aux autres de continuer à chercher comment lever la malédiction.

Mais il existe certaines façons de l'atteindre :

{# NOPE for now - Soit confectionner et lui faire boire une **potion magique d’autocombustion**, qui va retourner sa puissance magique contre lui ; cette potion doit impérativement lui être apportée suffisamment tôt, et par l’automate, pour qu’il ne soit pas soupçonneux. #}
{# NOPE for now - Soit reconstituer un pentacle de renvoi ailleurs TOO HARD, et utiliser le Tome 3 dessus pour expulser le Druide du monde des humains (mais attention il ne faut pas qu’il voie cela, il faut donc le détourner s’il vient voir ce que font les joueurs).  #}

- Soit ensorceler une fléchette d'arbalète pour qu’elle devienne **inévitablement létale** ; c’est un sortilège sombre du Thanathologue, le {% symbol "Sacrifice de Zarathoustra" for "unavoidable_bullet_spell_name" %}, qui exige la mort volontaire de **trois joueurs** pour créer une "arme qui ne pardonne pas". {% hint "unavoidable_bullet_spell_from_thanatologue" is needed %}
  L'alchimiste peut recréer des fléchettes grâce à une recette trouvée dans le domaine interdit. {% fact "parcival_alchemist_can_create_iridium_arrows" %} {% hint "arrow_recipe_for_alchemist" is needed %}

- Soit la façon la plus efficace : rendre un ritualiste invulnérable aux attaques physiques, toxiques, et magiques, puis l'envoyer détruire massivement les corridors d'outre-monde grâce à l'un de ses **rituels**, et murer ainsi les avatars dans leurs mondes respectifs. {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

Une prophétie holographique détaillant ce procédé de "diacre invulnérable" et ses limites peut être déclenchée en activant, par une Lotion de Restauration, un des portraits horrifiques suspendus au mur ; portrait reconnaissable, car il réagit au détecteur de métaux (le joueur possédant cet outil a des informations là-dessus).
{% hint "scary_lenticular_painting_with_metal_in_it" is needed %}
{% hint "prophecy_hologram_for_scary_lenticular_painting" is needed %}
{% fact "spy_sounder_knows_about_scary_lenticular_paintings" %}
{% fact "scary_lenticular_paintings_can_deliver_powerful_prophecy" %}
{% hint "potion_of_revelation_from_exorcist" is needed %}

- Si cette prophétie holographique n'est pas trouvée, une **intuition** de l'Oracle peut évoquer aussi ce plan de bataille, et met en garde contre une riposte du méchant à l'aide des fantômes. {% fact "parcival_oracle_has_fallback_intuition_about_last_battle" %}

Voici le déroulement "optimal" de cette bataille finale utilisant un rituel d'expulsion :

- Les joueurs doivent rassembler **le {% symbol "Collier éthérique de peau de pierre" for "etheric_stone_skin_necklace_name" %}, le {% symbol "Collier éthérique de force vitale" for "etheric_vital_force_necklace_name" %}, et le {% symbol "Collier éthérique d'aura manaïque" for "etheric_manaic_aura_necklace_name" %}**, qui sont stockés à différents endroits de la bibliothèque. {% hint "etheric_stone_skin_necklace" is needed %} {% hint "etheric_vital_force_necklace" is needed %} {% hint "etheric_manaic_aura_necklace" is needed %}

- Par sécurité, les autres avatars doivent être poussés par l'exorciste à chacun retourner dans son monde, sans quoi ils seraient mis en grave danger par le rituel. {% fact "diakon_exorcist_might_kill_remaining_avatars_with_expulsion_ritual" %}

- Lorsque l'exorciste commence son rituel, le druide est d'abord confus, puis, comprenant ce qui se passe, il l'attaque par différents moyens, mais en vain.

- En désespoir de cause, le druide va utiliser la {% symbol "Clochette Spectrale" for "table_bell_name" %} pour rameuter les spectres et ainsi mettre en danger le ritualiste ; celui-ci n'a pas la carrure pour endosser l'{% symbol "Armure de Mithril" for "arkon_armor_name" %} de l'arkonte (qui contient le {% symbol "Collier éthérique de bénédiction" for "etheric_benediction_necklace_name" %}), et se protéger ainsi des spectres. {% fact "druid_finally_uses_table_bell_as_weapon" %}{% fact "etheric_benediction_necklace_is_in_arkon_sacred_armor" %} À charge pour les autres joueurs de repousser les spectres (avec ladite armure de l'arkonte, avec des exorcismes...), sans se faire eux-mêmes attaquer par le druide.

- Une fois le rituel à son terme, le druide est comme blessé ; l'arkonte intervient alors pour clamer victoire, et appelle tous les diacres autour de lui pour quelques dernières répétitions de l'incantation rituelle. Il peut s'en désolidariser à la fin pour clamer : **"Per Horus et per Ra, per solem invictus, duceres {% symbol "Diviciacos" for "druid_name" %}, ACTA EST FABULA"**. Le druide est alors attiré par le pentacle et y meurt (https://fr.wikipedia.org/wiki/Per_Horus_et_per_Ra_et_per_Sol_Invictus_duceres).

- Si le diacre abandonne le rituel pour une raison ou une autre, le druide peut "faire un exemple" en tuant un des joueurs, puis réitère ses ordres envers les survivants.

Que le traître soit anéanti d'une manière ou d'une autre (balle maudite ou rituel d'expulsion), la malédiction prend fin, et l’épilogue peut se dérouler. {% fact "traitor_death_ends_cursed_enclosure" %}

Mais si un joueur suit les ordres du druide et lève la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %}, ou si tous tardent trop à agir et le druide brise finalement lui-même cette malédiction (grâce une formule prétendument trouvée dans un grimoire), alors le druide s'échappe immédiatement de la bibliothèque.

Les joueurs peuvent dans ce cas effectivement rentrer chez eux, mais avec l'amertume de l'échec : avoir lâché un monstre dans leur monde. Et les **avatars restants** (ou revenus en ayant senti le drame) peuvent choisir entre être révoqués, ou rester pour essayer d'aider cette planète face au nouveau péril.

{% endmacro %}
<{ quest_to_find_traitor_and_final_battle }/>


Finir le rituel d'expulsion des avatars (diacres)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les avatars refusent initialement que quiconque continue le rituel, commencé par l’arkonte et interrompu par la trahison du méchant, en vue de les renvoyer chez eux. En effet, ils ne veulent pas partir tant que les fantômes n’auront pas reçu justice et été libérés. À cela s’ajoute initialement la crainte que le rituel ait, en lui-même, causé ces drames.

Le pentacle et les objets du rituel sont toujours en place, le traître n’ayant pas osé toucher à cette magie sacrée qu’il ne connait pas, et ne pouvant de plus, par nature, transporter des romans. {% fact "avatars_cannot_carry_novels" %}

C'est uniquement une fois le plan de bataille finale bien établi, ou le méchant déjà supprimé par un quelconque moyen, que les avatars acceptent de retourner chez eux et de laisser le rituel de l'exorciste les renvoyer définitivement dans leurs mondes.  {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

Si un joueur tente de renvoyer par la force les avatars "gentils", cela causera certainement un certain chaos tant parmi les figurants que les joueurs.


Supprimer précocement la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %} de la bibliothèque (piège)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

La clôture de la bibliothèque peut être supprimée prématurément par un rituel connu des diacres, qui requiert la coopération d’au moins les **{% symbol "3 / 5 des vivants" for "library_cursed_enclosure_opening_quota" %}** présents, ainsi que des **ingrédients** facilement accessibles dans l’atelier d’alchimiste du domaine interdit. {% fact "diakon_invoker_can_break_cursed_enclosure" %} Mais si cette malédiction est détruite ainsi, le traître s’échappe de la bibliothèque, et c'est un échec pour tous, comme décrit ci-dessus.

Dans l’issue optimale du jeu, la malédiction de la bibliothèque est automatiquement levée à la mort du traître, et cette quête n’a plus lieu d’être. {% fact "traitor_death_ends_cursed_enclosure" %}

{# NOPE TOO MANY MISSIONS ALREADY

    Préserver les grimoires légendaires (bonus des diacres ?)

    La plupart des ouvrages de la bibliothèque sont des copies de livres courants, ou retrouvés depuis dan s d’autres lieux mystiques. Mais le {% symbol "Thanatologue" for "book_of_the_dead" %}, ainsi que deux ouvrages (Necronomicon? Codex Vampiris ?) ne doivent pas tomber dans les mains des impies qui vont probablement finir par trouver, à leur tour, cette bibliothèque.

    Les deux grimoires supplémentaires peuvent être trouvés grâce au *magnétisme sur une carte de la bibliothèque?, ou en soudoyant le voleur.

    Ils doivent être utiles aux joueurs, eux aussi, avant de pouvoir être détruits sans regrets. Ou au contraire doivent être des pièges pour les lecteurs trop audacieux...

#}


L'orbe spirituel, le vortex abyssal (piége) et la source de savoir (don)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*Ceci est une quête facultative.*

Dans le domaine interdit, les joueurs peuvent trouver un plateau avec une boule à plasma éteinte au centre, désignée comme un {% symbol "orbe spirituel" for "spiritual_orb_name" %}** ; 4 emplacements sont dessinés autour de lui.

Ces emplacements attendent chacun un objet-clé, qui est une moulure en résine epoxy :

- un cristal romantique (une rose dans une pyramide à base carrée)
- un cristal marin (un coquillage dans une pyramide à base triangulaire)
- un cristal piquant (un chardon dans un cube)
- un cristal innocent (des fleurs blanches dans un diamant)
{% hint 'spiritual_orb_key_square_base_pyramid' is needed %}
{% hint 'spiritual_orb_key_triangle_base_pyramid' is needed %}
{% hint 'spiritual_orb_key_cube_is_needed' is needed %}
{% hint 'spiritual_orb_key_diamond_is_needed' is needed %}

Il est indiqué, par un blason (à triade de flammes) que l'anthropologue connait, et par un extrait du Thanatologue, qu'en rassemblant ces cristaux et en clamant une certaine formule magique, on peut ouvrir le **"vortex abyssal"**. {% fact "anthropologist_knows_about_fire_triad_emblem" %} {% hint 'abyssal_vortex_hint_in_thanatologue' is needed %}

Les avatars ou fantômes Maupertuis ne savent rien à ce sujet, mais l'arkonte se méfie de cet artefact méconnu. {% fact "arkon_is_worried_about_spiritual_orb_magic" %}

il s'agit en réalité d'un canal de communication vers une dimension démoniaque. Une fois ce canal ouvert (donc une fois la boule à plasma allumée), les joueurs qui posent le doigt dessus sont contaminés par des influences néfastes trop puissantes pour eux. En fonction de leur personnage, ils vont avoir des gages montrant que leur santé mentale a été blessée ; avec toujours beaucoup d'agitation et de paroles incohérentes.

Exemples de gages :
- l'oracle se met à  faire des prédiction abracadabrantes
- l'alchimiste boit une de ses potions (non létale)
- d'autres se mettent à utiliser en vain leur détecteur de métaux, leur lampe UV, sans but...

Cet orbe peut aussi ouvrir des passages vers d'autres strates de la réalité. En particulier, le voleur connait la formule permettant d'ouvrir un passage vers la **{% symbol "Source de Savoir" for "link_to_djinn_world" %}**. Si les joueurs posent le doigt sur l'orbe connecté à ce monde-ci, ils deviennent liés au **monde invisible des Djinns**, petits esprits curieux, invisibles, inoffensifs, qui errent un peu partout. {% fact "phantom_thief_knows_formula_of_link_to_djinn_world" %}

Les joueurs peuvent utiliser ce don comme un moteur de recherche historique, et poser au maître de jeu des questions sur le lore de cette planète, sur les grands aspects de l'histoire des Maupertuis. Les djinns ne savent pas tout, ont des avis divergents, se trompent parfois, mais donnent des informations généralement instructives et utiles.

Le **Djinn renégat**, joué par le maître de jeu, a en réalité été coupé de la communion avec ses congénères par les invocations frénétiques et dangereuses de l'arkonte lors du combat tragique ; il recherche donc un artefact magique pour pouvoir se reconnecter à son monde spirituel, qui n'est autre que la {% symbol "Source de Savoir" for "link_to_djinn_world" %}.


Survol des compétences spécifiques des participants
=============================================================

Ces rôles peuvent être facilement réaffectés ou cumulés à l’intérieur d’une équipe, en cas de changements dans les joueurs présents. Ils viennent en plus des compétences communes à tous les joueurs (chercher des objets, utiliser des clefs, discuter avec des figurants), qui sont aussi nécessaires pour progresser dans les énigmes.

IMPORTANT : chaque rôle doit avoir son **“moment de gloire”** prévu dans le scénario - à charge pour le joueur de savoir s’en saisir.

Famille Parcival
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Gardien des bois : armé d'une arbalète, avec une force herculéenne ; il a un fort instinct de protection, et connait divers monstres
- Alchimiste : sait fabriquer des potions pour divers usages ; possède divers ingrédients (non matérialisés), et une sacoche avec des fioles vides
- Oracle : reçoit ponctuellement de grandes révélations visuelles ou auditives, ainsi que des intuitions

Agents secrets mirandiens
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Démineur : sait sécuriser des pièges/éboulements, possède des explosifs et des bougies LED ; connait bien la mécanique
- Sondeur : sait détecter les métaux et les champs magnétiques de surface ; reconnaît la nature anormale (archéologique, magique ou divinatoire) des artefacts
- Crocheteur : sait forcer certains cadenas, et ouvrir des serrures/antivols magnétiques ; a trouvé les potions des diacres

Diacres de {% symbol "Bahamoot" for "god_of_diakons" %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Désenvouteur : reconnait les envoûtements d'objets (par symboles ou code), supprime ceux négatifs, et connait les types de blessures
- Exorciste : sait attirer ou bannir des esprits, et bénir des armes ; connait les fantômes
- Invocateur : sait réaliser des rituels magiques complexes à l'aide de pentacles ou sceaux ; possède un encensoir

Explorateurs-archéologues héliossars
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Runologue : sait traduire des runes akarites et reconnaître divers codes secrets ; possède une loupe et un stéthoscope
- Dévoileur : sait lire les encres UV invisibles, et analyser scientifiquement (avec un code) des objets
- Anthropologue : érudit en traditions humaines, blasons, et valeurs marchandes ; ritualiste de Bahomoot ; connait les fantômes et les types de blessures


.. raw:: pdf

   PageBreak


L'univers du jeu
#############################

*Ces informations sont répliquées dans des résumés généraux ou fiches de personnage pertinentes.*

{% macro common_lore_for_all() %}

Contexte Historico-géographique
================================

{# FIXME DEDUPLICATE THIS ONE DAY #}

L'action se passe sur la planète Pangéa, en **l'{% symbol "an 1000" for "current_events_year" %} de l'{% symbol "ère du Grand Apaisement" for "current_era_name" %}** ; le niveau de développement actuel y est similaire à notre 20° siècle terrestre, mais avec une population bien plus réduite.

En réalité, toute l'Histoire de cette planète, de la préhistoire jusqu'à l'an 1900, est identique à la nôtre. Les références à ces époques de notre monde (Antiquité, Moyen-âge, Renaissance...), à leur production culturelle et artistique, sont donc valables sur Pangéa, même si peu de gens les connaissent.

C'est au début du 20° siècle que les deux mondes ont divergé. Pendant que le nôtre continuait son chemin vers les guerres mondiales, Pangéa a subi un bouleversement tectonique et climatique majeur, appelé le {% symbol "marasme planétaire" for "catastrophic_period" %}, qui a torpillé tout développement humain durant des siècles.

La planète est enfin sortie, à grand-peine, de ce cataclysme, et l'humanité reprend son essor.

La monnaie internationale est le **kash** (1 kash permet de se payer environ 100 pains).


Le {% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}
=====================================================================

L'arkonte Zarathoustra serait à l'origine de cet envoutement planétaire très puissant, et toujours en effet si longtemps après sa mise en place - au tout début de l'ère actuelle.

Sur Pangéa, toute personne qui jure quelque chose **"Par le {% symbol "Serment de Zarathoustra" for "unbreakable_oath_name" %}"** est tenu par les Cieux de respecter son engagement, quelles que soient ses propres croyances.

Concrètement, tout parjure sera rapidement sanctionné par un douloureux châtiment, allant de l'infirmité à la mort, selon la gravité du mensonge. Plus encore, les forces du destin se combineraient pour réaliser la promesse trahie, à la place de son auteur. Ainsi, lorsqu'un chevalier oriental jura par Zarathoustra qu'il détruirait un puits maléfique, mais revint sur sa promesse, la légende raconte que non seulement il perdit un bras lors de la bataille suivante, mais aussi que des boeufs sortirent de leur chemin pour démanteler le puits eux-mêmes.

Si certaines personnes jouent encore les sceptiques à ce sujet, dans les faits il n'est plus une seule personne qui se risquerait à abuser de ce serment ; et hormis en quelques cas graves, on préfère habituellement jurer sur la tête de quelqu'un ou sur son propre honneur, ce qui n'engage pas à grand-chose.

Les mystiques s'accordent sur le fait que ce serment ne s'applique qu'aux pangéens *vivants* ; les défunts, les divinités et des entités d'outre-monde s'en serviraient donc parfois pour leurrer des humains. {% fact "unbreakable_oath_only_concerns_living_pangeans" %}


Divinités et mondes alternatifs
=============================================

Beaucoup de croyances coexistent sur Pangea, apparaissent et disparaissent. Actuellement, les principales divinités adorées sont les **Yods** (une infinité dans l'unité), **{% symbol "Bahamoot" for "god_of_diakons" %}** le dragon cosmique, et diverses Forces de la Nature. Parmi les divinités inférieures, on trouve l'Ankou, guide des morts ; ainsi que les **Djinns**, des êtres inoffensifs, érudits et invisibles, qui sont répartis sur toute la planète. La rumeur court que nombre de dieux et déesses, anges et démons, seraient en réalité juste les habitants d'univers fort lointains, ou d'autres strates de la réalité.

.. raw:: pdf

   PageBreak

Carte du monde de Pangéa
==============================

*La géographie a très peu d'importance dans cette soirée mystère, inutile d'appendre ces pays et villes.*

[BR]

.. image:: ../assets/pangea_world_map_v10_8bits-rotated.png
    :align: center
    :width: 2000px


{% endmacro %}
<{ common_lore_for_all }/>

.. raw:: pdf

   PageBreak

{% macro common_npc_lore_knowledge() %}

Connaissances des personnages de l'ère Maupertuis
============================================================

*Voici ce que savent tous les avatars et les fantômes, sauf le voleur ; celui-ci connait un peu les vieilles légendes et le contexte du saccage du manoir, mais c'est tout. Délivrez ces informations aux joueurs, lorsqu'ils vous questionnent par eux-mêmes à ce sujet.*


Le {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ce mage a vécu {% symbol "3 siècles" for "mages_war_before_curse_timedelta" %} avant la malédiction de la bibliothèque, durant la {% symbol "Guerre des Trente Sorciers" for "mages_war_name" %}.

Redoutable magicien, alchimiste, et duelliste, il a défait tous ses adversaires. La légende raconte qu'il était invulnérable aux sortilèges magiques, et pouvait faire tomber la pluie ou la grêle sur des villes entières, quand ses adversaires invocateurs ne touchaient jamais plus que quelques ares de terrain à la fois.

Pour éviter tout empoisonnement, il avait appris à générer lui-même de la nourriture à partir de simples roches ; un savoir qui est resté dans sa descendance sous la forme d'une table de banquet magique, située dans la bibliothèque, qui transmute toute seule de la nourriture à partir des roches environnantes. {% fact "buffet_table_magically_generates_food" %}

Il a créé le château familial des Maupertuis, la bibliothèque enfouie, ainsi que le réseau de portails de transplanage la reliant aux domaines de ses vassaux.

Il est mort brusquement lors de grandes festivités, à l'approche de ses 50 ans, en s'étouffant avec un noyau de pêche. Il n'avait pas encore transmis à ses héritiers ses plus importants secrets.

Ses proches l'ont enterré à la va-vite dans une salle jouxtant la bibliothèque, dans sa robe de fêtes, sans oser risquer de déclencher quelque malédiction en le toilettant. En particulier, autant il était très fier de sa lignée, autant le mage était **haineux** envers la "piétaille" non-initiée aux arts magiques, et la légende raconte que sa tombe résonne encore de ce sentiment. {% fact "magus_mos_peratys_tomb_kills_non_heir_intruders" %}

Depuis, chaque génération de Maupertuis ajoute sa propre surcouche de protections à son tombeau, afin que nul **étranger** ne viole jamais la sépulture de ce vénérable aïeul, ni aucun des dangereux mystères qu'il a emportés dans la tombe. À ce jour, aucune guilde de mages sur la planète ne serait probablement capable de briser autant d'envoutements accumulés. Mais peut-être qu'il est possible d'y entrer par des moyens détournés, qui sait ? {% fact "magus_mos_peratys_tomb_is_extremly_well_sealed" %}

*Note : une fois libérés de leur ancrage, les fantômes PEUVENT entrer dans le tombeau en passant par les murs l'entourant, qui ne sont eux pas protégés par un {% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %} ni exclus de la {% symbol "Clôture Absolue" for "library_cursed_enclosure_name" %} entourant la bibliothèque entière. Il peuvent donc ramener quelques informations sur le contenu du tombeau.* {% fact "magus_mos_peratys_tomb_can_be_explored_by_free_phantoms" %}


Les colliers éthériques
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les légendes parlent de plusieurs colliers magiques forgés par des alchimistes durant cette {% symbol "Guerre des Trente Sorciers" for "mages_war_name" %}, et disparus peu après.
Il est communément admis que le {% symbol 'Mage Mos Peratys' for 'maupertuis_dynasty_founder' %} aurait mis la main sur plusieurs d'entre eux. En particulier, sa diction trainante mais tonitruante lors de toutes ses apparitions publiques a déclenché plus d'une suspicion. {% fact "magus_mos_peratys_often_wore_manaic_aura_necklace" %}

**{% symbol "Collier éthérique de peau de pierre" for "etheric_stone_skin_necklace_name" %}** (formé de perles plates ovales bleutées translucides) : Celui qui porte ce collier autour du cou devient insensible aux armes physiques (contondantes, perçantes ou tranchantes). En contrepartie, il marche et bouge les bras très lentement, tel un golem.

**{% symbol "Collier éthérique de force vitale" for "etheric_vital_force_necklace_name" %}** (formé de perles de bois) : Celui qui garde ce collier autour du cou devient insensible à tout ce qui attaque le corps par l'intérieur : maladies, poisons solides ou liquides, vapeurs toxiques... En contrepartie, il ne peut respirer que par la bouche (bruyamment), et ne peut ni boire ni manger.

**{% symbol "Collier éthérique d'aura manaïque" for "etheric_manaic_aura_necklace_name" %}** (formé d'un quartz avec collier fin doré) : Celui qui porte ce collier autour du cou devient insensible aux sortilèges élémentaux (de feu, de glace, de foudre...) et aux envoûtements maléfiques d'objets. En contrepartie, il ne peut parler que très fort et très lentement tant qu'il le porte. Les dommages de type "sacré" (blessures de fantômes, de démons...) ne sont pas évités par ce collier. {% fact "etheric_manaic_aura_protects_from_magic_and_cursed_objects_too" %}

**{% symbol "Collier éthérique de bénédiction" for "etheric_benediction_necklace_name" %}** (formé d'anneaux de Mithril avant d'être fondu dans l'armure de l'arkonte) : Celui qui garde ce collier autour du cou devient impalpable sur le plan spirituel, il ne peut donc plus être blessé par des fantômes, démons, ou malédictions. En contrepartie, cela lui demande une grande force physique car ce collier est extrêmement lourd. {% fact "etheric_benediction_necklace_is_in_arkon_sacred_armor" %}


Le déclin magique
+++++++++++++++++++++++++++

Dans les siècles suivants, le "contraste magique", c'est-à-dire la puissance phénoménale de quelques individus par rapport au reste de la population, s'est largement atténué. Bridés par le gout du secret et les limitations d'une pratique artisanale, les arts magiques et ésotériques ont presque partout été dépassés par les technologies guerrières ; ils ont surtout subsisté dans leur coloration religieuse, en lien avec le monde des morts.

Les grandes lignées de magiciens sont tombées l'une après l'autre, à cause de dissensions internes, ou d'agressions populaires plus ou moins justifiées.
La lignée des Maupertuis a tenu plus longtemps que les autres, grâce à une réputation favorable due à son orientation vers les soins médicinaux.

Depuis la chute du manoir familial, même la bibliothèque enfouie, pourtant bardée d'envoûtements de protection (anti-feu, anti-inondation, anti-casse...), se délite peu à peu ; certains murs, entièrement désenvoutés, se sont effondrés. Mais ce processus prendra encore de nombreux siècles ; et certains artefacts continuent de préserver, de manière isolée, les puissants flux magiques qui les traversent.


Le domaine interdit et la Bête
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Le domaine interdit des Maupertuis, un étage de la bibliothèque rempli de dangereux secrets, a toujours été protégé par des **monstres vivants**, enchantés pour se passer de nourriture et vivre longtemps. Choyées en échange de leurs bons services, ces créatures étaient, de génération en génération, présentées aux nouveaux héritiers Maupertuis, qui devenaient leurs nouveaux maîtres. L'identité de ces créatures était volontairement cachée, par sécurité, si bien que seuls les héritiers Maupertuis savaient à quelle espèce elles appartenaient.

Lors de la malédiction de la bibliothèque, il restait un monstre de garde, surnommé "La Bête", dans le domaine interdit ; il est probable qu'il a connu un funeste destin (les fantômes entendent parfois son cri lugubre, mais pas les avatars). Il parait qu'il avait la particularité d'être très myope, **ne voyant pas grand-chose à plus de 3m**. {% fact "characters_know_how_the_beast_works_regarding_3m_sight" %}

L'entrée du domaine interdit est, depuis la fondation de la bibliothèque, protégée par un **{% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %}**. Cet envoutement légendaire résiste spectaculairement aux **attaques physiques, magiques, et peut même bloquer les fantômes** ; ce dernier point est habituellement anecdotique, car les esprits peuvent habituellement contourner ce blocus et passer à travers les murs (cependant, les fantômes n'ont pas vu de spectre de la Bête errer de leur côté de la bibliothèque). {% fact "beast_cannot_access_normal_zone_because_of_ultimate_seal" %} {% fact "phantoms_cannot_cross_some_fence_enchantments" %}

Pour ouvrir temporairement l'accès au domaine interdit, il faut reconstituer sur un grimoire magique le **symbole secret des Maupertuis**, transmis de génération en génération ; l'accès est alors débloqué **pour 12 heures**. {% fact "secret_family_symbol_needed_for_forbidden_zone" %} {% fact "npcs_know_about_secret_family_symbol_system" %}

En définitive, parmi les protagonistes du drame, **seul Octave était déjà entré** (accompagné de ses parents) dans ce domaine interdit. {% fact "only_octave_had_been_in_forbidden_domain" %}


La derrière maisonnée des Maupertuis
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les parents Maupertuis étaient très différents et complémentaires ; par exemple autant {% symbol "Isadora" for "maupertuis_mother" %} avait une excellente **mémoire** et ne notait jamais rien, autant {% symbol "Quirinius" for "maupertuis_father" %}, lui, oubliait rapidement tout, et devait noter jusqu'à ses secrets les plus sensibles dans des carnets, qu'il laissait bien cachés dans la bibliothèque. {% fact "maupertuis_mother_had_excellent_memory_but_not_father" %}

Au moment de l'attaque du manoir, Mérédice de Maupertuis avait déjà beaucoup progressé dans les arts magiques, et en particulier - comme ses prédécesseurs - dans les potions et gemmes de guérison. Elle travaillait régulièrement dans les **cabinets d'alchimie et de gemmologie du domaine interdit**. Elle laissait d'ailleurs la plupart de ses affaires dans la bibliothèque, de peur de les perdre lors de ses excursions d'herboristerie dans les environs, ou en cas de cambriolage du manoir.

Octave, lui, avait à peine commencé ses apprentissages, d'autant plus qu'il était distrait par ses lectures romanesques et fantastiques. Il n'était donc jamais allé seul dans l'étage interdit (la Bête l'aurait d'ailleurs attaqué dans ce cas). {% fact "octave_would_have_been_attacked_by_beast_if_alone_in_forbidden_domain" %}

Il devait tout bientôt passer son **initiation appelée "adoubement"**, une cérémonie ne fonctionnant que pour les héritiers de la lignée Maupertuis : {% fact "only_maupertuis_heirs_can_take_initiation" %}

- Réussir à activer le **Sceau d'initiation** présent sur place
- Tenter de déterminer, uniquement par sa sensibilité aux auras magiques, quelle petite boite, parmi un ensemble, contenait sa **broche personnelle**, et obtenir ainsi cet artefact dynastique {% fact "octave_needed_to_pass_initiation_to_gain_his_jewel" %}
- En cas de réussite, **recevoir le symbole secret** de la famille Maupertuis ; être présenté à la Bête du domaine interdit, et recevoir d'elle un serment d'allégeance
- En cas d'échec, réessayer cette cérémonie dans 6 mois.

Durant son confinement dans la bibliothèque, Octave portait en souvenir la **broche de sa mère**, qu'il avait retrouvée sur place. {% fact "octave_carried_mother_jewel_after_her_death" %} {% hint 'maupertuis_mother_jewel_on_octave_tomb' is provided %}

Dans leur enfance, Octave et sa soeur jouaient à se créer des jeux de piste - et autres énigmes - l'un pour l'autre. Mérédice en avait créé un spécialement espiègle pour célébrer le futur adoubement d'Octave, en lui subtilisant sa tirelire remplie d'économies. Et elle avait placé la dernière énigme menant à ce petit trésor dans la **{% symbol "Boîte à Murmures" for "whispering_box" %} présente au fond d'un coffre de bois.** {% hint "whispering_box_with_children_enigma_in_common_brown_chest" is needed %} ; les membres de la famille utilisaient cette boite magique pour se laisser des messages, qu'ils écoutaient en posant le doigt dessus. {# Les joueurs doivent utiliser un stéthoscope pour lire ces messages #} Octave n'a jamais pu retrouver sa tirelire, probablement parce qu'elle était cachée dans le domaine interdit. {% fact "octave_moneybox_hidden_by_meredice_is_lost" %}


La {% symbol "Clochette Spectrale" for "table_bell_name" %} et la {% symbol "frénésie spectrale" for "phantom_frenzy_name" %}
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Si l'on vous parle d'une **clochette de table** (petite, ronde et métallique), vous ne savez rien à son sujet ; vous savez juste qu'elle n'était **pas visible** dans la bibliothèque de votre vivant (même pour le voleur), donc quelqu'un a dû l'apporter ou la sortir d'une cachette.
Les automates ignorent, étrangement, le son de cette sonnette.

Si quelqu'un appuie sur la clochette pour la première fois, le MJ doit déclencher la bande-son angoissante de la **{% symbol "frénésie spectrale" for "phantom_frenzy_name" %}**. les fantômes se mettent alors sous-forme non-incarnée, et se ruent vers le son de clochette. Une fois près d'elle, ils errent de gauche et de droite, non loin, éperdus, jusqu'à la fin de la bande-son, puis reviennent à ce qu'ils faisaient avant. {% fact "table_bell_triggers_spectral_frenzy" %}

Par la suite, la clochette est censée être **temporairement déchargée** de sa magie, les avatars et fantômes peuvent le sentir et le disent aux joueurs s'ils appuient encore sur la clochette. *Mettre un scotch noir dessus pour matérialiser cela.* {% fact "table_bell_is_only_usable_once" %}

*Spoiler : Il s'agit en réalité juste d'un signal de rappel oublié par l'Ankou lors d'un précédent passage, mais seul l'Ankou le sait.* {% fact "table_bell_belongs_to_ankou" %}

*Le druide doit discrètement voler cette clochette, après avoir compris son usage en discutant avec les joueurs.* {% fact "druid_must_steal_table_bell_when_usage_understood" %}

{% endmacro %}
<{ common_npc_lore_knowledge}/>



Le fonctionnement des fantômes
==============================================

{% macro phantom_knowledge_article() %}

Il existe bien peu de connaissances fiables sur le monde des morts. De nombreux exorcistes et mystiques attestent cependant que, parfois, au lieu de flotter librement vers l'au-delà, des défunts peuvent passer des années ou des siècles à errer sur Terre, pour des raisons fort diverses.

Des deux formes fantomatiques
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Il est possible de communiquer avec un fantôme lorsque celui-ci est dans une phase "incarnée". Il s'agit bien sûr d'un abus de langage, car le défunt reste incapable d'interagir normalement avec le monde de chair et de matière ; il n'en est pas moins capable de dialoguer, de raisonner, et de se souvenir de sa vie passée, même si la conscience qu'il a de sa situation peut être très variable. Ces moments privilégiés sont le meilleur moyen pour un exorciste de comprendre ce qui retient un fantôme sur terre, afin de prendre des mesures correctives. Ces phases d'incarnation sont plus fréquentes et longues lorsque des vivants sont dans les parages.

Le reste du temps, les fantômes errent comme des "spectres" sans but, privés de la plupart de leur intelligence, et uniquement attirés par les vivants lorsqu'ils les croisent de près. Le degré d'agitation de ces fantômes éthérés, désincarnés, dépend alors en partie du poids de leurs péchés terrestres {% fact "phantoms_of_sinners_have_faster_specters" %}. Mais tous peuvent entrer dans une intense "{% symbol "frénésie spectrale" for "phantom_frenzy_name" %}", lorsqu'ils sont touchés par les ondes de quelque rituel magique ou sacré, ou bien à certains moments significatifs de la journée ; leurs déplacements sont alors plus rapides, et ils semblent rechercher à tout prix le contact des vivants ou bien d'un artefact spécifique.

Fait intéressant, les fantômes gardent une grande partie de leurs instincts animaux, de leurs goûts et dégouts, même lorsqu'ils sont en errance spectrale. {% fact "phantoms_always_keep_most_of_their_instinct" %}

Il est établi que les fantômes peuvent le plus souvent passer à travers les murs et les objets ; cependant, n'étant pas entièrement dématérialisés, cela leur demande des efforts supplémentaires, aggravés lorsque les lieux ont été protégés par des envoûtements magiques ou des bénédictions sacrées. Dans les faits, les fantômes suivent donc souvent les mêmes parcours que les humains. Noter que certains enchantements puissants peuvent ériger des murs dans le monde des vivants ET des morts, empêchant donc aussi le passage des fantômes incarnés comme ceux désincarnés. {% fact "phantoms_cannot_cross_some_fence_enchantments" %}


De la dangerosité des revenants errants
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

La littérature ésotérique ne cesse de mettre en garde contre la dangerosité des fantômes lorsqu'il sont en phase "spectrale".

Toucher un de ces êtres errants, écartelé psychiquement entre le monde des vivants et celui des morts, inflige en effet de graves blessures au corps et à l'esprit ; des atteintes qui peuvent facilement mener à la mort. {% fact "phantom_touch_harms_the_living_only_when_disincarnated" %}

Il est donc indispensable de ne pas toucher (ou se laisser toucher par) un fantôme "désincarné", sauf si l'on porte des protections dûment bénites.

En revanche, les fantômes incarnés, doués de raison, sont entièrement inoffensifs, et passent à travers les êtres sans les affecter.


Des chaines spirituelles
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

les fantômes, d'une manière générale, s'éloignent peu de leur lieu de vie passé.

Mais les personnes mortes violemment peuvent se retrouver comme ancrées, emprisonnées près du lieu de leur chute, dans l'aura d'une étrange lumière sacrée. Elles ne peuvent s'incarner que près de cette lueur, bien que sous forme spectrale elles gardent une plus grande liberté - si l'on peut appeler cela ainsi. {% fact "beings_dead_violently_are_anchored" %}

Les personnes - ou même les bêtes - mortes naturellement, ne semblent pas avoir ce type de lien très localisé, et ce sont davantage des tâches inachevées ou des malédictions qui peuvent les retenir dans le monde des vivants. {% fact "beings_dead_naturally_are_not_anchored" %}

Notons qu'un fantôme ancré restera plus souvent sous forme spectrale, errante, qu'un fantôme libre de ses mouvements. {% fact "anchored_phantoms_turn_more_often_into_specters" %}


Des rituels de libération
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

De nombreux rituels sacrés permettent de chasser les fantômes, mais il est déconseillé de les utiliser sans avoir d'abord analysé la situation, car il est rare qu'un fantôme ainsi expulsé retrouve, par chance, la voie vers l'au-delà. Il en est de même des armes sacrées, qui ne sont que des formes primitives d'exorcisme, malgré leur grande utilité dans certaines situations délicates. Ne pas oublier qu'un fantôme ainsi malmené, une fois revenu, sera encore plus perturbé et désincarné qu'auparavant.

De nombreux voyants du monde spirituel évoquent le rôle d'un "psychopompe", d'un guide des âmes, qui parcourt la Terre pour ramener les fantômes vers les voies célestes. Cela expliquerait la soudaine disparition de défunts, en des lieux pourtant hantés sans relâche depuis des années. Mais cette figure énigmatique reste un sujet de vive controverse théologique.


Des périls des restes corporels
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Les personnes ayant de lourds péchés sur la conscience, en plus d'être plus promptes que les autres à devenir des fantômes, peuvent laisser des traces de ce passé dans leur dépouille mortelle. Une telle malédiction, qui se matérialise par des lueurs ou sonorités anormales, peut être très dangereuse pour un fossoyeur ou pilleur de tombe inopportun ; car elle inflige des blessures sacrées, s'il touche directement le crâne ou les ossements du défunt. {% fact "cursed_skull_and_bones_give_sacred_injuries" %}

Notons que ce sortilège peut perdurer jusque bien après le retour du fantôme au royaume des morts, exigeant ainsi l'intervention d'un désenvouteur en bonne et due forme.

{% endmacro %}
<{ phantom_knowledge_article }/>



Valeur des objets précieux
======================================

{% macro treasures_value_summary() %}

Vous connaissez bien les valeurs des pièces et pierreries.

Voici par exemple comment s'écoulaient, au meilleur prix, les éléments précieux du temps des Maupertuis.

- 1 pièce de monnaie couleur argent ou bronze vaut 1 kash (quelle que soit sa taille)
- 1 pièce en or vaut 10 kashes dans les grandes villes
- 1 petit diamant rond vaut 5 kashes dans les places marchandes de Keroskia
- 1 moyen diamant rectangulaire vaut 10 kashes sur le marché de Nimouk
- 1 grand diamant rond ou rectangulaire vaut jusqu'à 20 kashes dans les pays Axoliens
- La couleur (fumée ou non) des diamants est sans impact sur leur valeur

Noter que ces valeurs en kashes sont restées globalement constantes dans toute l'Histoire de Pangéa, jusqu'à nos jours.
{% fact "precious_objects_have_kept_same_kash_value_along_history" %}

*NOTE hors-jeu* : Pour ce qui est des bijoux précieux, leur valeur estimée est marquée sur une étiquette blanche.

{% endmacro %}
<{ treasures_value_summary }/>
