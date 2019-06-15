# -*- coding: utf-8 -*-
from django.shortcuts import render

__author__ = 'xiawu@zeuux.org'
__version__ = '$Rev$'
__doc__ = """  """

from django.utils import translation

def home(request):
	language = translation.get_language()
	# for k,v in settings.SUPPORT_LANGUAGES:
	# 	if language == k:
	# 		current_language = v
	# if not current_language:
	current_language = 'English'
	# if language.startswith('zh'):
	# 	is_zh = 'selected="selected"'
	# else:
	is_en = 'selected="selected"'
	return render(request, 'ui/public/index-template.html', locals())
