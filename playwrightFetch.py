from playwright.sync_api import sync_playwright,Playwright, TimeoutError as PlaywrightTimeoutError
import playwright
from tabulate import tabulate
from docxtpl import DocxTemplate
import time
import requests
import os

tailaibtn = "xpath=//button[@class='absolute top-1/2 left-1/2 z-10 flex h-9 w-[88px] -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-md bg-red100 font-bold text-white']//*[name()='svg']//*[name()='g']//*[name()='path'][2]"
tbdangnhapsai = "xpath=//div[@class='ant-notification-notice-message']"
opt="xpath=//div[@class='ant-modal-root']//input[1]"

def notify_flask_server(message):
    url = 'http://127.0.0.1:5000/notify'
    data = {'message': message}
    response = requests.post(url, json=data)
    print(f"Notification sent: {response.status_code}")

def check_page_blank(page):
    content = page.content()
    if '<body></body>' in content:
        page.reload()
        notify_flask_server("Page is blank")

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
        self.browser = playwright.firefox.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True, no_viewport=True)
        self.page = self.context.new_page()
        self.page.set_default_timeout(30000)
        def on_response(response):
            if response.url == self.page.url:  # Check only the main document
                check_page_blank(self.page)
        
        self.page.on('response', on_response)
        
        
    
        
    
    def khoidong(self):
        self.page.goto("https://dichvucong.bocongan.gov.vn/?home=1")
        self.page.get_by_role("link", name="Đăng nhập").click()
        self.page.locator("xpath=/html/body/div[4]/div/div[1]/div/div[2]/div/div[1]/a/div").click()
        self.page.locator('#icon-2').click()
        

    def get_log(self):
        return self.log
    
    def set_log(self,log_content):
        self.log.append(log_content)

    def extract_qr_code_src(self):
        try:
            if self.page.locator(tailaibtn).count()>0:
                self.page.locator(tailaibtn).click()
            else:
                qr_locator = self.page.locator("img[alt='qr_images']")
                if qr_locator.count()>0:
                    image_src = qr_locator.get_attribute('src') 
                    return image_src
                else:
                    return ""
        except playwright._impl._errors.TimeoutError:
            return ""

    def set_trangthaiDN(self): 
        try:
            userName_check = ''
            if self.page.locator("xpath=/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[2]/table/tbody/tr[2]/td").count()>0:
                ten = self.page.locator("xpath=/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[2]/table/tbody/tr[2]/td").inner_text()
                self.trangthaidn = "thanhcong--"+ten
            elif self.page.locator(opt).count()>0:
                self.trangthaidn = 'otp'
            elif self.page.locator(tbdangnhapsai).count()>0:
                self.trangthaidn = 'không lấy được tên'
                notify_flask_server("Sai") 
        except:
            return "lỗi"

    def logout(self):
        try:
            self.page.locator("xpath=//div[@class='user-btn']//a[@type='button']").click(timeout=3000)
            self.page.locator("xpath=//div[@class='user-btn open']//a[contains(text(),'Đăng xuất')]").click()
        except PlaywrightTimeoutError:
            self.page.locator("#userLogin").click(timeout=3000)
            self.page.locator("xpath=//a[contains(text(),'Đăng xuất')]").click()
        
    def halfClose(self):
        self.trangthaidn = ''
        self.log=[]
        self.CT_infor = {}
        self.page.close()
        self.context.close()
        self.context = self.browser.new_context(ignore_https_errors=True, no_viewport=True)
        self.page = self.context.new_page()
        self.page.set_default_timeout(30000)

    def closeVN(self):
        self.trangthaidn = ''
        self.log=[]
        self.CT_infor = {}
        self.page.close()
        self.context.close()
        self.context = self.browser.new_context(ignore_https_errors=True, no_viewport=True)
        self.page = self.context.new_page()
        self.page.set_default_timeout(30000)
        self.page.goto("https://dichvucong.bocongan.gov.vn/?home=1")
        self.page.get_by_role("link", name="Đăng nhập").click()
        self.page.locator("xpath=/html/body/div[4]/div/div[1]/div/div[2]/div/div[1]/a/div").click()
        self.page.locator('#icon-2').click()

    def get_trangthaiDN(self):
        try:
            if self.trangthaidn == "thanhcong":
                kq = "không lấy được tên"
                try:
                    userName_check = self.page.locator('xpath=/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[2]/table/tbody/tr[2]/td').inner_text(timeout=10000)
                    kq = userName_check
                except:
                    return "oops"
                return self.trangthaidn +"--"+kq
            else:
                self.set_trangthaiDN()
                return self.trangthaidn
        except:
            return "lỗi"
    
    def loginstb(self):
        while not self.login_suc:
            try:
               self.page.wait_for_selector('selector_for_successful_login', timeout=55000)  # Thay thế 'selector_for_successful_login' bằng selector thực tế
               self.login_suc = True
               notify_flask_server("Login successful")
            except:
                self.page.wait_for_selector(tailaibtn)
                self.page.click(tailaibtn)  # Thay thế 'selector_for_reload_button' bằng selector thực tế

        
    def getDOB(self):
        try:
            th_selector = 'th:has-text("Ngày sinh")'
            td_selector = f'{th_selector} + td'
            td_text = self.page.locator(td_selector).text_content()
            th_selectorid = 'th:has-text("Số CMND/CCCD")'
            td_selectorid = f'{th_selectorid} + td'
            td_textid = self.page.locator(td_selectorid).text_content()
            return td_text +" "+ td_textid
        except:
            return "lỗi"
    
    def getInf(self, nguoi):
        try:
            self.page.goto("https://dichvucong.dancuquocgia.gov.vn/")
            self.page.locator("#btnLogin").click()
            self.page.get_by_role("link", name=" Cổng dịch vụ công Quốc Gia").click()
            nguoi = {}
            self.page.locator("#userLogin").click()
            self.page.get_by_role("link", name="Tra cứu thông tin công dân").click()
            time.sleep(5)
            thongtin = ["Họ tên", "Giới tính", "Tình trạng hôn nhân", "Ngày sinh", "Quốc tịch", "Dân tộc", "Tôn giáo", "Nhóm máu", "Nơi đăng ký khai sinh", "Quê quán", "Nơi ở thường trú", "Nơi ở tạm trú", "Nơi ở hiện tại", "Nơi khai báo tạm vắng"]
            giatri = ["txtFULLNAME_RESULT", "txtGENDER_RESULT", "txtMARRIAGE_RESULT", "txtDOB_RESULT", "txtNATIONALITY_RESULT", "txtETHNIC_RESULT", "txtRELIGION_RESULT", "txtBLOOD_TYPE_RESULT", "txtBIRTH_PLACE_RESULT", "txtHOME_PLACE_RESULT", "txtPERMANENT_PLACE_RESULT", "txtTEMP_RES_RESULT", "txtLIVING_RESULT", "txtABS_RES_RESULT"]
            for i in range(14):
                ttlocator = self.page.locator("p#"+giatri[i])
                ttcontent = ttlocator.inner_text()
                nguoi[thongtin[i]] = ttcontent
            #self.page.locator("#houseHoldDetail").click()
            thongtinchuho = ["Họ và tên chủ hộ", "Số CMND/CCCD/ĐDCN", "Quốc tịch", "Quan hệ với chủ hộ"]
            giatrichuho = ["house_holder-name", "house_holder-pid", "house_holder-nationality", "house_holder-relationship"]
            for i in range(4):
                ttlocator = self.page.locator("p#"+giatrichuho[i])
                ttcontent = ttlocator.inner_text()
                nguoi[thongtinchuho[i]] = ttcontent
            rows = self.page.query_selector_all("tr[data-index]")
            nguoi["Số thành viên trong hộ"] = len(rows)
            count = 1
            for row in rows:
                cells = row.query_selector_all("td")
                row_data = [cell.inner_text() for cell in cells]
                nguoi["Họ, chữ đệm, tên người " + str(count)] = row_data[1]
                nguoi["Số ĐDCN/CMND người " + str(count)] = row_data[2]
                if nguoi["Số ĐDCN/CMND người " + str(count)][3] == "0" or nguoi["Số ĐDCN/CMND người " + str(count)][3] == "2":
                    nguoi["Giới tính người " + str(count)] = "Nam"
                else:
                    nguoi["Giới tính người " + str(count)] = "Nữ"
                count += 1
            nguoi["Quận huyện làm dv"] = self.districthtml
            nguoi["Phường xã làm dv"] = self.villagehtml
            return nguoi
        except:
            nguoi={'messageER':'lỗi'}
            return nguoi
        
    # def OTPSend(self,OTParr):
    #     try:
    #         print(OTParr)
    #         self.page.locator("xpath=//div[@class='ant-modal-root']//input[1]").press(OTParr[0] + "+" + OTParr[1] + "+" + OTParr[2] + "+" + OTParr[3] + "+" + OTParr[4] + "+" + OTParr[5])
    #         self.page.locator("xpath=//span[contains(text(),'Xác nhận')]").click()
    #         self.set_trangthaiDN()
    #     except:
            
    #         return "lỗi"

    def Timkiem_CCCD(self):
        try:
            self.page.get_by_role("link", name="Nộp hồ sơ trực tuyến").click()
            self.page.fill("input[name='txtKEYWORD']", "căn cước công dân")
            self.page.get_by_role("button", name="Tìm kiếm").click()
        except:
            
            return "lỗi"

    

    def chonlydo(self):
        self.page.wait_for_load_state("load")
        self.page.locator("#select2-cboreason-container").click()
        list_options = self.page.locator("ul.select2-results__options >> li[class*='select2-results__option']")
        list_values = [option.inner_text() for option in list_options.all()]

        if len(list_values) < 2:
            reason_input = self.page.locator("input[class='select2-search__field'][type='search'][tabindex='0']")
            reason_input.fill(f"{list_values[int(0)]}")
        else:
            dic_reasions = dict(zip(range(len(list_values)),list_values))
            print(tabulate(dic_reasions.items(), headers=["Key", "Value"], tablefmt="simple"))
            answer = input("Bạn hãy chọn lý do để đổi thẻ: ")
            reason_input = self.page.locator("input[class='select2-search__field'][type='search'][tabindex='0']")
            reason_input.fill(f"{list_values[int(answer)]}")
        reason_input.press("Enter")

    
    def confirm_data(self):
        checkbox_selector = "#chkassure"
        self.page.locator(checkbox_selector).click()
        self.page.locator("#btnNEXT_TAB_3").click()

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
        self.page.locator("#btnSEND_CCCD").click()

    def Caplai_CCCD_tinh(self):
        try:
            self.page.get_by_text("Cấp lại thẻ Căn cước công dân (thực hiện tại cấp tỉnh)").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.chonlydo_caplai(0)
            input_element_T = self.page.locator('#type_T')
            input_element_T.evaluate("element => element.removeAttribute('disabled')")
            radio_button = self.page.locator("#type_T")
            radio_button.check()
            self.page.locator("#select2-cbocityOrganization-container").click()
            search_input = self.page.locator("xpath=/html/body/span/span/span[1]/input")
            search_input.fill(f"{self.province}")
            search_input.press("Enter")
            self.page.locator("#btnNEXT_TAB_2").click()
            self.confirm_data()
            self.get_active_day()
            self.set_log("Cấp lại căn cước thành công")
            # self.page.locator("#btnSEND_CCCD").click()
            self.page.wait_for_timeout(10000)
            return "Cấp lại căn cước thành công"
        except:
            print("Đã gặp lỗi")
            return "lỗi"

    def xacminh_CCCD_tinh(self):
        try:
            self.page.get_by_text("Xác nhận số Chứng minh nhân dân, Căn cước công dân  (thực hiện tại cấp tỉnh)").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.chonlydo()
            input_element_T = self.page.locator('#type_T')
            input_element_T.evaluate("element => element.removeAttribute('disabled')")
            radio_button = self.page.locator("#type_T")
            radio_button.check()
            self.page.locator("#select2-cbocityOrganization-container").click()
            search_input = self.page.locator("xpath=/html/body/span/span/span[1]/input")
            search_input.fill(f"{self.province}")
            search_input.press("Enter")
            self.page.locator("#btnNEXT_TAB_2").click()
            self.confirm_data()
            self.get_active_day()
            self.set_log("Xác minh số chứng minh nhân dân, căn cước thành công")
            return self.get_log()
        except:
            
            return "lỗi"

    def chonlydo_caplai(self, num):
        try:
        #self.page.wait_for_load_state("load")
            self.page.locator("#select2-cboreason-container").click()
            list_options = self.page.locator("ul.select2-results__options >> li[class*='select2-results__option']")

            list_values = [option.inner_text() for option in list_options.all()]
            reason_input = self.page.locator("input[class='select2-search__field'][type='search'][tabindex='0']")
            reason_input.fill(f"{list_values[num]}")
            reason_input.press("Enter")
        except:
            
            return "lỗi"

   

    
    def Doithe_CCCD_tinh(self, num):
        try:
            self.page.get_by_text("Đổi thẻ Căn cước công dân (thực hiện tại cấp tỉnh)").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.chonlydo_caplai(num)
            input_element_T = self.page.locator('#type_T')
            input_element_T.evaluate("element => element.removeAttribute('disabled')")
            radio_button = self.page.locator("#type_T")
            radio_button.check()
            self.page.locator("#select2-cbocityOrganization-container").click()
            search_input = self.page.locator("xpath=/html/body/span/span/span[1]/input")
            search_input.fill(f"{self.province}")
            search_input.press("Enter")
            self.page.locator("#btnNEXT_TAB_2").click()

            self.confirm_data()
            self.get_active_day()
            self.set_log("Xác minh số chứng minh nhân dân, căn cước thành công")
            return self.get_log()
        except:
            
            return "lỗi"

    def Timkiem_CT(self):
        try:
            self.page.get_by_role("link", name="Nộp hồ sơ trực tuyến").click()
            self.page.locator("#select2-lv_block_search-container").click()
            self.page.fill("input[class='select2-search__field']","Đăng ký, Quản lý cư trú")
            self.page.keyboard.press('Enter')
            self.page.get_by_role("button", name="Tìm kiếm").click()
        except:
            
            return "lỗi"

    #---------GIA HẠN TẠM TRÚ-----------
    def Giahan_tamtru(self, hoso):
        try:
            self.page.get_by_text("Gia hạn tạm trú").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.page.reload()

            self.page.locator("#select2-cboRECEIVE_ADDR_CITY_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.province)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_DISTRICT_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.district)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_VILLAGE_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.village)
            self.page.keyboard.press('Enter')

            coquan = self.page.locator("#txtRECEIVE_ORG_ADDRESS").text_content()
            self.CT_infor["coquandangkycutru"] = coquan

            self.page.locator("#select2-cboBPROC_CASE_CODE-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(hoso["Trường hợp"])
            self.page.keyboard.press('Enter')

            if "theo danh sách" in hoso["Trường hợp"]:  #TRƯỜNG HỢP THEO DANH SÁCH
                if hoso[1] == "Là người khai báo":      #CÁI NÀY CHƯA SỬA CẦN XEM LẠI
                    self.page.locator("#chkIS_DECLARE_TAT_LIST").check()
                else:
                    self.page.locator("#txtFULLNAME_DEPUTY").fill(hoso["Người đại diện họ và tên"])
                    self.page.select_option('#cboDATE_FORMAT_DEPUTY', hoso["Người đại diện định dạng"])
                    self.page.locator("#txtDOB_DEPUTY").fill(hoso["Người đại diện ngày tháng năm sinh"])
                    self.page.locator("#txtIDENTIFIER_NUMBER_DEPUTY").fill(hoso["Người đại diện số định danh cá nhân"])
                    self.page.select_option('#cboDATE_FORMAT_DEPUTY', hoso["Người đại diện giới tính"])
                    self.page.locator("#txtPHONE_NUMBER_DEPUTY").fill(hoso["Người đại diện số điện thoại"])
                    self.page.locator("#txtPERMANENT_DEPUTY").fill(hoso["Người đại diện nơi thường trú"])
                    self.page.locator("#txtLIVING_DEPUTY").fill(hoso["Người đại diện nơi ở hiện tại"])
                self.page.locator("#txtNOTE_DEPUTY").fill(hoso["Ý kiến của người đại diện"])  #Ý KIẾN NGƯỜI ĐẠI DIỆN
                self.CT_infor["noidungdenghi"] = "Thủ tục gia hạn tạm trú - Gia hạn tạm trú theo danh sách"
                self.page.locator("#txtTEMP_RESIDENT_TO").fill(hoso["Thời hạn tạm trú đề nghị đến ngày"]) #THỜI HẠN TẠM TRÚ
                #BUTTON
                input_file = self.page.locator("input#uploadExcelImport")   
                input_file.set_input_files("danhsachthaydoi.xlxs")
                files_CT01 = []
                for i in range(int(hoso["Số người trong danh sách"])):
                    files_CT01.append(f'CT01_{i+1}.pdf')
                self.page.set_input_files('#fileUpload0', files_CT01)
                self.page.locator("#chkCHECK_LIABILITY").check()
                #self.page.locator("#btn-save-send").click()  GỬI
            else:
                if hoso["Người khai báo shaoang"]: #CẦN REVIEW LẠI
                    self.page.locator("#txtPHONE_NUMBER").fill(hoso["SĐT liên hệ"])
                    self.page.locator("#txtHH_PERSON_FULLNAME").fill(hoso["Họ tên chủ hộ"])
                    self.page.select_option('#select2-cboHH_PERSON_RELATIONSHIP_CODE-container', hoso["Quan hệ với chủ hộ"])
                    self.page.locator("#txtHH_PERSON_IDENTIFIER_NUMBER").fill(hoso["Số định danh cá nhân chủ hộ"])
        except:
            
            return "lỗi"

    #---------XÁC MINH CƯ TRÚ-----------
    def inphieuCT01(self, hoso, tenfile):
        try:
            self.CT_infor["coquandangkycutru"] = "Công An " + hoso["Phường xã"]
            self.CT_infor["noidungdenghi"] = hoso["Trường hợp"] + " cho " + hoso["Họ tên người khai"]
            self.CT_infor["hovaten"] = hoso["Họ tên người khai"]
            self.CT_infor["ngaysinh"] = hoso["Ngày tháng năm sinh"]
            self.CT_infor["gioitinh"] = hoso["Giới tính"]
            self.CT_infor["ddcn"] = hoso["Số căn cước"]
            self.CT_infor["sodienthoai"] = hoso["Số điện thoại"]
            self.CT_infor["tenchuho"] = hoso["Họ và tên chủ hộ"]
            self.CT_infor["quanhechuho"] = hoso["Quan hệ với chủ hộ"]
            self.CT_infor["ddcnchuho"] =  hoso["Số định danh chủ hộ"]
            self.CT_infor["stt"] = hoso["Số lượng thành viên cùng thay đổi"]
            soluong = int(hoso["Số lượng thành viên cùng thay đổi"])
            for i in range(soluong):
                hoten = hoso[f"Thành viên {i} họ tên"]
                ngaysinh = hoso[f"Thành viên {i} ngày sinh"]
                gioitinh = hoso[f"Thành viên {i} giới tính"]
                so_cccd = hoso[f"Thành viên {i} số căn cước"]
                quanhech = hoso[f"Thành viên {i} quan hệ với chủ hộ"]
                self.CT_infor[f"thongtinnguoithu{i}"] =[i+1,hoten,ngaysinh,gioitinh,so_cccd,quanhech]
            doc = DocxTemplate(f"word_template\\template{self.CT_infor['stt']}.docx")
            doc.render(self.CT_infor)
            doc.save(tenfile + ".docx")
        except:
            
            return "lỗi"
    def Xacminh_cutru(self, hoso):
        
            self.page.get_by_text("Xác nhận thông tin về cư trú").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.page.reload()

            self.page.locator("#select2-cboRECEIVE_ADDR_CITY_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.province)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_DISTRICT_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.district)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_VILLAGE_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.village)
            self.page.keyboard.press('Enter')

            coquan = self.page.locator("#select2-cboORG-container").text_content()
            # if "cấp cho NK thường trú trên địa bàn quản lý" in hoso[0].lower():
            self.page.locator("#select2-cboBPROC_CASE_CODE-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(hoso["Trường hợp"])
            self.page.keyboard.press('Enter')
            
            # else:
            #     self.page.locator("#select2-cboBPROC_CASE_CODE-container").click()
            #     self.page.locator("xpath=/html/body/span/span/span[1]/input").fill("Cấp cho NK thường trú khác địa bàn quản lý")
            #     self.page.keyboard.press('Enter')


            nguoikhai = "cho tôi"
            if "cho tôi" in nguoikhai or "cho mình" in nguoikhai:
                self.page.locator("#chkIS_CHANGED_PERSON").check()
                self.page.wait_for_timeout(1000)    
                self.page.locator("#txtHH_HEAD_FULLNAME").fill(hoso["Họ và tên chủ hộ"])

                self.page.locator("#select2-cboRELATIONSHIP_WITH_HHHEAD_ID-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(hoso["Quan hệ với chủ hộ"])
                self.page.keyboard.press('Enter')

                self.page.locator("#txtID_CARD_NUMBER_HHEAD").fill(hoso["Số định danh chủ hộ"])
            else:
                radio_button = self.page.locator("#chkIS_NOT_CHANGED_PERSON")
                radio_button.check()
                print("Mời nhập thông tin người khai hộ")
                name=input("Họ và tên: ")
                birthday = input("Ngày tháng năm sinh vd:15/03/2000 hoặc 03/2000 hoặc 2000 ")
                sex = input("Giới tính: ")
                cccd = input("Số căn cước công dân: ")
                tenchuho = input("Tên chủ hộ: ")
                quanhechuho = input("quanhevoichuho")
                cccd_chuho = input("Số căn cước của chủ hộ")

                self.CT_infor["hovaten"] = name
                self.CT_infor["ngaysinh"] = birthday
                self.CT_infor["gioitinh"] = sex
                self.CT_infor["ddcn"] = cccd
                self.CT_infor["tenchuho"] = tenchuho
                self.CT_infor["quanhechuho"] = quanhechuho
                self.CT_infor["ddcnchuho"] =  cccd_chuho

                self.page.fill("input[id='txtFULLNAME']",name)
                if len(birthday) == 10 or len(birthday) == 8 or len(birthday) == 9:
                    pass
                elif len(birthday) == 7 and len(birthday) == 6:
                    self.page.select_option("select#cboFORMAT_DATE", value="2")
                else:
                    self.page.select_option("select#cboFORMAT_DATE", value="3")
                self.page.fill("input[id='txtBIRTH_DATE']",birthday)

                self.page.locator("#select2-cboGENDER_ID-container").fill(sex)
                self.page.locator("#txtID_CARD_NUMBER").fill(cccd)
                self.page.locator("#txtHH_HEAD_FULLNAME").fill(tenchuho)
                self.page.locator("#select2-cboRELATIONSHIP_WITH_HHHEAD_ID-container").fill(quanhechuho)
                self.page.locator("#txtID_CARD_NUMBER_HHEAD").fill(cccd_chuho)

            soluongthanhvien = int(hoso["Số lượng thành viên cùng thay đổi"])
            
            for i in range(soluongthanhvien):
                hoten = hoso[f"Thành viên {i} họ tên"]
                self.page.locator(f"#txtFULLNAME_CUNGTD{i}").fill(hoten)

                ngaysinh = hoso[f"Thành viên {i} ngày sinh"]
                self.page.locator(f"#txtDOB_CUNGTD{i}").fill(ngaysinh)

                gioitinh = hoso[f"Thành viên {i} giới tính"]
                self.page.locator(f"#select2-cboGENDER_CUNGTD{i}-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(gioitinh)
                self.page.keyboard.press('Enter')


                so_cccd = hoso[f"Thành viên {i} số căn cước"]
                self.page.locator(f"#txtIDENTIFIER_NOCARD_NUMBER_CUNGTD{i}").fill(so_cccd)

                quanhech = hoso[f"Thành viên {i} quan hệ với chủ hộ"]
                self.page.locator(f"#select2-cboRELATIONSHIP_CHUHO_CUNGTD{i}-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(quanhech)
                self.page.keyboard.press('Enter')
                self.page.click(f"#tblNguoi_CUNGTD tr.selected[data-index='{i}'] td.center a.add_CUNGTD")
            
            
            self.page.locator("#chkRULE").click()
        
        
    def submitinfoXacminh(self, num):
            current_file_path = os.path.abspath(__file__)
            folderpath = os.path.dirname(current_file_path)
            
            danhsachfile = []
            for i in range(num):
                file_path = f"CT01_{str(i+1)}.jpg"
                realpath = os.path.join(folderpath, file_path)
                danhsachfile.append(realpath)
            print(danhsachfile)
            input_file = self.page.locator('input[id="fileUpload0"]')   
            # Upload the fileơ
            input_file.set_input_files(danhsachfile)
            self.page.locator("#select2-cboTYPE_GET_RESULT-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill("Nhận trực tiếp")
            self.page.keyboard.press('Enter')
            self.page.locator("#txtNUMBER_OF_RESULT").fill("1")
            # Còn nút gửi hồ sơ
            self.page.locator("#btn_Save_Send").click()

    def kiemtrattin(self):
        kq = "guithanhcong"
        if self.page.locator("#lblCheck_Du_Thong_Tin").count() > 0:
            kq = self.page.locator("#lblNAME_CITIZEN").text_content() + " " + self.page.locator("#lblCheck_Du_Thong_Tin").text_content()
        return kq

 
    #---------TÁCH HỘ-----------    
    def Tachho(self, hoso):
        try:
            self.page.get_by_text("Tách hộ").click()
            self.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
            self.page.reload()

            self.page.locator("#select2-cboRECEIVE_ADDR_CITY_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.province)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_DISTRICT_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.district)
            self.page.keyboard.press('Enter')

            self.page.locator("#select2-cboRECEIVE_ADDR_VILLAGE_ID-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(self.village)
            self.page.keyboard.press('Enter')

            coquan = self.page.locator("#select2-cboORG-container").text_content()
            # if "cấp cho NK thường trú trên địa bàn quản lý" in hoso[0].lower():
            self.page.locator("#select2-cboBPROC_CASE_CODE-container").click()
            self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(hoso["Trường hợp"])
            self.page.keyboard.press('Enter')
            
            # else:
            #     self.page.locator("#select2-cboBPROC_CASE_CODE-container").click()
            #     self.page.locator("xpath=/html/body/span/span/span[1]/input").fill("Cấp cho NK thường trú khác địa bàn quản lý")
            #     self.page.keyboard.press('Enter')


            nguoikhai = "khaiho"
            if "cho tôi" in nguoikhai or "cho mình" in nguoikhai:
                self.page.locator("#chkIS_CHANGED_PERSON").check()
                self.page.wait_for_timeout(1000)    
                self.page.locator("#txtHH_HEAD_FULLNAME").fill(hoso["Họ và tên chủ hộ"])

                self.page.locator("#select2-cboRELATIONSHIP_WITH_HHHEAD_ID-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(hoso["Quan hệ với chủ hộ"])
                self.page.keyboard.press('Enter')

                self.page.locator("#txtID_CARD_NUMBER_HHEAD").fill(hoso["Số định danh chủ hộ"])
            else:
                radio_button = self.page.locator("#chkIS_NOT_CHANGED_PERSON")
                radio_button.check()
                name=hoso["Họ tên người khai"]
                birthday = hoso["Ngày tháng năm sinh"]
                sex = hoso["Giới tính"]
                cccd = hoso["Số căn cước"]
                sdt = hoso["Số điện thoại"]
                tenchuho = hoso["Họ và tên chủ hộ"]
                quanhechuho = hoso["Quan hệ với chủ hộ"]
                cccd_chuho = hoso["Số định danh chủ hộ"]

                self.page.fill("input[id='txtFULLNAME']",name)
                if len(birthday) == 10 or len(birthday) == 8 or len(birthday) == 9:
                    pass
                elif len(birthday) == 7 and len(birthday) == 6:
                    self.page.select_option("select#cboFORMAT_DATE", value="2")
                else:
                    self.page.select_option("select#cboFORMAT_DATE", value="3")
                self.page.fill("input[id='txtBIRTH_DATE']",birthday)

                self.page.locator("#select2-cboGENDER_ID-container").fill(sex)
                self.page.locator("#txtID_CARD_NUMBER").fill(cccd)
                self.page.locator("#txtPHONE_NUMBER").fill(sdt)
                self.page.locator("#txtHH_HEAD_FULLNAME").fill(tenchuho)
                self.page.locator("#select2-cboRELATIONSHIP_WITH_HHHEAD_ID-container").fill(quanhechuho)
                self.page.locator("#txtID_CARD_NUMBER_HHEAD").fill(cccd_chuho)

            soluongthanhvien = int(hoso["Số lượng thành viên cùng thay đổi"])
            
            for i in range(soluongthanhvien):
                hoten = hoso[f"Thành viên {i} họ tên"]
                self.page.locator(f"#txtFULLNAME_CUNGTD{i}").fill(hoten)

                ngaysinh = hoso[f"Thành viên {i} ngày sinh"]
                self.page.locator(f"#txtDOB_CUNGTD{i}").fill(ngaysinh)

                gioitinh = hoso[f"Thành viên {i} giới tính"]
                self.page.locator(f"#select2-cboGENDER_CUNGTD{i}-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(gioitinh)
                self.page.keyboard.press('Enter')


                so_cccd = hoso[f"Thành viên {i} số căn cước"]
                self.page.locator(f"#txtIDENTIFIER_NOCARD_NUMBER_CUNGTD{i}").fill(so_cccd)

                quanhech = hoso[f"Thành viên {i} quan hệ với chủ hộ"]
                self.page.locator(f"#select2-cboRELATIONSHIP_CHUHO_CUNGTD{i}-container").click()
                self.page.locator("xpath=/html/body/span/span/span[1]/input").fill(quanhech)
                self.page.keyboard.press('Enter')
                self.page.click(f"#tblNguoi_CUNGTD tr.selected[data-index='{i}'] td.center a.add_CUNGTD")
            
            
            self.page.locator("#chkRULE").click()
        except:
            
            return "lỗi"

    def submitinfoTachho(self, hoso):
        try:
            input_file = self.page.locator("input#fileUpload0")   
            input_file.set_input_files("CT01.pdf")
            if "Cho o hop phap" in hoso.keys():
                self.page.locator("#chkIS_COMPULSORY1").check()
                input_file = self.page.locator("input#fileUpload1")   
                input_file.set_input_files("Cho o hop phap.pdf")
            if "Giay ly hon" in hoso.keys():
                self.page.locator("#chkIS_COMPULSORY2").check()
                input_file = self.page.locator("input#fileUpload2")   
                input_file.set_input_files("Giay ly hon.pdf")
        except:
            
            return "lỗi"
        # Còn nút gửi hồ sơ

 











