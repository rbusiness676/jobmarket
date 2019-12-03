from django.db import models

class Agent(models.Model):
    '''
        Agent details
    '''

    Agent_name = models.CharField(max_length=100, blank=False)
    Agent_id = models.CharField(max_length=10, null=False)
    bucket_no = models.CharField(max_length=10, null=False)
    Phone_no  = models.CharField(max_length=10, null=False)
    team_leader_id = models.ForeignKey('self', on_delete=models.CASCADE, default=1)

