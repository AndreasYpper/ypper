from flask_restful import Resource, reqparse
from models.machine import MachineModel
from sqlalchemy.exc import SQLAlchemyError


class Machine(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name is required.")
    parser.add_argument(
        "last_semi_service", required=True, help="This field is required."
    )
    parser.add_argument(
        "last_full_service", type=str, required=True, help="This field is required."
    )
    parser.add_argument(
        "last_full_service", type=str, required=True, help="This field is required."
    )
    parser.add_argument(
        "network_address", type=str, required=False
    )
    parser.add_argument(
        "machine_status_id", type=int, required=True, help="This field is required."
    )

    def get(self, _id):
        machine = MachineModel.find_by_id(_id)

        if machine:
            return machine.json(), 200

        return {"message": "Machine not found"}, 400

    def post(self):
        data = Machine.parser.parse_args()
        print(data)

        machine = MachineModel(**data)
        try:
            machine.save_to_db()

        except SQLAlchemyError as e:
            error = str(e.__dict__["orig"])
            return error, 500

        return machine.json()


class Machines(Resource):
    def get(self):
        return {"machines": [machine.json() for machine in MachineModel.query.all()]}
