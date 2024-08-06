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
    """
    Connects to the PostgreSQL database using the provided configuration.

    Args:
        config (dict): A dictionary containing database configuration parameters.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
    """
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
    """
    Creates the `bedrooms` table in the PostgreSQL database if it does not already exist.

    The table schema includes:
        - `bedroom_id` (INTEGER): Primary key for the table.
        - `title` (VARCHAR): The title of the bedroom.
        - `description` (TEXT): A text description of the bedroom.
        - `img_src` (VARCHAR): The URL or path to an image of the bedroom.
    """
    logger.info('Creating table bedrooms...')
    conn = connect_db(db_config)
    cursor = conn.cursor()
    cursor.execute(create_bedroom_table)
    conn.commit()
    cursor.close()
    conn.close()
    logger.info('Table bedrooms created.')

def delete_all_data():
    """
    Deletes all data from the `bedrooms` table in the PostgreSQL database.

    This function does not delete the table schema itself, only the data contained within.
    """
    logger.info('Deleting all data from bedrooms table...')
    conn = connect_db(db_config)
    cursor = conn.cursor()
    delete_query = "DELETE FROM bedrooms;"
    cursor.execute(delete_query)
    conn.commit()
    cursor.close()
    conn.close()
    logger.info('All data deleted from bedrooms table.')

def insert_bedroom(cursor, bedroom):
    """
    Inserts a single bedroom record into the `bedrooms` table.

    Args:
        cursor (psycopg2.cursor): A psycopg2 cursor object used to execute SQL commands.
        bedroom (tuple): A tuple containing the bedroom data to insert, with elements:
            - bedroom_id (int): The unique ID of the bedroom.
            - title (str): The title of the bedroom.
            - description (str): A text description of the bedroom.
            - img_src (str): The URL or path to an image of the bedroom.
    """
    insert_query = """
    INSERT INTO bedrooms (bedroom_id, title, description, img_src)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, bedroom)
    logger.info(f'Inserted bedroom: {bedroom}')

def process_csv(file_path, db_config):
    """
    Processes a CSV file and inserts its contents into the `bedrooms` table.

    Args:
        file_path (str): The path to the CSV file containing bedroom data.
        db_config (dict): A dictionary containing database configuration parameters.

    The function performs the following steps:
        1. Connects to the database.
        2. Deletes all existing data from the `bedrooms` table.
        3. Reads the CSV file and inserts each row into the table.
    """
    logger.info(f'Processing CSV file: {file_path}')
    conn = connect_db(db_config)
    cursor = conn.cursor()

    delete_all_data()
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
create_table()
process_csv(csv_file_path, db_config)