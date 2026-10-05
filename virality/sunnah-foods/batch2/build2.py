"""Batch 2: 10 product-focused scripts (black seed + creamed honey). Same renderer as build.py.

Facts come only from the Sunnah Foods Master Script Source Document (v2, Oct 2026), mostly
Parts 4 (product facts) and 5 (education library).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
S = build.SERIES_PRIMARY
CTA = build.CTA

SCRIPTS = [
    dict(
        slug="11-oil-to-coffee", title="Quit the oil, kept the seed", story="S-38 + Part 4 comparison",
        formula="Customer report", based_on="@BrainDecoded, 'Why Your Black Seed Oil Routine Is Failing', 61K views (routine-problem pattern)",
        hooks=[("54.2 OK", "A customer quit black seed oil over the aftertaste. Now it's in his morning coffee.", "QUIT THE OIL. KEPT THE SEED."),
               ("29.8 WEAK", "Black seed oil tastes like gasoline to a lot of people. Here's the other way to take it.", "THE OTHER WAY")],
        beats=[
            ("HOOK", "A customer quit black seed oil over the aftertaste. Now it's in his morning coffee.", "QUIT THE OIL. KEPT THE SEED.",
             "Face / spoon of honey dropping into black coffee"),
            ("PROOF", "That's from a real review. One of about 45 I have, from a customer named Mohammad Jawad.", "REAL REVIEW",
             "[DETAIL NEEDED: screenshot of his review, with his OK to show his name]"),
            ("STEP", "Black seed oil is fine. It's just concentrated, and the aftertaste is strong for a lot of people.", "OIL IS FINE. JUST STRONG.",
             "Plain unbranded oil bottle / face, honest"),
            ("REHOOK", "So I went a different way.", "A DIFFERENT WAY", "Jar turned toward camera"),
            ("PAYOFF", "Black seed ground extremely fine and creamed into raw unpasteurized honey, with sesame and olive oil. Black seed in every spoon, without the harsh aftertaste.",
             "BLACK SEED IN EVERY SPOON", "Grinder / creamy spoon pull in slow motion / jar label"),
            ("STEP", "And coffee works really well. The honey balances the bitterness.", "COFFEE + HONEY", "Stirring the coffee / first sip"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, coffee in hand"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "A customer gave up black seed oil over the aftertaste. Now he takes black seed honey in his morning coffee.",
                 "Creamed black seed honey: raw unpasteurized Alberta honey, finely ground black seed, sesame, olive oil."],
        tags=["#blackseedoil", "#blackseedhoney", "#blackseed", "#morningcoffee"],
        cover="OIL -> COFFEE", yt_title="He quit black seed oil. Now it's in his coffee.",
    ),
    dict(
        slug="12-four-ingredients", title="4 ingredients", story="Part 4 product facts + Part 5 health habit",
        formula="The List", based_on="Sakoon Nutrition product-reveal Shorts (317K, top outlier in the category)",
        hooks=[("50.6 OK", "4 ingredients. That's the whole jar.", "4 INGREDIENTS"),
               ("50.0 OK", "This jar has 4 ingredients, and you'd eat every one of them on its own.", "4. THAT'S IT.")],
        beats=[
            ("HOOK", "Four ingredients. That's the whole jar.", "4 INGREDIENTS", "Jar slammed gently on the counter / four ingredients lined up"),
            ("PROOF", "Raw unpasteurized Alberta honey, from a beekeeper with about ten hives.", "1. RAW ALBERTA HONEY",
             "Honey pour / beehive or farm footage"),
            ("STEP", "Black seed, ground extremely fine.", "2. BLACK SEED", "Seeds in macro / fine ground powder"),
            ("STEP", "Sesame seed. Extra virgin olive oil.", "3. SESAME  4. OLIVE OIL", "Sesame close-up / olive oil pour"),
            ("STEP", "No artificial preservatives.", "NO ARTIFICIAL PRESERVATIVES", "Label ingredient list close-up"),
            ("REHOOK", "Here's the rule I go by.", "MY RULE", "Face, close"),
            ("PAYOFF", "If you wouldn't eat the ingredient by itself, question why it's in your food.", "WOULD YOU EAT IT ALONE?",
             "Face / spoon pull"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Creamed black seed honey has 4 ingredients: raw unpasteurized Alberta honey, finely ground black seed, sesame seed, extra virgin olive oil.",
                 "No artificial preservatives."],
        tags=["#blackseedhoney", "#realfood", "#cleaningredients", "#rawhoney"],
        cover="ONLY 4", yt_title="Everything in a jar of black seed honey",
    ),
    dict(
        slug="13-three-weeks", title="3 weeks per jar", story="Part 4 how it's made",
        formula="The Time Anchor", based_on="Savannah Bee / Fulmer process and texture Shorts (process close-ups)",
        hooks=[("52.0 OK", "3 weeks. That's how long one jar of my black seed honey takes.", "3 WEEKS PER JAR"),
               ("50.7 OK", "You're paying for 3 weeks of work in every jar. Here's where it goes.", "3 WEEKS IN A JAR")],
        beats=[
            ("HOOK", "Three weeks. That's how long one jar of my black seed honey takes.", "3 WEEKS PER JAR",
             "Face / calendar with three weeks marked"),
            ("PROOF", "Week one. The raw honey gets creamed in a creaming machine.", "WEEK 1: CREAMING", "Creaming machine at the farm"),
            ("STEP", "Week two. Black seed, sesame and olive oil go in, and it's creamed and infused for another full week.",
             "WEEK 2: INFUSION", "Black seed going in / slow mix / texture"),
            ("STEP", "Week three. It's jarred and kept in a fridge at about 10 to 14 degrees, so the crystals settle.",
             "WEEK 3: 10-14°C", "Jar filling / fridge thermometer / jars on the shelf"),
            ("REHOOK", "Then my sister and I label it, box it, and ship it.", "LABEL. BOX. SHIP.", "Labeling / boxing / tape gun"),
            ("PAYOFF", "That's why it comes out smooth and spreadable, not runny.", "SMOOTH. NOT RUNNY.", "Knife spreading on toast in slow motion"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "How creamed black seed honey is made: one week creaming, a two-week infusion, then a week to settle.",
                 "Made in Alberta, Canada."],
        tags=["#creamedhoney", "#howitsmade", "#blackseedhoney", "#albertamade"],
        cover="3 WEEKS. 1 JAR.", yt_title="How one jar of black seed honey is made",
    ),
    dict(
        slug="14-zero-cream", title="0 cream in creamed honey", story="Part 5 what creamed honey is",
        formula="The Impossible Claim / myth", based_on="Fulmer Honey, 'Cream honey or classic liquid gold?', 3.3x their median",
        hooks=[("83.0 STRONG", "There's 0 cream in creamed honey. Here's what you're actually eating.", "0 CREAM"),
               ("61.2 OK", "Creamed honey has zero cream in it. Here's what it actually is.", "ZERO CREAM")],
        beats=[
            ("HOOK", "There's zero cream in creamed honey. Here's what you're actually eating.", "0 CREAM",
             "Face / jar opened toward camera / spoon pull"),
            ("PROOF", "Creamed honey is raw honey where the crystallization is carefully controlled.", "CONTROLLED CRYSTALLIZATION",
             "Liquid honey next to creamed honey"),
            ("STEP", "So instead of a runny liquid, you get something smooth and spreadable. Almost like velvet. Store it around 15 degrees and it stays that way.", "SMOOTH. SPREADABLE.",
             "Knife through the jar / spread on croissant"),
            ("REHOOK", "And if your regular honey ever turned hard and grainy?", "HARD AND GRAINY?", "Old crystallized jar from a cupboard"),
            ("PAYOFF", "That's not it going bad. Crystallization is natural, and it's a sign your honey is raw.", "NOT BAD. RAW.",
             "Face, small nod"),
            ("STEP", "I chose creamed because it makes black seed something you look forward to eating, not something that feels like medicine.",
             "SOMETHING TO LOOK FORWARD TO", "Spoon pull / croissant bite"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "What creamed honey actually is, and why crystallized honey hasn't gone bad.",
                 "Creamed black seed honey from Alberta."],
        tags=["#creamedhoney", "#rawhoney", "#honeyfacts", "#blackseedhoney"],
        cover="WHERE'S THE CREAM?", yt_title="There's no cream in creamed honey",
    ),
    dict(
        slug="15-181-substances", title="181 substances in raw honey", story="Part 5 raw vs commercial honey + S-21",
        formula="The Statistic", based_on="BrainDecoded-style ingredient education (72x outlier)",
        hooks=[("56.2 OK", "Raw honey has at least 181 substances. Here's why mine is never pasteurized.", "181+ SUBSTANCES"),
               ("61.2 OK", "181 substances. That's what's in raw honey before it gets heated.", "181")],
        beats=[
            ("HOOK", "Raw honey has at least 181 substances. Here's why mine is never pasteurized.", "181+ SUBSTANCES",
             "Face / raw honey pour in macro"),
            ("PROOF", "Enzymes, amino acids, minerals, vitamins, polyphenols. That's from a review in the Mediterranean Journal of Nutrition and Metabolism.",
             "SOURCE ON SCREEN", "List building on screen / citation card: 'Contribution of honey in nutrition and human health: a review'"),
            ("STEP", "A lot of commercial honey is heavily filtered and pasteurized at high temperatures. It keeps it looking uniform on the shelf.",
             "FILTERED. HEATED.", "Plain unbranded squeeze bottle / supermarket shelf, no brand visible"),
            ("REHOOK", "But excessive heat can damage enzymes. And ultra-filtration removes pollen.", "HEAT DAMAGES ENZYMES",
             "Face, plain"),
            ("PAYOFF", "Mine is raw and unpasteurized, from a small Alberta beekeeper. And the honey is never made from sugar water.",
             "RAW. UNPASTEURIZED. ALBERTA.", "Farm / beekeeper's hives / jar"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Raw honey contains at least 181 substances (Mediterranean Journal of Nutrition and Metabolism).",
                 "Why the honey in my black seed honey is raw, unpasteurized and from a small Alberta beekeeper."],
        tags=["#rawhoney", "#honeyfacts", "#blackseedhoney", "#albertahoney"],
        cover="RAW VS HEATED", yt_title="What heat does to honey",
    ),
    dict(
        slug="16-3000-years", title="3,000 years of black seed", story="Part 5 history + faith references",
        formula="Contrarian Flip (myth: 'just a trend')", based_on="Sakoon '3 islamic Ingredients You NEED' (33x) heritage pattern",
        hooks=[("75.1 STRONG", "You're not trying a trend. Black seed has been used for over 3,000 years.", "3,000+ YEARS"),
               ("39.2 WEAK", "Black seed oil was found in Tutankhamun's tomb.", "TUTANKHAMUN'S TOMB")],
        beats=[
            ("HOOK", "You're not trying a trend. Black seed has been used for over 3,000 years.", "3,000+ YEARS",
             "Face / seeds pouring"),
            ("PROOF", "Black seed oil was found in Tutankhamun's tomb. Around 1550 BC, the Ebers Papyrus documented it for digestive issues.",
             "TUTANKHAMUN. 1550 BC.", "Museum or archive images (licensed/public domain) / papyrus"),
            ("REHOOK", "And the Prophet, peace be upon him, said: there is healing in black seed for every disease except death.",
             "SAHIH AL-BUKHARI & MUSLIM", "Plain text card with the hadith and reference"),
            ("STEP", "Scholars understood that as broad healing potential, by Allah's permission.",
             "BY ALLAH'S PERMISSION", "Face, calm"),
            ("PAYOFF", "Today, it's clinically studied for gut issues, joint pain, and immunity when you're sick.",
             "STUDIED TODAY", "Study titles / spoon pull / jar"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Black seed (Nigella sativa, habbat al-barakah) has been used for over 3,000 years, from Tutankhamun's tomb to Ibn Sina.",
                 "Now clinically studied for gut issues, joint pain and immunity."],
        tags=["#blackseed", "#nigellasativa", "#habbatussauda", "#sunnahfoods"],
        cover="NOT A TREND", yt_title="Black seed has been used for 3,000 years",
    ),
    dict(
        slug="17-four-ways", title="1 spoon, 4 ways", story="Part 4 how to use it + safety notes",
        formula="The List", based_on="Savannah Bee usage Shorts (honeycomb charcuterie, 82x their median)",
        hooks=[("78.2 STRONG", "You only need 1 spoon a day. Here are 4 ways to take it.", "1 SPOON. 4 WAYS."),
               ("50.6 OK", "30 spoons in every jar. Here are 4 ways to take one.", "30 SPOONS PER JAR")],
        beats=[
            ("HOOK", "You only need one spoon a day. Here are four ways to take it.", "1 SPOON. 4 WAYS.", "Face / spoon held up"),
            ("STEP", "One. A 10 gram spoon, straight, after Fajr.", "1. AFTER FAJR", "Early window light / prayer mat folded / spoon"),
            ("STEP", "Two. In your coffee. The honey balances the bitterness.", "2. COFFEE", "Spoon into coffee / stir"),
            ("STEP", "Three. In tea or warm water. Warm, not boiling.", "3. TEA / WARM WATER", "Tea cup / kettle off the boil"),
            ("REHOOK", "Four is my favourite.", "4. MY FAVOURITE", "Face, small smile"),
            ("PAYOFF", "On a fresh croissant.", "FRESH CROISSANT", "Knife spread on a croissant / bite, slow motion"),
            ("STEP", "Quick notes. Not for babies under one. If you're pregnant, diabetic, or on medication, check with your doctor first.",
             "SAFETY FIRST", "Plain text card: not for babies under 1 / pregnant, diabetic or on medication: ask your doctor"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, croissant in hand"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "4 ways to take black seed honey: off the spoon after Fajr, in coffee, in tea or warm water, on a fresh croissant.",
                 "30 servings per jar."],
        tags=["#blackseedhoney", "#morningroutine", "#sunnahfoods", "#creamedhoney"],
        cover="4 WAYS", yt_title="4 ways to take black seed honey every day",
    ),
    dict(
        slug="18-first-taste", title="First taste reactions", story="S-31 + Part 4 taste",
        formula="Myth-buster + reaction", based_on="Sakoon 'game changer' product-reaction Short (317K) + your own event reaction footage",
        hooks=[("54.4 OK", "Black seed doesn't have to taste bitter to work. Watch people try it for the first time.", "FIRST TASTE"),
               ("38.0 WEAK", "You think black seed has to taste bitter to work. It doesn't.", "NOT BITTER")],
        beats=[
            ("HOOK", "Black seed doesn't have to taste bitter to work. Watch people try it for the first time.", "FIRST TASTE",
             "Face / first real reaction clip from your events (with permission)"),
            ("PROOF", "The most common thing people tell me after trying it: they expected it to be way more bitter.",
             "\"I EXPECTED IT TO BE BITTER\"", "3 or 4 reaction clips, about 1 second each"),
            ("STEP", "Instead, they say it tastes balanced.", "BALANCED", "Reaction clip, nodding"),
            ("REHOOK", "That makes sense. Most people already know what black seed tastes like.", "YOU KNOW THE TASTE",
             "Face, dry half smile"),
            ("STEP", "Earthy, peppery, with an intense aftertaste. That's why so many people quit it.", "WHY PEOPLE QUIT",
             "Loose seeds on a spoon"),
            ("PAYOFF", "You still taste the black seed here. It's just balanced with the natural sweetness of raw creamed honey.",
             "STILL BLACK SEED. BALANCED.", "Spoon pull in slow motion / jar"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "What people say the first time they try creamed black seed honey.",
                 "You still taste the black seed, without the overpowering bitter aftertaste."],
        tags=["#blackseed", "#tastetest", "#blackseedhoney", "#firsttaste"],
        cover="EXPECTED BITTER", yt_title="People try black seed honey for the first time",
    ),
    dict(
        slug="19-came-back-next-day", title="She came back the next day", story="S-32",
        formula="Customer report", based_on="testimonial storytime; you have a video clip of her",
        hooks=[("50.5 OK", "1 day after buying my honey, a woman came back to my table.", "SHE CAME BACK"),
               ("27.5 WEAK", "A customer came back to my table the next day to tell me how she felt.", "THE NEXT DAY")],
        beats=[
            ("HOOK", "One day after buying my honey, a woman came back to my table.", "SHE CAME BACK",
             "Face / event table"),
            ("PROOF", "She told me that morning she'd woken up low on energy and dizzy. She said it felt like her iron was low.",
             "LOW ENERGY. DIZZY.", "Face, listening tone"),
            ("STEP", "She took a spoonful, and afterwards she felt much more energetic.", "1 SPOONFUL", "Spoon / jar"),
            ("REHOOK", "Her words: up and running like a horse.", "\"UP AND RUNNING LIKE A HORSE\"",
             "Your real clip of her (with her permission)"),
            ("PAYOFF", "That's her experience, not a promise. Everyone's different, and consistency over time matters most.",
             "HER EXPERIENCE", "Face, calm / jar on the table"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "A customer came back to my table the next day to tell me how she felt after a spoon of black seed honey.",
                 "Her experience, in her words. Not a promise."],
        tags=["#blackseedhoney", "#customerreview", "#blackseed", "#smallbusiness"],
        cover="SHE CAME BACK", yt_title="She came back the next day to tell me this",
    ),
    dict(
        slug="20-six-jars", title="Why 6 jars", story="Part 4 offer + S-55",
        formula="The Payoff (offer)", based_on="honest-math transparency pattern (script 01 sequel)",
        hooks=[("81.8 STRONG", "6 jars for $99.95. Here's why I'd rather you buy 6 than 1.", "6 JARS. $99.95."),
               ("73.0 STRONG", "Buy 4 jars, get 2 free. Here's why I'd rather you buy 6 than 1.", "BUY 4, GET 2 FREE")],
        beats=[
            ("HOOK", "Six jars for $99.95. Here's why I'd rather you buy six than one.", "6 JARS. $99.95.",
             "Face / six jars lined up"),
            ("PROOF", "One jar is $24.99 plus shipping. I lose about $25 on that order.", "1 JAR: I LOSE ~$25",
             "Single jar / notes app with the math"),
            ("STEP", "The six-jar bundle is buy four, get two free. 33 percent off, with free shipping.", "BUY 4, GET 2 FREE",
             "Two jars slide in beside four / website bundle page"),
            ("REHOOK", "On that order, I actually make money. And you get two jars free.", "WE BOTH WIN",
             "Face, small smile"),
            ("PAYOFF", "30 servings a jar, 2 to 5 day shipping in Canada, and a 77-day money-back guarantee.",
             "30 SERVINGS. 77 DAYS.", "Box packed / shipping label / guarantee badge"),
            ("STEP", "No countdown timer. Just the honest math.", "JUST THE MATH", "Face, close"),
            ("SERIES", S, "", "Jar placed in a row"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, six jars behind"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Creamed black seed honey: 6 jars for $99.95 (buy 4, get 2 free), free shipping in Canada, 77-day money-back guarantee.",
                 "Why the bundle works better for both of us."],
        tags=["#blackseedhoney", "#smallbusiness", "#canadianmade", "#creamedhoney"],
        cover="WHY 6 JARS?", yt_title="Why I'd rather you buy 6 jars than 1",
    ),
]


def main():
    os.makedirs(os.path.join(HERE, "scripts"), exist_ok=True)
    index, say_all = ["# Sunnah Foods batch 2: 10 product scripts", ""], []
    for n, sc in enumerate(SCRIPTS, 11):
        md, total = build.render(sc, n)
        with open(os.path.join(HERE, "scripts", f"{sc['slug']}.md"), "w") as f:
            f.write(md)
        index.append(f"{n}. [{sc['title']}](scripts/{sc['slug']}.md): {total:.1f}s, hook {sc['hooks'][0][0]}, {sc['story']}")
        say_all += [b[1] for b in sc["beats"]] + sc["caption"]
    with open(os.path.join(HERE, "draft.txt"), "w") as f:
        f.write("\n".join(say_all) + "\n")
    with open(os.path.join(HERE, "INDEX.md"), "w") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    main()
