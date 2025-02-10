import os
import logging
from pathlib import Path
from urllib.request import urlretrieve

logger = logging.getLogger(__name__)


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
        try:
            url_patient = f"{url_base}/CQ500-CT-{patient_number}.zip"
            zip_filename = f"{destination}/{base_name}.zip"
            logger.info(f"Downloading {url_patient}...")
            urlretrieve(url=url_patient, filename=zip_filename)
            logger.info(f"File downloaded to {zip_filename}")
        except Exception as error:
            logger.error(f"Error downloading {url_patient}: {error}")
            raise error
