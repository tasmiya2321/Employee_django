# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmpDetails(models.Model):
    emp_id = models.AutoField(db_column='EMP_ID', primary_key=True)  # Field name made lowercase.
    fullname = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    dob = models.IntegerField(db_column='Dob', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.IntegerField(db_column='Phone_Number', blank=True, null=True)  # Field name made lowercase.
    email_id = models.TextField(db_column='Email_Id', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    center = models.IntegerField(db_column='Center', blank=True, null=True)  # Field name made lowercase.
    designation = models.TextField(db_column='Designation', blank=True, null=True)  # Field name made lowercase.
    date_of_joining = models.IntegerField(db_column='Date_of_Joining', blank=True, null=True)  # Field name made lowercase.
    education_qualification = models.TextField(db_column='Education_Qualification', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    resource_type = models.IntegerField(db_column='Resource_Type', blank=True, null=True)  # Field name made lowercase.
    date_of_resigning = models.IntegerField(db_column='Date_of_resigning', blank=True, null=True)  # Field name made lowercase.
    bank_name = models.TextField(db_column='Bank_Name', blank=True, null=True)  # Field name made lowercase.
    name_as_per_bank = models.TextField(db_column='Name_As_per_Bank', blank=True, null=True)  # Field name made lowercase.
    account_number = models.IntegerField(db_column='Account_Number', blank=True, null=True)  # Field name made lowercase.
    ifsc = models.TextField(db_column='IFSC', blank=True, null=True)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch', blank=True, null=True)  # Field name made lowercase.
    account_type = models.IntegerField(db_column='Account_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emp_details'


class Program(models.Model):
    pgm_id = models.AutoField(db_column='PGM_ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey(EmpDetails, models.DO_NOTHING, db_column='EMP_ID')  # Field name made lowercase.
    xref = models.ForeignKey('Xref', models.DO_NOTHING, db_column='XREF_ID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', blank=True, null=True, max_length=255)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    center_type = models.IntegerField(db_column='Center_Type', blank=True, null=True)  # Field name made lowercase.
    trainer_type = models.IntegerField(db_column='Trainer_Type', blank=True, null=True)  # Field name made lowercase.
    sponsor = models.IntegerField(db_column='Sponsor', blank=True, null=True)  # Field name made lowercase.
    beneficiaries = models.IntegerField(db_column='Beneficiaries', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Program'


class ProgramDetails(models.Model):
    pgm_id = models.AutoField(db_column='PGM_ID', primary_key=True)  # Field name made lowercase.
    xref = models.ForeignKey('Xref', models.DO_NOTHING, db_column='XREF_ID')  # Field name made lowercase.
    no_of_dropouts = models.IntegerField(db_column='No_of_dropouts', blank=True, null=True)  # Field name made lowercase.
    attendance_percentage = models.IntegerField(db_column='Attendance_percentage', blank=True, null=True)  # Field name made lowercase.
    pre_assessment_score = models.IntegerField(db_column='Pre_Assessment_Score', blank=True, null=True)  # Field name made lowercase.
    mid_assessment_score = models.IntegerField(db_column='Mid_Assessment_Score', blank=True, null=True)  # Field name made lowercase.
    post_assessment_score = models.IntegerField(db_column='Post_Assessment_Score', blank=True, null=True)  # Field name made lowercase.
    closure_report = models.TextField(db_column='Closure_report', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Program_details'


class Xref(models.Model):
    xref_id = models.AutoField(db_column='XREF_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    program_name = models.IntegerField(blank=True, null=True)
    project_name = models.CharField(db_column='Project_name', blank=True, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Xref'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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
