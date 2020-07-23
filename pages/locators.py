from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > .btn[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD1_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD2_INPUT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
