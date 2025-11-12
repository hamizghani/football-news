import os
import sys
import django
import json
import pathlib

# Ensure project root is on sys.path so Django project module is importable
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_news.settings')
django.setup()

from main.models import News

qs = News.objects.all()[:5]
result = []
for n in qs:
    def format_dt(d):
        if not d:
            return None
        from django.utils import timezone
        try:
            dt = d.astimezone(timezone.utc)
        except Exception:
            dt = d
        return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    result.append({
        'id': str(n.id),
        'title': n.title,
        'content': n.content,
        'category': n.category,
        'thumbnail': n.thumbnail,
        'news_views': n.news_views,
        'created_at': format_dt(getattr(n, 'created_at', None)),
        'is_featured': n.is_featured,
        'user_id': n.user.id if n.user else None,
    })

print(json.dumps(result, indent=2, ensure_ascii=False))
