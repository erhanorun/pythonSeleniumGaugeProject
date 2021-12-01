from BasePackage.base_page import BasePage


class CasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.get(self.read_props().get('data', 'url'))
        assert self.driver.current_url == self.read_props().get('data', 'url')
        self.click_element_by_xpath("//*[@id='type'][text() = 'GİRİŞ YAP']")
        self.click_element_by_xpath("//*[@href='/login?returnUrl=%2F&logtab=signin']")
        self.find_element_by_id("email").send_keys(self.read_props().get('data', 'mail'))
        self.find_element_by_id("pass").send_keys(self.read_props().get('data', 'pass'))
        self.click_element_by_id("login-button")

    def add_favourite(self):
        CasePage.login(self)
        self.find_element_by_id("navbar-search-input").send_keys("samsung")
        self.click_element_by_xpath("//*[@class='search__button']")
        self.click_element_by_xpath("//*[@id='product-list-container']/div/div/div[4]/div[3]/nav/ul/li[2]/a[text() = '2']")
        assert self.find_element_by_xpath("//*[@class='pagination__item active']/a").text == "2"
        product_list = self.driver.find_elements_by_class_name("product-list__product-name")
        product_codes = self.driver.find_elements_by_class_name("product-list__product-code")
        product_code = product_codes.__getitem__(2).text
        product_list.__getitem__(2).click()
        self.click_element_by_id("fav_Icon")
        self.click_element_by_xpath("//*[@id='modal-favorite']//*[@title='Close']")
        self.click_element_by_id("btnMyAccount")
        self.click_element_by_xpath("//*[@href='/uyeBilgi/favorilistem']")
        assert self.find_element_by_xpath("//*[@class='basket-cart__product-name']/span").text == product_code
        self.click_element_by_xpath("//*[@class='basket-cart__product-remove']/i")
        self.verify_element_not_exist_by_xpath("//*[@class='basket-cart__product-remove']/i")
