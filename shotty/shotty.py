import boto3
import click

session = boto3.Session()
ec2 = session.resource('ec2')

@click.command()
def list_instance():
    "List all ec2 instances"
    for i in ec2.instances.all():
        #print(i.id + " " i.instance_type)
        print(','.join((i.id,i.instance_type,i.state['Name'],i.public_dns_name)))
if __name__ == '__main__':
    list_instance()

