from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import index

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
static_files = StaticFiles(directory="public")
app.mount("/", static_files, name="static")
