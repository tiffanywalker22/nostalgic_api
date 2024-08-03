from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

db_config = {
    'dbname': 'nostalgic_bedrooms',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn


@app.route('/bedrooms', methods=['GET'])
def get_bedrooms():
    conn = connect_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM bedrooms")
    bedrooms = cursor.fetchall()
    cursor.close()
    conn.close()
    bedrooms_list = [dict(bedroom) for bedroom in bedrooms]
    return jsonify(bedrooms_list)

if __name__ == '__main__':
    app.run(debug=True)