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
                    customers
                 RESTART IDENTITY CASCADE;
                 """)
        )