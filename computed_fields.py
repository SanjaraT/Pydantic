from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    height: float
    married : bool
    allergies : List[str]
    email : EmailStr
    contact : Dict[str, str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient_data(patient : Patient):
    print("Patient Name : ",patient.name)
    print("Age : ",patient.age)
    print("Weight : ",patient.weight)
    print("Height : ",patient.height)
    print("BMI : ",patient.bmi)
    print("Marrital Status: ",patient.married)
    print("Allergies : ",patient.allergies)
    print("Email: ", patient.email)
    print("Contact Details : ",patient.contact)
    print("Patient Info Inserted Successfully!")


patient_info = {'name':'sanjara', 'age': 25,'weight':58.2,'height':'1.72', 'married': False,'allergies':['pollen','dust'],'email':'sanjaratunola@gmail.com','contact':{'phone1':'018205978330', 'phone2':'016209958331'}}
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

