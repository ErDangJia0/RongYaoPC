from selenium import webdriver
import csv,time
#创建浏览器对象，访问河道流量情况
url='http://xxfb.hydroinfo.gov.cn/ssIndex.html'
driver=webdriver.Chrome()
driver.get(url)
#点击查看河道水流按钮
driver.find_element_by_id('ysimg').click()
driver.find_element_by_xpath('//select[@id="stcdtype"]/option[@value="hd"]').click()
time.sleep(3)
Rlist=driver.find_elements_by_xpath('//div[@id="hdtable"]/table/tbody/tr[@class="td-show-1"] | //div[@id="hdtable"]/table//tbody/tr[@class="td-show-2"]')
for r in Rlist:
    info=r.text.split()
    if info[2]=="汾河":
        l=[
           info[0].strip(),
           info[1].strip(),
           info[2].strip(),
           info[3].strip(),
           info[4].strip(),
           info[5].strip(),
           info[6].strip(),
           info[-2].strip(),
           ]
        with open('汾河河道情况.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(l)
driver.quit()