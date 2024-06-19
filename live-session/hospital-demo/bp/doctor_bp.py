from flask import Blueprint, request, make_response, jsonify
from models import db, Doctor

doctor_bp = Blueprint("doctor", __name__, url_prefix="/doctors")

@doctor_bp.route ("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        doctors_from_db = Doctor.query.all()
        
        doctors = []

        for doctor in doctors_from_db:
            doctors.append(doctor.to_dict())

        return make_response( jsonify(doctors), 200 )

    elif request.method == "POST":
        new_doctor = Doctor(name=request.json["name"], specialism=request.json["specialism"])

        db.session.add(new_doctor)
        db.session.commit()

        if new_doctor.id:
            return make_response(jsonify(new_doctor.to_dict()), 201)

        else:
            make_response (jsonify( {"message": "Unsuccessful"}), 404)

# @doctor_bp.route ("/")
# def index():
#     doctors_from_db = Doctor.query.all()

#     doctors = []

#     for doctor in doctors_from_db:
#         #doctors.append(doctor.to_json())
#         doctors.append(doctor.to_dict())

#     return make_response( jsonify(doctors), 200 )


# @doctor_bp.route ("/", methods=["POST"])
# def create():
#     new_doctor = Doctor(name=request.json["name"], specialism=request.json["specialism"])

#     db.session.add(new_doctor)
#     db.session.commit()

#     if new_doctor.id:
#         #return make_response(jsonify(new_doctor.to_json()), 201)
#         return make_response(jsonify(new_doctor.to_dict()), 201)

#     else:
#         make_response (jsonify( {"message": "Unsuccessful"}), 404)

@doctor_bp.route ('/<int:doctor_id>', methods=["GET", "PATCH", "DELETE"])
def show_by_id(doctor_id):
    doctor = Doctor.query.filter(Doctor.id == doctor_id).first()

    if doctor:

        if request.method == "GET":
            return make_response(jsonify(doctor.to_dict()), 200)

        elif request.method == "PATCH":
            for attr in request.json:
                setattr(doctor, attr, request.json[attr])

            db.session.commit()
            return make_response(jsonify(doctor.to_dict()), 200)

        elif request.method == "DELETE":
            db.session.delete(doctor)
            db.session.commit()

            return make_response(jsonify({"message":"Succesfully deleted"}), 200)
        

        return make_response(jsonify(doctor.to_dict()), 200)

    return make_response(jsonify({"error": "No doctor found"}), 404)

    