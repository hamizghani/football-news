import os
import sys
import pathlib
import django

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_news.settings')
django.setup()

from django.test import Client
import json

c = Client()
resp = c.get('/json/')
print('Status:', resp.status_code)
try:
    parsed = resp.json()
    print(json.dumps(parsed, indent=2, ensure_ascii=False))
except Exception as e:
    print('Response content:', resp.content)
    print('Error parsing JSON:', e)
