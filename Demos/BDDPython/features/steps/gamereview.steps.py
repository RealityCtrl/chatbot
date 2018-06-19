from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from hamcrest import assert_that, starts_with
import time



@given(u'the user enters \'{intent}\'')
def step_impl(context, intent):
    webpage.load_chatbot()
    webpage.text_input_box.send_keys(intent)
    webpage.text_input_box.send_keys(Keys.RETURN)
    webpage.text_input_box.clear()



@when(u'asked for the game title the user enters \'{game}\'')
def step_impl(context, game):
    webpage.wait_for_next_message()
    webpage.text_input_box.send_keys(game)
    webpage.text_input_box.send_keys(Keys.RETURN)
    webpage.text_input_box.clear()


@when(u'when asked for the game platform the user enters \'{platform}\'')
def step_impl(context, platform):
    webpage.wait_for_next_message()
    webpage.text_input_box.send_keys(platform)
    webpage.text_input_box.send_keys(Keys.RETURN)
    webpage.text_input_box.clear()



@when(u'when prompted to confirm the user enters \'{confirm}\'')
def step_impl(context, confirm):
    webpage.wait_for_next_message()
    webpage.text_input_box.send_keys(confirm)
    webpage.text_input_box.send_keys(Keys.RETURN)
    webpage.text_input_box.clear()



@then(u'the chatbot should respond with \'{fulfillment}\'')
def step_impl(context, fulfillment):
    result_message = webpage.wait_for_next_message()
    if result_message.startswith('.'): # the chatbot returns ... messages whilst it is 'thinking'
        time.sleep(2)
        result_message = webpage.get_current_message_again() # see if it has finished thinking yet
    assert_that(result_message, starts_with(fulfillment))


class WebPage:

    instance = None

    def __init__(self):
       pass

    def load_chatbot(self):
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream") # options turn off the prompt for the microphone
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.website = self.driver.get('https://gamereviewstack-codebuilddeploy-xmvz-webappbucket-71jwxn1oy8i0.s3.amazonaws.com/index.html')
        self.number_of_messages = 1
        self.wait_for_next_message()
        self.text_input_box = self.driver.find_element_by_id('text-input')

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebPage()
        return cls.instance



    def wait_for_next_message(self):
        latest_message_from_bot = ''
        try:
            delay = 3  # this is a timeoout delay in seconds
            css_selector = '.message-bot:nth-child(' + str(self.number_of_messages) + ')'
            print('waiting for ' + css_selector)
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            time.sleep(2) # needs a brief pause to allow the chatbot time to put some content in the field
            latest_message_element = self.driver.find_element_by_css_selector(css_selector=css_selector)
            latest_message_from_bot = latest_message_element.text
            print('message received: ' + latest_message_from_bot)
            self.number_of_messages=self.number_of_messages+2 # it is two because every other one is from the human
        except TimeoutException:
            print("Loading took too much time!")
        return latest_message_from_bot


    def get_current_message_again(self):
        css_selector = '.message-bot:nth-child(' + str(self.number_of_messages-2) + ')'
        print('trying again for ' + css_selector)
        latest_message_element = self.driver.find_element_by_css_selector(css_selector=css_selector)
        latest_message_from_bot = latest_message_element.text
        print('message received: ' + latest_message_from_bot)
        return latest_message_from_bot


webpage = WebPage.get_instance()



