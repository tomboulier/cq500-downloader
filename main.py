import argparse

from src.cq500downloader.domain.usecases.download import download_dataset


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
