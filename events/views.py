import json
import os

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from events.models import Event, Sensor
from test_bolid import settings
from django.core.files import File



@method_decorator(csrf_exempt, name="dispatch")
class EventListView(ListView):

    model = Event

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        # events = Event.objects.all()

        search = self.object_list
        search_by_sensor = request.GET.get('sensor', None)
        if search_by_sensor:
            search = search.filter(sensor_id=search_by_sensor)

        search = search.order_by('temperature', 'humidity')

        paginator = Paginator(search, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        events = []
        for event in page_obj:
            events.append({
                'id': event.id,
                'name': event.name,
                'temperature': event.temperature,
                'humidity': event.humidity,
                'sensor_id': event.sensor_id,
            })

        response = {
            'items': events,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)


class EventDetailView(DetailView):

    model = Event

    def get(self, request, *args, **kwargs):
        event = self.get_object()

        return JsonResponse({
            'id': event.id,
            'name': event.name,
            'temperature': event.temperature,
            'humidity': event.humidity,
            'sensor_id': event.sensor_id,
        })


@method_decorator(csrf_exempt, name="dispatch")
class EventCreateView(CreateView):

    model = Event
    fields = ['id', 'name', 'temperature', 'humidity', 'sensor_id']

    def post(self, request, *args, **kwargs):

        json_data = json.loads(request.body)

        if 'temperature' not in json_data.keys():
            json_data['temperature'] = None
        if 'humidity' not in json_data.keys():
            json_data['humidity'] = None
        if 'name' not in json_data.keys():
            json_data['name'] = 'N/A'

        event = Event.objects.create(
            name=json_data['name'],
            temperature=json_data['temperature'],
            humidity=json_data['humidity'],
            sensor_id=json_data['sensor_id']
        )

        return JsonResponse({
            'id': event.id,
            'name': event.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class EventListCreateView(CreateView):

    model = Event
    fields = ['id', 'name', 'temperature', 'humidity', 'sensor_id']

    def post(self, request, *args, **kwargs):
        with open(os.path.abspath(os.getcwd())+'/data/data.json', 'r') as file:
            data = json.load(File(file))

        for item in data:
            if 'temperature' not in item.keys():
                item['temperature'] = None
            if 'humidity' not in item.keys():
                item['humidity'] = None
            if 'name' not in item.keys():
                item['name'] = 'N/A'

            Event.objects.create(
                name=item['name'],
                temperature=item['temperature'],
                humidity=item['humidity'],
                sensor_id=item['sensor_id']
            )

        return JsonResponse({
            'status': 'ok'
        }, status=201)


@method_decorator(csrf_exempt, name="dispatch")
class EventUpdateView(UpdateView):

    model = Event
    fields = ['name', 'temperature', 'humidity']

    def patch(self, request, *args, **kwargs):

        super().post(request, *args, **kwargs)
        json_data = json.loads(request.body)
        self.object.name = json_data['name']
        self.object.temperature = json_data['temperature']
        self.object.humidity = json_data['humidity']
        self.object.sensor_id = json_data['sensor_id']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'temperature': self.object.temperature,
            'humidity': self.object.humidity,
            'sensor_id': self.object.sensor_id
        })


@method_decorator(csrf_exempt, name="dispatch")
class EventDeleteView(DeleteView):

    model = Event
    success_url = "/"

    def delete(self, request, *args, **kwargs):

        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        }, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class SensorListView(ListView):

    model = Sensor

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        sensors = []
        for sensor in page_obj:
            sensors.append({
                'id': sensor.id,
                'name': sensor.name,
                'type': sensor.type
            })

        response = {
            'items': sensors,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)


class SensorDetailView(DetailView):

    model = Sensor

    def get(self, request, *args, **kwargs):
        sensor = self.get_object()

        return JsonResponse({
            'id': sensor.id,
            'name': sensor.name,
            'type': sensor.type
        })


@method_decorator(csrf_exempt, name="dispatch")
class SensorCreateView(CreateView):

    model = Sensor
    fields = ['id', 'name', 'type']

    def post(self, request, *args, **kwargs):

        json_data = json.loads(request.body)

        if 'type' not in json_data.keys():
            json_data['type'] = 1
        if 'name' not in json_data.keys():
            json_data['name'] = 'N/A'

        sensor = Sensor.objects.create(
            name=json_data['name'],
            type=json_data['type']
        )

        return JsonResponse({
            'id': sensor.id,
            'name': sensor.name,
            'type': sensor.type
        })


@method_decorator(csrf_exempt, name="dispatch")
class SensorUpdateView(UpdateView):

    model = Sensor
    fields = ['name', 'type']

    def patch(self, request, *args, **kwargs):

        super().post(request, *args, **kwargs)
        json_data = json.loads(request.body)
        self.object.name = json_data['name']
        self.object.temperature = json_data['type']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'type': self.object.type
        })


@method_decorator(csrf_exempt, name="dispatch")
class SensorDeleteView(DeleteView):

    model = Sensor
    success_url = "/"

    def delete(self, request, *args, **kwargs):

        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        }, status=200)
