# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Annotation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', related_name='Ann_created', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='Ann_deleted', blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    label = models.ForeignKey('Label', models.DO_NOTHING, blank=True, null=True)
    settings = models.CharField(max_length=255, blank=True, null=True)
    start = models.FloatField()
    text = models.CharField(max_length=255, blank=True, null=True)
    track = models.ForeignKey('Track', models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='Ann_updated', blank=True, null=True)

    class Meta:
        db_table = 'annotation'


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', related_name='cat_created',blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='cat_deleted', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    has_duration = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    scale_id = models.BigIntegerField(blank=True, null=True)
    settings = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='cat_updated',blank=True, null=True)
    video = models.ForeignKey('Video', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'category'


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    annotation = models.ForeignKey(Annotation, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', related_name='com_created',blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='com_deleted', blank=True, null=True)
    reply_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    text = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='com_updated',blank=True, null=True)

    class Meta:
        db_table = 'comment'


class Label(models.Model):
    id = models.BigIntegerField(primary_key=True)
    abbreviation = models.CharField(max_length=255)
    access = models.IntegerField(blank=True, null=True)
    category_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', related_name='lab_created',blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='lab_deleted', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    settings = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='lab_updated',blank=True, null=True)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'label'


class Track(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', related_name='trk_created',blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='trk_deleted', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    settings = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='trk_updated',blank=True, null=True)
    video = models.ForeignKey('Video', models.DO_NOTHING)

    class Meta:
        db_table = 'track'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)   
    created_by = models.ForeignKey('self', models.DO_NOTHING, db_column='created_by', related_name='usr_created', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('self', models.DO_NOTHING, db_column='deleted_by', related_name='usr_deleted', blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, db_column='updated_by', related_name='usr_updated',blank=True, null=True)

    class Meta:
        db_table = 'user'


class Video(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', related_name='vid_created', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, db_column='deleted_by', related_name='vid_deleted', blank=True, null=True)
    extid = models.CharField(unique=True, max_length=255)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by', related_name='vid_updated',blank=True, null=True)

    class Meta:
        db_table = 'video'
