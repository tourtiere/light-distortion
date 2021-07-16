from pyvips.vimage import Image
import pyvips
import sys
from typing import Tuple, List
import re

Point = List[int]
Couple = tuple[Point, Point]


def shepards(image: Image, couples: List[Couple]):

    if (len(couples) == 0):
        return

    index = Image.xyz(image.width, image.height)
    deltas = []
    weights = []

    for p1, p2 in couples:

        diff = index - p2

        distance = (diff[0]**2 + diff[1]**2)
        distance = distance.ifthenelse(distance, 0.1)

        weight = 1 / distance

        delta = [(p2[0] - p1[0]), (p2[1] - p1[1])] * weight * -1

        weights.append(weight)
        deltas.append(delta)

    # add, normalize
    index += sum(deltas) * sum(weights) ** -1

    return image.mapim(index, interpolate=pyvips.Interpolate.new('bicubic'))


if __name__ == "__main__":
    image = Image.new_from_file(sys.argv[1])

    couples = []
    matches = re.findall("(\d+),(\d+) (\d+),(\d+)", sys.argv[3])
    for match in matches:
        couple = [[int(match[0]), int(match[1])],
                  [int(match[2]), int(match[3])]]
        couples.append(couple)

    image = shepards(image, couples)
    image.write_to_file(sys.argv[2])
