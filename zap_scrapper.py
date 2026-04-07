from bs4 import BeautifulSoup, Tag
import csv
from selenium import webdriver

driver = webdriver.Firefox()

def get_url(product_name: str) -> str:
    """Returns the correct url format for the given product."""

    template = "https://www.zap.co.il/search.aspx?keyword={}"
    product_name = product_name.replace(" ", "+")
    return template.format(product_name)

# Might need to break this function to be in "main" code and not as a function
def filter_results(res):
    """Returns more precise filtered results."""

    filtered_res = []

    categories = get_categories(res)
    category = choose_category(categories)

    debug_count = 0


    for item in res:
        title_bool = is_correct_title(item)
        cat_bool = is_correct_category(item, category)
        spec_bool = is_correct_specification(item)
        #print(title_bool, cat_bool, spec_bool)
        if (title_bool
                and cat_bool
                and spec_bool):

            debug_count += 1
            filtered_res.append(item)
    print(f"found: {debug_count} correct item")
    return filtered_res

def is_correct_specification(item):
    # open correct_spec page
    specification_url = item.find("a", {"class": "more-details"})["href"]
    driver.get("https://www.zap.co.il" + specification_url)

    # scrap needed data from page
    soup_spec = BeautifulSoup(driver.page_source, "html.parser")
    #THIS IS TOO GENERIC, DO (class="specificationContainer") THEN PARMROW
    specifications_result= soup_spec.find_all("div", {"class": "paramRow"})
    print(f"🐞 has {len(specifications_result)} sections")
    specification = {}

    """print(f"Specification: {specifications_result}")
    for value in specifications_result:

        section_key = value.find("div", {"class": "ParamCol"}).text
        print(f"section key: {section_key}")

        if section_key in specification:
            specification.update(section_key, {})
        specification.update({section_key: {}})
        # print(f"Item section: {section_key}")
        section_value = value.find("div", {"class": "ParamColValue"}).text
        specification[section_key].append(section_value)

    print(specification)"""


    return True
    #compare and ask user for the intended result

def get_categories(res):
    """Returns a new array with all the categories.""" # too vague

    categories = []

    for item in res:
        category = get_item_category(item)
        categories.append(category)
    categories = list(set(categories))

    return categories

def is_correct_category(item, category: str) -> bool:
    """Returns true if the item has the correct category, false otherwise.""" # think for a word for results / x

    return get_item_category(item) == category

def get_item_category(item):
    """Returns the category of the item."""

    return item.find("a", {"class": "from-category"})["aria-label"].replace("מתוך קטגוריית ", "")

def choose_category(categories):
    """Returns the category desired by the user."""

    chosen_category = categories[0]

    if len(categories) > 1:
        header_text = "please select your desired category: "
        footer_text = "enter the index of the desired category > "

        chosen_category = handle_options(categories, header_text, footer_text)

    return chosen_category

def handle_options(lst, header: str, footer: str):
    """Displays options and Return the user desired option."""

    display_options(lst, header)
    return choose_option(lst, footer)

def display_options(lst: list[str], header: str) -> None: # maybe make header a kwarg
    """Displays option(s) from the given list of strings."""

    print(header)
    for index in range(len(lst)):
        print(f"{index + 1}. {lst[index]}")

def choose_option(lst: list[str], footer: str) -> str:
    """Returns the user desired option (should not be used singly)."""

    index = int(input(footer))
    return lst[index - 1]

def is_correct_title(item) -> bool:
    """Returns true if the item has the correct title, false otherwise."""

    item_title = item.find("span", {"data-title": ""}).text
    item_title = normalize_string(item_title)

    return is_subsequence(product, item_title)

def normalize_string(text: str) -> str:
    """Return the string in lower case with all whitespace removed."""

    return "".join(text.split()).lower()

def is_subsequence(a:str, b:str) -> bool: # CHECK WHICH AGR IS THE SHORTEST ONE
    """Checks if the first string argument is a subsequence of the second string argument."""

    a = min(a, b, key=len)
    b = max(a, b, key=len)

    min_index = 0
    max_index = 0

    while min_index < len(a) and max_index < len(b):
        if a[min_index] == b[max_index]:
            min_index += 1
            max_index += 1
        else:
            max_index += 1

    if min_index == len(a):
        return True
    return  False

def extract_record():
    print("WIP")

while True:
    divider_txt = "-" * 50
    welcome_txt = "🛒 welcome to zap.co.il CLI store 🛒"
    print(divider_txt)
    print(welcome_txt)
    print()

    # let user select amount of pages
    # should mention that it might only work for english search terms
    product = input("enter a product you would like to purchase: ")
    product_url = get_url(product)
    print(divider_txt)

    driver.get("https://www.zap.co.il/search.aspx?keyword={}".format(product))

    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = filter_results(soup.find_all("div", {"class" : "withModelRow ModelRowContainer"}))
    print(f"🐞 found: {len(results)} results before filtering")


#model_info_url = soup.find("a", {"class" : "more-details"})["href"]
#driver.get("https://www.zap.co.il" + model_info_url)

#print(model_info_url)