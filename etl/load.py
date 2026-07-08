from sqlalchemy import text
from database.connection import engine

TABLE_MAP = {
    "productos": "products",
    "proveedores": "suppliers",
    "clientes": "customers",
    "ventas": "sales",
    "importaciones": "imports",
}


COLUMN_MAP = {
    "productos": {
        "producto_id": "product_id",
        "nombre_producto": "product_name",
        "categoria": "category",
        "marca": "brand",
        "costo_unitario": "unit_cost",
        "precio_venta": "sale_price",
        "stock": "stock",
    },
    "proveedores": {
        "proveedor_id": "supplier_id",
        "nombre_proveedor": "supplier_name",
        "pais": "country",
        "ciudad": "city",
    },
    "clientes": {
        "cliente_id": "customer_id",
        "nombre_cliente": "customer_name",
        "tipo_cliente": "customer_type",
        "ciudad": "city",
    },
    "ventas": {
        "venta_id": "sale_id",
        "fecha": "sale_date",
        "cliente_id": "customer_id",
        "producto_id": "product_id",
        "cantidad": "quantity",
        "precio_unitario": "unit_price",
        "moneda": "currency",
    },
    "importaciones": {
        "importacion_id": "import_id",
        "fecha_importacion": "import_date",
        "proveedor_id": "supplier_id",
        "producto_id": "product_id",
        "cantidad_importada": "imported_quantity",
        "costo_total": "total_cost",
        "moneda": "currency",
        "estado": "status",
    },
}

def load_dataframe(df, dataset_name):
    table_name = TABLE_MAP[dataset_name]
    column_map = COLUMN_MAP[dataset_name]

    df = df.rename(columns=column_map)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print(f"{len(df)} filas cargadas en {table_name}")

def clear_tables():
    with engine.begin() as connection:
        connection.execute(
            text("""
                 TRUNCATE TABLE 
                    sales,
                    imports,
                    products,
                    suppliers,
                    customers,
                 data_quality_errors,
                 etl_logs
                 RESTART IDENTITY CASCADE;
                 """)
        )

def insert_etl_log(process_name, status, rows_processed=0, message=None):
    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO etl_logs(
                    process_name,
                    status,
                    rows_processed,
                    message
                )
                VALUES (
                    :process_name,
                    :status,
                    :rows_processed,
                    :message
                );
            """),
            {
                "process_name": process_name,
                "status": status,
                "rows_processed": rows_processed,
                "message": message,
                 },
        )

def insert_data_quality_error(dataset_name, row_reference, error_type, error_description):
    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO data_quality_errors(
                    dataset_name,
                    row_reference,
                    error_type,
                    error_description
                )
                VALUES (
                    :dataset_name,
                    :row_reference,
                    :error_type,
                    :error_description
                );
            """),
            {
                "dataset_name": dataset_name,
                "row_reference": str(row_reference),
                "error_type": error_type,
                "error_description": error_description,
            },
        ) 