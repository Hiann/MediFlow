from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="MediFlow System")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROTAS DE API (Backend) ---

@app.post("/api/doctors/", response_model=schemas.DoctorResponse)
def create_doctor_api(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db=db, doctor=doctor)

@app.get("/api/doctors/", response_model=List[schemas.DoctorResponse])
def read_doctors_api(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

# NOVO: Editar Médico
@app.put("/api/doctors/{doctor_id}", response_model=schemas.DoctorResponse)
def update_doctor_api(doctor_id: int, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = crud.update_doctor(db, doctor_id, doctor)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return db_doctor

# NOVO: Deletar Médico
@app.delete("/api/doctors/{doctor_id}")
def delete_doctor_api(doctor_id: int, db: Session = Depends(get_db)):
    success = crud.delete_doctor(db, doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return {"detail": "Médico deletado com sucesso"}

@app.post("/api/appointments/", response_model=schemas.AppointmentResponse)
def create_appointment_api(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = crud.create_appointment(db, appointment)
    if db_appointment is None:
        raise HTTPException(status_code=400, detail="Horário indisponível para este médico!")
    return db_appointment

# --- ROTAS DE PÁGINAS (Frontend) ---

@app.get("/", response_class=HTMLResponse)
async def view_dashboard(request: Request, db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "appointments": appointments
    })

@app.get("/agendar", response_class=HTMLResponse)
async def view_agendar(request: Request, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse("agendar.html", {
        "request": request, 
        "doctors": doctors
    })

@app.get("/medicos", response_class=HTMLResponse)
async def view_medicos(request: Request, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse("medicos.html", {
        "request": request, 
        "doctors": doctors
    })