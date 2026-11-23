class Subject:
    def __init__(self, subCode: str, subName: str, subUnit: int):
        self.subCode = subCode
        self.subName = subName
        self.subUnit = subUnit

    def __str__(self):
        return f"{self.subCode} {self.subName} ({self.subUnit} หน่วยกิต)"