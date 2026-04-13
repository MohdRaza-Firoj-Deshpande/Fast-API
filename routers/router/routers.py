from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/{id}', status_code=status.HTTP_200_OK)
def check(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found (greater than 5)'}  # ✅ Fixed message
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id} found'}                     # ✅ Fixed message