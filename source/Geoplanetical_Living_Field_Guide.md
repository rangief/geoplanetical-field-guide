# Geoplanetical: The Living Player’s Field Guide

> Guide edition: 0.1 · Latest **recorded** game version: 1.1.4 / build 26709373 · 2026-11-18

Community-informed, independent player handbook. **Not official.** Chapters marked NEEDS REVIEW may be outdated following a patch.

## Contents

- [Start here](#00-start-here)
- [Your first year](#01-first-year)
- [Economy & trade](#02-economy-and-trade)
- [Supply chains](#03-supply-chains)
- [Construction projects](#04-construction)
- [Electricity & reserves](#05-electricity-and-reserves)
- [Budget & debt](#06-budget-and-debt)
- [Inflation & currency](#07-inflation-and-currency)
- [Politics & laws](#08-politics-and-laws)
- [Unrest & population](#09-unrest-and-population)
- [Warfare](#10-warfare)
- [Diplomacy & sanctions](#11-diplomacy-and-sanctions)
- [Research, intelligence & space](#12-research-intelligence-space)
- [Fix common problems](#13-troubleshooting)
- [What changed in 1.1.4](#14-patch-114)
- [Glossary](#15-glossary)

<a id="00-start-here"></a>

# Start here: run a country, not a spreadsheet

**The big idea:** In *Geoplanetical*, nearly every clever move has a side effect. Your job isn't to make every number green. It's to figure out which problem is actually causing the others.

> **The first rule:** Pause, save, inspect, change one or two things, then let the simulation respond. Changing fifteen policies at once is a superb way to learn absolutely nothing.

## Your opening five-minute check

1. **Are you already in trouble?** Look for war, sanctions, political crises or an imminent election. Those may matter more than your grand industrial ambitions.
2. **Is the economy actually growing?** Open **Economy → Summary** and distinguish the growth number from prices, jobs and capacity.
3. **Where is the state money going?** Open **State Budget → Summary**. Cash, annual balance and debt are separate things.
4. **Can the country power its promises?** Check **Electricity** for unserved demand, grid pressure and fuel supply.
5. **Are people getting better off?** Read approval and household conditions, not just GDP.

## The game's basic chain reaction

A new factory needs workers, electricity and inputs. If any one is missing, it may sit idle. If the inputs become more expensive, prices rise. Higher prices can upset households. Then your popularity falls just as your expensive new project comes due. Congratulations: you've created three ministries' worth of paperwork with one click.

## What's new in 1.1.4?

The developer redesigned the **country panel**, made the main **GDP, growth and inflation** figures more useful as entry points, and added **Twaddle**, a fictional social feed reacting to events. Treat Twaddle as flavour and context, not a substitute for checking the actual game panels. The patch also changed important economic and political balancing.

**Remember:** This guide is practical advice, not a list of universal magic percentages. When a future patch changes a mechanic, the relevant chapter will be flagged for review.

*Evidence: community beginner guides plus official 1.1.4 notes. Review triggers: interface, simulation balance, starting conditions.*


---

<a id="01-first-year"></a>

# Your first year without setting everything on fire

**The big idea:** The first year is for learning your country's limits. You don't need a perfect country by December. You need a country that still has options.

## Day one: take an inventory

Pause and create a named save. Check wars, sanctions, cash flow, debt rating, inflation causes, electricity, approval and the election calendar. Write down just the top **three problems**. If there are ten problems, congratulations, but you still only have three hands' worth of attention.

## First month: fix the immediate blockage

- **Already at war?** Read the War Council and your military position before touching domestic policy.
- **Budget losing money?** Identify the largest adjustable spending and revenue lines; small deliberate changes beat panicked wholesale cuts.
- **Industry stalled?** Check whether orders, workers, inputs or electricity are missing. A factory isn't a customer.
- **Election coming?** Consider how long unpopular reforms take to affect approval and voter expectations.

## Months two to six: watch cause and effect

Let policy changes settle. Many outcomes happen at monthly reviews or after construction and research delays. Check whether the *reason* you made the decision is improving. If you raised a tariff to support local industry, did output move, or did you merely make imported inputs pricier?

## Rest of the year: commit selectively

Choose one long-term bet: strengthen your energy supply, unclog construction, improve education, stabilise debt, or invest where real demand exists. Do not start five national megaprojects simply because five buttons are available.

### Example: the ambitious new president

You inherit weak electricity and a large deficit. Building three factories first sounds impressive; fixing the supply of power and the construction bottleneck is more likely to make those factories useful later.

**Avoid:** Treating an old guide's timing estimates as exact in 1.1.4. The game is receiving frequent balancing changes.

*Evidence: warmaninger's first-year guide and grayassembly's beginner lessons; general sequence is editorial advice, not a tested universal optimal strategy.*


---

<a id="02-economy-and-trade"></a>

# Why your economy isn't growing

**The big idea:** Capacity is how much your firms *could* produce. Demand is what people and businesses actually want to buy. Building more capacity doesn't create the customers.

## Check the right screen

Open **Economy → Summary** for activity and capacity. Then **World Statistics → Production and Trade** to inspect a specific good, including domestic production, imports, capacity and constraints.

### When businesses have spare capacity

Your firms may be able to make more, but orders are going elsewhere or don't exist. Look at household demand, government purchasing and competition from imports before spending on more factories. A new warehouse full of unsold goods is not economic growth.

### When firms are running flat out

Expansion starts to make sense only if there is demand to serve and the project can receive inputs, workers and electricity. Check **Business & Investment → Productive Investment** and the good's available capacity.

### When imports dominate

Tariffs may encourage some buyers to use local firms, but they also raise costs for firms that rely on imported materials. Trade agreements may limit the effect of a tariff. Compare the local producer price with the landed import price and examine the supply chain first.

### Example: the car factory problem

You fund vehicle assembly but don't have reliable electronic components. The shiny new factory isn't much help if suppliers cannot deliver. Fix the bottleneck before buying more empty production floor.

**Patch watch, 1.1.4:** The developer revised economic balancing, industry and nationalisation behaviour, and fixed several annexation-related accounting problems. Old screenshots or precise tariff thresholds need rechecking.

*Evidence: warmaninger and Balee_92 community guides; official 1.1.4 balancing notes. Suggested diagnostic order is not a guaranteed formula.*


---

<a id="03-supply-chains"></a>

# Supply chains: find the missing link

**The big idea:** A country isn't one big factory. It's a web. When an important input disappears, several industries can suffer at once.

## Four kinds of inputs worth recognising

- **Critical input:** Something an industry cannot easily do without.
- **Substitute group:** Several inputs may fill a similar role; losing one may not stop production if an alternative remains.
- **Yield input:** Production may continue, but efficiency falls.
- **Energy:** Even a complete supply chain won't perform if it cannot get electricity.

These categories come from **Balee_92's community-collected production map**, recorded around 10 November 2026. The source reported **107 goods**. That count and the recipes must be checked against newer builds before being treated as current.

## Follow a shortage upstream

Suppose military equipment is expensive. Don't jump straight to a new arms factory. Check whether machinery, semiconductors, electronics, chemicals, skilled workers or electricity are limiting existing plants. A shortage several steps upstream can make multiple finished products expensive at once.

## A practical investigation

1. Open the affected good under **World Statistics → Production and Trade**.
2. Check its inputs, electricity, staffing and delivery conditions where the game exposes them.
3. Inspect the most constrained upstream good.
4. Consider targeted production, trade adjustments or strategic reserves.
5. Revisit the result after the next relevant simulation update.

### What about electronic components?

Balee_92 reported that electronic components were a major dependency in the recorded recipes. That's a **valuable clue**, not a guarantee that the same count or recipe tree holds after 1.1.4.

**Avoid:** Copying a historical supply-chain diagram into a new guide and calling it a live 1.1.4 database. The full recipe dataset is not present in the supplied text file.

*Evidence: Balee_92, community-recorded recipes. Review triggers: goods catalogue, recipe changes, trade, strategic reserves.*


---

<a id="04-construction"></a>

# Construction: why your projects are stuck

**The big idea:** Starting a project is easy. Getting materials, labour and usable building capacity is the hard part.

## The 'why isn't it building?' checklist

Visit **Economy → Construction Projects** and read the project's actual warning. Are deliveries late? Is funding suspended? Is the construction order book overloaded? Is a required material missing? Those are different problems, and they need different fixes.

### Project delayed by materials

Check the specific missing input. The older community analysis highlights **industrial minerals**, **construction materials**, water services and construction capacity as important parts of the building chain. Verify the current good's actual requirements before reacting.

### Too many projects at once

Projects compete for builders and materials. Starting five new projects can slow all five. Prioritise the one that removes the biggest bottleneck, then let capacity recover.

### Financing problem

Read whether the project is short of state funding, company funding or access to credit. Sending more materials won't repair a financing suspension.

### Example: the road to nowhere

You approve power plants, a factory and new housing together. They all need construction services. If the local sector is already at capacity, the schedule can slip across the board. Try sequencing the capacity-creating project first.

**Old-number warning:** The original guide contains specific project-size percentages and timing estimates derived from earlier code. This edition deliberately does not treat those as guaranteed for 1.1.4.

*Evidence: warmaninger's construction guide; verify exact construction formulas and project requirements after each relevant patch.*


---

<a id="05-electricity-and-reserves"></a>

# Electricity and reserves: keep the lights on

**The big idea:** Building more electricity capacity won't fix every power shortage. Sometimes the problem is fuel, storage, the grid or the location of the plant.

## Diagnose before building

Open **Electricity** and look at **Unserved**, the **adequacy margin**, fuel reserves and grid conditions. Ask which of these is actually limiting delivery.

- **Not enough usable generation:** Consider new power capacity and its construction timeline.
- **Fuel not arriving:** Inspect supply routes, sanctions and stockpiles before ordering another fuel-burning plant.
- **Renewables being wasted:** Check whether the grid needs storage, flexible generation or a different mix.
- **No suitable site:** The game's placement information should explain local output potential and blocked sites.

### Why 1.1.4 matters here

The latest verified patch made power output more dependent on local conditions and added clearer site estimates. It also expanded strategic reserves, including materials such as lithium, cobalt, nickel, rare earths, uranium and phosphate. Exact storage limits should be taken from the current game panel rather than memorised from older guides.

### Example: more solar, same blackout

Your country builds extra solar facilities but still loses power at the wrong time of day or season. That suggests checking storage, flexible generation and grid conditions instead of assuming the construction project failed.

**Avoid:** Treating a country's inherited electricity shortage and a *worsening* shortage as necessarily equivalent. The community guide reports baseline-related mechanics, but those details need current-game verification.

*Evidence: warmaninger's energy guide; official 1.1.4 energy and reserves changes.*


---

<a id="06-budget-and-debt"></a>

# The budget: cash, deficit and debt aren't twins

**The big idea:** A country can have money in the bank while running a deficit, or have a balanced annual budget while still carrying enormous debt.

## Three things to keep separate

- **Cash:** What the state has available now.
- **Balance or deficit:** Whether incoming government revenue covers spending over the period shown.
- **Debt:** Money owed from earlier borrowing and financing.

Open **State Budget → Summary** and read all three, plus the cost of new borrowing and the country's rating.

## If you're running out of money

Identify what's driving spending. Energy support, public services, defence and investments can behave differently. Don't cut everything equally. Consider what each cut would do to households, employment, approval and future output.

## If debt is climbing

Check whether the state is still borrowing, whether debt repayments are due, and whether your interest costs are changing. A healthy-looking budget headline does not necessarily include every one-off project or military expense.

## How to make a change without wrecking approval

Look at the projected consequences, move in small steps where possible, and watch how the economy responds. A sudden dramatic cut can solve one line and create a protest problem elsewhere.

### Example: the cheap tax cut

You lower taxes to stimulate business but then borrow heavily to keep services running. The apparent win may be offset by weaker finances and higher borrowing costs. The useful question is whether output and household conditions actually improved.

**Patch watch, 1.1.4:** Budget balancing, tax reactions, and several annexation accounting cases changed. Never copy old exact revenue multipliers into this edition without fresh evidence.

*Evidence: warmaninger and grayassembly; official 1.1.4 fiscal/political balancing changes.*


---

<a id="07-inflation-and-currency"></a>

# Inflation: don't treat every price rise with the same hammer

**The big idea:** A high inflation number tells you that prices are rising. It doesn't automatically tell you why.

## First stop: Price pressure

Open **Economy → Summary → Price Pressure**. Check whether the game attributes price changes to shortages, production costs, taxes, monetary conditions or other factors. Then visit **Money & Finance → Currency & Central Bank** to inspect policy rates and currency conditions.

### When prices rise because things are scarce

A higher interest rate won't instantly produce food, electricity or electronic components. Check the shortage itself, import restrictions, transport and realistic construction options.

### When monetary policy is involved

Interest rates can influence spending and investment, but usually with delays and side effects. Before taking control of the central bank, understand what the current policy is doing and why.

### When the currency is under pressure

Read foreign reserves, foreign obligations and monetary confidence. A dramatic currency change may be irreversible in some game configurations, according to the older community analysis. Confirm the current option's warning before clicking it.

### Example: the tax that made everything worse

A tariff protects one local industry, but several other firms use that imported good. Their costs rise and inflation gets worse. The real fix may be a narrower tariff, cheaper inputs or new domestic production.

**Important 1.1.4 correction:** The developer explicitly changed the **inflation algorithm**. The early-launch guide by **Traslo** says interest-rate control is the main solution; that should be treated as **historical player advice**, not a current universal rule. Precise numerical claims from earlier builds require retesting.

*Evidence: Traslo's early-launch inflation guide; warmaninger's differentiated price-pressure analysis; official 1.1.4 patch.*


---

<a id="08-politics-and-laws"></a>

# Politics: a good policy can still cost you the election

**The big idea:** The game doesn't only ask what a policy costs. It asks *who* bears that cost and how they react.

## Read more than one political number

Approval, stability, parliamentary support and an upcoming election are related but distinct. A popular government may still struggle with a coalition. A law may have support in principle but trigger a veto, partner dispute or public backlash.

## Before proposing a law

1. Open **Politics → Legislation** and read the proposed effect.
2. Check votes and coalition partners.
3. Look for consequences for affected groups.
4. Consider whether a smaller reform is safer than a sweeping change.
5. Give the outcome time to appear before changing ten more laws.

### Example: the reform that passes but hurts

You increase an unpopular tax to repair the budget. The law passes, but disposable income falls and approval suffers. The country may be financially steadier yet politically less stable. That isn't a contradiction; it's the trade-off.

## New political wrinkles in 1.1.4

The patch expanded **leader personalities**, redesigned parts of the government UI, and added new legal options around **political policing**, **exit rights** and the **role of the head of state**. These introduce different consequences and choices from older beginner guides. Treat the in-game previews as the source for any specific outcome.

**Avoid:** Using an old exact approval threshold as though it guarantees victory or prevents every crisis. The developer adjusted tax reactions and social-group support in 1.1.4.

*Evidence: warmaninger on legislation and approval; grayassembly on population reaction; official 1.1.4 politics notes.*


---

<a id="09-unrest-and-population"></a>

# Unrest, migration and people: listen to the cause

**The big idea:** A protest is a symptom. Suppressing the symptom won't necessarily fix the problem producing it.

## When a movement appears

Open **People → Movements**. Read its demand and what is pushing it. Is it about purchasing power, employment, public services, war, rights or a specific reform? Then inspect the group or region affected.

A useful response starts with the underlying cause. If living costs are the issue, focus on prices and incomes. If unemployment is the issue, empty promises about GDP may not help. Strong security responses may have additional political and social consequences, so read the game's previews.

## When your population shrinks

Check **People → Demographics** and **People → Migration**. Births, deaths, arrivals and departures have different causes and timelines. A better migration policy may not help if housing, safety or jobs are the real deterrent.

### Example: the attractive country nobody moves to

You loosen immigration rules but still have poor housing access and economic instability. The problem may be your country's attractiveness or capacity to receive migrants, not the formal cap.

## Version 1.1.4 changed the picture

The patch altered how some family policies affect births and introduced leader traits and laws that can influence public order and political reactions. That's a strong reason not to rely on the older guide's exact demographic timescales.

**Avoid:** Treating approval, stability, loyalty and the threat of unrest as the same number. They answer different questions.

*Evidence: warmaninger's protest and population sections; official 1.1.4 family/political changes.*


---

<a id="10-warfare"></a>

# War: the invasion is only the beginning

**The big idea:** Winning a battle, winning a war and living with the consequences are three different achievements.

## Before declaring war

Open the **War Council** and inspect the campaign objectives, balance of forces, expected political cost, international reaction and possible sanctions. Check whether your troops can actually reach the target and whether you have permission to use allied or foreign bases for combat.

### During a campaign

Look at **Defense → Command**, available formations, supply, equipment, military support and the war's progress. Don't assume that buying more equipment instantly creates a useful force at the right location.

### The 1.1.4 changes worth knowing

The developer improved **successive island landings**, **naval landing support**, **carrier-based air operations**, **strategic bomber range with support aircraft**, and **combat access to foreign-hosted bases**. The war panel also gives clearer ways to request allied involvement and explains refusals.

### Example: you have a base, but cannot attack from it

Owning aircraft at a friendly country's base does not necessarily mean the host allows attacks against your enemy. Check the war declaration and base-access information first. Otherwise your entire brilliant air plan might remain a very expensive parking arrangement.

## After fighting stops

Peace arrangements, sanctions, occupation and territorial changes may affect state finances and population services. The 1.1.4 patch altered several annexation and occupation behaviours, so older examples should be treated as scenarios, not fixed calculations.

**Avoid:** Relying on an older guide's precise army power ratios without new gameplay evidence.

*Evidence: warmaninger's conquest/defence guide; official 1.1.4 war and access notes.*


---

<a id="11-diplomacy-and-sanctions"></a>

# Sanctions and diplomacy: find the real price of a war

**The big idea:** Your army may win territory, but disrupted trade and angry neighbours can create problems for years.

## What sanctions actually disrupt

Read **Diplomacy → Sanctions and Crises**. Identify who is imposing measures, what is restricted, and which important goods or routes are affected. Then check **Production and Trade** for the knock-on effects. Not every sanction has the same consequences.

## Three useful questions

1. **What caused this sanction?** A war, conduct during occupation, a diplomatic dispute or another issue may call for different responses.
2. **Which partners matter most?** Focus first on the flows your economy actually relies on.
3. **What can you change?** Negotiation, policy change, alternative suppliers or more resilient domestic capacity may each help, with different costs.

## What's easier in 1.1.4?

The developer consolidated sanctions management and replies, added a way to approach willing countries more directly, and expanded automation for sanctions discussions. Check the current **Sanctions** screen rather than following an old button-by-button route.

### Example: the factory hit by a distant war

You never sent a soldier abroad, but one of your industrial suppliers gets caught in sanctions. Local prices rise because an essential input no longer arrives normally. Investigate the trade link before blaming the factory manager.

**Avoid:** Thinking sanctions are always a single direct deduction from GDP. Their effects can travel through goods, prices, confidence, approval and budget receipts.

*Evidence: warmaninger's sanctions guide; official 1.1.4 sanctions changes.*


---

<a id="12-research-intelligence-space"></a>

# Research, intelligence and the Moon: play the long game

**The big idea:** Some of the most exciting buttons in Geoplanetical have the longest delay before they pay off.

## Research: discovery isn't deployment

Open **Science & Technology** and inspect research points, delivery and whether the country can use the result. The older community analysis argues that education, administration and infrastructure affect how quickly innovations spread. Treat this as a useful framework and verify any exact current-game formula.

## Intelligence: define the objective

Use **Intelligence → Services** to inspect available agents, staffing and operations. Don't treat intelligence spending as universally free or riskless based on an older guide. Look at the current costs and consequences.

## Space: ambitious, but not magic money

Open **Space → Program**. Read mission access, research requirements, funding and settlement needs. A Moon programme can be a long-term national challenge, but it competes with domestic priorities.

### Example: the Moon-first presidency

Your country is short of power, short of money and struggling with skilled workers. A space programme can still be your chosen goal, but understand what you postpone to fund it. There's nothing wrong with playing for the spectacle; just don't confuse spectacle with a free economic fix.

**Patch watch, 1.1.4:** The **Space panel** was redesigned with clearer mission tracking and settlement controls, while Agenda links and launch access were improved. The older guide's exact Moon research budgets and timelines are not verified for this build.

*Evidence: warmaninger's long-term planning section; official 1.1.4 space-panel notes.*


---

<a id="13-troubleshooting"></a>

# The 'something is broken' checklist

Before reporting a bug, distinguish an unexpected outcome from a genuine fault. A project waiting for materials, an election lost after unpopular laws and an idle factory without orders may all be working exactly as designed.

## Situation: factories won't grow

**Check:** Orders, available capacity, missing inputs, workers and electricity. **Try:** Fix the limiting factor first, not the most visible number.

## Situation: inflation keeps climbing

**Check:** The **Price Pressure** breakdown, monetary conditions and shortages. **Try:** Address the largest plausible driver. **Don't:** Assume the central-bank rate fixes every kind of price rise.

## Situation: construction is frozen

**Check:** **Construction Projects → Needs Attention**, material deliveries and financing. **Try:** Read the exact warning and remove the relevant bottleneck.

## Situation: popularity collapses

**Check:** Real household conditions, recent legislation, elections, protests and public services. **Try:** Work back to the latest major change and its affected groups.

## Situation: military units won't move or attack

**Check:** Orders, access permissions, appropriate formations and supply. In 1.1.4, foreign-base combat permission is an especially useful thing to inspect.

## Situation: the game crashes or behaves impossibly

Create a named save if safe, note your **exact game version/build**, affected country, installed mods, steps to reproduce and any on-screen error. Test the same situation without third-party code mods only when your own backups and mod installers make that safe. Never destroy working files merely to prove a point.

## Situation: an online guide disagrees with your game

Check the guide's **last reviewed build**, the claim's evidence label and the most recent patch notes. If there is a mismatch, trust what the current game actually shows over old copied numbers and mark the guide section for review.

*Evidence: synthesis of four community guides; 1.1.4-specific note from official patch. Troubleshooting is advisory, not a proof that no bug exists.*


---

<a id="14-patch-114"></a>

# What's changed in Geoplanetical 1.1.4?

**Verified reference:** official patch notes titled *Balancing, Fixes, UI, (Everything) & Twaddle Social Feed - 1.1.4* (16 November 2026). Public Steam build **26709373** is the latest verified reference at the creation of this edition, not a guarantee about future builds.

## Changes that affect this handbook

| Topic | Patch change | What to revisit |
|---|---|---|
| **Economy & prices** | Inflation algorithm, budget balance and tax reactions updated | Old inflation percentages, tax 'rules' and approval estimates |
| **Industry** | Nationalisation and some annexation accounting corrected | Old examples of buying, seizing and managing industries |
| **Politics** | Leader personalities, new political laws and government roles | Law outcomes, protests and political strategy |
| **War** | Landings, air operations, foreign-base access and military reporting | Old invasion and aircraft guides |
| **Sanctions** | Centralised management, responses and automated discussions | Old click-by-click sanctions routes |
| **Energy & reserves** | Site-specific plant output and more reserve categories | Old energy-site and stockpile numbers |
| **Space** | Redesigned Space panel, improved launch-access links | Old button locations and settlement walkthroughs |
| **Navigation** | Country panel, top-bar drilldowns, trade screen and Twaddle | Old UI screenshots and menu routes |

## Not every old number survived

A numerical threshold in a November community guide is **not automatically wrong**, but it is **not automatically verified** just because the new update didn't mention it. That's why this edition uses decision rules and on-screen checks instead of filling the page with apparently exact calculations.

## What happens when 1.1.5 arrives?

The new patch goes into `data/patches.json`; impacted chapters are flagged **Needs review**. Editors inspect the note and, where necessary, the current game. Only those chapters are revised and marked reviewed. The rest stay as they are. See `MAINTAINERS.md` for the commands.

*Source: Geoplanetical's official Steam announcement and public-build tracking.*


---

<a id="15-glossary"></a>

# Plain-English glossary

**Approval:** How positively people currently view the government. Not identical to stability or votes.

**Stability:** How solid the country's political order is. May move differently from short-term approval.

**GDP:** A broad measure of economic production. More GDP does not necessarily mean every household is better off.

**Inflation:** The speed at which prices are rising. Slower inflation doesn't mean prices went back down.

**Real income:** Money's purchasing power after taking price changes into account.

**Capacity:** The amount a business or industry could produce under the relevant conditions.

**Demand:** The orders and consumption that actually give producers something to sell.

**Critical input:** A material or service a production process cannot easily replace.

**Tariff:** A tax on imports. Can affect consumers and companies that use imported inputs.

**Deficit:** Government spending exceeding revenue over a period.

**Debt:** Money still owed from borrowing. Different from the money the state has today.

**Foreign reserves:** Foreign currency assets that can matter for currency arrangements and external payments.

**Sanctions:** Measures restricting trade or other international relationships; inspect the specific measures rather than assuming all sanctions work alike.

**Unserved electricity:** Demand for electricity that isn't being supplied.

**Build number:** A particular Steam game build. A numbered game version such as `1.1.4` may have more than one build.

**Community finding:** Advice or a claim supplied by players, which may need fresh verification.

**Developer-confirmed:** A feature or change reported in the game's official patch notes; not necessarily proof of every implied gameplay outcome.

**Needs review:** The guide has identified a relevant newer patch and hasn't revalidated this chapter yet.

*Evidence: simplified terminology drawn from the supplied guides; definitions are explanatory, not substitutes for the current game UI.*


---

