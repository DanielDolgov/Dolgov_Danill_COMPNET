from fastapi import FastAPI
import psycopg2


from parser import parser_cccstore


DB_CONFIG = {
    "dbname": "DB_4",
    "user": "postgres",
    "password": "postgregory1",
    "host": "localhost",
    "port": 5432
}


def create_table():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT,
            price TEXT,
            reviews TEXT,
            rating TEXT
        )""")
    
    conn.commit()
    cur.close()
    conn.close()


def save_to_db(products):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE products RESTART IDENTITY;")
    
    for item in products:
        cur.execute("""
            INSERT INTO products (name, price, reviews, rating)
            VALUES (%s, %s, %s, %s)
        """, (item[0], item[1], item[2], item[3]))
    
    conn.commit()
    cur.close()
    conn.close()


def get_all_from_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    cur.execute("SELECT id, name, price, reviews, rating FROM products ORDER BY id ASC")
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "reviews": row[3],
            "rating": row[4]
        })
    
    return result


app = FastAPI()

create_table()


@app.get("/parse")
async def parse_endpoint():
    products = parser_cccstore()
    save_to_db(products)
    
    return {
        "status": "success",
        "message": f"Сохранено {len(products)} товаров",
        "total_count": len(products),
        "sample": products
    }


@app.get("/get-data")
async def get_data_endpoint():    
    data = get_all_from_db()

    return {
        "status": "success",
        "count": len(data),
        "data": data
    }


# Запуск сервера:
#    uvicorn server:app --reload


# http://127.0.0.1:8000/parse
# http://127.0.0.1:8000/get-data