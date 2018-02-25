def test_demo_check_logo(I):
    I.open_a_webpage("http://www.google.com")
    I.fill_field("gsfi", "Comcast")
    # Click search
    I.click("btnK")
    I.see_element("Digital Cable")
    I.click("Digital Cable")
    I.scroll_to_bottom()
    I.see_element("Press Room")
    I.click("Press Room")
    I.see_element("navigation__logo")
    I.say("The Logo is visible, as expected")
    I.quit()
