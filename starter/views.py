# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    # Doing nothing here
    return render(request, "starter/index.html", context={},)
