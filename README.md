# Swagger
Django rest framework loyhamizga swaggerni ulash

drf-yasg kutubxonasini o'rnatish
```
pip install drf-yasg
```

`settings.py` fayliga quydagi o'zgartirishni kiritamiz

```
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]

```

va

`urls.py` fayliga ham quydagi o'zgarishni kiritamiz

```
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schem_view = get_schema_view(
    openapi.Info(
        title="Poste Api",
        default_version="1.0.0",
        description="This is api documentation",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    path("swagger/doc/", schem_view.with_ui('swagger', cache_timeout=0)),
    ...
]

```

Natijani ko'rishingiz mumkin :blush: