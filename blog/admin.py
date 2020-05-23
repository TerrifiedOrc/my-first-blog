from django.contrib import admin
from .models import Post
from .models import CV
from .models import Education
from .models import Employment

admin.site.register(Post)

admin.site.register(CV)

admin.site.register(Education)

admin.site.register(Employment)