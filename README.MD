the following is the steps when you need to enable tensorflow automation

Prerequisites
  For AWS EC2:
    1. Go to the AWS Management Console, and click EC2 panel, then click Instances button in right area, click Launch Instance button to create a new Virtual Machine.
    2. Choose Red Hat Enterprise Linux 7.2 (HVM), SSD Volume Type, then click Select button
    3. Choose an Instance Type. choose the t2.micro.
    4. Configure Instance Details, don't need to change anything, use the default value.
    5. Add Storage, use the defalut value and go to the next step
    6. Tag Instance, input the TensorFlowImage into the value input area. then click the next button
    7. Configure Security Group, use the default value, then click the next button
    8. click launch button, the page will pop up the key pair, if you first time to launch the instance , you can create the key pair and download this keypair.  or you can choose the existing key pair.
    9. need to create a security group, you can go to the security group page, click the create security group button and input the security group name like tensorflowgroup and
       the description , then click the add rule button , choose the ssh type and choose the AnyWhere in Source , then click create button

   when the instance launch finished, then use ssh to go to this instance.  run following commands to install tensorflow
     1. install pip, run the following commands to install pip. python get-pip.py, you can get this file in our resource folder. or use curl -O https://bootstrap.pypa.io/get-pip.py
     2. add the variable in terminal, export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl
     3. install tensorflow: pip install --upgrade $TF_BINARY_URL
     4. need to install git: yum install git

    about the details of install tensorflow , please refer this page: https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html



  For Work Machine:
     1. need to install pip, please use the above steps to install pip
     2. need to install aws, pip install awscli
     3. configure the aws, when you finished the aws cli installation ,you can input the command the aws configure, the terminal will need you input the credential info. the credential info you can get
        it from the aws management console. go to the security credentials page, then click Access Keys (Access Key ID and Secret Access Key) button. you can create a new access key.
     4. configure the aws, also you need to input the area, you should use the same area that where you image in.
     5. need to install configparser, run command, pip install configparser
     6. need to install pip install boto3






