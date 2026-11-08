

{% include "missions/transfiliation_attempt/generic_mission_title_en.rst" %}


Agents,

our Duke is in desperate straits, because his plan to "merge" the Dorian Dukedom with Akaris is not going quite as planned.

Indeed, a secret Akarith council is soon to be held, and the dogma of "transfiliation" will notably be on the agenda.
If this dogma, which is defended tooth and nail by the Akarith High Judicators and our Duke, is rejected by the religious leaders of the various Akarith clans, this will bring the diplomatic negotiations to a dead end. Indeed, the Akariths will then no longer be able to regard the Dorians as their equals, "Chosen of the Yods". They will be their slaves, or their enemies.

But **the Akarith Archdeacon Baazel**, who is a fervent defender of transfiliation, has proclaimed that he would prove the rectitude of the Faith of the Dorians converted to their "Yodic" religion. To this end, he has proposed to his opponents that they call, during the council, one of these foreigners faithful to the Yods, and test his religious convictions. And your duo has been chosen as the "interlocutor drawn by lot".

It will fall to you to answer the telephone call made by the Akarith council. Swot up on Yodic theology and the quotes below, taking care not to mix up what the Akarith Judicators consider "orthodox" and what they consider "heretical", because things have changed a great deal over the centuries in this field.

You also have authority as **negotiators**, to find common ground that suits all the Akarith clans and the Dorians, in case the council is not convinced by this demonstration of doctrinal purity.

I must however warn you that it is with a heavy heart that I give you these missions; a wind of bitterness is indeed blowing among the Dorian population, which is beginning to regard our Duke's manoeuvres no longer as cautious diplomacy, but as submission, or even treason towards our former Masslavian and Heliossarian allies. I do not know what the new terms for the Dorians will be, but they will have to be compared with the default solution, that is to say a terrible war against the Akariths, alongside the other non-Akarith states.

Note that the outcome of all this will also depend on the other speakers who will testify before the council. It has thus leaked that **Prof. Schaladuk**, an expatriate Akarith sociologist living in Doria, could be asked to give his opinion on what the Dorians generally think of Akarith worship; and his answer is hard to predict.


*Colonel Der'Ham, Head of the Dorian Secret Services*


{% macro yodic_theology_simple_version() %}

Doctrinal Summaries
++++++++++++++++++++++

{{static_pages.yodic_theology.content|replace('=', '-')|replace('#', '+')|replace('image::', 'brokenimage')|replace('**Un ', '.. ')|replace('[BR]', '')}}

Yodic Quotes
++++++++++++++++++++

{{static_pages.yodic_quotes.content|replace('=', '-')|replace('#', '+')|replace('image::', 'brokenimage')|replace('**Un ', '.. ')|replace('[BR]', '')}}

{% endmacro %}

<{ yodic_theology_simple_version }/>
