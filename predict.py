from Utils.models import build_generator, build_discriminator
from Utils.image_preprocessing import plotAndSaveVoxel
import numpy as np
import os

def predict():

    batch_size = 1
    z_size = 200

    # Create models
    generator = build_generator()
    discriminator = build_discriminator()

    # Load model weights
    generator.load_weights(os.path.join("generated", "generator_weights.h5"))
    discriminator.load_weights(os.path.join("generated", "discriminator_weights.h5"))

    # Generate 3D images
    z_sample = np.random.normal(0, 0.33, size=[batch_size, 1, 1, 1, z_size]).astype(np.float32)
    generated_volumes = generator.predict(z_sample, verbose=3)

    i = 1
    for generated_volume in generated_volumes:
        voxels = np.squeeze(generated_volume)
        print(voxels.shape)
        plotAndSaveVoxel("generated-images/img_{}".format(i), voxels)
        i+=1


predict()
