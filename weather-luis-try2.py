import csv
import codecs
import urllib.request
import urllib.error
import sys

BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

ApiKey='J2SPFQATVW74M4R2LK9ESDA9W'
#UnitGroup sets the units of the output - us or metric
UnitGroup='metric'

#Location for the weather data
Location='Washington,DC'

#Optional start and end dates
#If nothing is specified, the forecast is retrieved. 
#If start date only is specified, a single historical or forecast day will be retrieved
#If both start and and end date are specified, a date range will be retrieved
StartDate = ''
EndDate=''

#JSON or CSV 
#JSON format supports daily, hourly, current conditions, weather alerts and events in a single JSON package
#CSV format requires an 'include' parameter below to indicate which table section is required
ContentType="csv"

#include sections
#values include days,hours,current,alerts
Include="days"

#basic query including location
ApiQuery=BaseURL + Location

#append the start and end date if present
if (len(StartDate)):
    ApiQuery+="/"+StartDate
    if (len(EndDate)):
        ApiQuery+="/"+EndDate

#Url is completed. Now add query parameters (could be passed as GET or POST)
ApiQuery+="?"

#append each parameter as necessary
if (len(UnitGroup)):
    ApiQuery+="&unitGroup="+UnitGroup

if (len(ContentType)):
    ApiQuery+="&contentType="+ContentType

if (len(Include)):
    ApiQuery+="&include="+Include

ApiQuery+="&key="+ApiKey

print(' - Running query URL: ', ApiQuery)
print()

try: 
    CSVBytes = urllib.request.urlopen(ApiQuery)
except urllib.error.HTTPError  as e:
    ErrorInfo= e.read().decode() 
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except  urllib.error.URLError as e:
    ErrorInfo= e.read().decode() 
    print('Error code: ', e.code,ErrorInfo)
    sys.exit()