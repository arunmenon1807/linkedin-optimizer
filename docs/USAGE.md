# How to use it

Copy any of these requests and adjust the details. They work the same way in Claude Code,
Claude.ai, ChatGPT or Gemini once the skill or prompt is installed (see the
[README](../README.md#install)).

- [Quick start](#quick-start)
- [Everyday requests](#everyday-requests)
- [Situations](#situations)
- [The fill-in loop](#the-fill-in-loop)
- [Apply mode](#apply-mode-let-it-make-the-changes)
- [Platform notes](#platform-notes)
- [Tips for better results](#tips-for-better-results)

## Quick start

1. On LinkedIn, open your profile → **More → Save to PDF**.
2. Attach the PDF and say:

> Optimize my LinkedIn profile. I'm targeting Senior Data Engineer roles in Australia.

You get, in order: a one-line summary of what it understood, three headline options, three value
propositions, a new About section, every role rewritten, skills to remove and add, Featured ideas,
a keyword map, an elevator pitch, a gap list, and a **Fill these in** list of questions.

## Everyday requests

**Full review** (the default)
> Here's my LinkedIn PDF. Do a full review for Product Manager roles at SaaS companies.

**Just the headline**
> Just my headline. I'm a QA engineer moving into test automation. Current headline: "QA Analyst at Acme".

**Just the About section**
> Rewrite my About for UX Designer roles. Keep it under 200 words and less formal.

**One role**
> Rewrite this role for recruiter search:
> Software Developer, Acme Bank, 2021–2024. Worked on payment APIs in Java. Helped with the cloud migration.

**Keyword check against real job postings** (the most useful input you can give it)
> Here are three job posts I'd apply to: [paste]. Build a keyword map from them and show what my
> profile is missing.

**Audit only, no rewrites**
> Don't rewrite anything yet. Just audit my profile and list the problems, most important first.

**Skills cleanup**
> My Skills section is full (100). Which skills should I remove, and which should I add for
> DevOps Engineer roles?

**Elevator pitch**
> Give me a 30-second pitch for networking events and a spoken version for a video intro.

## Situations

**Career switch**
> I'm a high-school maths teacher moving into data analytics. I've done the Google Data
> Analytics certificate and two Kaggle projects. Rewrite my profile so recruiters see an analyst,
> not a teacher — honestly, without pretending I've had an analyst job.

**Relocating**
> I'm moving from India to Canada next year and want Senior Java roles in Toronto. What should
> change on my profile, and how do I say I'm relocating?

**Freelance or consulting**
> I'm going independent as a Salesforce consultant. Rewrite my headline and About to win clients,
> not to find a job. Call to action: book a call via my website.

**Graduate or first job**
> I'm a final-year computer science student. I have two internships and a capstone project.
> Make my profile work for graduate software engineer programs.

**Returning after a break**
> I took two years off to care for family and want to return to marketing roles. How do I handle
> the gap on my profile?

**Leadership roles**
> I'm an engineering manager with 12 years' experience targeting Head of Engineering roles.
> Focus on scale, team size and business impact.

**Promoting a side project**
> I built an open-source tool: [link]. Suggest how to feature it on my profile, and draft a
> LinkedIn post announcing it as a short story.

## The fill-in loop

The tool never invents numbers. Where a figure would help, it writes a placeholder like `[X%]`
and asks you about it. Answer in rough notes — no need to be polished:

> 1. Both wins were in the Senior Developer role
> 2. Team of 6, I led 2 juniors
> 3. Latency went from about 800 ms to 200 ms
> 4. No idea on revenue, leave it out

It then produces a clean final version: every placeholder filled with your answer or removed.
If an answer is vague ("huge improvement"), it asks for a rough figure or phrases the line without
a number.

## Apply mode (let it make the changes)

If your AI has a browser you're signed in to LinkedIn with (for example Claude Code with
Claude in Chrome), you can ask it to make the edits for you:

> Apply the headline, About and all experience rewrites to my LinkedIn. Delete the duplicate role.
> Don't change my location.

It confirms the scope first, edits one section at a time, keeps "Notify network" off, and reads
the live profile after each save to check. Deletions (roles, skills) and posts are always
confirmed by name before they happen. It never types passwords or changes account settings.

More Apply-mode requests:

> Remove the generic skills (Oral Communication, Presentations…) and add the missing technical
> skills to each role.

> Move my two best posts to the top of Featured and remove the weakest two.

> Post this draft with my app screenshot attached. Show me the final text first.

## Platform notes

**Claude Code** — after installing the plugin, just ask in plain English, or name it:

> Use the linkedin-optimizer skill on my profile PDF in ~/Downloads/Profile.pdf

The plugin also includes an **agent**, which runs separately and hands back a finished report:

> Run the linkedin-optimizer agent on ~/Downloads/Profile.pdf for Senior Backend roles in Berlin.

The agent can't stop to ask questions mid-run, so give it the target role and goal up front. Use
the skill (in your main conversation) when you want back-and-forth or Apply mode.

**Claude.ai** — upload the skill zip once; after that, attach your PDF in any chat and ask.

**ChatGPT** — create a Custom GPT and paste the prompt file into **Instructions**. Or paste it at
the top of a new chat, then attach your PDF.

**Gemini** — create a Gem and paste the prompt file into its instructions.

## Tips for better results

- **Add job postings.** One to three real ads give it the exact words employers search for.
- **Say the market.** "Remote", "London" or "relocating to Singapore" changes the advice.
- **Share real numbers when you have them.** Team size, users, money saved, time cut, accuracy.
- **Ask for one section at a time** if the full run is too much to review at once.
- **Iterate.** "Make the headline less formal" or "shorter bullets for the 2019 role" both work.
- **Check facts before you paste.** It writes from what you give it — you're the final reviewer.
