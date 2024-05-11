from selenium import webdriver

def before_all(context):
    print("Começou")
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)

def before_scenario(context, scenario):
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

def after_scenario(context, scenario):
    print()
    print("Video baixado com sucesso!")

def after_all(context):
    context.driver.quit()

