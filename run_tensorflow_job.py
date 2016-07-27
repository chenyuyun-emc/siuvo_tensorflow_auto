#!/usr/bin python

import configparser
import boto3
import time


from tensorflowutils import execmd, Logger
from launch_instance import start_instance
from terminal_instance import stop_instance


logger = Logger().get()

def uploadDataToBucket():
    s3client = boto3.client('s3')
    bucket_name = 'siuvo-tensorflow-{}'.format(time.strftime("%Y%m%d%H%M%S"))
    logger.info('Creating new bucket with name: {}'.format(bucket_name))
    s3client.create_bucket(Bucket=bucket_name)
    logger.info('push the result file to the bucket: {}'.format(bucket_name))
    s3client.upload_file("result", bucket_name, "result")

def run_tensorflow():
    cf = configparser.ConfigParser()
    cf.read("resource/siuvonlpauto.conf")
    publicdnsname = cf.get("workvm","publicdnsname")
    command = cf.get("workvm","command")
    download_file = cf.get("workvm","download_file")
    username = cf.get("workvm","username")
    privatekey = cf.get("workvm", "privatekey")

    logger.info("going to run the tensorflow job")
    if execmd('ssh -i '+privatekey+' -o StrictHostKeyChecking=no '+username+'@'+ publicdnsname+ ' '+ command, False) == 0 and \
       execmd('scp -i '+privatekey+' -o StrictHostKeyChecking=no '+username+'@'+ publicdnsname+ ':'+ download_file+' result', False) == 0:
        logger.info("Successfully")
        uploadDataToBucket()




start_instance()
run_tensorflow()
stop_instance()

