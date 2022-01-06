import cv2
import glob
import os
from typing import List
import numpy

def get_images(input_dir:str, filename:str) -> List[numpy.ndarray]:

	"""
	Collects images from directory and returns an array of images to work with.

	Params:
	input_dir: Directory where two folders titled 'vertical' and 'horizontal' are expected, containing images.

	Return: A List of images.
	"""

	images = [cv2.imread(f'images/{filename}.jpg')]

	for imagefile in sorted(glob.glob(f'{input_dir}/vertical/{filename}_*.png'), key=os.path.getmtime):
		image = cv2.imread(imagefile)
		pad = images[0].shape[1] - image.shape[1]
		image = cv2.copyMakeBorder(image, 0, 0, 0, pad, cv2.BORDER_CONSTANT, None, 0)
		images.append(image)

	for imagefile in sorted(glob.glob(f'{input_dir}/horizontal/{filename}_*.png'), key=os.path.getmtime):
		image = cv2.imread(imagefile)
		pad_t = images[0].shape[0] - image.shape[0]
		pad_l = images[0].shape[1] - image.shape[1]
		image = cv2.copyMakeBorder(image, pad_t, 0, 0, pad_l, cv2.BORDER_CONSTANT, None, 0)
		images.append(image)

	image = cv2.imread(f'out/{filename}_resized.png')
	pad_t = images[0].shape[0] - image.shape[0]
	pad_l = images[0].shape[1] - image.shape[1]
	image = cv2.copyMakeBorder(image, pad_t, 0, 0, pad_l, cv2.BORDER_CONSTANT, None, 0)
	images.append(image)

	return images



def make_video(input_dir:str = 'visual_out', out_format:str = 'mp4', filename:str = 'arch', fps:int = 10) -> None:

	"""
	Takes as input the directory in which it expects two folders for vertical and horizontally reduced images, 
	and stitches them into a video.In case of uneven shapes, padding is added appropriately above and to the right 
	of the image frame.

	Params:
	input_dir: Directory where two folders titled 'vertical' and 'horizontal' are to be expected, containing images.
	out: Title of generated video.
	fps: Frames per second for the video indicating speed.
	"""

	images = get_images(input_dir, filename)

	h, w, _ = images[0].shape

	fourcc = cv2.VideoWriter_fourcc(*'mp4v') if out_format == 'mp4' else 0

	video = cv2.VideoWriter(filename = f'out/{filename}_result.{out_format}',
								fourcc = fourcc,
								fps = fps,
								frameSize = (w,h))

	for image in images:
		video.write(image)

	cv2.destroyAllWindows()
	video.release()
	print('Video generated.')

if __name__ == '__main__':
	make_video()