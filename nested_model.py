from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    code : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address

add_dict = {'city':'Mirpur', 'state': 'Dhaka', 'code': '1216'}
add1 = Address(**add_dict)

pat_dict ={'name':'Sanjara', 'age': 25, 'gender':'Female','address':add1}
pat1 = Patient(**pat_dict)

print(pat1)
print(pat1.address.code)
