from opensimplex import OpenSimplex
from enum import Enum
from pprint import  pprint

biomes = {"WATER": " ", "FOREST": "#", "STONE": "x", "SNOW": "_"}

def noise(nx, ny):
    gen = OpenSimplex()
    return gen.noise2d(nx,ny) / 2.0 + 0.5

def generate(width, height):
    value = []
    basefreq = 2.3
    midfreq = 2.5
    topfreq = 4

    for y in range(0,height):
        value.append([0] * width)
        for x in range(0, width):
            nx = x/width - 0.5 
            ny = y/height - 0.5
            n = 1 * noise(basefreq * nx,basefreq * ny) 
            + 0.5 * noise(midfreq * nx, midfreq * ny) 
            + 0.25 * noise(topfreq* nx, topfreq * ny)
            value[y][x] = convertToBiomes(n)
    
    return value


def convertToBiomes(noise):
    if(0 <= noise <= 0.2):
        return biomes["WATER"]
    if(0.2 < noise <= 0.5):
        return biomes["FOREST"]
    if(0.5 < noise <= 0.7):
        return biomes["STONE"]
    if(0.7 < noise <= 1):
        return biomes["SNOW"]


def printMap(values):
    for row in values:
        print()
        for x in row:
            print(x, end=" ")


printMap(generate(40,40))