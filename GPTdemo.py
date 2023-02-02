from fastapi import FastAPI
import openai
import json
import textwrap
app = FastAPI()

# openai.api_key = "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"
openai.api_key = "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"


# load JSON file
job_filepath = "Json/job_detail/Turing_ML.json"
# job_filepath = "Json/job_detail/Ubar_ML.json"
# job_filepath = "Json/job_detail/Uplers_automation_ML.json"


with open(job_filepath, 'r') as json_file:
    job_data = json.load(json_file)


linkedindata = "hemen.json"
filepath = "Json/New data/"+linkedindata
with open(filepath, 'r') as json_file:
    data = json.load(json_file)


# for skills
skills = ""
for i in range(len(data["data"]["skills"])):
    skills_data = data["data"]["skills"][i]
    if i == 0:
        skills += "\n" + skills_data
    else:
        skills += ", " + skills_data
skills = textwrap.indent(skills, "    ")


# for languages
languages = ""
for i in range(len(data["data"]["languages"])):
    languages_data = data["data"]["languages"][i]
    if i == 0:
        languages += "\n" + languages_data
    else:
        languages += ", " + languages_data

languages = textwrap.indent(languages, "    ")

# for user_experiences
user_experiences = ""

for j in range(len(data["data"]["user_carrier_data"]["user_experiences"])):
    starts_at = data["data"]["user_carrier_data"]["user_experiences"][j]['starts_at']
    ends_at = data["data"]["user_carrier_data"]["user_experiences"][j]['ends_at']
    company = data["data"]["user_carrier_data"]["user_experiences"][j]['company']
    title = data["data"]["user_carrier_data"]["user_experiences"][j]['title']
    description = data["data"]["user_carrier_data"]["user_experiences"][j]['description']
    location = data["data"]["user_carrier_data"]["user_experiences"][j]['location']

    user_experiences_data = "starts at: "+str(starts_at) +\
        ",\n""Ends at: "+str(ends_at) +\
        ",\n""Company: "+str(company) +\
        ",\n""Title: "+str(title) +\
        ",\n""description: "+str(description) +\
        ",\n""location: "+str(location)+".\n"

    # print(user_experiences)
    user_experiences += "\n"+user_experiences_data

user_experiences = textwrap.indent(user_experiences, "    ")

# for usereducation
usereducation = ""

for j in range(len(data["data"]["user_carrier_data"]["usereducation"])):
    starts_at = data["data"]["user_carrier_data"]["usereducation"][j]['starts_at']
    ends_at = data["data"]["user_carrier_data"]["usereducation"][j]['ends_at']
    field_of_study = data["data"]["user_carrier_data"]["usereducation"][j]['field_of_study']
    degree_name = data["data"]["user_carrier_data"]["usereducation"][j]['degree_name']
    school = data["data"]["user_carrier_data"]["usereducation"][j]['school']

    usereducation_data = "Starts at: "+str(starts_at) +\
        ",\nEnds at: "+str(ends_at) +\
        ",\nField of study: "+str(field_of_study) +\
        ",\nDegree name: "+str(degree_name) +\
        ",\nSchool: "+str(school) + ".\n"

    # print(usereducation)
    usereducation += "\n"+usereducation_data

usereducation = textwrap.indent(usereducation, "    ")

# for useraccomplishmentorganisations
useraccomplishmentorganisations = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentorganisations"])):
    org_name = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['org_name']
    title = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['title']
    description = data["data"]["user_carrier_data"]["useraccomplishmentorganisations"][j]['description']

    useraccomplishmentorganisations_data = "Organisation name: "+str(org_name) +\
        ",\nTitle: "+str(title) +\
        ",\nDescription: "+str(description) + ".\n"

    # print(useraccomplishmentorganisations)
    useraccomplishmentorganisations += "\n"+useraccomplishmentorganisations_data

useraccomplishmentorganisations = textwrap.indent(
    useraccomplishmentorganisations, "    ")

# for useraccomplishmentprojects
useraccomplishmentprojects = ""
print(len(data["data"]["user_carrier_data"]["useraccomplishmentprojects"]))
for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentprojects"])):
    title = data["data"]["user_carrier_data"]["useraccomplishmentprojects"][j]['title']
    description = data["data"]["user_carrier_data"]["useraccomplishmentprojects"][j]['description']

    useraccomplishmentprojects_data = "Title: "+str(title) +\
        ",\n""Description: "+str(description) + ".\n"

    useraccomplishmentprojects += "\n"+useraccomplishmentprojects_data


useraccomplishmentprojects = textwrap.indent(
    useraccomplishmentprojects, "    ")

# for uservolunteerwork
uservolunteerwork = ""
for j in range(len(data["data"]["user_carrier_data"]["uservolunteerwork"])):
    starts_at = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['starts_at']
    ends_at = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['ends_at']
    title = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['title']
    description = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['description']
    cause = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['cause']
    company = data["data"]["user_carrier_data"]["uservolunteerwork"][j]['company']

    uservolunteerwork_data = "Starts at: "+str(starts_at) +\
        ",\n""Ends at: "+str(ends_at) +\
        ",\n""Title: "+str(title) +\
        ",\n""Description: "+str(description) +\
        ",\n""Cause: "+str(cause) +\
        ",\n""Company: "+str(company) + ".\n"

    # print(uservolunteerwork)
    uservolunteerwork += "\n"+uservolunteerwork_data

uservolunteerwork = textwrap.indent(
    uservolunteerwork, "    ")

# for usercertifications
usercertifications = ""

for j in range(len(data["data"]["user_carrier_data"]["usercertifications"])):
    starts_at = data["data"]["user_carrier_data"]["usercertifications"][j]['starts_at']
    name = data["data"]["user_carrier_data"]["usercertifications"][j]['name']
    authority = data["data"]["user_carrier_data"]["usercertifications"][j]['authority']

    usercertifications_data = "Starts at: "+str(starts_at) +\
        ",\n""Name: "+str(name) +\
        ",\n""Authority: "+str(authority) + ".\n"

    # print(usercertifications)
    usercertifications += "\n"+usercertifications_data
usercertifications = textwrap.indent(
    usercertifications, "    ")

# for useraccomplishmentpublications
useraccomplishmentpublications = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmentpublications"])):
    name = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['name']
    publisher = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['publisher']
    description = data["data"]["user_carrier_data"]["useraccomplishmentpublications"][j]['description']

    useraccomplishmentpublications_data = "Name: "+str(name) +\
        ",\n""Publisher: "+str(publisher) +\
        ",\n""Description: "+str(description) + ".\n"

    # print(useraccomplishmentpublications)
    useraccomplishmentpublications += "\n"+useraccomplishmentpublications_data
useraccomplishmentpublications = textwrap.indent(
    useraccomplishmentpublications, "    ")

# for useraccomplishmenthonorsawards
useraccomplishmenthonorsawards = ""

for j in range(len(data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"])):
    title = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['title']
    issuer = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['issuer']
    description = data["data"]["user_carrier_data"]["useraccomplishmenthonorsawards"][j]['description']

    useraccomplishmenthonorsawards_data = "Title: "+str(title) +\
        ",\n""Issuer: "+str(issuer) +\
        ",\n""Description: "+str(description) + ".\n"

    # print(useraccomplishmenthonorsawards)
    useraccomplishmenthonorsawards += "\n"+useraccomplishmenthonorsawards_data
useraccomplishmenthonorsawards = textwrap.indent(
    useraccomplishmenthonorsawards, "    ")


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
job_description = textwrap.indent(job_description, "\n    ")
title = job_data["title"]
location = str(job_data["location"]["city"]) + "," + \
    str(job_data["location"]["region"])+"," + \
    str(job_data["location"]["country"])
company = job_data["company"]["name"]
industry = job_data["industry"][0]
employment_type = job_data["employment_type"]
job_functions = job_data["job_functions"][0]

profile_details = "Profile details:\n" \
    "     Name: "+str(First_name) + " "+str(last_name) + "\n"\
    "     Occupation: "+str(Occupation) + "\n"\
    "     Email: "+str(Email) + "\n"\
    "     Summary: "+str(Summary) + "\n"\
    "     Country: "+str(Country_full_name) + "\n"\
    "     City: "+str(City) + "\n"\
    "     State: "+str(state) + "\n"\
    "     Languages: "+str(Languages) + "\n"\
    "     Skills: \n     "+str(skills) + "\n"\
    "     Experiences: \n     "+str(User_experiences) + "\n"\
    "     Education: \n     "+str(User_education) + "\n"\
    "     Accomplishment organisations: \n     "+str(User_accomplishment_organisations) + "\n"\
    "     Projects: \n     "+str(User_accomplishment_projects) + "\n"\
    "     Volunteer work: \n     "+str(User_volunteer_work) + "\n"\
    "     Certifications: \n     "+str(User_certifications) + "\n"\
    "     Publications: \n     "+str(User_accomplishment_publications) + "\n"\
    "     Honors_awards: \n     "+str(User_accomplishment_honors_awards) + "\n"


job_details = "Job details:\n "\
    "     Title: \n          "+str(title) + "\n"\
    "     Compnay name: \n          "+str(company) + "\n"\
    "     Location: \n          "+str(location) + "\n"\
    "     Industry: \n          "+str(industry) + "\n"\
    "     Job description:      "+str(job_description) + "\n"\
    "     Employment type: \n          "+str(employment_type) + "\n"\
    "     Job functions: \n          "+str(job_functions) + "\n"

# cover_letter_format = "Cover letter format:\nplace contact informataion in the header\
#     Show achievements relevant to the role you're targeting.\
#     Target the employer's needs and prove you can help\
#     explain why you want to join and stay"

# cover_letter_format = "Cover letter format:\n\
#     Full name\
#     E-mail\
#     Job title\
#     Company name\
#     include 3-4 paragraphs and add in last Sincerely"
cover_letter_format = "\nCover Letter Format\n    Full name\n    Job title\n    E-mail\
    \n    Recruiter’s Job Title\
    \n    Company Name\
    \n    Opening para: Start cover letter in a way that attracts and holds the reader’s interest.Highlight achievements, display passion and enthusiasm, or drop names  \
    \n    Second Para: Explain them why you are the perfect fit Impress an employer by mentioning my skills/experience/achievements related to new position \
    \n    Closing Para: Show motivation to join the company Show them that you will satisfy their needs and stay with them for longer Close with a promise and \
    \n    Postscript(P.S): Magnet trick you can use to tell something impressive about career, even if it's not related to current job role And say that you'd be happy to provide more info on this if they find it interesting"

# --------------------------start-------------------------------------
# ------final corpus starts-------
# gpt_prompt = job_details + "\n "+profile_details + "\n\nThis is a format of cover letter" + cover_letter_format + "\n " +\
#     "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details using given cover letter format "
# gpt_prompt = cover_letter_format + "\n " + job_details + "\n "+profile_details + "\n" +\
#     "Write a job cover letter using mention cover letter format for provided profile details and job details "
# Compose a cover letter for a job by referencing the given profile information and job details, utilizing the specified cover letter format.
gpt_prompt = "Write a job cover letter using mention cover letter format for provided profile details and job details " + \
    cover_letter_format + "\n " + job_details + "\n "+profile_details + "\n"

print(gpt_prompt)


# ------final corpus ends-----


@app.get("/coverletter")
def index():

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
    # print("----------------cover letter----------------------")
    result = response['choices'][0]['text']
    with open("Json/output/demo.log", "a") as log_file:
        log_file.write("\n\n" + result
                       + "\n------------------------------------------------------------------------------\n")
    return result

# for multiple request

# gpt_prompt1 = job_details + "\n "+profile_details + \
#     "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"
# gpt_prompt2 = job_details + "\n "+profile_details + \
#     "\nWrite a Professional job cover letter for provided profile details and job details"
# gpt_prompt3 = job_details + "\n "+profile_details + \
#     "\nDraft a cover letter that aligns with the job details listed above and emphasizes your relevant skills and experience."
# gpt_prompt4 = job_details + "\n "+profile_details + \
#     "\nWrite a cover letter that illustrates how I abilities align with the job details provided above and why you are a strong candidate for the position for my profile details."
# gpt_prompt5 = job_details + "\n "+profile_details + \
#     "\nCompose a cover letter that highlights My qualifications for the position based on the provided job profile for my profile details."
# gpt_prompt6 = job_details + "\n "+profile_details + \
#     "\nCreate a well-written cover letter that showcases your skills and experience in relation to the given job and profile information."
# gpt_prompt7 = job_details + "\n "+profile_details + \
#     "\nPrepare a cover letter that demonstrates your suitability for the position, using the provided job and profile information as a guide."


# @app.get("/corpus")
# def index():

#     # print(gpt_prompt)
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt1,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response)
#     result = response['choices'][0]['text']
#     # print(result)
#     # print(response['id'])
#     # print(job_details)
#     with open("Json/output/prompt-1.log", "a") as log_file:
#         log_file.write("\n\n" + result
#                        + "\n------------------------------------------------------------------------------\n")

#     response2 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt2,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response2)
#     result2 = response2['choices'][0]['text']
#     # print(result2)
#     # print(response2['id'])
#     # print(job_details)
#     with open("Json/output/prompt-2.log", "a") as log_file:
#         log_file.write("\n\n" + result2
#                        + "\n------------------------------------------------------------------------------\n")

#     response3 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt3,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response3)
#     result3 = response3['choices'][0]['text']
#     # print(result3)
#     # print(response3['id'])
#     # print(job_details)
#     with open("Json/output/prompt-3.log", "a") as log_file:
#         log_file.write("\n\n" + result3
#                        + "\n------------------------------------------------------------------------------\n")

#     response4 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt4,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response4)
#     result4 = response4['choices'][0]['text']
#     # print(result4)
#     # print(response4['id'])
#     # print(job_details)
#     with open("Json/output/prompt-4.log", "a") as log_file:
#         log_file.write("\n\n" + result4
#                        + "\n------------------------------------------------------------------------------\n")

#     response5 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt5,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response5)
#     result5 = response5['choices'][0]['text']
#     # print(result5)
#     # print(response5['id'])
#     # print(job_details)
#     with open("Json/output/prompt-5.log", "a") as log_file:
#         log_file.write("\n\n" + result5
#                        + "\n------------------------------------------------------------------------------\n")

#     response6 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt6,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response6)
#     result6 = response6['choices'][0]['text']
#     # print(result6)
#     # print(response6['id'])
#     # print(job_details)
#     with open("Json/output/prompt-6.log", "a") as log_file:
#         log_file.write("\n\n" + result6
#                        + "\n------------------------------------------------------------------------------\n")

#     response7 = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=gpt_prompt7,
#         temperature=0.99,
#         max_tokens=500,
#         top_p=1.0,
#         frequency_penalty=0.3,
#         presence_penalty=0.9
#     )
#     # print("----------------cover letter----------------------")
#     # print(response7)
#     result7 = response7['choices'][0]['text']
#     # print(result7)
#     # print(response7['id'])
#     # print(job_details)
#     with open("Json/output/prompt-7.log", "a") as log_file:
#         log_file.write("\n\n" + result7
#                        + "\n------------------------------------------------------------------------------\n")

#     return result


# ----------------------------end----------------------------------


# for kill a port
# sudo kill - 9 `sudo lsof - t - i: 8000`
# http://127.0.0.1:8000

# for run
# uvicorn GPTdemo:app
