# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:30:52 2022

@author: t580
"""


from pydantic import BaseModel
from typing import List
class Heart(BaseModel):
    age:int
    gender:int
    ChestPainType:int
    MaxHR:int
    ExerciseAngina:int
    FastingBS:int
   