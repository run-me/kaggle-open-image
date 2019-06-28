import tensorflow as tf
import tensorflow_hub as hub


class BaseModel:

	def create_session(self):
		module_handle = "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"
		with tf.Graph().as_default():
			# Model handle form tensorflow-hub
			detector = hub.Module(module_handle)

			# input image
			image_string_placeholder = tf.placeholder(tf.string)
			model_input_image = tf.image.decode_jpeg(image_string_placeholder)

			# Module accepts as input tensors of shape [1, height, width, 3], i.e. batch
			# of size 1 and type tf.float32.
			decoded_image_float = tf.image.convert_image_dtype(image=model_input_image, dtype=tf.float32)
			module_input = tf.expand_dims(decoded_image_float, 0)

			# Run model and obtain output
			model_output = detector(module_input, as_dict=True)
			init_ops = [tf.global_variables_initializer(), tf.tables_initializer()]

			session = tf.Session()
			session.run(init_ops)

		return session, image_string_placeholder, model_input_image, model_output
