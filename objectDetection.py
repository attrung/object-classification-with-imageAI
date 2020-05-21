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
    print(nameList)
    return nameList, probList

def unique(nameList):
    d = {}
    for pos in range(len(nameList)):
        if nameList[pos] in d:
            nameList[pos] += str(d[nameList[pos]] + 1)
            d[nameList[pos]] += 1
        else:
            d[nameList[pos]] = 0
    return nameList

