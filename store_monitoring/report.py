from django.http import HttpResponse
from django.views import View
from store_monitoring.models import StoreStatus, TimeZone, MenuHours, StoreResult, UuidMapping
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ulid import ULID
from datetime import datetime, timedelta
import threading
import time
import tracemalloc
import logging

tracemalloc.start()


@method_decorator(csrf_exempt, name="dispatch")
class create_report(View):
    @csrf_exempt
    def post(self, request):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        unique_id = ULID.from_timestamp(time.time())
        print('getting the async function start', unique_id)
        # thread = threading.Thread(
        #     target=self.process_data,
        #     args = (unique_id,)
        # )
        # print('before stating thread')
        # thread.start()
        # print('thread started')
        self.process_data(unique_id)
        return HttpResponse('ok')


    def process_data(self, unique_id):
        try:
            print()
            UuidMap = UuidMapping()
            # result = StoreResult()
            UuidMap.uuid = unique_id
            UuidMap.status = 1
            UuidMap.save()
            id = UuidMap.id
            self.calcutateLastHourUptime(id)
            self.calculateLastDayUptime(id)
            self.calculateLastWeekUptime(id)
            # self.calculateLastHourDowntime(id)
            # self.calculateLastWeekDowntime(id)
            # self.calculateLastDayDowntime(id)

            print('inside the async function', unique_id)
        except Exception as e:
            print('Exception occur in process_data function',e)
        return "task_complete"
    def calcutateLastHourUptime(self, id):
        # interval = timedelta(hours=1)
        interval = timedelta(days=500)
        one_hour_age = datetime.utcnow() - interval
        print('58')
        data = StoreStatus.objects.filter(timestamp_utc__gt=one_hour_age).all()  #gives all the store which is active in the last hour
        for row in data:
            print('isnide the loop', row.store_id)
            print('62')
            calculate_last_hour_active_time = MenuHours.objects.filter(store_id=row.store_id, day=0, start_time_local__gt=one_hour_age).first()
            print('64')
            ifExists = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).exists()
            if ifExists:
                print('67')
                result = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).first()
                if calculate_last_hour_active_time is None:
                    result.uptime_last_hour = calculate_last_hour_active_time
                else:
                    result.uptime_last_hour += calculate_last_hour_active_time
                result.save()
                print('result updated')
            else:
                result = StoreResult()
                result.store_id = row.store_id
                result.uptime_last_hour = calculate_last_hour_active_time
                result.uuid_ref = id
                result.save()
                print('result created')
            print(row.store_id)


    def calculateLastDayUptime(id):
        # interval = timedelta(hours=1)
        interval = timedelta(days=500)
        one_hour_age = datetime.utcnow() - interval
        print('58')
        data = StoreStatus.objects.filter(timestamp_utc__gt=one_hour_age).all()  #gives all the store which is active in the last hour
        for row in data:
            print('isnide the loop', row.store_id)
            print('62')
            calculate_last_day_active_time = MenuHours.objects.filter(store_id=row.store_id, day=1, start_time_local__gt=one_hour_age).first()
            print('64')
            ifExists = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).exists()
            if ifExists:
                print('67')
                result = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).first()
                if calculate_last_day_active_time is None:
                    result.uptime_last_hour = calculate_last_day_active_time
                else:
                    result.uptime_last_hour += calculate_last_day_active_time
                result.save()
                print('result updated')
            else:
                result = StoreResult()
                result.store_id = row.store_id
                result.uptime_last_hour = calculate_last_day_active_time
                result.uuid_ref = id
                result.save()
                print('result created')
            print(row.store_id)

    def calculateLastWeekUptime(id):
        # interval = timedelta(hours=1)
        interval = timedelta(days=500)
        one_hour_age = datetime.utcnow() - interval
        print('58')
        data = StoreStatus.objects.filter(timestamp_utc__gt=one_hour_age).all()  #gives all the store which is active in the last hour
        for row in data:
            print('isnide the loop', row.store_id)
            print('62')
            calculate_last_week_active_time = MenuHours.objects.filter(store_id=row.store_id, day__ite=7, start_time_local__gt=one_hour_age).first()
            print('64')
            ifExists = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).exists()
            if ifExists:
                print('67')
                result = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).first()
                if calculate_last_week_active_time is None:
                    result.uptime_last_hour = calculate_last_week_active_time
                else:
                    result.uptime_last_hour += calculate_last_week_active_time
                result.save()
                print('result updated')
            else:
                result = StoreResult()
                result.store_id = row.store_id
                result.uptime_last_hour = calculate_last_week_active_time
                result.uuid_ref = id
                result.save()
                print('result created')
            print(row.store_id)
    def calculateLastHourDowntime(id):
        # interval = timedelta(hours=1)
        interval = timedelta(days=500)
        one_hour_age = datetime.utcnow() - interval
        print('58')
        data = StoreStatus.objects.filter(timestamp_utc__gt=one_hour_age).all()  #gives all the store which is active in the last hour
        for row in data:
            print('isnide the loop', row.store_id)
            print('62')
            calculate_last_week_active_time = MenuHours.objects.filter(store_id=row.store_id, day=1, start_time_local__gt=one_hour_age).first()
            print('64')
            ifExists = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).exists()
            if ifExists:
                print('67')
                result = StoreResult.objects.filter(store_id=row.store_id, uuid_ref=id).first()
                if calculate_last_week_active_time is None:
                    result.uptime_last_hour = calculate_last_week_active_time
                else:
                    result.uptime_last_hour += calculate_last_week_active_time
                result.save()
                print('result updated')
            else:
                result = StoreResult()
                result.store_id = row.store_id
                result.uptime_last_hour = calculate_last_week_active_time
                result.uuid_ref = id
                result.save()
                print('result created')
            print(row.store_id)
    def calculateLastDayDowntime(id):
        pass
    def calculateLastWeekDowntime(id):
        pass

    def calculateLastHourUptime():
        StoreStatus.object.filter()

@method_decorator(csrf_exempt, name="dispatch")
class get_report(View):
    @csrf_exempt
    def get(self, request):
        pass
