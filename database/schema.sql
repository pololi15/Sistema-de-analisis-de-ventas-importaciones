CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(80) NOT NULL,
    brand VARCHAR(80) NOT NULL,
    unit_cost NUMERIC(12,2),
    sale_price NUMERIC(12,2) NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name VARCHAR(150) NOT NULL,
    country VARCHAR(80) NOT NULL,
    city VARCHAR(80) NOT NULL
);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    city VARCHAR(80) NOT NULL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,

    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE imports (
    import_id INTEGER PRIMARY KEY,
    import_date DATE NOT NULL,
    supplier_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    imported_quantity INTEGER NOT NULL,
    total_cost NUMERIC(12,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    status VARCHAR(50) NOT NULL,

    CONSTRAINT fk_imports_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id),

    CONSTRAINT fk_imports_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE etl_logs (
    log_id SERIAL PRIMARY KEY,
    process_name VARCHAR(100) NOT NULL,
    status VARCHAR(30) NOT NULL,
    rows_processed INTEGER DEFAULT 0,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE data_quality_errors (
    error_id SERIAL PRIMARY KEY,
    dataset_name VARCHAR(100) NOT NULL,
    row_reference TEXT,
    error_type VARCHAR(100) NOT NULL,
    error_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);