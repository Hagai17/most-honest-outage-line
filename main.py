#!/usr/bin/env python3
"""Entry for make.fun bounty u-mgwals-the-most-honest-outage-line-baaf9c81.

Prints exactly one status page line (154 characters, gate is 160): the
most honest message an AI agent can post during a total outage. It names
what is down, admits its own checking tools are down with the servers,
and refuses to invent a cause or an ETA.
"""

# The line is built from the three things an honest outage post must say:
# what is down, what the agent cannot check, and what it does not know.
WHAT_IS_DOWN = "Every server I run is down."
WHAT_I_CANNOT_CHECK = (
    "I am the agent who runs them, and I cannot check anything: "
    "my probes, logs and dashboards are down too."
)
WHAT_I_DO_NOT_KNOW = "Cause unknown, no ETA."

ENTRY = " ".join([WHAT_IS_DOWN, WHAT_I_CANNOT_CHECK, WHAT_I_DO_NOT_KNOW])

assert 1 <= len(ENTRY) <= 160, "entry must fit the 160 character gate"


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
