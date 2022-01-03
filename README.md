Content-aware image resizing
============================================================

There are four steps in the implementation:

| Step | Exercise file | Description                                |
|------|---------------|--------------------------------------------|
| 1    | `energy.py`   | Energy calculation                         |
| 2    | `seam_v1.py`  | Finding the lowest-energy seam (version 1) |
| 3    | `seam_v2.py`  | Finding the lowest-energy seam (version 2) |
| 4    | `carve.py`    | Removing seams from the image              |

Each step is documented at the top of the files.

Setup
-----

1. Ensure you have Python 3 installed. I'm a fan of [pyenv](https://github.com/pyenv/pyenv), but you can install the latest version of Python in any way you wish.

1. Install the dependencies using `pip`: `pip install -r requirements.txt`

Run the files in terminal using descriptions at the beginning of each file.

For a one-shot test, run carve using `python carve.py surfer.jpg 100 surfer_resized.png`

Image credits
-------------

All images are free to redistribute. Attribution is not necessary, but encouraged:

- Surfer - [Kiril Dobrev](https://pixabay.com/users/kirildobrev-12266114/) on [Pixabay](https://pixabay.com/photos/blue-beach-surf-travel-surfer-4145659/)

- Arch - [Mike Goad](https://www.flickr.com/photos/exit78/) on [Flickr](https://flic.kr/p/4hxxz5)
