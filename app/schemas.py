from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# --- SCHEMAS DE MÉDICO ---
class DoctorBase(BaseModel):
    name: str
    specialty: str

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS DE CONSULTA ---
class AppointmentBase(BaseModel):
    patient_name: str
    patient_phone: str
    date_time: datetime
    notes: Optional[str] = None
    doctor_id: int

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    status: str
    doctor: DoctorResponse # Retorna os dados do médico junto!
    class Config:
        from_attributes = True