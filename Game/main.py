import pygame, sys
sys.path.insert(1, '/home/ibrahim/Downloads/trialObjectDetection/RealTimeObjectDetectionNew')

from settings import *
from level import Level
from pygame import mixer
# from multiprocessing import Process
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
level = Level(screen)
mixer.init()
mixer.music.load('music.ogg')
mixer.music.set_volume(0.7)
mixer.music.play(-1)

# score = {}
# id = {}

# WORKSPACE_PATH = '/home/ibrahim/Downloads/AnotherObjectDetection/RealTimeObjectDetectionNew/Tensorflow/workspace'
# SCRIPTS_PATH = '/home/ibrahim/Downloads/AnotherObjectDetection/RealTimeObjectDetectionNew/Tensorflow/scripts'
# APIMODEL_PATH = '/home/ibrahim/Downloads/AnotherObjectDetection/RealTimeObjectDetectionNew/Tensorflow/models'
# ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
# IMAGE_PATH = WORKSPACE_PATH+'/images'
# MODEL_PATH = WORKSPACE_PATH+'/models'
# PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
# CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
# CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

# labels = [{'name':'a', 'id':1}, {'name':'two', 'id':2}, {'name':'five', 'id':3}]

# with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
#     for label in labels:
#         f.write('item { \n')
#         f.write('\tname:\'{}\'\n'.format(label['name']))
#         f.write('\tid:{}\n'.format(label['id']))
#         f.write('}\n')

# # !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x {IMAGE_PATH + '/train'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/train.record'}
# # !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x{IMAGE_PATH + '/test'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/test.record'}

# # !cd Tensorflow && git clone https://github.com/tensorflow/models

# CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
# # !mkdir {'Tensorflow/workspace/models/'+CUSTOM_MODEL_NAME}
# # !cp {PRETRAINED_MODEL_PATH+'/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config'} {MODEL_PATH+'/'+CUSTOM_MODEL_NAME}

# import tensorflow as tf
# from object_detection.utils import config_util
# from object_detection.protos import pipeline_pb2
# from google.protobuf import text_format

# CONFIG_PATH = MODEL_PATH+'/'+CUSTOM_MODEL_NAME+'/pipeline.config'
# config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)

# pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
# with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:                                                                                                                                                                                                                     
#     proto_str = f.read()                                                                                                                                                                                                                                          
#     text_format.Merge(proto_str, pipeline_config)  

# pipeline_config.model.ssd.num_classes = 3
# pipeline_config.train_config.batch_size = 4
# pipeline_config.train_config.fine_tune_checkpoint = PRETRAINED_MODEL_PATH+'/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0'
# pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
# pipeline_config.train_input_reader.label_map_path= ANNOTATION_PATH + '/label_map.pbtxt'
# pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/train.record']
# pipeline_config.eval_input_reader[0].label_map_path = ANNOTATION_PATH + '/label_map.pbtxt'
# pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/test.record']

# config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
# with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:                                                                                                                                                                                                                     
#     f.write(config_text)   

# print("""python {}/research/object_detection/model_main_tf2.py --model_dir={}/{} --pipeline_config_path={}/{}/pipeline.config --num_train_steps=5000""".format(APIMODEL_PATH, MODEL_PATH,CUSTOM_MODEL_NAME,MODEL_PATH,CUSTOM_MODEL_NAME))

# import os
# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as viz_utils
# from object_detection.builders import model_builder

# # Load pipeline config and build a detection model
# configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
# detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# # Restore checkpoint
# ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
# ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-9')).expect_partial()

# @tf.function
# def detect_fn(image):
#     image, shapes = detection_model.preprocess(image)
#     prediction_dict = detection_model.predict(image, shapes)
#     detections = detection_model.postprocess(prediction_dict, shapes)
#     return detections

# import cv2 
# import numpy as np

# category_index = label_map_util.create_category_index_from_labelmap(ANNOTATION_PATH+'/label_map.pbtxt')

# # Setup capture
# cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# def det():
#     while True:
#         ret, frame = cap.read()
#         image_np = np.array(frame)
#         input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
#         detections = detect_fn(input_tensor)
        
#         num_detections = int(detections.pop('num_detections'))
#         detections = {key: value[0, :num_detections].numpy()
#                     for key, value in detections.items()}
#         detections['num_detections'] = num_detections

#         # detection_classes should be ints.
#         detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

#         label_id_offset = 1
#         image_np_with_detections = image_np.copy()

#         viz_utils.visualize_boxes_and_labels_on_image_array(
#                     image_np_with_detections,
#                     detections['detection_boxes'],
#                     detections['detection_classes']+label_id_offset,
#                     detections['detection_scores'],
#                     category_index,
#                     use_normalized_coordinates=True,
#                     max_boxes_to_draw=5,
#                     min_score_thresh=.5,
#                     agnostic_mode=False)
        
#         score = detections['detection_scores'][0]
#         id = detections['detection_classes'][0]

#         if(score>=0.6):
#             if(id==0):
#                 pyautogui.press('space')
#             elif(id==1):
#                 pyautogui.press('up')
#             elif(id==2):
#                 pyautogui.press('down')

#         cv2.imshow('object detection',  cv2.resize(image_np_with_detections, (800, 600)))
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#                 cap.release()
#                 break

# det()


while True:
    for event in pygame.event.get():
        # print(det())
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    if(level.gameover):
        level=Level(screen)
    level.run()

    pygame.display.update()
    clock.tick(60)

# p1 = Process(target=det)
# p2 = Process(target=game)
# p1.start()
# p1.join()
# p2.start()
# p2.join()