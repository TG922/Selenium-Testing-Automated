from selenium import webdriver
import time

import requests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.thesparksfoundationsingapore.org/')


print("\n \n************** Let's Check For The TestCases *********************\n")

########################## TestCase 1: Title ###############################

print("TestCase #1:")
if(driver.title):
    print("Title Verification Successful: ",driver.title)
else:
    print("Title Verification Failed!\n")


########################## TestCase 2: Home button #########################

print("TestCase #2:")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")


########################## TestCase 3: Check if navbar appears #########################

print("TestCase #3:")
try:
    driver.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")


######################## TestCase 4: Scrolling down ########################################

print("TestCase #4:")
for i in range(0,1500,200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("scrolled down")



###################### TestCase 5: scrolling up ######################################

print("TestCase #5:")
driver.find_element_by_id("toTopHover").click()
time.sleep(1)
print("scrolled up")


########################## TestCase 6: About Us Page #########################

print("TestCase #6:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)

    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)


########################## TestCase 7: Policies and Code #########################

print('TestCase #7:')
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)


########################## TestCase 8: Workshop page #########################

print('TestCase #8:')
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    driver.find_element_by_link_text('LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')


########################## TestCase 9: Links Page #########################

print("TestCase #9")
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    driver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    driver.find_element_by_link_text('Visit LINKS @TSF').click()
    time.sleep(3)
    print('LINKS Verfication successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")


########################## TestCase 10: Check If Logo Exists #########################

print('TestCase #10:')
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')


########################## TestCase 11:   Check the Form #########################

print("TestCase #11:")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    driver.find_element_by_name('Name').send_keys('Tarun')
    time.sleep(3)
    driver.find_element_by_name('Email').send_keys('gaurtarun@gmail.com')
    time.sleep(3)
    select =Select(driver.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)


# ########################## TestCase 12:   Check the Contact us Page #########################

print("TestCase #12:")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(1)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)
   
    
    if(info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')
   
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")


# ########################## TestCase 13: again back to main page #########################

print("TestCase #13:")
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/h1/a").click()
print(" again back to main page")
time.sleep(3)


# ########################## TestCase 14:  clicking 1-6 #########################

print("TestCase #14:")

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[2]/a").click()
print(" clicked 2 internships ")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
print(" clicked 3 Mentorship ")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
print(" clicked 4 support ")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
print(" clicked 5 scholarships ")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
print(" clicked 6 community ")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
print("scrolled 500px")


# ########################## TestCase 15: iframe for youtube #########################

print("TestCase #15:")

required_frame = driver.find_element_by_xpath("//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
driver.switch_to.frame(required_frame) 

element = driver.find_element_by_xpath("//button[@aria-label='Play']")
element.click()

print("YouTube video played")

time.sleep(10)
stop = driver.find_element_by_xpath("/html/body/div/div/div[1]/video").click()
print("Pause Video\n")
time.sleep(1.5)

driver.refresh()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print("page refreshed & Scrolled down\n")
time.sleep(2)

# ########################## TestCase 16: Jobs at Angel.co Portal #########################

print("TestCase #16:")

driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a").click()
print("Jobs at Angel.co Portal page:- Success\n")
time.sleep(8)


# ########################## TestCase 17: Jobs at Tech in Asia Portal #########################

print("TestCase #17:")

driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a").click()
print("Jobs at Tech in Asia Portal page:- Success\n")
time.sleep(8)


# ########################## TestCase 18: Code for India page #########################

print("TestCase #18:")

driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]/ul/li[3]/a").click()
print("Code for India page:- Success\n")
time.sleep(8)


# ########################## TestCase 19: Internships at Internshala ##################

print("TestCase #19:")

driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[3]/ul/li/a").click()
print("Internships at Internshala page:- Success\n")
time.sleep(5)




