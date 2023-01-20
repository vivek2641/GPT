import json
from fastapi import FastAPI
import openai

app1 = FastAPI()

openai.api_key = "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"


job_filepath = "Json/job_detail/Hewlett Packard Enterprise.json"
with open(job_filepath, 'r') as json_file:
    job_data = json.load(json_file)

linkedindata = "vishwkadu.json"
filepath = "Json/"+linkedindata
with open(filepath, 'r') as json_file:
    profile_data = json.load(json_file)


gpt_prompt = "Job details: " + str(job_data) + "\n Profile details: " + str(profile_data) + \
    "\nWrite a job cover letter for provided profile details if job application is done for the above mention job details"
# gpt_prompt = "Write a cover letter to Prodcrew's HR department. His name is Dharmesh Thakor. An ML project is being worked on by Prodcrew. Prodcrew is hiring for the position of Ml developer, and the qualifications are as follows: 1. Must be enrolled in a computer science or comparable course leading to a bachelor's or master's degree. 2. Solid programming skills in Python and OOPs 3. Experience using OpenCV and Numpy to navigate image processing techniques 4. Must be conversant with the TorchVision and PyTorch frameworks 5. Data preparation in the COCO or CityScapes formats must be mastered.\n so i have to apply for this job .\n My name is Vivek Solanki. I completed my Bachelors in Information Technology in 2021 and completed with 8.27 CPI. I completed my 6 months internship at MaxGen Technologies in Machine Learning. I also learned Python, Django, Machine Learning Models, Deep Learning Models, Computer Vision etc and my goal is to become a great Machine Learning Developer and I have one year experience in Fx Data Lab as Associate Machine Learning Developer."

print(gpt_prompt)
@app1.get("/coverletter")
def index():

    # print(gpt_prompt)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.99,
        max_tokens=4097,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.9
    )
    print("----------------cover letter----------------------")
    result = response['choices'][0]['text']
    print(result)
    json_object = json.dumps(result, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    return result
