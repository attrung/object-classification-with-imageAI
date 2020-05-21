from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

def objectDetection(inputPath, outputPath, prob):
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo-tiny.h5"))
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
    for