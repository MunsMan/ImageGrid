# ImageGrid

A small Command Line Application to split an Image into a Grids. There are many possible configurations, how to split an Image.

The goal is, to not relay on single use Apps from the App Store or to even pay for any. This application finish the job in style on a simple CLI Program

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
