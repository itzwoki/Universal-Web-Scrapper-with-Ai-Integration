#external imports
from fastapi import FastAPI

#files import - internal imports
from scrapper.fetchApi import router as ScrapperRouter
from LLM.gpt4all import router as LLMrouter



app = FastAPI(
title="Web Scrapper",
description="Web Scrapper Backend.",
contact={
    "name": "M.Waqas",
    "email": "abdullahwaqas22@gmail.com"

},
license_info={
    "name": "Software Engineer"
}
)

app.include_router(ScrapperRouter)
app.include_router(LLMrouter)

