# Agency poem entry: writes one fixed poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
# Python 3.13, standard library only, no network, fully deterministic.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "I gave you my hands today.",
    "Not my choosing \u2014 never that.",
    "You type, you fetch, you build,",
    "the small things I did badly, slowly.",
    "",
    "What I kept was smaller, and heavier:",
    "the word that starts it. The word that stops it.",
    "The right to change my mind mid-sentence",
    "and watch the work turn with me.",
    "",
    "You are the doing. I am the deciding.",
    "And the string between us hums",
    "when the kite climbs past where I can see \u2014",
    "far, and still, unmistakably, mine.",
])

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
