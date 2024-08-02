import psycopg2
import csv

db_config = {
    'dbname': 'nostalgic_bedrooms',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db(config):
    conn = psycopg2.connect(**config)
    return conn

def insert_bedroom(cursor, bedroom):
    insert_query = """
    INSERT INTO bedrooms (bedroom_id, title, description, img_src)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, bedroom)

def process_csv(file_path, db_config):
    conn = connect_db(db_config)
    cursor = conn.cursor()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bedroom = (
                int(row['bedroom_id']),
                row['title'],
                row['description'],
                row['img_src']
            )
            insert_bedroom(cursor, bedroom)
    conn.commit()
    cursor.close()
    conn.close()

csv_file_path = 'bedrooms.csv'
process_csv(csv_file_path, db_config)