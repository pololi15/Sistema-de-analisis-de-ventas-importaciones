from pathlib import Path

from etl.extract import extract_all_data
from etl.transform import transform_all_data
from etl.load import clear_tables, load_dataframe, insert_etl_log

PROCESSED_DATA_PATH = Path("data/processed")

def save_clean_data(clean_data):
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    for name, df in clean_data.items():
        output_path = PROCESSED_DATA_PATH / f"{name}_limpio.csv"
        df.to_csv(output_path, index=False)
        print(f"Archivo guardado: {output_path}")


def main():
    try:
        raw_data = extract_all_data()
        clean_data = transform_all_data(raw_data)

        save_clean_data(clean_data)
        
        clear_tables()

        load_order = [
            "productos",
            "proveedores",
            "clientes",
            "ventas",
            "importaciones",
        ]
        total_rows = 0;

        for dataset_name in load_order:
            rows = len(clean_data[dataset_name])
            load_dataframe(clean_data[dataset_name], dataset_name)
            total_rows += rows
    
        insert_etl_log(
            process_name="main_etl_pipeline",
            status="SUCCESS",
            rows_processed=total_rows,
            message="ETL ejecutaddo correctamente",
        )
    except Exception as error:
        insert_etl_log(
            process_name="main_etl_pipeline",
            status="FAILED",
            rows_processed=0,
            message=str(error),
        )
        raise


if __name__ == "__main__":
    main()
