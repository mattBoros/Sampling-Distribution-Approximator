import os
from save_sampling_distribution_image import save_sampling_distribution_image
import PATHS


for path in os.listdir(PATHS.sampling_distribution_folder):
    abs_path_to_image = os.path.join(PATHS.sampling_distribution_folder, path)
    os.unlink(abs_path_to_image)


for sample_size in range(1, 26):
    print('saving n = {0}'.format(sample_size))
    sample_size_str = '0' + str(sample_size) if sample_size < 10 else str(sample_size)
    path = os.path.join(PATHS.sampling_distribution_folder,
                        'sampling_distribution_n_equals_{0}'.format(sample_size_str)
                        )
    print(path)
    save_sampling_distribution_image(sample_size, path=path)











