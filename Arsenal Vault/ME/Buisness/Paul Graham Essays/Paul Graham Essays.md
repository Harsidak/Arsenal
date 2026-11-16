## 1. How to Get Startup Ideas

1. **What problem did you hit?** Building my own ARC-AGI-3 agent, it kept acting on things it had never verified, because nothing it learned stayed true and checkable. _[fill: the exact moment and date]_
2. **Noticed or thought up?** Noticed. I saw it in my own agent, then measured it: in my first pilot, answering from a summary gave 39% confident wrong answers about details the full history had right.
3. [BLANK]
4. [BLANK]
5. **Who comes after the first niche?** First, agent teams where a wrong fact costs money. Then any team running long-lived agents per customer, because every one of them builds up facts that go stale.
6. **Why are Mem0 and Zep demand, not a reason to stop?** Mem0 handled 186M memory API calls in Q3 2025, so teams already pay for memory. Its own users report it serving superseded facts (issues #4956, #5867), and that failure is exactly what I fix.
7. **What do you see that others don't?** Agents will run for months for the same customer, so the bottleneck moves from the model to what the agent remembers and whether it's still true.

## 2. Do Things That Don't Scale

1. [BLANK]
2. **What will you do by hand first?** For each early user, I'll resolve identities and versions myself and check every "not recorded" answer by hand. Then I'll automate the resolver once I've seen enough real cases.
3. [BLANK]
4. **How will first users feel?** Their agent stops citing stale facts on their own data, and they deal with me directly, not a ticket queue.
5. **Narrow group?** Engineers at agent startups already on Mem0 or similar who've hit superseded facts, starting with the people who reported it publicly.
6. **Launch or partnership?** Neither. I recruit users one at a time; framework integrations come once users ask for them.

## 3. Startup = Growth

1–4. [BLANK]  
5. **Shortcut you'll refuse?** Claiming traction I don't have. A number I can't defend costs more than a small true one.  
6. **What does $500K buy?** Compute and time: a year of full-time work to ship the SDK, test it on real customer data, and get the first paying teams. _[fill: budget split]_

## 4. Schlep Blindness

1. **The tedious part everyone avoids?** Deciding which "Acme" is which, which fact replaced which, and removing memories that turn out to be wrong. It's entity resolution and versioning on messy real data.
2. **Why haven't Mem0 or Zep done it?** My read: similarity search is general and quick to ship, while exact identity needs per-domain resolution and a write rule. Mem0's v3 went add-only, which skips conflict resolution entirely.
3. **The schlep that defines Sarbloh?** Proving absence: answering "not recorded" only when it's true, which means owning identity end to end.
4. **What don't you know yet?** Whether identity resolution holds up on real, messy data. My results are synthetic, and keys learned end to end failed in my tests.
5. **What do agent builders wish someone else would solve?** Knowing which of their agent's memories are still true.

## 5. Frighteningly Ambitious Startup Ideas

1. **The terrifying version?** AI that gets better every day it's used, from its own experience, without retraining. That's a hypothesis — say so.
2. **The small starting point?** A memory layer that tells an agent "not recorded" instead of guessing.
3. **Big vision without sounding naive?** Lead with the small measured thing, and mention the big vision only as where it leads, labelled as a hypothesis.
4. **If your picture of the future is wrong?** Agents still need memory that doesn't serve stale facts. That product stands on its own even if continual learning never works.
5. **Which side of impossible is continual learning?** The wrong side, today. Writing facts into weights failed in my tests (M04); keeping experience in structure works on synthetic data, so memory ships first.

## 6. Founder Mode + How to Do Great Work

1. **Staying in the details once you hire?** I keep writing the experiment designs and kill criteria myself, and I review every result before it ships.
2. **When do you override an investor?** When the data says I'm right. My default is that I'm wrong — I've killed seven of my own hypotheses.
3. **Evidence you can't stop?** Coding since 14, and _[14]_ pre-registered experiments in about four weeks, part-time, alongside a full-time degree and an ICLR submission.
4. **The gap at the frontier?** Memory systems get tested on whether they recall facts, almost never on whether they answer confidently about facts that were never stored. The newest state-of-the-art paper left those questions out of its evaluation entirely. _Verify the LoCoMo counts before you cite this._
5. **Wrong and changed course?** I spent months on AI glasses, stress-tested the idea in September, found nothing a funded team couldn't copy, and stopped. In research I write kill criteria before each run; seven ideas died, including writing facts into weights.
6. _[fill: your real daily routine]_
7. **Who do you want to become like?** Nobody full-time yet, and that's the gap. My first hire is a mathematician stronger than me.
