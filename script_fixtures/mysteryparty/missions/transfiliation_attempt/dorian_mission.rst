

{% include "missions/transfiliation_attempt/generic_mission_title.rst" %}


Agents,

notre duc est aux abois, car son plan consistant à faire "fusionner" le Duché Dorien avec l'Akarie ne se déroule pas tout à fait comme prévu.

En effet, un concile secret akarite doit bientôt se dérouler, et il y sera notamment question du dogme de la "transfiliation".
Si ce dogme, qui est défendu bec et ongles par les hauts-judicateurs akarites et notre Duc, est rejeté par les chefs religieux des différents clans akarites, cela mettra dans l'impasse les négociations diplomatiques. En effet, les doriens ne pourront alors plus être considérés par les akarites comme leurs égaux, "élus des Yods". Ils seront leurs esclaves, ou leurs ennemis.

Mais **l'archidiacre akarite Baazel**, qui est un fervent défenseur de la transfiliation, a proclamé qu'il prouverait la rectitude de la Foi des doriens convertis à leur religion "yodique". Il a pour cela proposé à ses opposants d'appeler, pendant le concile, un de ces étrangers fidèles aux Yods, et de tester ses convictions religieuses. Et votre duo a été choisi comme "interlocuteur tiré au sort".

C'est à vous qu'il reviendra de répondre à l'appel téléphonique émis par le concile akarite. Potassez la théologie yodique et les citations ci-dessous, en prenant garde à ne pas mélanger ce que les judicateurs akarites considèrent comme "orthodoxe", et ce qu'ils considèrent comme "hérétique", car les choses ont bien changé au cours des siècles, dans ce domaine.

Vous avez aussi autorité comme **négociateurs**, pour trouver un terrain d'entente qui convienne à tous les clans akarites et aux doriens, au cas où le concile ne serait pas convaincu par cette démonstration de pureté doctrinale.

Je dois cependant vous prévenir que c'est à contrecœur que je vous donne ces missions ; un vent d'amertume souffle en effet parmi la population dorienne, qui commence à considérer les manœuvres de notre Duc non plus comme de la diplomatie prudente, mais comme de la soumission, voire de la trahison envers nos anciens alliés masslaves et héliossars. Je ne sais pas quelles seront les nouvelles conditions des doriens, mais il faudra comparer cela à la solution par défaut, c'est à dire une terrible guerre contre les akarites, au côté des autres états non-akarites.

Notez que l'issue de tout ceci dépendra aussi des autres orateurs qui témoigneront devant le concile. Il a ainsi fuité que le **Pr Schaladuk**, sociologue akarite expatrié en Dorie, pourrait être sollicité pour donner son avis sur ce que les doriens pensent généralement du culte akarite ; et difficile de présager de sa réponse.


*Colonel Der'Ham, Chef des Services Secrets Doriens*


{% macro yodic_theology_simple_version() %}

Résumés Doctrinaux
++++++++++++++++++++++

{{static_pages.yodic_theology.content|replace('=', '-')|replace('#', '+')|replace('image::', 'brokenimage')|replace('**Un ', '.. ')|replace('[BR]', '')}}

Citations Yodiques
++++++++++++++++++++

{{static_pages.yodic_quotes.content|replace('=', '-')|replace('#', '+')|replace('image::', 'brokenimage')|replace('**Un ', '.. ')|replace('[BR]', '')}}

{% endmacro %}

<{ yodic_theology_simple_version }/>
