from __future__ import annotations

from abc import ABC, abstractmethod

import openpyxl
from pydantic import BaseModel


class ExcelProcessor(ABC):
    @abstractmethod
    def process(self, wb: openpyxl.Workbook) -> BaseModel: ...
