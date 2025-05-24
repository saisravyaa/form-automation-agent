import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="form_automation",
        user="postgres",
        password="admin123"  # use your actual password
    )

def get_city_info(city_name: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, latitude, longitude, state, zip FROM cities WHERE name = %s", (city_name.lower(),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {
            "city": row[0],
            "latitude": row[1],
            "longitude": row[2],
            "state": row[3],
            "zip": row[4]
        }
    return None
