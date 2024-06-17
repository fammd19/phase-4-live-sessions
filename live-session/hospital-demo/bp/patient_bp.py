from flask import Blueprint, request, make_response, jsonify
from models import db, Patient, Doctor, Appointment
from datetime import datetime

patient_bp = Blueprint("patient", __name__, url_prefix="/patients")

@patient_bp.route ("/")
def index():
    patients_from_db = Patient.query.all()

    patients = []

    for patient in patients_from_db:
        patients.append(patient.to_dict())

    return make_response( jsonify(patients), 200 )


@patient_bp.route ("/", methods=["POST"])
def create():
    birthdate = datetime.strptime(request.json['birthdate'],'%Y-%m-%d')
    
    new_patient = Patient(name=request.json["name"], birthdate=birthdate)

    db.session.add(new_patient)
    db.session.commit()

    if new_patient.id:
        return make_response(jsonify(new_patient.to_dict()), 201)

    else:
        make_response (jsonify( {"message": "Unsuccessful"}), 404)


@patient_bp.route ("/<int:patient_id>")
def show_by_id(patient_id):
    patient = Patient.query.filter(Patient.id==patient_id).first()

    if patient:
        return make_response (jsonify( {"message": "Patient found"}), 200)

    else: 
        return make_response (jsonify( {"message": "Patient not found"}), 404)


@patient_bp.route('/int:patient_id', methods=['PATCH'])
def update(patient_id):
    pass

@patient_bp.route('/int:patient_id', methods=['DELETE'])
def delete (patient_id):
    pass


#as patient makes appointment, create appointment route should be in patients bp
@patient_bp.route ("/<int:patient_id>/consult-doctor", methods=["POST"])  
def consult_doctor(patient_id):
    patient = Patient.query.filter(Patient.id==patient_id).first()

    if patient:
        doctor = Doctor.query.filter(Doctor.id==request.json['doctor_id']).first()
        if doctor:
            appointment = Appointment(patient_id=patient.id, doctor_id=doctor.id, complaint=request.json['complaint'])
            db.session.add(appointment)
            db.session.commit()

            if appointment.id:
                return make_response(jsonify({"message": "Appointment made"}), 200)

        else:
            return make_response(jsonify({"message": "No Dcotor found"}), 404)

    else:
        return make_response(jsonify({"message": "Patient not found"}), 404)


