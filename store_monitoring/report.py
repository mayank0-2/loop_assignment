import asyncio
from django.http import HttpResponse
from django.views import View
from store_monitoring.models import StoreStatus, TimeZone, MenuHours, StoreResult, UuidMapping
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import connections, connection
from django.http import HttpResponse
from ulid import ULID
import time, datetime
from asgiref.sync import sync_to_async
import tracemalloc

tracemalloc.start()


@method_decorator(csrf_exempt, name="dispatch")
class create_report(View):
    @csrf_exempt
    async def post(self, request):
        unique_id = ULID.from_timestamp(time.time())
        print('getting the async function start', unique_id)
        async_function = self.process_data(unique_id)
        loop = asyncio.get_event_loop()
        loop.create_task(async_function)
        # sync_to_async(async_function)  # or async_function
        # asyncio.to_thread(async_function)
        return HttpResponse('ok')


    async def process_data(self, unique_id):
        try:
            UuidMap = UuidMapping()
            result = StoreResult()
            UuidMap.uuid = unique_id
            instance = UuidMap.save()
            id = instance[0].id
            calcutateLastHourUptime(id)
            calculateLastDayUptime(id)
            calculateLastWeekUptime(id)
            calculateLastHourDowntime(id)
            calculateLastWeekDowntime(id)
            calculateLastDayDowntime(id)

            print('inside the async function', unique_id)
        except Exception as e:
            print(e)
        return "task_complete"


    def calculateLastHourUptime():
        StoreStatus.object.filter()

@method_decorator(csrf_exempt, name="dispatch")
class get_report(View):
    @csrf_exempt
    def get(self, request):
        pass
