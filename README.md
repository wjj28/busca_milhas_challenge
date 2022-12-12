# busca_milhas_Lenovo_challenge


## Description

* Go to [webscraper.io](https://webscraper.io/test-sites/e-commerce/allinone/) and get all Lenovo notebooks sorted from the cheapest to the most expensive.

* For optimization purposes,the collected data is stored in a JSON file


## Getting Started

### Framework used
* Flask

 ### Packages used
 * Selenium
 * JSON
 * Jsonify
 * Render_template
 
  ### Driver used
 * [Chrome driver](https://chromedriver.chromium.org/downloads)
 
 Executable driver path needs to be set in  [ line 6 ]
 ```
getting_all_files.py  👉🏿  (executable_path=driver_path)
``` 

 

## Note📝
### The project is divided in 2 phases: 
* Collecting the laptops information
* Render the page where all the information will be displayed

### Running the Project

Git Clone this repository:

```
git clone https://github.com/wjj28/busca_milhas_challenge.git
```

CD into the project folder:

```
cd busca_milhas_challenge
```

Collect the data and store it as JSON
```
import2json.py
```

Render the webpage to get all the data
```
restful_api.py
```


### Objectives Breakdown
* Collect all the Lenovo laptops' links from the website
* Collect every single information available for each laptop
* Sort the laptops by price (from cheapest to the most expensive)
* Save the results into a JSON file 
* Generate a RESTful API to display the laptops' information in JSON format


### What Was Successfully Accomplished
* Collecting all the Lenovo laptops' info ✔
* Collecting the prices for the different HDD of each laptop ✔
* Sorting the laptops by price ✔
* Saving the results into a JSON file ✔
* Generate a RESTful API to display the laptops' information in JSON format ✔

### Built With

* [Python](https://www.python.org/) - The Programming Language
* [Pycharm](https://www.jetbrains.com/pycharm/) - The Code Editor



