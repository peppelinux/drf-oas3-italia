[![License](https://img.shields.io/github/license/peppelinux/drf-oas3-italia.svg)](https://github.com/peppelinux/drf-oas3-italia/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/peppelinux/drf-oas3-italia.svg)](https://github.com/peppelinux/drf-oas3-italia/issues)

# Django Rest Framework italia OpenAPIv3

Django application on top of DRF that implements the [Italian Interpolability Guideline for PA](https://docs.italia.it/italia/piano-triennale-ict/lg-modellointeroperabilita-docs/it/bozza/doc/profili-di-interazione/regole-comuni-rest-soap.html)


# Setup

````
pip install drf_italia
````

In your django project include `drf_italia` in `settings.INSTALLED_APPS`.

# Usage


This is an example `urls.py` file about how get the things working.

````
from django.conf import settings
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view
from rest_framework.schemas.agid_schema_views import get_schema_view

from rest_framework.schemas.openapi_agid import AgidSchemaGenerator as openapi_agid_generator


from . import views
from . import api_views

app_name = 'ricerca'
base_url = 'api/ricerca'

agid_api_dict = {'title': "Unical - Ricerca",
                 #  'generator_class': openapi_agid_generator,
                 'permission_classes': (permissions.AllowAny,),
                 'description': "OpenData per la Ricerca in Unical",
                 'termsOfService': 'https://tos.unical.it',
                 'x-api-id': '00000000-0000-0000-0000-000000000001',
                 'x-summary': 'OpenData per la Ricerca in Unical',
                 'license': dict(name='apache2',
                                 url='http://www.apache.org/licenses/LICENSE-2.0.html'),
                 'servers': [dict(description='description',
                                  url='https://storage.portale.unical.it'),
                             dict(description='description',
                                  url='https://ricerca.unical.it')],
                 'tags': [dict(description='description',
                               name='api'),
                          dict(description='description',
                               name='public')],
                 'contact': dict(email = 'giuseppe.demarco@unical.it',
                                 name = 'Giuseppe De Marco',
                                 url = 'https://github.com/UniversitaDellaCalabria'),
                 'version': "0.1.2"
}

urlpatterns = [
    # here other urls definitions ...
]

if 'rest_framework' in settings.INSTALLED_APPS:
    router = routers.DefaultRouter()
    #  router.register('api/ricerca', api_views.ApiDocenteViewSet)
    urlpatterns += path('api', include(router.urls)),

    # dynamic Schema export resource
    urlpatterns += path('openapi',
                        get_schema_view(**agid_api_dict),
                        name='openapi-schema'),

    # API Views then follows up ...
    urlpatterns += path('{}/docenti/'.format(base_url),
                        api_views.ApiDocenteList.as_view()),
    urlpatterns += path('{}/docente/<int:pk>/'.format(base_url),
                        api_views.ApiDocenteDetail.as_view()),

    # ...
````
