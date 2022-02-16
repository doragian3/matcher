from app import db


"""
This is association table between Candidate skills to skill table 
"""
candidate_skills = db.Table('candidate_skills',
                            db.Column('candidate_id', db.Integer, db.ForeignKey('candidates.id')),
                            db.Column('skill_id', db.Integer, db.ForeignKey('skills.id')))


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    jobs = db.relationship("Job", back_populates="skills")

    # job = db.relationship("Job", back_populates="parent")

    def __init__(self, name):
        self.name = name


class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    skills_to_candidate = db.relationship('Skill', secondary='candidate_skills', backref='own')


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)
    skills = db.relationship("Skill", back_populates="jobs", uselist=False)

    def __init__(self, title, skill_id):
        self.title = title
        self.skill_id = skill_id
