import asyncio
from django.http import HttpResponse
from django.views import View
from store_monitoring.models import StoreStatus, TimeZone, MenuHours
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import connections, connection
from django.http import HttpResponse
from ulid import ULID
import time, datetime


@method_decorator(csrf_exempt, name="dispatch")
class create_report(View):
    @csrf_exempt
    async def post(self, request):
        unique_id = ULID.from_timestamp(time.time())
        print('getting the async function start', unique_id)
        asyncio.create_task(self.process_data(unique_id))
        return HttpResponse('ok')

    async def process_data(self, unique_id):
        await asyncio.sleep(10)
        print('inside the async function', unique_id)
        return "task_complete"


@method_decorator(csrf_exempt, name="dispatch")
class get_report(View):
    @csrf_exempt
    def get(self, request):
        pass
