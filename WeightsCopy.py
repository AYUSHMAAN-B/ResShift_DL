import shutil

# Define the source path (input directory) and destination path (output directory)
source_path = '/kaggle/input/weights/autoencoder_vq_f4.pth'
destination_path = '/kaggle/working/weights/autoencoder_vq_f4.pth'

# Create the directory in the output path if it doesn't exist
output_dir = '/kaggle/working/weights'
os.makedirs(output_dir, exist_ok=True)

# Copy the file from input to output
shutil.copy(source_path, destination_path)

print("File copied successfully!")
