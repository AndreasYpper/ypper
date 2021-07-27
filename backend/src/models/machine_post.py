from db import db


class MachinePostModel(db.Model):
    __tablename__ = "machine_posts"

    machine_post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(150))
    author = db.Column(db.String(30))
    active = db.Column(db.Boolean)

    machine_id = db.Column(
        db.Integer, db.ForeignKey("machines.machine_id")
    )

    def __init__(self, title, content, author, machine_id):
        self.title = title
        self.content = content
        self.active = author
        self.active = True
        self.machine_id = machine_id

    def json(self):
        return {
            "machine_post_id": self.machine_post_id,
            "title": self.title,
            "content": self.content,
            'author': self.author,
            'active': self.active,
            'machine_id': self.machine_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(machine_post_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
