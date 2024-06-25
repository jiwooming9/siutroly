#Thêm các thư viện cần thiêt
from flask import Flask, render_template, request, jsonify,session,redirect, url_for
import google.generativeai as genai
from playwright.sync_api import sync_playwright,Playwright
from playwrightFetch import *
from gevent import monkey
import time
import prompt
from datetime import datetime
import os
import chucnang
#Khai báo cáo biến cho hệ thống
monkey.patch_all()
app = Flask(__name__)
current_flow = "normal"
date_format = "%d/%m/%Y"
dichvucong = ""
chitiet = ""
chitiet_dvc = ""
chon_lydo_doithe = ""
doithetheotuoi = ""
chatflag = 0
login_status = False
hoso=[]
age = 0
nguoi = {}
chucnang.clear_print_queue()
notifications = ""
threads_safe = [
                {
                    "category": "HARM_CATEGORY_DANGEROUS",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE",
                },
]
generation_config = {
    "temperature": 0.3,
    "top_p": 0.3,
    "top_k": 1,
    "max_output_tokens": 500,
}
def send_messageG(msg):
    global chatt
    while True:
        try:
            ans = chatt.send_message(msg,safety_settings=threads_safe)
            return ans.text 
        except:
            time.sleep(2)    
os.environ['GOOGLE_API_KEY'] = "AIzaSyAgX68LjbI8uh3PaerAbbZIaLDavCk-FS8"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash-latest',   #gemini-1.5-flash-latest
safety_settings=threads_safe,
generation_config=generation_config,
)
chatt = model.start_chat(history=[])
VneID = VNeIDPage(Playwright)
#aloy = chatt.send_message(prompt.batdau + prompt.prompt_quydinhcancuoc, safety_settings=threads_safe)\
lmfao = send_messageG(prompt.khoidong)
def khoitaobien():
    global login_status
    global dichvucong 
    global chitiet
    global chitiet_dvc
    global chon_lydo_doithe
    global doithetheotuoi
    global chatt
    global chatflag
    global hoso
    global age
    global nguoi
    global notifications
    chucnang.clear_print_queue()
    chatt = model.start_chat(history=[])
    lmfao = send_messageG(prompt.khoidong + "Đây là thông tin về dịch vụ công căn cước để lấy thông tin: " + prompt.prompt_quydinhcancuoc)
    #aloy = chatt.send_message(prompt.batdau + prompt.prompt_quydinhcancuoc, safety_settings=threads_safe)
    dichvucong = ""
    chitiet = ""
    chitiet_dvc = ""
    chon_lydo_doithe = ""
    doithetheotuoi = ""
    chatflag = 0
    hoso=[]
    nguoi={}
    age = 0
    login_status = False
    notifications = ""
def removeTT(input_str):
    new = input_str
    if "bbangcutru" in input_str:
        new = new.replace("<br> bbangcutru", "")
        new = new.replace("bbangcutru<br>", "")
        new = new.replace("bbangcutru", "")
    if "bbangcancuoc" in input_str:
        new = new.replace("<br> bbangcancuoc", "")
        new = new.replace("bbangcancuoc<br>", "")
        new = new.replace("bbangcancuoc", "")
    if "bbangtt" in input_str:
        new = new.replace("<br> bbangtt", "")
        new = new.replace("bbangtt<br>", "")
        new = new.replace("bbangtt", "")
    return new



##NỘI DUNG HỆ THỐNG
#Trang chủ

@app.route("/")
def index():
    return render_template('index.html',current_flow=current_flow)

#Chào người dùng
@app.route("/greentings")
def greetings():
    data = {'greetings': "Xin chào tôi là trợ lý ảo dịch vụ công về căn cước và cư trú. Tôi có thể giúp gì được cho bạn? ", 
            'pre_start': "Để thực hiện dịch vụ công, vui lòng đăng nhập quét QR code bằng ứng dụng VNeID hoặc đặng nhập bằng tài khoản ở khung bên cạnh"}
    VneID.khoidong()
    return data

@app.route('/restart')
def restart():
    global VneID
    # if login_status == True:
    #     VneID.logout()
    VneID.halfClose()
    khoitaobien()
    return redirect(url_for('index'))

@app.route('/restartBrowser')
def restartBrowser():
    VneID.closeVN()
    return "ok"

@app.route('/notify', methods=['POST'])
def notify():
    global notifications
    data = request.json
    print(f"Received notification: {data}")
    notifications = data["message"]
    return "Notification received", 200

@app.route('/notifications', methods=['GET'])
def get_notifications():
    global notifications
    sendS = notifications
    notifications = ""
    return jsonify({'notifications': sendS})


#PHƯƠNG THỨC ĐĂNG NHẬP  
#Đăng nhập bằng tài khoản
# @app.route("/post-login",methods=["GET","POST"])
# def login():
#     global login_status
#     try:
#         UserID = request.form["userID"]
#         UserPass = request.form["userPass"]
#         VneID.loginForm(UserID=UserID,UserPass=UserPass)
#         VneID.set_trangthaiDN()
#         if "thanhcong" in VneID.get_trangthaiDN():
#             login_status = True
#         print({"Username": UserID, "Password": UserPass})
#         return VneID.get_trangthaiDN()
#     except:
#         raise Exception("Lỗi đăng nhập!")
    
# #Kiểm tra OTP   
# @app.route("/otp-check",methods=["POST"])
# def check_OTP():
#     try:
#         received_otp = request.form.get("otp")
#         otp_arr = [x for x in received_otp]
#         VneID.OTPSend(otp_arr)
#         return jsonify({"OTPcode":received_otp})
#     except:
#         raise Exception("Lỗi OTP!")


#Lấy mã QR 
@app.route("/get_qr_code")
def get_qr_code():
    global login_status
    global doithetheotuoi
    global chatflag
    global age
    global chatt
    global nguoi
    qr_code_src = ''
    trangthaidn = VneID.get_trangthaiDN()
    if login_status == False:
        qr_code_src = VneID.extract_qr_code_src()
    dob = ''
    expdate = ''
    if "thanhcong" in trangthaidn and login_status == False:
        chatflag = 0
        login_status = True
        thongtinchung = VneID.getDOB()
        dob = thongtinchung.split()[0]
        nguoi["Số định danh"] = thongtinchung.split()[1]
    if dob !='':
        datemod = datetime.strptime(dob, date_format)
        today = datetime.today()
        age = today.year - datemod.year - ((today.month, today.day) < (datemod.month, datemod.day))
        if 24 <= age <= 25:
            doithetheotuoi = 'doithe25'
        if 39 <= age <= 40:
            doithetheotuoi = 'doithe40'
        if 59 <= age <= 60:
            doithetheotuoi = 'doithe60'
    data = {"QR": qr_code_src,
            "TTDN": trangthaidn}
    print(trangthaidn)
    return data

@app.route('/laythongtin', methods=['GET'])
def laythongtin():
    global nguoi
    nguoi2 = VneID.getInf(nguoi)
    return jsonify(nguoi2)
            
    

#Giao tiếp với người dân    
@app.route("/get", methods=["POST"])
def chat():
    #Khai báo biến global
    global dichvucong
    global chitiet
    global chitiet_dvc
    global login_status
    global doithetheotuoi
    msg = request.form["msg"]
    global chatflag
    global chatt
    global hoso
    global nguoi
    #Kiểm tra biến đăng nhập để chuyển luồng
    if msg == '':
        return
    if chitiet_dvc != "" and "đồng ý" in msg.lower():
        chitiet = chitiet_dvc
        chitiet_dvc = ""
        if dichvucong == "Đăng ký, quản lý cư trú":
            hab = send_messageG("Đã xong phần tìm kiếm dịch vụ công. Tiếp theo hãy hướng dẫn tôi cách nhập thông tin vào phiếu CT01, nếu tôi hỏi bạn cách điền trường nào trong phiếu CT01 thì bạn trả lời cho tôi giới hạn điền của trường đó. Giới hạn câu trả lời trong việc hướng dẫn khai thông tin vào phiếu CT01. Nếu tôi hỏi về cách thêm thành viên thì trả lời bấm vào nút dấu cộng trên bảng thông tin bên trái.")
        if dichvucong == "Cấp, quản lý thẻ căn cước":
            hab = send_messageG("Tôi đã thực hiện xong dịch vụ công này. Hãy bắt đầu lại từ đầu, giúp tôi tìm dịch vụ công khác. " + prompt.khoidong)
        print(f"{dichvucong} --- {chitiet}")
        dvc = "Dịch vụ công phù hợp là " + dichvucong + " --- " + chitiet
        dichvucong = "" 
        return dvc
    if msg == "Huỷ":
        dichvucong = ""
        chitiet_dvc = ""
        send_messageG("Hãy quên những yêu cầu mà tôi vừa đưa ra. Tôi sẽ đưa yêu cầu mới ở lần trả lời kế tiếp. Bạn thực hiện phân loại dịch vụ công về căn cước hay cư trú lại từ đầu. Đừng đưa ra gợi ý về tên dịch vụ công lúc này.")
        return "Hãy mô tả chi tiết hơn yêu cầu của bạn."
    if msg == "Dịch vụ công căn cước":
        hab = send_messageG(prompt.prompt_dvccancuoc)
        dichvucong = "Cấp, quản lý thẻ căn cước"
        return "Một số dịch vụ công hay được tiếp nhận:<br>-Dịch vụ 1: Cấp lại thẻ do mất---Dịch vụ 2: Cấp đổi thẻ do hết hạn<br>"
    if msg == "Dịch vụ công cư trú":
        hab = send_messageG(prompt.prompt_dvccutru)
        dichvucong = "Đăng ký, quản lý cư trú"
        return "Một số dịch vụ công hay được tiếp nhận:<br>-Dịch vụ 1: Xác nhận thông tin cư trú---Dịch vụ 2: Tách hộ<br>"
    response = send_messageG(msg)
    print("Thử " + response)
    if dichvucong == '':
        time.sleep(3)
        adap = ""
        if "bbangcancuoc" in response:
            adap = response
            dichvucong = "Cấp, quản lý thẻ căn cước"
            response = send_messageG(prompt.prompt_dvccancuoc)
            response = adap +"<br>"+ response
            print(response)
        if "bbangcutru" in response:
            adap = response
            dichvucong = "Đăng ký, quản lý cư trú"
            response = send_messageG(prompt.prompt_dvccutru)
            response = adap +"<br>"+ response
            print(response)
            
    if chitiet_dvc == "":
        if "phù hợp" in response and "căn cước" in response and "do mất" in response:
            chitiet_dvc = "cấp lại căn cước do mất"
        if "phù hợp" in response and "căn cước" in response and "hư hỏng" in response:
            chitiet_dvc = "cấp đổi căn cước do hư hỏng"
        if "phù hợp" in response and "căn cước" in response and "thông tin họ tên" in response:
            chitiet_dvc = "cấp đổi căn cước do thay đổi thông tin họ tên"
        if "phù hợp" in response and "căn cước" in response and "đặc điểm nhận dạng" in response:
            chitiet_dvc = "cấp đổi căn cước do thay đổi đặc điểm nhận dạng"
        if "phù hợp" in response and "căn cước" in response and "sai sót thông tin" in response:
            chitiet_dvc = "cấp đổi căn cước do có sai sót thông tin trên căn cước"
        if "phù hợp" in response and "căn cước" in response and "hết hạn" in response:
            chitiet_dvc = "cấp đổi căn cước do hết hạn"
        if "phù hợp" in response and "xác minh" in response.lower() or "xác nhận" in response.lower():
            chitiet_dvc = "xác nhận số"
        if "phù hợp" in response.lower() and ("xác minh" in response.lower() or "xác nhận" in response.lower()):
            chitiet_dvc = "xác minh cư trú"
        if "phù hợp" in response and "tách hộ" in response.lower():
            chitiet_dvc = "tách hộ"
        response = removeTT(response)
        return response
    response = removeTT(response)
    return response

@app.route("/chon_dvc_caplai")
def dvc_caplai():
    if (VneID.Timkiem_CCCD()=="lỗi"):
        return "lỗi"
    status = VneID.Caplai_CCCD_tinh()
    print(status)
    if (status=="lỗi"):
        return "lỗi"
    return status
@app.route("/chon_dvc_doithe")
def dvc_doithe():
    global age
    global doithetheotuoi
    num = 0
    if (VneID.Timkiem_CCCD()=="lỗi"):
        return "lỗi"
    if doithetheotuoi!='' or chitiet == "cấp đổi căn cước do hết hạn":
        if doithetheotuoi == 'doithe25' or abs(age-25)<2:
            doithetheotuoi = ''
            num = 6
        if doithetheotuoi == 'doithe40' or abs(age-40)<2:
            doithetheotuoi = ''
            num = 7
        if doithetheotuoi == 'doithe60' or abs(age-60)<2:
            doithetheotuoi = ''
            num = 8
    if chitiet == "cấp đổi căn cước do hư hỏng":
        num = 0
    elif chitiet == "cấp đổi căn cước do thay đổi thông tin họ tên":
        num = 1
    elif chitiet == "cấp đổi căn cước do thay đổi đặc điểm nhận dạng":
        num = 2
    elif chitiet == "cấp đổi căn cước do có sai sót thông tin trên căn cước":
        num = 5
    status = VneID.Doithe_CCCD_tinh(num)
    if (status == 'lỗi'):
        return "lỗi"
    return status
@app.route("/chon_dvc_xacminh")
def dvc_xacminh():
    if (VneID.Timkiem_CCCD()=="lỗi"):
        return "lỗi"
    status = VneID.xacminh_CCCD_tinh()
    if (status == 'lỗi'):
        return "lỗi"
    return status

@app.route("/inCT01", methods=["GET","POST"])
def inCT01():
    global hoso
    msg = request.get_json()
    key = ["Thành phố", "Quận huyện", "Phường xã", "Trường hợp", "Họ tên người khai", "Ngày tháng năm sinh", "Giới tính", "Số căn cước", "Số điện thoại", "Họ và tên chủ hộ", "Quan hệ với chủ hộ","Số định danh chủ hộ", "Số lượng thành viên cùng thay đổi","Dữ liệu bảng" ]
    hoso = dict(zip(key,msg.split(";;")))
    bangthanhvien = hoso["Dữ liệu bảng"].split(",")
    for i in range(int(hoso["Số lượng thành viên cùng thay đổi"])):
        hoso[f"Thành viên {i} họ tên"] = bangthanhvien[(i*5)+0]
        hoso[f"Thành viên {i} ngày sinh"] = bangthanhvien[(i*5)+1]
        hoso[f"Thành viên {i} giới tính"] = bangthanhvien[(i*5)+2]
        hoso[f"Thành viên {i} số căn cước"] = bangthanhvien[(i*5)+3]
        hoso[f"Thành viên {i} quan hệ với chủ hộ"] = bangthanhvien[(i*5)+4]
    kiemtra = "Đã in"
    print(hoso)
    if (VneID.inphieuCT01(hoso,"CT01")=="lỗi"):
        kiemtra = "Lỗi"
    chucnang.intailieu("CT01.docx")
    result = {
    'message': kiemtra,
    }
    return jsonify(result)

@app.route("/scantailieu", methods=["GET","POST"])
def scantailieu():
    global hoso
    print("Chuẩn bị scan")
    msg = request.get_json()
    time.sleep(5)
    kq = 1
    #kq = chucnang.scanlientuc(msg)
    if kq > 0:
        hoso[msg] = kq
    result = {
        'message': kq,
    }
    return jsonify(result)

@app.route("/dvc_xacminhcutru", methods=["GET","POST"])
def dvc_xacminhcutru():
    global hoso
    result = {
        'message': 'lỗi',
    }
    if (VneID.Timkiem_CT()=="lỗi"):
        return jsonify(result)
    if (VneID.Xacminh_cutru(hoso)=="lỗi"):
        return jsonify(result)
    if (VneID.submitinfoXacminh(hoso["CT01"])=="lỗi"):
        return jsonify(result)
    time.sleep(5)
    result["message"] = VneID.kiemtrattin()
    if (result["message"]!="guithanhcong"):
        return jsonify(result)
    hab = send_messageG("Tôi đã làm xong dịch vụ công Xác minh cư trú. Hãy bắt đầu lại từ đầu, giúp tôi tìm dịch vụ công khác. " + prompt.khoidong)
    result['message'] = 'guithanhcong'
    return jsonify(result)

@app.route("/dvc_tachho", methods=["GET","POST"])
def dvc_tachho():
    global hoso
    result = {
        'message': 'lỗi',
    }
    if (VneID.Timkiem_CT()=="lỗi"):
        return jsonify(result)
    if (VneID.Tachho(hoso)=="lỗi"):
        return jsonify(result)
    if (VneID.submitinfoTachho(hoso)=="lỗi"):
        return jsonify(result)
    time.sleep(3)
    result["message"] = VneID.kiemtrattin()
    if (result["message"]!="guithanhcong"):
        return jsonify(result)
    hab = send_messageG("Tôi đã làm xong dịch vụ công Tách hộ. Hãy bắt đầu lại từ đầu, giúp tôi tìm dịch vụ công khác. " + prompt.khoidong)
    result['message'] = 'guithanhcong'
    return jsonify(result)


# @app.route('/xemlichsu_trochuyen')
# def xemlichsu_trochuyen():
#     global chon_lydo_doithe
#     _history = ""
#     for i in range(len(chatt.history)):
#         if i % 2 != 0:
#             _history+= "," + str(chatt.history[i].parts[0]).replace("text: ","")
#     if "chờ" in _history[1:]:
#         if "hư hỏng" in _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do bị hư hỏng không sử dụng được"
#         if "họ tên" in  _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do thay đổi thông tin họ tên"
#         if "nhận dạng" in _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do thay đổi đặc điểm nhận dạng"
#         if "giới tính" in  _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do xác định lại giới tính"
#         if "quê quán" in _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do xác định lại quê quán"
#         if "sai sót thông tin" in  _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước do có sai sót thông tin trên Căn cước"
#         if "25" in _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước khi công dân đủ 25 tuổi"
#         if "40" in  _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước khi công dân đủ 40 tuổi"
#         if "60" in _history[1:]:
#             chon_lydo_doithe = "Đổi Căn cước khi công dân đủ 60 tuổi"
#     chatt._history = []
#     VneID.Timkiem_CCCD()
#     VneID.page.get_by_text("Đổi thẻ Căn cước công dân (thực hiện tại cấp tỉnh)").click()
#     VneID.page.get_by_role("link", name="Nộp hồ sơ", exact=True).click()
#     VneID.page.wait_for_load_state("load")
#     VneID.page.locator("#select2-cboreason-container").click()
#     reason = VneID.page.locator("input[class='select2-search__field']")
#     reason.fill(chon_lydo_doithe)
#     VneID.page.wait_for_timeout(2000)
#     input_element_T = VneID.page.locator('#type_T')
#     input_element_T.evaluate("element => element.removeAttribute('disabled')")
#     radio_button = VneID.page.locator("#type_T")
#     radio_button.check()

#     VneID.page.locator("#select2-cbocityOrganization-container").click()
#     search_input = VneID.page.locator("xpath=/html/body/span/span/span[1]/input")
#     search_input.fill(f"{VneID.province}")
#     search_input.press("Enter")


#     VneID.page.locator("#btnNEXT_TAB_2").click()

#     VneID.confirm_data()
#     VneID.get_active_day()
#     VneID.page.wait_for_timeout(5000)
#     return chon_lydo_doithe 



if __name__ == "__main__":
    app.run(debug=False)
