from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Patient Info Inserted Successfully!")

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Patient Info Updated Successfully!")

patient_info = {'name':'Sanjara', 'age': 25}
obj1 = Patient(**patient_info)

insert_patient_data(obj1)

