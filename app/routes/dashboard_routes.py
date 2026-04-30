from fastapi import APIRouter

router = APIRouter()

@router.get('/team-overview')
async def get_team_overview():
    # Logic to fetch team overview
    return {'message': 'Team overview data'}

@router.get('/statistics')
async def get_statistics():
    # Logic to fetch statistics
    return {'message': 'Statistics data'}

@router.get('/top-players')
async def get_top_players():
    # Logic to fetch top players
    return {'message': 'Top players data'}

@router.get('/weakest-metrics')
async def get_weakest_metrics():
    # Logic to fetch weakest metrics
    return {'message': 'Weakest metrics data'}

