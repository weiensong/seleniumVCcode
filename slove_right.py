import random
import time
from abc import ABC

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains

from robot import Robot


class SloveRight(Robot, ABC):
    def __init__(self, default_config):
        super().__init__(default_config)

    def test_slove_right(self):
        if not self.wait_ele_xpath_safe('//*[@class="handler animate" and last() ]'):
            print('未发现滑块,跳过')
            return
        for _ in range(3):
            try:
                if not self.wait_ele_xpath_safe('//*[@class="drag_text" and text()="验证通过"]'):
                    button = self.find_ele_xpath('//*[@class="handler animate" and last() ]')
                    ActionChains(self.driver).click_and_hold(button).perform()
                    ActionChains(self.driver).move_by_offset(random.randint(60, 100), 0).perform()
                    time.sleep(0.1)

                    ActionChains(self.driver).click_and_hold(button).perform()
                    ActionChains(self.driver).move_by_offset(random.randint(160, 200), 0).perform()
                    time.sleep(0.1)

                    ActionChains(self.driver).click_and_hold(button).perform()
                    ActionChains(self.driver).move_by_offset(360, 0).perform()
                    ActionChains(self.driver).release(button).perform()
                    time.sleep(1)
                else:
                    break
            except StaleElementReferenceException:
                self.find_ele_xpath('//*[@id="dom_id"]/div/span/a').click()
