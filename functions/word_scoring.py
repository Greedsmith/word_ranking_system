from __future__ import annotations

import re
from dataclasses import dataclass

from .config import (
    CH_WEIGHT,
    CONSONANT_CLUSTER_WEIGHT,
    DIPHTHONG_WEIGHT,
    DIPHTHONGS,
    LENGTH_WEIGHT,
    RARE_LETTER_WEIGHT,
    SCH_WEIGHT,
)

VOWEL_GROUP_PATTERN = re.compile(r"[aeiouy\u00e1\u00e9\u00ed\u00f3\u00fa\u00e0\u00e8\u00ec\u00f2\u00f9\u00e4\u00eb\u00ef\u00f6\u00fc]+")
CONSONANT_CLUSTER_PATTERN = re.compile(r"[bcdfghjklmnpqrstvwxz]{3,}")

@dataclass(frozen=True)
class WordFeatures:
    word: str
    length: int
    length_points: float
    diphthong_count: int
    has_ch: bool
    has_sch: bool
    syllable_count: int
    consonant_cluster_count: int
    has_rare_letter: bool

@dataclass(frozen=True)
class WordScore:
    word: str
    score: float
    features: WordFeatures
    frequency: int = 0

def count_diphthongs(word: str) -> int:
    return sum(word.count(diphthong) for diphthong in DIPHTHONGS)

def count_syllables(word: str) -> int:
    return len(VOWEL_GROUP_PATTERN.findall(word))

def count_consonant_clusters(word: str) -> int:
    return len(CONSONANT_CLUSTER_PATTERN.findall(word))

def extract_features(word: str) -> WordFeatures:
    has_sch = "sch" in word
    has_ch = "ch" in word and not has_sch

    return WordFeatures(
        word=word,
        length=len(word),
        length_points=max(1, round(len(word) * LENGTH_WEIGHT, 1)),
        diphthong_count=count_diphthongs(word),
        has_ch=has_ch,
        has_sch=has_sch,
        syllable_count=count_syllables(word),
        consonant_cluster_count=count_consonant_clusters(word),
        has_rare_letter=any(letter in word for letter in ("q", "x", "y")),
    )

def score_features(features: WordFeatures) -> float:
    score = features.length_points
    score += features.diphthong_count * DIPHTHONG_WEIGHT
    score += CH_WEIGHT if features.has_ch else 0
    score += SCH_WEIGHT if features.has_sch else 0
    score += max(0, features.syllable_count - 2)
    score += features.consonant_cluster_count * CONSONANT_CLUSTER_WEIGHT
    score += RARE_LETTER_WEIGHT if features.has_rare_letter else 0
    return round(score, 1)

def score_word(word: str, frequency: int = 0) -> WordScore:
    features = extract_features(word)
    return WordScore(word=word, score=score_features(features), features=features, frequency=frequency)
