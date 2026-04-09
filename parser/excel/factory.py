from __future__ import annotations

from models.attachment import Attachment
from .base import ExcelProcessor
from .conceptos import ExcelConceptosProcessor
from .importes import ExcelImportesProcessor


def get_processor(att: Attachment) -> ExcelProcessor:
    """Selecciona el processor adecuado según el adjunto.

    TODO: ajustar la heurística al nombre/contenido real de los excels.
    """
    name = att.filename.lower()
    if "importe" in name or "factura" in name or "liquidacion" in name:
        return ExcelImportesProcessor()
    return ExcelConceptosProcessor()
