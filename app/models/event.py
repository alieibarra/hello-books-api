from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date
        }

        return result