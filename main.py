from fastapi import FastAPI, WebSocket
import asyncio
import pandas as pd
import json


# Create application
app = FastAPI(title='WebSocket Example')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
# Create a fastapi websocket endpoint to send random numbers to the client

    await websocket.accept()
    while True:
        await websocket.send_json(json.loads(pd.read_html("https://merolagani.com/LatestMarket.aspx")[0].to_json(orient="records")))
        await asyncio.sleep(30)

@app.get("/")
async def root():
    return json.loads(pd.read_html("https://merolagani.com/LatestMarket.aspx")[0].to_json(orient="records"))