
{# CONTAINER OF MACROS, AUTOLOADED BY JINJA-MACROS-TAGS #}


{% macro player_possessions() %}

Your account at the Bank of Salima:

- Standard cash: {{current_player_account}} kashes

- {{ current_player_extra_goods | default("No other possessions", True) }}

{% endmacro %}



{% macro long_range_phone() %}
Low-Frequency Telephone
    It may happen that, for natural or malicious reasons, mobile phones get no signal. In such cases, nothing beats having, as you do, a miniaturised super transceiver, capable of reaching a telephone relay from anywhere on Pangea. Because of the enormous expenditure of energy required to set up a communication, this device may only be used **three times** during the evening, to reach a single recipient each time. *Ask the Game Master before placing a call with this system.*
{% endmacro %}


{% macro knownledge_of_medecine() %}
Medical Knowledge
    You had started medical studies, and not much remains of them except a certain familiarity with medical vocabulary. *Discreetly ask the Game Master for the meaning of any technical medical terms you may come across.*
{% endmacro %}

{% macro __OLDIE_medical_education() %}
Medical Knowledge
    Before turning to your current career, you spent several years at medical school. And it left its mark on you, enough that even today you retain a good deal of it. You will therefore be able to decipher the jargon of medically themed documents without much trouble. [Show the Game Master the documents you want deciphered]
{% endmacro %}


{% macro knownledge_of_poisons() %}
Knowledge of Poisons
  Over the years, you have acquired the ability to detect immediately, by smell or by taste, that a substance contains a poison. You then know how to recognise this toxin, and recall its effects on a victim. *Ask the Game Master whether something you have found is poisoned or not (and if so, the details of the harmful product).*

{#
.. useful for:
  - ethanol in the cider: a neurotoxin that disinhibits, excites, anaesthetises, creates dependency, and attacks the membranes of neuronal cells; but with no lasting effect if drunk in moderation
  - liqueur brought by a bidder: nothing to report
  - nuts brought by a bidder: nothing to report
  - LG's medication: digoxin, it is a medicine but also a poison
  - remains of oleander (oleandrin)
  - lily-of-the-valley water (if intercepted)
#}
{% endmacro %}



{% macro real_news() %}
World Press Dispatch
    In recognition of your professionalism as a reporter, your editor-in-chief has done you an immense favour: your "scoops" are no longer subject to the standard verification process, and can reach the radio stations and newspapers of the entire planet in under 15 min. The downside of this great power is that if you broadcast a false piece of news, your career could come to an abrupt end.
    Use the Anthropia portal to transmit such a dispatch to your employer.
{% endmacro %}


{% macro firewall_news() %}
Media Firewall
    When your investigation into the wrongdoings of a notable of Faeran began to bear fruit, he immediately asked his friends in the Press to run headlines about "Smear campaigns allegedly being orchestrated by envious rivals"; this vague counter-information cut the ground from under your feet, and considerably reduced the impact of your article. You are thinking of using this technique should a genuinely malicious media assault be brewing against you or one of your loved ones.


{% endmacro %}

{% macro fake_news() %}
Press Disinformation
    Thanks to your contacts, you have got hold of **two submission codes** of the international news agency. Each of them allows you to broadcast a piece of news, true or false, which will immediately be picked up by the radio stations and newspapers of the entire planet (even if it gets verified and denied later). To use this ability, you must send a **text** message to this news agency, by any available means.
{% endmacro %}


{% macro _____OBSOLETE_runic_translator() %}
Yodic Rune Translator
    One of your contacts recently got hold of a prototype portable translator, developed at the Alifir Academy. This tool, which looks like a camera, is capable of transcribing and then translating any text in ancient Yodic runes that you may have in your hands. *Ask the Game Master to make use of this ability.*
{# UNUSED
.. useful for:
   - rune on a vase: XXXXXXXXXX
   - notes in LG's notebook
   - Panorbium Fortuna book
   - papers from Shark's P.O. box (the Judicator's instructions)
#}
{% endmacro %}


{% macro hypnotic_interview() %}
Boolean Interrogation under Trance
    You have recently mastered direct mesmerism. You may therefore, **once at most** during the evening, isolate yourself with a protagonist (player or not), and hypnotise them. A Game Master must attend the interview. You may then ask the victim **a maximum of 3 questions**, which they will be compelled to answer truthfully, only with "yes" or "no" or "I don't know" or "blocked" (when the question is phrased in such a way that none of the three other possible answers fits). After that, the victim will be released; they will remember the interrogation but will have no evidence to prove it. **Does not work on Inspector Shark or on the Tabellion, as their iron will protects them against this kind of hypnosis.**
{% endmacro %}


{% macro lie_detector_written_interview() %}
Lie-detector paper
    You have **three** truth-interview slips, a recent invention of your employer. The principle is to write between one and three questions on them, have a person answer in writing, then have this interview analysed to detect possible lies. The person interviewed in this way must be informed of the procedure, and consenting. *Bring the completed slip to the Game Master, so that they can later report the result of the truth analysis to you.*
{% endmacro %}


{% macro passcard_hacking() %}
Pass-Card Lockpicking
    You have just received a hacking kit for "pass cards", which are spreading enormously throughout Sabarim at the moment (these locks bear a logo showing a hand inserting a magnetic card). Loyd Georges is known to be a pioneer in their use. *By laying your hand flat on a "pass card" lock* **for 10 seconds**\ *, you will be able to open it. It will lock itself again when closed.*
{#
.. useful for:
  - mailbox at the entrance (contains Loakim's letter)
  - LG's safe
  - closing intermediate doors, e.g. kitchen, to talk?
  # TODO find other uses
#}
{% endmacro %}


{% macro new_identity_and_life() %}
Fresh Start
    As a precaution, your service has arranged everything needed to forge a **new life** in Sabarim (with visa, fake identity papers, entries in administrative registers, a well-paid job as a henchman...) for anyone who might need it; this will work even if the person is the target of a judicial investigation, unless they are already behind bars (e.g. if they were unable to raise bail to remain free pending trial). This fresh start would also work for you (faking your death in the process).
{% endmacro %}


{% macro djinn_interview() %}
Consulting the Djinns
    Your wealth has allowed you to prepay for **three questions** to the Djinns of Sedes Sancta, who are a kind of independent sect, dedicated to the accumulation of knowledge (about ancient facts, or recent news). You must ask all your questions during a single telephone call to their headquarters. Results not guaranteed, but usually very satisfactory.
{% endmacro %}


{% macro _OLDIE_fake_memory() %}
XXXX Memory Suggestion
    .. Over the last few days you have undergone intensive training to master hypnotic suggestion. You may therefore, **twice at most** during the evening, isolate yourself with a protagonist (player or not), and hypnotise them. A Game Master must attend the interview. You may then dictate an event, distant or recent **(but dating from at least the day before)**, real or fictitious, and the victim will become deeply convinced of its truth, **by default with no time limit**. But if this "false memory" conflicts with logic, or with other knowledge they have, the victim need only remain dogmatically convinced of it **for 30 min**; after which they may take a step back from this strange memory (but still "in roleplay fashion"). In any case, the victim will not remember, on their own, having been hypnotised. **Does not work on Inspector Shark, however, as his iron will protects him against this kind of hypnosis.**
{% endmacro %}


{% macro fake_alphonse_memory() %}
Memory Suggestion on Alphonse
    You have recently begun to master hypnotic suggestion; but it only works so far on feeble-minded humans. You may therefore, **twice at most** during the evening, isolate yourself with old **Alphonse**, and hypnotise him. You may then dictate an event, more or less distant (but dating from at least the day before), real or fictitious, and the victim will become deeply convinced of its truth, **for about 15 min**; after which he will no longer quite know what to make of it (and will not remember having been hypnotised).
{% endmacro %}


{% macro anthropia_deletion() %}
Anthropia Purge
    An informant has passed you a "reset code", allowing you to delete ALL the data of an Anthropia account. This operation cannot be undone. To do so, you simply have to send the Anthropia IT department a message containing the targeted username and the special code "VOIDIFY" somewhere in its content. Any textual means can be used for this.
{% endmacro %}


{% macro mercenaries_hiring() %}
Mercenaries
    As part of your investigation, you have treated yourselves to the services of a small gang of thugs (6 people), poorly organised but fairly brutal when needed. If you need to give them a mission, you will have to contact them, by whatever means.
{% endmacro %}


{% macro manor_police_searches() %}
Manor search
    The criminology squad, tasked with methodically searching the manor, has been held back by your superiors until you were on the premises. It is up to you to indicate, as you go along, which room they should search, before they hand over their potential findings to you in person. A search takes **30 minutes** on average.
    They will probably have more success if you tell them, each time, what in particular to look for.
    The dining room, where the guests are, cannot be searched (the inspector is supposed to have "had a look around" there), and police officers are already combing the manor grounds as well as the upper floors.
    The 10 rooms available for searching: **halls, study, library, Loyd Georges' bedroom, Opal's bedroom, old Alphonse's bedroom, Rydji's bedroom, kitchen, pantry, kennel**.
{% endmacro %}

{% macro pneumatic_tubes() %}
Pneumatic Tubes
    During a previous visit to Loyd Georges' home, you noticed a pneumatic tube communication hub which, although obsolete, still seems to be in working order. On a hunch, you therefore decided to buy and keep *ONE* tube on you, just in case. This tube will allow you to send, at any time, a paper message or a small object to an equipped recipient (police, hospital, town hall, fire brigade, press, nobles of the surrounding area...). *If there is a reply (of which you will be notified), the tube can be used again.*
{% endmacro %}


{% macro graphological_analysis() %}
Graphological-Stylistic Analyser
    This prototype, which looks like a camera, lets you find out whether a text (handwritten or printed) was written by the same person as another document. The result is given with a "percentage of certainty", because this type of analysis is not an exact science. It can also give rough indications about the origin and character of the person who wrote it.
    *Ask the Game Master to make use of this ability.*
{#
.. useful for:
   - Preparatory physics work: actually originating from NALAVUT
   - Shark's letters to his sister
   - Loyd Georges' annotation on the recipe "Sabarith-style Veal Blanquette"
   - Waden's letter to Loyd Georges mentioning GemmoKorps
   - Other texts without a seal...
#}
{% endmacro %}


{% macro document_authentication_lamp() %}
Document Authentication
    If a document does not bear a "tamper-proof seal" (signature within a circle) attesting to its authenticity, you have a chance of detecting whether it is genuine or a forgery, thanks to your authenticity analyser.
    *With the ultraviolet lamp, look for a yellow seal (invisible under normal light) on the document. If it contains a vowel, the document is authentic; if it contains a consonant, or any other symbol, it is a forged document.*
{% endmacro %}



{% macro wireline_fax() %}
Secure Landline Fax-Phone
    The Sabarim police department has installed a secure fax-phone in the manor, which only its members can use. This phone is not affected by the mobile phone signal jammer, of course. The callers see each other on video, rather blurrily.
{% endmacro %}


{% macro __OLDIE_phone_redirection() %}
Call Forwarding
    Even though it is illegal, more than once during your career you have intercepted the communications of an individual you suspected without proof. And your interception system is still operational, even if it does not work with the new so-called "mobile" phones, even if it can only divert a single line at any given time, and even if it can only be configured once a day. [Tell the Game Master, during the game, which landline phone you want to divert, if you know of one that interests you]
{% endmacro %}


{% macro __OLDIE_manaic_retrocamera() %}
Manaic Retrocamera
    Your mentors in Akaris have just sent you a prototype of a revolutionary invention: the **manaic retrocamera**. Usable at most once a day (as it consumes a great deal of energy), this camera can reconstruct, in the place where one stands, what happened at a given time (e.g. "3 days ago between {% symbol "16:00" for "" %} and {% symbol "17:00" for "" %}"), as long as it dates from at least the day before; the result is obviously still a little blurry, but this technology could well revolutionise more than one scientific field. Ask the GM to make use of it.
{% endmacro %}


{% macro akarith_riot() %}
Akarith Riot
    A trump card. Hundreds of Akarith fanatics, undercover in Sabarim, have been placed under your command. They are only waiting for a sign from you to throw themselves body and soul into a suicide mission that may serve the cause of the Yods. They are not good fighters, but used well, they can carry out a very effective lightning raid. To contact these troops, however, you must leave the manor, and go and call them from the telephone booth of the neighbouring hamlet.
{% endmacro %}


