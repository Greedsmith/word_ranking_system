from __future__ import annotations

import csv
from pathlib import Path

from .ranking import PageDifficulty, TextDifficulty
from .word_scoring import WordScore

def yes_no(value: bool) -> str:
    return "ja" if value else "nee"

def write_word_csv(ranking: list[WordScore], output_file: Path) -> None:
    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "woord",
                "score",
                "lengte",
                "lengte_punten",
                "tweeklanken",
                "heeft_ch",
                "heeft_sch",
                "lettergrepen_schatting",
                "medeklinkerclusters",
                "zeldzame_letter",
                "frequentie"
            ]
        )
        for item in ranking:
            features = item.features
            writer.writerow(
                [
                    item.word,
                    item.score,
                    features.length,
                    features.length_points,
                    features.diphthong_count,
                    yes_no(features.has_ch),
                    yes_no(features.has_sch),
                    features.syllable_count,
                    features.consonant_cluster_count,
                    yes_no(features.has_rare_letter),
                    item.frequency
                ]
            )

def write_word_text_report(ranking: list[WordScore], output_file: Path) -> None:
    lines = [
        "Woorden gerangschikt op moeilijkheid",
        "",
        "woord | score | lengte | lengtepunten | tweeklanken | ch | sch | lettergrepen | clusters | zeldzame letter | frequentie",
        "-" * 124,
    ]

    for item in ranking:
        features = item.features
        lines.append(
            f"{item.word} | {item.score} | {features.length} | {features.length_points} | "
            f"{features.diphthong_count} | {yes_no(features.has_ch)} | "
            f"{yes_no(features.has_sch)} | {features.syllable_count} | "
            f"{features.consonant_cluster_count} | {yes_no(features.has_rare_letter)} | "
            f"{item.frequency}"
        )

    output_file.write_text("\n".join(lines), encoding="utf-8")

def write_text_score_csv(analyses: list[TextDifficulty], output_file: Path) -> None:
    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "tekst",
                "score",
                "woorden",
                "unieke_woorden",
                "gemiddelde_woordscore",
                "gemiddelde_woordlengte",
                "gemiddelde_zinslengte",
                "moeilijke_woorden_percentage"
            ]
        )
        for item in analyses:
            writer.writerow(
                [
                    item.name,
                    item.score,
                    item.word_count,
                    item.unique_word_count,
                    item.average_word_score,
                    item.average_word_length,
                    item.average_sentence_length,
                    item.difficult_word_percentage
                ]
            )

def write_text_score_report(analyses: list[TextDifficulty], output_file: Path) -> None:
    lines = [
        "Teksten gerangschikt op moeilijkheid",
        "",
        "tekst | score | woorden | unieke woorden | gem. woordscore | gem. zinslengte | moeilijke woorden %",
        "-" * 102,
    ]
    for item in analyses:
        lines.append(
            f"{item.name} | {item.score} | {item.word_count} | "
            f"{item.unique_word_count} | {item.average_word_score} | "
            f"{item.average_sentence_length} | {item.difficult_word_percentage}"
        )
    output_file.write_text("\n".join(lines), encoding="utf-8")

def write_page_csv(pages: list[PageDifficulty], output_file: Path) -> None:
    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "bron",
                "pagina",
                "score",
                "woorden",
                "gemiddelde_woordscore",
                "moeilijke_woorden_percentage",
                "moeilijkste_woorden"
            ]
        )
        for page in pages:
            writer.writerow(
                [
                    page.source,
                    page.page_number,
                    page.score,
                    page.word_count,
                    page.average_word_score,
                    page.difficult_word_percentage,
                    page.top_difficult_words
                ]
            )

def write_page_report(pages: list[PageDifficulty], output_file: Path) -> None:
    lines = [
        "Pagina's gerangschikt op moeilijkheid",
        "",
        "bron | pagina | score | woorden | gem. woordscore | moeilijke woorden % | moeilijkste woorden",
        "-" * 102,
    ]
    for page in pages:
        lines.append(
            f"{page.source} | {page.page_number} | {page.score} | "
            f"{page.word_count} | {page.average_word_score} | "
            f"{page.difficult_word_percentage} | {page.top_difficult_words}"
        )
    output_file.write_text("\n".join(lines), encoding="utf-8")
