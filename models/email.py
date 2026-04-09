from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .attachment import Attachment


@dataclass
class EmailMetadata:
    subject: str
    mail_from: str
    mail_to: list[str]
    mail_cc: list[str]
    date: datetime | None
    message_id: str | None


@dataclass
class Email:
    metadata: EmailMetadata
    attachments: list[Attachment] = field(default_factory=list)
    source_path: str | None = None

    def excel_attachments(self) -> list[Attachment]:
        return [a for a in self.attachments if a.is_excel()]

    def pdf_attachments(self) -> list[Attachment]:
        return [a for a in self.attachments if a.is_pdf()]
