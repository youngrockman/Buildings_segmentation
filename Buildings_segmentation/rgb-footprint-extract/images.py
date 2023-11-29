import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from pathlib import Path

def convert_image(input_image_path, output_directory):
    # Read the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Get the file name without extension
    file_name = Path(input_image_path).stem

    # Save as npy file
    npy_path = f"{output_directory}\\{file_name}.npy"
    np.save(npy_path, img_array)
    print(f"{npy_path} successfully saved")

    # Save as png file
    png_path = f"{output_directory}\\{file_name}_new.png"
    plt.imsave(png_path, img_array.astype(np.uint8))
    print(f"{png_path} successfully saved")

    # Save secondary npy file
    secondary_npy_path = f"{output_directory}\\{file_name}_new.npy"
    np.save(secondary_npy_path, img_array)
    print(f"{secondary_npy_path} successfully saved")

    # Save secondary png file
    secondary_png_path = f"{output_directory}\\{file_name}_new.png"
    plt.imsave(secondary_png_path, img_array.astype(np.uint8))
    print(f"{secondary_png_path} successfully saved")

# Example usage
input_image_path = r"C:\pythonProject1test\rgb-footprint-extract\images"
output_directory = r"C:\pythonProject1test\rgb-footprint-extract\npy images"
convert_image(input_image_path, output_directory)
