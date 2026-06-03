from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

WORD_PATTERN = re.compile(r"[a-zA-Z\u00c0-\u017f]+(?:['-][a-zA-Z\u00c0-\u017f]+)*")
PAGE_SEPARATOR_PATTERN = re.compile(r"(?:\f|^\s*={3,}\s*pagina\s*={3,}\s*$)", re.IGNORECASE | re.MULTILINE)
SENTENCE_PATTERN = re.compile(r"[.!?]+")

@dataclass(frozen=True)
class TextDocument:
    name: str
    text: str

@dataclass(frozen=True)
class PageText:
    source: str
    page_number: int
    text: str

def extract_words(text: str) -> list[str]:
    matches = WORD_PATTERN.findall(text.lower())
    return [word.strip("'-") for word in matches if word.strip("'-")]

def count_sentences(text: str) -> int:
    sentence_count = len([part for part in SENTENCE_PATTERN.split(text) if part.strip()])
    return max(1, sentence_count)

def read_text_documents(input_dir: Path) -> list[TextDocument]:
    documents: list[TextDocument] = []
    for txt_file in sorted(input_dir.glob("*.txt")):
        documents.append(TextDocument(name=txt_file.name, text=txt_file.read_text(encoding="utf-8")))
    return documents

def count_words_in_documents(documents: list[TextDocument]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for document in documents:
        counter.update(extract_words(document.text))
    return counter

def split_pages(text: str) -> list[str]:
    pages = [page.strip() for page in PAGE_SEPARATOR_PATTERN.split(text)]
    return [page for page in pages if page]

def read_page_texts(input_dir: Path) -> list[PageText]:
    pages: list[PageText] = []
    for txt_file in sorted(input_dir.glob("*.txt")):
        for page_number, page_text in enumerate(split_pages(txt_file.read_text(encoding="utf-8")), start=1):
            pages.append(PageText(source=txt_file.name, page_number=page_number, text=page_text))
    return pages
