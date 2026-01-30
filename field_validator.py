from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['ibl.com','aabl.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def traansform_name(cls, value):
        return value.upper()

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

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Patient Info Updated Successfully!")

patient_info = {'name':'sanjara', 'age': 25,'weight':58.2, 'married': False,'email':'sanjaratunola@ibl.com','linkedin':'http://sanjara.com/1322','contact':{'phone1':'018205978330', 'phone2':'016209958331'}, }
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

