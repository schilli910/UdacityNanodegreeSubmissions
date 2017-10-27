import zipfile
from Utils import *
import sqlite3
import pandas as pd


def compress_and_open_sqlite():
  zip = zipfile.ZipFile(INPUTFILE_DIR + INPUTZIPFILE)
  zip.extractall(path=INPUTFILE_DIR)
  conn = sqlite3.connect(INPUTFILE_DIR + DATABASENAME)
  return conn


def execute_query_print_results(conn, sql_query):
  cur = conn.cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()
  for row in rows:
    print row


def sql_to_dataframe(conn, sql):
  df = pd.read_sql_query(sql, conn)
  return df


def desc_table(table_df, table_name):
  print SEPARATOR
  print "For table " + table_name + " there are " + str(table_df.shape[0]) + \
        " entries with "+ str(table_df.shape[1]) + " features"


if __name__ == '__main__':
    conn = compress_and_open_sqlite()
    players_df = sql_to_dataframe(conn, select_all_query_table("Player"))
    desc_table(players_df, "Player")


