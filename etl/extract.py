from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw")

def read_csv_file(filename: str) -> pd.DataFrame:
    file_path = RAW_DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {file_path}")

    return pd.read_csv(file_path)

def extract_all_data() -> dict[str, pd.DataFrame]:
    return {
        "productos": read_csv_file("productos.csv"),
        "provedores": read_csv_file("proveedores.csv"),
        "clientes": read_csv_file("clientes.csv"),
        "ventas": read_csv_file("ventas.csv"),
        "importaciones": read_csv_file("importaciones.csv"),
    }

if __name__ == "__main__":
    dataframes = extract_all_data()

    for name, df in dataframes.items():
        print(f"\n==== {name.upper()} ====")
        print(df.head())
        print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
        