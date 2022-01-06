"""
The first step in the seam carving algorithm: computing the energy of an image.

Usage:  python3 energy.py surfer.jpg surfer-energy.png
"""


import sys
from typing import List

from utils import Color, read_image_into_array, write_array_into_image


def energy_at(pixels:list[Color], x:int, y:int) -> int:
    """
    Compute the energy of the image at the given (x, y) position.

    The energy of the pixel is determined by looking at the pixels surrounding
    the requested position. In the case the requested position is at the edge
    of the image, the current position is used whenever a "surrounding position"
    would go out of bounds.

    Params:
    pixels: 2D List of Color objects.
    x: x coordinate of pixel under consideration.
    y: y coordinate of pixel under consideration.

    Return: Energy at the coordinate location. 
    """


    pixelx1 = pixels[max(0, x - 1)][y]
    pixelx2 = pixels[min(len(pixels) - 1, x + 1)][y]
    pixely1 = pixels[x][max(0, y - 1)]
    pixely2 = pixels[x][min(len(pixels[0]) - 1, y + 1)]

    r1x,g1x,b1x = pixelx1.r, pixelx1.g, pixelx1.b
    r2x,g2x,b2x = pixelx2.r, pixelx2.g, pixelx2.b
    r1y,g1y,b1y = pixely1.r, pixely1.g, pixely1.b
    r2y,g2y,b2y = pixely2.r, pixely2.g, pixely2.b

    dx = (r1x - r2x) ** 2 + (b1x - b2x) ** 2 + (g1x - g2x) ** 2
    dy = (r1y - r2y) ** 2 + (b1y - b2y) ** 2 + (g1y - g2y) ** 2


    return dx + dy

def compute_energy(pixels:List[List[Color]], metric:str = 'gradient') -> List[List[int]]:
    """
    Compute the energy of the image at every pixel. Should use the `energy_at`
    function to actually compute the energy at any single position.

    Params:
    pixels: 2D List of Color objects.
    metric: String indicating metric of energy calculation.

    Return: 2D List of numbers, each representing the energy value at the corresponding position.
    """

    energy_data = []

    if metric == 'gradient':

        for i, r in enumerate(pixels):

            energy = []

            for j, _ in enumerate(r):

                energy.append(energy_at(pixels, i, j))

            energy_data.append(energy)

    return energy_data


def energy_data_to_colors(energy_data:List[List[int]]) -> List[List[Color]]:
    """
    Convert the energy values at each pixel into colors that can be used to
    visualize the energy of the image. The steps to do this conversion are:

      1. Normalize the energy values to be between 0 and 255.
      2. Convert these values into grayscale colors, where the RGB values are
         all the same for a single color.

    Params:
    energy_data: 2D List of integer energy values at coordinate locations.

    Return: 2D List of Color objects as calculated.
    """

    colors = [[0 for _ in row] for row in energy_data]

    max_energy = max(
        energy 
        for row in energy_data 
        for energy in row
    )

    for y, row in enumerate(energy_data):
        for x, energy in enumerate(row):
            energy_normalized = round(energy / max_energy * 255)
            colors[y][x] = Color(
                energy_normalized,
                energy_normalized,
                energy_normalized
            )

    return colors


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'USAGE: {__file__} <input> <output>')
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(f'images/{input_filename}')

    print('Computing the energy...')
    energy_data = compute_energy(pixels)
    energy_pixels = energy_data_to_colors(energy_data)

    print(f'Saving {output_filename}')
    write_array_into_image(energy_pixels, output_filename)
