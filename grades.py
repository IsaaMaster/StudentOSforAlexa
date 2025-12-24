import requests
import dotenv
import os
import json

dotenv.load_dotenv()

CANVAS_AUTH_SECRET = os.getenv("CANVAS_AUTH_SECRET")
CANVAS_API_URL = "https://canvas.instructure.com/api/v1/"

def main():
    #classData = getClassData()
    classData = mockCourseData()
    print(getGrade("Acting I: Foundations", classData))

def getClassData():
    """
    Fetches course data from the Canvas API, including total scores for each course.
    """
    headers = {
        "Authorization": f"Bearer {CANVAS_AUTH_SECRET}"
    }
    response = requests.get(f"{CANVAS_API_URL}/courses?include[]=total_scores", headers=headers)
    return response.json()


def getGrades(course_data):
    """
    Extracts and prints the current scores for each course from the provided course data.
    """
    for course in course_data:
        if 'enrollments' in course:
            print(f"Course: {course['name']}", end=" - ")
            print(course["enrollments"][0]["computed_current_score"])

def getGrade(course_name, course_data):
    """
    Retrieves the grade for a specific course by name from the provided course data.
    """
    for course in course_data:
        if 'enrollments' in course:
            if course['name'].lower() == course_name.lower():
                return course["enrollments"][0]["computed_current_score"]
    return None


def mockCourseData():
    """
    locads mock course data from a local JSON file for testing purposes.
    saves time and avoids hitting the API repeatedly during development.
    """
    if os.path.exists("mockCourseData.json"):
        with open("mockCourseData.json", "r") as f:
            return json.load(f)
    return None

def saveMockCourseData(data):
    """
    Saves mock course data to a local JSON file for future testing.
    """
    with open("mockCourseData.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()