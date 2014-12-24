from django.db import models
from uuidfield import UUIDField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class License(models.Model):
    title           = models.CharField(max_length=32)
    license_type    = models.CharField(max_length=32)
    #author_user_id = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Resource(models.Model):
    uuid  = UUIDField(auto=True, primary_key=True)
    group = models.ForeignKey(Group)

    url  = models.URLField(max_length=255)
    name = models.CharField(max_length=32)
    desc = models.TextField()
    created_on  = models.DateTimeField()
    modified_on = models.DateTimeField()

    # Assuming we won't get files larger than 2GB
    #TODO# Restrist charfields with options. Left for later due to needing
    ###### to gather a large list of types up.
    file_size     = models.PositiveIntegerField() 
    file_hash     = models.CharField(max_length=32)
    file_type     = models.CharField(max_length=32)
    file_mimetype = models.CharField(max_length=32)
    file_format   = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class DataSet(models.Model):
    uuid     = UUIDField(auto=True, primary_key=True)
    title    = models.CharField(max_length=32)
    url_name = models.CharField(max_length=32)
    version  = models.CharField(max_length=32)
    url      = models.URLField(max_length=256)
    notes    = models.TextField()

    DATASET_TYPES = (
        ('dataset', 'Data Set'),
        ('unknown', 'Unknown')
    )
    set_type = models.CharField(
        max_length=32, choices=DATASET_TYPES, default='dataset')
    #maintainer_user_id = models.ForeignKey(User)
    #author_user_id = models.ForeignKey(User)

    is_private = models.BooleanField(default=False)
    is_open    = models.BooleanField(default=False)

    DATASET_ACTIVITY_STATES = (
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('active', 'Active'),
    )
    activity_state = models.CharField(
        max_length=32, choices=DATASET_ACTIVITY_STATES, default='inactive')


    created_on  = models.DateTimeField()
    modified_on = models.DateTimeField()

    tags      = models.ManyToManyField(Tag)
    resources = models.ManyToManyField(Resource, through='DataSetResource')

    def __unicode__(self):
        return self.title

###
# Many to (Many, One) models
###

class DataSetResource(models.Model):
    dataset  = models.ForeignKey(DataSet)
    resource = models.ForeignKey(Resource)
    position = models.PositiveIntegerField()

class DataSetExtra(models.Model):
    dataset = models.ForeignKey(DataSet)
    name    = models.CharField(max_length=32)
    content = models.TextField()

class DataSetRating(models.Model):
    dataset = models.ForeignKey(DataSet)
    #user_id = models.ForeignKey(User)
    rating  = models.FloatField()

