from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

import asyncio
import threading
import schedule
import time

from core.config import project_settings
from apis.update_tools import tool_table_update
from db.update_tool import update_tool
from db.delete_data import delete_data


def include_router(app):
    app.include_router(tool_table_update)


def start_application():
    app = FastAPI(title = project_settings.project_title, version = project_settings.project_version)
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=["*"], 
        allow_credentials=True, 
        allow_methods=["*"], 
        allow_headers=["*"],
        )
   
    include_router(app)
    update_tool()

    return app
 
app = start_application()


def run_scheduled_jobs():
    while True:
        delete_data()
        time.sleep(5)
        if server_running == False:
            break

if __name__ == "__main__":
    # Start the threads
    thread1 = threading.Thread(target=run_scheduled_jobs)
    thread1.start()
    import uvicorn
    global server_running
    server_running = True
    uvicorn.run(app, host="127.0.0.1", port=8000, lifespan="on")
    server_running = False
    


