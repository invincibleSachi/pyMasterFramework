import os
import LogUtils
log=LogUtils.getLogger()

def downloadFolderFromS3(s3BucketName,srcFolder,targetFolderName):
    cmd="aws s3 sync s3://"+s3BucketName+"/"+srcFolder+" "+targetFolderName
    log.info("executing command "+cmd)
    os.system(cmd)

def uploadFolder2S3(s3BucketName,srcfolderName,destFolderName):
    cmd="aws s3 sync "+srcfolderName+" s3://"+s3BucketName+"/"+destFolderName
    log.info("executing command " + cmd)
    os.system(cmd)

def syncBucketFromS3(s3Bucket, destFolder):
    cmd="aws s3 sync %s %s" %(s3Bucket, destFolder)
    log.info("executing command " + cmd)
    os.system(cmd)

