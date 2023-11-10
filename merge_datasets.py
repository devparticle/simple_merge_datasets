import os
import shutil
from PIL import Image

def merge_dir(source_paths, dest_path):
  if not os.path.exists(dest_path):
    os.makedirs(dest_path)

  for source in source_paths:
    for image in os.listdir(source):
      if file.endswith(".jpg") or file.endswith(".png"):
        shutil.copyfile(os.path.join(source, file), os.path.join(dest_path, file))

def rename(dest_path, new_dir_name):
  for i, file in enumerate(os.listdir(dest_path)):
    if file.endswith(".jpg") or file.endswith(".png"):
      file_new = f"{new_dir}_{0 + i}.jpg"
      os.rename(os.path.join(dest_path, file), os.path.join(dest_path, file_new))

if __name__ == "__main__":
  source_paths = ["dir1", "dir2", "dir3"]

  dest_path = "merged_dir"

  merge_dir(source_paths, dest_path)

  rename(dest_path, new_dir_name)
