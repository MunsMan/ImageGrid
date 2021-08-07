[![Build](https://github.com/MunsMan/ImageGrid/actions/workflows/build_test.yml/badge.svg?branch=main)](https://github.com/MunsMan/ImageGrid/actions/workflows/build_test.yml)

# ImageGrid

A small Command Line Application to split an Image into a Grids. There are many possible configurations, how to split an Image.

The goal is, to not relay on single use Apps from the App Store or to even pay for any. This application finish the job in style off a simple CLI Program.

## Example

The goal is, to split the following Image into a Row of 3

![Original Image](https://github.com/MunsMan/ImageGrid/blob/Images/img/DSC08314-Pano.jpg)

`grid <Image> -r 3` or `grid <Image> --row 3`

Image 0x0 | Image 0x1 | Image 0x2
:--------:|:---------:|:---------:
![Split1](https://github.com/MunsMan/ImageGrid/blob/Images/img/DSC08314-Pano_0x0.jpg) | ![Split2](https://github.com/MunsMan/ImageGrid/blob/Images/img/DSC08314-Pano_0x1.jpg) | ![Split3](https://github.com/MunsMan/ImageGrid/blob/Images/img/DSC08314-Pano_0x2.jpg)

## Setup

1. Clone the Repo
2. Enter the Repo
3. `python3 setup.py install`
4. `cd .. & rm -rf ImageGrid`
5. `grid`

### Uninstall

1. `pip3 uninstall ImageGrid`

## Commands

`grid [OPTIONS] IMAGE`

**IMAGE** - is the path to the Image from which the Grid should be created

### Options

- `-r` or `--row` - Number of Images the in a Row of the Grid.
- `-c` or `--column` - Number of Images the in a Column of the Grid.

## Request

If any functionality is missing, create a Issue and request the feature.
