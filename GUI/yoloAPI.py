from ultralytics import YOLO

model = YOLO("model/best.pt")

results = model("test.jpg")

print(results[0].boxes)
print(results[0].names)

