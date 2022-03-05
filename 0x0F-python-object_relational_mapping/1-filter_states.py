#!/usr/bin/python3
"""
A script that filter states where name starts with upper N, order by id ASC
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3], charset='utf8')
    curser =db.curser()
    curser.execute("SELECT * FROM states WHERE name[0] = N ORDER BY id ASC")
    rows = curser.fetchall()
    for row in rows:
        print(row)
    curser.close()
    db.close()
