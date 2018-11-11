import os
import shutil
import sys
from os.path import dirname

testing_path = dirname(os.path.abspath(__file__))
project_path = dirname(testing_path)

sys.path.append(project_path)
sys.path.append(os.path.join(project_path, "src/"))
sys.path.append(os.path.join(project_path, "testing/"))


import argparse
import ConfigParser
from Framework.utils import LogUtils
from Framework.utils import S3Util
import testconstants


def Main():
    parser = argparse.ArgumentParser(
        description=' list test arguments')
    logs=LogUtils.getLogger()
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(testing_path, 'configs.ini'))
    config_env=config.get('testconfig','env')

    # Changing the paths for logging to avoid permission issues
    logging_src = os.path.join(project_path, 'src/logging.conf')
    logging_new = os.path.join(project_path, 'src/logging_test.conf')

    # Get test config params
    is_downloadAllTestDataFromS3=eval(config.get('testconfig','downloadAllTestDataFromS3'))
    is_measureCodeCoverage=eval(config.get('testconfig','measureCodeCoverage'))
    runTestInParallel=int(config.get('testconfig','runInParallelThreadsCount'))

    # command line arguments with there decsription..
    parser.add_argument('-e', '--env', dest='env', metavar="env", type=str, help='environment', default=config_env)
    parser.add_argument('-c', '--coverage', metavar="coverage", type=bool, help='For end time of logs',
                        default=is_measureCodeCoverage)
    parser.add_argument('-m', '--marker', dest='marker', metavar="marker", type=str, help='markers', default='')
    logs.info("==================== Test configurations =====================")
    logs.info("config_env:"+config_env)
    logs.info("is_downloadAllTestDataFromS3: "+str(is_downloadAllTestDataFromS3))
    logs.info("is_measureCodeCoverage :"+str(is_measureCodeCoverage))
    logs.info("runTestInParallel: "+str(runTestInParallel))

    # parse_args() for parsing arguments
    args = parser.parse_args()

    env = args.env
    is_code_coverage = args.coverage

    # sync data from S3
    S3Util.syncBucketFromS3(testconstants.S3_TEST_DATA, testconstants.TEST_INPUT_DATA)
    S3Util.syncBucketFromS3(testconstants.S3_MODELS_FOLDER, testconstants.TEST_MODELS_PATH)

    # Run pytest framework
    runSuiteCmd = "pytest " + testconstants.TEST_CASES_PATH + " --junitxml=" + testconstants.TEST_REPORT + "/report.xml"
    
    if runTestInParallel > 1:
        runSuiteCmd += " -n " + str(runTestInParallel)
    if is_code_coverage is True:
        runSuiteCmd += " --cov " + project_path + " --cov-report html:" + testconstants.TEST_REPORT+"/cov_html"
    if args.marker != '':
        runSuiteCmd += " -m " + args.marker
    
    logs.info("running following command "+runSuiteCmd)
    exitcode = os.system(runSuiteCmd)
    if exitcode != 0:
        sys.exit(1)


if __name__=="__main__":
    Main()
