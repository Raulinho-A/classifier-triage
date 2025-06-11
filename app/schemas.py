from pydantic import BaseModel
from typing import Literal

class TriageInput(BaseModel):
    sex: Literal[0, 1]                  # 0 = Female, 1 = Male (por ejemplo)
    age: int
    arrival_mode: int                  # Codificado numéricamente
    injury: int                        # 0 = No, 1 = Sí
    chief_complain: str                # Texto libre
    mental: int                        # Escala tipo AVPU o similar
    pain: int                          # 0 = No, 1 = Sí
    nrs_pain: int                      # Escala numérica del dolor 0-10
    sbp: int                           # Systolic BP
    dbp: int                           # Diastolic BP
    hr: int                            # Heart Rate
    rr: int                            # Respiratory Rate
    bt: float                          # Body Temperature