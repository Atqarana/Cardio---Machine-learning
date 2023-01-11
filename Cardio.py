# -*- coding: utf-8 -*-
"""
Created on Fri june 29 12:27:22 2022
@author: Atqa Rana
"""
from fastapi import FastAPI, Request
import uvicorn
import pickle
from fastapi.middleware.cors import CORSMiddleware
from models import Heart
cardio=FastAPI()
origins =["*"]

cardio.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= False,
    allow_methods=["*"],
	allow_headers=["*"],
    max_age=36000,
)
model=pickle.load(open("model.pkl","rb"))

@cardio.get("/")
async def root_url():
    return {'message' : "Successfully Running the server..."}


@cardio.post("/pred")
async def pred(data:Heart):
    age=data.age
    gender=data.gender
    ChestPainType=data.ChestPainType
    MaxHR=data.MaxHR
    ExerciseAngina=data.ExerciseAngina
    FastingBS=data.FastingBS
    features=list([age,gender,ChestPainType,MaxHR,ExerciseAngina,FastingBS])
    pred=model.predict([features])
  
    
    if(pred==1):
        return 1
    else:
        return 0


if __name__=="__main__":
   #uvicorn.run(cardio,host="192.168.66.115",timeout_keep_alive=300)
    uvicorn.run(cardio,host="172.24.54.49",timeout_keep_alive=300)
    
    