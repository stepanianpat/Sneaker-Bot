from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('/Users/patrick/Downloads/chromedriver')

driver.get("http://www.footlocker.com/");

driver.find_element_by_xpath('//*[@id="navigation-links"]/ul[1]/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="shop_sub_menu_top"]/ul').click()

driver.find_element_by_xpath('//*[@id="shop_sub_menu_top"]/ul/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="navigation-dropdown"]/div[1]/div[2]/div[2]').click()

driver.find_element_by_xpath('//*[@id="group_Product_Type"]/li[1]/a').click()

driver.find_element_by_xpath('//*[@id="endeca_search_results"]/ul/li[1]/p[1]').click()

driver.find_element_by_name('//*[@id="quickviewMoreInfo"]').click()



# driver.find_element_by_xpath('//*[@id="quickview_product_form"]').click()

# driver.find_element_by_xpath('//*[@id="quickview_product_form"]').click()
# driver.find_element_by_xpath('//*[@id="quickview_product_form"]').click()





# men = driver.find_elemedriver.nt_by_css_selector(".navigation-gender-men .top-cat-link").move_to_element().

# driver.select_by_visible_text("")
