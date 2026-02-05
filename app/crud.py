from sqlalchemy.orm import Session
from . import models, schemas
from datetime import timedelta

# --- MÉDICOS ---
def get_doctors(db: Session):
    return db.query(models.Doctor).all()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# NOVO: Atualizar Médico
def update_doctor(db: Session, doctor_id: int, doctor_data: schemas.DoctorCreate):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if db_doctor:
        db_doctor.name = doctor_data.name
        db_doctor.specialty = doctor_data.specialty
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

# NOVO: Deletar Médico
def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if db_doctor:
        # Nota: Se houver consultas vinculadas, o banco pode bloquear dependendo da config.
        # Aqui vamos deletar o médico. As consultas podem ficar órfãs ou deletar em cascata.
        db.delete(db_doctor)
        db.commit()
        return True
    return False

# --- CONSULTAS ---
def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    # 1. Regra de Negócio: Verificar Conflito
    exists = db.query(models.Appointment).filter(
        models.Appointment.doctor_id == appointment.doctor_id,
        models.Appointment.date_time == appointment.date_time,
        models.Appointment.status != "Cancelado"
    ).first()

    if exists:
        return None 

    # 2. Se livre, cria
    db_appointment = models.Appointment(**appointment.dict(), status="Agendado")
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session):
    return db.query(models.Appointment).order_by(models.Appointment.date_time).all()