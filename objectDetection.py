from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd() + '/static/image/'

def objectDetection(inputPath, outputPath, prob):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image = os.path.join(execution_path, inputPath), output_image_path = os.path.join(execution_path, outputPath), minimum_percentage_probability = prob)

    nameList = []
    probList = []
    for eachObject in detections:  
        nameList.append(eachObject["name"])
        probList.append(eachObject["percentage_probability"])
    return nameList, probList

def main():
    inputPath = "static/upload/image.jpg"
    outputPath = "static/upload/imagenew.jpg"
    probability = 80

    objectDetection(inputPath, outputPath, probability)

if __name__ == "__main__":
    main()

