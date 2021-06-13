from flask_restful import Resource, reqparse
from models.machine_status import MachineStatusModel
from sqlalchemy.exc import SQLAlchemyError


class MachineStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Title is required.")

    def get(self, _id):
        machine_status = MachineStatusModel.find_by_id(_id)

        if machine_status:
            return machine_status.json(), 200

        return {"message": "Machine not found"}, 400

    def post(self):
        data = MachineStatus.parser.parse_args()
        print(data)

        machine = MachineStatusModel(**data)
        try:
            machine.save_to_db()

        except SQLAlchemyError as e:
            error = str(e.__dict__["orig"])
            return error, 500

        return machine.json()


class MachineStatuses(Resource):
    def get(self):
        return {
            "machine_statuses": [
                machine_status.json() for machine_status in MachineStatusModel.query.all()
            ]
        }
