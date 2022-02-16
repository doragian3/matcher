from app import db
from app.models import Skill, Job, Candidate, candidate_skills
from flask import jsonify, abort
from difflib import SequenceMatcher


def add_skill_control(skill_name):
    """
    Add skill to db skills with skill name
    :param skill_name: str
    :return: jsonify result
    """
    try:
        if skill_name is None:
            raise Exception("There is no Skill name")

        exists = db.session.query(Skill).filter_by(name=skill_name).first()
        if exists:
            return jsonify("skill already exists")

        s = Skill(name=skill_name)

        db.session.add(s)
        db.session.commit()
        return jsonify("skill was added")
    except Exception as ex:
        abort(500)


def add_job_control(title, skill_id):
    """
     Add job to db jobs with title and skill id
    :param title: str
    :param skill_id: str
    :return: jsonify result
    """
    try:
        if title is None or skill_id is None:
            raise Exception("The arguments are missing")

        exists = db.session.query(Job).filter_by(title=title).all()
        if len(exists) > 0:
            return jsonify("Job already exists")
        skill_exists = db.session.query(Skill).filter_by(id=skill_id).all()
        if len(skill_exists) == 0:
            return jsonify("Skill not exists")

        j = Job(title, skill_id=skill_exists[0].id)
        db.session.add(j)
        db.session.commit()
        return jsonify("job was added")
    except Exception as ex:
        abort(500)


def add_candidate_control(title, skills_ids):
    """
    Add candidate to db candidate, and add rows to the association table candidate_skills
    :param title: str
    :param skills: list
    :return: jsonify result
    """
    try:
        if title is None or skills_ids is None:
            raise Exception("The title or skills Missing")

        skills_ids_obj = db.session.query(Skill).filter(Skill.id.in_(skills_ids)).all()
        if len(skills_ids_obj) != len(skills_ids):
            return jsonify("Some skills not exists")

        c = Candidate(title=title)
        for s in skills_ids_obj:
            c.skills_to_candidate.append(s)
        db.session.add(c)
        db.session.commit()
        return jsonify("candidate was added")
    except Exception as ex:
        abort(500)


def candidate_finder_control(job_id):
    """
    Searching candidate match
    :param job_id: str
    :return: jsonify result
    """
    try:
        matched_candidate_title = []
        job_search = db.session.query(Job).filter_by(id=job_id).first()
        if job_search is None:
            raise Exception("Job doesnt exists")

        matched_candidate_skill = db.session.query(candidate_skills).filter_by(skill_id=job_search.skill_id).all()
        matched_candidate_skill = [candidate_id for candidate_id, skill_id in matched_candidate_skill]
        all_candidate = db.session.query(Candidate).all()

        for candidate in all_candidate:
            if SequenceMatcher(None, job_search.title, candidate.title).ratio() > 0.5:
                matched_candidate_title.append(candidate.id)
        if len(matched_candidate_skill) == 0 and len(matched_candidate_title) == 0:
            return jsonify("candidates not founded")
        else:
            return jsonify(
                f"candidate was founded by skill candidate ids:{matched_candidate_skill} by title candidate ids:: {set(matched_candidate_title)}")
    except Exception as ex:
        abort(500)
