class Building:
    def __init__(self, buildingCode: str):
        self.buildingCode = buildingCode
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)

    def listRooms(self):
        for r in self.rooms:
            print(f"  - {r}")

    def __str__(self):
        return f"อาคาร {self.buildingCode}"