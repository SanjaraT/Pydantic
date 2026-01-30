from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : Optional[List[str]]=None
    email : EmailStr
    linkedin : AnyUrl
    contact : Dict[str, str]

    @model_validator(mode='after')
    def val_emergency_con(cls, model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError('Patients older than 60 muust have an emergency contact.')
        return model

def insert_patient_data(patient : Patient):
    print("Patient Name : ",patient.name)
    print("Age : ",patient.age)
    print("Weight : ",patient.weight)
    print("Marrital Status: ",patient.married)
    print("Allergies : ",patient.allergies)
    print("Email: ", patient.email)
    print("Linkedin URL: ", patient.linkedin)
    print("Contact Details : ",patient.contact)
    print("Patient Info Inserted Successfully!")

patient_info = {'name':'sanjara', 'age': 65,'weight':58.2, 'married': False,'email':'sanjaratunola@ibl.com','linkedin':'http://sanjara.com/1322','contact':{'phone1':'018205978330'}, }
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

