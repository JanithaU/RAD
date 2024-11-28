import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv
from core.config import settings
from api.app_router import note_router,user_router
from api.auth_router import router
from api.aws_router import aws_router

from db.session import get_db
from fastapi import Depends




# load_dotenv(".env")


def add_routers(app):
    app.include_router(note_router,prefix="/notes", tags=["notes"])
    app.include_router(user_router,prefix="/users", tags=["users"])
    app.include_router(router, prefix="/auth", tags=["Authentication"])
    app.include_router(aws_router,prefix="/aws", tags=["cloud"])

def start_app():
    app = FastAPI(title="Notes", version=settings.PROJECT_VERSION)
    add_routers(app)
    return app

app = start_app()

# # Get the correct database URL dynamically
# db_url = get_database_url()

# # Add middleware with the selected DB URL
# app.add_middleware(DBSessionMiddleware, db_url=db_url)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
