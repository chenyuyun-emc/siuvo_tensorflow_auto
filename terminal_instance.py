#!/usr/bin python

import boto3
import configparser
from tensorflowutils import Logger

logger = Logger().get()

def stop_instance():

    ec2 = boto3.resource('ec2')

    cf = configparser.ConfigParser()
    cf.read("resource/siuvonlpauto.conf")

    instanceId = cf.get("workvm","instanceid")

    logger.info("going to shutdown the vm: {}".format(instanceId))
    ec2.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [instanceId]}]).stop()
    ec2.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [instanceId]}]).terminate()