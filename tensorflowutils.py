#!/usr/bin python

# Execute system command and logger

import subprocess
import logging
import os
import inspect


class Logger(object):
    def __init__(self):
        LOGGING_DIR = "log/"
        logger = logging.getLogger('siuvologger')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            file_name = os.path.join(LOGGING_DIR, 'sivuotensorflow.log' )
            handler = logging.FileHandler(file_name)
            #formatter = logging.Formatter('%(asctime)s %(levelname)s:'+name+' %(message)s')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s[%(funcName)s]:%(lineno)d %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger

# Function execmd(): Command execution
def execmd(cmd, mode, operation='PROD',cwd=None):
    if operation == 'PROD':
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        output, error = p.communicate()
    else:
        cmd = "echo \'%s\'" % cmd
        output = None
        error = None
    logfunction(cmd, output, error)
    # verbose mode
    if mode:
        print('# Executing command # ' + cmd)
        if output and error:
            print output
            print error
    # silent mode
    else:
        if p.returncode == 1:
            print error
    if operation == 'PROD':
        return p.returncode
    else:
        return 0


# Function logfunction(): log results or errors to a log file
# Change this function in the future to use logging
def logfunction(cmd, output, error):
    callref = inspect.stack()[2][3] + ':'
    mylog = Logger.get(Logger())
    mylog.info('%s %s' %(callref, cmd))
    if output:
        mylog.info('%s %s' %(callref, output))
    if error:
        mylog.error('%s %s' %(callref, error))

