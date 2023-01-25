from fastapi import FastAPI
import openai
import json
app = FastAPI()

openai.api_key = "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"


job_filepath = "Json/job_detail/Turing_ML.json"
with open(job_filepath, 'r') as json_file:
    job_data = json.load(json_file)

linkedindata = "linkedindatafinal.json"
filepath = "Json/New data/"+linkedindata
with open(filepath, 'r') as json_file:
    data = json.load(json_file)


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

        usereducation_data = \
            "    Field of study: "+str(field_of_study) +\
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

    uservolunteerwork_data =\
        "    Title: "+str(title) +\
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

        usercertifications_data = \
            "    Name: "+str(name) +\
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


job_details = "Job details:\n "\
    "    Title: "+str(title) + "\n"\
    "    Company name: "+str(company) + "\n"\
    "    Location: "+str(location) + "\n"\
    "    Industry: "+str(industry) + "\n"\
    "    Job description: "+str(job_description) + "\n"\
    "    Employment type: "+str(employment_type) + "\n"\
    "    Job functions: "+str(job_functions) + "\n"
# print(job_details)


# --------------------------start-------------------------------------
# ------final corpus starts-------
prompt = job_details + "\n "+profile_details + \
    "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"
gpt_prompt = prompt
# ------final corpus ends-----

# gpt_prompt = "Create a cover letter which contains not more than 3 paragraphas and which contain experience,projects and volunteer work " + \
# gpt_prompt = "Create a cover letter which contains experience,projects and volunteer information in different paragraph\n" + \
#     "experience:" + str(User_experiences) + ",\n projects:" + str(User_accomplishment_projects) + \
#     ",\n volunteer works:"+str(User_volunteer_work)+"."


# prompt = job_details + " this is a job details. wait for my secound request"

# secound_prompt = profile_details + \
#     " this is a profile details. wait for my next request"
# third_prompt = job_details + \
#     " this is a job details. wait for my next request"
# forth_prompt = "Can You create a cover letter for maction above profile details and job det"

# prompt = "so can you Write a job cover letter for provided profile details if job application is done for the above mention job details."
# gpt_prompt = "I have to create a cover letter for me so can you wait for my secound request"

# gpt_prompt = '''Profile details: Name: ????????‍???? Progyan Bhattacharya Occupation: Senior Software Engineer Interview Kickstart Email: vishw@htree.plus Summary: Stack Web Application Developer Specialisation React/Node & Docker Vocal Hexagonal Architecture | TDD Practice Code Quality Coding Country: India City: Greater Bengaluru Area state: West Bengal Languages: Bengali, English, Hindi skills: agile methodologies, ajax, algorithm design, artificial intelligence, neural networks, business strategy, core java, css, css3, data science, structures, design patterns, event management, facebook api, open graph protocols, gamification, html, html 5, html5, j2se, javascript, jquery, json, linux, machine learning, magento, marketing mysql, natural language processing, node.js, parallax, php, poetry, product programming, python, risk semantic web, seo, software development, start venture web applications, services, zend framework experiences: starts_at: 2021-10-01T00:00:00Z, ends_at: None, company: Kickstart, title: Engineer, description: - Actively Hiring Building Frontend Team ground-up. Creating culture Platform-first Development Experience Product-led Growth initiatives. Mentoring Fresh Talents Onboarding Development. Managing Lifecycle, Architecture, Infrastructure scale Cross-team communication Team., location: Remote. 2019-01-01T00:00:00Z, 2021-09-30T00:00:00Z, HackerRank, II, Built source solution @hackerrank/firepad collaborative text editing Monaco editor. library powers editors IDE platform. Designed architecture led development effort building virtual onsite experience post-Covid Remote setups. Interactive Playback reporting user interactions activities platform interview process evaluation purposes. Conducting interviews SDE II SSE roles upscale Engineering team continue solving complex problems come. Open Source tool extract Type module improve developer consumer applications. Continious improvement application performance quality experience., Area, India. 2018-09-01T00:00:00Z, 2018-12-31T00:00:00Z, Chatbot Job Cirkit, Lead hiring scratch create easy manager blue-collar job track performance. Was built multiple users high level flexibility UI. Using practices method software. Used Technologies: React, Redux, Material Design, RSA Encryption, Kolkata 2018-05-01T00:00:00Z, 2018-05-31T00:00:00Z, Apexcedo, Developer, official site consultation service study. Design principles grid layout UX based jQuery/Ajax., 2018-02-01T00:00:00Z, 2018-06-30T00:00:00Z, Tech-Mantra, Project Supervisor, Supervisor maintainer organization. working on-line smart Molan aimed students developers., Bengal, 2017-07-01T00:00:00Z, 2017-09-30T00:00:00Z, RegOpz Pvt. Ltd., * Worked cloud multi-tenant brings ease monetary information/regulation bank systems. component-driven Reactive interface React/Redux Bootstrap Implemented role functionality accessibility maker-checker update. Manage monitor flow common RESTful API Flask-Python utilizes multi-threading Dataframes. Redesigned SQL Database structured distributed clusters., Easy Daftar, Karunamoyee, Salt Lake, Kolkata. 2017-02-01T00:00:00Z, 2019-06-30T00:00:00Z, Bytes Club, Co-Founder, Co-founder Technical Club University Technology knowledge products domain including Development, Source, Internet Machine Learning, Competitive Programming etc., Technology. 2016-01-01T00:00:00Z, 2016-02-29T00:00:00Z, Ocaision, UI LAMP website., Sector Lake. education: 2015-01-01T00:00:00Z, 2019-12-31T00:00:00Z, field_of_study: Technology, degree_name: Engineer’s Degree, school: 2007-01-01T00:00:00Z, 2015-12-31T00:00:00Z, Science, Higher Secondary, Birati High School. accomplishment_organisations: Organisation Title: Co-founder, Description: None. projects: Operational Transformations, collection Synchronisation Algorithm Adapters Transformation. storybook-addon-sass-postcss, Storybook plugin/addon incorporates loaders External Stylesheets SASS Language Support CSS Modules proper Post processing support browser vendor platforms.. babel-plugin-flow-generate-typedef, Babel Plugin Generate Library Definition Libraries Modules.. MIPS Simulator, micro assembler interpreter written Assembly education purpose. Modular compiler easily manageable, expandable portable. standards MIPS-IV. Current Development: memory allocation.. ServerX, Open-source HTTP/HTTPS Server Handler Socket parallel Data Processing (MIMD) capabilities. Extensive dynamic allocation. Cross-platform compatible IO. Keep-Alive Connections.. Volunteer work: Starts_at: Ends_at: Coach, Helping people Pro-bono Mental Health, Career, Resume Preparation. Follow: #TheProDev, Cause: Social_services, Company: Pro Dev. 2022-02-01T00:00:00Z, Community Builder, Education, Amazon Services (AWS). certifications: 2020-04-01T00:00:00Z, name: Started Google Kubernetes Engine, authority: Google. 2019-10-01T00:00:00Z, Certified ScrumMaster (CSM), Scrum Alliance. 2016-06-01T00:00:00Z, CS50 : edX Honor Certificate Introduction edX. C#, 2015-11-01T00:00:00Z, Bootstrap, Verified Science Python, publications: Optimise Image Builds Gitlab C, publisher: AWS Service enact transactions persistent layers choices services databases, TypeScript way.. Bulding Scalable Modern Microservices World, Level Git Connected, Defining single Lexical Scoping Closure ES5 Container Module Pattern (Inversion Control) maintain dependencies modules.. Evolution JavaScript Dependency Injection, Plain Adapter creates contract plugs sockets adapter mediator.. Pattern: Create Many, Repository perfect place Domain logic Models Enitity Definition.. Layer, Startup, Explanation Hexaginal Princeples Driven Ecosystem React framework.. quirky caching FS speed CI build time.. honors_awards: Hacktoberfest 2019, issuer: DigitalOcean, Hactoberfest 2018, 2017, Contributing community GitHub. Services, 2020, DigitalOcean Inc., Write cover letter for above profile details and job details'''
# gpt_prompt = '''Job details: Title: Remote Machine Learning Engineer Jobs Compnay Turing Location: None,None,India Industry: ['Software Development'] description: emerging edtech startup building initial team talented individuals Engineer. engineer actively contributing developing adaptive testing solution employs machine learning education space. company raised pre-seed fund aims implement Adaptive exciting opportunity work fast-paced customer-first environment. requires overlap PST. **Job Responsibilities:** * Assist back-end infrastructure, data pipelines, models AI-backed products Experiment techniques create test program features extending improving existing frameworks libraries Work engineers model embed AI analytics business decision processes Integrate end-users experiments tests, perform statistical analysis, interpret tuning scaling Requirements:** Bachelor's/Master's degree Engineering, Science equivalent experience) 3+ years relevant experience hands-on Systems versed and/or MERN stacks Expertise Artificial Intelligence Experience science projects psychometrics required excellent communication skills proficiency English Employment type: Full-time functions: Engineering Technology Profile Name: Hemen Ashodia Occupation: Founder / Chief Scientist F(x) Data Labs PVT LTD Email: hemen@htree.plus Summary: invent. Country: India City: Ahmedabad state: Gujarat Languages: English, Gujarati, Hindi skills: agile methodologies, ajax, algorithm design, artificial intelligence, neural networks, strategy, core java, css, css3, science, structures, design patterns, event management, facebook api, open graph protocols, gamification, html, html 5, html5, j2se, javascript, jquery, json, linux, learning, magento, marketing mysql, natural language processing, node.js, parallax, php, poetry, product programming, python, risk semantic web, seo, software development, start venture web applications, services, zend framework experiences: starts 2018-11-01T00:00:00Z, Ends None, Company: Medlex.ai, Developer, location: None. 2015-03-01T00:00:00Z, 2015-07-31T00:00:00Z, Zidisha, Officer, Zidisha online microlending community connects lenders borrowers — matter distance disparity them. More 200,000 people worldwide started Zidisha., Area, India. 2013-05-01T00:00:00Z, 2015-02-28T00:00:00Z, Remarkin.com, CEO, Remarkin.com start-up easy, engaging creative., Ahmedabad. 2013-03-01T00:00:00Z, Venture Design Fellow, Studio, Studio methodology based conducted field engineering innovation. University Collaboration Center Stanford University, 2012-07-01T00:00:00Z, 2013-04-30T00:00:00Z, Aspire Institute, Trainer/ faculty, Coaching Advance development PHP, 2012-10-31T00:00:00Z, Vox Populi Club, Tech-Event Manager, VP-club club L.D. College that organizes events Engineers Beating ..:), 2012-01-01T00:00:00Z, 2012-12-31T00:00:00Z, Magazine, Techtonic, Working tech department Vox-Populi Magazine., 2012-11-30T00:00:00Z, Manager Technical Events, Event manger Club In LD Ahmedabad, 2011-08-01T00:00:00Z, 2012-04-30T00:00:00Z, Topupchat.com, CEO/founder, CEO invent feature website topupchat.com, the entire idea, code designed invented me, 2018-03-01T00:00:00Z, 2019-12-31T00:00:00Z, ArtuData, Scientist, 80% profit generated 2% visitors ArtuData empowers sales teams identify leads real-time, focus convert paying customers. boost efficiency ROI reducing cost acquisition., 2018-01-01T00:00:00Z, 2018-12-31T00:00:00Z, Johnson & Johnson, Lead Expert, Worked Expert - Science. Created millions points, identification strategies increase effectiveness professional educational events., Loom Network, Built Karma decentralized crypto platform implemented Sparse Merkle Tree., Paravision, TensorFlow Invented fastest correct face 99.81% accuracy., 2015-08-01T00:00:00Z, LTD, Labs, working called h+tree increases speed limit databases serves number users time. tree capable deliver 300% compared B+Tree. servers exceptionally fast server eventually. The goal setting cloud infrastructure inject h+Tree delivering industry!, 2012-05-01T00:00:00Z, 2012-07-31T00:00:00Z, Amitech, Web Facebook Application Developer Firefox Extension Amitech. Amitech Ahmedabad., education: Starts 2013-01-01T00:00:00Z, 2015-12-31T00:00:00Z, Field study: Entrepreneurship Thinking, Degree Fellowship, School: VentureStudio Partnered California. 2010-01-01T00:00:00Z, 2014-12-31T00:00:00Z, IT, BE, L.D 2003-01-01T00:00:00Z, 2010-12-31T00:00:00Z, Science, 12th, High School, Bhuj-Kutch. accomplishment_organisations: projects: Topupchat.com(Free Recharge), Description: Chat fiends free Mobile Recharge. Net Meeting, portal easy virtual meeting.. ICATES2013, responsive International Conference Advances Tribology Systems. MN Framework, extremely robust highly distributed PHP projects. Helpful beginners intermediates experts. LGD Library, Layered image processing library PHP. Famous, app update fb status stylish way. PicInChat.com, upload Send pic friends chat big smiles. Debate, Debate war words An debate. Volunteer work: certifications: publications: Fx Optimiser upto faster Neural Network Training, Publisher: OpenReview, successor Adam Optimiser. It observed throuput Training. honors_awards: title: Leadership Excellence Award, issuer: Technological Gujarat, India, Create a cover letter which contains experience,projects and volunteer infomration in different paragraph\n'''
# gpt_prompt = "Job details: Title: Remote Machine Learning Engineer Jobs Compnay Turing Location: None,None,India Industry: Software Development description: emerging edtech startup building initial team talented individuals Engineer. engineer actively contributing developing adaptive testing solution employs machine learning education space. company raised pre-seed fund aims implement Adaptive exciting opportunity work fast-paced customer-first environment. requires overlap PST. **Job Responsibilities:** * Assist back-end infrastructure, data pipelines, models AI-backed products Experiment techniques create test program features extending improving existing frameworks libraries Work engineers model embed AI analytics business decision processes Integrate end-users experiments tests, perform statistical analysis, interpret tuning scaling Requirements:** Bachelor's/Master's degree Engineering, Science equivalent experience) 3+ years relevant experience hands-on Systems versed and/or MERN stacks Expertise Artificial Intelligence Experience science projects psychometrics required excellent communication skills proficiency English Employment type: Full-time functions: Engineering Technology Profile Hemen Ashodia Occupation: Founder / Chief Scientist F(x) Data Labs PVT Email: hemen@htree.plus Summary: invent. Country: India City: Ahmedabad Gujarat Languages: English, Gujarati, Hindi skills: agile methodologies, ajax, algorithm design, artificial intelligence, neural networks, strategy, core java, css, css3, science, structures, design patterns, event management, facebook api, open graph protocols, gamification, html, html 5, html5, j2se, javascript, jquery, json, linux, learning, magento, marketing mysql, natural language processing, node.js, parallax, php, poetry, product programming, python, risk semantic web, seo, software development, start venture web applications, services, zend framework experiences: starts 2018-11-01T00:00:00Z, Ends Company: Medlex.ai, Developer, location: 2015-03-01T00:00:00Z, 2015-07-31T00:00:00Z, Zidisha, Officer, Zidisha online microlending community connects lenders borrowers — matter distance disparity 200,000 people worldwide started Zidisha., Area, India. 2013-05-01T00:00:00Z, 2015-02-28T00:00:00Z, Remarkin.com, CEO, Remarkin.com start-up easy, engaging creative., Ahmedabad. 2013-03-01T00:00:00Z, Venture Design Fellow, Studio, Studio methodology based conducted field engineering innovation. University Collaboration Center Stanford University, 2012-07-01T00:00:00Z, 2013-04-30T00:00:00Z, Aspire Institute, Trainer/ faculty, Coaching Advance development PHP, 2012-10-31T00:00:00Z, Vox Populi Club, Tech-Event Manager, VP-club club L.D. College organizes events Engineers Beating ..:), 2012-01-01T00:00:00Z, 2012-12-31T00:00:00Z, Magazine, Techtonic, Working tech department Vox-Populi Magazine., 2012-11-30T00:00:00Z, Manager Technical Events, Event manger Club LD Ahmedabad, 2011-08-01T00:00:00Z, 2012-04-30T00:00:00Z, Topupchat.com, CEO/founder, CEO invent feature website topupchat.com, entire idea, code designed invented 2018-03-01T00:00:00Z, 2019-12-31T00:00:00Z, ArtuData, Scientist, 80% profit generated 2% visitors ArtuData empowers sales teams identify leads real-time, focus convert paying customers. boost efficiency ROI reducing cost acquisition., 2018-01-01T00:00:00Z, 2018-12-31T00:00:00Z, Johnson & Johnson, Lead Expert, Worked Expert - Science. Created millions points, identification strategies increase effectiveness professional educational events., Loom Network, Built Karma decentralized crypto platform implemented Sparse Merkle Tree., Paravision, TensorFlow Invented fastest correct face 99.81% accuracy., 2015-08-01T00:00:00Z, Labs, working called h+tree increases speed limit databases serves number users time. tree capable deliver 300% compared B+Tree. servers exceptionally fast server eventually. goal setting cloud infrastructure inject h+Tree delivering industry!, 2012-05-01T00:00:00Z, 2012-07-31T00:00:00Z, Amitech, Web Facebook Application Developer Firefox Extension Amitech. Amitech Ahmedabad., education: Starts 2013-01-01T00:00:00Z, 2015-12-31T00:00:00Z, Field study: Entrepreneurship Thinking, Degree Fellowship, School: VentureStudio Partnered California. 2010-01-01T00:00:00Z, 2014-12-31T00:00:00Z, L.D 2003-01-01T00:00:00Z, 2010-12-31T00:00:00Z, Science, 12th, High School, Bhuj-Kutch. accomplishment_organisations: projects: Topupchat.com(Free Recharge), Description: Chat fiends free Mobile Recharge. Net Meeting, portal easy virtual meeting.. ICATES2013, responsive International Conference Advances Tribology Systems. MN Framework, extremely robust highly distributed PHP projects. Helpful beginners intermediates experts. LGD Library, Layered image processing library PHP. Famous, app update fb status stylish PicInChat.com, upload Send pic friends chat big smiles. Debate, Debate war debate. Volunteer work: certifications: publications: Fx Optimiser upto faster Neural Network Training, Publisher: OpenReview, successor Adam Optimiser. observed throuput Training. honors_awards: title: Leadership Excellence Award, issuer: Technological Gujarat, India, Write a job professional cover letter for provided profile details if job application is done for the above mention job details"
# gpt_prompt = ''''''

# WorldOfAwesomeness?** **Hit Apply button!** Employment type: functions: Engineering Technology Profile Name: ????????‍???? Progyan Bhattacharya Occupation: Senior Software Interview Kickstart Email: vishw@htree.plus Summary: Web Application Specialisation React/Node & Docker Vocal Hexagonal Architecture | TDD Practice Quality Coding Country: India City: Greater Bengaluru Area state: West Bengal Languages: Bengali, English, Hindi skills: agile methodologies, ajax, algorithm artificial intelligence, neural networks, business strategy, core java, css, css3, science, structures, event facebook api, open graph protocols, gamification, html, html 5, html5, j2se, javascript, jquery, json, linux, machine learning, magento, marketing mysql, natural language processing, node.js, parallax, php, poetry, programming, python, risk semantic web, seo, development, start venture web applications, services, zend framework experiences: starts 2021-10-01T00:00:00Z, Ends None, Company: Kickstart, Engineer, Actively Hiring Building Frontend Team ground-up. Creating culture Platform-first Development Product-led Growth initiatives. Mentoring Fresh Talents Onboarding Development. Managing Lifecycle, Architecture, Infrastructure Cross-team Team., location: Remote. 2019-01-01T00:00:00Z, 2021-09-30T00:00:00Z, HackerRank, II, Built source solution @hackerrank/firepad collaborative text editing Monaco editor. library powers editors IDE platform. Designed led effort building virtual onsite post-Covid Remote setups. Interactive Playback reporting user interactions activities interview evaluation purposes. Conducting interviews SDE II SSE roles upscale continue complex come. Open Source tool extract Type module developer consumer applications. Continious improvement experience., Area, India. 2018-09-01T00:00:00Z, 2018-12-31T00:00:00Z, Chatbot Cirkit, Lead hiring scratch easy manager blue-collar job track performance. Was built multiple users level flexibility UI. Using practices method software. Used Technologies: React, Redux, Material Design, RSA Encryption, Kolkata 2018-05-01T00:00:00Z, 2018-05-31T00:00:00Z, Apexcedo, Developer, official site consultation service study. principles grid layout UX based jQuery/Ajax., 2018-02-01T00:00:00Z, 2018-06-30T00:00:00Z, Tech-Mantra, Project Supervisor, Supervisor maintainer organization. on-line smart Molan aimed students developers., Bengal, 2017-07-01T00:00:00Z, 2017-09-30T00:00:00Z, RegOpz Pvt. Ltd., Worked cloud multi-tenant ease monetary information/regulation bank systems. component-driven Reactive interface React/Redux Bootstrap Implemented role functionality accessibility maker-checker update. Manage monitor flow common RESTful API Flask-Python utilizes multi-threading Dataframes. Redesigned Database structured clusters., Easy Daftar, Karunamoyee, Salt Lake, Kolkata. 2017-02-01T00:00:00Z, 2019-06-30T00:00:00Z, Bytes Club, Co-Founder, Co-founder Technical Club University domain Development, Source, Internet Learning, Competitive Programming etc., Technology. 2016-01-01T00:00:00Z, 2016-02-29T00:00:00Z, Ocaision, UI LAMP website., Sector Lake. 2018-06-01T00:00:00Z, 2018-08-31T00:00:00Z, Globe (ATG), • fluid handling jQuery. Core mechanism notification mailing maintainable trait. administrator user. Improved security application, Mesh Education Inc., generation teaching deployed Electron Desktop. features caching, auto-updating offline improved existing React jQuery/NodeJS. Performed creating asynchronous request Axios resolving promises Redux-promise middleware. UI/UX binding WebSocket Channels serivce. Data (structured/unstructured) collection monitoring deep learning purpose visualizing output. Green Sock Animation Plugin Transition user-friendly Semantic Framework., education: Starts 2015-01-01T00:00:00Z, 2019-12-31T00:00:00Z, Field study: Technology, Degree Engineer’s Degree, School: 2007-01-01T00:00:00Z, 2015-12-31T00:00:00Z, Science, Secondary, Birati High School. accomplishment_organisations: Organisation Co-founder, Description: None. projects: Operational Transformations, Synchronisation Algorithm Adapters Transformation. storybook-addon-sass-postcss, Storybook plugin/addon incorporates loaders External Stylesheets SASS Language Support CSS Modules proper Post processing browser vendor platforms.. babel-plugin-flow-generate-typedef, Babel Generate Library Definition Libraries Modules.. MIPS Simulator, micro assembler interpreter Assembly education purpose. Modular compiler easily manageable, expandable portable. MIPS-IV. Current Development: memory allocation.. ServerX, Open-source HTTP/HTTPS Server Handler Socket parallel Processing (MIMD) capabilities. Extensive dynamic allocation. Cross-platform compatible IO. Keep-Alive Connections.. Volunteer work: Coach, people Pro-bono Mental Health, Career, Resume Preparation. Follow: #TheProDev, Social_services, Pro Dev. 2022-02-01T00:00:00Z, Community Builder, Education, Amazon (AWS). certifications: 2020-04-01T00:00:00Z, Started Google Engine, Authority: Google. 2019-10-01T00:00:00Z, ScrumMaster (CSM), Scrum Alliance. 2016-06-01T00:00:00Z, CS50 : edX Honor Certificate Introduction edX. C#, 2015-11-01T00:00:00Z, Bootstrap, Verified Science publications: Optimise Image Builds Gitlab C, Publisher: AWS Service enact transactions persistent layers choices services TypeScript way.. Bulding Scalable Modern Microservices World, Level Git Connected, Defining single Lexical Scoping Closure ES5 Container Module Pattern (Inversion Control) dependencies modules.. Evolution JavaScript Dependency Injection, Plain Adapter creates plugs sockets adapter mediator.. Pattern: Many, Repository Domain logic Models Enitity Definition.. Layer, Startup, Explanation Hexaginal Princeples Driven Ecosystem framework.. quirky caching FS speed CI build time.. honors_awards: title: Hacktoberfest 2019, issuer: DigitalOcean, Hactoberfest 2018, 2017, Contributing community GitHub. Services, 2020, DigitalOcean Write cover letter profile details mention
# gpt_prompt = "Job details: Title: Stack - Developer Compnay Uplers Location: Mumbai,Maharashtra,India Industry: Services Consulting description: **Experience: 5+ Years** **Profile: Engineer** **Location: Remote** **Pay: $2600 (USD)** **Shift Time: IST Shift ( 9:30 6:30 PM)** **What Talent Network?** Network place talents meet opportunities. platform candidate perfect opportunity work global companies contractual basis. talent network Indian benefit gain access career exposure. With you'll support, guidance, opportunities level. ready embark journey challenge, engine! **Contractual Position** A position requires sign agree terms contract working. structure offer variety commitments refine established skills create ones. **Uplers brings positions benefits like:** ✔ Higher pay industry standards Full-time Ability short period Control **Perks joining Network:** * **Talent Success Coach:** connected dedicated coach guide assignments clients. **Payout:** paid currencies earn standards. **Opportunity:** Work international exposure exciting projects. **Mobility:** comfort living room couch breezy beach. **How 1. step, register portal 2. Clear decks application form 3. Gear clear 3-stage assessment process 4. Certified **Full Engineer Responsibilities** Architect, design, implement, maintain high-performance, scalable systems on-premise Cloud Engage customers, product management, marketing, operations support engineers products conception development production maintenance Code Java, Python, Shell script and/or C++/C Design develop software SpringBoot, Angular, microservices, SQL NoSQL databases Deploy code production, debug fixe issues proposals, architecture, projects, designs, competitive analysis, technology case studies, escalation post mortem, executive staff Execute projects entirety feature specification, implementation validation Document specifications, bug updates Create plan verifiable milestones time estimates deliver Constructively collaborate team requirements gathering, design reviews Participate QA effective test plans, automated cases, rigorous testing Benchmark performance, identify bottlenecks, troubleshoot improve performance Handle customer escalations Qualifications** BS MS science field 3+ years relevant experience Experience developing Enterprise quality Strong programming Linux environment scripting, C knowledge object oriented principles, architectural patterns, databases, operating systems, engineering Good understanding on-disk in-memory data structures algorithms emphasis scalability REST APIs microservice architecture effectively fellow members written verbal communication Stand Out** based, hybrid SaaS, PaaS Iaas Spring Boot, frameworks AWS, Azure, GCP, S3, technologies infrastructure Containers, Docker, Kubernetes Postgres relational database concepts including multithreading concurrent clustering high availability, distributed storage backup, replication, disaster recovery, storage, NAS, NFS networking, orchestration large scale management Artificial Intelligence (AI) / Machine Learning robotics, warehouse (WMS) message queuing workflow motivated managed enjoy working positive attitude technical competence Pragmatic approach solving problems collaboration Open-minded, passionate, ideological Biased automation ensuring works Team-first helping succeed **Uplift Uplers** believes connecting people. people-first organization, constantly strives individuals won't break ground. Helping doesn't surprise growing popular industry. **All set enter #WorldOfAwesomeness?** **Hit Apply button!** Employment type: functions: Engineering Technology Profile Name: ????????‍???? Progyan Bhattacharya Occupation: Senior Software Interview Kickstart Email: vishw@htree.plus Summary: Web Application Specialisation React/Node & Docker Vocal Hexagonal Architecture | TDD Practice Quality Coding Country: India City: Greater Bengaluru Area state: West Bengal Languages: Bengali, English, Hindi skills: agile methodologies, ajax, algorithm artificial intelligence, neural networks, business strategy, core java, css, css3, science, structures, event facebook api, open graph protocols, gamification, html, html 5, html5, j2se, javascript, jquery, json, linux, machine learning, magento, marketing mysql, natural language processing, node.js, parallax, php, poetry, programming, python, risk semantic web, seo, development, start venture web applications, services, zend framework experiences: starts 2021-10-01T00:00:00Z, Ends None, Company: Kickstart, Engineer, Actively Hiring Building Frontend Team ground-up. Creating culture Platform-first Development Product-led Growth initiatives. Mentoring Fresh Talents Onboarding Development. Managing Lifecycle, Architecture, Infrastructure Cross-team Team., location: Remote. 2019-01-01T00:00:00Z, 2021-09-30T00:00:00Z, HackerRank, II, Built source solution @hackerrank/firepad collaborative text editing Monaco editor. library powers editors IDE platform. Designed led effort building virtual onsite post-Covid Remote setups. Interactive Playback reporting user interactions activities interview evaluation purposes. Conducting interviews SDE II SSE roles upscale continue complex come. Open Source tool extract Type module developer consumer applications. Continious improvement experience., Area, India. 2018-09-01T00:00:00Z, 2018-12-31T00:00:00Z, Chatbot Cirkit, Lead hiring scratch easy manager blue-collar job track performance. Was built multiple users level flexibility UI. Using practices method software. Used Technologies: React, Redux, Material Design, RSA Encryption, Kolkata 2018-05-01T00:00:00Z, 2018-05-31T00:00:00Z, Apexcedo, Developer, official site consultation service study. principles grid layout UX based jQuery/Ajax., 2018-02-01T00:00:00Z, 2018-06-30T00:00:00Z, Tech-Mantra, Project Supervisor, Supervisor maintainer organization. on-line smart Molan aimed students developers., Bengal, 2017-07-01T00:00:00Z, 2017-09-30T00:00:00Z, RegOpz Pvt. Ltd., Worked cloud multi-tenant ease monetary information/regulation bank systems. component-driven Reactive interface React/Redux Bootstrap Implemented role functionality accessibility maker-checker update. Manage monitor flow common RESTful API Flask-Python utilizes multi-threading Dataframes. Redesigned Database structured clusters., Easy Daftar, Karunamoyee, Salt Lake, Kolkata. 2017-02-01T00:00:00Z, 2019-06-30T00:00:00Z, Bytes Club, Co-Founder, Co-founder Technical Club University domain Development, Source, Internet Learning, Competitive Programming etc., Technology. 2016-01-01T00:00:00Z, 2016-02-29T00:00:00Z, Ocaision, UI LAMP website., Sector Lake. 2018-06-01T00:00:00Z, 2018-08-31T00:00:00Z, Globe (ATG), • fluid handling jQuery. Core mechanism notification mailing maintainable trait. administrator user. Improved security application, Mesh Education Inc., generation teaching deployed Electron Desktop. features caching, auto-updating offline improved existing React jQuery/NodeJS. Performed creating asynchronous request Axios resolving promises Redux-promise middleware. UI/UX binding WebSocket Channels serivce. Data (structured/unstructured) collection monitoring deep learning purpose visualizing output. Green Sock Animation Plugin Transition user-friendly Semantic Framework., education: Starts 2015-01-01T00:00:00Z, 2019-12-31T00:00:00Z, Field study: Technology, Degree Engineer’s Degree, School: 2007-01-01T00:00:00Z, 2015-12-31T00:00:00Z, Science, Secondary, Birati High School. accomplishment_organisations: Organisation Co-founder, Description: None. projects: Operational Transformations, Synchronisation Algorithm Adapters Transformation. storybook-addon-sass-postcss, Storybook plugin/addon incorporates loaders External Stylesheets SASS Language Support CSS Modules proper Post processing browser vendor platforms.. babel-plugin-flow-generate-typedef, Babel Generate Library Definition Libraries Modules.. MIPS Simulator, micro assembler interpreter Assembly education purpose. Modular compiler easily manageable, expandable portable. MIPS-IV. Current Development: memory allocation.. ServerX, Open-source HTTP/HTTPS Server Handler Socket parallel Processing (MIMD) capabilities. Extensive dynamic allocation. Cross-platform compatible IO. Keep-Alive Connections.. Volunteer work: Coach, people Pro-bono Mental Health, Career, Resume Preparation. Follow: #TheProDev, Social_services, Pro Dev. 2022-02-01T00:00:00Z, Community Builder, Education, Amazon (AWS). certifications: 2020-04-01T00:00:00Z, Started Google Engine, Authority: Google. 2019-10-01T00:00:00Z, ScrumMaster (CSM), Scrum Alliance. 2016-06-01T00:00:00Z, CS50 : edX Honor Certificate Introduction edX. C#, 2015-11-01T00:00:00Z, Bootstrap, Verified Science publications: Optimise Image Builds Gitlab C, Publisher: AWS Service enact transactions persistent layers choices services TypeScript way.. Bulding Scalable Modern Microservices World, Level Git Connected, Defining single Lexical Scoping Closure ES5 Container Module Pattern (Inversion Control) dependencies modules.. Evolution JavaScript Dependency Injection, Plain Adapter creates plugs sockets adapter mediator.. Pattern: Many, Repository Domain logic Models Enitity Definition.. Layer, Startup, Explanation Hexaginal Princeples Driven Ecosystem framework.. quirky caching FS speed CI build time.. honors_awards: title: Hacktoberfest 2019, issuer: DigitalOcean, Hactoberfest 2018, 2017, Contributing community GitHub. Services, 2020, DigitalOcean. \nWrite a job professional cover letter for provided profile details if job application is done for the above mention job details"
# gpt_prompt = '''Job details: Title: Stack - Developer Company Uplers Location: Mumbai,Maharashtra,India Industry: Services Consulting description: **Experience: 5+ Years** **Profile: Engineer** **Location: Remote** **Pay: $2600 (USD)** **Shift Time: IST Shift ( 9:30 6:30 PM)** Talent Network?** Network place talents meet opportunities. platform candidate perfect opportunity work global companies contractual basis. talent network Indian benefit gain access career exposure. you'll support, guidance, opportunities level. ready embark journey challenge, engine! **Contractual Position** position requires sign agree terms contract working. structure offer variety commitments refine established skills create **Uplers brings positions benefits ✔ Higher pay industry standards Full-time Ability short period Control **Perks joining Network:** * **Talent Success Coach:** connected dedicated coach guide assignments clients. **Payout:** paid currencies earn standards. **Opportunity:** Work international exposure exciting projects. **Mobility:** comfort living room couch breezy beach. 1. step, register portal 2. Clear decks application form 3. Gear clear 3-stage assessment process 4. Certified Engineer Responsibilities** Architect, design, implement, maintain high-performance, scalable systems on-premise Cloud Engage customers, product management, marketing, operations support engineers products conception development production maintenance Code Java, Python, Shell script and/or C++/C Design develop software SpringBoot, Angular, microservices, SQL NoSQL databases Deploy code production, debug fixe issues proposals, architecture, projects, designs, competitive analysis, technology case studies, escalation post mortem, executive staff Execute projects entirety feature specification, implementation validation Document specifications, bug updates Create plan verifiable milestones time estimates deliver Constructively collaborate team requirements gathering, design reviews Participate QA effective test plans, automated cases, rigorous testing Benchmark performance, identify bottlenecks, troubleshoot improve performance Handle customer escalations Qualifications** BS MS science field 3+ years relevant experience Experience developing Enterprise quality Strong programming Linux environment scripting, knowledge object oriented principles, architectural patterns, databases, operating systems, engineering Good understanding on-disk in-memory data structures algorithms emphasis scalability REST APIs microservice architecture effectively fellow members written verbal communication Stand based, hybrid SaaS, PaaS Iaas Spring Boot, frameworks AWS, Azure, GCP, S3, technologies infrastructure Containers, Docker, Kubernetes Postgres relational database concepts including multithreading concurrent clustering high availability, distributed storage backup, replication, disaster recovery, storage, NAS, NFS networking, orchestration large scale management Artificial Intelligence (AI) / Machine Learning robotics, warehouse (WMS) message queuing workflow motivated managed enjoy working positive attitude technical competence Pragmatic approach solving problems collaboration Open-minded, passionate, ideological Biased automation ensuring works Team-first helping succeed **Uplift Uplers** believes connecting people. people-first organization, constantly strives individuals won't break ground. Helping doesn't surprise growing popular industry. set enter #WorldOfAwesomeness?** **Hit Apply button!** Employment type: functions: Engineering Technology Profile Vishw Kadu Occupation: F(x) Data Labs Email: vishwk@htree.plus features based user feedback.g codes, troubleshooting simple/complex issues, implementing Country: India City: Ahmedabad Gujarat Languages: English, Gujrati, Hindi, Marathi skills: react, nodejs, python, django experiences: starts 2021-08-01T00:00:00Z, Ends Company: Labs, Engineer, location: Ahmedabad. 2021-01-01T00:00:00Z, 2021-02-01T00:00:00Z, Sparks Foundation, Web Development Intern, completed month internship web developer. internship, build basic banking App ReactJs, PHP Mysql., 2019-11-01T00:00:00Z, 2020-11-01T00:00:00Z, Wisebite.in, Freelance Blogger, Blog Writer Ahmedabad, Gujarat, India. education: Starts 2019-01-01T00:00:00Z, 2022-01-01T00:00:00Z, Field study: Programming/Programmer, General, Degree Bachelor School: Government College,Gandhinagar. 2016-01-01T00:00:00Z, Engineering, High School Diploma, R.C.Technical Institute,Ahmedabad 640. accomplishment_organisations: projects: Unomation, Description: Unomation Automation Application Arduino Uno Sensors.. Volunteer work: 2020-03-01T00:00:00Z, Coordinator, coordinator Code-o-fiesta, ARTS_AND_CULTURE, College, Gandhinagar. 2020-06-01T00:00:00Z, Tutor, Content Creator YouTube channel Topic., EDUCATION, YouTube. SCIENCE_AND_TECHNOLOGY, Wisebite.in. certifications: Front-End React, Authority: Coursera. 2020-08-01T00:00:00Z, UI Frameworks Tools: Bootstrap 4, Introduction Programming IoT Boards, publications: honors_awards: \nWrite a job professional cover letter for provided profile details if job application is done for the above mention job details'''
profile_gpt_prompt = "profile details:\n"+profile_details + \
    "\n Can you paraphrase this profile data in 300 words"
job_gpt_prompt = "job details:\n"+job_details + \
    "\n Can you paraphrase this job details in 300 words"
profile = '''Vishw Kadu is a full stack engineer holding 1.5 years of experience in the software engineering industry. Born and raised in India's metropolitan city, Ahmedabad, Vishw is a proven innovator who has shown extraordinary skills in identifying technological requirements for businesses by implementing ingenious methods of development. He is experienced in developing databases, generating user interfaces as well as writing and testing codes to diagnose any anomalies. 

An alumnus of Government Engineering College, Gandhinagar, he holds a Bachelor’s degree in Computer Programming/Programmer General and has acquired professional skills like ReactJS, NodeJS, Python and Django. Moreover, his educational background includes High School Diploma in Computer Engineering from R.C Technical Institute Ahmadabad 640. 

Vishw worked as Web Development Intern at The Sparks Foundation during 2021-02-01T00:00:00Z; where he had developed an elementary banking web application with ReactJS, PHP and Mysql as part of his internship duties. Additionally, he worked as freelance blogger at Wisebite.in from 2019-11-01T00:00:00Z to 2020-11-01T00:00:00Z. 

His experiences are recognised through certifications like Front-End Web Development With React (Coursera), Front-End Web UI Frameworks and Tools: Bootstrap 4 (Coursera) and Introduction and Programming with IoT Boards (Coursera). He has also been associated with volunteer works such as coordinator for “Code - O - Festa” at Government Engineering College and online tutor at YouTube channel “High On Code” assisted under two causes; Arts & culture and Education respectively  

Owing to his brilliant acumen towards development with various technologies, Vishw Kadu is an highly effective IT expert transforming mundane tasks into creative processes relentlessly.
'''
job = '''Uplers Talent Network is looking for an experienced Full Stack Engineer to join our team and provide web development services on a contractual basis. The engineer will be responsible for the design, implementation, and maintenance of high-performance and scalable systems. By joining our Talent Network, you can expect higher pay than industry standards and global exposure with exciting international projects. This full-time contractual position requires 5+ years' experience and offers a variety of commitments that allow you to refine established skills and create new ones.

Responsibilities include architecting, designing, implementing, and maintaining systems on-premise or Cloud computing; engaging with customers, product management, marketing, operations and support engineers; coding in Java, Python, Shell script, C++/C; developing software using frameworks like SpringBoot, Angular, microservices as well as SQL and NoSQL databases; deploying code in production, debugging issues, and fixing them; presenting proposals to executive staff among other tasks. You should also have strong knowledge of object oriented design principles, architectural patterns, operating systems, software engineering and must be able to create work plans with verifiable milestones. Lastly, the ideal candidate should possess excellent written and verbal communication skills along with basic understanding of AWS/Azure/GCP technologies/infrastructure/containers (Docker)/Kubernetes/message queuing systems/workflow management systems etc.

You can benefit from our platform by getting access to a dedicated coach who will guide you before, during as well as after your assignments with clients. Uplers Talent Network not only provides you with an opportunity to gain different skills in a short period but also gives you the flexibility of working from home while controlling your career path at the same time. We encourage self motivation and self management in order to deliver projects within estimates while adhering to industry-standard best practices - such as automated testing - that guarantee successful outcomes.

This is your chance to join one of the most popular companies in the industry offering contracts with generous payouts made in major currencies worldwide! So if you’re ready for your next challenge take the first step – by registering on our portal today!'''
prompt = "Job details:\n "+job + "\n profile details:"+profile + \
    "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"
# gpt_prompt = prompt
# print(job_details)
print(gpt_prompt)
print(len(gpt_prompt.split()))

# gpt_prompt = '''Jobdetails:Title:RemoteMachineLearningEngineerJobsCompanyname:TuringLocation:None,None,IndiaIndustry:SoftwareDevelopmentJobdescription:AnemergingedtechstartupbuildinganinitialteamoftalentedindividualsislookingforaMachineLearningEngineer.Theengineerwillbeactivelycontributingtodevelopingacomputeradaptivetestingsolutionthatalsoemploysmachinelearningfortheeducationspace.Thecompanyhasrecentlyraisedapre-seedfundandaimstoimplementanAdaptiveLearningSystem.Thiswouldbeanexcitingopportunityforthosewhowanttoworkinafast-pacedandcustomer-firstenvironment.ItrequiresanoverlapwithPST.**JobResponsibilities:***Assistinbuildingback-endinfrastructure,datapipelines,andMLmodelsforAI-backedproducts*ExperimentwithMLtechniquestocreateandtestnewprogramfeatures*AssistinextendingandimprovingexistingMLframeworksandlibraries*Workalongsidedataengineerstocreatedataandmodelpipelines,andembedAIandanalyticsintothebusinessdecisionprocesses*IntegrateMLmodelstoend-usersandrunexperiments*Runtests,performstatisticalanalysis,interprettestresults,andperformtuningandscaling**JobRequirements:***Bachelor's/Master'sdegreeinEngineering,ComputerScience(orequivalentexperience)*Atleast3+yearsofrelevantexperienceasaMachineLearningEngineer*Musthavehands-onexperienceinAdaptiveLearningSystems*ShouldbewellversedinMEANand/orMERNstacks*ExpertiseinMachineLearningandArtificialIntelligence*Experienceindatascienceprojectsandpsychometricsisrequired*MusthaveexcellentcommunicationskillswithproficiencyinEnglishEmploymenttype:Full-timeJobfunctions:EngineeringandInformationTechnologyProfiledetails:Name:????????‍????ProgyanBhattacharyaOccupation:SeniorSoftwareEngineeratInterviewKickstartEmail:vishw@htree.plusSummary:FullStackWebApplicationDeveloperwithSpecialisationonReact/Node&DockerVocalAbout:HexagonalArchitecture|TDDasBestPractice|CodeQuality|ArchitectureFirstCodingPracticeCountry:IndiaCity:GreaterBengaluruAreastate:WestBengalLanguages:Bengali,English,Hindiskills:agilemethodologies,ajax,algorithmdesign,artificialintelligence,artificialneuralnetworks,businessstrategy,c,c++,corejava,css,css3,datascience,datastructures,designpatterns,eventmanagement,facebookapi,facebookopengraphprotocols,gamification,html,html5,html5,j2se,java,javascript,jquery,json,linux,machinelearning,magento,marketingstrategy,mysql,naturallanguageprocessing,node.js,parallax,php,poetry,productdesign,programming,python,riskmanagement,semanticweb,seo,softwaredevelopment,startups,venturedevelopment,webapplications,webdevelopment,webservices,zendframeworkexperiences:startsat:2021-10-01T00:00:00Z,Endsat:None,Company:InterviewKickstart,Title:SeniorSoftwareEngineer,description:-ActivelyHiringandBuildingFrontendTeamfromground-up.-CreatingacultureofPlatform-firstDevelopmentExperienceandProduct-ledGrowthinitiatives.-MentoringFreshTalentsandOnboardingthemintoSoftwareDevelopment.-ManagingSoftwareDevelopmentLifecycle,Architecture,InfrastructureatscaleandCross-teamcommunicationforFrontendTeam.,location:Remote.startsat:2019-01-01T00:00:00Z,Endsat:2021-09-30T00:00:00Z,Company:HackerRank,Title:SoftwareDevelopmentEngineerII,description:-Builtanopensourcesolution@hackerrank/firepadtohavecollaborativetexteditingusingMonacoaseditor.ThislibrarypowersourowneditorsandIDEinourInterviewplatform.-Designedarchitectureandleddevelopmentefforttowardbuildingvirtualonsiteexperienceforpost-CovidRemoteInterviewsetups.-DesignedarchitectureforInteractivePlaybacksystemforreportinguserinteractionsandactivitiesinInterviewplatformduringaninterviewprocessforevaluationpurposes.-ConductinginterviewsforSDEIIandSSErolestoupscaleEngineeringteamtocontinuesolvingcomplexproblemsastheycome.-BuiltanOpenSourcetooltoextractTypeinformationfromlibrarymoduletohelptoimprovedeveloperexperienceinconsumerapplications.-Continiousimprovementtowardapplicationperformanceandqualityofexperience.,location:BengaluruArea,India.startsat:2018-09-01T00:00:00Z,Endsat:2018-12-31T00:00:00Z,Company:ChatbotInc,JobCirkit,Title:LeadSoftwareEngineer,description:Builtahiringplatformfromscratchtocreateeasyexperienceforhiringmanagerforhiringblue-collarjobandtracktheirperformance.WasLeadFrontendEngineerandbuilttheproductacrossmultipleusersandroleswithhighlevelofflexibilityinUI.UsingbestpracticesandTDDmethodtocreatewholesoftware.UsedTechnologies:React,Redux,MaterialDesign,RSAEncryption,location:KolkataArea,India.startsat:2018-05-01T00:00:00Z,Endsat:2018-05-31T00:00:00Z,Company:Apexcedo,Title:WebDeveloper,description:DevelopmentofofficialsiteforApexcedo,aconsultationserviceforabroadstudy.UsingMaterialDesignprinciplesongridlayoutandUXisbasedonjQuery/Ajax.,location:KolkataArea,India.education:Fieldofstudy:InformationTechnology,Degreename:Engineer’sDegree,School:WestBengalUniversityofTechnology,Kolkata.Fieldofstudy:Science,Degreename:HigherSecondary,School:BiratiHighSchool.accomplishment_organisations:Organisationname:BytesClub,Title:Co-founder,Description:None.projects:Title:OperationalTransformations,Description:AcollectionofSynchronisationAlgorithmandAdaptersbaseduponOperationalTransformation.Title:storybook-addon-sass-postcss,Description:AStorybookplugin/addonthatincorporatesloadersforExternalStylesheetswithSASSLanguageSupportandCSSModuleswithproperPostprocessingtosupportacrossmultiplebrowservendorandplatforms..Title:babel-plugin-flow-generate-typedef,Description:BabelPlugintoGenerateLibraryDefinitionforLibrariesandModules..Title:MIPSSimulator,Description:*AmicroassemblerandinterpreterwrittenforMIPSAssemblyLanguageforeducationpurpose.*Modulardesignforcompilertomakeiteasilymanageable,expandableandportable.*FollowsstandardsforMIPS-IV.*CurrentDevelopment:Stackmemoryallocation..Title:ServerX,Description:*AnOpen-sourceHTTP/HTTPSWebServerHandlerusingWebSocketwithparallelDataProcessing(MIMD)capabilities.*Extensiveuseofmulti-threadinganddynamicmemoryallocation.*Cross-platformcompatiblewithSocketIO.*CurrentDevelopment:Keep-AliveConnections..Volunteerwork:Title:Coach,Description:HelpingpeoplewithPro-bonoconsultationonMentalHealth,Technology,Career,ResumeBuildingandInterviewPreparation.Follow:#TheProDev,Cause:Social_services,Company:TheProDev.Title:Coach,Description:HelpingpeoplewithPro-bonoconsultationonMentalHealth,Technology,Career,ResumeBuildingandInterviewPreparation.Follow:#TheProDev,Cause:Social_services,Company:TheProDev.Title:CommunityBuilder,Description:HelpingpeoplewithPro-bonoconsultationonMentalHealth,Technology,Career,ResumeBuildingandInterviewPreparation.Follow:#TheProDev,Cause:Education,Company:AmazonWebServices(AWS).Title:CommunityBuilder,Description:HelpingpeoplewithPro-bonoconsultationonMentalHealth,Technology,Career,ResumeBuildingandInterviewPreparation.Follow:#TheProDev,Cause:Education,Company:AmazonWebServices(AWS).certifications:Name:GettingStartedwithGoogleKubernetesEngine,Authority:Google.Name:CertifiedScrumMaster(CSM),Authority:ScrumAlliance.Name:CS50:edXHonorCodeCertificateforIntroductiontoComputerScience,Authority:edX.Name:edXHonorCodeCertificateforProgrammingwithC#,Authority:edX.publications:Name:OptimiseYourDockerImageBuildsinGitlabC,Publisher:AWSCommunityBuilder,Description:ADataServicethatcanenacttransactionsacrossmultiplepersistentlayerswithflexibilityinchoicesofservicesanddatabases,theTypeScriptway..Name:BuldingaScalableDataServiceintheModernMicroservicesWorld,Publisher:LevelUpCoding-GitConnected,Description:DefiningsinglemodulewithLexicalScopingandClosureinES5andusingContainerModulePattern(InversionofControl)tomaintaindependenciesacrossmultiplemodules..Name:EvolutionofModulesinJavaScriptwithDependencyInjection,Publisher:JavaScriptinPlainEnglish,Description:AdapterPatternisapartofHexagonalArchitectureanditcreatesinterfaceasyourcontractwithoutsideworld.Onecanusemultipleplugsinmultiplesocketswiththehelpofanadapterasmediator..Name:TheAdapterPattern:CreateOne,UseMany,Publisher:JavaScriptinPlainEnglish,Description:RepositoryasaperfectplacetoputyourDomainlogicforDataModelsoutsideEnitityDefinition..Name:InsideOut:RepositoryPatternforDataLayer,Publisher:TheStartup,Description:ExplanationofHexaginalArchitecturePrinceplesofDomainDrivenDevelopmentinWebEcosystemusingReactasframework..Name:InsideOut:HexagonalArchitectureinReact,Publisher:TheStartup,Description:AquirkywayofcachingDockerFSlayerstospeedupCIbuildtime..honors_awards:title:Hacktoberfest2019,issuer:DigitalOcean,Description:None.title:Hactoberfest2018,issuer:DigitalOcean,Description:None.title:Hactoberfest2017,issuer:DigitalOcean,Description:ContributingtotheOpenSourcecommunityinGitHub.title:AWSCommunityBuilder,issuer:AmazonWebServices,Description:None.Writeajobcoverletterforprovidedprofiledetailsifjobapplicationisdonefortheabovementionjobdetails'''


@app.get("/coverletter")
def index():

    print(gpt_prompt)
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
    print(response)
    result = response['choices'][0]['text']
    print(result)
    print(response['id'])
    # print(job_details)
    with open("Json/output/demo.log", "a") as log_file:
        log_file.write(gpt_prompt + "\n\n" + result
                       + "\n------------------------------------------------------------------------------\n")

    return result


@app.get("/compressdata_coverletter")
def index():

    # print(gpt_prompt)
    profile_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=profile_gpt_prompt,
        temperature=0.99,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9

    )
    profile_com = profile_response['choices'][0]['text']

    job_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=job_gpt_prompt,
        temperature=0.99,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9

    )
    job_com = job_response['choices'][0]['text']
    gpt_prompt = "Job details:\n "+job_com + "\n profile details:"+profile_com + \
        "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.99,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9

    )


# ----------------------------end----------------------------------


# for kill a port
# sudo kill - 9 `sudo lsof - t - i: 8000`
# http://127.0.0.1:8000

# for run
# uvicorn GPTdemo:app
