SUMMARY OF NPC SPEECHES
==============================================

INTRODUCTION TO THE GAME (by the Game Master)
---------------------------------------------------

**I invite you to close your eyes**

You have come a long way, you have overcome many obstacles,
to reach the portal leading to the Maupertuis secret archives.

There, you awakened a magic present since time immemorial.
Here you are, weightless, sucked in by a whirlwind towards the depths of the earth.

But in the midst of this tumult, you glimpse other silhouettes around you, **open your eyes wide**!
You do not know what brings these people here, but one thing is certain: today, destiny has brought you together.

You recognise Diakons, by their purple stole
You recognise archaeologists, by their beige belt
You recognise soldiers, by their green armband
And finally, the famous Parcival lineage, by their blue jabot

But suddenly, one of you has a deep intuition!

You feel a jolt, everything blurs... and here you are in the Maupertuis sanctuary.



BUFFET OPENING (by the Inventor avatar)
---------------------------------------------------

{% macro buffet_opening_speech() %}

::

    Onward, automatons, dust off,  prepare, welcome, make it shine!
    Let your pistons push, let your gears turn, for this most important day of the year
    Serve the dishes and the wines to the guests for the most solemn of anniversaries
    The one on which we remember the end of the finest of eras

    Let us hasten, let us feast, let us dance, at the Otherworld Buffet
    Let us no longer stay moaning, prostrate beside these tombs
    O my companions in joy and in sorrow, how I wish that today would bring an end
    To our rage and our tears in the face of so cruel a fate

    But what do I see, what do I hear, this time we have other guests?
    Could it be that our centuries-old wishes have at last been granted?
    My heart would so love to believe it, but my mind is waiting to see...


Alternative version in alexandrines (by Cyck du Clivra):

::

    My dearest automatons, prepare, make it shine!
    Let your pistons and your gears push on this year
    This buffet of dishes and wines is offered to us
    Let us celebrate the most solemn of anniversaries

    Let us hasten, feast, and dance for the otherworld
    Let us no longer linger beside these tombs
    My companions, I wish that today would bring an end
    To tears and despair in the face of a cruel fate

    Let us welcome without further delay our guests,
    May by their great talent our wishes be granted
    My heart would love to believe it but my mind awaits
    That our poor souls be released from torment


After the music:

::

    Ladies and gentlemen, living people of Pangea, I bid you welcome to the Otherworld Buffet!

If the laden buffet is not already visible, the Inventor can make it appear with a simple formula such as **"My stomach rumbles, my throat runs dry, O table, fill me up!"**. {% fact "buffet_table_magically_generates_food" %}

{% endmacro %}
<{ buffet_opening_speech }/>


MISSION CONFESSION (by the Arkon phantom)
----------------------------------------------------------

{% macro arkon_mission_report_speech() %}

500 years before this day, as I was meditating at the Rochesombre Monastery, I sensed the presence of uprooted spirits, near the ruins of the Maupertuis manor.

I passed through the teleportation portal, and in this buried library, I met Octave and the Archivist. But they were not alone.

At their side were unnatural incarnations, come from the imaginary worlds.

I convinced them to return forever to their universes, so as not to upset the balance of all things.

They agreed. So I began the ritual to rupture the otherworld corridors.

But a tragedy occurred. I was attacked by an apocalyptic monstrosity. It withstood everything, my weapons, my magic, my exorcisms. I fought, I prayed, in vain. When it struck me in the forehead, I knew that my hour had come.

So, with my dying breath, I dared a forbidden spell. I deployed an Absolute Enclosure around the library, an impassable moat for the living as for the dead, for the just as for the unjust.

And since that day, I wait. I wait for humanity to send what is needed to rid the world of this demon, and thus put an end to the curse that I myself unleashed.

I shall bear before the Yods the weight of my errors and my faults.

But today it is to you, my confessor, that I entrust myself to finish what I began...

{% endmacro %}
<{ arkon_mission_report_speech }/>

.. raw:: pdf

   PageBreak

CASSANDRA'S PROPHECY (by a female NPC actor)
------------------------------------------------

*This speech is usually delivered by a pre-recorded hologram.*

Children, listen to me.

I am Cassandra, distant granddaughter of the Dark Magus, and prophetess of the tutelary deities of Pangea.

Since my childhood I have never ceased to warn of the terrible dangers that this library represented; less because of its bewitched artefacts, than because of the magical auras that have been piling up here for centuries. Auras which, misdirected, could rip open the sacred frontiers separating the different universes.

However, out of incredulity, out of cowardice, out of laziness, all refused to listen to me.

But there is no need to hope in order to undertake, nor to succeed in order to persevere.
At the twilight of my life, I therefore bequeath to you, future generations, these final omens.

Catastrophes are under way, which nothing can stop any more.
And one day, children, you will find yourselves facing the greatest threat this planet has ever seen arise.

Keep a cool head, know how to keep your distance from a monstrosity you could not defeat.

But when the last battle is on the horizon, become builders; the builders of the most unshakeable warrior who has ever existed. May he fear neither weapons, nor poisons, nor spells. May he stand firm in the face of the storm, while he leads the ultimate invocation of expulsion.

Stay on your guard, children. Glory is found only in perils, success is found only in the union of forces, but a traitor is found only among one's friends.


FAREWELL TO THE PLAYERS (by the phantom Octave)
----------------------------------------------------------

{% macro octave_epilogue_speech() %}

*The epilogue takes place when, one way or another, the enclosure of the library has been broken; the phantoms can then finally pass on to the afterlife.*

*At the start of the epilogue music, Octave, wearing his wings, openly rejoices at being able to soon see his family again. When the singer's voice begins at 1:12, he dashes up the stairs, stops dead halfway, turns back, and bids farewell to the various groups of players, at full speed, until 1:39; then, as the music grows in intensity, Octave dashes to the top of the stairs calling out to his parents, and disappears; he is soon followed by the other phantoms, winged too.*

*Below is an example of a farewell speech, to be adapted of course if some teams have not succeeded in their quest. No pre-recorded version for this speech, as it must remain very spontaneous and natural.*

My friends the Diakons, I thank you for all you have done for us; may you always fight the demonic forces well, and above all never again burn manors that have done you no harm!

My friends the Mirandian soldiers, I am glad that our magic mill will go on serving a fine cause, and I hope that with it, you will be able to go on living in peace on your island, for as long as the sun shines!

My friends the Heliossarian explorers, I am counting on you to thwart the Akariths' insane plans, with my ancestor's ring. The legions of undead had better watch out!

Finally, my great-great-great-grandnephews and grandnieces the Parcivals, it has been an immense joy to make your acquaintance. Take good care of your sister {% symbol "Philomène" for "parcival_sick_child_name" %}, and perpetuate for a long time, forever, the wisdom of our noble lineage!


{% endmacro %}
<{ octave_epilogue_speech }/>


