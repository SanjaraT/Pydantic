from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name',description='Enter your name')]
    age : int
    weight : Annotated[float, Field(gt=0,strict = True)]
    married : bool
    allergies : Optional[List[str]]=None
    email : EmailStr
    linkedin : AnyUrl
    contact : Dict[str, str]
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

patient_info = {'name':'Sanjara', 'age': 25,'weight':58.2, 'married': False,'email':'sanjaratunola@gmail.com','linkedin':'http://sanjara.com/1322','contact':{'phone1':'018205978330', 'phone2':'016209958331'}, }
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

