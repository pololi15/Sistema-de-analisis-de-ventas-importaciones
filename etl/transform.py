import pandas as pd


def normalize_text(value):
    if pd.isna(value):
        return value
    return str(value).strip().upper()


def normalize_currency(value):
    value = normalize_text(value)

    currency_map = {
        "BS.": "BOB",
        "BOLIVIANOS": "BOB",
        "BOB": "BOB",
        "USD": "USD",
    }

    return currency_map.get(value, value)


def clean_products(df):
    df = df.copy()

    df["nombre_producto"] = df["nombre_producto"].apply(normalize_text)
    df["categoria"] = df["categoria"].apply(normalize_text)
    df["marca"] = df["marca"].apply(normalize_text)

    df["costo_unitario"] = pd.to_numeric(df["costo_unitario"], errors="coerce")
    df["precio_venta"] = pd.to_numeric(df["precio_venta"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")

    df = df.drop_duplicates(subset=["nombre_producto", "marca"])

    return df


def clean_suppliers(df):
    df = df.copy()

    df["nombre_proveedor"] = df["nombre_proveedor"].apply(normalize_text)
    df["pais"] = df["pais"].apply(normalize_text)
    df["ciudad"] = df["ciudad"].apply(normalize_text)

    df = df.drop_duplicates(subset=["nombre_proveedor", "pais", "ciudad"])

    return df


def clean_customers(df):
    df = df.copy()

    df["nombre_cliente"] = df["nombre_cliente"].apply(normalize_text)
    df["tipo_cliente"] = df["tipo_cliente"].apply(normalize_text)
    df["ciudad"] = df["ciudad"].apply(normalize_text)

    df = df.drop_duplicates(subset=["nombre_cliente", "tipo_cliente", "ciudad"])

    return df


def clean_sales(df):
    df = df.copy()

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
    df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
    df["moneda"] = df["moneda"].apply(normalize_currency)

    df = df[df["fecha"].notna()]
    df = df[df["cantidad"] > 0]
    df = df[df["precio_unitario"] > 0]

    return df


def clean_imports(df):
    df = df.copy()

    df["fecha_importacion"] = pd.to_datetime(
        df["fecha_importacion"],
        errors="coerce",
        dayfirst=False,
    )
    df["cantidad_importada"] = pd.to_numeric(df["cantidad_importada"], errors="coerce")
    df["costo_total"] = pd.to_numeric(df["costo_total"], errors="coerce")
    df["moneda"] = df["moneda"].apply(normalize_currency)
    df["estado"] = df["estado"].apply(normalize_text)

    df = df[df["fecha_importacion"].notna()]
    df = df[df["cantidad_importada"] > 0]
    df = df[df["costo_total"] > 0]

    return df


def transform_all_data(dataframes):
    return {
        "productos": clean_products(dataframes["productos"]),
        "proveedores": clean_suppliers(dataframes["proveedores"]),
        "clientes": clean_customers(dataframes["clientes"]),
        "ventas": clean_sales(dataframes["ventas"]),
        "importaciones": clean_imports(dataframes["importaciones"]),
    }