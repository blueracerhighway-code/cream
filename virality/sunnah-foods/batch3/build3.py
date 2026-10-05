"""Batch 3: 10 problem-agitate-solution scripts. The product only appears at SOLUTION.

Problems come from Part 6 (the customer) of the Sunnah Foods Master Script Source Document;
everything said about the product comes from Parts 3 to 5 and 7.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
S = build.SERIES_PRIMARY
CTA = build.CTA
CTA_BEAT = ("CTA", CTA, 'Comment "HONEY"', "Face full frame")
SERIES_BEAT = ("SERIES", S, "", "Jar placed in a row")


def sc(slug, title, problem, hooks, beats, caption, tags, cover, yt_title):
    return dict(slug=slug, title=title, story=f"Problem: {problem}", formula="Problem-Agitate-Solution",
                based_on="PAS structure requested; problem framing matches @BrainDecoded 'Why Your Black Seed Oil Routine Is Failing' (61K)",
                hooks=hooks, beats=beats + [SERIES_BEAT, CTA_BEAT],
                caption=["Comment HONEY and I'll send you the link."] + caption,
                tags=tags, cover=cover, yt_title=yt_title)


SCRIPTS = [
    sc("21-taste-for-hours", "You taste it for hours", "the taste (Part 6 pain point + customer quotes)",
       [("50.5 OK", "You take 1 spoon of black seed oil and taste it for hours.", "TASTE IT FOR HOURS"),
        ("54.4 OK", "You know it's good for you. But 1 spoon of black seed oil ruins your whole morning.", "1 SPOON. WHOLE MORNING.")],
       [("HOOK", "You take 1 spoon of black seed oil and taste it for hours.", "TASTE IT FOR HOURS",
         "Face, grimace / plain unbranded oil bottle / spoon"),
        ("AGITATE", "Then you burp it back up. A lot of people say it tastes like gasoline.", "\"LIKE GASOLINE\"",
         "Face, dry look / gas pump icon graphic"),
        ("AGITATE", "So you tell yourself, I know it's good for me, I just can't drink it. And the bottle sits there.",
         "\"I JUST CAN'T DRINK IT\"", "Bottle pushed to the back of a cupboard / cupboard door closing"),
        ("REHOOK", "Oil is fine. It's just not the only way to take black seed.", "NOT THE ONLY WAY", "Face, close"),
        ("SOLUTION", "I grind black seed extremely fine and cream it into raw unpasteurized Alberta honey, with sesame and olive oil. 2 weeks of infusion.",
         "CREAMED BLACK SEED HONEY", "Grinder / jar reveal / spoon pull in slow motion"),
        ("PROOF", "You still taste the black seed. Just without the overpowering aftertaste.", "NO HARSH AFTERTASTE",
         "First-taste reaction clip from an event (with permission)")],
       ["Black seed oil taste too strong? Lingering aftertaste, burping it back up?",
        "Creamed black seed honey: finely ground black seed in raw Alberta honey, without the overpowering aftertaste."],
       ["#blackseedoil", "#blackseed", "#blackseedhoney", "#nigellasativa"],
       "THE AFTERTASTE", "Black seed oil aftertaste? Try it this way"),

    sc("22-one-spoon-a-day", "You're failing at 1 spoon a day", "consistency (Part 7 compliance gap)",
       [("63.7 OK", "You're not failing at black seed. You're failing at 1 spoon a day, and here's why.", "1 SPOON A DAY"),
        ("47.1 WEAK", "You bought black seed with 100+ active compounds. Now it's sitting in your cupboard.", "100+ COMPOUNDS")],
       [("HOOK", "You're not failing at black seed. You're failing at 1 spoon a day, and here's why.", "1 SPOON A DAY",
         "Face / single spoon held up"),
        ("AGITATE", "You start strong. A few days in, the taste wins, and you stop.", "THE TASTE WINS",
         "Calendar: first days ticked, then blank"),
        ("AGITATE", "And with black seed, consistency over time is what matters most.", "CONSISTENCY > INTENSITY",
         "Face, plain"),
        ("REHOOK", "So the problem isn't you. The routine has to be something you can enjoy.", "THE PROBLEM ISN'T YOU",
         "Face, close"),
        ("SOLUTION", "That's why I made black seed into creamed honey. Something you'd actually look forward to.",
         "SOMETHING TO LOOK FORWARD TO", "Jar reveal / spoon pull"),
        ("PROOF", "1 spoon, about 10 grams. Attach it to what you already do. On toast. In your tea. In your coffee.", "TOAST. TEA. COFFEE.",
         "Toast / tea / coffee, one second each")],
       ["Why most people stop taking black seed, and how to make it a daily habit.",
        "Creamed black seed honey on toast, in tea or in coffee."],
       ["#blackseed", "#healthyhabits", "#blackseedhoney", "#morningroutine"],
       "WHY YOU QUIT", "Why you keep quitting black seed"),

    sc("23-tried-everything", "You've tried 5 things", "\"I've tried everything\" (Part 6)",
       [("50.4 OK", "You've tried 5 things for your health and none of them stuck.", "5 THINGS. NONE STUCK."),
        ("49.8 WEAK", "Black seed oil, capsules, fish oil, turmeric, vitamins. You've tried all 5.", "TRIED ALL 5")],
       [("HOOK", "You've tried 5 things for your health and none of them stuck.", "5 THINGS. NONE STUCK.",
         "Face / five bottles lined up, no brands visible"),
        ("AGITATE", "Black seed oil. Capsules. Fish oil. Turmeric. Vitamins.", "OIL. CAPSULES. FISH OIL...",
         "Each bottle tapped as it's said, about 1 second each"),
        ("AGITATE", "Every one is another pill, another bottle, another thing to remember.", "ANOTHER THING TO REMEMBER",
         "Bottles pushed aside one by one"),
        ("REHOOK", "Health doesn't have to be complicated.", "IT DOESN'T HAVE TO BE COMPLICATED", "Face, close"),
        ("SOLUTION", "A spoon of real food. Creamed black seed honey, made from 4 ingredients you'd eat on their own.",
         "REAL FOOD. 4 INGREDIENTS.", "Jar placed where the bottles were / four ingredients"),
        ("PROOF", "Black seed is clinically studied for gut issues, joint pain, and immunity when you're sick. And this is a food, not another pill.",
         "A FOOD, NOT A PILL", "Study citation card / spoon on toast")],
       ["Tried black seed oil, capsules, fish oil, turmeric and vitamins, and nothing stuck?",
        "Creamed black seed honey is a food, not another pill. 4 ingredients."],
       ["#blackseed", "#naturalhealth", "#realfood", "#blackseedhoney"],
       "NOTHING STUCK?", "Tried everything for your health? Read this"),

    sc("24-kids-daily-fight", "Kids and black seed", "parents who can't get kids to take black seed (Part 6, S-34)",
       [("66.4 OK", "Getting your kids to take 1 spoon of black seed shouldn't be a daily fight.", "NOT A DAILY FIGHT"),
        ("50.7 OK", "1 mom told me her kids eat black seed every day now.", "HER KIDS. EVERY DAY.")],
       [("HOOK", "Getting your kids to take 1 spoon of black seed shouldn't be a daily fight.", "NOT A DAILY FIGHT",
         "Face / spoon held out across a breakfast table"),
        ("AGITATE", "You know the benefits. You probably grew up with it. But it's bitter, and they push it away.",
         "BITTER. PUSHED AWAY.", "Hand pushing a spoon away (staged with an adult hand)"),
        ("REHOOK", "A lot of parents already know black seed and honey. The hard part is a way kids will actually take it.",
         "THE HARD PART", "Face, close"),
        ("SOLUTION", "So I made it. Black seed creamed into raw honey. Smooth, a little sweet, and still black seed.",
         "SMOOTH. STILL BLACK SEED.", "Jar reveal / spread on toast"),
        ("PROOF", "1 mom told me her kids now eat it every day, because they like the taste. Never for babies under one, though.",
         "NOT FOR BABIES UNDER 1", "Toast on a kid's plate / text card: not for babies under 1")],
       ["Kids won't take black seed because it's bitter? One mom told me hers now eat this every day.",
        "Creamed black seed honey. Never for babies under one."],
       ["#muslimmom", "#blackseed", "#kidsnutrition", "#blackseedhoney"],
       "THE MORNING FIGHT", "How to get kids to take black seed"),

    sc("25-bees-behind-your-honey", "The bees behind your honey", "trust: is it really raw? (Part 6, S-21, S-23)",
       [("77.8 STRONG", "You don't know 1 thing about the bees behind your honey.", "WHO MADE YOUR HONEY?"),
        ("47.7 WEAK", "My beekeeper has about 10 hives. Do you know where your honey comes from?", "10 HIVES")],
       [("HOOK", "You don't know 1 thing about the bees behind your honey.", "WHO MADE YOUR HONEY?",
         "Face / plain unbranded honey bottle held up"),
        ("AGITATE", "Was it heated? Filtered? Were syrups added? Most of the time, you can't tell.", "HEATED? FILTERED? SYRUP?",
         "Bottle turned to the label / squinting at small print"),
        ("REHOOK", "That's why I refused to build my product on honey I couldn't trace.", "I HAD TO KNOW", "Face, close"),
        ("SOLUTION", "My honey is raw and unpasteurized, from a small Alberta beekeeper with about 10 hives. I know how the bees are managed.",
         "10 HIVES. ALBERTA.", "Farm / hives / beekeeper's hands"),
        ("PROOF", "I even turned down a supplier that makes thousands of kilos a season. The honey is never made from sugar water.",
         "NEVER MADE FROM SUGAR WATER", "Jar / creamy spoon pull")],
       ["Do you know where your honey comes from? Raw, unpasteurized, from a small Alberta beekeeper with about ten hives.",
        "Creamed black seed honey. The honey is never made from sugar water."],
       ["#rawhoney", "#albertahoney", "#blackseedhoney", "#knowyourfood"],
       "WHO MADE IT?", "Do you know where your honey comes from?"),

    sc("26-joint-pain-loop", "Joint pain and 1 more pill", "joint pain and trying everything (current ad focus, Part 6)",
       [("50.7 OK", "Joint pain has you trying 1 more cream, 1 more pill, 1 more oil.", "1 MORE PILL"),
        ("37.8 WEAK", "If joint pain has you buying pill after pill, watch this.", "PILL AFTER PILL")],
       [("HOOK", "Joint pain has you trying 1 more cream, 1 more pill, 1 more oil.", "1 MORE PILL",
         "Face / hand rubbing a knee / three unbranded products"),
        ("AGITATE", "And the results don't last, because you can't stay consistent with any of them. Black seed oil is usually on that list too.", "RESULTS DON'T LAST",
         "Products pushed into a drawer"),
        ("REHOOK", "Here's what a lot of people don't know. Black seed is clinically studied for gut issues, joint pain, and immunity when you're sick.",
         "CLINICALLY STUDIED", "Study citation card"),
        ("SOLUTION", "So I made it into creamed honey, something you can take every day without forcing it down.",
         "EVERY DAY. NO FORCING.", "Jar reveal / spoon pull"),
        ("PROOF", "It's a food, not a replacement for anything your doctor gave you. If you're on medication, check with them first.",
         "A FOOD. ASK YOUR DOCTOR.", "Face, calm / text card")],
       ["Black seed is clinically studied for joint pain. Most people quit it because of the taste.",
        "Creamed black seed honey: a food you can take every day. On medication? Check with your doctor first."],
       ["#jointpain", "#blackseed", "#naturalhealth", "#blackseedhoney"],
       "STILL SORE?", "Joint pain and black seed: the part people miss"),

    sc("27-junk-food-zero-effort", "Junk food takes 0 effort", "friction: healthy food is inconvenient (Part 3 'what the business taught him')",
       [("62.6 OK", "Junk food takes 0 effort. That's the whole problem.", "0 EFFORT"),
        ("43.6 WEAK", "You want to eat healthy. Junk food just takes 0 effort.", "0 EFFORT")],
       [("HOOK", "Junk food takes 0 effort. That's the whole problem.", "0 EFFORT",
         "Face / bag of chips opened"),
        ("AGITATE", "It's convenient, it tastes good, and it's made for instant dopamine.", "MADE FOR DOPAMINE",
         "Chips / sugary snacks, quick cuts"),
        ("AGITATE", "Healthy food usually feels inconvenient or unpleasant. So even when you want to be healthier, you don't stick with it.",
         "THE PROBLEM IS FRICTION", "Sad salad / face, plain"),
        ("REHOOK", "I struggle with this too. If I'm hungry, I'll grab shawarma, a rice bowl, or chips.", "ME TOO",
         "Face, dry smile / shawarma"),
        ("SOLUTION", "So I made something healthy that's just as easy. 1 spoon of creamed black seed honey. On toast, or in your coffee.",
         "1 SPOON. ZERO PREP.", "Jar / spoon on toast / spoon in coffee"),
        ("PROOF", "Taste matters more than people admit. If you don't enjoy it, you won't keep doing it.", "TASTE MATTERS",
         "Croissant bite, slow motion")],
       ["Healthy eating fails because of friction, not because you don't want it.",
        "Creamed black seed honey: one spoon, no prep, and it actually tastes good."],
       ["#healthyhabits", "#realfood", "#blackseedhoney", "#easyhealthy"],
       "WHY HEALTHY FAILS", "Why you can't stick to eating healthy"),

    sc("28-cant-pronounce-it", "If you can't pronounce it", "processed 'health' products (Part 5 unpopular opinions)",
       [("79.3 STRONG", "If you can't pronounce half the ingredients in your health food, that's the problem.", "CAN'T PRONOUNCE IT?"),
        ("40.8 WEAK", "Your health food has more ingredients than my jar has. Mine has 4.", "MINE HAS 4")],
       [("HOOK", "If you can't pronounce half the ingredients in your health food, that's the problem.", "CAN'T PRONOUNCE IT?",
         "Face / long ingredient list on an unbranded package, zoomed"),
        ("AGITATE", "A lot of health products are still heavily processed, and marketed more on looks and trends than on wellness.",
         "PROCESSED. TRENDY.", "Shiny packaging, no brands visible / face, plain"),
        ("AGITATE", "So you pay for healthy, and you still don't know what you're eating.", "WHAT ARE YOU EATING?",
         "Package flipped back and forth"),
        ("REHOOK", "My rule: if you wouldn't eat the ingredient by itself, question why it's in your food.", "MY RULE",
         "Face, close"),
        ("SOLUTION", "My jar has four. Raw unpasteurized Alberta honey, finely ground black seed, sesame seed, extra virgin olive oil.",
         "4 INGREDIENTS", "Jar reveal / four ingredients, one second each"),
        ("PROOF", "No artificial preservatives. The closer your food is to its natural state, the better.", "NO ARTIFICIAL PRESERVATIVES",
         "Label close-up / spoon pull")],
       ["If you can't pronounce the ingredients, question why they're in your food.",
        "Creamed black seed honey: 4 ingredients, no artificial preservatives."],
       ["#cleaningredients", "#realfood", "#readthelabel", "#blackseedhoney"],
       "READ THE LABEL", "Can you pronounce what's in your health food?"),

    sc("29-gift-for-mom", "Another candle for your mom?", "what to gift your mother (S-40)",
       [("78.0 STRONG", "Another candle for your mom? Here's 1 gift she'll actually use every morning.", "ANOTHER CANDLE?"),
        ("50.7 OK", "1 jar. That's the gift my customers buy for their moms more than anything.", "1 JAR FOR MOM")],
       [("HOOK", "Another candle for your mom? Here's 1 gift she can use every morning.", "ANOTHER CANDLE?",
         "Face / candle held up, then set down"),
        ("AGITATE", "Flowers die. Candles burn out. Most gifts end up on a shelf.", "ENDS UP ON A SHELF",
         "Wilted flowers / shelf of unused gifts"),
        ("REHOOK", "One of the most common things my customers do is buy a jar for their mom.", "MOST COMMON GIFT",
         "Face, close"),
        ("SOLUTION", "Creamed black seed honey. Raw Alberta honey, black seed, sesame and olive oil. 30 servings, 1 spoon with her morning tea.",
         "1 SPOON WITH HER TEA", "Jar reveal / tea cup / spoon"),
        ("PROOF", "A lot of moms already know black seed. This is a version that actually tastes good.", "SHE KNOWS BLACK SEED",
         "Jar beside a teapot / wrapped box")],
       ["One of the most common gifts my customers buy: a jar of creamed black seed honey for their mom.",
        "Raw Alberta honey, black seed, sesame, olive oil."],
       ["#giftformom", "#blackseedhoney", "#muslimgifts", "#sunnahfoods"],
       "GIFT FOR MOM", "A gift your mom will actually use"),

    sc("30-why-24-99", "$24.99 for honey?", "\"It's too expensive\" (Part 6 objections)",
       [("88.0 STRONG", "$24.99 for a jar of honey? Here's what you're actually paying for.", "$24.99 FOR HONEY?"),
        ("75.1 STRONG", "You think $24.99 is a lot for honey. Here's what's in the jar.", "$24.99?")],
       [("HOOK", "$24.99 for a jar of honey? Here's what you're actually paying for.", "$24.99 FOR HONEY?",
         "Face / jar with the price tag"),
        ("AGITATE", "Fair question. You can get honey for less at the supermarket.", "FAIR QUESTION",
         "Plain unbranded supermarket honey"),
        ("AGITATE", "But think about the oil or capsules you bought and stopped taking. That was money too.", "MONEY YOU ALREADY SPENT",
         "Half-full unbranded bottle at the back of a cupboard"),
        ("REHOOK", "Here's what's in this one.", "WHAT'S IN THIS ONE", "Jar turned to camera"),
        ("SOLUTION", "Raw unpasteurized honey from a beekeeper with about 10 hives. Black seed ground extremely fine. Three weeks from start to finish.",
         "10 HIVES. 3 WEEKS.", "Farm / grinder / calendar"),
        ("PROOF", "30 servings a jar, and a 77-day money-back guarantee if it's not for you.", "30 SERVINGS. 77 DAYS.",
         "Spoon / guarantee badge")],
       ["Why a jar of creamed black seed honey costs $24.99.",
        "Raw unpasteurized Alberta honey, finely ground black seed, three weeks to make, 30 servings, 77-day money-back guarantee."],
       ["#blackseedhoney", "#rawhoney", "#smallbusiness", "#creamedhoney"],
       "WORTH IT?", "Why my honey costs $24.99"),
]


def main():
    os.makedirs(os.path.join(HERE, "scripts"), exist_ok=True)
    index, say_all = ["# Sunnah Foods batch 3: 10 problem-agitate-solution scripts", ""], []
    for n, s in enumerate(SCRIPTS, 21):
        md, total = build.render(s, n)
        with open(os.path.join(HERE, "scripts", f"{s['slug']}.md"), "w") as f:
            f.write(md)
        index.append(f"{n}. [{s['title']}](scripts/{s['slug']}.md): {total:.1f}s, hook {s['hooks'][0][0]}")
        say_all += [b[1] for b in s["beats"]] + s["caption"]
    with open(os.path.join(HERE, "draft.txt"), "w") as f:
        f.write("\n".join(say_all) + "\n")
    with open(os.path.join(HERE, "INDEX.md"), "w") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    main()
