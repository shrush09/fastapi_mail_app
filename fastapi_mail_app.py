from fastapi import (
    FastAPI, 
    BackgroundTasks, 
    UploadFile, File, 
    Form, 
    Query,
    Body,
    Depends
)
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.responses import JSONResponse
from starlette.requests import Request
from pydantic import BaseModel, EmailStr
from typing import List
import uvicorn

app = FastAPI()

class EmailSchema(BaseModel):
    email: List[EmailStr]

conf = ConnectionConfig(
    MAIL_USERNAME = "shrushtimor",
    MAIL_PASSWORD = "Shrushti@123",
    MAIL_FROM = "shrushtimor09@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False
)

@app.post("/emailbackground")
async def send_in_background(
    background_tasks: BackgroundTasks,
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.dict().get("email"),
        body="Simple background task",
        )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message,message)
    
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


if __name__ == "__main__":
    uvicorn.run("fastapi_mail_app:app", reload=True)