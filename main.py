from fastapi import Request, Depends, FastAPI
from fastapi.responses import JSONResponse

from repository import StreamRepository, RedisRepository
from services import set_links, get_links_in_range

app = FastAPI()


async def redis_repository() -> RedisRepository:
    return RedisRepository()


@app.get("/visited_domains/", response_class=JSONResponse)
async def read_item(
    start,
    end,
    repository: StreamRepository = Depends(redis_repository),
):
    return get_links_in_range(start, end, repository)


@app.post("/visited_links/")
async def create_item(
    request: Request, repository: StreamRepository = Depends(redis_repository)
):
    data = await request.json()
    return set_links(data, repository)
