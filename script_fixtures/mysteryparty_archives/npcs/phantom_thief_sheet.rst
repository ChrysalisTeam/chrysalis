Fantôme - Le voleur {% symbol "Fédore Pass’muraille" for "thief_name" %}
#####################################################

Votre histoire
=======================

Votre profil
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

{# BEWARE - NO COMMON TRAGEDY OR LORE KNOWLEDGE FOR THIS NPC #}

<{ phantom_thief_character_summary }/>


Informations et instructions spécifiques
========================================

Etant en mauvaise posture dans votre quête du trésor, vous avez décidé de monnayer cher vos informations aux autres explorateurs de cette bibliothèque, quitte à ce qu'ils trouvent avant vous.

Vous savez ne plus réussir à prendre en main des richesses, mais pour éviter d'être cambriolé pendant vos "absences", vous exigez que les paiements soient faits dans votre **{% symbol 'pochette sans fond' for 'thief_moneybox_name' %}**, une sorte de tirelire magique, qu'ils doivent d'abord retrouver pour vous. {% hint "thief_moneybox" is needed %}

Important : vous devez **vider** en hors-jeu cette pochette chaque fois que vous vous promenez en spectre.


**Informations à revendre**

- Vous aviez mis la main sur un précieux coffret à bijoux ayant appartenu à la jeune {% symbol "Isadora" for "maupertuis_mother" %}, la future mère d'Octave ; personne n'avait réussi à l'ouvrir, mais votre talent auditif vous a permis de découvir le nombre attendu par les engrenages : **{% symbol "159" for "maupertuis_mother_thanatologue_chest_code" %}**. Avec un peu de chance, elle a continué à utilisé ce code pour protéger d'autres secrets.  **PRIX : 160 kashes** {% fact "thief_knows_about_isadora_thanatologue_chest_code" %} {% hint 'isadora_code_for_thanatologue_chest_code' is provided %}

- Vous savez que la broche en laiton de Mérédice de Maupertuis, évoquée dans les souvenirs de certains de ses descendants, était une pièce importante pour avoir accès au trésor ; elle laissait cette broche dans son petit bureau d'études d'occultisme, qui trônait **dans le coin du domaine interdit, par delà le laboratoire d'alchimie**. {% fact "thief_knows_about_location_of_maupertuis_daughter_jewel" %}. **PRIX : 160 kashes**.

- La formule magique pour activer votre {% symbol 'astrolabe de téléportation' for 'thief_teleportation_device_name' %} est **"Astrolabe, transporte moi là-bas"** {% fact "thief_knows_teleportation_device_formula" %}. Il peut téléporter jusqu'à {% symbol '3 personnes' for 'thief_teleportation_device_simultaneous_limit' %} à la fois, du moment qu'elles tiennent chacune l'un de ses pieds. On peut l'utiliser autant de fois qu'on veut, mais vous prévenez qu'il faut attendre {% symbol '30 secondes' for 'thief_teleportation_device_cooldown' %} entre chaque téléportation. **PRIX : 200 kashes**


{# LATER indice pour la quete de la potion de guérison #}


Estimation des monnaies et gemmes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Vous connaissez bien la valeur des pièces et pierreries, ainsi que les meilleurs endroits pour les écouler à **meilleur prix**.
Bien entendu, lorsque vous négociez, vous sous-estimez systématiquement de **20%** les richesses que l'on vous apporte, et escroquez ainsi ceux qui ne s'y connaissent pas. Mais face à un expert en estimation de biens, vous vous inclinez.

<{ treasures_value_summary }/>


