class Student:
    def __init__(self, sid: str, fullname: str):
        self.sid = sid
        self.fullname = fullname

    def __str__(self):
        return f"รหัสนักศึกษา: {self.sid} ชื่อ: {self.fullname}"