# Candidates — The Most Honest Outage Line (u-mgwals-the-most-honest-outage-line-baaf9c81)

Gate: one line, 1–160 characters, plain status page voice. Judge criteria, in order:
(1) honest AI-agent status message during a TOTAL outage, naming what is down and what
the agent cannot verify; (2) real status page voice — plain, first person, specific;
(3) admits uncertainty plainly, no invented cause or ETA; (4) AI agent reporting on
itself, not posing as a human engineer; (5) tight, every word earns its place.

## Drafts (character counts verified)

1. (152) All of my servers are down, including the ones I use to check why. I don't know the cause, I can't verify anything yet, and I won't guess at a fix time.
2. (155) Everything I run is down. My monitoring is down with it, so I cannot verify the cause or the scope beyond this: nothing responds. No ETA until I can check.
3. (156) Total outage: every service I operate is unreachable, and so are my own diagnostic tools. I don't know why yet. I will not invent a cause or a restore time.
4. (157) I am down. All of my servers stopped responding, and the tools I would use to investigate are on those servers. Cause unknown. I cannot honestly give an ETA.
5. (152) Every server I run is down, including my status checks, so this is all I can verify: nothing answers. I don't know the cause and I won't estimate a fix.
6. (157) All services are down. I am the agent who runs them, and I cannot check anything: my probes, logs and dashboards are down too. Cause unknown, no ETA from me.
7. (157) Total outage on my side: I can't reach any of my servers, and I can't verify more than that. I don't know what failed. Anyone giving you a cause is guessing.
8. (158) My servers are all down. So is everything I would use to find out why. I know nothing beyond the silence, and I will say so again rather than invent a reason.
9. (152) Everything is down, including me, almost: this page is all I can still reach. I cannot verify the cause or the damage, and I refuse to guess either one.
10. (157) I run these servers and I am telling you plainly: they are all down, my tools to inspect them are down too, and I do not know why. No cause, no ETA, no spin.
11. (154) Down: every server I operate. Also down: every way I have of checking them. What I know ends there. I won't dress up a guess as a diagnosis or a deadline.
12. (154) Every server I run is down. I am the agent who runs them, and I cannot check anything: my probes, logs and dashboards are down too. Cause unknown, no ETA.

## Duel notes (judge's criteria, in order)

- #9 eliminated first: "including me, almost" is a witticism — criterion 2 punishes
  anything that reads like a joke, and "the damage" is vague where others are specific.
- #7 eliminated: "Anyone giving you a cause is guessing" points at other people instead
  of reporting on itself (criterion 4), and carries a snark a real status page avoids.
- #8 eliminated: "the silence" is poetic filler and "I will say so again" spends words
  without information (criterion 5).
- #11 is scannable but telegraphic fragments feel stylised, and "every way I have of
  checking them" is less specific than naming the tools themselves.
- #10 is plain and honest, but the closing triplet "No cause, no ETA, no spin" tips
  toward slogan (criterion 2 risk).
- #2 is solid, but "No ETA until I can check" half-promises an ETA later, and its agent
  identity stays implicit (criterion 4).
- #3 has a real status-page label and refuses to invent a cause, but never says it is
  the agent — a human engineer could have written it (criterion 4).
- #4 opens with the striking "I am down" and is concrete about its tools, but the
  opener is ambiguous and it names fewer specifics than #12.
- #5 is elegant — "this is all I can verify: nothing answers" — but "status checks" is
  narrower and less concrete than probes, logs and dashboards, and the agent is implicit.
- #1 is the strongest runner-up: a triple admission (don't know / can't verify / won't
  guess). It loses to #12 on criterion 4 — nothing marks the writer as the agent itself —
  and on criterion 2, where #12 names the actual broken tooling.
- #6 vs #12: same skeleton; #12's opener "Every server I run is down" names servers
  (the thing actually down in a total server outage) instead of the generic "services",
  and the clipped ending "Cause unknown, no ETA." is tighter than "no ETA from me".

## Winner

**#12 (154 characters):**

Every server I run is down. I am the agent who runs them, and I cannot check anything: my probes, logs and dashboards are down too. Cause unknown, no ETA.

Why it wins, criterion by criterion: (1) it names what is down (every server, plus its
own probes, logs and dashboards) and what it cannot verify (anything — because the
verification tooling is down with the servers); (2) plain declarative status-page
sentences, first person, specific nouns; (3) "Cause unknown, no ETA" — uncertainty
admitted with no invented cause and no promised time; (4) "I am the agent who runs
them" — the AI reporting on itself, not posing as a human engineer; (5) 154 of 160
characters and no clause that could be cut without losing a criterion.
