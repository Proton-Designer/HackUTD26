---
name: 12-visual-design
description: Open when setting the team's design tokens and chart theme in hour 1, choosing number vs chart vs table for any result, laying out the first screen a judge sees, showing model confidence or a forecast, running the hour 18-22 polish pass, or building slides, the Devpost thumbnail, or a table poster.
---
# Visual design and information presentation

## Use this when
- Hour 1-2: four people are about to build screens in parallel and nobody has fixed the palette, type, spacing, or chart theme yet.
- A result has to go on screen or on a slide ("we cut time 5x", "92% accuracy", "model is 0.87 confident") and you must pick big number, chart, or table, then pick which chart.
- Laying out the main demo screen or dashboard, which a judge standing 1-2 m from the laptop will read in a few seconds.
- Hour 18-22: features work, the UI looks "off" or bland, and there are about 2 hours for polish.
- Building the pitch slides, the Devpost gallery thumbnail, or a printed table poster.
- A teammate or an AI snippet proposes a pie, gauge, radar, 3D chart, resized-icon pictogram, map, or "futuristic cockpit" look.

## Core principles
1. **Every view gets exactly one focal point. Create it by muting everything else, not by making the focal point louder (counterintuitive).** Viewers give a visual about 3-8 seconds and spot one difference in color, size, or position before reading anything. Keep highlighted material to about 10% of the view. [Knaflic, Storytelling with Data, p.141-147, 151] [Few, Show Me the Numbers, p.88, 99] [Refactoring UI, p.34-35] [Lupton, Thinking with Type, p.99-100]
2. **Choose every low-level value from a fixed set picked in hour 1, written down for all builders, and never nudge pixels.** Four builders with no shared spec ship four styles that read as four products. Spacing steps differ by at least 25%; allow about 3 card sizes (1x, 2x, full width), because fewer sizes look calmer. [Refactoring UI, p.21-25, 53-58, 81-86] [Lupton, p.134] [Muller-Brockmann, Grid Systems, p.7, 9, 123]
3. **Hierarchy has to work in grayscale before any color goes on (counterintuitive).** Use weight and text color as well as size: about 3 text colors (dark, mid gray, light gray), 2 weights, nothing under 400. Make labels smaller and grayer than their values, or drop them when the format is obvious. [Refactoring UI, p.8-10, 28-31, 36-40] [Bringhurst, Elements of Typographic Style, p.55-56]
4. **If two things differ, make them very different.** 12pt vs 14pt, or dark brown vs black, reads as a mistake, not contrast. Use about 1.5-2x between adjacent text levels, and stack 2-3 differences between a key number and its supporting text. [Williams, Non-Designer's Design Book, p.115, 124] [Lupton, p.42] [Muller-Brockmann, p.39]
5. **Group with space before you add boxes, and delete borders before you add effects (counterintuitive).** Gaps between groups must be larger than gaps within a group; borders split the screen into boxes the eye processes one by one. Grouping strength runs enclosure > connection > proximity/similarity, so save a filled card for the one group you want to stand out. [Williams, p.22-24] [Few, Information Dashboard Design, p.75, 87-92] [Refactoring UI, p.77-80, 193-196]
6. **Never show a number alone: ask "compared to what?" and put the baseline next to it.** A two-point before/after chart of a speeding crackdown looked like success until neighboring states showed the same drop. "3 min vs 20 min manually" persuades where "saves time" doesn't. Chart the gap around a labeled zero line when the claim is "X vs Y". [Tufte, Visual Display, p.71-72] [Few, Information Dashboard Design, p.43-47] [Few, Show Me the Numbers, p.135-137]
7. **Write the takeaway sentence first, then let its wording pick the form.** "Changed over time" points to a line, "larger than" to sorted bars, "vs plan" to a deviation chart, one or two numbers to big text. A chart wrapped around a simple trend wastes space; save charts for rich, variable data. [Few, Show Me the Numbers, p.121-125] [Knaflic, p.67-69, 78] [Tufte, p.27]
8. **Show quantity with length or position, using one dimension only; never angle, area, 3D, or a resized icon.** A class asked to judge a true 16:1 circle ratio guessed 5 to 50. Scaling an icon in width and height squares the change: one 454% rise drawn as a barrel read about 59 times too large. Repeat identical icons instead. [Few, Show Me the Numbers, p.91-93] [Tufte, p.66-68] [Chopra et al., Data Handling and Visualization, p.130]
9. **Keep the Lie Factor between 0.95 and 1.05, and start bars at zero.** Lie Factor = size of effect shown / size of effect in data; Tufte measured newspaper charts at 2.8 to 14.8. A truncated axis turned a 13% rise into an apparent 460% jump. One judge who spots it stops trusting every number. For a tight range like 91% vs 94%, use a dot plot. [Tufte, p.54-55, 59] [Knaflic, p.83-86] [Chopra et al., p.118-121]
10. **Make everything gray, give the one key series the single accent, and use hue only for categories.** Ordered values get one hue light-to-dark or Viridis, never a rainbow, which invents boundaries that aren't in the data. With more than 4-5 colored series, highlight one and gray the rest. [Knaflic, p.123-126, 157-160] [Chopra et al., p.155-158] [Tufte, p.148]
11. **Never let color carry meaning alone. Use blue vs orange instead of red vs green, and add an icon or label.** About 1 in 12 men has a color-vision deficiency, and projectors wash out hue for everyone. Check every screen in grayscale and in the devtools vision-deficiency emulator. [Chopra et al., p.157-160] [Tufte, p.176] [Duarte, slide:ology, p.132-133]
12. **Polish changes how usable judges think the product is, but cannot rescue thin data or a broken demo.** Better-looking designs are rated easier to use. If a chart looks boring, find a sharper number or comparison; decoration never makes thin data interesting. [Lidwell, Universal Principles of Design, p.30] [Tufte, p.116] [Duarte, p.233]

## Decision procedure
Run this for every widget, chart, or slide that shows information.

1. **Write the takeaway** as one sentence, naming the audience (the table judge or the sponsor judge) and what they should remember. If you can't, the content is exploratory: move it to a backup slide or the README and stop. [Knaflic, p.47, 49-50]
2. **Count the values that carry the message.**
   - 1-2 values: big number plus delta vs baseline, optional sparkline. Stop; no chart.
   - 3 to about 12 values where pattern or comparison matters: chart (step 3).
   - Judges may need exact values: an aligned table in the UI (tabular numerals, right-aligned, no cell borders), never on a live slide. Pull the key row out as a chart or sentence. [Few, Information Dashboard Design, p.102-106] [Lupton, p.204-206] [Bringhurst, p.70-72]
3. **Pick the form from the wording of the sentence.**
   - Over time: line if samples are evenly spaced, dots if irregular.
   - Across categories, or a ranking: horizontal bars sorted by value.
   - Share of a whole: sorted bars, with "of 100%" in the title.
   - Vs target or baseline: deviation bars or line around a labeled zero.
   - Spread (latency, scores): low/median/high marker bars, never the mean alone.
   - One KPI against a target: bullet graph, never a gauge.
   - Several variants or segments: small multiples with identical axes on one screen, never tabs the judge must remember across. [Tufte, p.163-168]
   - Model confidence or risk: "about 9 of 10 similar cases" plus a 10x10 dot array, not a bare 0.87. Forecasts get a shaded range band. [Chopra et al., p.106-111]
   - Map only if location itself matters. Two units: two stacked charts, never a dual axis.
   [Few, Show Me the Numbers, p.126-146] [Few, Information Dashboard Design, p.49-51, 107-111]
4. **Check the series count.** More than 4 colored series: highlight one, gray the rest. More than 8 categories: top 4-5 plus "Other". Hundreds of points: opacity 0.3-0.5. [Chopra et al., p.122, 135-136]
5. **Integrity gates. A chart that fails any of these does not ship.**
   - Bar axis min is exactly 0; tighter range means switch to dots.
   - Ruler check: longest/shortest mark ratio matches the data ratio within 5% (Lie Factor). [Tufte, p.54-55]
   - Compared panels share one scale. Units and denominators match (per user, per minute, or percent). [Tufte, p.57-58] [Lidwell, p.90]
   - Forecasts are dotted or labeled FORECAST. Footnote gives n, source, and an "as of" time. [Knaflic, p.199] [Few, Show Me the Numbers, p.149-153]
   - Fix "wrong" (scale errors) before "bad" (misleading perception) before "ugly". [Wilke, Fundamentals of Data Visualization, p.19-20]
6. **Declutter in erasing rounds.** Remove frame and ticks; mute or drop gridlines; drop markers and redundant labels. Never rotate axis labels (45-degree text reads 52% slower): flip to horizontal bars. Label series directly, colored to match. Round to the precision the decision needs ($3.8M). [Knaflic, p.119-130] [Tufte, p.95-100]
7. **Focus.** Gray everything, accent the one key bar or line, add 2-3 annotations at key points. The title is the takeaway sentence, not a topic label. [Knaflic, p.182-186] [Duarte, p.94-97]
8. **Go/no-go test.** Show it 5 seconds to someone who didn't build it and ask what it says. Correct: ship. Wrong: back to step 3. Correct but slow, or they ask what a color means: back to step 6. [Knaflic, p.105] [Tufte, p.147]

For whole screens:
- Squint and count where the eye stops. More than 3-5 stops: merge into groups. [Williams, p.50]
- The largest element is the most important one, not the easiest to build. Rank widgets 1..N before layout and give rank 1 the biggest field. [Knaflic, p.156] [Muller-Brockmann, p.84]
- Exactly one filled button. [Refactoring UI, p.46-49]
- Main view: 3-6 summary numbers plus an exceptions list on one screen, no scrolling. [Few, Information Dashboard Design, p.39-42, 82-83]

## Checklists

**A. Hour-1 token sheet (30 min, shared with all four builders before any UI work)** [Seed: A. Hackathon visual kit, §A1] [Refactoring UI, p.21-25]
- [ ] Spacing 4/8/16/24/32/48/64. Type 12/14/16/20/24/30/36, body 16, line-height 1.5 body, 1.1-1.25 headings.
- [ ] One family (Inter, Geist, or system stack), weights 400-700, real files loaded for each weight used (no browser-faked bold or italic). Paste a test string first: product name, a name with diacritics, digits 0-9, $ and %. Text colors gray-900/600/400, never #000. [Bringhurst, p.95-96, 185] [Lupton, p.48]
- [ ] One brand hue with shades 50-900, semantic colors each paired with an icon or text, at most about 5 hues. Sequential data: Viridis or one-hue ramp; categories: a ColorBrewer colorblind-safe set. [Williams, p.325-326] [Chopra et al., p.158-159]
- [ ] One radius, shadows sm/md/lg/xl by elevation, prose max-width about 65ch, page max 1024-1280px.
- [ ] `font-variant-numeric: tabular-nums` and right alignment on every metric, table column, and live counter, so numbers line up and stop jittering. [Lupton, p.56-57] [Bringhurst, p.71-72]
- [ ] One chart config used by every chart: beginAtZero, data line 2px, axes and grid 0.5-1px light gray or off, no border, gray series plus accent, direct labels, sorted data, shared number formatter, containers about 3:2. [Tufte, p.178-183]

**B. Screen polish pass (15 min per demo-path screen, reviewer who didn't build it)** [Williams, p.19-20, 342] [Seed: A. Hackathon visual kit, §A2]
- [ ] Squint/grayscale: the intended element is still obviously first. Accent covers about 10% of the screen or less.
- [ ] Proximity: within-group gaps < between-group gaps; each heading sits closer to its own content than to the block above.
- [ ] Alignment: one strong left edge, no "almost aligned" elements, no centered heading over left-aligned text. [Williams, p.77-78]
- [ ] Remove every second border, cut every element the demo script never touches, then bump card padding one step. [Refactoring UI, p.49-53]
- [ ] Body contrast at least 4.5:1, large text 3:1. On colored panels use a tint of the panel's own hue, not gray. [Refactoring UI, p.31-34, 131-135]
- [ ] Icon-only buttons only for close, search, settings; label the rest. [Lupton, p.98]
- [ ] Empty, loading, and stubbed states styled, not raw spinners (judges often try a fresh account). Test with the longest and shortest real strings. [Refactoring UI, p.189-192] [Bringhurst, p.178]
- [ ] Readable from 2-3 m on the actual demo laptop at low brightness; zoom to 125-150% if needed. [Duarte, p.143, 152] [Lupton, p.41-42]

**C. Slide, thumbnail, and poster pre-flight** [Duarte, p.28-29, 140, 143] [Knaflic, p.228-230]
- [ ] One idea and an action title per slide; reading only the titles tells the story.
- [ ] Under 50 words per slide (75 means it's a document), text 28-30pt or larger, no live tables, never a table and a chart of the same numbers.
- [ ] Product name and logo on first and last slides only. One template, broken once on purpose for the headline-metric or demo slide. [Bringhurst, p.166] [Reynolds, p.139-140]
- [ ] Devpost thumbnail at 3:2: product screenshot, name, tagline, high contrast, app's brand color. [Seed: A. Hackathon visual kit, §A5]
- [ ] Poster: headline at standing eye height (about 170 cm), one claim plus about 3 images, readable from 2-3 m, content well inside the trim edge. [Muller-Brockmann, p.35, 129-130]
- [ ] Deck exported and shown once on the exact machine and screen used for judging. Backup slide with raw numbers, method, and n. [Bringhurst, p.194-195] [Duarte, p.88]

## Anti-patterns
1. **Shipping the library default chart.** Tell: a donut from an AI snippet, a legend box, heavy gridlines, auto-scaled axis, pattern fills. Fix: route every chart through the shared config in checklist A. [Tufte, p.102-108]
2. **The bare model score.** Tell: "confidence 0.87" or a single forecast line. Fix: restate as "about 9 of 10 similar cases" with a dot array, and draw the range band. [Chopra et al., p.108-111, 115-116]
3. **Comparison hidden behind tabs.** Tell: the judge clicks between model variants or segments and has to remember the last view. Fix: one row of small multiples with identical axes. [Tufte, p.163-168]
4. **Color confetti.** Tell: every series, widget, or row has its own hue, or the accent is on buttons, links, headings, and icons at once. Fix: gray everything, one accent for "look here", same meaning for each color on every screen. [Williams, p.114] [Chopra et al., p.151-155]
5. **The cockpit look.** Tell: radial gauges, glow, dark gradients behind charts, 3D. Fix: go flat, use bullet graphs, solid background. A gradient behind a chart makes identical bars look different. [Few, Information Dashboard Design, p.12-13, 58-61] [Few, Show Me the Numbers, p.93-94]
6. **Boxes inside boxes.** Tell: border plus shadow plus background on every card, even spacing everywhere. Fix: separate with spacing, then a background tint, then a light shadow. Delete borders wherever a tint is present. [Refactoring UI, p.193-196]
7. **Four teammates, four styles.** Tell: three button styles, two radii, mixed icon sets, 13px or 17.5px sizes, a second or third font, browser-faked italics. Fix: freeze the token sheet in hour 1, one icon library, reject arbitrary values in review. [Refactoring UI, p.14-20] [Muller-Brockmann, p.39, 150] [Bringhurst, p.58-59]
8. **Slide as document.** Tell: bullets on every slide, text under 24pt, a feature-comparison grid. Fix: one phrase plus one visual per slide, a real screenshot instead of stock art, detail moved to the README. [Reynolds, p.140-146] [Bringhurst, p.192-193]
9. **Decorative motion.** Tell: things pulse, fly in, auto-animate. Fix: motion only for a real alert or to show a state change; at most one signature animation, and it should reveal data. [Few, Information Dashboard Design, p.71] [Tufte, p.111-113]
10. **Full-width text.** Tell: LLM output runs edge to edge on a wide monitor. Fix: cap prose at 45-75 characters (aim for about 65ch), line-height about 1.5, break long model output into short sections with subheads. [Bringhurst, p.26-27] [Muller-Brockmann, p.30] [Refactoring UI, p.90-93]

## Hackathon calibration
- **Borrow the system, don't build it.** Tailwind plus shadcn/ui defaults already follow Refactoring UI's scales; change only the brand hue and font. Skip HSL shade-building, custom modular scales, kerning, and font tinkering. [Seed: A. Hackathon visual kit, §A1] [Refactoring UI, p.119-128] [Bringhurst, p.199]
- **A system is itself a differentiator.** Most deadline-driven display work skips a layout system; a 30-minute grid and style sheet makes you look planned in a 200-project room. [Muller-Brockmann, p.137-138]
- **Time budget:** 30 min of tokens at the start; 20-30 min of grayscale sketching per core screen at real size with real copy, then build in the browser; a protected polish block of about 2 hours; about 90 min for the deck inside the final 3-4 hours. [Lupton, p.192] [Muller-Brockmann, p.42, 85-86] [Reynolds, p.125, 128-129]
- **Science-fair viewing conditions dominate.** A judge stands about 4 minutes, glances at the screen for seconds, and may try the app cold. Put the headline metric top-left, keep logo, filters, and instructions small (you narrate), and test at standing distance. [Few, Information Dashboard Design, p.56-57, 92-94] [Knaflic, p.164-165]
- **Projectors wash out pastels, mid-tones, thin strokes, and yellow.** Use very dark on very light or the reverse, and bump weight one step if thin type vanishes on the venue screen. [Duarte, p.132-133] [Bringhurst, p.193, 237]
- **Pick one dashboard role and fake live data.** Most demos should be "strategic" (one-glance answer) or "operational-feeling". Replay recorded data instead of building streaming. Build one drill-down: overview, flagged exception, one click to detail. [Few, Information Dashboard Design, p.27, 31-33, 82]
- **Ignore for this event:** paragraph indents, justification, hyphenation, widows, old-style figures, and optical kerning (except the logo and README); print and CMYK unless you print a poster (then proof early); iterative user testing beyond one 5-second stranger test per key screen.
- **If the demo path is broken, fix it before touching the theme.** Polish multiplies a working demo; it doesn't replace one. [Duarte, p.233]

## Where experts disagree
- **Pie charts.** Few, Knaflic, and Tufte ban them (Tufte calls several pies nearly useless). Duarte allows up to 8 clearly different slices; the seed kit allows 2-3. Follow the ban: sorted bars with "of 100%" in the title. If a sponsor template forces a pie, 3 slices or fewer, labeled directly. [Few, Information Dashboard Design, p.47-48] [Tufte, p.171] [Duarte, p.92-93] [Seed: C. Information presentation, §C2]
- **Small data: table or chart?** Tufte says 20 numbers or fewer belong in a table; Few and Knaflic keep tables off live slides because audiences won't scan them while you talk. In the app, a 3-5 row aligned table (baseline vs ours) is fine. On a slide, use a big-number row or sorted bars. [Tufte, p.30, 171] [Knaflic, p.71]
- **Density vs white space.** Tufte and Lupton say a dense, well-organized screen beats several sparse ones; Muller-Brockmann and Refactoring UI say remove an element and add padding when in doubt. Make the first screen a judge sees spacious, and allow density only in the one analytic view a technical judge explores. [Tufte, p.155-162] [Lupton, p.99] [Muller-Brockmann, p.64, 72]
- **One change or stacked changes.** Bringhurst says vary one attribute (size, or weight, or italic) and lighten weight as size grows; Williams says stack differences so contrast can't be missed; Lupton allows 1-3 cues per level. For headings and inline emphasis, change one or two (size plus weight, never bold plus italic plus caps). For the key metric vs its label, stack 2-3. [Bringhurst, p.60] [Williams, p.115, 124] [Lupton, p.132]
- **Font choice and weight.** Williams pairs a black headline with a light (300) body; Refactoring UI says a neutral sans is fine and nothing below 400; Bringhurst says one well-made family beats many. In the app: one family, 400-700. Use heavy-vs-light only on the logo, title slide, and poster. [Williams, p.137, 300-302] [Refactoring UI, p.28-31] [Bringhurst, p.197]
- **How minimal to go.** Tufte and Few push data-ink to the limit; Reynolds says not every nonessential element is noise, and Tufte himself calls his rules options. Keep data displays stark; title and problem slides may carry one relevant photo. [Tufte, p.88-95, 184] [Reynolds, p.129, 135] [Seed: C. Information presentation, §C3]
- **Line-chart baselines.** Knaflic allows a flagged non-zero baseline on lines; inbound Huff-style advice says never truncate. Bars always start at zero; a line may be cropped only with a labeled axis and the real % change stated. [Knaflic, p.83-86] [Seed: C. Information presentation, §C5]
- **Grids.** The seed kit, Muller-Brockmann, and Lupton use a 12-column grid (it divides into 2, 3, 4, 6); Refactoring UI says fixed widths beat percentage grids. Use a fixed 240-280px sidebar plus a 12-column content area, and a 3-4 column grid on slides. [Muller-Brockmann, p.50] [Refactoring UI, p.66-72] [Seed: D. Layout and grids, §D]
- **Text limits on slides.** Seed kit: about 7 words; Reynolds rejects fixed rules; Duarte: 50-75 words. At a table pitch, one phrase, 3 short items at most. [Seed: A. Hackathon visual kit, §A4] [Reynolds, p.140-142] [Duarte, p.28-29]

## Go deeper
- search_experts("lie factor size of effect shown in graphic", domain="12-visual-design")
- search_experts("small multiples identical axes comparison", domain="12-visual-design")
- search_experts("frequency framing icon array probability uncertainty band", domain="12-visual-design")
- search_experts("bullet graph instead of gauge for KPI vs target", domain="12-visual-design")
- search_experts("declutter gridlines direct labels data-ink erase", domain="12-visual-design")
- search_experts("tabular figures align numbers right table furniture", domain="12-visual-design")
- search_experts("chart type by relationship ranking deviation distribution", domain="12-visual-design")
- search_experts("exhibition poster standing visitor eye height reading distance", domain="12-visual-design")
