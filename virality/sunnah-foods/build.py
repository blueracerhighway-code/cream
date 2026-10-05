"""Builds the 10 Sunnah Foods scripts. Every SAY line is timed with speech.py.

Facts come only from the Sunnah Foods Master Script Source Document (v2, Oct 2026).
Story IDs are noted on each script so they can be checked against the source.
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.expanduser("~/.claude/skills/virality/tools")
WPM = 160  # assumed calm pace; replace with his measured pace once we have a video of him

SERIES_PRIMARY = "This is day X of selling black seed honey until I can afford to get married. Y jars left."
OVERLAY = 'Upper-middle, 0:00-0:03, same font every video: small "DAY X" above large "Y JARS UNTIL I CAN GET MARRIED"'
CTA = "Comment HONEY and I'll send you the link."

SCRIPTS = [
    dict(
        slug="01-lose-25-per-jar", title="I lose $25 on one jar", story="S-55",
        formula="The Cost", based_on="founder-transparency pattern (Poppi founder-led origin video, per NoGood); payoff-first per hookscore",
        hooks=[("87.0 STRONG", "I lose $25 when you buy one jar of my honey.", "-$25 PER JAR"),
               ("80.1 STRONG", "Every single jar I sell costs me $52 to get to your door.", "$52 TO REACH YOU")],
        beats=[
            ("HOOK", "I lose $25 when you buy one jar of my honey.", "-$25 PER JAR",
             "Face, jar held at chest / jar set down on the counter / price tag close-up"),
            ("PROOF", "It's $24.99 plus $3 shipping. It costs me about $7 to make, $10 to ship, and $35 in ads to reach you.",
             "$7 + $10 + $35 = $52", "Notes app with the math typed out / jar / shipping box being taped / real Ads Manager cost-per-purchase screen"),
            ("REHOOK", "So why would I do that on purpose?", "WHY ON PURPOSE?", "Face, close, plain question"),
            ("PAYOFF", "Because I'm betting you'll come back. After about three orders, I make money on a customer.",
             "3 ORDERS = PROFIT", "Repeat-order list with names blurred / 6-jar bundle laid out / box packed"),
            ("STEP", "I'm not in it for the quick fast money. I want this to be a family business my grandchildren own.",
             "LONG GAME", "Sister labeling jars (if she's OK on camera) / shelf of finished jars"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, jar beside the head"),
            ("SERIES", SERIES_PRIMARY, "", "Hands placing one jar on a row, cut on the last word"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "What one jar of black seed honey actually costs me: $7 to make, $10 to ship, $35 in ads.",
                 "Why I keep selling it anyway."],
        tags=["#blackseedhoney", "#smallbusiness", "#foundersjourney", "#edmontonbusiness"],
        cover="-$25 PER JAR", yt_title="What I actually make on a $24.99 jar of honey",
    ),
    dict(
        slug="02-200kg-sludge", title="200 kilos of sludge", story="S-22",
        formula="The Mistake / Cost", based_on="mistake-turned-win storytime; payoff-first per hookscore",
        hooks=[("77.8 STRONG", "I ruined 200 kilos of honey on my first production run.", "200 KG. RUINED."),
               ("46.4 WEAK", "200 kilos of honey came out like sludge, and I couldn't sell any of it.", "200 KG OF SLUDGE")],
        beats=[
            ("HOOK", "I ruined 200 kilos of honey on my first production run.", "200 KG. RUINED.",
             "Face / [DETAIL NEEDED: any photo or clip of the hard first batch] / buckets"),
            ("PROOF", "I got the ratios wrong. The black seed, sesame and olive oil were basically doubled for the same amount of honey.",
             "RATIOS: DOUBLED", "Black seed close-up / sesame / olive oil bottle / ratio written on paper with the mistake circled"),
            ("STEP", "It came out basically like sludge. Not sellable.", "NOT SELLABLE",
             "Spoon that won't go in, or a stand-in demo labeled 'reenactment'"),
            ("REHOOK", "So I bought another 200 kilos and made it again, with the right ratios.", "ANOTHER 200 KG",
             "Second order / the right ratio on paper"),
            ("PAYOFF", "Then I blended some of the first batch into the new one. It had been infusing for so long, the final honey tasted even better.",
             "TASTED EVEN BETTER", "Pour / creamy spoon pull in slow motion / face tasting"),
            ("STEP", "Small formula mistakes become huge problems. Now precision is everything.",
             "PRECISION > SPEED", "Scale reading / labeled jars lined up"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, jar in hand"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "My first production run of creamed black seed honey went wrong. 200 kg, wrong ratios.",
                 "How the mistake ended up in the final recipe."],
        tags=["#blackseedhoney", "#creamedhoney", "#smallbusiness", "#businessmistakes"],
        cover="200 KG OF SLUDGE", yt_title="I ruined my first 200 kilos of honey",
    ),
    dict(
        slug="03-kitchenaid-died", title="The KitchenAid that died", story="S-13",
        formula="The Time Anchor", based_on="most visual founder moment (source doc); payoff-first per hookscore",
        hooks=[("77.8 STRONG", "3 days of creaming honey killed my KitchenAid.", "3 DAYS. 1 DEAD MIXER."),
               ("45.8 WEAK", "I ran my KitchenAid 10 minutes every hour for 3 days. Then the motor stopped.", "10 MIN EVERY HOUR")],
        beats=[
            ("HOOK", "Three days of creaming honey killed my KitchenAid.", "3 DAYS. 1 DEAD MIXER.",
             "Face / [DETAIL NEEDED: the mixer, if he still has it] / paddle thick with honey"),
            ("PROOF", "Ten minutes every hour, for about three days, with the black seed already in. It got so thick the motor stopped.",
             "10 MIN EVERY HOUR", "Clock / mixer running / mixer silent"),
            ("STEP", "I googled fixes. Nothing worked.", "GOOGLED IT. NOTHING.", "Phone screen scrolling a search, real or recreated"),
            ("REHOOK", "So I grabbed another mixer and held it in my hands for a couple more days until it was ready.",
             "HELD IT FOR DAYS", "Hand mixer in hand / arm close-up / honey turning creamy"),
            ("PAYOFF", "Then I gave all those kilograms away for free. I knew that was the only way to get my name out there.",
             "GAVE IT ALL AWAY", "Jars being handed out, no faces without permission"),
            ("STEP", "Now it's creamed at a partner Alberta honey farm, to my ratios.", "PARTNER ALBERTA FARM",
             "Farm creaming machine / finished jar"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "How my first batch of creamed black seed honey killed a stand mixer.",
                 "Then I gave every kilo away for free."],
        tags=["#blackseedhoney", "#creamedhoney", "#smallbusiness", "#foundersjourney"],
        cover="RIP KITCHENAID", yt_title="Creamed honey broke my stand mixer in 3 days",
    ),
    dict(
        slug="04-first-sale-7", title="My first sale was $7", story="S-15c",
        formula="The Payoff (small number)", based_on="milestone storytime; payoff-first per hookscore",
        hooks=[("81.4 STRONG", "My first ever sale was $7, to a brother from the masjid.", "FIRST SALE: $7"),
               ("81.6 STRONG", "$7. That was my first sale, and I still remember who bought it.", "$7")],
        beats=[
            ("HOOK", "My first ever sale was $7, to a brother from the masjid.", "FIRST SALE: $7",
             "Face / masjid exterior / plain jar, no label"),
            ("PROOF", "No label. No business yet. Just honey in a jar.", "NO LABEL. NO BUSINESS.",
             "Unlabeled jar / bare counter"),
            ("STEP", "That was the first time I realized someone valued what I made enough to pay for it.",
             "SOMEONE PAID FOR IT", "Face, close"),
            ("REHOOK", "But what stuck with me was his reaction.", "HIS REACTION", "Face, small smile"),
            ("PAYOFF", "He was surprised it tasted that good with black seed in it. He loved how balanced it was.",
             "BALANCED, NOT BITTER", "Spoon pull / black seed close-up / honey on a croissant"),
            ("STEP", "Later, once there was a label, another brother became one of my first official customers. Alhamdulillah.",
             "FIRST OFFICIAL CUSTOMER", "Labeled jar now / shelf of jars"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "My first sale of black seed honey was $7, before there was even a label.",
                 "Muslim small business, built one jar at a time."],
        tags=["#blackseedhoney", "#muslimbusiness", "#smallbusiness", "#firstsale"],
        cover="FIRST SALE: $7", yt_title="My first ever sale was $7",
    ),
    dict(
        slug="05-why-people-quit-black-seed", title="Why people quit black seed", story="Part 5 education + Part 7 compliance gap",
        formula="The Mistake (educational)", based_on="@BrainDecoded, 'Why You Should Eat Black Seed Daily', 25K views, 72x their median; same channel 'Why Your Black Seed Oil Routine Is Failing', 61K views",
        hooks=[("54.9 OK", "Black seed has over 100 active compounds. Most people quit it over the taste.", "100+ COMPOUNDS. STILL QUIT."),
               ("50.6 OK", "Black seed is bitter. That's why most people quit it, not because it doesn't work.", "WHY PEOPLE QUIT")],
        beats=[
            ("HOOK", "Black seed has over 100 active compounds. Most people quit it over the taste.", "100+ COMPOUNDS. STILL QUIT.",
             "Black seeds pouring in macro / face"),
            ("PROOF", "There are hundreds of published studies on it. Black seed is clinically studied for gut issues, joint pain, and immunity when you're sick.",
             "HUNDREDS OF STUDIES", "[DETAIL NEEDED: 1 or 2 real study titles to show] / citation card: Acta Scientific Microbiology, Black Cumin (Nigella sativa L.): Studies on Phytochemistry"),
            ("STEP", "But on its own, it's earthy, peppery, a little bitter, with an intense aftertaste.", "EARTHY. BITTER. INTENSE.",
             "Spoon of loose seeds / face reacting honestly"),
            ("REHOOK", "So the problem usually isn't believing in it. It's staying consistent.", "THE REAL PROBLEM: CONSISTENCY",
             "Calendar with missed days, real or simple graphic"),
            ("PAYOFF", "So I grind it extremely fine and cream it into raw unpasteurized Alberta honey. You still taste the black seed, without the harsh aftertaste.",
             "FINE GROUND + RAW HONEY", "Grinder / creamy texture pull / jar label ingredients"),
            ("STEP", "One spoon in the morning. Or in your coffee.", "1 SPOON A DAY", "Spoon into coffee / spoon after Fajr, window light"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Black seed (Nigella sativa, kalonji, habbat al-barakah) is clinically studied for gut issues, joint pain and immunity.",
                 "Most people quit because of the taste. Here's how I made it something you can take every day."],
        tags=["#blackseed", "#nigellasativa", "#kalonji", "#blackseedhoney"],
        cover="WHY PEOPLE QUIT", yt_title="Most people quit black seed for this one reason",
    ),
    dict(
        slug="06-mom-kids-every-day", title="Her kids eat it every day", story="S-34",
        formula="Customer report (family/heritage)", based_on="@sakoonnutrition, 'MY GRANDMA SWEARS BY THIS', 3.2K views, 74x their median (family endorsement pattern)",
        hooks=[("51.8 OK", "1 mom told me her kids eat black seed every day now.", "HER KIDS. EVERY DAY."),
               ("33.4 WEAK", "A mom told me her kids now eat black seed every day, and they actually like it.", "KIDS + BLACK SEED")],
        beats=[
            ("HOOK", "One mom told me her kids eat black seed every day now.", "HER KIDS. EVERY DAY.",
             "Face / jar on a breakfast table"),
            ("PROOF", "Because they actually like the taste. That's what she told me.",
             "THEY LIKE THE TASTE", "Toast with honey spread / spoon"),
            ("REHOOK", "If you grew up with black seed, you know it's usually the thing kids have to be forced to take.",
             "USUALLY FORCED", "Face, dry half smile / black seed oil bottle (no brand shown)"),
            ("PAYOFF", "A lot of moms already know about black seed and honey. The hard part is a way their kids will actually take it every day.",
             "THE HARD PART", "Jar / croissant / tea"),
            ("STEP", "Quick note. Honey is never for babies under one.", "NOT FOR BABIES UNDER 1", "Plain text card, held 2 seconds"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "A mom told me her kids now eat black seed honey every day because they like the taste.",
                 "Her experience, in her words. Never for babies under one."],
        tags=["#blackseedhoney", "#muslimmom", "#blackseed", "#kidsnutrition"],
        cover="KIDS ASK FOR IT", yt_title="Her kids eat black seed every day now",
    ),
    dict(
        slug="07-300-ads-0-sales", title="$300 on ads, $0 sales", story="S-29",
        formula="The Payoff (loss)", based_on="honest e-commerce journey; payoff-first per hookscore",
        hooks=[("80.8 STRONG", "I spent $300 on Meta ads and made $0.", "$300 SPENT. $0 BACK."),
               ("84.4 STRONG", "$300 on ads. Zero sales. Here's what I got wrong.", "$300 -> $0")],
        beats=[
            ("HOOK", "I spent $300 on Meta ads and made $0.", "$300 SPENT. $0 BACK.",
             "Face / real Ads Manager row showing the spend"),
            ("PROOF", "Before that, I built the website and paid someone for SEO. Zero sales.",
             "WEBSITE + SEO = 0", "Website on phone / empty orders page"),
            ("STEP", "So I spent a couple of months learning Meta ads.",
             "EVERY CAMPAIGN, A LESSON", "Laptop at night / notes"),
            ("REHOOK", "$274 got me about five sales. $200 got me about $200 back. $264 got me 18 add-to-carts and zero sales, because my website had an issue.",
             "18 CARTS. $0.", "Each campaign row on screen one at a time, never summed"),
            ("PAYOFF", "Then one campaign made back two times what it spent. Now I run my own, and it's around two sales a day.",
             "~2 SALES A DAY", "Orders page / packing two boxes"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Every Meta ads campaign I ran for my black seed honey, with the real numbers.",
                 "Small business e-commerce, from zero sales to about two a day."],
        tags=["#metaads", "#smallbusiness", "#ecommerce", "#blackseedhoney"],
        cover="$300 -> $0", yt_title="Every Meta ads campaign I ran, with real numbers",
    ),
    dict(
        slug="08-first-event-300", title="First event vs second event", story="S-27 + S-27a (card says they connect)",
        formula="Before and After", based_on="then-vs-now milestone; payoff-first per hookscore",
        hooks=[("84.4 STRONG", "My first event cost $300. I made about $300 profit.", "$300 IN. ~$300 PROFIT."),
               ("84.4 STRONG", "My first event made $300. My second one made $1,200.", "$300 -> $1,200")],
        beats=[
            ("HOOK", "My first event cost $300. I made about $300 profit.", "$300 IN. ~$300 PROFIT.",
             "Face / event table photo from Ramadan"),
            ("PROOF", "Three days. It was slow.", "3 DAYS. SLOW.", "Quiet table / jars waiting"),
            ("STEP", "But I got something worth more. People trying it for the first time, on camera. My first real reaction videos.",
             "FIRST REACTION VIDEOS", "His real customer reaction clips (with permission), 1 second each"),
            ("STEP", "Kids who normally hate black seed actually enjoyed it.", "KIDS ENJOYED IT", "Kid reaction clip, only with parent's permission"),
            ("REHOOK", "Then I did another event that Ramadan.", "ANOTHER EVENT", "Second event footage"),
            ("PAYOFF", "That one made about $1,200. Same honey. I just didn't stop after the slow one.", "~$1,200",
             "Busy table / jars going into bags"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "My first Ramadan event selling black seed honey made about $300 profit. The next made about $1,200.",
                 "Edmonton small business, year one."],
        tags=["#ramadanmarket", "#blackseedhoney", "#smallbusiness", "#edmonton"],
        cover="$300 -> $1,200", yt_title="My first event vs my second one",
    ),
    dict(
        slug="09-77-day-guarantee", title="Why 77 days", story="S-56 (connects to S-55)",
        formula="Contrarian Flip", based_on="trust/values explainer; payoff-first per hookscore",
        hooks=[("77.2 STRONG", "My money-back guarantee is 77 days, not 30. Here's why.", "77 DAYS. NOT 30."),
               ("73.0 STRONG", "If you return my honey, I lose about $52. I still give you 77 days.", "-$52 PER RETURN")],
        beats=[
            ("HOOK", "My money-back guarantee is 77 days, not 30. Here's why.", "77 DAYS. NOT 30.",
             "Face / website guarantee badge on phone"),
            ("PROOF", "I like the number seven. But seven days isn't enough to really try something. So, 77.", "7 -> 77",
             "Number 7 written / 77 written next to it"),
            ("REHOOK", "And if you return a jar, I lose about $52. That's okay. It's part of the business.", "-$52. THAT'S OKAY.",
             "Face, calm"),
            ("PAYOFF", "In Islam, we're taught to be easy and lenient in business. The Prophet, peace be upon him, said: may Allah have mercy on a man who is lenient when he sells, when he buys, and when he demands back his money.",
             "SAHIH AL-BUKHARI 2076", "Plain text card with the hadith and reference / face"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame, a beat of silence before this line"),
            ("SERIES", SERIES_PRIMARY, "", "Jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "Why my black seed honey has a 77-day money-back guarantee instead of 30.",
                 "Sahih al-Bukhari 2076."],
        tags=["#muslimbusiness", "#blackseedhoney", "#smallbusiness", "#halalbusinesspractice"],
        cover="WHY 77?", yt_title="Why my guarantee is 77 days, not 30",
    ),
    dict(
        slug="10-dad-200-jars", title="200 jars before my dad believed", story="S-49",
        formula="The Payoff (milestone)", based_on="relatable family-pressure storytime; payoff-first per hookscore",
        hooks=[("77.8 STRONG", "I sold 200 jars before my dad got behind this business.", "200 JARS. THEN DAD."),
               ("71.4 STRONG", "I had to sell 200 jars before my dad believed in this business.", "200 JARS")],
        beats=[
            ("HOOK", "I sold 200 jars before my dad got behind this business.", "200 JARS. THEN DAD.",
             "Face / stacked boxes of jars"),
            ("PROOF", "My parents come from the mindset where university and a stable job matter most.",
             "UNIVERSITY. STABLE JOB.", "Face / house exterior"),
            ("STEP", "My dad was really reluctant. This was new, it was hard, and nothing was certain.", "NEW. HARD. NO GUARANTEE.",
             "Face, quiet"),
            ("REHOOK", "Then I showed him I'd sold more than 200 jars.", "200+ JARS", "Orders page or sales sheet scroll"),
            ("PAYOFF", "He became really supportive. When they saw the inventory, the equipment, the manufacturing, they were amazed.",
             "DAD: ALL IN", "Wide shot of the setup in the house / boxes / labels"),
            ("STEP", "But telling them business can work isn't enough. The only real proof is results.", "PROOF = RESULTS",
             "Face, close"),
            ("CTA", CTA, 'Comment "HONEY"', "Face full frame"),
            ("SERIES", "This is day X of building a honey company with my sister in my parents' house. Y jars to go.", "",
             "Sister's hands labeling jars (with her OK) / jar placed in a row"),
        ],
        caption=["Comment HONEY and I'll send you the link.",
                 "My dad didn't believe in my black seed honey business until I sold 200 jars.",
                 "20, building a Muslim family business in Edmonton."],
        tags=["#muslimbusiness", "#smallbusiness", "#foundersjourney", "#blackseedhoney"],
        cover="DAD WASN'T SOLD", yt_title="My dad didn't believe in my business until this",
    ),
]


def time_lines(lines):
    cmd = ["python3", os.path.join(TOOLS, "speech.py"), "--wpm", str(WPM), "--json"]
    for line in lines:
        cmd += ["--line", line]
    return json.loads(subprocess.check_output(cmd))


def ts(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}" if s % 1 else f"{int(m)}:{int(s):02d}"


def render(sc, n):
    # CTA is always the last beat; the series line sits right before it
    sc["beats"] = [b for b in sc["beats"] if b[0] != "CTA"] + [b for b in sc["beats"] if b[0] == "CTA"]
    timing = time_lines([b[1] for b in sc["beats"]])
    total = timing["total"]
    out = [f"# Script {n:02d}: {sc['title']}", "",
           "- platform: Reels, TikTok, Shorts",
           f"- length: {total:.1f}s at {WPM} wpm (ASSUMED pace, not yet measured from his videos)",
           f"- formula: {sc['formula']} (hookscore {sc['hooks'][0][0]}, payoff LEADS)",
           "- keyword: HONEY",
           f"- story: {sc['story']} (Master Script Source Document)",
           f"- based on: {sc['based_on']}",
           f"- series overlay: {OVERLAY}", "",
           "## Hook options (hookscore.py)", "",
           "| score | spoken | on screen |", "| --- | --- | --- |"]
    out += [f"| {s} | {sp} | {scr} |" for s, sp, scr in sc["hooks"]]
    out += ["", "## Script", ""]
    for i, (beat, line) in enumerate(zip(sc["beats"], timing["lines"]), 1):
        label, say, screen, visual = beat
        start, end = line["start"], line["start"] + line["seconds"]
        out += [f"### {i}. {label} ({ts(start)}-{ts(end)})", f"SAY: {say}"]
        if screen:
            out.append(f"SCREEN: {screen}")
        out += [f"VISUAL: {visual}", ""]
    out += ["## Caption", "", sc["caption"][0], "", "\n".join(sc["caption"][1:]), "",
            "## Hashtags", "", " ".join(sc["tags"]), "",
            "## Cover", "", f"COVER: {sc['cover']}", f"TITLE: {sc['yt_title']}", ""]
    return "\n".join(out), total


def main():
    index = ["# Sunnah Foods: 10 short-form scripts", ""]
    say_all = []
    for n, sc in enumerate(SCRIPTS, 1):
        md, total = render(sc, n)
        with open(os.path.join(HERE, "scripts", f"{sc['slug']}.md"), "w") as f:
            f.write(md)
        index.append(f"{n:02d}. [{sc['title']}](scripts/{sc['slug']}.md): {total:.1f}s, hook {sc['hooks'][0][0]}, {sc['story']}")
        say_all += [b[1] for b in sc["beats"]] + sc["caption"]
    with open(os.path.join(HERE, "draft.txt"), "w") as f:
        f.write("\n".join(say_all) + "\n")
    with open(os.path.join(HERE, "INDEX.md"), "w") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "scripts"), exist_ok=True)
    main()
