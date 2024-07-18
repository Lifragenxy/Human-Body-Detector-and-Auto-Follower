from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="Ick0RwB9A8OyNxRtXk7r"
)

result = CLIENT.infer("test.jpg", model_id="bsa-axrpu/1")

print(result['predictions'])