from tests.fixtures import TEST_USER


def test_login(selenium):
    selenium.implicitly_wait(10)
    selenium.set_window_size(1124, 850)
    selenium.get('http://127.0.0.1:8000')
    selenium.find_element_by_id("navbar-login").click()
    assert selenium.title == "StarterWeppy | Account"
    email_input = selenium.find_element_by_id("email")
    email_input.clear()
    email_input.send_keys(TEST_USER.email)
    password_input = selenium.find_element_by_id("password")
    password_input.send_keys(TEST_USER.password)
    login_btn = selenium.find_element_by_css_selector("form > div:nth-child(4) > input")
    login_btn.click()
    loggedin_header = selenium.find_element_by_id("loggedin-header")
    assert loggedin_header.text == "Profile"
