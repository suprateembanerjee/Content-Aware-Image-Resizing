"""
The third and final step in the seam carving process: removing the lowest-energy
seam from an image. By doing so iteratively, the size of the image can be
reduced (in one dimension) by multiple pixels.

Usage:    python3 carve.py surfer.jpg 10 surfer-resized.png False
"""


import sys
from typing import List
from statistics import mean
from time import time_ns
import numpy as np

from energy import compute_energy
from seam import compute_seam, visualize_seam
from utils import Color, read_image_into_array, write_array_into_image
from video_stitch import make_video


def remove_seam(image:List[List[Color]], seam_xs:list[int]) -> List[List[Color]]:
    """
    Remove pixels from the given image, as indicated by each of the
    x-coordinates in the input. The x-coordinates are specified from top to
    bottom and span the entire height of the image.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    one element in each row, but will have the same number of rows.
    """

    cropped = []

    for i, row in enumerate(image):
        row.pop(seam_xs[i])
        cropped.append(row)

    return cropped



def remove_n_seams(image:List[List[Color]], num_seams_to_remove:int, filename:str, orientation:str = 'vertical') -> List[List[Color]]:
    """
    Iteratively:

    1. Find the lowest-energy seam in the image.
    2. Remove that seam from the image.

    Repeat this process `num_seams_to_remove` times, so that the resulting image
    has that many pixels removed in each row.

    While not necessary, you may want to save the intermediate images in the
    process, in case you want to see how the image gets progressively smaller.
    The `visualize_seam_on_image` is available if you want to visualize the
    lowest-energy seam at each step of the process.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    `num_seams_to_remove` elements in each row, but will have the same number of
    rows.
    """

    times = []

    if orientation[0] == 'h':
        image = list(map(list, zip(*image[::-1])))



    for i in range(num_seams_to_remove):

        t1 = time_ns()
        energy_data = compute_energy(image)
        seam, _ = compute_seam(energy_data)
        visualized_pixels = visualize_seam(image, seam)
        image = remove_seam(image, seam)
        times.append(time_ns() - t1)
  
        if orientation[0] == 'h':
            visualized_pixels = list(map(list, zip(*visualized_pixels)))[::-1]

        write_array_into_image(visualized_pixels, f'visual_out/{orientation}/{filename}_{i}.png')

    print(f'Average time taken per seam: {mean(times)/10**9:.2f}s')

    if orientation[0] == 'h':
        image = list(map(list, zip(*image)))[::-1]

    return image

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f'USAGE: {__file__} <input> <num-seams-to-remove> <output> <generate video (True/False)>')
        sys.exit(1)

    input_filename = sys.argv[1]
    num_seams_to_remove = int(sys.argv[2])
    output_filename = sys.argv[3]
    video = eval(sys.argv[4])

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(f'images/{input_filename}')

    print(f'Resizing...')
    resized_pixels = remove_n_seams(image = pixels,
                                    num_seams_to_remove = num_seams_to_remove,
                                    filename = input_filename[:-3])

    print(f'Saving {output_filename}...')
    write_array_into_image(resized_pixels, output_filename)

    if video:
        print('Generating Video...')
        make_video(input_dir = 'visual_out',
                    out = 'result.mp4',
                    filename = input_filename[:-3],
                    fps = 10)
    
    print('Complete')
