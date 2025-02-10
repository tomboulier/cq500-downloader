import os
import subprocess
from pathlib import Path
from typing import Optional


def download_cq500(destination: str = "cq500") -> None:
    """
    Downloads the CQ500 dataset using wget or aria2.

    Parameters
    ----------
    destination : str, optional
        Directory where the dataset will be downloaded, by default "cq500"
    """
    url_list = "http://headctstudy.qure.ai/static/cq500_files.txt"
    os.makedirs(destination, exist_ok=True)

    cmd = f"wget -i {url_list} -P {destination}"  # Default to wget

    if shutil.which("aria2c"):
        cmd = f"aria2c -x5 -i {url_list} -d {destination}"  # Use aria2 if available

    subprocess.run(cmd, shell=True, check=True)
    print(f"CQ500 dataset downloaded in {destination}")


def main(download: bool = True) -> None:
    """
    Main function to handle dataset download.

    Parameters
    ----------
    download : bool, optional
        Whether to download the dataset, by default True
    """
    data_dir = "cq500"

    if download:
        download_cq500(destination=data_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CQ500 Dataset Downloader")
    parser.add_argument("--download", action="store_true", help="Download the CQ500 dataset")
    args = parser.parse_args()

    main(download=args.download)
