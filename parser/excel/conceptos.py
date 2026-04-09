from __future__ import annotations

import openpyxl

from models.excel_types import ExcelConceptos, ConceptoRow
from .base import ExcelProcessor


class ExcelConceptosProcessor(ExcelProcessor):
    def process(self, wb: openpyxl.Workbook) -> ExcelConceptos:
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))

        # TODO: adaptar índices de columna a la estructura real del Excel
        referencia = str(rows[0][1]) if rows else ""
        conceptos = []
        for row in rows[1:]:  # asume fila 0 = cabecera con referencia
            if row[0] is None:
                continue
            conceptos.append(ConceptoRow(
                codigo=str(row[0]),
                descripcion=str(row[1] or ""),
                valor=str(row[2] or ""),
            ))

        return ExcelConceptos(referencia=referencia, conceptos=conceptos)
