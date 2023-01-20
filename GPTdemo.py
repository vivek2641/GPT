from fastapi import FastAPI
import openai
import json

app = FastAPI()

openai.api_key = "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"


job_filepath = "Json/job_detail/Hewlett Packard Enterprise.json"
with open(job_filepath, 'r') as json_file:
    job_data = json.load(json_file)

linkedindata = "linkedindatafinal.json"
filepath = "Json/"+linkedindata
with open(filepath, 'r') as json_file:
    profile_data = json.load(json_file)

print(profile_data)
First_name = str(profile_data["data"]["first_name"])
last_name = profile_data["data"]["last_name"]
Occupation = profile_data["data"]["occupation"]
Email = profile_data["data"]["email"]
Summary = profile_data["data"]["summary"]
Country_full_name = profile_data["data"]
City = profile_data["data"]
state = profile_data["data"]
Languages = profile_data["data"]["languages"]
skills = profile_data["data"]["skills"]
user_carrier_data = ""
User_experiences = profile_data["data"]["user_carrier_data"]["user_experiences"]
user_education = profile_data["data"]["user_carrier_data"]["usereducation"]
User_accomplishment_organisations = profile_data["data"][
    "user_carrier_data"]["useraccomplishmentorganisations"]
user_accomplishment_projects = profile_data["data"]["user_carrier_data"]["useraccomplishmentprojects"]
User_certifications = profile_data["data"]["user_carrier_data"]["usercertifications"]
User_accomplishment_publications = profile_data["data"][
    "user_carrier_data"]["useraccomplishmentpublications"]
User_accomplishment_honors_awards = profile_data["data"][
    "user_carrier_data"]["useraccomplishmenthonorsawards"]


profile_details = "Profile details:\n" \
    "Name: "+First_name + " "+last_name + "\n"\
    "Occupation: "+Occupation + "\n"\
    "Email: "+Email + "\n"\
    "Summary: "+Summary + "\n"\
    "Country: "+Country_full_name + "\n"\
    "City: "+City + "\n"\
    "state: "+state + "\n"\
    "Languages: "+Languages + "\n"\
    "skills: "+skills + "\n"\
    "experiences: "+User_experiences + "\n"\
    "education: "+user_education + "\n"\
    "accomplishment_organisations: "+User_accomplishment_organisations + "\n"\
    "projects: "+user_accomplishment_projects + "\n"\
    "certifications: "+User_certifications + "\n"\
    "publications: "+User_accomplishment_publications + "\n"\
    "honors_awards: "+User_accomplishment_honors_awards + "\n"\
    # "Email: "+Email + "\n"\
# "Email: "+Email + "\n"\


job_details = "Job details:\n "
prompt = job_details + "\n "+profile_details + \
    "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"


gpt_prompt = prompt


@app.get("/coverletter")
def index():

    print(gpt_prompt)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.99,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9
    )
    print("----------------cover letter----------------------")
    result = response['choices'][0]['text']
    print(result)

    return result


# your_name = "Vivek Solanki"
# education = {"collage": "Sal Collage of engineering",
#              "course": "bachelor of engineering",
#              "completed year": "2021",
#              "CPI": "8.27"}
# role = "Machine Learning Engineering "
# personal_exp = {"company_name": "Maxgen technology",
#                 "years": "0.6",
#                 "position": "machine learning engineer",
#                 "projects": "face detection"
#                 }

# contact_person = "Dharmesh Thakor"
# company_name = "Prodcrew"
# job_desc = "1. Must be associated in bachelor or master degree course in computer science or related field 2. Strong command over Python programming language and OOPs 3. Familiarity with image processing algorithms with OpenCV and Numpy 4. Must be familiar with PyTorch and TorchVision frameworks 5. Must know how to prepare dataset in COCO or CityScapes formats 5. Must be available for atleast 3 months"
# passion = ""
# mydec = "My name is Vivek Solanki. I completed my Bachelors in Information Technology in 2021 and completed with 8.27 CPI. I completed my 6 months internship at MaxGen Technologies in Machine Learning. I also learned Python, Django, Machine Learning Models, Deep Learning Models, Computer Vision etc and my goal is to become a great Machine Learning Developer and I have one year experience in Fx Data Lab as Associate Machine Learning Developer"


# gpt_prompt = "Correct this to standard English:\n\nis my name vivek and i expirience in ML"
# gpt_prompt = ("Write a cover letter to " + contact_person + " from " + your_name + " for a " + role + "job at " + company_name + "." +
#               " I have " + personal_exp["years"] + " yearsn of " + personal_exp["position"] +
#               " experience at " + personal_exp["company_name"] + "."
#               " I have compeleted my graduation in " +
#               education["course"] + "at" + education["collage"] + "from" +
#               education["completed year"] +
#               "and CPI is " + education["CPI"] + "."
#               " I am excited about the job because " + job_desc + ".")


# gpt_prompt="Write a cover letter to Dharmesh Thakor from Vivek Solanki for a Machine Learning Engineering job at Prodcrew. I have 0.6 yearsn of machine learning engineer experience at Maxgen technology. I have compeleted my graduation in bachelor of engineeringatSal Collage of engineeringfrom2021and CPI is 8.27. I am excited about the job because performance Requirements: 1. Must be associated in bachelor or master degree course in computer science or related field 2. Strong command over Python programming language and OOPs 3. Familiarity with image processing algorithms with OpenCV and Numpy 4. Must be familiar with PyTorch and TorchVision frameworks 5. Must know how to prepare dataset in COCO or CityScapes formats 5. Must be available for atleast 3 months I am passionate about "
# gpt_prompt="Write a cover letter to Dharmesh Thakor from Vivek Solanki for a Machine Learning Engineering job at Prodcrew. my name is vivek solanki. i had completed my bachelors at 2021 in information technology And completed with 8.27 CPI. i had completed my 6 months of internship at maxgen technology in machine learning. also i learned python, django, Machine learning models, Deep learning models, computer vision, and etc. and My goal is to become a great machine learning developer also i have one year of expirience at Fx data labs in associate machine learning devloper. "
# gpt_prompt="Write a cover letter from Vivek Solanki to Dharmesh Thakor for Machine Learning Engineering job at Prodcrew. My name is Vivek Solanki. I completed my Bachelors in Information Technology in 2021 and completed with 8.27 CPI. I completed my 6 months internship at MaxGen Technologies in Machine Learning. I also learned Python, Django, Machine Learning Models, Deep Learning Models, Computer Vision etc and my goal is to become a great Machine Learning Developer and I have one year experience in Fx Data Lab as Associate Machine Learning Developer."
# gpt_prompt=("Write a cover letter to Dharmesh thakor they is HR of prodcrew. they are hiring for ML devloper job Requirements is " + job_desc + " so apply for that " +mydec+" .")
# gpt_prompt="Write a cover letter to Prodcrew's HR. HR name is Dharmesh Thakor. Prodcrew is working on ML project. prodcrew is hiring for Ml devloper and there requirements is \n" +job_desc+" \n so i have to apply for this job .\n My name is Vivek Solanki. I completed my Bachelors in Information Technology in 2021 and completed with 8.27 CPI. I completed my 6 months internship at MaxGen Technologies in Machine Learning. I also learned Python, Django, Machine Learning Models, Deep Learning Models, Computer Vision etc and my goal is to become a great Machine Learning Developer and I have one year experience in Fx Data Lab as Associate Machine Learning Developer."
# gpt_prompt="Write a cover letter to Prodcrew's HR department. His name is Dharmesh Thakor. An ML project is being worked on by Prodcrew. Prodcrew is hiring for the position of Ml developer, and the qualifications are as follows: 1. Must be enrolled in a computer science or comparable course leading to a bachelor's or master's degree. 2. Solid programming skills in Python and OOPs 3. Experience using OpenCV and Numpy to navigate image processing techniques 4. Must be conversant with the TorchVision and PyTorch frameworks 5. Data preparation in the COCO or CityScapes formats must be mastered.\n so i have to apply for this job .\n My name is Vivek Solanki. I completed my Bachelors in Information Technology in 2021 and completed with 8.27 CPI. I completed my 6 months internship at MaxGen Technologies in Machine Learning. I also learned Python, Django, Machine Learning Models, Deep Learning Models, Computer Vision etc and my goal is to become a great Machine Learning Developer and I have one year experience in Fx Data Lab as Associate Machine Learning Developer."


# job_filepath = "Json/job_detail/Hewlett Packard Enterprise.json"
# with open(job_filepath, 'r') as json_file:
#     job_data = json.load(json_file)

# linkedindata = "vishwkadu.json"
# filepath = "Json/"+linkedindata
# with open(filepath, 'r') as json_file:
#     profile_data = json.load(json_file)


# gpt_prompt = "Job details: " + str(job_data) + "\n Profile details: " + str(profile_data) + \
#     "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"


# @app.get("/coverletter")
# def index():

#     print(gpt_prompt)
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=gpt_prompt,
#         temperature=0.99,
#         max_tokens=2048,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     print("----------------cover letter----------------------")
#     result = response['choices'][0]['text']
#     print(result)

#     return result


# for kill a port
# sudo kill - 9 `sudo lsof - t - i: 8000`
# http://127.0.0.1:8000

# for run
# uvicorn GPTdemo:app
