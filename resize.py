"""
Usage:	python resize.py andaman.jpg 3500 5500 andaman_resized.png True
"""

import sys
from time import time_ns
import numpy as np
from typing import List


from carve import remove_n_seams
from utils import Color, read_image_into_array, write_array_into_image
from video_stitch import make_video


def resize(image:List[List[Color]], target_dims:tuple[int,int], filename:str) -> List[List[Color]]:

	"""
	Liquid Rescales an image into specified dimentions. Input dimensions should not be smaller than target dimensions.

	Params:
	image: An image in List[List[Color]] format.
	target_dims: Target dimensions of the image, as a tuple of integers.

	Return: Resized image in List[List[Color]] format. 
	"""

	h = len(image)
	w = len(image[0])

	seams_vert = w - target_dims[0]
	seams_horiz = h - target_dims[1]

	print(f'Vertical Seams to be reduced: {seams_vert}')
	print(f'Horizontal Seams to be reduced: {seams_horiz}')

	resized = remove_n_seams(image = image,
							num_seams_to_remove = seams_vert,
							filename = filename,
							orientation = 'vertical')
	print(f'Vertical seams reduced. New shape: ({len(resized)},{len(resized[0])}). Saving {filename}_intermediate.png...')
	write_array_into_image(resized, f'out/{filename}_intermediate.png')
	resized = remove_n_seams(image = image,
							num_seams_to_remove = seams_horiz,
							filename = filename,
							orientation = 'horizontal')
	print(f'Horizontal seams reduced. New shape: ({len(resized)},{len(resized[0])}).')

	return resized

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f'USAGE: {__file__} <input> <target height> <target width>  <generate video (True/False)>')
        sys.exit(1)

    input_filename = sys.argv[1]
    target_height = int(sys.argv[2])
    target_width = int(sys.argv[3])
    video = eval(sys.argv[4])
    filename = input_filename[:-4]
    output_filename = filename + '_resized.png'

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(f'images/{input_filename}')

    print(f'Resizing...')
    resized = resize(pixels, (target_width,target_height), filename)

    print(f'Saving {output_filename}...')
    write_array_into_image(resized, f'out/{output_filename}')

    if video:
        print('Generating Video...')
        make_video(input_dir = 'visual_out',
                    out_format = 'mp4',
                    filename = filename,
                    fps = 10)
    
    print('Complete.')