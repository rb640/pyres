from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('reports.views',
	# Example:
    # (r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	('^profit_report/$', 'profit_report'),
	('^ready_reports_list/$', 'ready_reports_list'),
	('^report_view/$', 'report_view'),
	('^profit_region_report/$', 'profit_region_report'),
	('^create_report/$', 'create_report'),	
)
