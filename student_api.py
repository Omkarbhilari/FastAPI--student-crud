
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field,EmailStr

app = FastAPI()


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    email: EmailStr
    course: str = Field(min_length=2, max_length=50)


# Temporary storage
students = {}



@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    students[student_id] = student
    return {"message": "Student created", "student": student}


# READ ALL
@app.get("/students")
def get_students():
    return students


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = student
    return {"message": "Student updated", "student": student}


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]
    return {"message": "Student deleted"}
