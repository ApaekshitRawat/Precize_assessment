from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from Result_page import Result_page


@pytest.mark.usefixtures("setup")
class Test:
    def test_Top_10_Restrorants_in_City(self ,request):
        # Access the command-line argument
        # Enter city name -  use command in terminal --> pytest test_main.py --city="city name"
        city_name = request.config.getoption("--city")

        # Call the method in the page class
        Res= Result_page(self.driver)
        restaurant_data = Res.get_top_restaurants(city_name)

        # Now use the data and pass it to the save_to_json method
        if restaurant_data:
            # Save data to JSON
            Res.save_to_json(restaurant_data, city_name)
