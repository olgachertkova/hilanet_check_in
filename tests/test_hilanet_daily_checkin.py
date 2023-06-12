from playwright.sync_api import Page


def test_daily_check_in(page: Page, user, password):
    print("Automatic HILANET check-in for WIX employers.\n" +
                "Version 2.01.\n" +
                "(C) Olga Chertkova, olga@chertkov.info, 2023\n" +
                "https://github.com/olgachertkova/hilanet_check_in.git\n")

    page.goto('https://wix.net.hilan.co.il/login?lang=en')
    print('--- Open site ---')
    page.locator('#user_nm').fill(user)
    print('--- Enter user number ---')
    page.locator('#password_nm').fill(password)
    print('--- Enter password ---')
    page.locator('[type="submit"]').click()
    print('--- Click Login ---')
    manual_report_button = page.locator('//div[@class="pt-1"][contains(.,"Manual reports")]')
    manual_report_button.wait_for(timeout = 50000)
    manual_report_button.click()
    page.select_option('(//td/select)[1]', 'Work from home')
    page.locator("input[value='Save']").click()
    print('--- Select type of work and save ---')
    alert_frame = page.frame_locator('iframe')
    message = alert_frame.locator('#messagePlace').inner_text()
    alert_frame.locator('#secondButton').click()
    print('--- Switch to alert window and submit ---')
    print(f'Message in alert: {message}')
    assert message == 'Data saved successfully', "UNSUCCESSFULLY"
