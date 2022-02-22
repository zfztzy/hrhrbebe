# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplicantInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    graduated_from = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    working_seniority = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    related = models.CharField(max_length=255, blank=True, null=True)
    arrival_time = models.CharField(max_length=255, blank=True, null=True)
    recommender = models.CharField(max_length=255, blank=True, null=True)
    recommend_time = models.CharField(max_length=255, blank=True, null=True)
    own_interviewer = models.CharField(max_length=255, blank=True, null=True)
    own_interview_results = models.CharField(max_length=255, blank=True, null=True)
    reason1 = models.CharField(max_length=255, blank=True, null=True)
    own_interview_time = models.CharField(max_length=255, blank=True, null=True)
    machine_test_type = models.CharField(max_length=255, blank=True, null=True)
    machine_test_score = models.CharField(max_length=255, blank=True, null=True)
    machine_test_time = models.CharField(max_length=255, blank=True, null=True)
    hw_interviewer1 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_results1 = models.CharField(max_length=255, blank=True, null=True)
    reason2 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_time1 = models.CharField(max_length=255, blank=True, null=True)
    hw_interviewer2 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_results2 = models.CharField(max_length=255, blank=True, null=True)
    reason3 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_time2 = models.CharField(max_length=255, blank=True, null=True)
    final_result = models.CharField(max_length=255, blank=True, null=True)
    final_time = models.CharField(max_length=255, blank=True, null=True)
    reason4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_info'


class ProjectInfo(models.Model):
    project_id = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    business = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    delivery_leader = models.CharField(max_length=255, blank=True, null=True)
    pm = models.CharField(db_column='PM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qa = models.CharField(db_column='QA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hr = models.CharField(db_column='HR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hwpm = models.CharField(db_column='HWPM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_info'


class ProjectStatusInfo(models.Model):
    date = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    sow_num = models.CharField(max_length=255, blank=True, null=True)
    project_num = models.CharField(max_length=255, blank=True, null=True)
    new_project_num = models.CharField(max_length=255, blank=True, null=True)
    offset_num = models.CharField(max_length=255, blank=True, null=True)
    monthly_target = models.CharField(max_length=255, blank=True, null=True)
    urgency = models.CharField(db_column='Urgency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mouthly_reach = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_status_info'


class RecruitmentInfo(models.Model):
    internal_id = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=255, blank=True, null=True)
    position_attribute = models.CharField(max_length=255, blank=True, null=True)
    skill_keyword = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.CharField(max_length=255, blank=True, null=True)
    working_seniority = models.CharField(max_length=255, blank=True, null=True)
    proposed_time = models.CharField(max_length=255, blank=True, null=True)
    proposer = models.CharField(max_length=255, blank=True, null=True)
    arrival_time = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    recruiter = models.CharField(max_length=255, blank=True, null=True)
    project_leader = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urgency = models.CharField(db_column='Urgency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    interviewer = models.CharField(max_length=255, blank=True, null=True)
    synthetical_interviewer = models.CharField(max_length=255, blank=True, null=True)
    arrival_num = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    close_time = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_info'
