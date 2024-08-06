import psycopg2
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


db_config = {
    'dbname': 'nostalgic_bedrooms',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db(config):
    logger.info('Connecting to the database...')
    conn = psycopg2.connect(**config)
    logger.info('Connected to the database.')
    return conn

create_bedroom_table = """
CREATE TABLE IF NOT EXISTS bedrooms (
    bedroom_id INTEGER PRIMARY KEY,
    title VARCHAR,
    description TEXT,
    img_src VARCHAR
);
"""

def create_table():
    logger.info('Creating table bedrooms...')
    conn = connect_db(db_config)
    cursor = conn.cursor()
    cursor.execute(create_bedroom_table)
    conn.commit()
    cursor.close()
    conn.close()
    logger.info('Table bedrooms created.')

def insert_bedroom(cursor, bedroom):
    insert_query = """
    INSERT INTO bedrooms (bedroom_id, title, description, img_src)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, bedroom)
    logger.info(f'Inserted bedroom: {bedroom}')

def process_csv(file_path, db_config):
    logger.info(f'Processing CSV file: {file_path}')
    conn = connect_db(db_config)
    cursor = conn.cursor()

    create_table()
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
    logger.info('CSV file processed and data inserted into the database.')

csv_file_path = 'bedrooms.csv'
process_csv(csv_file_path, db_config)