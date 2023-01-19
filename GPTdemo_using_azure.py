import json
import requests
import os
from fastapi import FastAPI
import openai

# app = FastAPI()

openai.api_key = "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"


def data(linkedindata):
    filepath = "Json/"+linkedindata
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    
    
    print(data["skills"])


data = data("Hemenbhai.json")


# def read_json(filepath):
#     with open(filepath, 'r') as json_file:
#         data = json.load(json_file)
#     return data
    

# data = read_json("Json/linkedindata.json")

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
# gpt_prompt = ("Write a cover letter to " + contact_person + " from " + your_name + " for a " + role + "job at " + company_name + "." +
#               " I have " + personal_exp["years"] + " years of " + personal_exp["position"] + "." +
#               " experience at " + personal_exp["company_name"] + "."
#               " I have compeleted my graduation in " +
#               education["course"] + "at" + education["collage"] + "from" +
#               education["completed year"] +
#               "and CPI is " + education["CPI"] + "."
#               " I am excited about the job because " + job_desc + ".")


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
# http://127.0.0.1:8000

# for run
# uvicorn GPTdemo:app
