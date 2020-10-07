from browser import Browser

class HeaderPageElements(object):
    INPUT_BUSCA = '#id-search-field'
    BUTTON_OK = '#submit'

class HeaderPage(Browser):
    def preenche_input_busca(self, texto):
        self.driver.find_element_by_css_selector(HeaderPageElements.INPUT_BUSCA).send_keys(texto)

    def click_btn_go(self):
        self.driver.find_element_by_css_selector(HeaderPageElements.BUTTON_OK).click()