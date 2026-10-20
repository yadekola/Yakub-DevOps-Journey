CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(40) NOT NULL UNIQUE,
    name VARCHAR(160) NOT NULL,
    category VARCHAR(80) NOT NULL,
    price_minor INTEGER NOT NULL CHECK (price_minor BETWEEN 0 AND 1000000000),
    quantity INTEGER NOT NULL CHECK (quantity BETWEEN 0 AND 1000000000),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX products_category_idx ON products (category);
