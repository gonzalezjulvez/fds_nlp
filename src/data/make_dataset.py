# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from types_dataset import types_train


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    PATH_INPUT = Path(project_dir) / input_filepath
    PATH_OUTPUT = Path(project_dir) / output_filepath

    products = pd.read_csv(PATH_INPUT / "products.csv", sep=";")
    tags_train = pd.read_csv(PATH_INPUT / "tags_train.csv", sep=";")
    users = pd.read_csv(PATH_INPUT / "users.csv", sep=";")
    df_train = (
        tags_train.merge(products, on="product_id", how="left")
        .merge(users, on="user_id", how="left")
        .astype(types_train)
    )
    df_train.to_parquet(PATH_OUTPUT / "train.parquet", index=False)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
