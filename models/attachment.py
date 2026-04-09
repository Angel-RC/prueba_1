from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ExcelLLMInfo:
    summary: str | None = None           # descripción general del documento
    topics: list[str] = field(default_factory=list)   # temas/categorías detectados
    key_values: dict[str, str] = field(default_factory=dict)  # campos relevantes extraídos


@dataclass
class ExcelInfo:
    sheets: list[str]
    row_count: dict[str, int]
    col_count: dict[str, int]
    headers: dict[str, list[str]]  # sheet -> first row values
    llm_info: ExcelLLMInfo | None = None


@dataclass
class PDFInfo:
    page_count: int
    text_preview: str | None = None  # first ~500 chars


@dataclass
class Attachment:
    filename: str
    content_type: str
    content: bytes
    info: ExcelInfo | PDFInfo | None = None

    @property
    def extension(self) -> str:
        return Path(self.filename).suffix.lower()

    def is_excel(self) -> bool:
        return self.extension in {".xlsx", ".xls", ".xlsm"}

    def is_pdf(self) -> bool:
        return self.extension == ".pdf"
