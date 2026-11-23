from Student import Student
from Course import Course

class Enrollment:
    def __init__(self, semester: int, year: int, student: Student):
        self.semester = semester
        self.year = year
        self.student = student
        self.courses = []

    def addCourse(self, course: Course):
        self.courses.append(course)

    def showEnrollment(self):
        print("=" * 60)
        print(f"ข้อมูลการลงทะเบียนเรียน ภาคการศึกษาที่ {self.semester}/{self.year}")
        print(self.student)
        print("-" * 60)
        print("รายวิชาที่ลงทะเบียน:")
        total_units = 0
        for idx, c in enumerate(self.courses, 1):
            print(f"{idx}. {c}")
            total_units += c.subject.subUnit
        print("-" * 60)
        print(f"รวมหน่วยกิตทั้งหมด: {total_units} หน่วยกิต")
        print("=" * 60)