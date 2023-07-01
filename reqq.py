import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '{"hf_pipeline": "text-generation","model_deployed_url":"https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer","inputs": "Hello, how are you today? ","parameters": {"min_new_tokens": 10,"do_sample": true,"temperature": 1.0,"max_new_tokens": 20,"num_return_sequences": 5}}'

response = requests.post('https://ml-yajat-intern-yajat-8000.demo1.truefoundry.com/predict', headers=headers, data=data)

print(response.json())