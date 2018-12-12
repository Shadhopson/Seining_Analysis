from bs4 import BeautifulSoup
import requests
start_site = "https://tidesandcurrents.noaa.gov/api/datagetter?product=water_temperature&begin_date="
start_date = 20080501
middle_site = "&end_date="
end_date = 20181101
end_site = "&station=8518750&time_zone=lst_ldt&units=english&interval=h&format=json&application=NOS.COOPS.TAC.PHYSOCEAN"
#r = requests.get(start_site + start_date + middle_site + end_date + end_site)
#data = r.text
def get_data_from_noaa(product, start_date, end_date):
    start_site  = "https://tidesandcurrents.noaa.gov/api/datagetter?product="
    beg_mid = "&begin_date="
    middle_site = "&end_date="
    end_site = "&station=8518750&time_zone=lst_ldt&units=english&interval=h&format=json&application=NOS.COOPS.TAC.PHYSOCEAN"
    while start_date < end_date:
        print (start_date, start_date + 600)
        full_site = start_site+product+beg_mid+str(start_date)+middle_site +str(start_date+600) +end_site
        
        r = requests.get(full_site)

        data = r.text
        write_to = product+"_data/"+product+str(start_date)[:4]+'.json'
        f = open(write_to,"w")
        f.write(data)
        f.close()
        start_date += 10000


get_data_from_noaa('water_temperature',20080501,20181101)
