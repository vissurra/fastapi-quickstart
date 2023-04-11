import uvicorn
from fastapi import FastAPI, Depends
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from app.database.base import db
from app.database.user import UserToken, User
from app.router import user


def get_db():
    try:
        if db.is_closed():
            db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()


app = FastAPI(dependencies=[Depends(get_db)],
              openapi_url='/fastapi/openapi.json',
              docs_url='/fastapi/docs',
              redoc_url='/fastapi/redoc')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user.router)


@app.get("/")
def root():
    return {
        'message': 'Hello World'
    }


@app.get("/fastapi")
def root():
    return {
        'message': 'Hello FastAPI'
    }


if __name__ == '__main__':
    with db.connection_context():
        logger.info('Create tables')
        db.create_tables([User, UserToken])

    uvicorn.run("server:app", host='0.0.0.0', port=8000)
