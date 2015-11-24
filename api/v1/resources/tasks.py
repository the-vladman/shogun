import os
from celery import Celery
import ckanapi
from ckanops import dcat_to_utf8_dict, munge, converters, upsert_dataset

celeryapp = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')
CATALOG = os.getenv('CATALOG_HOST')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


@celeryapp.task(name='tasks.harvesting')
def harvesting(url):
    catalog = dcat_to_utf8_dict(url)
    for dcat_dataset in catalog.get('dataset', []):
        ckan_dataset = converters.dcat_to_ckan(dcat_dataset)
        ckan_dataset['name'] = munge.munge_title_to_name(ckan_dataset['title'])
        ckan_dataset['state'] = 'active'
        upsert_dataset(remote, ckan_dataset)
