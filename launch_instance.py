# Import the SDK
import boto3
import configparser
import time
from tensorflowutils import Logger

logger = Logger().get()


def start_instance():

  #create the connection
  ec2 = boto3.resource('ec2')

  #read the configuration file
  cf = configparser.ConfigParser()
  cf.read("resource/siuvonlpauto.conf")

  imageId = cf.get("ec2","ImageId")
  instanceType = cf.get("ec2","InstanceType")
  keyName = cf.get("ec2","KeyName")
  securityGroups = cf.get("ec2","SecurityGroups")
  print imageId 

  logger.info("going to launch ec2 instance")
  #launch the instance
  reservation = ec2.create_instances(ImageId=imageId, MinCount=1, MaxCount=1, InstanceType=instanceType, KeyName=keyName, SecurityGroups=[securityGroups])

  time.sleep(120)

  instances = ec2.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [reservation[0].id]}])
  for instance in instances:
    cf.set("workvm", "publicDnsName", instance.public_dns_name)
    cf.set("workvm", "instanceId", instance.id)
    print(instance.id, instance.public_dns_name)
    with open("resource/siuvonlpauto.conf","w+") as f:
      cf.write(f)


