import os
import zipfile
import logging
from pathlib import Path
from urllib.request import urlretrieve

logger = logging.getLogger(__name__)


def download_patient(patient_number: int, destination_file: Path) -> None:
    """
    Downloads a single patient from the CQ500 dataset.

    Parameters
    ----------
    patient_number : int
        Patient number to download
    destination_file : Path, optional
        Directory where the dataset will be downloaded, by default "cq500"
    """
    url_base = "https://s3.ap-south-1.amazonaws.com/qure.headct.study"
    patient_base_name = f"CQ500-CT-{patient_number}"
    url_patient = f"{url_base}/{patient_base_name}.zip"

    try:
        logger.info(f"Downloading {url_patient}...")
        urlretrieve(url=url_patient, filename=destination_file)
        logger.info(f"File downloaded to {destination_file}")
    except Exception as error:
        logger.error(f"Error downloading {url_patient}: {error}")
        raise error


def unzip_patient(patient_zip_filepath: Path, destination: Path) -> None:
    """
    Unzips a patient file.

    Parameters
    ----------
    patient_zip_filepath : Path
        Path to the patient zip file
    destination : Path
        Directory where the dataset will be downloaded

    Raises
    ------
    FileNotFoundError
        If the patient zip file is not found
    FileNotFoundError
        If the destination directory is not found
    """
    if not patient_zip_filepath.exists():
        raise FileNotFoundError(f"File {patient_zip_filepath} not found")

    if not destination.exists():
        raise FileNotFoundError(f"Destination directory {destination} not found")

    try:
        logger.info(f"Unzipping {patient_zip_filepath}...")
        with zipfile.ZipFile(patient_zip_filepath, "r") as zip_ref:
            zip_ref.extractall(destination)
        logger.info(f"Unzipped {patient_zip_filepath}")
    except Exception as error:
        logger.error(f"Error unzipping {patient_zip_filepath}: {error}")

    os.remove(patient_zip_filepath)


def download_dataset(destination: Path = Path("cq500")) -> None:
    """
    Downloads the CQ500 dataset using wget or aria2.

    Parameters
    ----------
    destination : Path, optional
        Directory where the dataset will be downloaded, by default Path("cq500")
    """
    url_base = "https://s3.ap-south-1.amazonaws.com/qure.headct.study"
    os.makedirs(destination, exist_ok=True)

    for patient_number in range(491):
        base_name = f"CQ500-CT-{patient_number}"
        patient_zip_filepath = Path(f"{destination}/{base_name}.zip")
        download_patient(patient_number, patient_zip_filepath)
        unzip_patient(patient_zip_filepath, destination)
