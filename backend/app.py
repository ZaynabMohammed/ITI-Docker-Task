from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Backend!"

@app.route("/db")
def db_connect():
    try:
        conn = psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            host=os.environ['DB_HOST']
        )
        return "Connected to DB!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
