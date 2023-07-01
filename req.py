import json
from fastapi import HTTPException
import base64 as bs
import requests
import PIL.Image as Image
import io

def isb64(x):
    try:
        if isinstance(x,str):
            x_bytes = bytes(x, 'utf-8')
        elif isinstance(x,bytes):
            x_bytes = x
        else:
            raise ValueError("Invalid url- contained unicodes/ not in str-bytes format")
        return bs.b64encode(bs.b64decode(x_bytes))
    except:
        return False
    



def v2(link, input, params, pipeline):
    payload = {
            "parameters": {
            "content_type": "application/json",
            "headers": {}
            },
            "inputs": [
            {
                "name": "array_inputs",
                "shape": [-1],
                "datatype": "BYTES",
                "parameters": {
                "content_type": "application/json",
                "headers": {}
                },
                "data": input
            }
            ],
            "outputs": [
            {
                "name": "output",
                "parameters": {
                "content_type": "application/json",
                "headers": {}
                }
            }
            ]
        }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    # print(pipeline)
    
    if pipeline == "zero-shot-classification":
        labels= json.dumps(params['candidate_labels'])
        print(f"[INFO] Recived request for {pipeline}")
        size = len(params["candidate_labels"])
        payload = {
            "parameters": {
            "content_type": "application/json",
            "headers": {}
            },
            "inputs": [
            {
                "name": "array_inputs",
                "shape": [
                -1
                ],
                "datatype": "BYTES",
                "parameters": {
                "content_type": "application/json",
                "headers": {}
                },
                "data": input
            },
            {
                "name": "candidate_labels",
                "shape": [
                size
                ],
                "datatype": "BYTES",
                "parameters": {
                "content_type": "application/json",
                "headers": {}
                },
                "data": labels
            }
            ],
            "outputs": [
            {
                "name": "output_*",
                "parameters": {
                "content_type": "application/json",
                "headers": {}
                }
            }
            ]
        }
        
    elif pipeline == "object-detection":
        
        print(f"[INFO] Recived request for {pipeline}")
        if isinstance(input, str) and input.startswith("http"):
            payload["parameters"]["content_type"] = "string"
            payload["inputs"][0]["parameters"]["content_type"] = "str"
        elif isinstance(input, str) and input.endswith(tuple([".jpg", ".jpeg", ".png"])):
            image = Image.open(input)
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='PNG')
            image_bytes = image_bytes.getvalue()
            image_base64 = bs.b64encode(image_bytes).decode('utf-8')
            payload["parameters"]["content_type"] = "string"
            payload["inputs"][0]["parameters"]["content_type"] = "pillow_image"
            payload["inputs"][0]["shape"] = [-1,-1,-1]
            payload["inputs"][0]["data"] = image_base64 

        elif isb64(input):
            payload["parameters"]["content_type"] = "string"
            payload["inputs"][0]["parameters"]["content_type"] = "pillow_image"
            payload["inputs"][0]["shape"] = [-1,-1,-1]
            
        else:
            raise HTTPException(422, "Invalid Image")
    
    elif pipeline == "token-classification":
        print(f"[INFO] Recived request for {pipeline}")
        payload["inputs"][0]["content_type"] = "BOOL"
        
    elif pipeline == "text-generation":
        print(f"[INFO] Recived request for {pipeline}")
        payload["inputs"][0]["content_type"] = "BOOL"
        
    else:
        raise HTTPException(400, "Invalid/unsupported pipeline")
    
    try:
        r = requests.post(url = link,data=json.dumps(payload), headers= headers)
        print(f"[INFO] Request sent with status code {r.status_code}")
        return r
    except requests.exceptions.RequestException as e:
        raise HTTPException(500, e)
    
