from app.settings import PROJECT_NAME, BACKEND_CORS_ORIGINS, APP_ROOT
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import index


app = FastAPI(title=PROJECT_NAME)
app = FastAPI()

############
#  ROUTES  #
############
all_routers = [index.router]
for router in all_routers:
    app.include_router(router)

##################
#  STATIC FILES  #
##################
public_folder_path = APP_ROOT + "/public"
static_files = StaticFiles(directory=public_folder_path)
app.mount("/", static_files, name="static")

#################
#  MIDDLEWARES  #
#################
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin) for origin in BACKEND_CORS_ORIGINS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
