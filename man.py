from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def etl_run():
    raw = extract_data(raw)
    processed = transform_data(raw)
    load_data(processed)


if __name__ == "__main__":
    run_etl()

# This is the main entry point for the ETL pipeline.
