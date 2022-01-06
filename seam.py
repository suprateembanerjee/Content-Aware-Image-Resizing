"""
An implementation of the second step in the seam carving algorithm: finding
the lowest-energy seam in an image. In this version of the algorithm, not only
is the energy value of the seam determined, but it's possible to reconstruct the
entire seam from the top to the bottom of the image.

Isolated Usage:    python3 seam.py surfer.jpg surfer-seam-energy.png
"""


import sys
from typing import List

from energy import compute_energy
from utils import Color, read_image_into_array, write_array_into_image


class SeamEnergyWithBackPointer:
    """
    Represents the total energy of a seam along with a back pointer:

      - Stores the total energy of a seam that ends at some position in the
        image. The position is not stored because it can be inferred from where
        in a 2D grid this object appears.

      - Also stores the x-coordinate for the pixel in the previous row that led
        to this particular seam energy. This is the back pointer from which the
        entire seam can be reconstructed.

    """

    total_energy = 0
    prev_x = 0

    def __init__(self, total_energy:int, prev_x:int, total_width:int) -> None:

        self.total_energy = total_energy
        if prev_x:
            self.prev_x = min(max(0, prev_x), total_width)
        else:
            self.prev_x = prev_x

    def __repr__(self) -> str:

        return f'Energy: {self.total_energy} Previous x: {self.prev_x}'

    def __gt__(self, other) -> bool:
        return self.total_energy > other.total_energy


def compute_seam(energy_data: List[List[int]]) -> tuple[list[int],int]:
    """
    Find the lowest-energy vertical seam given the energy of each pixel in the
    input image. The image energy should have been computed before by the
    `compute_energy` function in the `energy` module.

    This is the second version of the seam finding algorithm. In addition to
    storing and finding the lowest-energy value of any seam, you will also store
    back pointers used to reconstruct the lowest-energy seam.

    At the end, you will return a list of x-coordinates where you would have
    returned a single x-coordinate instead.

    This is one of the functions you will need to implement. You may want to
    copy over the implementation of the first version as a starting point.
    Expected return value: a tuple with two values:

      1. The list of x-coordinates forming the lowest-energy seam, starting at
         the top of the image.
      2. The total energy of that seam.
    """

    M = []

    for i, row in enumerate(energy_data):
        m = []

        for j, energy in enumerate(row):

            if i == 0:
                m.append(SeamEnergyWithBackPointer(energy, None, len(row)))

            else:
                choices = []
                choices.append(M[-1][max(j - 1, 0)].total_energy)
                choices.append(M[-1][j].total_energy)
                choices.append(M[-1][min(j + 1, len(row) - 1)].total_energy)

                choice = choices.index(min(choices))

                m.append(SeamEnergyWithBackPointer(energy + choices[choice], j + choice - 1, len(row)))

        M.append(m)


    seam_head = M[-1].index(min(M[-1]))
    seam = []
    energy = min(M[-1])

    while(M[-1][seam_head].prev_x != None):
        seam.append(seam_head)
        prev_x = M[-1][seam_head].prev_x
        M = M[:-1]
        seam_head = prev_x

    seam.append(seam_head)
    seam = list(reversed(seam))

    return seam, energy


def visualize_seam(pixels: List[List[Color]], seam: list[int]) -> List[List[Color]]:
    """
    Draws a red line on the image along the given seam. This is done to
    visualize where the seam is.

    """

    h = len(pixels)
    w = len(pixels[0])

    new_pixels = [[p for p in row] for row in pixels]

    for y, x in enumerate(seam):
        min_x = max(x - 2, 0)
        max_x = min(x + 2, w - 1)

        for i in range(min_x, max_x + 1):
            new_pixels[y][i] = Color(255, 0, 0)

    return new_pixels


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'USAGE: {__file__} <input> <output>')
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(input_filename)

    print('Computing the energy...')
    energy_data = compute_energy(pixels)

    print('Finding the lowest-energy seam...')
    seam_xs, min_seam_energy = compute_vertical_seam_v2(energy_data)

    print(f'Saving {output_filename}')
    visualized_pixels = visualize_vert_seam(pixels, seam_xs)
    write_array_into_image(visualized_pixels, output_filename)

    print()
    print(f'Minimum seam energy was {min_seam_energy} at x = {seam_xs[-1]}')
