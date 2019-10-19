


{% include "missions/berserk_elixir_recipe/opal_remedy_quest.rst" %} {# BEFORE MAIN OBJECTIVES #}


<{ title_main_missions }/>
=========================================

{% macro magnus_parents_must_protect_family() %}
Protéger votre famille
    Entre les fanatiques akarites et les adversaires politiques, vos proches sont en danger. Il s'agira donc de les défendre, à n'importe quel prix.
{% endmacro %}


{% macro opal_main_objectives() %}

<{ magnus_parents_must_protect_family }/>

Sauver votre santé et celle de Loyd Georges
    Votre dernier espoir semble résider dans ce fameux "Elixir Berserk", vous espérez que Rydji et {% symbol "Rodok" for "lg_adventurer_friend_name" %} pourrons vous mettre sur sa piste... {% fact "opal_knows_about_berserk_elixir" as author %}

Aider à élucider le crime contre Loyd Georges
    Vous n'avez que moyennement confiance dans les compétences restantes du vieillissant inspecteur Shark, donc vous comptez bien enquêter un peu en parallèle, peut-être par l'intermédiaire de son adjoint de police. Surtout que, en l'absence de coupable, on pourrait finir par vous accuser, vous !

Défendre l'orbe de Loyd Georges
    Ce prodige archéologique est passé au second plan à cause des récents évènements, mais vous vous sentez un devoir de protéger l'orbe de Loyd Georges, si vaillamment récupéré, contre les agents étrangers. Seulement, vous ne savez même pas où il l'a caché...

Tacler les "purificateurs" akarites
    Vous avez une sérieuse dent contre cette secte qui a attenté à votre vie, et peut-être à celle de Loyd Georges. Donc si l'occasion se présente...

{% endmacro %}

<{ opal_main_objectives }/>





{% if not standalone %}
{% include "missions/nazur_secrets/specific_mission_briefing.rst" %}
{% endif %}

