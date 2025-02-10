import os
import subprocess
from pathlib import Path
from typing import Optional
import shutil
import argparse


def download_cq500(destination: str = "cq500") -> None:
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


def convert_to_nifti(source: str, destination: str) -> None:
    """
    Converts the downloaded files to NIfTI format.

    Parameters
    ----------
    source : str
        Directory where the downloaded files are located
    destination : str
        Directory where the converted files will be saved
    """
    os.makedirs(destination, exist_ok=True)
    # Placeholder for conversion logic
    print(f"Converting files from {source} to NIfTI format in {destination}")
    # Implement conversion logic here


def preprocess_data(source: str, destination: str) -> None:
    """
    Preprocesses the NIfTI files.

    Parameters
    ----------
    source : str
        Directory where the NIfTI files are located
    destination : str
        Directory where the preprocessed files will be saved
    """
    os.makedirs(destination, exist_ok=True)
    # Placeholder for preprocessing logic
    print(f"Preprocessing NIfTI files from {source} to {destination}")
    # Implement preprocessing logic here


def cli() -> None:
    """
    Command-line interface for the CQ500 dataset downloader.
    """
    data_dir = "cq500"
    nifti_dir = "cq500_nifti"
    preprocessed_dir = "cq500_preprocessed"

    parser = argparse.ArgumentParser(description="CQ500 Dataset Downloader and Processor")
    parser.add_argument("--download", action="store_true", help="Download the CQ500 dataset")
    parser.add_argument("--convert", action="store_true", help="Convert the dataset to NIfTI format")
    parser.add_argument("--preprocess", action="store_true", help="Preprocess the NIfTI files")
    args = parser.parse_args()

    if args.download:
        download_cq500(destination=data_dir)
    if args.convert:
        convert_to_nifti(source=data_dir, destination=nifti_dir)
    if args.preprocess:
        preprocess_data(source=nifti_dir, destination=preprocessed_dir)

    if not any(vars(args).values()):
        parser.print_help()


if __name__ == "__main__":
    cli()
