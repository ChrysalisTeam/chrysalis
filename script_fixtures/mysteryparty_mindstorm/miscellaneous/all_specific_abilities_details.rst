
{# CONTAINER OF MACROS, AUTOLOADED BY JINJA-MACROS-TAGS #}


{% macro player_possessions() %}

Votre compte à la banque de Salima :

- Argent standard : {{current_player_account}} kashes

- {{ current_player_extra_goods | default("Pas d'autres possessions", True) }}

{% endmacro %}



{% macro long_range_phone() %}
Téléphone Basse-Fréquence
    Il peut arriver que, pour des raisons naturelles ou malfaisantes, le téléphone mobile ne capte pas. Rien ne vaut, dans ce cas, d'avoir comme vous un super émetteur-récepteur miniaturisé, capable de joindre un relais téléphonique depuis n'importe où sur Pangéa. A cause de l'énorme dépense d'énergie nécessaire pour la mise en place d'une communication, ce dispositif ne pourra être utilisé que **trois fois** durant la soirée, pour joindre un unique destinataire à chaque fois. *Solliciter le maître du jeu avant de passer un appel avec ce système.*
{% endmacro %}


{% macro knownledge_of_medecine() %}
Culture Médicale
    Vous aviez commencé des études de médecine, et il ne vous en reste pas grand chose sinon une certaine connaissance du vocabulaire médical. *Demandez discrètement au maître du jeu la signification des termes médicaux techniques que vous rencontreriez.*
{% endmacro %}

{% macro __OLDIE_medical_education() %}
Culture Médicale
    Avant de vous tourner votre carrière actuelle, vous aviez passé plusieurs années en faculté de médecine. Et cela vous a marqué, suffisamment pour qu'aujourd'hui encore vous en ayez de bons restes. Vous pourrez donc déchiffrer sans grande peine le jargon des documents à thématique médicale. [Présentez au maître de jeu les documents à vous déchiffrer]
{% endmacro %}


{% macro knownledge_of_poisons() %}
Connaissance des Poisons
  Vous avez, au long des années, acquis la capacité de détecter immédiatement, au sentir ou au goûter, qu'une substance contient un poison. Vous savez dès lors de reconnaître ce toxique, et vous souvenir de ses effets sur une victime. *Demandez au maître du jeu si quelque chose que vous avez trouvé est, ou non, empoisonné (et le cas échéant, les détails du produit nocif).*

{#
.. utile pour:
  - éthanol du cidre : neurotoxique qui désinhibe, excite, anesthésie, rend dépendant, et attaque les membranes des cellules neuronales ; mais sans effet durable s'il est bu avec modération
  - liqueur apportée par enchérisseur: RAS
  - noix apportées par enchérisseur : RAS
  - médicaments de LG : digoxine, c'est un médicament mais aussi un poison
  - restes de laurier rose (oléandrine)
  - eau de muguet (si interceptée)
#}
{% endmacro %}



{% macro real_news() %}
Dépêche Presse Mondiale
    Face à votre professionnalisme en tant que reporter, votre rédac' chef vous a fait une immense faveur : vos "scoops" ne sont désormais plus soumis au processus standard de vérification, et peuvent atteindre les radios et les journaux de la planète entière en moins de 15mn. Le contrecoup de ce grand pouvoir, c'est que si vous diffusez une fausse nouvelle, votre carrière pourrait se terminer abruptement.
    Utilisez le portail Anthropia pour transmettre une telle dépêche à votre employeur.
{% endmacro %}


{% macro firewall_news() %}
Pare-feu Médiatique
    Lorsque votre enquête sur les malversations d'un notable de Faeran a commencé à aboutir, celui-ci a immédiatement demandé à ses amis de la Presse de faire des gros titres sur des "Campagnes de calomnie qui seraient en cours de montage par des adversaires envieux" ; cette information vague mais contraire vous a coupé l'herbe sous le pied, et a considérablement réduit l'impact de votre article. Vous songez à utiliser cette technique si un assaut médiatique réellement malveillant se préparait contre vous ou un de vos proches.


{% endmacro %}

{% macro fake_news() %}
Intox Presse
    Grâce à vos contacts, vous avez mis la main sur **deux codes de soumission** de l'agence des dépêches internationales. Chacun d'entre eux vous permet de diffuser une nouvelle, vraie ou fausse, qui sera immédiatement reprise par les radios et les journaux de la planète entière (quitte à être vérifiée et démentie plus tard). Pour utiliser cette capacité, il faut envoyer un message **textuel** à cette agence d'information, par tout moyen disponible.
{% endmacro %}


{% macro _____OBSOLETE_runic_translator() %}
Traducteur de Runes Yodique
    Un de vos contacts a récemment mis la main sur un prototype de traducteur portatif, développé à l'Académie d'Alifir. Cet outil, qui ressemble à un appareil photo, est capable de transcrire puis traduire n'importe quel texte d'anciennes runes yodiques que vous auriez entre les mains. *S'adresser au maître du jeu pour mettre en œuvre cette compétence.*
{# UNUSED
.. utile pour:
   - rune sur un vase : XXXXXXXXXX
   - notes dans le calepin de LG
   - livre Panorbium Fortuna
   - papiers de la boite postale de Shark (instructions du judicateur)
#}
{% endmacro %}


{% macro hypnotic_interview() %}
Interrogatoire Booléen sous Transe
    Vous maîtrisez depuis peu l'envoûtement direct. Vous pourrez donc, **une fois maximum** dans la soirée, vous isoler avec un protagoniste (joueur ou non), et l'hypnotiser. Un maître de jeu doit assister à l'entretien. Vous pourrez alors poser **maximum 3 questions** à la victime, à laquelle elle sera obligé de répondre la vérité, uniquement par "oui" ou "non" ou "je ne sais pas" ou "blocage" (quand la question est posée de telle façon qu'aucune des trois autres réponses possibles ne convient). Après cela, la victime sera libérée, elle se souviendra de l'interrogatoire mais n'aura pas d'élément pour le prouver. **Ne marche pas sur l'inspecteur Shark ni sur le Tabellion, car leur volonté d'acier les prémunit contre ce genre d'hypnose.**
{% endmacro %}


{% macro lie_detector_written_interview() %}
Papier détecteur de mensonge
    Vous disposez de **trois** bulletins d'entretien-vérité, une invention récente de votre employeur. Le principe est d'y écrire entre une et trois questions, d'y faire répondre par écrit une personne, puis de faire analyser cet entretien pour y détecter les possibles mensonges. La personne ainsi interrogée doit être informée du procédé, et consentante. *Apportez le bulletin rempli au maître de jeu, afin qu'il vous rapporte plus tard le résultat de l'analyse de vérité.*
{% endmacro %}


{% macro passcard_hacking() %}
Crochetage par Carte Passe
    Vous venez de recevoir un kit de piratage des "cartes pass", qui se répandent énormément dans Sabarim en ce moment (ces serrures ont un logo montrant une main insérant une carte magnétique). Loyd Georges est connu pour être un précurseur dans leur utilisation. *En mettant votre main à plat sur une serrure "carte pass" **pendant 10 secondes**, vous pourrez l'ouvrir. Elle se reverrouillera d'elle-même à la fermeture.*
{#
.. utile pour:
  - boite aux lettres de l'entrée (contient lettre de Loakim)
  - coffre-fort de LG
  - fermer portes intermédiaires, ex. cuisine, pour discuter ?
  # TODO trouver autres usages
#}
{% endmacro %}


{% macro new_identity_and_life() %}
Nouveau Départ
    Votre service a, par précaution, prévu tout le nécessaire pour forger une **nouvelle vie** dans Sabarim (avec visa, faux papiers d'identité, inscriptions dans des registres administratif, job d'homme de main bien rémunéré...) à quelqu'un qui en aurait besoin ; cela fonctionnera même si la personne est visée par une enquête judiciaire, sauf si elle est déjà sous les verrous (ex. si elle n'a pas pu rassembler une caution financière pour rester libre en attendant le procès). Ce nouveau départ fonctionnerait aussi pour vous (en simulant au passage votre décès).
{% endmacro %}


{% macro djinn_interview() %}
Sollicitation des Djinns
    Vos richesses vous ont permis de prépayer **trois questions** aux Djinns de Sedes Sancta, qui sont une espèce de secte indépendante, dédiée à l'accumulation de la connaissance (sur des faits anciens, ou d'actualité récente). Vous devez poser toutes vos questions lors d'un unique appel téléphonique à leur siège. Résultats non garantis, mais habituellement très satisfaisants.
{% endmacro %}


{% macro _OLDIE_fake_memory() %}
XXXX Suggestion Mémorielle
    .. Vous avez subi ces derniers jours un intense entraînement pour maîtriser la suggestion hypnotique. Vous pourrez donc, **deux fois maximum** dans la soirée, vous isoler avec un protagoniste (joueur ou non), et l'hypnotiser. Un maître de jeu doit assister à l'entretien. Vous pourrez alors édicter un événement, lointain ou récent **(mais datant d'au moins la veille)**, réel ou fictif, et la victime deviendra profondément convaincue de sa véracité, **par défaut sans limitation de durée**. Mais si ce "faux souvenir" rentre en conflit avec la logique, ou bien d'autres connaissances qu'elle a, la victime ne devra en rester dogmatiquement convaincue **que pendant 30mn** ; après quoi elle pourra prendre du recul avec cet étrange souvenir (mais toujours "façon roleplay"). Dans tous les cas, la victime ne se souviendra pas, d'elle-même, avoir été hypnotisée. **Ne marche pas sur l'inspecteur Shark, par contre, sa volonté d'acier le prémunissant contre ce genre d'hypnoses.**
{% endmacro %}


{% macro fake_alphonse_memory() %}
Suggestion Mémorielle sur Alphonse
    Vous commencez, depuis peu, à maîtriser la suggestion hypnotique ; mais elle ne marche encore qu'avec les humains faibles du ciboulot. Vous pourrez donc, **deux fois maximum** dans la soirée, vous isoler avec le vieil **Alphonse**, et l'hypnotiser. Vous pourrez alors édicter un événement, plus ou moins lointain (mais datant d'au moins la veille), réel ou fictif, et la victime deviendra profondément convaincue de sa véracité, **pendant environ 15mn** ; après quoi il ne saura plus trop quoi en penser (et ne se souviendra pas d'avoir été hypnotisé).
{% endmacro %}


{% macro anthropia_deletion() %}
Purge Anthropia
    Un indic' vous a transmis un "code de réinitialisation", permettant de supprimer TOUTES les données d'un compte Anthropia. Cette opération ne peut être annulée. Il vous suffit, pour faire cela, d'envoyer au service informatique d'Anthropia un message, ayant l'identifiant ciblé et le code spécial "VOIDIFY" quelque part dans son contenu. Tout moyen textuel est utilisable pour cela.
{% endmacro %}


{% macro mercenaries_hiring() %}
Mercenaires
    Dans le cadre de votre enquête, vous vous êtes offerts les services d'un petit gang de malfrats (6 personnes), peu organisé mais assez bourrin quand il le faut. Si vous avez besoin de leur donner une mission, il vous faudra les contacter, par quelque moyen que ce soit.
{% endmacro %}


{% macro manor_police_searches() %}
Perquisition du manoir
    La brigade criminologique, chargée de fouiller méthodiquement le manoir, a été retardée par vos supérieurs jusqu'à ce que vous soyez sur les lieux. C'est à vous d'indiquer, au fur et à mesure, quelle pièce ils devront perquisitionner, avant vous rapporter en mains propres leurs potentielles trouvailles. Une fouille prend **30 minutes** en moyenne.
    Ils auront probablement plus de succès si vous leur indiquez, à chaque fois, quoi chercher en particulier.
    La salle à manger, où se trouvent les invités, n'est pas fouillable (l'inspecteur est censé y "avoir fait un tour"), et des policiers ratissent déjà le parc du manoir ainsi que les étages.
    Les 10 salles disponibles à la fouille : **halls, bureau, bibliothèque, chambre de Loyd Georges, chambre d'Opal, chambre du vieil Alphonse, chambre de Rydji, cuisine, garde-manger, chenil**.
{% endmacro %}

{% macro pneumatic_tubes() %}
Tubes Pneumatiques
    Vous avez observé, lors d'un précédent passage chez Loyd Georges, un central de communication par tubes pneumatiques, qui bien que désuet, semble encore en état de marche. Intuitivement, vous avez donc décidé d'acheter et de garder sur vous *UN* tube, au cas où. Ce tube permettra d'envoyer à tout moment un message papier ou un petit objet vers un destinataire équipé (police, hôpital, mairie, pompiers, presse, nobles des environs...). *En cas de réponse (qui vous sera notifiée), le tube pourra être à nouveau utilisé.*
{% endmacro %}


{% macro graphological_analysis() %}
Analyseur Graphologico-Stylistique
    Ce prototype, qui ressemble à un appareil-photo, vous permet de savoir si un texte (manuscrit ou imprimé) a été écrit par la même personne qu'un autre document. Le résultat est donné avec un "pourcentage de certitude", car ce type d'analyse n'est pas une science exacte. Il peut aussi donner des indications approximatives sur l'origine et le caractère de la personne qui a écrit.
    *S'adresser au maître du jeu pour mettre en œuvre cette compétence.*
{#
.. utile pour:
   - Travaux préparatoire de physique : originaires du NALAVUT en réalité
   - Lettres de Shark à sa soeur
   - Annotation de Loyd Georges sur la recette "Blanquette de veau à la Sabarite"
   - Lettre de Waden à Loyd Georges parlant de GemmoKorps
   - Autres textes sans sceau...
#}
{% endmacro %}


{% macro document_authentication_lamp() %}
Authentification de document
    Si un document ne porte pas de "sceau infalsifiable" (signature dans un cercle) attestant de son authenticité, vous avez un chance de détecter s'il s'agit d'un vrai ou d'un faux, grâce à votre analyseur d'authenticité.
    *Avec la lampe à ultraviolets, cherchez un sceau jaune (invisible sous lumière normale) sur le document. S'il contient une lettre voyelle, il est authentique ; s'il contient une lettre consonne, ou tout autre symbole, c'est un document falsifié.*
{% endmacro %}



{% macro wireline_fax() %}
Téléphone-fax Filaire Sécurisé
    Le département de police de Sabarim a installé un téléphone-fax sécurisé dans le manoir, que seuls ses membres peuvent utiliser. Ce téléphone n'est pas impacté par le brouilleur d'ondes des téléphones mobiles, bien sûr. Les interlocuteurs se voient en vidéo, de façon assez floue.
{% endmacro %}


{% macro __OLDIE_phone_redirection() %}
Redirection Téléphonique
    Même si c'est illicite, vous avez plus d'une fois durant votre carrière, intercepté les communications d'un individu que vous suspectiez sans preuve. Et votre système d'interception est toujours opérationnel, même s'il ne marche pas avec les nouveaux téléphones dits "mobiles", même s'il ne peut détourner qu'une seule ligne à un moment donné, et même s'il ne peut être configuré qu'une seule fois par jour. [Dites au maître de jeu, pendant la partie, quel téléphone filaire vous voulez détourner, si vous en connaissez un qui vous intéresse]
{% endmacro %}


{% macro __OLDIE_manaic_retrocamera() %}
Rétrocaméra Manaïque
    Vos mentors d'Akarie viennent de vous faire parvenir un prototype d'une invention révolutionnaire : la **rétrocaméra manaïque**. Utilisable maximum 1 fois par jour (car très consommatrice en énergie), cette caméra peut reconstituer, dans l'endroit où l'on se trouve, ce qui s'est passé à une heure donnée (ex. "il y a 3 jours entre {% symbol "16h" for "" %} et {% symbol "17h" for "" %}"), tant que cela date d'au moins la veille ; le résultat est évidemment encore un peu flou, mais cette technologie pourrait bien révolutionner plus d'un domaine scientifique. S'adresser au MJ pour mettre en œuvre.
{% endmacro %}


{% macro akarith_riot() %}
Emeute Akarite
    Une carte maîtresse. Des centaines de fanatiques akarites, infiltrés en Sabarim, ont été placés sous votre commandement. Ils n'attendent qu'un signe de votre part pour se jeter corps et âme dans une mission-suicide qui puisse servir la cause des Yods. Ils ne savent pas bien se battre, mais bien utilisés, ils peuvent mener une action coup-de-poing très efficace. Pour contacter ces troupes, vous devez cependant vous absenter du manoir, pour aller les appeler via la cabine téléphonique du hameau voisin.
{% endmacro %}


