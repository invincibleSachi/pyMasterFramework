import os
from os.path import dirname as up
import LogUtils
logs=LogUtils.getLogger()


currentFile = os.path.abspath(__file__)
testingPath = up(up(up(currentFile)))


def getDBQueryResult(cur, query):
    cur.execute(query)
    records = cur.fetchone()
    return records


