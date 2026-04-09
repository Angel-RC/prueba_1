from __future__ import annotations

import openpyxl

from models.excel_types import ExcelImportes, ImporteRow
from .base import ExcelProcessor


class ExcelImportesProcessor(ExcelProcessor):
    def process(self, wb: openpyxl.Workbook) -> ExcelImportes:
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))

        # TODO: adaptar índices de columna a la estructura real del Excel
        titulo = str(rows[0][0]) if rows else ""
        filas = []
        for row in rows[2:]:  # asume fila 0 = título, fila 1 = cabeceras
            if row[0] is None:
                continue
            filas.append(ImporteRow(
                concepto=str(row[0]),
                importe=float(row[1] or 0),
                moneda=str(row[2]) if row[2] else "EUR",
            ))

        total = sum(f.importe for f in filas) if filas else None
        return ExcelImportes(titulo=titulo, filas=filas, total=total)
