import paramiko
import os
import LogUtils
import FileIOUtils
from os.path import expanduser

log=LogUtils.getLogger()
def executeRemoteCommand(hostName,cmd,userName="ubuntu",mySSHKey=None):
    if hostName is not None:
        if userName is None:
            userName="ubuntu"
        if mySSHKey is None:
            home = expanduser("~")
            log.info(home)
            mySSHKey= home+"/.ssh/id_rsa"
            log.info(mySSHKey)
            sshcon = paramiko.SSHClient()  # will create the object
        try:
            log.info("ssh connection established.. ")
            sshcon.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
            sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # no known_hosts error
            sshcon.connect(hostName, username=userName, password=None,
                           timeout=20, key_filename=mySSHKey)  # no passwd needed
            log.info("executing command %s at remote server %s", cmd, hostName)
            stdin, stdout, stderr=sshcon.exec_command(cmd)
            log.info("ssh command still executing")
            if stdout.channel.recv_exit_status()==0:
                log.info("command %s  executed at remote server %s", cmd, hostName)
            else:
                log.info(" command %s failed with exit status %s ",cmd,str(stdout.channel.recv_exit_status()))
                log.info(" error "+str(stderr))
        except Exception as e:
            log.info(cmd + " execution failed "+e.message)
            pass
        finally:
            sshcon.close()
    else:
        log.info("hostName is none exiting ...")


def downloadFile(hostName,userName,remoteFile,targetFolder):
    cmd = "scp -o StrictHostKeyChecking=no " + userName + "@" + hostName + ":" + remoteFile + " " + targetFolder
    log.info("executing command %s", cmd)
    try:
        executeCommand(cmd)
    except:
        log.info("file download failed ",cmd)
        pass
def downloadFileParamIKO(hostName,userName,remoteFile,targetFolder):
    cmd ="scp "+userName+"@"+hostName+":"+remoteFile+" "+targetFolder
    executeCommand(cmd)
def executeCommand(cmd):
    log.info("executing command %s", cmd)
    os.system(cmd)