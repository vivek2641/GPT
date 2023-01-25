from fastapi import FastAPI
import openai
import json
app = FastAPI()

openai.api_key = "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"

# Load json file of job details and linkedin data


job_filepath = "Json/job_detail/Turing_ML.json"
with open(job_filepath, 'r') as json_file:
    job_data = json.load(json_file)

linkedindata = "vivek.json"
filepath = "Json/New data/"+linkedindata
with open(filepath, 'r') as json_file:
    data = json.load(json_file)


# create a string for particular feild


# for skills
skills = ""
for i in range(len(data["data"]["skills"])):
    skills_data = data["data"]["skills"][i]
    if i == 0:
        skills += "    " + skills_data
    else:
        skills += ", " + skills_data

# for languages
languages = ""
for i in range(len(data["data"]["languages"])):
    languages_data = data["data"]["languages"][i]
    if i == 0:
        languages += "    " + languages_data
    else:
        languages += ", " + languages_data

# for user_experiences
user_experiences = ""
for j in range(len(data["data"]["user_carrier_data"]["user_experiences"])):
    if j < 4:
        starts_at = data["data"]["user_carrier_data"]["user_experiences"][j]['starts_at']
        ends_at = data["data"]["user_carrier_data"]["user_experiences"][j]['ends_at']
        company = data["data"]["user_carrier_data"]["user_experiences"][j]['company']
        title = data["data"]["user_carrier_data"]["user_experiences"][j]['title']
        description = data["data"]["user_carrier_data"]["user_experiences"][j]['description']
        location = data["data"]["user_carrier_data"]["user_experiences"][j]['location']

        user_experiences_data = "    starts at: "+str(starts_at) +\
            ",\n""    Ends at: "+str(ends_at) +\
            ",\n""    Company: "+str(company) +\
            ",\n""    Title: "+str(title) +\
            ",\n""    description: "+str(description) +\
            ",\n""    location: "+str(location)+".\n"

        # print(user_experiences)
        user_experiences += "\n"+user_experiences_data

# for usereducation
usereducation = ""

for j in range(len(data["data"]["user_carrier_data"]["usereducation"])):
    if j < 4:
        starts_at = data["data"]["user_carrier_data"]["usereducation"][j]['starts_at']
        ends_at = data["data"]["user_carrier_data"]["usereducation"][j]['ends_at']
        field_of_study = data["data"]["user_carrier_data"]["usereducation"][j]['field_of_study']
        degree_name = data["data"]["user_carrier_data"]["usereducation"][j]['degree_name']
        school = data["data"]["user_carrier_data"]["usereducation"][j]['school']

        usereducation_data = "    Starts at: "+str(starts_at) +\
            ",\n""    Ends at: "+str(ends_at) +\
            ",\n""    Field of study: "+str(field_of_study) +\
            ",\n""    Degree name: "+str(degree_name) +\
            ",\n""    School: "+str(school) + ".\n"

        # print(usereducation)
        usereducation += "\n"+usereducation_data

# for useraccomplishmentorganisations
useraccomplishmentorganisations = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentorganisations"])):
    org_name = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['org_name']
    title = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['title']
    description = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['description']

    useraccomplishmentorganisations_data = "    Organisation name: "+str(org_name) +\
        ",\n""    Title: "+str(title) +\
        ",\n""    Description: "+str(description) + ".\n"

    # print(useraccomplishmentorganisations)
    useraccomplishmentorganisations += "\n"+useraccomplishmentorganisations_data


# for useraccomplishmentprojects
useraccomplishmentprojects = ""
for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentprojects"])):
    title = data["data"]["user_carrier_data"]["useraccomplishmentprojects"][j]['title']
    description = data["data"]["user_carrier_data"]["useraccomplishmentprojects"][j]['description']

    useraccomplishmentprojects_data = "    Title: "+str(title) +\
        ",\n""    Description: "+str(description) + ".\n"

    useraccomplishmentprojects += "\n"+useraccomplishmentprojects_data

# for uservolunteerwork
uservolunteerwork = ""
for j in range(len(data["data"]["user_carrier_data"]["uservolunteerwork"])):
    starts_at = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['starts_at']
    ends_at = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['ends_at']
    title = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['title']
    description = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['description']
    cause = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['cause']
    company = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['company']

    uservolunteerwork_data = "    Starts at: "+str(starts_at) +\
        ",\n""    Ends at: "+str(ends_at) +\
        ",\n""    Title: "+str(title) +\
        ",\n""    Description: "+str(description) +\
        ",\n""    Cause: "+str(cause) +\
        ",\n""    Company: "+str(company) + ".\n"

    # print(uservolunteerwork)
    uservolunteerwork += "\n"+uservolunteerwork_data

    # print(uservolunteerwork)
    uservolunteerwork += "\n"+uservolunteerwork_data

# for usercertifications
usercertifications = ""

for j in range(len(data["data"]["user_carrier_data"]["usercertifications"])):
    if j < 4:
        starts_at = data["data"]["user_carrier_data"]["usercertifications"][j]['starts_at']
        name = data["data"]["user_carrier_data"]["usercertifications"][j]['name']
        authority = data["data"]["user_carrier_data"]["usercertifications"][j]['authority']

        usercertifications_data = "    Starts at: "+str(starts_at) +\
            ",\n""    Name: "+str(name) +\
            ",\n""    Authority: "+str(authority) + ".\n"

        # print(usercertifications)
        usercertifications += "\n"+usercertifications_data

# for useraccomplishmentpublications
useraccomplishmentpublications = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentpublications"])):
    name = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['name']
    publisher = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['publisher']
    description = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['description']

    useraccomplishmentpublications_data = "    Name: "+str(name) +\
        ",\n""    Publisher: "+str(publisher) +\
        ",\n""    Description: "+str(description) + ".\n"

    # print(useraccomplishmentpublications)
    useraccomplishmentpublications += "\n"+useraccomplishmentpublications_data

# for useraccomplishmenthonorsawards
useraccomplishmenthonorsawards = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"])):
    if j < 4:
        title = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['title']
        issuer = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['issuer']
        description = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['description']

        useraccomplishmenthonorsawards_data = "    title: "+str(title) +\
            ",\n""    issuer: "+str(issuer) +\
            ",\n""    Description: "+str(description) + ".\n"

        # print(useraccomplishmenthonorsawards)
        useraccomplishmenthonorsawards += "\n"+useraccomplishmenthonorsawards_data


# define all the variables

First_name = str(data["data"]["first_name"])
last_name = data["data"]["last_name"]
Occupation = data["data"]["occupation"]
Email = data["data"]["email"]
Summary = data["data"]["summary"]
Country_full_name = data["data"]["country_full_name"]
City = data["data"]["city"]
state = data["data"]["state"]
# Languages = data["data"]["languages"]
Languages = languages
# skills = data["data"]["skills"]
skills = skills

# User_experiences = data["data"]["user_carrier_data"]["user_experiences"]
User_experiences = user_experiences

# User_education = data["data"]["user_carrier_data"]["usereducation"]
User_education = usereducation

# User_accomplishment_organisations = data["data"][
# "user_carrier_data"]["useraccomplishmentorganisations"]
User_accomplishment_organisations = useraccomplishmentorganisations

# User_accomplishment_projects = data["data"]["user_carrier_data"]["useraccomplishmentprojects"]
User_accomplishment_projects = useraccomplishmentprojects

# User_volunteer_work = User_certifications = data[
#     "data"]["user_carrier_data"]["uservolunteerwork"]
User_volunteer_work = uservolunteerwork

# User_certifications = data["data"]["user_carrier_data"]["usercertifications"]
User_certifications = usercertifications

# User_accomplishment_publications = data["data"][
#     "user_carrier_data"]["useraccomplishmentpublications"]
User_accomplishment_publications = useraccomplishmentpublications

# User_accomplishment_honors_awards = data["data"][
#     "user_carrier_data"]["useraccomplishmenthonorsawards"]
User_accomplishment_honors_awards = useraccomplishmenthonorsawards


job_description = job_data["job_description"]

title = job_data["title"]
location = str(job_data["location"]["city"]) + "," + \
    str(job_data["location"]["region"])+"," + \
    str(job_data["location"]["country"])
company = job_data["company"]["name"]
industry = job_data["industry"][0]
employment_type = job_data["employment_type"]
job_functions = job_data["job_functions"][0]


# create Prompt for profile data
profile_details = "Profile details:\n" \
    "Name: "+str(First_name) + " "+str(last_name) + "\n"\
    "Occupation: "+str(Occupation) + "\n"\
    "Email: "+str(Email) + "\n"\
    "Summary: "+str(Summary) + "\n"\
    "Country: "+str(Country_full_name) + "\n"\
    "City: "+str(City) + "\n"\
    "state: "+str(state) + "\n"\
    "Languages: "+str(Languages) + "\n"\
    "skills: "+str(skills) + "\n"\
    "experiences: "+str(User_experiences) + "\n"\
    "education: "+str(User_education) + "\n"\
    "accomplishment_organisations: "+str(User_accomplishment_organisations) + "\n"\
    "projects: "+str(User_accomplishment_projects) + "\n"\
    "Volunteer work: "+str(User_volunteer_work) + "\n"\
    "certifications: "+str(User_certifications) + "\n"\
    "publications: "+str(User_accomplishment_publications) + "\n"\
    "honors_awards: "+str(User_accomplishment_honors_awards) + "\n"

# create Prompt for job data
job_details = "Job details:\n "\
    "    Title: "+str(title) + "\n"\
    "    Company name: "+str(company) + "\n"\
    "    Location: "+str(location) + "\n"\
    "    Industry: "+str(industry) + "\n"\
    "    Job description: "+str(job_description) + "\n"\
    "    Employment type: "+str(employment_type) + "\n"\
    "    Job functions: "+str(job_functions) + "\n"


# --------------------------start-------------------------------------
# ------final corpus starts-------
prompt = job_details + "\n "+profile_details + \
    "\nWrite a professional job cover letter for provided profile details if job application is done for the above mention job details with cover letter format"
gpt_prompt = prompt
# ------final corpus ends-----


@app.get("/coverletter")
def index():

    # print(gpt_prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.99,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9,
        stop=["Job details:", "Profile details:"]
    )
    print("----------------cover letter----------------------")
    # print(response)
    result = response['choices'][0]['text']
    print(result)
    # print(response['id'])
    # print(job_details)
    with open("Json/output/demo.log", "a") as log_file:
        log_file.write(gpt_prompt + "\n\n" + result
                       + "\n------------------------------------------------------------------------------\n")

    return result

# ----------------------------end----------------------------------


# for kill a port http://127.0.0.1:8000
# sudo kill - 9 `sudo lsof - t - i: 8000`


# for run
# uvicorn GPTdemo:app
