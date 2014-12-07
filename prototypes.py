import sys
from django.conf import settings

settings.configure(
	DEBUG=True,
	SECRET_KEY='N1mqPak4p2sqm6p#+8l8fyxf+ox(le)8&jh_5^sxa!=2!-wxj0',
	ROOT_URLCONF='rapidprototype.urls',
	MIDDLEWARE_CLASSES=(),
	INSTALLED_APPS=(
		'django.contrib.staticfiles',
		'django.contrib.webdesign',
		'rapidprototype'
		),
	STATIC_URL='/static/'
	)

if __name__ == '__main__':
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)