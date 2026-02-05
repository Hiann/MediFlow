from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

# Classe Pai: O Médico
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String) # Ex: Cardiologista, Clínico Geral
    
    # Relacionamento: Um médico tem VÁRIAS consultas
    appointments = relationship("Appointment", back_populates="doctor")

# Classe Filha: A Consulta
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    patient_phone = Column(String) # Para enviar zap depois (ideia futura)
    date_time = Column(DateTime)   # Data e Hora exata
    notes = Column(String, nullable=True)
    status = Column(String, default="Agendado") # Agendado, Concluído, Cancelado
    
    # Chave Estrangeira: Aponta para o ID do Médico
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    # Relacionamento Reverso: A consulta sabe quem é seu médico
    doctor = relationship("Doctor", back_populates="appointments")