
<{ diakon_group_sheet }/>

Vos compétences
====================================

<{ diakon_sheet_intro }/>

Mais votre vocation s'est rapidement imposée à vous : exorciste, c'est-à-dire celui qui connait le monde des esprits et ses règles, et dispose de divers rituels pour le contrer.

Reportez-vous à **l'article en annexe** pour une description détaillée du monde des morts ; des connaissances que vous pourrez théâtralement enseigner à vos alliés au cours du jeu, lorsque le sujet se présentera.


Les rituels d'exorcisme
+++++++++++++++++++++++++++++++++++++++++++++++

Vos rituels exigent des artefacts, des gestuelles, des invocations, et parfois l'usage de potions en soutien de votre force psychique.

*NOTE hors-jeu : n'hésitez pas à simuler l'épuisement que vous procurent les plus exigeants de ces rituels d'exorcisme, quitte à vous effondrer à genoux après l'un d'eux.*

Vous aviez emporté dans vos poches des **Potions de Charme et de Focus** pour vos rituels habituels ; vous possédiez aussi **une dose de Lotion de Révélation**, confiée avec une mystérieuse insistance par l'oracle du monastère.
Cependant, par mégarde, vous les avez **fait tomber** à un moment - difficile de savoir si c'était avant ou après le saut à travers le portail magique. Diantre. Mais peut-être trouverez-vous sur place de quoi vous réapprovisionner, de toute façon.
{% hint 'potion_of_focus_from_exorcist' is needed %} {% hint 'potion_of_charm_from_exorcist' is needed %} {% hint "potion_of_revelation_from_exorcist" is needed %} {% fact "diakon_exorcist_lost_potions_bag_found_by_lockpicker" %}
{% macro phantom_related_spells() %}


Bénédiction d'arme
-----------------------------------------

Vous êtes capable de bénir une arme de poing, ou une munition (flèche, balle...), pour quelle ait prise sur les entités du monde des morts.
Les armes ainsi sacrées ne peuvent bien sûr pas réellement blesser ou tuer des êtres qui sont déjà morts ; mais par les impacts mystiques qu'ils infligent, elles peuvent chasser des fantômes agressifs, et atténuer leur lien au monde des vivants ; ce dernier effet les condamne à passer une plus grande proportion de temps sous forme spectrale, entre deux incarnations. {% fact "diakon_exorcist_can_bless_parcival_woodsman_arrows" %}

Cette bénédiction ne fonctionne que sur les métaux nobles : **Paladium, Iridium, Platine, ou Mithril**.

Rituel :

- Prendre une gorgée de Philtre de Focus {% hint "potion_of_focus_from_exorcist" is needed %}
- Imposer les mains sur l'arme de poing ou la munition présentée
- Clamer **"Armement qui blesses la chair, blesse aussi l'âme"** {# (ou bien la version latine : "Tu et caro dolet, et anima nocere") #}


Expulsion d'esprit
-----------------------------------------

Vous êtes capable de chasser une créature du monde des morts, pour la faire sortir d'un corps possédé, ou juste l'envoyer loin de vous ; cela la fait systématiquement repasser sous forme spectrale, non incarnée, si elle ne l'était pas déjà (mais pendant quelques minutes uniquement). L'esprit ainsi chassé va fuir au hasard, en évitant le lieu d'où il a été chassé, mais sans pouvoir traverser pour autant les possibles barrières spirituelles qui le retiendraient habituellement lorsqu'il est en spectre. {% fact "diakon_exorcist_can_chase_away_beast_temporarily" %}

Cet exorcisme étant épuisant psychiquement pour vous, vous ne pouvez le réaliser qu'une fois toutes les **{% symbol "10 minutes" for "phantom_eviction_cooldown" %}**. Il ne touche qu'un seul esprit par invocation.

Rituel :

- Lever les bras vers le ciel, paumes face au fantôme
- Crier **"Par {% symbol "Bahamoot" for "god_of_diakons" %}, arrière, esprit errant"** {# (ou bien la version latine : "Vade retro, mali spiritus OUDATED") #}


Charme d'esprit
-----------------------------------------

Vous êtes capable de charmer une créature du monde des morts, qu'elle soit sous forme incarnée ou spectrale ; elle ne change pas de forme, en revanche elle est irrésistiblement attirée par vous pendant 30 secondes, mais se déplace particulièrement lentement. Cela ne lui permet cependant pas de passer à travers les obstacles qui la bloqueraient habituellement. {% fact "diakon_exorcist_can_attract_slowed_beast_temporarily" %}

Cet exorcisme étant épuisant psychiquement pour vous, vous ne pouvez le réaliser qu'une fois toutes les **{% symbol "10 minutes" for "phantom_charm_cooldown" %}**. Il ne touche qu'un seul esprit par invocation.

Rituel :

- Prendre une gorgée de Potion de Charme {% hint "potion_of_charm_from_exorcist" is needed %}
- Mettre les bras croisés sur votre coeur
- Crier **"Par {% symbol "Bahamoot" for "god_of_diakons" %}, lambine vers moi, esprit errant"** {# (ou bien la version latine : "Venite ad me errantes spiritu") #}


Libération d'ancrage spirituel
-----------------------------------------

Si vous rencontrez un fantôme bloqué dans une petite zone - typiquement le lieu de sa mort violente - lorsqu'il est sous forme incarnée, ce rituel vous permet de le libérer de cette chaine invisible. Comme tous les fantômes, il restera néanmoins par la suite soumis aux contraintes d'un possible {% symbol "Sceau de barrage absolu" for "ultimate_seal_name" %}, ou autre sortilège contraignant, dressé sur sa route.

Rituel :

- Rassembler **2 autres {% symbol "initiés" for "ritualist_kind_name" %}**, en plus de vous, en cercle autour du fantôme incarné
- Se mettre tous les trois avec les bras étendus à l'horizontale
- Clamer tous ensemble **"Esprit errant, nous brisons les chaines qui te retiennent"**, trois fois d'affilée

D'après la littérature mystique, un fantôme ainsi libéré de ses chaines spirituelles passera moins souvent dans sa forme spectrale. {% fact "anchored_phantoms_turn_more_often_into_specters" %}

**Annulation** : n'importe lequel des initiés qui ont participé au rituel peut, tant que le fantôme n'est pas passé dans l'au-delà, restaurer la chaine invisible qui l'attachait à un point précis. Il suffit de tendre les paumes ouvertes vers le fantôme incarné, et de clamer **"Esprit errant, je restaure les chaines qui te retenaient"**. Le fantôme va alors retourner à son emplacement initial d'attache. {% fact "diakons_can_all_anchor_phantoms" %}

{% endmacro %}
<{ phantom_related_spells }/>


Rupture globale de corridor d'outre-monde
------------------------------------------

Vous êtes capable de couper les passerelles existant entre des mondes disjoints, tels les portails que certains sorciers ouvrent vers le monde des esprits, ou vers d'autres mondes parallèles. {% fact "diakon_exorcist_knows_how_to_expel_avatars" %}

Les plus grands mystiques sont capables de procéder à cette rupture sélectivement, en ne rompant qu'un seul corridor - attaché à un objet spécifique - à la fois. Mais votre exorcisme est un peu plus sommaire, et va anéantir tous les points d'attache inter-monde qui se situent dans un rayon de 100 pas autour de vous.

Rituel :

- Utiliser un {% symbol "pentacle canonique (étoile à 5 branches dans un cercle)" for "standard_pentacle_description" %} activé
- Placer au centre de ce pentacle le maximum d'objets attachés aux corridors outre-monde (talismans maudits, livres d'avatars...)
- La présence d'{% symbol "initiés" for "ritualist_kind_name" %} supplémentaires autour du pentacle est conseillée, mais pas indispensable
- Tendre le bras droit vers le portail, les doigts bien écartés
- Clamer en boucle cette incantation : **"Par le soleil victorieux, Par le pouvoir des cieux, Portails disparaissez"** pendant au moins **30 secondes**
- Il est important de rester bien **immobile** pendant l'incantation, sans quoi le pentacle peut être déstabilisé (il s'éteint brièvement) et cela retarde la finalisation du rituel

Attention, cet exorcisme ne fonctionne sans problèmes que si toutes les entités qui sont venues en ce monde par un des corridors présents sont **retournées** dans leur monde, ou à défaut sont placées **dans** le pentacle. Sans cela, le ritualiste rencontrera une résistance mystique, et l'invocation ne sera pas résolue au bout du temps habituel. Si l'officiant continue alors son invocation pendant **30 secondes supplémentaires**, cela forcera la finalisation du rituel, mais avec la conséquence dramatique de **"tuer"** lesdites entités d'outre-monde encore présentes ; quoi que cela signifie concrètement, tant cette situation est contre-nature.
{% fact "diakon_exorcist_might_kill_remaining_avatars_with_expulsion_ritual" %}

{# WRONG Notez qu'il est possible, en une seule invocation, de briser plusieurs corridors d'outre-monde à la fois, mais il faut pour cela placer les objets liés à chacun de ces corridors dans le pentacle, et surtout avoir autant de diacres participant au gestes rituels et incantations qu'il n'y a de corridors à fermer.
 OUTDATED clamer "Portail vers d'autres mondes, je t'en conjure, ferme ton seuil à jamais" en répétition pendant 30 secondes, les bras levés (ou bien la version latine : "Porta ad alios mundos, sigillum tuum limen") #}



Vos connaissances sur les différents types de blessures
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Vous savez qu'il existe différents types de blessures, parfois naturelles, parfois surnaturelles, mais l'enseignement que vous deviez suivre à ce sujet a été maintes fois repoussé... si bien que vous en êtes pour l'instant réduit à solliciter vos confrères lorsqu'une personne de votre entourage se fait blesser par un esprit errant. Un comble pour un exorciste ! 



Encyclopédie du monde des esprits
===================================================================

<{ phantom_knowledge_article }/>


