from fastapi import FastAPI
from grades import getGrade, mockCourseData


app = FastAPI()

@app.get("/canvas/grades/{course_name}")
def get_course_grade(course_name: str):
    """
    Endpoint to get the grade for a specific course by name.
    """
    classData = mockCourseData()
    grade = getGrade(course_name, classData)
    if grade is None:
        return {"error": "Course not found"}
    
    return {"course_name": course_name, "grade": grade}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Canvas Grades API"}