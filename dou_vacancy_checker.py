import sys
import os
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from lxml import html


base = 'http://jobs.dou.ua/vacancies/?'
city = '%d0%9a%d0%b8%d0%b5%d0%b2'

if len(sys.argv) > 1:
    search = sys.argv[1]
else:
    search = 'python'

# url example:
# http://jobs.dou.ua/vacancies/?search=java&city=%D0%9A%D0%B8%D0%B5%D0%B2
url = base + '&'.join((
                       'city=' + city,
                       'search=' + search,
                     ))

display = Display(visible=0, size=(800, 600))  # hidden browser
display.start()
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get(url)
source = driver.page_source


def main():
    tree = html.fromstring(source)
    # before clicking with selenium
    # vacancy_list = parse_list(tree)
    # print 'There are {} vacancies.'.format(len(vacancy_list))

    xpth = './/div[@class="more-btn"]/a'

    while more_btn_is_visible(tree):
        print 'there is "more-btn"...',
        element = driver.find_element_by_xpath(xpth)
        element.click()
        time.sleep(1)
        print 'Clicked.'
        time.sleep(1.5)
        tree = html.fromstring(driver.page_source)

    vacancy_list = parse_list(tree)
    print 'Finally:\n There are {} vacancies.'.format(len(vacancy_list))

    notify()
    driver.close()
    display.stop()


def parse_list(tree):
    vacancy_list = tree.find('.//div[@id="vacancyListId"]')
    vacancies = vacancy_list.findall('.//li[@class="l-vacancy"]')
    hot_vacancies = vacancy_list.findall('.//li[@class="l-vacancy __hot"]')
    final_vacancy_list = vacancies + hot_vacancies
    return final_vacancy_list


def more_btn_is_visible(tree):
    btn_is_present = tree.xpath('.//div/@class="more-btn"')
    if btn_is_present:
        btn_div = tree.find_class('more-btn')
        a = btn_div[0].findall('.//*')[0]
        btn_is_visible = 'display: none' not in a.attrib.get('style', '')
    return btn_is_present and btn_is_visible


def notify():
    pass


if __name__ == '__main__':
    main()
