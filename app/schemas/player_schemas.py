from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    age: int
    position: str

def __str__(self):
        return f"{self.name} ({self.position})"

class PlayerUpdate(BaseModel):
    name: str = None
    age: int = None
    position: str = None

class PlayerResponse(BaseModel):
    id: int
    name: str
    age: int
    position: str

class PerformanceMetricResponse(BaseModel):
    player_id: int
    games_played: int
    average_score: float
