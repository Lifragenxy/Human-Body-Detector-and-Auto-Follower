from roboflow import Roboflow

rf = Roboflow(api_key="Ick0RwB9A8OyNxRtXk7r")
project = rf.workspace().project("bsa-axrpu")
model = project.version("1").model

print(model)

#job_id, signed_url, expire_time = model.predict_video(
#    "E:\\Videos\\ai\\Banana Shooter 2024-07-18 00-47-10.mp4",
#    fps=5,
#    prediction_type="batch-video",
#)
#
#results = model.poll_until_video_results(job_id)
#
#print(results)
