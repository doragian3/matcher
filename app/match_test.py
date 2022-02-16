from flask import Flask
import unittest
from app import app
from app import db


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
         Creates a new database for the unit test to use
        """
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debug.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """
         Ensures that the database is emptied for next unit test
        """
        self.app.te = Flask(__name__)
        db.drop_all()

    def test_add_skill(self):
        response = self.app.post("/add_skill/", json={"name": "test"})
        self.assertTrue("skill was added" in str(response.data))

    def test_add_skill_already_exists(self):
        self.app.post("/add_skill/", json={"name": "test_skill"})
        response = self.app.post("/add_skill/", json={"name": "test_skill"})
        self.assertTrue("skill already exists" in str(response.data))

    def test_add_candidate(self):
        self.app.post("/add_skill/", json={"name": "test_skill"})
        response = self.app.post("/add_candidate/", json={"title": "Software developer", "skills_ids": [1]})
        self.assertTrue("candidate was added" in str(response.data))

    def test_add_candidate_skill_dont_exists(self):
        response = self.app.post("/add_candidate/", json={"title": "Software developer", "skills_ids": [1]})
        self.assertTrue("Some skills not exists" in str(response.data))


    def test_add_job(self):
        self.app.post("/add_skill/", json={"name": "test_skill"})
        response = self.app.post("/add_job/", json={"title": "Software developer", "skill_id": "1"})
        self.assertTrue("job was added" in str(response.data))

    def test_candidate_finder_success(self):
        self.app.post("/add_skill/", json={"name": "test_skill"})
        self.app.post("/add_job/", json={"title": "Software developer", "skill_id": "1"})
        self.app.post("/add_candidate/", json={"title": "Software developer", "skills_ids": [1]})
        response = self.app.post("/candidate_finder/", json={"job_id": 1})
        self.assertTrue("candidate was founded by skill" in str(response.data))

    def test_candidate_finder_not_found(self):
        self.app.post("/add_skill/", json={"name": "test_skill"})
        self.app.post("/add_skill/", json={"name": "test_skill2"})
        self.app.post("/add_job/", json={"title": "Software developer", "skill_id": "1"})
        self.app.post("/add_candidate/", json={"title": "hr", "skills_ids": [2]})
        response = self.app.post("/candidate_finder/", json={"job_id": 1})
        self.assertTrue("candidates not founded" in str(response.data))


if __name__ == '__main__':
    unittest.main()
