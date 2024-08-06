from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  # Setting up logging configuration
logger = logging.getLogger()

db_config = {
    'dbname': 'nostalgic_bedrooms',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)

def connect_db():
    """
    Connects to the PostgreSQL database using the provided configuration.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
    """
    logger.info('Connecting to the database...')
    conn = psycopg2.connect(**db_config)
    logger.info('Connected to the database.')
    return conn


@app.route('/bedrooms', methods=['GET'])
def get_bedrooms():
    """
    Retrieves a list of all bedrooms from the `bedrooms` table in the PostgreSQL database.

    The function queries the database for all records in the `bedrooms` table and returns them
    as a JSON array.

    Returns:
        flask.Response: A Flask `Response` object containing a JSON array of bedroom objects.
        The JSON array includes:
            - `bedroom_id` (int): The unique ID of the bedroom.
            - `title` (str): The title of the bedroom.
            - `description` (str): A text description of the bedroom.
            - `img_src` (str): The URL or path to an image of the bedroom.
    """
    logger.info('Received request for all bedrooms.')
    conn = connect_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM bedrooms")
    bedrooms = cursor.fetchall()
    cursor.close()
    conn.close()
    bedrooms_list = [dict(bedroom) for bedroom in bedrooms]
    logger.info('Returning list of all bedrooms.')
    return jsonify(bedrooms_list)

if __name__ == '__main__':
    """
    Starts the Flask application if the script is executed directly.

    The application runs in debug mode for development purposes.
    """
    logger.info('Starting Flask application...')
    app.run(debug=True)