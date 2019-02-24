#!/usr/bin/env python
import os
import boto3

ec2 = boto3.resource("ec2", region_name='ap-southeast-2')
tag = ec2.Tag('resource_id','key','value')
client = boto3.client('ec2', region_name='ap-southeast-2')

ACCOUNT_ID = boto3.client('sts').get_caller_identity().get('Account')

# Gather AMIs and figure out which ones to delete
my_images = ec2.images.filter(Owners=[ACCOUNT_ID])

# Filter on tag and remove Image, Gold Tag
filters = [{'Name': 'tag:Image', 'Values': ['Gold'],'Name': 'tag:Name', 'Values': ['Planit Server2012R2 Gold'],}]
gold = ec2.images.filter(Filters=filters).all()
all_gold = []
for ami in gold.all():
    if ami.id not in all_gold:
        all_gold = all_gold + [ami.id]
        print("------------------------")
        print ("Number of Gold Images: {}".format(len(all_gold)))
        print("List of Gold Images: \n{}".format('\n'.join(map(str, all_gold))))
            
for image in my_images:
    if image.id in all_gold:
            print "untagging image %s" % image.id
            client.delete_tags(Resources=[image.id],Tags=[{"Key": 'Image'}])