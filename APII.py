from fastapi import FastAPI

students = [
    {"id":1, "name":"Deepanshu", "age":22},
    {"id":2, "name":"Harshuuuu", "age":21},
]



app = FastAPI()

@app.get("/students")
def get_students():
    return {
        "Message":"All Students",
        "data":students
    }




@app.get("/student/{student_id}")
def get_student(student_id:int):
    for x in students:
        if x["id"] == student_id:
            return x 
    return {"message":"Student Not Found    "}



@app.post("/student")
def add_student(id:int, name:str, age:int):
    new_student = {
        "id":id,
        "name":name,
        "age":age
    }

    students.append(new_student)
    return {
        "message":"Student Add",
        "data":new_student
    }   


@app.put("/student/{student_id}")
def update_student(student_id: int,name: str,age: int):
    
    for student in students:
        if student["id"] == student_id:
           student["name"] = name
           student["age"] =age

           return{
                "message": "student update successfully",
                "data" : student
           }
    return {"message": "student not found"}

@app.patch("/student/{student_id}")
def patch_student(student_id: int,age: int):


    for student in students:
        if student ["id"] == student_id:
             student["age"] = age


             return {
                  "message": "student age updated",
                  "data" : student
             }
    return {"message": "student not found"}



@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            
            return{
                "message": "student deleted successfully"

            }
        return{"message": "student not found"}

