 # coding: utf-8
import sys
sys.path.append("C:\Python27\Lib\site-packages\lxml-2.3beta1-py2.7-win32.egg")
from celery.decorators import task
from django.db import connection
from lxml import etree


@task()
def report_generator(sql_query,xml_report_name,name_of_rows):
	cursor = connection.cursor()
	cursor.execute(sql_query)
		
	results = etree.Element("RESULTS")		
	for rows in cursor.fetchall():
		i=0
		xml_row = etree.SubElement(results, "ROW")
		for row in rows:			
			etree.SubElement(xml_row, "COLUMN", NAME=name_of_rows[i]).text = unicode(row)
			i+=1
					
	handle = etree.tostring(results, pretty_print=True, xml_declaration=True, encoding='utf-8')
	applic = open("C:\\djcode\\portal\\xml\\"+xml_report_name, "w")
	applic.writelines(handle)
	applic.close()
	