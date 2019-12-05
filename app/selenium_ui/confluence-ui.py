from selenium_ui.confluence import modules


# this action should be the first one
def test_0_selenium_a_login(webdriver, confluence_datasets, confluence_screen_shots):
    modules.login(webdriver, confluence_datasets)


def test_1_selenium_view_page(webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_page(webdriver, confluence_datasets)


def test_1_selenium_create_page(webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_page(webdriver, confluence_datasets)


def test_1_selenium_edit_page(webdriver, confluence_datasets, confluence_screen_shots):
    modules.edit_page(webdriver, confluence_datasets)


def test_1_selenium_create_comment(webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_comment(webdriver, confluence_datasets)


def test_1_selenium_view_blog(webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_blog(webdriver, confluence_datasets)


def test_1_selenium_view_dashboard(webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_dashboard(webdriver, confluence_datasets)


""" Add custom actions anywhere between login and log out action. Move this to a different line as needed.
    Write your custom selenium scripts in `../extension/extension.py`. Refer to `modules.py` for examples.
"""
# def test_1_selenium_custom_action(webdriver, confluence_datasets, confluence_screen_shots):
#     modules.custom_action(webdriver, confluence_datasets)


# this action should be the last one
def test_2_selenium_z_log_out(webdriver, confluence_datasets, confluence_screen_shots):
    modules.log_out(webdriver, confluence_datasets)