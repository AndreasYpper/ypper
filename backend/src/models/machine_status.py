from db import db


class MachineStatusModel(db.Model):
    __tablename__ = "machine_statuses"

    machine_status_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))

    machines = db.relationship("MachineModel", backref="machine_statuses", lazy=True)

    def __init__(self, title):
        self.title = title

    def json(self):
        return {"machine_status_id": self.machine_status_id, "title": self.title}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(machine_status_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
