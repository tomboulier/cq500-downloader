import os
import subprocess
from pathlib import Path
from typing import Optional
import shutil
import argparse


def download_dataset(destination: str = "cq500") -> None:
    """
    Downloads the CQ500 dataset using wget or aria2.

    Parameters
    ----------
    destination : str, optional
        Directory where the dataset will be downloaded, by default "cq500"
    """
    url_list = "http://15.206.3.216/static/cq500_files.txt"
    os.makedirs(destination, exist_ok=True)

    cmd = f"wget -c -i {url_list} -P {destination}"  # Default to wget with resume support

    if shutil.which("aria2c"):
        cmd = f"aria2c -x5 -c -i {url_list} -d {destination}"  # Use aria2 if available with resume support

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"CQ500 dataset downloaded in {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")


def cli() -> None:
    """
    Command-line interface for the CQ500 dataset downloader.
    """
    parser = argparse.ArgumentParser(description="CQ500 Dataset Downloader and Processor")
    parser.add_argument("--download", action="store_true", help="Download the CQ500 dataset")
    parser.add_argument("--destination-folder", type=str, default="cq500", help="Destination folder for the dataset")
    args = parser.parse_args()

    if args.download:
        download_dataset(destination=args.destination_folder)
    else:
        parser.print_help()


if __name__ == "__main__":
    cli()
