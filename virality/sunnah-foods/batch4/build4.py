"""Batch 4: 10 founder-story scripts, one story card each (stories not used in batch 1).

Facts come only from the Sunnah Foods Master Script Source Document (v2, Oct 2026).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
S = build.SERIES_PRIMARY
CTA_BEAT = ("CTA", build.CTA, 'Comment "HONEY"', "Face full frame")


def series(line=S, visual="Jar placed in a row"):
    return ("SERIES", line, "", visual)


def sc(slug, title, story, hooks, beats, caption, tags, cover, yt_title, series_beat=None):
    return dict(slug=slug, title=title, story=story, formula="Founder storytime",
                based_on="founder-led origin pattern (Poppi founder video, per NoGood) + batch 1 payoff-first hooks",
                hooks=hooks, beats=beats + [series_beat or series(), CTA_BEAT],
                caption=["Comment HONEY and I'll send you the link."] + caption,
                tags=tags, cover=cover, yt_title=yt_title)


SCRIPTS = [
    sc("31-down-to-130", "Down to $130", "S-51",
       [("78.0 STRONG", "I put $11,786 into this business. At one point I had $130 left.", "$11,786 IN. $130 LEFT."),
        ("58.6 OK", "At one point, running this business, I was down to $130.", "DOWN TO $130")],
       [("HOOK", "I put $11,786 into this business. At one point I had $130 left.", "$11,786 IN. $130 LEFT.",
         "Face / notes app with $11,786 / bank app balance, blurred except the number"),
        ("STEP", "I haven't paid myself a salary. Nearly everything goes back into the business.", "$0 SALARY",
         "Boxes of jars / face"),
        ("REHOOK", "So when I got down to around $130, I had to borrow money for more inventory.", "BORROWED FOR INVENTORY",
         "Face, close"),
        ("PAYOFF", "People see revenue and think profit. Almost all of it goes into inventory, ingredients, packaging, shipping and scaling.",
         "REVENUE IS NOT PROFIT", "Ingredient order / jar stack / shipping boxes, 1 second each"),
        ("STEP", "Once I sell $11,786 worth of jars, I'm back at zero. Then it can start making money.", "BACK TO $0 FIRST",
         "Notes app: $11,786 with a progress line")],
       ["I've put $11,786 into my black seed honey business, and at one point I was down to $130.",
        "Why revenue isn't profit for a small business."],
       ["#smallbusiness", "#foundersjourney", "#entrepreneurlife", "#blackseedhoney"],
       "DOWN TO $130", "I was down to my last $130"),

    sc("32-label-machine", "The $500 label machine", "S-23e (connects to S-23c)",
       [("80.8 STRONG", "My $500 label machine lasted 1 production run.", "$500. 1 RUN."),
        ("77.8 STRONG", "I spent $500 on a label machine that ruined every label.", "$500 MISTAKE")],
       [("HOOK", "My $500 label machine lasted 1 production run.", "$500. 1 RUN.",
         "Face / [DETAIL NEEDED: the old machine, if you still have it]"),
        ("PROOF", "It was semi-automatic. It kept ruining labels and wouldn't put them on properly.", "RUINED LABELS",
         "Crumpled labels on the table"),
        ("STEP", "After hours of setting it up, it was just a terrible disaster. So I stopped using it.", "\"A TERRIBLE DISASTER\"",
         "Face, dry"),
        ("REHOOK", "So I bought a manual one for about $100. I twist it myself.", "$100 MANUAL",
         "Hands twisting the manual labeler"),
        ("PAYOFF", "It worked way better. For about 500 jars. Then it started doing a terrible job too.", "500 JARS. THEN...",
         "Crooked label close-up"),
        ("STEP", "So right now, it's labeling by hand. The jars are slightly uneven, so some labels go on crooked and we redo them.",
         "BACK TO HANDS", "Peeling a crooked label / reapplying / sister's hands, with her OK")],
       ["My $500 label machine lasted one production run. The $100 one lasted about 500 jars.",
        "Small business packaging, the unglamorous side."],
       ["#smallbusiness", "#behindthescenes", "#packaging", "#blackseedhoney"],
       "$500 MISTAKE", "The label machine that ruined my first run"),

    sc("33-6000-machine", "The $6,000 machine", "S-18",
       [("80.8 STRONG", "$6,000. That's the machine I needed and couldn't afford.", "$6,000 MACHINE"),
        ("75.0 STRONG", "I couldn't afford a $6,000 honey machine, so I found a farm instead.", "COULDN'T AFFORD IT")],
       [("HOOK", "$6,000. That's the machine I needed and couldn't afford.", "$6,000 MACHINE",
         "Face / photo of a creaming machine"),
        ("PROOF", "A proper creamed honey machine. And they took months to ship.", "MONTHS TO SHIP", "Calendar flip / face"),
        ("REHOOK", "So I partnered with a local Alberta honey farm instead.", "PARTNER FARM", "Farm footage"),
        ("STEP", "I buy creamed honey from them, bring the black seed, sesame and olive oil, and give them the exact ratio. They cream and infuse it to my formula.",
         "MY RATIO. THEIR MACHINE.", "Ingredients handed over / creaming machine running"),
        ("PAYOFF", "The machine slowly mixes regular honey with creamed honey, stirring about every 10 minutes, until the whole batch is creamed.",
         "EVERY 10 MINUTES", "Paddle turning / texture changing"),
        ("STEP", "Didn't have $6,000. Found another way.", "FOUND ANOTHER WAY", "Finished jar / face")],
       ["I couldn't afford a $6,000 creamed honey machine, so I partnered with a local Alberta honey farm.",
        "How creamed black seed honey gets made."],
       ["#smallbusiness", "#creamedhoney", "#albertamade", "#foundersjourney"],
       "NO MACHINE", "I couldn't afford the machine, so I did this"),

    sc("34-400-to-1000", "400 jars to 1,000", "S-23d (first run per timeline)",
       [("80.8 STRONG", "My first run was 400 jars. My last one was 1,000.", "400 -> 1,000"),
        ("54.8 OK", "I just bought 600 kilos of honey for 1,000 jars.", "600 KG")],
       [("HOOK", "My first run was 400 jars. My last one was 1,000.", "400 -> 1,000",
         "Face / wall of finished jars"),
        ("PROOF", "For that last run, I bought 600 kilos of creamed honey.", "600 KG OF HONEY",
         "Buckets / pallet / invoice with prices blurred"),
        ("STEP", "Start to finish, one run takes about 3 weeks.", "3 WEEKS PER RUN", "Calendar"),
        ("REHOOK", "And that first run of 400? That's the one where 200 kilos came out like sludge.", "THE SLUDGE RUN",
         "Face, dry smile"),
        ("PAYOFF", "Same product now. Just a lot more of it, and I'm a lot more careful with ratios.", "MORE CAREFUL NOW",
         "Scale reading / spoon pull"),
        ("STEP", "And every jar still gets labeled and packed by me and my sister.", "STILL BY HAND",
         "Labeling / packing, sister's hands with her OK")],
       ["My first production run of black seed honey was 400 jars. The latest was 1,000, from 600 kg of creamed honey.",
        "Small business production, then and now."],
       ["#smallbusiness", "#thenvsnow", "#foundersjourney", "#blackseedhoney"],
       "400 -> 1,000", "From 400 jars to 1,000"),

    sc("35-seven-stores", "7 stores, 0 sales", "S-25",
       [("54.8 OK", "I had 0 sales when 7 stores agreed to carry my honey.", "0 SALES. 7 STORES."),
        ("50.6 OK", "0 sales. 7 stores said yes anyway.", "7 STORES SAID YES")],
       [("HOOK", "I had 0 sales when 7 stores agreed to carry my honey.", "0 SALES. 7 STORES.",
         "Face / jars on a store shelf"),
        ("PROOF", "7 stores in Edmonton, including Medina Halal Meats.", "7 EDMONTON STORES",
         "Store exteriors, 1 second each (with owners' OK)"),
        ("STEP", "I didn't email them. I walked in.", "I WALKED IN", "Walking through a door / face"),
        ("REHOOK", "Here's what I actually brought.", "WHAT I BROUGHT", "Jar set on a counter"),
        ("PAYOFF", "Real customer feedback, proof people wanted it, and a simple, low-risk way for them to try carrying it.",
         "FEEDBACK. DEMAND. LOW RISK.", "Phone with customer messages, names blurred / jar"),
        ("STEP", "Walking in directly is still the best thing that's worked for me.", "STILL MY #1 STRATEGY", "Face, close")],
       ["How I got my black seed honey into 7 Edmonton stores with zero sales.",
        "Walk in, bring real feedback, make it low risk."],
       ["#smallbusiness", "#edmonton", "#retail", "#blackseedhoney"],
       "7 STORES SAID YES", "How I got into 7 stores with 0 sales"),

    sc("36-two-jobs-midnight", "2 jobs, home at midnight", "S-03",
       [("54.5 OK", "Warehouse in the morning, clinic after, home around midnight. That's how I saved.", "HOME AT MIDNIGHT"),
        ("48.6 WEAK", "I used to work 2 jobs in 1 day and get home around midnight.", "2 JOBS. 1 DAY.")],
       [("HOOK", "Warehouse in the morning, clinic after, home around midnight. That's how I saved.", "HOME AT MIDNIGHT",
         "Face / clock at midnight"),
        ("PROOF", "Several times, I finished a warehouse shift in the morning, then went to work at a clinic later that day.",
         "2 JOBS. 1 DAY.", "Warehouse photo / clinic exterior, no patients"),
        ("STEP", "Some nights I didn't get home until around midnight. My mom would get upset that I was home so late.",
         "MOM WASN'T HAPPY", "Front door at night / face, small smile"),
        ("REHOOK", "I was saving most of what I made.", "SAVING MOST OF IT", "Face, close"),
        ("PAYOFF", "That money is what's in this business now.", "IT'S ALL IN HERE", "Jars / boxes")],
       ["Two jobs in one day, home around midnight. That's where the money in this business came from.",
        "Founder story, Edmonton."],
       ["#foundersjourney", "#hustle", "#smallbusiness", "#muslimbusiness"],
       "2 JOBS. 1 DAY.", "I worked 2 jobs a day to fund this",
       series_beat=series("This is day X of making back the money I was supposed to get married with. Y jars left.")),

    sc("37-gps-boss", "The boss who hated GPS", "S-05",
       [("81.4 STRONG", "My boss drove 30 minutes the wrong way because he hated GPS.", "30 MIN THE WRONG WAY"),
        ("75.0 STRONG", "30 minutes in the wrong direction, because my boss refused to trust GPS.", "HE HATED GPS")],
       [("HOOK", "My boss drove 30 minutes the wrong way because he hated GPS.", "30 MIN THE WRONG WAY",
         "Face, straight / phone map"),
        ("PROOF", "This was my labor job. He used to make fun of me for using GPS.", "HE MOCKED THE GPS",
         "Face, dry"),
        ("STEP", "One day, the GPS showed we were going the wrong direction. I told him once.", "I TOLD HIM ONCE",
         "Map with a wrong-way arrow"),
        ("REHOOK", "He ignored me, and kept making fun of the GPS.", "IGNORED", "Face, long blink"),
        ("PAYOFF", "About 30 minutes later, he realized we were going to the wrong address.", "30 MINUTES LATER",
         "Clock jump / face, deadpan")],
       ["My old boss made fun of me for using GPS, then drove 30 minutes the wrong way.",
        "Storytime from my labor job, before I started selling black seed honey."],
       ["#storytime", "#worststories", "#foundersjourney", "#blackseedhoney"],
       "HE HATED GPS", "My boss drove 30 minutes the wrong way"),

    sc("38-fifteen-years-medina", "15 years to Medina", "Part 1 original plan + S-48",
       [("58.0 OK", "15 years of med school and saving before I could move to Medina. Then I found honey.", "15 YEARS -> MEDINA"),
        ("47.6 WEAK", "My old plan had me moving to Medina in 15 years.", "15 YEARS")],
       [("HOOK", "15 years of med school and saving before I could move to Medina. Then I found honey.", "15 YEARS -> MEDINA",
         "Face / Medina photo from your trip"),
        ("PROOF", "That was the plan. About 10 years of medical study and training, then years of working, living frugally, and saving.",
         "10 YEARS OF MED", "Old university photo / face"),
        ("STEP", "And honestly, I wasn't passionate about medicine. It was process of elimination.", "PROCESS OF ELIMINATION",
         "Face, honest"),
        ("REHOOK", "In December 2023, I visited Medina. Hearing the birds around Fajr, the peace was unlike anything I'd felt.",
         "DECEMBER 2023", "Your Medina footage / photos at dawn"),
        ("PAYOFF", "This business didn't start as a plan to move there. But now it could be. Running it from Medina, with people managing it here in Canada.",
         "MEDINA, INSHALLAH", "Jar / Medina photo / face")],
       ["My old plan: about 15 years of medicine and saving before I could move to Medina.",
        "How a black seed honey business changed that plan."],
       ["#medina", "#muslimentrepreneur", "#foundersjourney", "#sunnahfoods"],
       "THE OLD PLAN", "My 15-year plan to move to Medina"),

    sc("39-two-people", "Mostly 2 people", "S-23b + Part 1 team",
       [("51.8 OK", "Most days, this company is 2 people: me and my little sister.", "2 PEOPLE"),
        ("38.7 WEAK", "A lot of the time, I am the department. All 4 of them.", "I AM THE DEPARTMENT")],
       [("HOOK", "Most days, this company is 2 people: me and my little sister.", "2 PEOPLE",
         "Face / two pairs of hands at the packing table (her OK first)"),
        ("PROOF", "She helps with labeling, jarring and shipping.", "SHE: LABELS. JARS. SHIPS.", "Sister's hands labeling"),
        ("STEP", "I do marketing, coordinate with the farm, sort out jars and labels, and prep and ship orders.",
         "ME: EVERYTHING ELSE", "Laptop / phone call / jar boxes / tape gun, 1 second each"),
        ("REHOOK", "A lot of the time, I am the department.", "\"I AM THE DEPARTMENT\"", "Face, deadpan"),
        ("PAYOFF", "For specific tasks, I hire freelancers. But mostly, it's us.", "MOSTLY US", "Wide shot of the setup"),
        ("STEP", "Owning a business means you choose your own hours. Which can mean choosing to work more than a normal job.",
         "CHOOSE YOUR HOURS", "Clock / face, dry smile")],
       ["Most days, The Sunnah Foods is two people: me and my little sister.",
        "Running a small family business from my parents' house."],
       ["#familybusiness", "#smallbusiness", "#behindthescenes", "#blackseedhoney"],
       "THE WHOLE TEAM", "My whole company is me and my sister",
       series_beat=series("This is day X of building a honey company with my sister in my parents' house. Y jars to go.",
                          "Sister's hands labeling (with her OK) / jar placed in a row")),

    sc("40-gave-it-away", "Thousands given away", "S-14",
       [("78.0 STRONG", "Before I sold 1 jar, I'd given away thousands of dollars of honey.", "THOUSANDS. FREE."),
        ("76.4 STRONG", "I gave away thousands of dollars of honey before my first sale.", "GAVE IT AWAY")],
       [("HOOK", "Before I sold 1 jar, I'd given away thousands of dollars of honey.", "THOUSANDS. FREE.",
         "Face / jars being handed out, no faces without permission"),
        ("PROOF", "Kilograms and kilograms. To brothers at the masjid, my Sunday Quran group, and neighbours in my building.",
         "MASJID. QURAN GROUP. NEIGHBOURS.", "Masjid exterior / apartment hallway / jars"),
        ("STEP", "The Sunday Quran group was the first group I told. They were extremely supportive, and honest.",
         "THE FIRST GROUP", "Face, warm"),
        ("REHOOK", "Not all of it was nice. A lot of people loved it. A good amount gave me constructive criticism.", "NOT ALL NICE",
         "Face, dry"),
        ("PAYOFF", "That's my 1 piece of business advice. Solve a real problem. Give it away until demand gets too high. Then start charging.",
         "GIVE IT AWAY FIRST", "Face, close / jar")],
       ["Before my first sale, I gave away thousands of dollars of black seed honey.",
        "The one piece of business advice I'd give: give it away until demand is too high, then charge."],
       ["#businessadvice", "#smallbusiness", "#foundersjourney", "#muslimbusiness"],
       "GAVE IT AWAY", "I gave away thousands before my first sale"),
]


def main():
    os.makedirs(os.path.join(HERE, "scripts"), exist_ok=True)
    index, say_all = ["# Sunnah Foods batch 4: 10 founder-story scripts", ""], []
    for n, s in enumerate(SCRIPTS, 31):
        md, total = build.render(s, n)
        with open(os.path.join(HERE, "scripts", f"{s['slug']}.md"), "w") as f:
            f.write(md)
        index.append(f"{n}. [{s['title']}](scripts/{s['slug']}.md): {total:.1f}s, hook {s['hooks'][0][0]}, {s['story']}")
        say_all += [b[1] for b in s["beats"]] + s["caption"]
    with open(os.path.join(HERE, "draft.txt"), "w") as f:
        f.write("\n".join(say_all) + "\n")
    with open(os.path.join(HERE, "INDEX.md"), "w") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    main()
