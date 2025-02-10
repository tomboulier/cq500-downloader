# CQ500 Downloader

## Description

CQ500 Downloader is a Python tool for downloading the 
[CQ500 brain CT scan dataset](https://academictorrents.com/details/47e9d8aab761e75fd0a81982fa62bddf3a173831).
This tool provides a command-line interface to manage the dataset efficiently.

## Features

- Download the CQ500 dataset using `wget` or `aria2`.
- (to be implemented) Convert the downloaded files to NIfTI format.

## Requirements

- Python 3.12 or higher
- `wget` or `aria2` for downloading the dataset

## Installation

Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/cq500-downloader.git
cd cq500-downloader
```

## Usage

```sh
python main.py --download
```

To see the full list of available commands and options, run:

```sh
python main.py --help
```

## License

This project is licensed under the [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).
