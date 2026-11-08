

<{ title_previous_day }/>
==============================

{% macro peridot_and_topaz_lg_encounter() %}

Your investigation had been stalling for a few days, and you were about to go for a drink at the local pub to see whether inspiration would strike, when Loyd Georges offers you a one-to-one interview, announcing that he has "important information" to share with you. This is more than you could have hoped for.

As your colleague – or rather, his cover – has also been invited to an interview on his side, you decide to show up together, building a story of friendship "à la Orestes and Pylades" between you; these ancient mythologies are, after all, very fashionable among the elites of Sabarim. **You therefore go to your host's for {% symbol "15:00" for "lg_meeting_time_for_peridot_topaz" %}.**

<{ arrival_at_manor_with_butler }/>

Loyd Georges receives you in his study. Initially rather sullen, and a little groggy from digestion, he falls completely for your historico-mythological jargon, and even though you often feel like you are walking on thin air, you manage to impress him with a few well-prepared anecdotes.

Calling you "friends", he confesses to feeling surrounded by spies, and to taking it very badly. He actually had no important information to share with you, and only wanted to meet you to put you to the test. He admits, however, to being very uncomfortable in this role of interrogator, and to having doubts about his ability to extract information from anyone at all.

You can sense that this idea of a "test" was not his own. You try to get him talking, but, despite the trust gained, he remains guarded.
{% if standalone %}
At most he confesses to you that he found a magnificent jewel in the buried temple, a jewel he prefers to keep hidden until things settle down. That does not get you very far...
{% else %}
He does end up confessing to you, nevertheless, that he owned an orb, which has been stolen.
Plague take it... to your knowledge, it has not reappeared on the black market, and the Akariths have not been crowing, which they would not have failed to do had they recovered one of the three orbs they await like the messiah; a foreign power must therefore have got hold of it, but which one? Masslavia, Heliossar, Lordania...?
{% endif %}

At the end of the interview, just before 16:00, the butler firmly escorts you back to the entrance gate.

You both spend the evening, until very late, in a trendy Salima club, the {% symbol "Luxor Excelcis" for "peridot_topaz_alibi_club_name" %}; even treating yourselves to the luxury of striking up a trio with the opera singer during an interlude.  {% fact "peridot_topaz_alibi_is_strong" as author %}

<{ default_previous_day_ending }/>

{% endmacro %}
<{ peridot_and_topaz_lg_encounter }/>
