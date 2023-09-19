# This is a script for converting BrightField image into DarkField image
# Import packages
import time
from tifffile import imread, imsave
from multiprocessing import Pool
import numpy as np
import os
import argparse


# ---------------------------------------- Please do not change the code below ----------------------------------------

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def invert_img(file_name, img: np.array, output_path):
    print(f'Processing: {file_name}')
    inv_img = np.invert(imread(img), dtype='uint16')
    imsave(os.path.join(output_path, rf"{file_name.replace('.tif', '')}_invert.tif"), inv_img)


def create_output_folder(dir_for_output):
    if not os.path.isdir(dir_for_output):
        os.makedirs(dir_for_output)
    else:
        return


# --------------------------------------- Argparse, initialize parser ---------------------------------------
parser = argparse.ArgumentParser(
    description="The script for converting BrightField image into DarkField image")

# Add args
parser.add_argument("input_dir",
                    help="Home directory of your TIFF folder.",
                    type=dir_path)
parser.add_argument("output_dir",
                    help="Directory of your output folder.",
                    type=dir_path)
parser.add_argument("prefix",
                    help="The name of your child folder."
                         "\nex. pos",
                    type=str)
parser.add_argument("suffix_start",
                    help=("Start number of your child folder."
                          "\nex. for pos11 - pos15, enter 11"),
                    type=int)
parser.add_argument("suffix_stop",
                    help=("Stop number of your child folder."
                          "\nex. for pos11 - pos15, enter 15"),
                    type=int)

parser.add_argument("n_cpu",
                    help="CPU number you’d like to use for parallel running the script",
                    type=int)

# Compile args
args = parser.parse_args()

# Assign args into variables
input_dir = args.input_dir
output_dir = args.output_dir
child_folder_prefix = args.prefix
child_folder_suffix_start = args.suffix_start
child_folder_suffix_stop = args.suffix_stop
n_cpu = args.n_cpu

# --------------------------------------- Processing ---------------------------------------
child_folder_name = [f'{child_folder_prefix}{num}' for num in
                     range(child_folder_suffix_start, child_folder_suffix_stop + 1)]

for folder_name in child_folder_name:
    input_folder = os.path.join(input_dir, folder_name)
    output_folder = os.path.join(output_dir, folder_name)

    # Create folder for output directory
    create_output_folder(output_folder)

    # list input file name, file path (np.array) and output path (directory)
    file_lst = [(os.path.basename(arr), arr, output_folder) for arr in
                (os.path.join(input_folder, file) for file in os.listdir(input_folder))]

    if __name__ == '__main__':
        print(f'----------------------------- Start processing folder: {folder_name} ---------------------------------')
        # Start timer
        start_time = time.perf_counter()
        with Pool(n_cpu) as pool:
            results = pool.starmap(invert_img, file_lst)
            # End timing
            finish_time = time.perf_counter()

            print(f'Programed finished for: {folder_name}\n'
                  f'It takes {round(finish_time - start_time)} seconds')
