from django.db import models

# Create your models here.


class MenuHours(models.Model):
    store_id = models.BigIntegerField(null=True)
    day = models.IntegerField(null=True)
    start_time_local = models.CharField(max_length=8, null=True)
    end_time_local = models.CharField(max_length=8, null=True)

    class Meta:
        db_table = 'menu_hours'


class TimeZone(models.Model):
    store_id = models.BigIntegerField(null=True)
    timezone_str = models.CharField(max_length=28, null=True)

    class Meta:
        db_table = 'time_zone'


class StoreStatus(models.Model):
    store_id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=6, null=True)
    timestamp_utc = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'store_status'


class StoreResult(models.Model):
    store_id = models.IntegerField()
    uptime_last_hour = models.IntegerField()
    uptime_last_day = models.IntegerField()
    uptime_last_week = models.IntegerField()
    downtime_last_hour = models.IntegerField()
    downtime_last_day = models.IntegerField()
    downtime_last_week = models.IntegerField()
    uuid_associated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store_result'


class UuidMapping(models.Model):
    uuid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'uuid_mapping'