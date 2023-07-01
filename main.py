from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import Dict, Any
from req import v2
import json

app = FastAPI()


class PredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: Dict[str, Any] = Field(default_factory=dict)



@app.post(path="/predict")
def predict(request: PredictRequest):
    link = request.model_deployed_url
    input = request.inputs
    params = request.parameters
    pipe = request.hf_pipeline

    r = v2(link, input, params, pipe)

    return json.loads(r.json()["outputs"][0]["data"][0])
