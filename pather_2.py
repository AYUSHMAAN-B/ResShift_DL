from utils.util_common import write_path_to_txt

# Define the directory containing your training images and the output text file path
dir_folder = '/kaggle/input/flickrfaceshq-dataset-ffhq'
txt_path = '/kaggle/output/ResShift_DL/files256.txt'
search_key = '*.png'  # or '*.jpg' if only using jpg images

# Create text file with all image paths
write_path_to_txt(dir_folder=dir_folder, txt_path=txt_path, search_key=search_key)
print(f"Text file created at {txt_path}")