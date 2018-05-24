import boto3
import click

session=boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.command()
def list_instances():
   for i in ec2.instances.all():
      print(','.join((
	        i.instance_id,
			i.placement['AvailabilityZone'],
			i.instance_type,
			i.state['Name'])))

if __name__=='__main__':
  list_instances()