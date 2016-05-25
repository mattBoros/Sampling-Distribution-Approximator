import os


def join(*args):
    current_path = args[0]
    for path in args[1:]:
        current_path = os.path.join(current_path, path)
    return current_path


def get_parent_dir(path):
    return os.path.dirname(path)


base_path = __file__
for i in range(3):
    base_path = get_parent_dir(base_path)


population_distribution = join(base_path, 'distribution.png')

stack_heights = join(base_path, 'temp', 'stackHeights.txt')

jar = join(base_path, 'source', 'java', 'sampling_distribution_stack_saver.jar')

sampling_distribution_folder = join(base_path, 'sampling_distribution_images')

print(population_distribution)
print(stack_heights)
print(jar)
print(sampling_distribution_folder)
