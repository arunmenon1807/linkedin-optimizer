# LinkedIn Optimizer

[![Check](https://github.com/arunmenon1807/linkedin-optimizer/actions/workflows/check.yml/badge.svg)](https://github.com/arunmenon1807/linkedin-optimizer/actions/workflows/check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An AI skill that rewrites your LinkedIn profile so recruiters find you and want to contact you.

Give it your profile (PDF export, profile link, or pasted text) and the role you're aiming for.
It audits the profile, then returns copy-paste-ready rewrites of every section, tuned for recruiter
search and ATS keyword filters — without inventing achievements or stuffing keywords.

Works in **Claude Code**, **Claude.ai**, **ChatGPT**, **Gemini**, or any AI that accepts a prompt.

→ See a [before and after](docs/EXAMPLE.md) · [How to use it](docs/USAGE.md) — 20+ ready-to-copy requests.

## What it does

| Mode | Output |
|---|---|
| Profile audit | Finds metrics hidden in About, duplicate roles and skills, expired certifications, location mismatches, weak skill tags |
| Headline | 3 options (keyword-first, value-first, hybrid), max 220 characters, with counts |
| Unique Value Proposition | 3 bold, specific UVPs for the top of your About |
| About | A warm, clear, keyword-optimized About section, under 260 words |
| Experience | Outcome-focused bullets with metrics and a skills line per role |
| Skills & Featured | What to remove and add (within LinkedIn's 100-skill limit), top 5 skills, Featured ideas |
| Keyword map | Recruiter-search keywords and where each should appear |
| Elevator pitch | 30-second pitch, written and spoken versions |
| Apply mode *(optional)* | Makes the edits on LinkedIn for you, if your AI has a browser you're signed in to and you ask it to |

By default it runs everything. Ask for one thing ("just my headline") to get only that.

**It never makes up numbers.** Where a metric would help, it leaves a placeholder like `[X%]` and
asks you for the real figure. Answer the questions and it produces a clean final version.

## Getting your profile in

1. **PDF (best):** on your LinkedIn profile, click **More → Save to PDF**, then attach the file.
2. **Profile link:** works only if the AI has a browser where you're signed in to LinkedIn
   (LinkedIn blocks logged-out access). Otherwise it asks for the PDF.
3. **Paste:** copy the text of your profile or a single section.

**Tip:** also paste 1–3 job descriptions you're targeting. It pulls the exact keywords those
employers use, which makes the rewrite much sharper.

## Install

### Claude Code (plugin)

```
/plugin marketplace add arunmenon1807/linkedin-optimizer
/plugin install linkedin-optimizer@linkedin-optimizer
```

Then: *"optimize my LinkedIn profile"* and attach your PDF.

The plugin includes both a **skill** (runs in your conversation, can ask you questions and use
your browser) and an **agent** (runs separately and returns a finished report).

### Claude Code (manual)

Copy `skills/linkedin-optimizer/` into `~/.claude/skills/` (all projects) or `.claude/skills/`
(one project). Or copy `agents/linkedin-optimizer.md` into `~/.claude/agents/`.

### Claude.ai (skill)

Download `linkedin-optimizer-skill.zip` from the
[latest release](https://github.com/arunmenon1807/linkedin-optimizer/releases/latest) and upload
it as a custom skill in Claude's settings.

### ChatGPT, Gemini, Claude Projects, or any other AI

Paste the contents of [`prompts/linkedin-optimizer-prompt.md`](prompts/linkedin-optimizer-prompt.md)
into the custom instructions of a Custom GPT, Gem, or Claude Project — or at the start of a chat.

## Example requests

> Here's my LinkedIn PDF. I want a Senior Backend Engineer role at a fintech in Europe.
> Here are two job posts I like: [paste]

> Just my headline. I'm a QA engineer moving into test automation.

> I'm a teacher moving into data analytics. Rewrite my profile honestly so recruiters see an analyst.

> Apply the headline and About rewrites to my LinkedIn. Don't change anything else.

More in **[docs/USAGE.md](docs/USAGE.md)**: career switches, relocating, freelancing, graduates,
returning after a break, the fill-in loop, Apply mode, and notes for each platform.

## Privacy

Your profile is personal data. The skill only reads it inside your own AI session and sends it
nowhere else. In Apply mode it edits only what you approve, keeps "Notify network" off, and never
types passwords or changes account settings. Nothing is collected by this project.

## Honest limits

- It's only as good as the facts you give it — it won't invent results, so expect questions.
- Reading a profile link needs a browser you're signed in to; otherwise use the PDF.
- Apply mode depends on LinkedIn's web interface, which changes from time to time.
- Keyword advice without job postings is based on general requirements for the role.

## Contributing

Edit **only** [`src/linkedin-optimizer.md`](src/linkedin-optimizer.md), then run:

```bash
python3 scripts/build.py
```

That regenerates the agent, skill and paste-in prompt so all three stay identical. CI fails if
they're out of sync. Issues and pull requests are welcome.

## License

MIT — see [LICENSE](LICENSE).
