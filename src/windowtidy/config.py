from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json


@dataclass
class Config:
    grid_cols: int = 3
    grid_rows: int = 2

    @staticmethod
    def path() -> Path:
        return Path.home() / ".config" / "windowtidy" / "config.json"

    @classmethod
    def load(cls) -> "Config":
        p = cls.path()
        if not p.exists():
            return cls()
        data = json.loads(p.read_text())
        return cls(**{k: data.get(k, getattr(cls, k)) for k in ("grid_cols", "grid_rows")})

