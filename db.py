import pymysql.cursors

def store_temp(param, reading, created_at):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='code@2215Name',
                                 database='libelium',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # Create a new record
        sql = f'''insert into parameter_data (param, reading, createdAt) values ("{param}", "{reading}", "{created_at}")'''
        cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
