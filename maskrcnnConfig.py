import numpy
import tensorflow
import mrcnn.config
import mrcnn.utils 
import mrcnn.model
from mrcnn.model import MaskRCNN

class MaskCRNNConfig(mrcnn.config.Config):
    Name = 'coco_pretrained_model_config'
    IMAGES_PER_GPU = 10 