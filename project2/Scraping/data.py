import datetime
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




s=Service(ChromeDriverManager().install())


month=["pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000000","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000030","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000061","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000091","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000122","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000152","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000183","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000213","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000244","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000275","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000305","pps_0a2f09577a224be78d590adfb91145c7tree-view-control0000336"] 

num=0
this=month[num]

f = open(str(num)+'.csv', "w")


driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.moj.gov.sa/ar/opendata/bi/birealestate/Dashboards/100_kpiDistrict/101_Monthly/kpi101_04.aspx#")

select = Select(WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.NAME, 'pps_9cff892d90c34d10b920290a355684fcSelect'))))

all_options = [o.get_attribute('value') for o in select.options]
select.select_by_value('CB174D0AA2D07A7E66E98E39B7E570BE')

time.sleep(3)

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.ID, 'pps-tree-label-pps_bc4df99f7ddf4407b566bcb3f37376f4tree-view-control'))).click()
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.ID, 'pps-tree-selector-pps_bc4df99f7ddf4407b566bcb3f37376f4tree-view-control'))).click()
driver.find_element(By.CSS_SELECTOR,'#pps-tree-apply-pps_bc4df99f7ddf4407b566bcb3f37376f4tree-view-control').click()
time.sleep(3)

count=0

time.sleep(3)
WebDriverWait(driver, 3).until(
EC.presence_of_element_located(
    (By.ID, 'pps-tree-label-text-pps_0a2f09577a224be78d590adfb91145c7tree-view-control'))).click()
time.sleep(3)

x=driver.find_element(By.ID, this )
driver.execute_script("arguments[0].click();", x)



time.sleep(3)

findAll= WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.ID, 'olap_toolbar_ti_appi')))
time.sleep(3)
findAll.click()

time.sleep(13)


tbody = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'ms-bigrid-table')))

for row in tbody.find_elements(By.XPATH , './/tr')[1:]:
    row_elements = [td.text for td in row.find_elements(By.XPATH,".//td")]
    transaction_number = int(row_elements[4])
    data =  row_elements[0]+","+(row_elements[5].split()[1].translate(str.maketrans('', '', string.punctuation)))+","+(row_elements[6].translate(str.maketrans('', '', string.punctuation)))+"\n"
    count += 1
    print(count)
    f.write(str(data))
f.close()
   