from fastapi import APIRouter

router = APIRouter()
router.tags = ["Tweets"]


@router.get("/")
def index():
    pass
