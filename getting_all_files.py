from collect_links import all_lenovo_notebooks

from selenium import webdriver

# Driver path
driver_path = " "

driver = webdriver.Chrome(executable_path=driver_path)

# all lenovo laptops
all_laptops = []

for url in all_lenovo_notebooks:
    driver.get(url)

    # All laptops are under the css element thumbnail
    laptops_brand = driver.find_elements_by_css_selector(".thumbnail .row")

    # hdd size
    new_hdd_size = []

    # hdd price
    new_hdd_price = []

    # stored hdd prices
    hdd_prices = {}

    for laptop in laptops_brand:

        # notebook name
        notebook_name = laptop.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text

        # image
        image = laptop.find_element_by_tag_name("img").get_attribute("src")

        # rating
        rating = laptop.find_elements_by_css_selector(".ratings .glyphicon")
        stars = len(rating)

        # description
        notebook_description = laptop.find_element_by_class_name("description").text.strip()

        # hdd size
        swatches_length = laptop.find_elements_by_css_selector(".swatches button")

        # hdd size length
        hdd_length = len(swatches_length)

        for i in range(1, hdd_length):
            hdd_size = laptop.find_element_by_xpath(
                f'/ html / body / div[1] / div[3] / div / div[2] / div / div / div[2] / '
                f'div[2] / button[{i}]').text

            laptop.find_element_by_xpath(f'/ html / body / div[1] / div[3] / div / div[2] / div / div / div[2] / '
                                         f'div[2] / button[{i}]').click()

            notebook_price = laptop.find_element_by_class_name("price").text

            notebook_review = laptop.find_element_by_class_name("ratings").text

            # store hdd size into hdd list
            new_hdd_size.append(hdd_size)

            # splitting and converting the price to float value
            price = notebook_price.split("$")
            float_price = float(price[1])

            # store hdd price into hdd list
            new_hdd_price.append(float_price)

            # splitting and converting the review to int value
            review = notebook_review.split()
            int_review = int(review[0])

            # Store the hdd size & price key-value pair into a dictionary
            hdd_prices.update({hdd_size: float_price})

    # storing the lenovo notebooks information in a dict
    lenovo_notebook = {
        'Image': image,
        'Model': notebook_name,
        'Description': notebook_description,
        "Link": url,
        'Price': hdd_prices,
        'Rating': stars,
        'Reviews': int_review
    }

    all_laptops.append(lenovo_notebook)

print(len(all_laptops))

driver.quit()
