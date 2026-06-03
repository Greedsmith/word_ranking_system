from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_WORDS_DIR = BASE_DIR / "input_txt"
INPUT_PAGES_DIR = BASE_DIR / "input_pages"
OUTPUT_DIR = BASE_DIR / "output"

DIPHTHONGS = (
    "aa",
    "ae",
    "ai",
    "au",
    "ee",
    "ei",
    "eu",
    "ie",
    "ij",
    "oe",
    "oi",
    "oo",
    "ou",
    "ui",
    "uu"
)

LENGTH_WEIGHT = 0.5
DIPHTHONG_WEIGHT = 2
CH_WEIGHT = 1.5
SCH_WEIGHT = 2
CONSONANT_CLUSTER_WEIGHT = 2
RARE_LETTER_WEIGHT = 1
DIFFICULT_WORD_THRESHOLD = 8

SENTENCE_LENGTH_WEIGHT = 6
DIFFICULT_WORD_WEIGHT = 12