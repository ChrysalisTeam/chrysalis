
Données communes aux serviteurs du manoir
============================================

Programme de la journée des entretiens
+++++++++++++++++++++++++++++++++++++++++++

Voici les heures d'arrivées qui furent planifiées pour les différents entretiens de la veille.

{% macro lg_interviews_planning() %}
- {% symbol "11h" for "amethyst" %} : {{character_properties.amethyst.official_name}} (Amethyst)
- {% symbol "12h" for "lg_meeting_time_for_malachite" %} : {{character_properties.malachite.official_name}} (Malachite)
- {% symbol "15h" for "lg_meeting_time_for_peridot_and_topaz" %} : {{character_properties.peridot.official_name}} (Peridot) et {{character_properties.topaz.official_name}} (Topaz)
- {% symbol "16h" for "lg_meeting_time_for_spinel" %} : {{character_properties.spinel.official_name}} (Spinel)
- {% symbol "17h" for "lg_meeting_time_for_garnet" %} : {{character_properties.garnet.official_name}} (Garnet)
{% endmacro %}

<{ lg_interviews_planning }/>



Informations diverses si enquête des joueurs
++++++++++++++++++++++++++++++++++++++++++++++++

Ces dernières semaines, Loyd Georges et son entourage ont subi de nombreuses attaques :

- deux tentatives de cambrioler le manoir {% fact 'spinel_robs_lg_manor_fail' %} {% fact 'peridot_robs_lg_manor_fail' %}
- cambriolage d'un entrepôt de Loyd Georges, heureusement vie de pièces de valeur {% fact 'malachite&spinel_rob_alifir_warehouse' %}
- tentative d'enlèvement du Professeur Loakim  {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- sans doute bien d'autres intrigues et tentatives de larcin, dont vous n'avez hélas pas eu vent...


En ce qui concerne le jour des entretiens (la veille du jour actuel) :

- Loyd Georges a reçu tôt le matin un étrange colis, dans un sac de toile brune, et l'a caché. Alphonse a gaffé en parlant de cela à Rydji devant l'inspecteur, causant par la suite une dispute entre le sir et l'inspecteur. Nul ne sait ce que Loyd Georges a fait du contenu, mais le sac en toile trainait, aux dernières nouvelles, sur une étagère de la bibliothèque. {% fact "alphonse_blunder_revealed_panorbium_fortuna_arrival" %} {% fact 'panorbium_fortuna_bag_remains_in_library' %}
- le système de surveillance a été désactivé peu après {% symbol "12h" for "first_alarm_deactivation_time" %}, mais le majordome Rydji s'en est aperçu à son retour en début d'après-midi, et l'a réactivé. Nul ne sait pourquoi cela est arrivé.
- Loyd Georges est le seul à avoir mangé de la blanquette de veau au dîner : l'inspecteur était parti, Alphonse aussi (au tripot {% symbol "La Murge de Salima" for "alphonse_alibi_bar" %}), et Rydji est végétarien.
- Une partie du dîner avait été mise de côté, et donnée par le cuisinier au chien Bedou. *Celui-ci est finalement découvert mort au fond du parc, pendant la soirée spéciale, avec la bouche et la langue enflées et irritées.*
- Peu après la découverte de Loyd georges inanimé, Rydji a vérifié qu'Opal dormait à poings fermés dans sa chambre (il ne réagissait pas du tout aux stimulis). {% fact "rydji_could_not_wake_up_opal_after_lg_troubles" %}
- les poubelles ont été vidées par les services municipaux le lendemain matin, très tôt.


Loyd Georges prenait quotidiennement de la Digoxine au coucher, pour ses problèmes de rythme cardiaque. Le mémo d'instructions laissé au mur pour Robb Barrow le mentionne correctement, mais c'est de toute façon le majordome qui a effectué le dosage, comme à son habitude.

LG était il-allergique à quelque chose ? Oui, à la poussière et aux foins, mais pas d'allergie alimentaire connue (ainsi les arachides apportées sont hors de cause).

Baignant depuis longtemps dans l'archéologie de Loyd Georges, vous savez que la **bague à tête de mort** de l'ambassadeur akarite est typique des {% symbol "hauteurs de Kéroskia" for "akarith_ambassador_skull_ring_origin" %}. L'autre est plus commune.


Mémo pharmacologique des toxiques cardiaques
+++++++++++++++++++++++++++++++++++++++++++++

*Ce mémo sert, pour les serviteurs, à répondre aux questions des convives, si on leur demande des précisions sur les symptomes de Loyd Georges la veille (dus à un empoisonnement à l'oléandrine), sur son traitement médical pour sa tachycardie...*

Les deux molécules suivantes ont une action similaire, à savoir renforcer la contraction cardiaque, ralentir et régulariser les mouvements du cœur. On les utilise donc dans le traitement de diverses affections du cœur, dont l'insuffisance cardiaque.

- La digoxine est un glycoside cardiotonique extrait de la feuille de digitale laineuse.
- La digitoxine ou digitaline ou digitoxoside est un glycoside cardiotonique extrait de la digitale pourpre (Digitalis purpurea) et de la digitale laineuse (Digitalis lanata).

Autre plantes entrainant une bradycardie (rythme cardiaque trop bas) : Chélidoine, Hellébore, Muguet, et l’oléandrine contenue dans le laurier rose.

Les divers troubles causés par l’oléandrine du laurier rose :

- Cardio-respiratoires : troubles de la fréquence cardiaque engendrant une alternance d’accélérations (tachycardie) et de ralentissements (bradycardie) anormaux de cette fréquence
- Digestifs : une perte d’appétit, une diarrhée parfois hémorragique, des coliques
- Nerveux : prostration, tremblements musculaires, convulsions, coma
- Dermatologiques : Sudation importante, extrémités froides
- Psychiques : confusion, troubles de la vision (phosphènes), obnubilation (apathie)
- Oculaires: pupilles dilatées (mydriase)

Mais l'oléandrine ne donne pas les symptômes suivants, qui sont spécifiques à d’autres poisons :

- taches violettes sur le corps et la langue

