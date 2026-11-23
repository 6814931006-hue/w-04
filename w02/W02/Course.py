from Subject import Subject
from Lecturer import Lecturer
from Room import Room

class Course:
    def __init__(self, section: int, subject: Subject, lecturer: Lecturer, room: Room):
        self.section = section
        self.subject = subject
        self.lecturer = lecturer
        self.room = room

    def __str__(self):
        return f"{self.subject} | กลุ่มเรียน (Sec): {self.section} | ผู้สอน: {self.lecturer} | สถานที่: {self.room}"