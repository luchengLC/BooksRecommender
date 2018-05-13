# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BrBooks(models.Model):
    bookid = models.CharField(db_column='bookId', primary_key=True, max_length=20)  # Field name made lowercase.
    bookname = models.CharField(db_column='bookName', max_length=100)  # Field name made lowercase.
    subjecturl = models.CharField(db_column='subjectUrl', max_length=100)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=100)  # Field name made lowercase.
    author = models.CharField(max_length=100)
    pubdate = models.CharField(db_column='pubDate', max_length=40)  # Field name made lowercase.
    publisher = models.CharField(max_length=100)
    ratingscore = models.CharField(db_column='ratingScore', max_length=20)  # Field name made lowercase.
    ratingnum = models.IntegerField(db_column='ratingNum')  # Field name made lowercase.
    price = models.CharField(max_length=20)
    isbn = models.CharField(db_column='ISBN', max_length=20)  # Field name made lowercase.
    summary = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'br_books'


class BrTags(models.Model):
    bookid = models.CharField(db_column='bookId', primary_key=True, max_length=20)  # Field name made lowercase.
    tagname = models.CharField(db_column='tagName', max_length=40)  # Field name made lowercase.
    booktagrank = models.IntegerField(db_column='bookTagRank')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'br_tags'
        unique_together = (('bookid', 'tagname'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Favor(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=20)  # Field name made lowercase.
    bookid = models.CharField(db_column='bookId', max_length=20)  # Field name made lowercase.
    starnum = models.IntegerField(db_column='starNum')  # Field name made lowercase.
    startime = models.IntegerField(db_column='starTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favor'
        unique_together = (('userid', 'bookid'),)


class ItemCfSimilar(models.Model):
    bookid1 = models.CharField(db_column='bookId1', primary_key=True, max_length=20)  # Field name made lowercase.
    bookid2 = models.CharField(db_column='bookId2', max_length=20)  # Field name made lowercase.
    similar = models.FloatField()

    class Meta:
        managed = False
        db_table = 'item_cf_similar'
        unique_together = (('bookid1', 'bookid2'),)


class Users(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=40)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=40, blank=True, null=True)
    field_selfintro = models.CharField(db_column=' selfIntro', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'users'
