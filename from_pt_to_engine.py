from ultralytics import YOLO
import tensorrt
import numpy as np
# Load the YOLOv8 model
model = YOLO('./orin_weights/best_v8n.pt')

# Export the model to TensorRT format
model.export(format='engine', half=True,device='cuda:0')  # creates 'yolov8n.engine'

# # Load the exported TensorRT model
# tensorrt_model = YOLO('./weights/best_v5s6u.engine')
# np.bool = np.bool_
# # Run inference
# results = tensorrt_model('https://ultralytics.com/images/bus.jpg',imgsz=1280)
