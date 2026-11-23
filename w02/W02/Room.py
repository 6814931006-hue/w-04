from Building import Building

class Room:
    def __init__(self, roomCode: str, building: Building = None):
        self.roomCode = roomCode
        self.building = building

    def __str__(self):
        b_info = f" ({self.building})" if self.building else ""
        return f"ห้อง {self.roomCode}{b_info}"