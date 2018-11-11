import logging
from logging import handlers
import sys
from ... import testconstants

LOGFILE=testconstants.TEST_LOGS+"testLog.out"
log=None
def setLogger():
    log = logging.getLogger('')
    log.setLevel(logging.DEBUG)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    log.addHandler(ch)

    fh = handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*10), backupCount=7)
    fh.setFormatter(format)
    log.addHandler(fh)
    return log
def getLogger():
    if log is None:
        return setLogger()
    else:
        return log