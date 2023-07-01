from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

def add_user_to_db(data):
    with engine.connect() as conn:

        conn.execute(text(f"INSERT INTO users (firstName, lastName, email, password, phone, address, city, province, country) VALUES ('{data['firstName']}', '{data['lastName']}', '{data['email']}', '{data['password']}', '{data['phone']}', '{data['address']}', '{data['city']}', '{data['province']}', '{data['country']}')"))