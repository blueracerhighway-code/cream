"""Proper endings for all 40 scripts.

Every script now closes: story resolves -> LANDING (what it meant) -> BRIDGE (why follow / why
try the jar) -> SERIES (with a lead-in) -> CTA (link + 77-day guarantee as risk reversal).

Facts come from the Master Script Source Document. Script 37's ending (boss yelling, never
working for someone again) and script 38's "follow my journey" line come from the founder's
own message on 2026-10-05.
"""

CTA_GUARANTEE = "Comment HONEY and I'll send you the link. It comes with a 77-day money-back guarantee."
CTA_PLAIN = "Comment HONEY and I'll send you the link."

FOUNDER = "Anyways, "
NEW_HERE = "If you're new here, "


def b(label, say, screen, visual):
    return (label, say, screen, visual)


ENDINGS = {
    # ---- batch 1: founder stories ----
    "01-lose-25-per-jar": ([
        b("LANDING", "So when you buy your first jar, I'm not trying to make money off you. I'm hoping you come back.",
          "I'M HOPING YOU COME BACK", "Face, close / jar handed toward camera"),
        b("BRIDGE", "Follow along to see if the bet pays off.", "WILL IT PAY OFF?", "Face, small smile"),
    ], FOUNDER, CTA_GUARANTEE),
    "02-200kg-sludge": ([
        b("LANDING", "So when you open a jar now, you're tasting a very expensive lesson.", "AN EXPENSIVE LESSON",
          "Jar opening / spoon pull"),
        b("BRIDGE", "Stick around. There are a lot more mistakes where that came from.", "MORE MISTAKES COMING",
          "Face, dry smile"),
    ], FOUNDER, CTA_GUARANTEE),
    "03-kitchenaid-died": ([
        b("LANDING", "When I do something, I like to do it properly. No compromises.", "NO COMPROMISES",
          "Face, close"),
        b("BRIDGE", "From a dead KitchenAid in my apartment to a jar you can order today. Follow along to see where it goes next.",
          "APARTMENT -> YOUR DOOR", "Old kitchen / finished jar / shipping box"),
    ], FOUNDER, CTA_GUARANTEE),
    "04-first-sale-7": ([
        b("LANDING", "That brother paid $7 for honey with no label.", "$7. NO LABEL.", "Unlabeled jar"),
        b("BRIDGE", "The version you can get now has the label, the proper recipe, and a guarantee.",
          "NOW: LABEL. RECIPE. GUARANTEE.", "Labeled jar turned to camera"),
    ], FOUNDER, CTA_GUARANTEE),
    "05-why-people-quit-black-seed": ([
        b("BRIDGE", "If you've quit black seed before because of the taste, this is the version to try.",
          "QUIT BEFORE? TRY THIS.", "Face / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "06-mom-kids-every-day": ([
        b("BRIDGE", "If your kids won't touch black seed, this is the one to try with them.",
          "TRY IT WITH YOUR KIDS", "Toast on a plate / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "07-300-ads-0-sales": ([
        b("LANDING", "Every one of those sales gets me a little closer to my goal.", "CLOSER TO THE GOAL",
          "Packing a box"),
        b("BRIDGE", "Follow along to see if I get there.", "WILL I MAKE IT?", "Face, close"),
    ], FOUNDER, CTA_GUARANTEE),
    "08-first-event-300": ([
        b("LANDING", "If you never made it to one of my events, you don't have to wait for the next one.",
          "MISSED THE EVENTS?", "Event table photo"),
        b("BRIDGE", "It ships across Canada, usually in 2 to 5 days.", "SHIPS ACROSS CANADA", "Box taped / shipping label"),
    ], FOUNDER, CTA_GUARANTEE),
    "09-77-day-guarantee": ([
        b("BRIDGE", "So try it. If it's not for you, you've got 77 days to get your money back.",
          "77 DAYS TO DECIDE", "Face, calm / jar"),
    ], FOUNDER, CTA_PLAIN),
    "10-dad-200-jars": ([
        b("LANDING", "So that's what this series is. Me trying to prove it, 1 jar at a time.",
          "PROVING IT, 1 JAR AT A TIME", "Jar placed on a row"),
        b("BRIDGE", "Follow along and see if I can.", "WATCH ME TRY", "Face, close"),
    ], FOUNDER, CTA_GUARANTEE),

    # ---- batch 2: product ----
    "11-oil-to-coffee": ([
        b("BRIDGE", "If black seed oil never worked out for you, try this in your coffee tomorrow morning.",
          "TRY IT IN YOUR COFFEE", "Coffee cup / spoon"),
    ], NEW_HERE, CTA_GUARANTEE),
    "12-four-ingredients": ([
        b("BRIDGE", "Flip over whatever's in your pantry and count. Then try 1 with 4.", "COUNT YOURS",
          "Hand flipping a pantry jar / then this jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "13-three-weeks": ([
        b("BRIDGE", "3 weeks to make. 2 to 5 days to get to your door.", "3 WEEKS -> YOUR DOOR",
          "Calendar / shipping box"),
    ], NEW_HERE, CTA_GUARANTEE),
    "14-zero-cream": ([
        b("BRIDGE", "If you've never tried creamed honey, this is a good 1 to start with.", "NEVER TRIED IT?",
          "Spoon pull / face"),
    ], NEW_HERE, CTA_GUARANTEE),
    "15-181-substances": ([
        b("BRIDGE", "If you care where your honey comes from, this is why I built it this way.",
          "KNOW WHERE IT'S FROM", "Farm / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "16-3000-years": ([
        b("BRIDGE", "Over 3,000 years of use. I just made it taste good enough to take every day.",
          "3,000 YEARS. NOW IT TASTES GOOD.", "Seeds / spoon pull / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "17-four-ways": ([
        b("BRIDGE", "If you only try 1, start with the croissant.", "START WITH #4", "Croissant bite"),
    ], NEW_HERE, CTA_GUARANTEE),
    "18-first-taste": ([
        b("BRIDGE", "If you've been avoiding black seed because of the taste, I'd love to see your reaction too.",
          "YOUR REACTION NEXT", "Face / jar held out"),
    ], NEW_HERE, CTA_GUARANTEE),
    "19-came-back-next-day": ([
        b("BRIDGE", "I can't promise you'll feel what she felt. But you've got 77 days to try it for yourself.",
          "77 DAYS TO TRY IT", "Face, calm / jar"),
    ], NEW_HERE, CTA_PLAIN),
    "20-six-jars": ([
        b("BRIDGE", "If you're going to try it properly, 6 jars is how I'd do it.", "TRY IT PROPERLY",
          "Six jars lined up"),
    ], NEW_HERE, CTA_PLAIN),

    # ---- batch 3: problem-agitate-solution ----
    "21-taste-for-hours": ([
        b("BRIDGE", "So if the oil isn't working for you, don't quit black seed. Change the format.",
          "CHANGE THE FORMAT", "Oil bottle set aside / jar in front"),
    ], NEW_HERE, CTA_GUARANTEE),
    "22-one-spoon-a-day": ([
        b("BRIDGE", "Give it 77 days. If it doesn't fit your routine, you get your money back.",
          "GIVE IT 77 DAYS", "Calendar / jar"),
    ], NEW_HERE, CTA_PLAIN),
    "23-tried-everything": ([
        b("BRIDGE", "If nothing else has stuck, try something you actually look forward to.",
          "SOMETHING YOU'LL KEEP", "Jar / spoon on toast"),
    ], NEW_HERE, CTA_GUARANTEE),
    "24-kids-daily-fight": ([
        b("BRIDGE", "If your kids fight you on black seed, try this with them this week.",
          "TRY IT THIS WEEK", "Breakfast table / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "25-bees-behind-your-honey": ([
        b("BRIDGE", "If you want honey you can actually trace, this is it.", "HONEY YOU CAN TRACE",
          "Hives / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "26-joint-pain-loop": ([
        b("BRIDGE", "If the taste was what made you quit, try it this way.", "TRY IT THIS WAY", "Spoon pull / jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "27-junk-food-zero-effort": ([
        b("BRIDGE", "Keep the jar next to your coffee. That's the whole trick.", "NEXT TO YOUR COFFEE",
          "Jar placed beside a coffee maker"),
    ], NEW_HERE, CTA_GUARANTEE),
    "28-cant-pronounce-it": ([
        b("BRIDGE", "Count the ingredients in yours. Then try 1 with 4.", "COUNT YOURS",
          "Package flipped / this jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "29-gift-for-mom": ([
        b("BRIDGE", "Next time you're stuck on a gift, skip the candle.", "SKIP THE CANDLE",
          "Candle pushed aside / wrapped jar"),
    ], NEW_HERE, CTA_GUARANTEE),
    "30-why-24-99": ([
        b("BRIDGE", "And if it's not worth it to you, you get your money back.", "NOT WORTH IT? MONEY BACK.",
          "Face, calm"),
    ], NEW_HERE, CTA_PLAIN),

    # ---- batch 4: founder stories ----
    "31-down-to-130": ([
        b("BRIDGE", "Follow along to see if I get back to zero.", "BACK TO ZERO?", "Face, close / jar row"),
    ], FOUNDER, CTA_GUARANTEE),
    "32-label-machine": ([
        b("LANDING", "Next goal is a fully automatic labeling machine.", "NEXT: AUTO LABELER", "Face / crooked label"),
        b("BRIDGE", "Every jar gets me a little closer. Follow along to see when I finally get it.",
          "FOLLOW ALONG", "Jar placed on a row"),
    ], FOUNDER, CTA_GUARANTEE),
    "33-6000-machine": ([
        b("LANDING", "One day, I want to own machines like that.", "ONE DAY", "Photo of a creaming machine"),
        b("BRIDGE", "Every jar gets me a little closer. Follow along and see if I get there.", "FOLLOW ALONG",
          "Face, close"),
    ], FOUNDER, CTA_GUARANTEE),
    "34-400-to-1000": ([
        b("LANDING", "From 400 jars to 1,000, alhamdulillah. The next run, inshallah, even bigger.",
          "NEXT RUN: BIGGER", "Wall of jars"),
        b("BRIDGE", "Follow along to see it.", "FOLLOW ALONG", "Face, small smile"),
    ], FOUNDER, CTA_GUARANTEE),
    "35-seven-stores": ([
        b("BRIDGE", "And if my honey isn't in a store near you yet, it ships across Canada.",
          "NOT NEAR YOU? IT SHIPS.", "Shipping box / map of Canada"),
    ], FOUNDER, CTA_GUARANTEE),
    "36-two-jobs-midnight": ([
        b("LANDING", "Now I'm working to earn all of it back.", "EARNING IT BACK", "Jar row"),
        b("BRIDGE", "Follow along to see if I do.", "WILL I?", "Face, close"),
    ], FOUNDER, CTA_GUARANTEE),
    "37-gps-boss": ([
        b("STEP", "Then he got mad and yelled, why didn't you tell me we were going the wrong way?",
          "\"WHY DIDN'T YOU TELL ME?\"", "Face, deadpan"),
        b("STEP", "I did tell him. Once. He just kept going on and on, and never stopped.",
          "I DID. ONCE.", "Face, long blink / slow zoom"),
        b("LANDING", "Moments like that are why I'll never go back to working for someone else.",
          "NEVER AGAIN", "Face, close"),
        b("BRIDGE", "I'd rather build my future making money for myself.", "BUILDING MY OWN", "Jar row / labeling"),
    ], FOUNDER, CTA_GUARANTEE),
    "38-fifteen-years-medina": ([
        b("BRIDGE", "Follow my journey to see if I'll be able to achieve my goals.", "WILL I MAKE IT?",
          "Face, close / Medina photo"),
    ], FOUNDER, CTA_GUARANTEE),
    "39-two-people": ([
        b("BRIDGE", "So when your order shows up, there's a good chance my sister or I packed it.",
          "PACKED BY US", "Packing a box / tape"),
    ], FOUNDER, CTA_GUARANTEE),
    "40-gave-it-away": ([
        b("BRIDGE", "That's exactly what I did with this honey. Now it's your turn to try it.",
          "YOUR TURN", "Jar handed toward camera"),
    ], FOUNDER, CTA_GUARANTEE),
}


def apply(sc):
    """Insert the ending beats before SERIES, add the series lead-in, set the CTA."""
    if sc["slug"] not in ENDINGS:
        return sc
    bridges, lead, cta = ENDINGS[sc["slug"]]
    beats = [x for x in sc["beats"] if x[0] not in ("SERIES", "CTA")]
    series = next(x for x in sc["beats"] if x[0] == "SERIES")
    cta_beat = next(x for x in sc["beats"] if x[0] == "CTA")
    line = series[1]
    series = (series[0], lead + line[0].lower() + line[1:], series[2], series[3])
    cta_beat = (cta_beat[0], cta, cta_beat[2], cta_beat[3])
    return dict(sc, beats=beats + bridges + [series, cta_beat])
