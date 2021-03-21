from db import db


class MachineModel(db.Model):
    __tablename__ = "machines"

    machine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"machine_id": self.machine_id, "name": self.name}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(machine_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
