
Shared data for the manor servants
============================================

Schedule of the interview day
+++++++++++++++++++++++++++++++++++++++++++

Here are the arrival times that were planned for the various interviews of the previous day.

{% macro lg_interviews_planning() %}
- {% symbol "11:00" for "amethyst" %}: {{character_properties.amethyst.official_name}} (Amethyst)
- {% symbol "12:00" for "lg_meeting_time_for_malachite" %}: {{character_properties.malachite.official_name}} (Malachite)
- {% symbol "15:00" for "lg_meeting_time_for_peridot_and_topaz" %}: {{character_properties.peridot.official_name}} (Peridot) and {{character_properties.topaz.official_name}} (Topaz)
- {% symbol "16:00" for "lg_meeting_time_for_spinel" %}: {{character_properties.spinel.official_name}} (Spinel)
- {% symbol "17:00" for "lg_meeting_time_for_garnet" %}: {{character_properties.garnet.official_name}} (Garnet)
{% endmacro %}

<{ lg_interviews_planning }/>



Miscellaneous information in case the players investigate
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Over the last few weeks, Loyd Georges and his entourage have suffered numerous attacks:

- two attempts to burgle the manor {% fact 'spinel_robs_lg_manor_fail' %} {% fact 'peridot_robs_lg_manor_fail' %}
- the burglary of one of Loyd Georges' warehouses, fortunately empty of any valuable items {% fact 'malachite&spinel_rob_alifir_warehouse' %}
- an attempted kidnapping of Professor Loakim  {% fact 'peridot&topaz_abduct_emilos_loakim_fail' as author %}
- no doubt many other schemes and attempted thefts, which you have unfortunately never heard of...


Regarding the day of the interviews (the day before the current one):

- Early in the morning, Loyd Georges received a strange parcel, in a brown canvas bag, and hid it. Alphonse blundered by mentioning this to Rydji in front of the inspector, which later caused a row between the gentleman and the inspector. Nobody knows what Loyd Georges did with the contents, but the canvas bag was, at last report, lying around on a shelf in the library. {% fact "alphonse_blunder_revealed_panorbium_fortuna_arrival" %} {% fact 'panorbium_fortuna_bag_remains_in_library' %}
- the surveillance system was deactivated shortly after {% symbol "12:00" for "first_alarm_deactivation_time" %}, but the butler Rydji noticed it on his return in the early afternoon, and reactivated it. Nobody knows why this happened.
- Loyd Georges is the only one who ate the veal blanquette at dinner: the inspector had left, so had Alphonse (off to the gambling den {% symbol "La Murge de Salima" for "alphonse_alibi_bar" %}), and Rydji is a vegetarian.
- Part of the dinner had been set aside, and given by the cook to the dog Bedou. *The dog is eventually found dead at the far end of the grounds, during the special evening, with a swollen and irritated mouth and tongue.*
- Shortly after Loyd Georges was found unconscious, Rydji checked that Opal was fast asleep in his room (he did not react at all to stimuli). {% fact "rydji_could_not_wake_up_opal_after_lg_troubles" %}
- the bins were emptied by the municipal services very early the next morning.


Loyd Georges took Digoxin every day at bedtime, for his heart rhythm problems. The instruction memo left on the wall for Robb Barrow mentions it correctly, but in any case it was the butler who measured out the dose, as he always did.

Was LG allergic to anything? Yes, to dust and hay, but no known food allergy (so the peanuts that were brought in are not to blame).

Having long been steeped in Loyd Georges' archaeology, you know that the Akarith Ambassador's **skull ring** is typical of the {% symbol "Keroskia highlands" for "akarith_ambassador_skull_ring_origin" %}. The other one is more common.


Pharmacological memo on cardiac toxins
+++++++++++++++++++++++++++++++++++++++++++++

*This memo is for the servants to use when answering the guests' questions, if they are asked for details about Loyd Georges' symptoms the day before (due to oleandrin poisoning), about his medical treatment for his tachycardia...*

The following two molecules have a similar action, namely strengthening the heart's contraction, and slowing and regularising the heart's movements. They are therefore used in the treatment of various heart conditions, including heart failure.

- Digoxin is a cardiotonic glycoside extracted from the leaf of the woolly foxglove.
- Digitoxin, also called digitalin or digitoxoside, is a cardiotonic glycoside extracted from the purple foxglove (Digitalis purpurea) and the woolly foxglove (Digitalis lanata).

Other plants causing bradycardia (an abnormally low heart rate): celandine, hellebore, lily of the valley, and the oleandrin contained in oleander.

The various disorders caused by the oleandrin of oleander:

- Cardio-respiratory: heart rate disorders producing an abnormal alternation of acceleration (tachycardia) and slowing (bradycardia) of that rate
- Digestive: loss of appetite, diarrhoea that is sometimes haemorrhagic, colic
- Nervous: prostration, muscle tremors, convulsions, coma
- Dermatological: heavy sweating, cold extremities
- Psychological: confusion, visual disturbances (phosphenes), obnubilation (apathy)
- Ocular: dilated pupils (mydriasis)

But oleandrin does not produce the following symptoms, which are specific to other poisons:

- purple spots on the body and tongue

