# coding: utf-8
# Create your views here.
import os
from time import localtime, strftime
from reports.tasks import report_generator
from django.shortcuts import render_to_response
from django.http import HttpResponse
from lxml import etree


def profit_report(request): # Отчет о начислениях
	
	moment =  strftime("%d-%m-%Y_%H.%M.%S", localtime())
	result = report_generator.delay(r"SELECT ROUND(SUM(PROFIT),4), ROUND(SUM(FIRST_COST),4), ROUND(SUM(MINUTES),4) FROM NAFIGATOR.NETCOM_PROFIT_REPORT WHERE MOMENT >= '" + str(request.GET['from_date']) + "' AND MOMENT<='" + str(request.GET['to_date']) + "'" ,
	"profit-report_"+moment+"_2010-12-01-2010-12-31.xml",
	(unicode('Начислено','utf-8'),unicode('Себестоимость','utf-8'),unicode('Кол-во минут','utf-8')))
	return HttpResponse('ok')
	
def profit_region_report(request): # Отчет о начислениях по регионам
	moment =  strftime("%d-%m-%Y_%H.%M.%S", localtime())
	result = report_generator.delay(r"SELECT * FROM NAFIGATOR.NETCOM_REGION_PROFIT_REPORT","profit-region-report_"+moment+"_2010-12-01-2010-12-31.xml",(unicode('Регион','utf-8'),unicode('Количество клиентов','utf-8'),unicode('Начислено','utf-8'),unicode('Оплачено в $','utf-8'), unicode('Оплачено в сом','utf-8')))
	return HttpResponse('ok')

def	 ready_reports_list(request): # Список готовых отчетов
	directory = "C:\\djcode\\portal\\xml\\"
	files = os.listdir(directory)
	xml_files_ext = filter(lambda x: x.endswith('.xml'), files)
	
	return render_to_response('ready_report_list.html', locals())

def	report_view(request):# просмотреть отчет
	directory = "C:\\djcode\\portal\\xml\\"
	parser = etree.XMLParser(ns_clean=True)
	tree = etree.parse(directory+request.GET['file'],parser)
	root = tree.getroot()
	
	table_values = []
	for rows in root.getchildren():
		table_values.append({'names':[],'values':[]})
		for column in rows.getchildren():
			table_values[-1]['names'].append(column.attrib['NAME'])
			table_values[-1]['values'].append(column.text)		
	return render_to_response('report_view.html', locals())
	
def create_report(request):# Создание отчета
	report_type = 'profit_report'
	return render_to_response('report_create.html', locals())