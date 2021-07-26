from db import db
from sqlalchemy import Date


class MachineModel(db.Model):
    __tablename__ = "machines"

    machine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    last_semi_service = db.Column(Date)
    last_full_service = db.Column(Date)
    network_address = db.Column(db.String(40))

    machine_status_id = db.Column(
        db.Integer, db.ForeignKey("machine_statuses.machine_status_id")
    )

    def __init__(
        self,
        name,
        last_semi_service,
        last_full_service,
        network_address,
        machine_status_id,
    ):
        self.name = name
        self.last_semi_service = last_semi_service
        self.last_full_service = last_full_service
        self.network_address = network_address
        self.machine_status_id = machine_status_id

    def json(self):
        return {
            "machine_id": self.machine_id,
            "name": self.name,
            "last_semi_service": str(self.last_semi_service),
            "last_full_service": str(self.last_full_service),
            "network_address": self.network_address,
            "machine_status_id": self.machine_status_id,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(machine_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
