import os
from os.path import dirname as up
import pytest
from Framework.utils import LogUtils
import json
import psycopg2


logs=LogUtils.getLogger()
currentFile = os.path.abspath(__file__)
testingPath = up(up(currentFile))

@pytest.fixture(scope="session", autouse=True)
def initLogs():
    log=LogUtils.getLogger()
    return log

def connect_to_database(env):
    envJson = os.path.join(testingPath, "environment.json")
    with open(envJson, 'rb') as fp:
        envVar = json.load(fp)
    records=[]
    database = envVar[env]['dbName']
    username = envVar[env]['dbuser']
    hostname = envVar[env]['dbHost']
    password = envVar[env]['dbpwd']
    print database, username, hostname, password

    conn = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname
    )
    return conn

@pytest.fixture(scope="session", autouse=True)
def db_conn(request):
    env = 'production'
    try:
        conn = connect_to_database(env)
    except Exception, exc:
        conn = None
        logs.info("Unable to connect to production database")

    if conn is None:
        try:
            env = 'local'
            conn = connect_to_database(env)
        except:
            conn = None
            logs.info("Unable to connect to local database")

    def final():
        if conn is not None:
            conn.close()
    request.addfinalizer(final)
    return conn
