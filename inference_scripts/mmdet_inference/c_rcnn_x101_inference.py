from det_frameworks.mmdetection.mmdet.apis import init_detector, inference_detector, show_result

config_file = 'det_frameworks/mmdetection/configs/cascade_rcnn_x101_64x4d_fpn_1x.py'
checkpoint_file = 'det_frameworks/mmdetection/checkpoints/cascade_rcnn_x101_64x4d/' \
                  'cascade_rcnn_x101_64x4d_fpn_2x_20181218-5add321e.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = 'test_images/1.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
show_result(img, result, model.CLASSES)

# # test a list of images and write the results to image files
# imgs = ['test1.jpg', 'test2.jpg']
# for i, result in enumerate(inference_detector(model, imgs)):
#     show_result(imgs[i], result, model.CLASSES, out_file='result_{}.jpg'.format(i))

# https://stackoverflow.com/questions/56690223/ubuntu-18-04-lts-install-cocoapi/56722306#56722306
