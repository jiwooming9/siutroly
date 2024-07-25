from playwright.sync_api import sync_playwright,Playwright, TimeoutError as PlaywrightTimeoutError
import playwright
import time

class VNeIDPage:
    def __init__(self, playwright: Playwright):
        self.province = "Quảng Ninh"
        self.district = "Thành phố Hạ Long"
        self.village = "Phường Hà Tu"
        self.districthtml = "halong"
        self.villagehtml = "hatu"
        self.trangthaidn = ''
        self.log=[]
        self.CT_infor = {}
        self.login_suc = False
        playwright = sync_playwright().start()
        self.browser = playwright.firefox.launch(headless=True)
        self.context = self.browser.new_context(ignore_https_errors=True, no_viewport=True)
        self.page = self.context.new_page()
        self.page.set_default_timeout(30000)
        self.page.goto("https://dichvucong.dancuquocgia.gov.vn/portal/p/home/dvc-gioi-thieu.html")
        self.page.get_by_role("link", name="Đăng nhập").click()
        self.page.locator("xpath=//img[@src='p/home/img/header/quoc_huy.png']").click()
        self.page.locator('#idp-name2').click()

    def get_active_day(self):
        table = self.page.locator("table")
        cells = table.locator("td")
        selected_date_label = self.page.locator("#lblselectedDate")

        for cell in cells.element_handles():
            cell.click() 
            current_date = selected_date_label.inner_text()
            if current_date:
                self.page.locator("#btnNEXT_TAB_4").click()
                break 
        self.page.locator("#btnFinishPage2").click()

    def spam(self):
        self.page.goto("https://dichvucong.dancuquocgia.gov.vn/portal/p/home/dvc-CCCD-tren-14-tuoi.html?csrt=3703838003069409130")
        self.page.locator("#txtPHONE_NUMBER_NDN").fill("0359996643")
        self.page.locator("#select2-cboLyDoCap-container").click()
        self.page.locator("xpath=/html/body/span/span/span[1]/input").fill("chip")
        self.page.keyboard.press('Enter')
        self.page.locator("#chkCapTinh").click()
        self.page.locator("#select2-cboORGTinh-container").click()
        self.page.locator("xpath=/html/body/span/span/span[1]/input").fill("Quảng Ninh")
        self.page.keyboard.press('Enter')
        self.page.locator("#chkRULE").click()
        self.page.locator("#btnSaveNextToPage2").click()
        self.get_active_day()
    
lmao = VNeIDPage(Playwright)
while(True):
    lmao.spam()
    time.sleep(5)
