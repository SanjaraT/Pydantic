from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : Optional[List[str]]=None
    contact : Dict[str, str]

def insert_patient_data(patient : Patient):
    print("Patient Name : ",patient.name)
    print("Age : ",patient.age)
    print("Weight : ",patient.weight)
    print("Marrital Status: ",patient.married)
    print("Allergies : ",patient.allergies)
    print("Contact Details : ",patient.contact)
    print("Patient Info Inserted Successfully!")

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Patient Info Updated Successfully!")

patient_info = {'name':'Sanjara', 'age': 25,'weight':58.2, 'married': False,'contact':{'email':'sanjartunola@gmail.com','phone':'22339987'}}
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

