import time

   import driver as driver

	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.service import Service
	from selenium import webdriver

	from selenium.webdriver.common.by import By
	service = Service(executable_path=r"F:\new\Rcm\chromedriver.exe")

	driver = webdriver.Chrome(service=service)

	driver.get("http://192.168.49.99:4000/login")

	# Locate the username and password fields and input the credentials

	username_field = driver.find_element(By.NAME, "username")
	username_field.send_keys("pappu@gmail.com")
	password_field = driver.find_element(By.NAME, "password")
	password_field.send_keys("9847344754")
	# Sbmit the login form

	password_field.send_keys(Keys.RETURN)
	# Wait for the page to load and check for the presence of the dashboard element

	dashboard_element = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div/div/div/h2")
	if dashboard_element:

	    print("Test Passed!")

	else:

  	  print("Test Failed.")
	time.sleep(5)

	# Close the browser
	driver.quit()
