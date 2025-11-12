import os, sys, pathlib, django
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_news.settings')
django.setup()

from django.test import RequestFactory
from main.views import show_json

rf = RequestFactory()
req = rf.get('/json/')

try:
    resp = show_json(req)
    print('Response type:', type(resp))
    print('Status code:', getattr(resp, 'status_code', None))
    # Try to print JSON content
    if hasattr(resp, 'content'):
        print(resp.content[:1000])
except Exception as e:
    import traceback
    traceback.print_exc()
