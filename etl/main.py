from extract import extract_all_data
from transform import transform_all_data


def main():
    raw_data = extract_all_data()
    clean_data = transform_all_data(raw_data)

    for name, df in clean_data.items():
        print(f"\n===== {name.upper()} LIMPIO =====")
        print(df)
        print(f"Filas limpias: {len(df)}")


if __name__ == "__main__":
    main()