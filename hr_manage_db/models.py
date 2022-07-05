# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplicantInfo(models.Model):
    key = models.AutoField(primary_key=True)
    recommend_time = models.DateTimeField(blank=True, null=True)
    recommender = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    graduated_from = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    graduation = models.CharField(max_length=255, blank=True, null=True)
    working_seniority = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    onjob = models.CharField(max_length=100, blank=True, null=True)
    interviews = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    reason1 = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(max_length=255, blank=True, null=True)
    own_interview_results = models.CharField(max_length=255, blank=True, null=True)
    suggest_level = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_results1 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_results2 = models.CharField(max_length=255, blank=True, null=True)
    reason2 = models.CharField(max_length=255, blank=True, null=True)
    process_status = models.CharField(max_length=255, blank=True, null=True)
    arrival_time = models.CharField(max_length=255, blank=True, null=True)
    offersuggest = models.CharField(max_length=100, blank=True, null=True)
    reason4 = models.CharField(max_length=255, blank=True, null=True)
    final_time = models.DateTimeField(blank=True, null=True)
    giveup_time = models.DateTimeField(blank=True, null=True)
    entrance = models.CharField(max_length=255, blank=True, null=True)
    related = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    own_interviewer = models.CharField(max_length=255, blank=True, null=True)
    own_interview_time = models.DateTimeField(blank=True, null=True)
    machine_test_type = models.CharField(max_length=255, blank=True, null=True)
    machine_test_score = models.CharField(max_length=255, blank=True, null=True)
    machine_test_time = models.DateTimeField(blank=True, null=True)
    hw_interviewer1 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_time1 = models.DateTimeField(blank=True, null=True)
    hw_interviewer2 = models.CharField(max_length=255, blank=True, null=True)
    hw_interview_time2 = models.DateTimeField(blank=True, null=True)
    final_result = models.CharField(max_length=255, blank=True, null=True)
    resume_status = models.CharField(max_length=255, blank=True, null=True)
    reason3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_info'


class ContactInfo(models.Model):
    key = models.AutoField(primary_key=True)
    employee_num = models.IntegerField()
    employeename = models.CharField(max_length=100, blank=True, null=True)
    charger_name = models.CharField(max_length=100)
    contact_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    contact_type = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    leader = models.CharField(max_length=100, blank=True, null=True)
    pm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_info'


class CustomerInfo(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    hw_num = models.CharField(max_length=100, blank=True, null=True)
    hwdu = models.CharField(max_length=100, blank=True, null=True)
    hwpdu = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phonenum = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EmployeeInfo(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    rt_num = models.IntegerField(unique=True)
    hw_num = models.CharField(max_length=100, blank=True, null=True)
    wb_num = models.CharField(max_length=100, blank=True, null=True)
    w3_num = models.CharField(max_length=100, blank=True, null=True)
    rtemail = models.CharField(max_length=100, blank=True, null=True)
    hwemail = models.CharField(max_length=100, blank=True, null=True)
    prolevel = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=100, blank=True, null=True)
    entrydate = models.CharField(max_length=100, blank=True, null=True)
    checkindate = models.CharField(max_length=100, blank=True, null=True)
    facedate = models.CharField(max_length=100, blank=True, null=True)
    ompendingtime = models.CharField(db_column='OMPendingtime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endworktime = models.CharField(max_length=100, blank=True, null=True)
    levelprojecttime = models.CharField(max_length=100, blank=True, null=True)
    offworktime = models.CharField(max_length=100, blank=True, null=True)
    projectim = models.CharField(db_column='projectIM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(max_length=100, blank=True, null=True)
    projecttype = models.CharField(max_length=100, blank=True, null=True)
    hwmanager = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    pdumanager = models.CharField(max_length=100, blank=True, null=True)
    pm = models.CharField(max_length=100, blank=True, null=True)
    phonenum = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_info'


class PduInfo(models.Model):
    key = models.AutoField(primary_key=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hwpdu_leader = models.CharField(db_column='HWPDU_Leader', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    pdu_manager = models.CharField(db_column='PDU_manager', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdu_qa = models.CharField(db_column='PDU_QA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdu_hr = models.CharField(db_column='PDU_HR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdu_info'


class PoInfo(models.Model):
    key = models.AutoField(primary_key=True)
    project_po = models.CharField(max_length=255, blank=True, null=True)
    po_name = models.CharField(max_length=255, blank=True, null=True)
    business = models.CharField(max_length=255, blank=True, null=True)
    pm = models.CharField(db_column='PM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    star_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onsite = models.CharField(max_length=255, blank=True, null=True)
    operating_model = models.CharField(max_length=255, blank=True, null=True)
    price_intax = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    delivery_leader = models.CharField(max_length=255, blank=True, null=True)
    qa = models.CharField(db_column='QA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hr = models.CharField(db_column='HR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hwpm = models.CharField(db_column='HWPM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    omper = models.CharField(db_column='OMPer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(max_length=255, blank=True, null=True)
    omp_endtime = models.CharField(db_column='OMP_endtime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount_extax = models.CharField(db_column='amount _extax', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    inkpi = models.CharField(db_column='INKPI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_info'


class ProjectInfo(models.Model):
    key = models.AutoField(primary_key=True)
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
    omper = models.CharField(db_column='OMPer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pm2 = models.CharField(db_column='PM2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_info'


class ProjectStatusInfo(models.Model):
    key = models.AutoField(primary_key=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    po_num = models.CharField(db_column='PO_NUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    sow_num = models.IntegerField(blank=True, null=True)
    project_num = models.IntegerField(blank=True, null=True)
    new_project_num = models.IntegerField(blank=True, null=True)
    offset_num = models.IntegerField(blank=True, null=True)
    monthly_target = models.IntegerField(blank=True, null=True)
    urgency = models.CharField(db_column='Urgency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    monthly_reach = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_status_info'


class RaiseSalaryInfo(models.Model):
    key = models.AutoField(primary_key=True)
    rt_num = models.ForeignKey(EmployeeInfo, models.DO_NOTHING, db_column='rt_num')
    tj_date = models.DateTimeField(blank=True, null=True)
    before_level = models.CharField(max_length=100, blank=True, null=True)
    after_level = models.CharField(max_length=100, blank=True, null=True)
    tx_time = models.DateTimeField(blank=True, null=True)
    before_salary = models.CharField(max_length=100, blank=True, null=True)
    increase = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raise_salary_info'


class RecruitmentInfo(models.Model):
    key = models.AutoField(primary_key=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    pdu = models.CharField(db_column='PDU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=255, blank=True, null=True)
    proposer = models.CharField(max_length=255, blank=True, null=True)
    position_attribute = models.CharField(max_length=255, blank=True, null=True)
    skill_keyword = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    type2 = models.CharField(max_length=255, blank=True, null=True)
    urgency = models.CharField(db_column='Urgency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    requirements = models.TextField(blank=True, null=True)
    working_seniority = models.CharField(max_length=255, blank=True, null=True)
    proposed_time = models.DateTimeField(blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    recruiter = models.CharField(max_length=255, blank=True, null=True)
    project_leader = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interviewer = models.CharField(max_length=255, blank=True, null=True)
    synthetical_interviewer = models.CharField(max_length=255, blank=True, null=True)
    arrival_num = models.CharField(max_length=255, blank=True, null=True)
    omptype = models.CharField(db_column='OMPType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    close_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    internal_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_info'


class TableCol(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    table_type = models.CharField(max_length=255, blank=True, null=True)
    col = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    justtest = models.CharField(max_length=100, blank=True, null=True)
    is_filter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_col'


class UserInfo(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
        unique_together = (('user_name', 'nickname'),)


class UserLevel(models.Model):
    level = models.IntegerField(primary_key=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    hr_manage = models.IntegerField(blank=True, null=True)
    project_manage = models.IntegerField(blank=True, null=True)
    kpi = models.IntegerField(db_column='KPI', blank=True, null=True)  # Field name made lowercase.
    staff = models.IntegerField(blank=True, null=True)
    business = models.IntegerField(blank=True, null=True)
    list = models.IntegerField(blank=True, null=True)
    sign_up = models.IntegerField(blank=True, null=True)
    pduinfo = models.IntegerField(blank=True, null=True)
    applicant = models.IntegerField(blank=True, null=True)
    recruitment = models.IntegerField(blank=True, null=True)
    pojectstatus = models.IntegerField(blank=True, null=True)
    recruitchart = models.IntegerField(blank=True, null=True)
    projectmanager = models.IntegerField(blank=True, null=True)
    projectinfo = models.IntegerField(blank=True, null=True)
    poinfo = models.IntegerField(blank=True, null=True)
    polist = models.IntegerField(blank=True, null=True)
    customerinfo = models.IntegerField(blank=True, null=True)
    employee = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    apphome = models.IntegerField(blank=True, null=True)
    employeenum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_level'
