
<{ title_previous_day }/>
==============================

Your investigation had been stalling for a few days, and you were about to provoke an encounter with an enemy agent, to get things moving, when Loyd Georges offered you a one-to-one interview, announcing that he had "important information" to share with you. **So you go to the manor, when the day comes, at {% symbol "11:00" for "lg_meeting_time_for_amethyst" %}.**

{% macro arrival_at_manor_with_butler() %}
The heavy gate of the grounds opens slowly, then slams shut behind you. A pot-bellied Salimian gendarme reluctantly steps out of his wide sentry box, checks your papers, and puts you through a weapons detector. Loyd Georges' butler, Rydji, then comes to meet you.

As you enter the manor's magnificent Great Hall, you immediately notice the camera watching over the whole room. That never makes anything simpler. There does not seem to be one in the small hall, but how many others are scattered throughout the mansion, or even the grounds?
{% endmacro %}
<{ arrival_at_manor_with_butler }/>

You promptly meet Loyd Georges in his study. He seems tense! You do your best to put him at ease, and the bottle of digestive liqueur you offer him is a step in the right direction; it is a foreign liqueur that caught your eye in Salima's large shopping arcade, as it boasts an amusing blue colour, and an old-fashioned wax-sealed stopper. Loyd Georges promises to open it in your honour at the meal. {% fact 'amethyst_offers_liquor_to_lg' as author %}

You enquire about this famous "information" he has for you.
After clumsily trying to answer your questions with other questions (about your travels, about your collections of antiques and gemstones...), the sir gets muddled up, and confesses to you that he has no revelation for you, but that he mainly wanted to know more about who he was dealing with. You laugh with him about how badly he is going about it, to which he replies that indeed, a career in the Sabarith police would have been a very bad idea for him.

You then try to get him talking about his recent discoveries; he briefly recounts his expedition and the myth of the Orbs, but he seems to be unaware of the Orbs' real effect, if there is one. He half-admits to having held one in his own hands, but your attempts to push him in that direction only make him suspicious...

After this cordial but unproductive interview, at around 11:45, Loyd Georges calls the butler to see you out.
You put your leather gloves back on. This interview is about to leave a bitter taste in your mouth. You could not get into the manor at night, because of the Dantesque protections of the perimeter wall, and you would walk out today without a single tangible clue? Not a chance! Time to improvise.

The butler walks you back across the grounds to the guard post. You then call out to the gendarme on duty, claiming that "the more you think about it, the more certain you are that you have seen him somewhere before; weren't you at university together?". The butler goes off about his business, and for a few minutes you keep up a chaotic conversation, which you steer towards the unfathomable subtleties of pre-tectonic pottery from Keroskia. In the end, your unfortunate interlocutor is slumped in his sentry box, with a single plea in his eyes: "get out of here and leave me alone". You pretend to be running late, and briskly step out, asking him to open the gate. The heavy metal door closes again, with a great crash; but taking advantage of being out of the gendarme's sight, you have stayed inside, between the sentry box and the perimeter wall.

Cautiously, from bush to tree, you make your way around the grounds, to come back towards the rear of the manor; most of the windows are curtained, which suits you well. No mastiff in sight, either. Old Alphonse is coming and going to hang out the washing, on the back porch, humming bawdy tunes. A moment of inattention on his part, and there you are, back inside the manor.

You hide in the cubbyhole under the spiral staircase of the Great Hall. The old dog Bedou was sleeping in the secondary hall a moment ago, let's hope it stays that way.

The clock strikes 12. Through the wall, you hear Loyd Georges talking, in his bedroom, with Inspector Shark. The policeman harangues his host, pushing him to be more direct and brutal with the "suspects". Loyd Georges, already weary, says he is doing his best. Then a dialogue captures your attention.

- May I have the identity of this individual who, I hear, disguised himself as a dustman to approach you early this morning?
- Who told you that?
- It is my job to know everything; and to protect you, including from yourself.
- This "individual" was merely bringing me fresh news of my friend Professor Loakim, and he left without delay. There is no malice in that.
- You underestimate your enemies' power of corruption. Did he give you any objects, which could be booby-trapped? Was he left alone in the manor, at any point?
- No and no. Let us set aside this harmless event, which is wasting our time.

The butler then enters the Great Hall with a new visitor, which interrupts their argument. Impossible to hear the rest of the exchanges, now that they are taking place in Loyd Georges' study again; the inspector seems to have stayed behind to listen from the bedroom, the sly devil.

You are thinking about your next moves, when you notice a small screen built into the wall. What luck, the control terminal for the manor's cameras. You locate the position of the **cameras ({% symbol "great hall, study, library, dining room, kitchen" for "videosurveillance_cameras_locations" %})**, and of the occupants of the place, before disabling this system. That takes a real thorn out of your side. {% fact 'amethyst_disabled_surveillance_cameras' as author %}

You anticipate the servants' movements within the manor. At around 12:15, the butler calls out to Alphonse that he is going into town to prepare the logistics for tomorrow's evening, and that he is therefore entrusting him with keeping an eye on the visitors.
One of the auction participants, **{{character_properties.opal.official_name}}**, passes a few steps away from you, limping on his cane.

Unable to approach the most interesting rooms, you go upstairs, and spend a long time browsing Loyd Georges' "collection", a jumble of motley objects of little value: Slavinkian leather hats, enormous pachyderms in carved wood, old half-worm-eaten grimoires of Thelassar tales, eroded bronze weapons and masks... The floor is well swept, but on the artefacts and display cases, dust has long since reclaimed its rights. No object seems to have been touched recently, and no apparent hiding place. Zounds.

Going back down the stairs, at around 12:45, you have a hunch. Could the post have been delivered? Bingo! The mailbox in the vestibule is not properly closed; in it you find two advertising brochures, a letter from an anonymised P.O. box, and a thin parcel. You stuff these last two items into your pocket.

Footsteps in the Great Hall force you to migrate towards the dining room, but old Alphonse keeps heading your way, and there is noise in the kitchen... so you take refuge in the spacious pantry. As you jump to hide behind the wine barrels, you find yourself face to face with another intruder. The bidder {{character_properties.malachite.official_name}}.

{% macro spies_locked_in_pantry() %}

{% fact 'amethyst_and_malachite_locked_in_pantry' as author %}

The individual looks just as dumbfounded as you are.

In this highly unpleasant situation, a tacit truce is immediately established. You remain for 5 minutes in silence, side by side, listening to the final preparations for the midday meal; and wondering how to leave the manor without a hitch, when the time comes.

Everything speeds up when a grey canine muzzle comes sniffing under the pantry door. Alphonse's voice rings out.

- Bedou! Leave all that food alone, you blasted gourmet! Your bowl is waiting for you outside!

The dog barks frantically while scratching at the door. You look at each other for a few seconds, you and your accidental sidekick, before turning towards the pantry's high transom window. Climbing onto a chest, you break the strap that holds it shut, climb out one after the other with a few athletic moves, and close it again just before the door opens.
{% endmacro %}
<{ spies_locked_in_pantry }/>

The other spy crawls along the wall on all fours, taking advantage of the cover of a small hedge with red berries; he seems to know what he is doing, so you follow in his footsteps. No alarm has been triggered, but that is no reason to linger here. Having reached the front of the manor, the individual gets back on his feet, and heads for the gate; you catch up with him, and exchange small talk with him, disguising your voice, and taking care to stand on the side opposite the sentry box.

{% macro spies_escape_from_manor() %}
The gendarme opens up for you without even looking up from his newspaper.
Without a word, save for a slight tip of the hat, you each go your separate ways; with a great sense of relief deep in your chest.
{% endmacro %}
<{ spies_escape_from_manor }/>

An incomplete relief, however. The thin brown parcel must have fallen while you were climbing through the transom window. But you do find the folded letter at the bottom of your pocket, and its contents leave you pensive. {% fact 'amethyst_has_stolen_manor_letter' as author %} {% fact 'amethyst_has_lost_thin_manor_parcel' as author %} {% hint "stolen_manor_letter_for_amethyst" is needed %}

You spend the rest of the day trying, in vain, to obtain information about the Orb.
You go to bed very early, in your little room on the {% symbol "8th floor of the SalimaGlobeCenter Hotel" for "amethyst_hostel_room" %}.
{% fact "amethyst_alibi_is_void" as author %}

{% macro no_partner_communication_occurred_and_gala_planned() %}
The next day, you are taken up by a multitude of small matters to settle, and so you have no time to take stock with your partner. A grand gala evening is planned for the night, to relaunch this series of auctions.
{% endmacro %}

{% macro pantry_spies_ending() %}
<{ no_partner_communication_occurred_and_gala_planned }/>You fully intend to take advantage of it to extract some information from Loyd Georges, and to investigate the other bidders further, including your involuntary "ally" from the pantry. Will that be enough to get to the bottom of this whole Orb business?
{% endmacro %}
<{ pantry_spies_ending }/>

