#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import pyarrow.parquet as pq
import tqdm

def run():
    engine = create_engine("postgresql://postgres:postgres@db:5432/ny_taxi")

    # Part 1: CSV
    df_iter1 = pd.read_csv("./taxi_zone_lookup.csv",
                       iterator=True,
                       chunksize=10000)


    first_csv = True
    for df_chunk_1 in tqdm.tqdm(df_iter1):
        if first_csv:
            df_chunk_1.to_sql(
                name="taxi_zone_lookup",
                con=engine,
                if_exists="replace",
                index=False
            )
            first_csv = False

        else:
            f_chunk_1.to_sql(
                name="taxi_zone_lookup",
                con=engine,
                if_exists="append",
                index=False
            )

    # Part 2: Parquet
    parquet_file = pq.ParquetFile("./green_tripdata_2025-11.parquet")

    first_parquet = True
    for batch in tqdm.tqdm(parquet_file.iter_batches(batch_size=10000)):
        df_chunk = batch.to_pandas()

        if first_parquet:
            df_chunk.to_sql(name="green_tripdata_2025-11", 
                                   con=engine,
                                   if_exists="replace",
                                   index=False
                                   )
            first_parquet = False

        else:
            df_chunk.to_sql(name="green_tripdata_2025-11",
                           con=engine,
                           if_exists='append',
                           index=False)
if __name__ == "__main__":
    run()
