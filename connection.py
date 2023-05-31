import psycopg2

def connect(user, password):
    try:
        conn = psycopg2.connect(dbname='Library', user=user, password=password, host='localhost')
        return conn
    except:
        return None