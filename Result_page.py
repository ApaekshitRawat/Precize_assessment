import json
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class Result_page:


    def __init__(self, driver):
        self.driver = driver

    # Locators for the page
    searchTextElement = (By.CSS_SELECTOR, "textarea[title=\"Search\"]")
    morePlacesElement = (By.CSS_SELECTOR, "//span[contains(text(),\"More places\")]")

    # Function with the logic to get top 10 restaurants depending on the input of city
    def get_top_restaurants(self, city_name):
        search_query = f"top 10 restaurants in {city_name}"

        search_box = self.driver.find_element(*Result_page.searchTextElement)
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        self.driver.find_element(By.XPATH, "//span[contains(text(),\"More places\")]").click()

        # Wait for results to load - could have used explicit wait if loading time was not consistent
        time.sleep(2)
        restaurant_data = {}
        try:
            # Locate result blocks
            results = self.driver.find_elements(By.XPATH,"//div[contains(@class,\"full-list\")]/div/div/div/div/div/div/div/div/div/a/div/div")

            for result in results[:10]:  # Limiting to top 10
                # Extracting restaurant names
                try:
                    name = result.find_element(By.XPATH,"./div[1]/span").text

                    print("namess are " + name)
                except:
                    continue

                # Extracting address details
                try:
                    address = result.find_element(By.XPATH,"./div[3]").text
                except:
                    address = "No details available"

                # Storing data
                restaurant_data[name] = {
                    'details': address
                }

        except Exception as e:
            print("An error occurred:", e)

        finally:
            print(restaurant_data)
            self.driver.quit()

        return restaurant_data


    # Function to save the data into a json file
    def save_to_json(self,data, city_name):

        # Defining filename with city name
        filename = f"{city_name}_top_restaurants.json"

        # Writing data to JSON file
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data saved to {filename}")