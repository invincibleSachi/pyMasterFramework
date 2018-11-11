import os
import os.path
import glob

def readFile(fileName):
    with open(fileName) as f:
        content = f.readlines()
        return content
def mergeFiles(filename1, filename2,targetFile):
    with open(targetFile, "a") as myfile:
        myfile.write(readFile(filename1))
        myfile.write(readFile(filename2))
        myfile.close
def appendLine2File(filename,line):
    with open(filename, 'a+') as f:
        line=line+"\n"
        f.write(line)
        f.close
def mergeAllFiles(dirName,targetFile,filePattern=None):
    print "dir %s",dirName
    print " targetFile %s",targetFile
    currDir=os.getcwd()
    os.chdir(dirName)
    if filePattern is None:
        read_files = glob.glob("*.log")
    else:
        read_files = glob.glob(filePattern)
    try:
        with open(targetFile, "wb") as outfile:
            for file in read_files:
                with open(file, "rb") as myfile:
                    outfile.write(readFile(file))
    except Exception as e:
        print "error while merging the files " + e.message
        os.chdir(currDir)
    finally:
        os.chdir(currDir)

def mergeAllFilesShell(dirName,targetFile,filePattern=None):
    cmd="cat "+dirName+filePattern+" > "+targetFile
    print cmd
    os.system(cmd)
def renameFile(src,dest):
    try:
        os.rename(src,dest)
    except Exception as e:
        print "error while renaming the file "+ e.message
def isFileExists(filename):
    return os.path.exists(filename)

def deleteFileifExists(filename):
    try:
        os.remove(filename)
        print("file " + filename+ " has been deleted")
    except OSError:
        pass
