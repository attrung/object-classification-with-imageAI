from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

def objectDetection(inputPath, outputPath, prob):
    detector = ObjectDetection()
    # detector.setModelTypeAsRetinaNet()
    # detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo-tiny.h5"))
    # detector.setModelTypeAsYOLOv3()
    # detector.setModelPath((os.path.join(execution_path , "yolo.h5")))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image = os.path.join(execution_path + '/static/image/', inputPath), output_image_path = os.path.join(execution_path + '/static/image/', outputPath), minimum_percentage_probability = prob)

    nameList = []
    probList = []
    for eachObject in detections:
        nameList.append(str(eachObject["name"]))
        probList.append(eachObject["percentage_probability"])
    nameList = unique(nameList)
    return nameList, probList

def unique(nameList):
    d = {}
    for pos in range(len(nameList)):
        if nameList[pos] in d:
            d[nameList[pos]] += 1
            nameList[pos] += str(d[nameList[pos]] + 1)
        else:
            d[nameList[pos]] = 0
    return nameList

