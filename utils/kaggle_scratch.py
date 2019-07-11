# For running inference on the TF-Hub module.
import tensorflow as tf
from model.base_model import BaseModel
from utils.json_crud import JsonCRUD

from PIL import Image
from PIL import ImageOps

import glob
import io
import os
from tqdm import tqdm

# Check available GPU devices.
print("The following GPU devices are available: %s" % tf.test.gpu_device_name())


def image_list_generator(img_dir):
    images = glob.glob(img_dir + "/*")
    return images


def convert_predictions(prediction_dict):
    prediction_dict = prediction_dict[0]
    prediction_string = ""
    prediction_string_list = []
    for i in range(len(prediction_dict["detection_scores"])):
        prediction_string += prediction_dict["detection_class_names"][i].decode("utf-8") + " "\
                             + str(prediction_dict["detection_scores"][i]) + " "\
                             + " ".join(str(coord) for coord in prediction_dict["detection_boxes"][i])
        prediction_string_list.append(prediction_string)

    prediction_string_complete = " ".join(pred_string for pred_string in prediction_string_list)
    return prediction_string_complete


def image_feeder(image_path, new_width=256, new_height=256, display=False):
    pil_image = Image.open(image_path)
    resized_pil = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)
    rgb_converted = resized_pil.convert("RGB")
    # TODO send back bytes image value
    img_byte_array = io.BytesIO()
    rgb_converted.save(img_byte_array, format='PNG')
    if display:
        print("implement display image not implemented now")
    return img_byte_array.getvalue()


def run_model_inference(image_list):
    images_count = 0
    prediction_dict = dict()

    model = BaseModel()
    session, image_string_input, model_input_image, model_output = model.create_session()

    for image in tqdm(image_list):
        image_id = os.path.basename(image)[:-4]
        img_byte = image_feeder(image, new_width=1280, new_height=856)

        with tf.Graph().as_default():
            prediction = session.run([model_output], feed_dict={image_string_input: img_byte})

        pred_string = convert_predictions(prediction)
        prediction_dict[image_id] = pred_string
        images_count += 1

    return prediction_dict


IMAGE_ROOT_DIR = "/media/mash-compute/mWm_drive_00/dataset/kaggle_open_image/unzipped"

JSON_PATH = "/media/breakthrough/plnarData/universe/dataset/openSourced/" \
            "google_openImage/kaggle/kaggle-open-image/save_file.json"

SUBMISSION_FILE = "/media/breakthrough/plnarData/universe/dataset/openSourced/" \
                  "google_openImage/submissions/sample_submission.csv"

if __name__ == "__main__":
    # generate list of images in the root image directory for the inference
    root_images = image_list_generator(IMAGE_ROOT_DIR)
    # run model inference with the list of images path generated above
    pred_dict = run_model_inference(root_images)
    json_ops = JsonCRUD().save_dict_to_json(pred_dict)

