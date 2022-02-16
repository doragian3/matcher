# Matcher app
This is matcher job app
Writing with flask and SQLAlchemy

Objects:
  Skill
  
  candidate
  
  Job

Table for each object and Association table candidate_skills - between Candidate skills to skill table 


for the front used postman:

http://127.0.0.1:5000/add_skill/
json = {"name":"c#"}

http://127.0.0.1:5000/add_job/
{"title":"software developer", "skill_id":"1"}

http://127.0.0.1:5000/add_candidate/
{"title":"Software", "skills_ids":[1,2]}

http://127.0.0.1:5000/candidate_finder/
{"job_id":1 }


