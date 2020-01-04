#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dépendances
import mysql.connector as db

file = __file__.split('\\')[-1]

USER_NAME = 'teleinfo'
USER_PASSWORD = 'ti'
DATABASE_NAME = 'D_TEST'

print('Testing SQL connection')
print(file + ':', 'DATABASE_NAME=' + DATABASE_NAME)

connection = db.connect(host='localhost', user=USER_NAME, password=USER_PASSWORD, database=DATABASE_NAME)
engine = connection.cursor()

print('Testing data injection')
engine.execute(""" INSERT INTO T_TEST_SQL SET msg = 'test-sql', val = %s, ts = NOW() """, (12001,))
connection.commit()

print('Testing data query')
engine.execute(""" SELECT * FROM T_TEST_SQL """)
s = engine.fetchall()
print(s)
#print("'{}':".format(s.statement))

connection.close()

print('Finished.')


