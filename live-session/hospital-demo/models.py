from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Doctor (db.Model, SerializerMixin):
    __tablename__ = "doctors"

    serialize_rules=('-appointments.doctor','-appointments.patient')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialism = db.Column(db.String)

    appointments = db.relationship("Appointment", back_populates="doctor", cascade="all, delete-orphan")
    patients=association_proxy("appointments", "patient", creator=lambda p: Appointment(patient=p) )


    # def to_json(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "specialism": self.specialism
    #     }

    def __repr__(self):
        return f"Doctor {self.id}: {self.name} - {self.specialism}"

class Patient (db.Model, SerializerMixin):
    __tablename__ = "patients"

    serialize_rules=('appointments.complaint',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.Date) #YYYY-MM-DD

    appointments = db.relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")
    doctors=association_proxy("appointments", "doctor",creator=lambda d: Appointment(doctor=d) )

    # def to_json(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "birthdate": self.birthdate
    #     }

    def __repr__(self):
        return f"{self.id}: {self.name}"


class Appointment(db.Model, SerializerMixin):

    __tablename__ = "appointments"

    serialize_rules=('-doctor.appointments','-patient.appointments')

    id = db.Column(db.Integer, primary_key=True)
    complaint = db.Column(db.String)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    
    doctor = db.relationship("Doctor", back_populates='appointments')
    patient = db.relationship("Patient", back_populates='appointments')
