import kronos
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from screenshots.models import Website

@kronos.register('*/5 * * * *')
def take_screenshots():
    print "Take Screenshots Running....."
    websites = Website.objects.all()
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0")
    driver = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs',desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
    driver.set_window_size(2000, 1500)
    for website in websites:
        if website.screenshot:
            screenshot_name = website.screenshot
        else:
            screenshot_name = int(round(time.time() * 1000))
        driver.get(website.link)
        time.sleep(2)
        driver.save_screenshot("/home/patidar/work/Python/web_screenshots/static/img/%s.png"%(screenshot_name))
        website.screenshot = screenshot_name
        website.save()
    print "Take Screenshots Ending....."