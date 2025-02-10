import os
import logging
from urllib.request import urlretrieve

logger = logging.getLogger(__name__)


def download_dataset(destination: str = "cq500") -> None:
    """
    Downloads the CQ500 dataset using wget or aria2.

    Parameters
    ----------
    destination : str, optional
        Directory where the dataset will be downloaded, by default "cq500"
    """
    url_base = "https://s3.ap-south-1.amazonaws.com/qure.headct.study"
    os.makedirs(destination, exist_ok=True)

    for patient_number in range(491):
        try:
            url_patient = f"{url_base}/CQ500-CT-{patient_number}.zip"
            logger.info(f"Downloading {url_patient}...")
            urlretrieve(url=url_patient, filename=f"{destination}/CQ500-CT-{patient_number}.zip")
            logger.info(f"Downloaded {url_patient}.")
        except Exception as error:
            logger.error(f"Error downloading {url_patient}: {error}")
            raise error
