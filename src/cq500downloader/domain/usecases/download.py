import os
import shutil
import subprocess


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
