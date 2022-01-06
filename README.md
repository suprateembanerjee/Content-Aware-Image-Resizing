Context-Aware Image Resizing (Liquid Rescaling)
============================================================

There are four steps in the implementation:

| Step | Exercise file    | Description                                |
|------|------------------|--------------------------------------------|
| 1    | `energy.py`      | Energy calculation                         |
| 2    | `seam.py`        | Finding the lowest-energy seam             |
| 3    | `carve.py`       | Removing seams from the image              |
| 4    | `resize.py`      | Resizing an image to given dimensions      |
| 5    | `video_stitch.py`| Stitching visualized frames to make a video|


Each step is documented at the top of the exercise file.

Setup
-----

1. Ensure you have Python 3 installed. I'm a fan of [pyenv](https://github.com/pyenv/pyenv), but you can install the latest version of Python in any way you wish.

1. Install the dependencies using `pip`: `pip install -r requirements.txt`

Run the files in terminal using descriptions at the beginning of each file.

For a one-shot test, run carve using `python resize.py andaman.jpg 1300 2000 True`

File Format
---------
Images are stored inside the **images** directory, in *jpg* format.

Outputs such as videos, intermediate and final images are stored in the **out** directory in *mp4* and *png* format respectively. Videos are titled similarly to the input image, with "\_result" suffixed, while images are suffixed with "\_intermediate" and "\_resized" to indicate the intermediate and final output.

Visualized seams are stored in the **visual_out** directory. Two subdirectories titled **vertical** and **horizontal** contain vertical reductions and horizontal reductions respectively. The frames are titled similarly to the input images with "\_x" suffixed where x denotes number of reduction, in *png* format. These are used to construct the video output at the end, if indicated so while operating **resize.py**.


Image credits
-------------

All images are free to redistribute. Attribution is not necessary, but encouraged:

- Seatree - [Suprateem Banerjee](https://www.instagram.com/dolphinextreme48/) on [Blues Photo Journal](www.tinyurl.com/blues-photobook)

- Andaman - [Suprateem Banerjee](https://www.instagram.com/dolphinextreme48/) from Personal Collection

- Surfer - [Kiril Dobrev](https://pixabay.com/users/kirildobrev-12266114/) on [Pixabay](https://pixabay.com/photos/blue-beach-surf-travel-surfer-4145659/)

- Arch - [Mike Goad](https://www.flickr.com/photos/exit78/) on [Flickr](https://flic.kr/p/4hxxz5)
