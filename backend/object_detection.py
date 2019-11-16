from imageai.Detection import ObjectDetection
import os


def detect_objects(image_path):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(
        os.path.join(execution_path, "./resnet50_coco_best_v2.0.1.h5")
    )
    detector.loadModel()

    # custom_objects = detector.CustomObjects(couch=True);
    custom_objects = detector.CustomObjects(
        bicycle=True,
        car=True,
        motorcycle=True,
        truck=True,
        skis=True,
        snowboard=True,
        skateboard=True,
        surfboard=True,
        tennis_racket=True,
        bottle=True,
        wine_glass=True,
        cup=True,
        fork=True,
        knife=True,
        spoon=True,
        bowl=True,
        chair=True,
        couch=True,
        potted_plant=True,
        bed=True,
        dining_table=True,
        tv=True,
        laptop=True,
        mouse=True,
        remote=True,
        keyboard=True,
        cell_phone=True,
        microwave=True,
        oven=True,
        toaster=True,
        sink=True,
        refrigerator=True,
        book=True,
        clock=True,
        vase=True,
        scissors=True,
        teddy_bear=True,
        hair_dryer=True,
    )

    detections, objects_path = detector.detectCustomObjectsFromImage(
        custom_objects=custom_objects,
        input_image=os.path.join(execution_path, image_path),
        output_image_path=os.path.join(execution_path, "imagenew.jpg"),
        minimum_percentage_probability=30,
        extract_detected_objects=True,
    )

    file_paths = []
    for _eachObject, eachObjectPath in zip(detections, objects_path):
        # print(
        #     eachObject["name"],
        #     " : ",
        #     eachObject["percentage_probability"],
        #     " : ",
        #     eachObject["box_points"],
        # )
        # print("Object's image saved in " + eachObjectPath)
        file_paths.append(eachObjectPath)
        # print("--------------------------------")

    return file_paths
