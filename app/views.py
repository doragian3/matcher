from flask import jsonify, request

from app import app
from app import controller


@app.route("/")
def index():
    return "<p>Hello to Jobs Finder!</p>"


@app.route("/add_skill/", methods=["POST"])
def add_skill():
    try:
        skill_name = request.json.get('name')
        return controller.add_skill_control(skill_name)

    except Exception as ex:
        return jsonify("skill name argument don't exists")


@app.route("/add_job/", methods=["POST"])
def add_job():
    try:
        title = request.json.get('title')
        skill_id = request.json.get('skill_id')
        return controller.add_job_control(title, skill_id)

    except Exception as ex:
        return jsonify("jobs arguments missing")


@app.route("/add_candidate/", methods=["POST"])
def add_candidate():
    try:
        title = request.json.get('title')
        skills_ids = request.json.get('skills_ids')
        return controller.add_candidate_control(title, skills_ids)
    except Exception as ex:
        return jsonify("candidate arguments missing")


@app.route("/candidate_finder/", methods=["POST"])
def candidate_finder():
    try:
        job_id = request.json.get('job_id')
        return controller.candidate_finder_control(job_id)
    except Exception as ex:
        return jsonify("candidate arguments missing")

