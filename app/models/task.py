from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    dueDate = db.Column(db.DateTime, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False, default="backlog")
    

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "dueDate": self.dueDate,
            "priority": self.priority,
            "status": self.status,
        }

        return result