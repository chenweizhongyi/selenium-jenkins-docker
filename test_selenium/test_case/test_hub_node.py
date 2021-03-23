from selenium import webdriver

ds = {'platform': 'ANY',
      'browserName': "chrome",
      'version': '',
      'javascriptEnabled': True
      }
dr = webdriver.Remote(command_executor='http://192.168.254.128:5001/wd/hub', desired_capabilities=ds)
dr.get("https://www.baidu.com")