import nest_asyncio
nest_asyncio.apply()
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from workflows.form_agent import create_form_agent
from services.form_filler import fill_sample_form

app = FastAPI()

# Allow Angular to connect from localhost:4200
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-agent")
async def run_agent(request: Request):
    body = await request.json()
    address = body.get("address", "")

    agent = create_form_agent()
    result = agent.invoke({"address": address})
    
    if "address_info" in result:
        await fill_sample_form(result["address_info"])

    return result
