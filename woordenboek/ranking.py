from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .config import DIFFICULT_WORD_THRESHOLD
from .text_utils import PageText, TextDocument, count_sentences, extract_words
from .word_scoring import WordScore, score_word


@dataclass(frozen=True)
class TextDifficulty:
    name: str
    level: str
    level_score: float
    word_count: int
    unique_word_count: int
    average_word_score: float
    average_word_length: float
    average_sentence_length: float
    difficult_word_percentage: float


@dataclass(frozen=True)
class PageDifficulty:
    source: str
    page_number: int
    score: float
    level: str
    word_count: int
    average_word_score: float
    difficult_word_percentage: float
    top_difficult_words: str


def build_word_ranking(counter: Counter[str]) -> list[WordScore]:
    ranking = [score_word(word, frequency) for word, frequency in counter.items()]
    return sorted(
        ranking,
        key=lambda item: (
            -item.score,
            -item.features.length,
            -item.features.diphthong_count,
            item.word,
        ),
    )


def calculate_level_score(
    average_word_score: float,
    average_sentence_length: float,
    difficult_word_percentage: float,
) -> float:
    score = average_word_score
    score += average_sentence_length / 6
    score += difficult_word_percentage / 12
    return round(score, 1)


def level_from_score(score: float) -> str:
    if score < 4.5:
        return "A1"
    if score < 5.8:
        return "A2"
    if score < 7.0:
        return "B1"
    if score < 8.4:
        return "B2"
    if score < 10.0:
        return "C1"
    return "C2"


def analyze_text(name: str, text: str) -> TextDifficulty:
    words = extract_words(text)
    word_scores = [score_word(word) for word in words]
    word_count = len(words)

    if word_count == 0:
        return TextDifficulty(name, "A1", 0, 0, 0, 0, 0, 0, 0)

    average_word_score = sum(item.score for item in word_scores) / word_count
    average_word_length = sum(len(word) for word in words) / word_count
    difficult_words = [item for item in word_scores if item.score >= DIFFICULT_WORD_THRESHOLD]
    difficult_word_percentage = len(difficult_words) / word_count * 100
    average_sentence_length = word_count / count_sentences(text)
    level_score = calculate_level_score(
        average_word_score,
        average_sentence_length,
        difficult_word_percentage,
    )

    return TextDifficulty(
        name=name,
        level=level_from_score(level_score),
        level_score=level_score,
        word_count=word_count,
        unique_word_count=len(set(words)),
        average_word_score=round(average_word_score, 1),
        average_word_length=round(average_word_length, 1),
        average_sentence_length=round(average_sentence_length, 1),
        difficult_word_percentage=round(difficult_word_percentage, 1),
    )


def analyze_documents(documents: list[TextDocument]) -> list[TextDifficulty]:
    analyses = [analyze_text(document.name, document.text) for document in documents]
    combined_text = "\n\n".join(document.text for document in documents)
    if combined_text.strip():
        analyses.insert(0, analyze_text("Alle input_txt bestanden samen", combined_text))
    return analyses


def analyze_pages(pages: list[PageText]) -> list[PageDifficulty]:
    page_scores: list[PageDifficulty] = []
    for page in pages:
        text_difficulty = analyze_text(f"{page.source} pagina {page.page_number}", page.text)
        ranking = build_word_ranking(Counter(extract_words(page.text)))
        top_words = ", ".join(item.word for item in ranking[:5])
        page_scores.append(
            PageDifficulty(
                source=page.source,
                page_number=page.page_number,
                score=text_difficulty.level_score,
                level=text_difficulty.level,
                word_count=text_difficulty.word_count,
                average_word_score=text_difficulty.average_word_score,
                difficult_word_percentage=text_difficulty.difficult_word_percentage,
                top_difficult_words=top_words,
            )
        )

    return sorted(page_scores, key=lambda item: (-item.score, item.source, item.page_number))

