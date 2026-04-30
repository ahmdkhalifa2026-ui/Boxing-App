from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Models
class Match(BaseModel):
    opponent: str
    date: str
    result: str  # win/loss/draw 
    performance_data: dict

class TrainingSession(BaseModel):
    date: str
    duration: int  # duration in minutes
    exercises: str  # description of exercises
    performance_data: dict

# In-memory storage (replace with a database in production)
matches = []
training_sessions = []

# Routes for recording matches
@router.post('/matches/')
def record_match(match: Match):
    matches.append(match.dict())
    return {'message': 'Match recorded successfully!', 'match': match}

@router.get('/matches/')
def get_matches():
    return matches

# Routes for recording training sessions
@router.post('/training/')
def record_training(training: TrainingSession):
    training_sessions.append(training.dict())
    return {'message': 'Training session recorded successfully!', 'training': training}

@router.get('/training/')
def get_training_sessions():
    return training_sessions
