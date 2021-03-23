from selenium.webdriver.common.by import By



def black_list(fun):
    def wapper(*args,**kwargs):
        # 避免循环导入
        from pageobject.base_page import BasePage
        # 黑名单
        black_list_s = [(By.CSS_SELECTOR, 'button.ivu-btn-primary1')]
        #
        instance:BasePage = args[0]
        try:
            element = fun(*args,**kwargs)
            # print("没有弹窗1")
            return element
        except Exception as e:
            for i in black_list_s:
                elements = instance.finds(*i)
                if len(elements) > 0:
                    elements[0].click()
                    # print("点击弹窗")
                if len(elements) == 0:
                    # print("没有这个元素")
                    raise e
        return wapper
    return wapper