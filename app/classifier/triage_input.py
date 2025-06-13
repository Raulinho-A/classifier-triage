from pydantic import BaseModel, Field

class TriageInput(BaseModel):
    Group: int = Field(..., description="Tipo de ED: 1 = Local (3er nivel), 2 = Regional (4to nivel)")
    Sex: int = Field(..., description="Sexo del paciente: 1 = Mujer, 2 = Hombre")
    Age: int = Field(..., description="Edad del paciente (años)")
    Arrival_mode: int = Field(..., description="Modo de llegada: 1=Camina, 2=Ambulancia pública, 3=Vehículo privado, etc.")
    Injury: int = Field(..., description="Llegó por lesión: 1 = No, 2 = Sí")
    Mental: int = Field(..., description="Estado mental: 1=Alerta, 2=Respuesta verbal, 3=Respuesta al dolor, 4=Inconsciente")
    NRS_pain: float = Field(..., description="Escala numérica del dolor (0-10)")
    SBP: float = Field(..., description="Presión arterial sistólica (mmHg)")
    HR: float = Field(..., description="Frecuencia cardíaca (latidos por minuto)")
    RR: float = Field(..., description="Frecuencia respiratoria (respiraciones por minuto)")
    BT: float = Field(..., description="Temperatura corporal (°C)")

