from inference_sdk import InferenceHTTPClient
import screenreader


def fetch_results_by_path(path: str = "test.jpg"):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="Ick0RwB9A8OyNxRtXk7r"
    )

    scimage = screenreader.fetch_screen()
    result = CLIENT.infer(scimage, model_id="bsa-axrpu/3")

    return result['predictions']

if __name__ == "__main__":
    print(fetch_results_by_path())