from ultralytics import YOLO
import screenreader

global model
model = YOLO("model/best.pt")

def fetch_boxes_by_path(path="test.jpg"):
    results = model.predict(screenreader.fetch_screen())
    predictions = results[0].boxes.xyxy  # 如果你只有一张图片的结果，使用 [0] 来获取第一张图片的结果

    nms = ['107', '114', 'died', 'human']
    order = 0
    box_list = []
    for pred in predictions:
        # 遍历每个检测结果
        #for pred in predictions:
        x1, y1, x2, y2 = pred.tolist()  # 获取坐标、置信度和类别
        # 计算框的宽度和高度
        box_width = x2 - x1
        box_height = y2 - y1
        # 打印位置、大小、置信度和类别

        box_list.append({'x': (x1+x2)//2,
                         'y': (y1+y2)//2,
                         'width': box_width,
                         'height': box_height,
                         'confidence': float(results[0].boxes.conf[order]),
                         'class': nms[int(results[0].boxes.cls[order])]})

        order += 1

    return box_list

if __name__ == "__main__":
    print(fetch_boxes_by_path())