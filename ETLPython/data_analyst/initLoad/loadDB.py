import psycopg2
import os

db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'cristovive',
    'host': 'localhost',
    'port': '5432',
}

sql_file_path = os.path.abspath('prueba.sql')


def ejecutar_script_sql(conn, script_path):
    try:
        with conn.cursor() as cursor:
            with open(script_path, 'r') as sql_file:
                sql_script = sql_file.read()

            cursor.execute(sql_script)

        conn.commit()
        print('Script SQL ejecutado con éxito.')

    except Exception as e:
        print(f'Error al ejecutar el script SQL: {e}')

try:
    connection = psycopg2.connect(**db_config)
    print('Conexión exitosa.')

    ejecutar_script_sql(connection, sql_file_path)

finally:
    if connection:
        connection.close()
        print('Conexión cerrada.')
