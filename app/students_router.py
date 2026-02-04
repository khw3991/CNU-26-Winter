from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    major: str


students = [
    Student(id=20251846, name='Amber', major='Computer Science'),
    Student(id=20240921, name='Johnson', major='English'),
]

Students_router=APIRouter(prefix='/students', tags=["students"])

class stuCreate(BaseModel):
    id : int
    name : str
    major : str

class stuPut(BaseModel):
    name :str
    major : str

class stuPatch(BaseModel):
    name : Optional[str]=None
    major : Optional[str]=None

@Students_router.get('/')
def get_students():
    return students

@Students_router.post(path='/')
def create_student(payload: stuCreate):
    student = Student(id=payload.id, name=payload.name, major=payload.major)
    students.append(student)
    return student

@Students_router.delete('/{stu_id}')
def remove_student(stu_id:int):
    for student in students:
        if student.id==stu_id:
            students.remove(student)
            return
    raise HTTPException(status_code=404, detail='Student not found')


@Students_router.get('/{stu_id}')
def get_student_by_id(stu_id: int):
    for student in students:
        if student.id== stu_id:
            return student
    raise HTTPException(status_code=404, detail='Student not found')

@Students_router.put(path='/{stu_id}')
def update_student(payload:stuPut, stu_id :int):
    for student in students:
        if student.id == stu_id:
            student.name=payload.name
            student.major=payload.major
            return student
    raise HTTPException(status_code=404, detail='Student not found')

@Students_router.patch(path='/{stu_id}')
def patch_item(payload:stuPatch, stu_id:int):
    for student in students:
        if student.id==stu_id:
            if payload.name is not None:
                student.name=payload.name
            if payload.major is not None:
                student.major=payload.major
            return student
    raise HTTPException(status_code=404, detail='Student not found')



