from dataclasses import dataclass
from typing import Union

import allure
from playwright.sync_api import Page

from enums import User


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Login page behavior")
@dataclass
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    @allure.step("Login with username {username} and password {password}")
    def login(self, username: Union[User, str], password: str):
        if hasattr(username, "value"):
            self.user_name_field.fill(username.value)
        else:
            self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
