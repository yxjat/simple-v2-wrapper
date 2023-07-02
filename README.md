# Fast API Wrapper for V2 Inference Protocol
---
This is a one stop solution for creating v2 requests, in the most basic format ever! Simply send in the deployed model urls and your inputs and watch the magic happen. Returns Json formatted output data with interpretable code which makes it even easier to use with almost every huggingface model. 
</br>
</br>
</br>
![The Pipeline](https://github.com/yxjat/simple-v2-wrapper/assets/96134951/80ee8257-a2e8-46df-b005-9e6f0069cf48)

> ### Deployed Url:- https://v2.demo1.truefoundry.com/predict

</br>

## Currently supports the following pipelines:
---
https://huggingface.co/sshleifer/tiny-gpt2
```bash
text-generation
```

https://huggingface.co/d4data/biomedical-ner-all/tree/main
```bash
token-classification
```

https://huggingface.co/typeform/distilbert-base-uncased-mnli

```bash
zero-shot-classification
```

https://huggingface.co/TahaDouaji/detr-doc-table-detection
```bash
object-detection
```

Input Format:
```json
{
  "hf_pipeline": string,
  "model_deployed_url": string,
  "inputs": any,
  "parameters":any
}
```
</br>
</br>

### The following script is an example in action!

>cUrls can also be used similarly
</br>
Object detection:
</br>

```python
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '{ "hf_pipeline": "object-detection","model_deployed_url": "https://object-intern-yajat.demo1.truefoundry.com/v2/models/object/infer", "inputs": "https://www.w3.org/WAI/WCAG22/Techniques/pdf/img/table-word.jpg","parameters": {}}'

response = requests.post('https://v2.demo1.truefoundry.com/predict', headers=headers, data=data)

print(response.json())

```
</br>
Output:
</br>

```json
[
	{
		"score":0.9906801581382751,
		"label":"table",
		"box":{
			"xmin":20,
			"ymin":54,
			"xmax":479,
			"ymax":257
		}
	}
]
```
</br>
</br>
</br>
Text Generation:
</br>

```python
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '{"hf_pipeline": "text-generation","model_deployed_url":"https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer","inputs": "Hello, how are you today? ","parameters": {"min_new_tokens": 10,"do_sample": true,"temperature": 1.0,"max_new_tokens": 20,"num_return_sequences": 5}}'

response = requests.post('https://v2.demo1.truefoundry.com/predict', headers=headers, data=data)

print(response.json())

```

Output:

```json
[
	{
		"generated_text":"Hello how are you today?PocketProsPros Late Boone� brutality skilletOutside omega Late workshops omega representations predators incarcer WheelsGy PocketGy Pocket653MostOutside representations factors Bend grandchildren praying boils Medicacious Redux mutual omega skillet Pocket predators predators� representations Tre"
	}
]
```
</br>
</br>

## Working on localhost

To get started on your own pc,

1. Clone the repo:
```bash
git clone https://github.com/yxjat/simple-v2-wrapper
```

2. Run the uvicorn server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
And you're all set!

</br>
</br>

## Deployed models:

```bash
https://object-intern-yajat.demo1.truefoundry.com
```
```bash
https://textgen-intern-yajat.demo1.truefoundry.com
```

> Note! the object detection pipeline might take a while to respond (10s)

