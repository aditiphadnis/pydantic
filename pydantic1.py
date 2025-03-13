from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool

Employee(name="Chris DeTuma", 
        email="cdetuma@example.com",
        date_of_birth="1998-04-02",
        salary= 123_000.00,
        department="IT",
        elected_benefits=True,
        )

new_employee_dict = {"name": "Chris DeTuma",
                     "email": "cdetuma@example.com",
                     "date_of_birth": "1998-04-02",
                     "salary": 123_000.00,
                     "department": "IT",
                     "elected_benefits": True,
            }
Employee.model_validate(new_employee_dict)

new_employee_json = """
{"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
"name":"Eric Slogrenta",
"email":"eslogrenta@example.com",
"date_of_birth":"1990-01-02",
"salary":125000.0,
"department":"HR",
"elected_benefits":false}
"""


new_employee = Employee.model_validate_json(new_employee_json)


print(new_employee.model_dump())

print(new_employee.model_dump_json())

jsonschema= Employee.model_json_schema()

print(jsonschema)