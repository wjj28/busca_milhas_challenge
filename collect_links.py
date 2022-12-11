from selenium import webdriver

# Chrome Driver
chrome_driver_path = "C:/additional_packages/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#website link
url = "https://webscraper.io/test-sites/e-commerce/allinone"

driver.get(url)

#find computers tab in the main page
computer_tab = driver.find_element_by_link_text("Computers")

#click on the tab link to see all the computer devices
computer_tab.click()


#find laptops tab in the computer page
laptops_tab = driver.find_element_by_link_text("Laptops")

#click on the tab link to see all the laptop devices
laptops_tab.click()


# target brand
brand = 'lenovo'

# # All laptops are under the css element thumbnail
laptops_brand = driver.find_elements_by_css_selector(".thumbnail")

all_lenovo_notebooks = []

# go through all the laptop brands to find the brand we want ("LENOVO")
for laptop in laptops_brand:

    brands_result = laptop.find_element_by_class_name("title").text

    # check if the notebook is 'Lenovo'
    if brand in brands_result.lower():

        # storing the lenovo notebooks in a dict
        lenovo_notebook = laptop.find_element_by_tag_name("a").get_attribute("href")

        # print(lenovo_notebook)

        all_lenovo_notebooks.append(lenovo_notebook)
print(f'Lenovo Laptops: {all_lenovo_notebooks}')

driver.quit()


