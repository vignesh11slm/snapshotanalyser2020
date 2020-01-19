import boto3
session = boto3.Session()
ec2 = session.resource('ec2')

def list_instance():
    for i in ec2.instances.all():
    	print(i)

if __name__ == '__main__':
    list_instance()
