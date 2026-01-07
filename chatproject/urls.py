"""
URL configuration for chatproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    # include() plugs in another URLconf
    # This makes all chat app URLs available at the root
]
'''

**URL Routing Explained**:
- User visits `http://localhost:8000/` → `chat.views.index`
- JavaScript POSTs to `/chat/` → `chat.views.chat`

## Part 7: Create Templates

**Create folder structure**:

chat/
└── templates/
    └── chat/
        └── index.html
'''
