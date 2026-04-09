from pydantic import BaseModel


class ImporteRow(BaseModel):
    concepto: str
    importe: float
    moneda: str = "EUR"


class ExcelImportes(BaseModel):
    """Excel con filas de importes (ej. facturas, liquidaciones)."""
    titulo: str
    filas: list[ImporteRow]
    total: float | None = None


# ---------------------------------------------------------------------------


class ConceptoRow(BaseModel):
    codigo: str
    descripcion: str
    valor: str


class ExcelConceptos(BaseModel):
    """Excel con conceptos clave-valor (ej. fichas de producto, configuraciones)."""
    referencia: str
    conceptos: list[ConceptoRow]
