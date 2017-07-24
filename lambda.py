import boto3
def lambda_handler(event, context):
    client = boto3.client('autoscaling')
	response = client.update_auto_scaling_group(
	    AutoScalingGroupName='ApacStudioAboContactListAutoScaling',
		LaunchConfigurationName='ApacStudioAboContactListLC',
		MinSize=1,
		MaxSize=1,
		DesiredCapacity=1,
		AvailabilityZones=[
			'ap-northeast-1a',
		]
)
    



