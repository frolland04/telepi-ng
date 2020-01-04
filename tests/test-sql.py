#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dépendances
import MySQLdb  # Besoin de "mysqlclient"

file = __file__.split('\\')[-1]

USER_NAME = 'teleinfo'
USER_PASSWORD = 'ti'
DATABASE_NAME = 'D_TEST'

print(file + ':', 'DATABASE_NAME=' + DATABASE_NAME)

connection = MySQLdb.connect('localhost', USER_NAME, USER_PASSWORD, DATABASE_NAME)
engine = self.connection.cursor()

engine.execute(
""" INSERT T_TEST_SQL set
msg = 'FATAL EXCEPTION CAUSED ABORTING',
val = %s,
ts = NOW() """,
144
)

connection.close()
