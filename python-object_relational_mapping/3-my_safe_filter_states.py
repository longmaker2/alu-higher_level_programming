#!/usr/bin/python3
'''Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?'''

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    cursor = conn.cursor()
    sql = """ SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC """

    cursor.execute(sql, (sys.argv[4],))
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    conn.close()
