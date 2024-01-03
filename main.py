from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

import os



path=os.getcwd()
for x in path:
    if x == '\\':
        x='/'



app = FastAPI()
app.mount("/public", StaticFiles(directory="public", html=True))
#app.mount("/static", StaticFiles(directory="/", html=True))

origins = ["https://localhost", "http://127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],#, "OPTIONS", "DELETE", "PATH", "PUT"],
    allow_headers=["Content-Type", "Accept", "Location", "Allow", "Content-Disposition", "Sec-Fetch-Dest"],
)

@app.get("/")
def read_root():
    return RedirectResponse("http://127.0.0.1:8000/public/index.html")