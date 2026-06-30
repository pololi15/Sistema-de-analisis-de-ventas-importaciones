from pathlib import Path

from extract import extract_all_data
from transform import transform_all_data

PROCESSED_DATA_PATH = Path("data/processed")

def save_clean_data(clean_data):
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    for name, df in clean_data.items():
        output_path = PROCESSED_DATA_PATH / f"{name}_limpio.csv"
        df.to_csv(output_path, index=False)
        print(f"Archivo guardado: {output_path}")


def main():
    raw_data = extract_all_data()
    clean_data = transform_all_data(raw_data)

    for name, df in clean_data.items():
        print(f"\n===== {name.upper()} LIMPIO =====")
        print(df)
        print(f"Filas limpias: {len(df)}")
    save_clean_data(clean_data)

if __name__ == "__main__":
    main()