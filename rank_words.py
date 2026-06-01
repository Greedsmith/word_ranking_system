from __future__ import annotations

from woordenboek.config import INPUT_PAGES_DIR, INPUT_WORDS_DIR, OUTPUT_DIR
from woordenboek.ranking import analyze_documents, analyze_pages, build_word_ranking
from woordenboek.reports import (
    write_page_csv,
    write_page_report,
    write_text_score_csv,
    write_text_score_report,
    write_word_csv,
    write_word_text_report,
)
from woordenboek.text_utils import count_words_in_documents, read_page_texts, read_text_documents


def prepare_directories() -> None:
    INPUT_WORDS_DIR.mkdir(exist_ok=True)
    INPUT_PAGES_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def rank_words() -> int:
    documents = read_text_documents(INPUT_WORDS_DIR)
    ranking = build_word_ranking(count_words_in_documents(documents))

    write_word_csv(ranking, OUTPUT_DIR / "word_ranking.csv")
    write_word_text_report(ranking, OUTPUT_DIR / "word_ranking.txt")
    return len(ranking)


def rank_pages() -> int:
    pages = analyze_pages(read_page_texts(INPUT_PAGES_DIR))

    write_page_csv(pages, OUTPUT_DIR / "page_ranking.csv")
    write_page_report(pages, OUTPUT_DIR / "page_ranking.txt")
    return len(pages)


def rank_story_scores() -> int:
    documents = read_text_documents(INPUT_WORDS_DIR)
    analyses = analyze_documents(documents)

    write_text_score_csv(analyses, OUTPUT_DIR / "story_level.csv")
    write_text_score_report(analyses, OUTPUT_DIR / "story_level.txt")
    return len(analyses)


def main() -> None:
    prepare_directories()

    unique_words = rank_words()
    page_count = rank_pages()
    text_count = rank_story_scores()

    print(f"{unique_words} unieke woorden verwerkt.")
    print(f"{page_count} pagina's verwerkt.")
    print(f"{text_count} tekstscore-analyses gemaakt.")
    print(f"Resultaten opgeslagen in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
