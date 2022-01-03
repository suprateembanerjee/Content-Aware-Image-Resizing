import cv2

def make_video(input_dir:str = 'visual_out', out:str = 'result.avi', num_frames:int = 100, fps:int = 10) -> None:

	images = [cv2.imread('surfer.jpg')]

	for i in range(num_frames):
		image = cv2.imread(f'{input_dir}/{i}.png')
		pad = images[0].shape[1] - image.shape[1]
		image = cv2.copyMakeBorder(image, 0, 0, 0, pad, cv2.BORDER_CONSTANT, None, 0)
		images.append(image)

	h, w, _ = images[0].shape

	if out[-3:] == 'mp4':
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		video = cv2.VideoWriter(filename = out, 
								fourcc = fourcc,
								fps = fps,
								frameSize = (w,h))
	else:
		video = cv2.VideoWriter(filename = out,
								fourcc = 0,
								fps = fps,
								frameSize = (w,h))

	for image in images:
		video.write(image)

	cv2.destroyAllWindows()
	video.release()

if __name__ == '__main__':
	make_video()