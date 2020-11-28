import mariadb
import sys

try:
    conn = mariadb.connect(
        user="spaceshooter",
        password="avafqKyzK5uEu89e",
        host="mariadb-test.rumpfhuber.icu",
        port=3306,
        database="spaceshooter"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform:\n{e}")
    sys.exit(1)