# Component 1.2: Partner Intelligence & 20-Minute Zoom Interview Strategy
## Partner Dossier: Andrew Miklas (General Partner, Y Combinator)

---

### Executive Profile: The High-Availability Operator & Distributed Systems Architect

**Andrew Miklas** is a General Partner at [Y Combinator](https://www.ycombinator.com/people/andrew-miklas), co-founder and founding Chief Technology Officer of [PagerDuty](https://www.pagerduty.com/) (YC S10, NYSE: [PD](https://www.nyse.com/quote/XNYS:PD)), and former Venture Partner at [S28 Capital](https://www.s28capital.com/). 

Miklas represents the archetype of the **"Five-Nines Pragmatist"** inside YC's partnership. Alongside co-founders [Alex Solomon](https://www.ycombinator.com/founders/alex-solomon) and Baskar Puvanathasan, Miklas took PagerDuty from a bootstrapped side-project hatched by three University of Waterloo software engineering alumni into the mission-critical digital operations platform powering incident management for over 70% of the Fortune 100. PagerDuty was incubated in YC Summer 2010 and became the second company in Y Combinator history to complete an initial public offering on the New York Stock Exchange (April 2019).

As founding CTO, Miklas architected PagerDuty’s legendary high-availability alerting pipeline under an unforgiving operational mandate: *when the rest of the internet is broken, PagerDuty must work*. He scaled PagerDuty's product and engineering teams from zero to 80+ engineers, built multi-carrier redundancy across voice, SMS, and push notification infrastructure, and pioneered early modern DevOps and Site Reliability Engineering (SRE) practices. After transitioning from day-to-day operations at PagerDuty, Miklas spent seven years as a Venture Partner at [S28 Capital](https://www.s28capital.com/)—a $170M+ early-stage enterprise software fund—investing in mission-critical developer tools, cloud infrastructure, and security platforms, including [Retool](https://retool.com/), [Clerk](https://clerk.com/), [CaptivateIQ](https://www.captivateiq.com/), [Teleport](https://goteleport.com/), and [CodeStream](https://dev.to/codestream/confessions-of-a-first-time-vc-1o3i).

Miklas joined Y Combinator as a Visiting Group Partner for the S24 batch and was promoted to **General Partner** in May 2025. In the partnership, Miklas operates at the intersection of deep technical infrastructure, resilient AI systems, and multi-generational consumer educational technology. His landmark Fall 2026 Request for Startups, [The Primer](https://www.ycombinator.com/rfs?batch=Fall%202026), envisions an AI tutor inspired by Neal Stephenson's sci-fi masterpiece *The Diamond Age*, demonstrating his dual appetite for bulletproof backend infrastructure and transformative societal applications.

---

### 1. Official YC Bio & Career Milestones

| Year / Period | Milestone / Role | Strategic Context & Operational Significance |
| :--- | :--- | :--- |
| **2002 – 2007** | **BSE, Software Engineering**, [University of Waterloo](https://uwaterloo.ca/) | Rigorous software engineering training with 6 co-op terms, including 4 terms at ATI Technologies (now AMD) and 2 terms at Amazon. |
| **2007 – 2008** | **MSc, Computer Science**, [University of Toronto](https://www.utoronto.ca/) | Advanced computer science graduate research focusing on distributed computing, systems architecture, and algorithms. |
| **2008 – 2009** | **Software Infrastructure Engineer**, [Amazon](https://www.amazon.com/) | Built distributed internal infrastructure and operational tools. Experienced firsthand Amazon's internal pager and on-call alerting workflows that sparked PagerDuty. |
| **2009 – 2016** | **Co-Founder & CTO**, [PagerDuty](https://www.pagerduty.com/) (YC S10) | Founded PagerDuty with Waterloo classmates Alex Solomon and Baskar Puvanathasan. Built original high-availability telephony/push architecture; scaled engineering & product to 80+ people. |
| **Summer 2010** | **Y Combinator Batch S10 Alumni** | Accepted into YC on their 4th application attempt. Bootstrapped from $0 to hypergrowth, turning developer on-call pain into enterprise SaaS standard. |
| **2016 – 2024** | **Venture Partner**, [S28 Capital](https://www.s28capital.com/) | Led and supported Seed/Series A investments in enterprise infrastructure, developer productivity, and data security ([Clerk](https://clerk.com/), [Teleport](https://goteleport.com/), [CaptivateIQ](https://www.captivateiq.com/), [CodeStream](https://dev.to/codestream/confessions-of-a-first-time-vc-1o3i)). Angel investor in [Retool](https://retool.com/). |
| **April 2019** | **PagerDuty IPO (NYSE: PD)** | PagerDuty went public on the NYSE at an initial valuation of $1.8B+, becoming only the 2nd YC startup to achieve a traditional public listing. |
| **April 2024** | **Visiting Group Partner**, [Y Combinator](https://www.ycombinator.com/blog/meet-ycs-newest-visiting-group-partners) | Joined YC full-time alongside Jon Xu and Ooshma Garg to mentor batch companies in B2B SaaS, dev tools, and enterprise architecture. |
| **May 2025** | **Promoted to General Partner**, [Y Combinator](https://www.ycombinator.com/blog/welcome-jon-and-andrew) | Elevated to permanent General Partner, leading group office hours, partner interviews, and admissions. |
| **Fall 2026** | **Author, YC Request for Startups: "The Primer"** | Published landmark RFS calling for founders to build a lifelong adaptive AI tutor for young children, inspired by Neal Stephenson's *The Diamond Age*. |

---

### 2. Deep Dive: Lectures, Podcasts, and Technical Philosophy

Miklas is an articulate, methodical systems thinker who dissects startup mechanics through the lens of engineering principles, operational resilience, and enduring customer habits. 

#### A. The Venture Podcast (August 2024): *Advice for Aspiring Founders & Operating Lessons*
In an extensive interview on [The Venture Podcast](https://podcasts.apple.com/gb/podcast/andrew-miklas-yc-visiting-group-partner-and-co/id1777140549?i=1000675126460) (and [YouTube](https://www.youtube.com/watch?v=l22jp_yrOiw)), Miklas broke down how technical founders transition from engineering to early-stage investing and what differentiates enduring startups from fragile experiments:

1. **The Fallacy of the Tarpit Idea vs. Earned Operational Pain:**
   > *"If you have no experience at all, it's very hard to generate ideas outside of student life. You end up with software for students exchanging notes or textbook marketplaces—the classic tarpit ideas because that's all you know. But I also don't think you need to spend a decade at Google. A couple of co-op terms or two years working in an industry where you see broken operational workflows gives you the exact insight you need."*
   - **Tactical Takeaway:** Miklas values founders who earned their insight by living through concrete operational failure. If you are solving a problem, he expects you to describe the exact human or organizational friction you observed in the trenches.

2. **The "Thin Wrapper" & AI Model Deficiency Trap:**
   > *"If a product is built merely to compensate for a temporary deficiency in an AI model, it likely will not have long-term viability as a business. A successful solution integrates AI as part of a broader, durable system, not just as an isolated API call."*
   - **Tactical Takeaway:** If OpenAI, Anthropic, or Google can release a checkpoint update that makes your product obsolete overnight, you do not have a company. Miklas tests whether your product embeds deep workflow hooks, proprietary data loops, or high-availability operational orchestration that models cannot replicate.

3. **Coding as Precision Thinking and Specification:**
   > *"Learning how to code is still vital if you want to go into tech—being able to accurately describe the product you want is a skill, and that skill is developed by writing code. A number of coders end up being excellent writers because they learn clarity of thought."*
   - **Tactical Takeaway:** In an interview with Miklas, hand-waving conceptual fluff is fatal. He expects founders to describe their product and architecture with the deterministic precision of a compiler.

4. **The "I Learned Something New" Investment Signal:**
   > *"When evaluating teams to back, a strong indicator of a good investment is leaving a meeting with a sense of having learned something new."*
   - **Tactical Takeaway:** If you tell Miklas common knowledge, you are losing. You must teach him an unexpected, counterintuitive fact about your market, customer behavior, or architectural bottleneck within the first 3 minutes.

#### B. Founder Firesides with Amjad Masad (April 2026): *The Future of Software Development & Generalist Operators*
In a wide-ranging discussion with [Amjad Masad](https://www.ycombinator.com/library/bl-replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the-future) (Co-founder & CEO of Replit), Miklas explored the changing role of software engineers in an era of AI code generation:

1. **From Code Generation to Business Problem Solvers:**
   - Miklas and Masad discussed how engineers inside hypergrowth startups are no longer rewarded simply for typing syntax, but for diagnosing operational bottlenecks across customer support, HR, and billing, and building autonomous internal tools that eliminate manual toil.
   - Miklas emphasized that software has transitioned from being an "artisan craft" to an operational utility. The startups that win are those that shorten the feedback loop between identifying customer pain and deploying high-availability software to solve it.

#### C. Confessions of a First-Time VC (June 2019): *Capturing Developer Knowledge & Software Churn*
In his interview with [Claudio Pinkus on DEV Community](https://dev.to/codestream/confessions-of-a-first-time-vc-1o3i), Miklas articulated his thesis on enterprise software knowledge management:
- **The "Brain Drain" of Software Development:** When engineers switch jobs every 18 months, companies keep the raw git repository, but they lose the mental model—the *why* behind architectural decisions.
- Miklas backs tools that institutionalize implicit tribal knowledge into explicit workflows. Whether in developer tools or enterprise workflows, products that turn ephemeral human behavior into durable organizational memory command the highest net revenue retention.

#### D. PagerDuty Architecture & AWS re:Invent Fireside with Werner Vogels: *Zero-Downtime Reliability*
At [AWS re:Invent](https://www.pagerduty.com/newsroom/pagerduty-cto-discuss-innovation-technology-amazons-aws-reinvent-conference/) alongside Amazon CTO Dr. Werner Vogels and GitHub CTO Chris Wanstrath, Miklas detailed how PagerDuty built an infrastructure platform where downtime equals customer disaster:
- **Mean Time to Detect (MTTD) vs. Mean Time to Resolve (MTTR):** Operations platforms must not merely alert; they must compress the entire lifecycle of an incident.
- **Fail-Safe Telephony & Carrier Diversity:** When Twilio or AWS experiences regional degradation, critical alerts cannot stall. PagerDuty engineered multi-provider fallbacks across SMS aggregators, voice trunks, and data queues.
- Miklas holds founders building B2B SaaS and infra to the same high-availability standard: *What happens to your customers when your underlying LLM provider goes down for 4 hours?*

---

### 3. Requests for Startups (RFS) & Active Investment Theses

#### Thesis 1: "The Primer" — The Lifelong Adaptive AI Tutor (Fall 2026 RFS)
Published in YC's [Fall 2026 Requests for Startups](https://www.ycombinator.com/rfs?batch=Fall%202026), Miklas articulated a deeply personal and ambitious thesis on AI-driven childhood education:
- **The Core Inspiration:** In Neal Stephenson’s 1995 cyberpunk novel *The Diamond Age: Or, A Young Lady's Illustrated Primer*, a young girl receives an interactive book that adapts to her cognitive growth, psychology, and life experiences—teaching her not merely how to read, but how to think, reason, and develop wisdom.
- **The Modern Inflection Point:**
  > *"For the first time in history, something like the Primer is starting to feel possible. The best education has always come from one-on-one tutoring. Aristotle taught Alexander. But that privilege has been reserved for the few. AI can bring it to every child. And great tutors do more than drill facts. Over years, they learn a child's mind, and with it how to teach what can't be drilled at all: thinking, reasoning, even wisdom. In Stephenson's story, the Primer is an AI tutor that never runs out of patience or time."*
- **The Immediate Wedge:**
  - Start with foundational literacy, writing, and early arithmetic for children aged 4 to 8.
  - A consumer software product that a parent purchases directly to help their child master core skills, while simultaneously functioning as a teacher's classroom assistant rather than an adversarial teacher replacement.
  - The product must "win twice": provide genuine pedagogical engagement for the child while demonstrating undeniable, measurable mastery metrics to the parent.
- **The Long-Term Moat:** A persistent, longitudinal learner profile that follows a student over years, dynamically modeling cognitive strengths, learning velocity, memory decay, and intrinsic motivation.

#### Thesis 2: High-Availability Mission-Critical Enterprise Infrastructure
Drawing directly from his PagerDuty founding journey, Miklas hunts for B2B platforms where failure is intolerable:
- **Zero-Failure Incident Management & SRE:** Automated root-cause remediation, noise suppression, and real-time incident resolution pipelines.
- **Security & Access Control:** Infrastructure that eliminates manual credential management (e.g., [Teleport](https://goteleport.com/)).
- **Authentication & User Management:** Foundational identity infrastructure where a 5-second outage cascades into millions of locked-out users (e.g., [Clerk](https://clerk.com/)).

#### Thesis 3: Developer Productivity & "Small Software" Deployments
- Software that empowers non-traditional engineers and operations generalists to build bespoke, mission-critical workflows without maintaining fragile custom backends (e.g., [Retool](https://retool.com/)).
- Tools that capture implicit architectural rationale and automate code migrations across enterprise repositories.

---

### 4. Portfolio Companies & Founder Archetypes

Miklas champions founders who combine deep technical rigor with commercial pragmatism—especially engineers who have lived inside broken operational workflows and refuse to accept standard industry inefficiencies.

```
                    ┌────────────────────────────────────────┐
                    │      ANDREW MIKLAS FOUNDER ARCHETYPE   │
                    └───────────────────┬────────────────────┘
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│   THE SYSTEMS    │           │   THE VERTICAL   │           │   THE MISSION    │
│    ARCHITECT     │           │    OPERATOR      │           │    VISIONARY     │
├──────────────────┤           ├──────────────────┤           ├──────────────────┤
│• Waterloo/U of T │           │• Ex-operator who │           │• Bold ambition   │
│  technical DNA   │           │  knows exact ROI │           │  (e.g., Primer,  │
│• High-availability│          │• Automates unsexy│           │  edtech, frontier│
│  mindset (99.99%)│           │  compliance/ops  │           │  infrastructure) │
│• Clerk, Teleport,│           │• Particularity,  │           │• Long-term data  │
│  Nodus Compute   │           │  Sherpa, Uno     │           │  retention moat  │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

#### Notable YC Companies Mentored & Advised (Primary Partner / Group Partner):
1. [Particularity](https://www.ycombinator.com/companies/particularity) (YC F26)
   - **Wedge:** Building the modern software and automated compliance stack for state and federal government regulators.
   - **Why Miklas Backed Them:** Regulatory compliance across multi-jurisdiction frameworks is fragmented, manual, and painful. Particularity replaces manual audit bottlenecks with automated regulatory intelligence.
2. [Nodus Compute](https://www.ycombinator.com/founders/1792661-viswa-kotra) (Viswa Kotra, Pranav Varshney)
   - **Wedge:** High-performance distributed computing and GPU resource orchestration for AI model workloads.
   - **Why Miklas Backed Them:** Directly aligns with Miklas's distributed systems background—optimizing hardware utilization and low-latency scheduling under heavy concurrent load.
3. [Sherpa](https://www.ycombinator.com/founders/norbu-sonam) (Norbu Sonam, Ethan Kinnan)
   - **Wedge:** Operational navigation and agentic workflows for enterprise logistics and field services.
4. [Uno Wallet](https://www.ycombinator.com/founders/1631278-mordi-shadpour) (Mordi Shadpour)
   - **Wedge:** Consumer financial intelligence automating transaction routing across cards and payment networks.
5. [Boxes.dev](https://www.ycombinator.com/founders/295276-drew-regitsky) (Drew Regitsky)
   - **Wedge:** Cloud developer environments and sandboxed infrastructure for software teams.
6. [Flai](https://www.ycombinator.com/founders/1587100-juan-alzugaray) (Juan Alzugaray)
   - **Wedge:** AI data pipelines and automated customer insights founded by former Netflix data scientists.
7. [Spine](https://www.ycombinator.com/founders/4028056-ece-cokar) (Ece Cokar)
   - **Wedge:** Legal tech and structured contract workflow automation.
8. [Mirrors](https://www.ycombinator.com/founders/3174410-aryan-singhal) (Aryan Singhal)
   - **Wedge:** Cutting-edge multimodal AI research applied to synthetic evaluation benchmarks.

#### Landmark Angel & S28 Capital Investments:
- [Clerk](https://clerk.com/): Drop-in authentication and user management for React and Next.js developers.
- [Teleport](https://goteleport.com/): Zero-trust identity-native infrastructure access for servers, databases, and Kubernetes.
- [Retool](https://retool.com/): The fast way to build internal software tools and dashboards.
- [CaptivateIQ](https://www.captivateiq.com/): Agile sales commission management software.
- [CodeStream](https://dev.to/codestream/confessions-of-a-first-time-vc-1o3i): In-IDE developer collaboration and contextual knowledge capture (acquired by New Relic).

---

### 5. Partner Psychology & 20-Minute Zoom Interview Strategy

During the 20-minute YC Zoom interview, Andrew Miklas approaches founders like a peer CTO conducting a high-stakes architectural and commercial post-mortem. He is calm, intensely analytical, and deeply allergic to buzzwords.

```
┌───────────────────────────────────────────────────────────────────────────┐
│                    ANDREW MIKLAS: INTERVIEW SCORECARD                     │
├─────────────────────────────────────┬─────────────────────────────────────┤
│        INSTANT DISQUALIFIERS        │          GREEN FLAG SIGNALS         │
├─────────────────────────────────────┼─────────────────────────────────────┤
│ ❌ Tarpit student ideas without      │ 🟢 Earned operational insight from  │
│    industry experience or pain      │    living through real enterprise   │
│ ❌ "Wrapper" products vulnerable    │    breakdowns                       │
│    to foundation model updates      │ 🟢 Deep architectural understanding │
│ ❌ Hand-waving answers on systems    │    of edge cases, latency, and SLA  │
│    reliability and fault tolerance  │ 🟢 Clear understanding of developer │
│ ❌ Arrogance without metrics;       │    adoption vs. enterprise sales    │
│    inability to explain churn       │ 🟢 Teaches the partner something    │
│ ❌ Vague marketing claims without    │    surprising and counterintuitive  │
│    deterministic user conversion    │    about the customer's workflow    │
└─────────────────────────────────────┴─────────────────────────────────────┘
```

#### Immediate Disqualifiers (Red Flags):
1. **The LLM Capability Gap Trap:** Claiming you have a company when all you have done is prompt-engineer an API call around a known GPT/Claude limitation. Miklas will ask: *"What prevents Anthropic or OpenAI from releasing an update next Tuesday that renders your core value proposition obsolete?"* If you do not have proprietary data, deep system integrations, or workflow locking, you are done.
2. **Abstract Conceptualizing Without Systems Knowledge:** If you claim your platform provides 99.99% reliability or enterprise-grade compliance, but you stumble when asked about fallback queues, carrier diversity, or data residency, Miklas will immediately lose confidence.
3. **The Unearned Tarpit Idea:** Proposing generic student solutions (study planners, shared notes, campus event finders) without proprietary distribution or profound technological advantage.
4. **Defensiveness Under Technical Interrogation:** When Miklas pokes at a weak link in your tech stack or unit economics, responding with defensive posturing rather than dispassionate technical reality will eliminate your application.

#### Green Flag Signals:
1. **Deterministic Operational Clarity:** Answering questions in complete, concise, quantitative sentences: *"We convert 18% of self-serve developers into paid accounts within 14 days, and our net revenue retention across the first cohort is 134%."*
2. **Teaching Him Something Surprising:** Revealing an obscure, high-friction operational constraint inside an enterprise or regulated industry that only someone who spent 100 hours with end users would know.
3. **Resilient System Design:** Demonstrating that you have thought through catastrophic failure modes—how your software degrades gracefully when third-party APIs fail.
4. **Relentless Tenacity:** PagerDuty took four tries to get into YC. Miklas deeply respects technical founders who iterate relentlessly, take user feedback, and refuse to quit.

---

### 6. Question Bank & 15-Second Answer Templates

When facing Andrew Miklas, your answers must be crisp, devoid of filler, and structured around **Fact $ightarrow$ Metric $ightarrow$ Mechanism**.

#### Q1: "What are you building in plain English?"
- **The Trap:** Using buzzwords like "autonomous agentic AI orchestration framework for enterprise workflows."
- **15-Second Answer Template:**
  > *"We build automated incident dispatch for Kubernetes clusters. When a microservice crashes, our agent correlates the logs across Datadog, identifies the faulty pull request, and rolls back the deployment in under 45 seconds—before an on-call engineer even wakes up."*

#### Q2: "What prevents OpenAI or Anthropic from wiping out your product in their next model update?"
- **The Trap:** Arguing that your prompts are better or that you have a "nicer UI."
- **15-Second Answer Template:**
  > *"Models provide the intelligence, but we own the execution plane. We integrate with 42 proprietary SCADA and ERP databases behind enterprise VPCs that foundation models cannot access. The switching cost isn't the prompt; it's the security clearance, audit logs, and SOC2 compliance engine we have embedded into their internal infrastructure."*

#### Q3: "How did you get your first 10 paying customers?"
- **The Trap:** "We ran LinkedIn ads and cold emails."
- **15-Second Answer Template:**
  > *"I worked as an SRE at Snowflake and manually resolved this problem for 18 months. When we launched, I called 15 former colleagues running DevOps teams. Ten of them installed our CLI tool within 48 hours, and 8 converted to annual contracts at $12,000 ACV because it saved each engineer 6 hours of midnight on-call duty per week."*

#### Q4: "If you're building an adaptive AI tutor (The Primer), how do you prove learning outcomes rather than just screen time?"
- **The Trap:** "Kids love using it and parents leave great reviews."
- **15-Second Answer Template:**
  > *"We measure phonetic decoding speed and reading comprehension delta every 7 days through subtle interactive micro-assessments disguised as gameplay. In our 200-family pilot, 1st graders using our app 15 minutes a day advanced their Lexile reading score 2.4x faster than the district average over 8 weeks, giving parents verified progress reports they share with teachers."*

#### Q5: "What is the single biggest bottleneck to scaling your business right now?"
- **The Trap:** "We just need more capital to hire sales reps."
- **15-Second Answer Template:**
  > *"Our bottleneck is enterprise security review. Developers install our open-source agent in 5 minutes, but closing the $50k enterprise contract takes 60 days of Infosec sign-off. We are currently implementing automated SOC2 and HIPAA isolation containers to compress that review window from 8 weeks to 10 days."*

---

### 7. Strategic Action Checklist Before You Face Andrew Miklas

Before stepping into your 20-minute Zoom interview with Andrew Miklas, execute this operational checklist:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    ANDREW MIKLAS INTERVIEW PREPARATION                     │
├────────────────────────────────────────────────────────────────────────────┤
│ [ ] 1. Identify Your Non-Model Moat: Define exactly what data,             │
│        infrastructure hooks, or workflow locks survive if frontier models  │
│        become 10x smarter and 10x cheaper tomorrow.                        │
│ [ ] 2. Map Your High-Availability Edge Cases: Know your system's failure   │
│        modes. What happens when your database locks, your LLM provider has │
│        an outage, or latency spikes 5x?                                    │
│ [ ] 3. Prepare One Counterintuitive Insight: Have one surprising, verified │
│        operational fact about your customer that Miklas does not know.     │
│ [ ] 4. Quantify Land-and-Expand Dynamics: If targeting developers, have   │
│        your bottoms-up adoption metrics (GitHub stars, CLI downloads) and  │
│        your conversion rate to top-down enterprise contracts memorized.    │
│ [ ] 5. Strip Every Corporate Buzzword: Eliminate terms like "holistic",    │
│        "paradigm", "disruptive", and "seamless". Replace them with active  │
│        verbs, concrete tools, and exact numbers.                           │
│ [ ] 6. Rehearse the 15-Second Plain-English Hook: Ensure your opening      │
│        sentence can be understood by an engineer who has reviewed 50       │
│        pitches today.                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### Verified Source Grounding & Citations

- **Official YC Profile:** [Andrew Miklas - Y Combinator Partner Directory](https://www.ycombinator.com/people/andrew-miklas)
- **General Partner Announcement:** [Welcoming Jon Xu and Andrew Miklas as YC's Newest General Partners](https://www.ycombinator.com/blog/welcome-jon-and-andrew) (May 21, 2025)
- **Visiting Partner Announcement:** [Meet YC's Newest Visiting Group Partners](https://www.ycombinator.com/blog/meet-ycs-newest-visiting-group-partners) (April 17, 2024)
- **PagerDuty YC Directory & History:** [PagerDuty - Y Combinator Profile](https://www.ycombinator.com/companies/pagerduty) | [Andrew Miklas Founder Profile](https://www.ycombinator.com/founders/andrew-miklas)
- **PagerDuty 10-Year Retrospective:** [A Decade of Duty: A Brief Look at PagerDuty's History](https://www.pagerduty.com/blog/company/decade-of-duty/) (Alex Solomon, Feb 2019)
- **Bessemer Venture Partners Investment Memo:** [PagerDuty Investment Memo](https://www.bvp.com/memos/pagerduty) (Series B Analysis & Cohort Expansion)
- **YC Fall 2026 Requests for Startups:** [Requests for Startups - Fall 2026 Edition](https://www.ycombinator.com/rfs?batch=Fall%202026) (Features *The Primer* by Andrew Miklas)
- **Inc. Magazine Analysis of Fall 2026 RFS:** [Y Combinator Just Revealed the Startup Ideas It Wants Most for Fall 2026](https://www.inc.com/lucia-auerbach/y-combinator-requests-for-startups-fall-2026/91379840)
- **The Venture Podcast & YouTube Interview:** [Andrew Miklas | YC Visiting Group Partner & Co-Founder of PagerDuty](https://www.youtube.com/watch?v=l22jp_yrOiw) | [Apple Podcasts](https://podcasts.apple.com/gb/podcast/andrew-miklas-yc-visiting-group-partner-and-co/id1777140549?i=1000675126460)
- **Replit Founder Firesides:** [Replit's CEO On The Only Two Jobs Left In The Company Of The Future](https://www.ycombinator.com/library/bl-replit-s-ceo-on-the-only-two-jobs-left-in-the-company-of-the-future) (Hosted by Andrew Miklas, April 2026)
- **DEV Community Interview:** [Confessions of a First-Time VC: Andrew Miklas](https://dev.to/codestream/confessions-of-a-first-time-vc-1o3i) (June 2019)
- **S28 Capital Firm Profile & Team:** [S28 Capital Team Directory](https://www.s28capital.com/team/andrew-miklas/) | [About S28 Capital](https://www.s28capital.com/about/)
- **AWS re:Invent Fireside Chat:** [PagerDuty CTO to Discuss Innovation at AWS re:Invent with Werner Vogels](https://www.pagerduty.com/newsroom/pagerduty-cto-discuss-innovation-technology-amazons-aws-reinvent-conference/)
- **Mentored YC Portfolio Startups:** [Particularity](https://www.ycombinator.com/companies/particularity), [Viswa Kotra / Nodus Compute](https://www.ycombinator.com/founders/1792661-viswa-kotra), [Norbu Sonam / Sherpa](https://www.ycombinator.com/founders/norbu-sonam), [Boxes.dev](https://www.ycombinator.com/founders/295276-drew-regitsky), [Uno Wallet](https://www.ycombinator.com/founders/1631278-mordi-shadpour), [Flai](https://www.ycombinator.com/founders/1587100-juan-alzugaray), [Spine](https://www.ycombinator.com/founders/4028056-ece-cokar), [Mirrors](https://www.ycombinator.com/founders/3174410-aryan-singhal).
