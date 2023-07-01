Fast API Wrapper for V2 Inference Protocol
---



1. You can run the fastapi with uvicorn as `uvicorn main:app --host 0.0.0.0 --port 8000`  
2. Then you can run the test runner as `python test_all.py http://0.0.0.0:8000/predict` - Note the `TASK_TO_URL` contains urls to models hosted internally by Truefoundry

Finally you can deploy your fastapi app on Truefoundry and re run the test runner as `python test_all.py <YOUR URL>`

> Note the object detection model might take 15-30s to respond
