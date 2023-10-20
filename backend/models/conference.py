from extensions import db


class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(200), nullable=True)
    rsvp = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(300), nullable=True)
    url = db.Column(db.String(300), nullable=True)

    # Add a relationship to track which user created the conference
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    creator = db.relationship("User", backref="conferences")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date_time": self.date_time.isoformat()
            if self.date_time
            else None,  # Convert datetime to string
            "venue": self.venue,
            "rsvp": self.rsvp,
            "image_url": self.image_url,
            "url": self.url,
            "user_id": self.user_id,
            "creator": {
                "id": self.creator.id,
                "email": self.creator.email,
                "full_name": self.creator.full_name,
                "is_admin": self.creator.is_admin
                # Add more user fields here as required
            },
        }
