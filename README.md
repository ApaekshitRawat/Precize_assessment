## Python script that fulfills the following requirements:

* Prompt the user to enter the name of a city.
* Retrieve the top 10 restaurants in the specified city based on the food, comparing ratings and reviews through a Google search.
* Store the collected restaurant data in a JSON file, using the restaurant names as keys and their relevant details (such as ratings and reviews) as values.




For getting the user to enter the city name , I have added the command line support , in the terminal use this command to trigger the test - 
```
pytest test_main.py --city="city name"

```
( add city name of your choice )



> * Here I have used POM(page object model) approach to seperate the test logic from the methods and fields.
> * Result_page.py class is the page class containing the locators and methods for the functinality
> * test_main.py is the test class where test logic is written , here I am calling methods from the page class
> * conftest.py is the pytest class where pytest fixtures are written to handle the setup / teardown logic and input from command line

