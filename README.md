# Image LUT Inversion Parallel
*The project is built for converting bright field microscopy images into dark field microscopy images (with wilti-processing)*

This step-by-step tutorial is built for Windows and relies on Python as the interpreter. 

Note:
1. The designed structure of data for conversion for this project is:
<img width="313" alt="image" src="https://github.com/derKakadu0714/Image-LUT-Inversion-Parallel/assets/103349391/7aade2b8-deed-4633-8820-f308e0f5ee82">


2. The tiff file must be 16 bits!

## Pre-requirement
1. [Python](https://www.python.org/)
2. [Anaconda Distribution](https://www.anaconda.com/download)
3. [The custom script (This page)](https://github.com/derKakadu0714/Image-LUT-Inversion-Parallel)
4. Create a project (folder) for the repo.

## Installation
1. Open the Anaconda PowerShell Prompt
2. ```cd your project folder```
3. Create a new conda environment and install scikit-image
4. ```conda create --name inversion python=3.11```
5. ```conda activate inversion```
6. ```conda install scikit-image```
   
Installation success!


## Command line usage
Entering:
```python main.py -h```

<img width="636" alt="image" src="https://github.com/derKakadu0714/Image-LUT-Inversion-Parallel/assets/103349391/6bb4d7fc-0a5c-4573-85d3-45f9780a50bc">

As shown, all of the ‘positional arguments' are the arguments required for the usage, see explaination below. 

**input_dir:** The home directory of your data (TIFF file), which is the directory before the child folder (child folder = ‘pos’ folder)

**output_dir:** The directory you’d like to save your data. Notice that there is no need to create ‘child folder (pos0… )’ again by yourself

**prefix:** The ‘name’ of your child folder. Ex. pos

**suffix_start:** Start number for your child folder, Take pos11-pos15 for instance, enter 11

**suffix_stop:** Stop number for your child folder, Take pos11-pos15 for instance, enter 15

**n_cpu:** CPU number you’d like to use for parallel running the script

### To run the script
Now, to run and use the script in shell, the arguments will have to be listed "positionally" and separated by blank, which means, those arguments should be listed by the order of: 

**input_dir output_dir prefix suffix_start suffix_stop n_cpu**

So, the command will now be

```python main.py input_dir output_dir prefix suffix_start suffix_stop n_cpu```

Example:
For the data with child folder pos0 to pos5

<img width="1334" alt="image" src="https://github.com/derKakadu0714/Image-LUT-Inversion-Parallel/assets/103349391/5b6d249e-a4cb-43e0-ae2d-6e992cab8fd3">
<img width="1352" alt="image" src="https://github.com/derKakadu0714/Image-LUT-Inversion-Parallel/assets/103349391/206ffb88-4bcf-48e7-823e-2e2dff8acdee">

And the script has run successfully!
