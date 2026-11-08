

<{ title_previous_day }/>
==============================

{% macro peridot_and_topaz_lg_encounter() %}

Votre enquête piétinait depuis quelques jours, et vous étiez sur le point d’aller boire un coup au pub du coin pour voir si l’inspiration vous venait, quand Loyd Georges vous propose un entretien en tête-à-tête, annonçant avoir des "informations importantes" à vous communiquer. Voilà qui est inespéré.

Comme votre collègue – ou plutôt, sa couverture – a également été convié de son côté à un entretien, vous décidez de vous présenter tous les deux, en construisant une histoire d’amitié "à la Oreste et Pilade" entre vous ; ces anciennes mythologies sont, après tout, très à la mode chez les élites de Sabarim. **Vous vous rendez donc chez votre hôte pour {% symbol "15h" for "lg_meeting_time_for_peridot_topaz" %}.**

<{ arrival_at_manor_with_butler }/>

Loyd Georges vous reçoit dans son bureau. Initialement assez maussade, et un peu sonné par la digestion, il marche à fond dans votre jargon historico-mythologique, et même si vous avez souvent le sentiment de marcher dans le vide, vous arrivez à l’impressionner avec quelques anecdotes bien préparées.

Vous appelant "amis", il vous avoue se sentir entouré d’espions, et très mal le vivre. Il n’avait en fait aucune information importante à vous communiquer, et n’a voulu vous rencontrer que pour vous mettre à l’épreuve. Il admet cependant être très mal à l’aise dans ce rôle d’interrogateur, et avoir des doutes sur sa capacité à soutirer des informations à qui que ce soir.

Vous sentez bien que cette idée de "mise à l’épreuve" n’était pas de lui. Vous cherchez à le faire parler, mais, malgré la confiance acquise, il reste sur la réserve.
{% if standalone %}
Tout au plus vous avoue-t-il qu'il a trouvé un joyau magnifique dans le temple enfoui, joyau qu'il préfère garder caché jusqu'à ce que les choses se tassent. Voilà qui ne vous avance pas beaucoup...
{% else %}
Il finit tout de même par vous avouer qu'il possédait un orbe, qui a été volé.
Malepeste… à votre connaissance, il n’est pas reparu sur le marché noir, et les akarites n’ont pas plastronné, ce qu’ils n’auraient manqué de faire s’ils avaient retrouvé l’un des trois orbes qu’ils attendent comme le messie ; une puissance étrangère a donc dû le récupérer, mais laquelle ? Masslavie, Héliossar, Lordanie...?
{% endif %}

A la fin de l'entretien, juste avant 16h, le majordome vous raccompagne d'un pas ferme jusqu'au portail d'entrée.

Vous passez tous deux la soirée, jusque très tard, dans un club branché de Salima, le {% symbol "Luxor Excelcis" for "peridot_topaz_alibi_club_name" %} ; en vous payant même le luxe d'entonner un trio avec la cantatrice durant un interlude.  {% fact "peridot_topaz_alibi_is_strong" as author %}

<{ default_previous_day_ending }/>

{% endmacro %}
<{ peridot_and_topaz_lg_encounter }/>
