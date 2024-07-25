#Thêm các thư viện cần thiêt
from flask import Flask, render_template, request, jsonify,session,redirect, url_for
import google.generativeai as genai
from playwright.sync_api import sync_playwright,Playwright
from playwrightFetch import *
from gevent import monkey
from threading import Thread
from googleapiclient.discovery import build
import feedparser
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
nguoi2 = {}
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
            time.sleep(5)    
def get_news(url="https://vtcnews.vn/rss/thoi-su.rss"):
    feed = feedparser.parse(url)
    return feed.entries

os.environ['GOOGLE_API_KEY'] = ""
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash-latest',   #gemini-1.5-flash-latest
safety_settings=threads_safe,
generation_config=generation_config,
)
chatt = model.start_chat(history=[])
VneID = VNeIDPage(Playwright)
def kdv():
    VneID.khoidong()
lmfao = send_messageG(prompt.khoidong + prompt.prompt_dvccancuoc + prompt.prompt_dvccutru)
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
    global nguoi2
    chucnang.clear_print_queue()
    chatt = model.start_chat(history=[])
    lmfao = send_messageG(prompt.khoidong + prompt.prompt_dvccancuoc + prompt.prompt_dvccutru)
    dichvucong = ""
    chitiet = ""
    chitiet_dvc = ""
    chon_lydo_doithe = ""
    doithetheotuoi = ""
    chatflag = 0
    hoso=[]
    nguoi={}
    nguoi2={}
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

def timtuoi(datestr):
    today = datetime.now()
    birthday = datetime.strptime(datestr, "%d/%m/%Y")
    tuoi = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        tuoi -= 1
    return tuoi



##NỘI DUNG HỆ THỐNG
#Trang chủ

@app.route("/")
def index():
    tintuc = ""
    news = get_news()
    for article in news:
        tintuc += article['title'] + ". "
    return render_template('index.html',current_flow=current_flow, my_string=tintuc)

#Chào người dùng
@app.route("/greentings")
def greetings():
    data = {'greetings': "Xin chào tôi là trợ lý ảo dịch vụ công về căn cước và cư trú. Tôi có thể giúp gì được cho bạn? ", 
            'pre_start': "Để thực hiện dịch vụ công, vui lòng đăng nhập quét QR code bằng ứng dụng VNeID hoặc đặng nhập bằng tài khoản ở khung bên cạnh"}
    return data

@app.route("/ktBrowser")
def ktBrowser():
    Thread(target=kdv).start()
    return "ok"

@app.route('/restart')
def restart():
    global VneID
    # if login_status == True:
    #     VneID.logout()
    VneID.halfClose()
    khoitaobien()
    return "ok"

@app.route('/restartBrowser')
def restartBrowser():
    VneID.page.reload()
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
    if "thanhcong" in trangthaidn and login_status == False:
        chatflag = 0
        login_status = True
    data = {"QR": qr_code_src,
            "TTDN": trangthaidn}
    
    print(trangthaidn)
    return data

@app.route('/laythongtin', methods=['GET'])
def laythongtin():
    global nguoi
    global nguoi2
    if len(nguoi2) == 0:
        nguoi2 = VneID.getInf(nguoi)
    print(nguoi2)
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
            hab = send_messageG("Đã xong phần tìm kiếm dịch vụ công. Tiếp theo hãy hướng dẫn tôi cách nhập thông tin vào phiếu CT01, nếu tôi hỏi bạn cách điền trường nào trong phiếu CT01 thì bạn trả lời cho tôi giới hạn điền của trường đó. Giới hạn câu trả lời trong việc hướng dẫn khai thông tin vào phiếu CT01. Nếu tôi hỏi về cách thêm thành viên thì trả lời bấm vào nút dấu cộng trên bảng thông tin bên trái. Các câu trả lời của bạn nên hướng đến chủ đề dịch vụ công về cư trú nhé.")
        if dichvucong == "Cấp, quản lý thẻ căn cước":
            hab = send_messageG("Đã xong phần tìm kiếm dịch vụ công. Tiếp theo hãy hướng dẫn tôi cách nhập thông tin vào trường khai thông tin cấp căn cước. Nếu tôi hỏi thêm người KHÁC không có trong danh sách, hãy trả lời theo hướng Liên hệ với cán bộ để được giúp đỡ. Giới hạn câu trả lời trong việc hướng dẫn khai thông tin")
        print(f"{dichvucong} --- {chitiet}")
        dvc = "Dịch vụ công phù hợp là " + dichvucong + " --- " + chitiet
        dichvucong = "" 
        return dvc
    if msg == "Huỷ":
        dichvucong = ""
        chitiet_dvc = ""
        send_messageG("Hãy quên những yêu cầu mà tôi vừa đưa ra. Tôi sẽ đưa yêu cầu mới ở lần trả lời kế tiếp. Bạn thực hiện phân loại dịch vụ công về căn cước hay cư trú lại từ đầu. Đừng đưa ra gợi ý về tên dịch vụ công lúc này.")
        return "Hãy mô tả chi tiết hơn yêu cầu của bạn."
    response = send_messageG(msg)
    print("Thử " + response)            
    if chitiet_dvc == "":
        if "phù hợp" in response and "căn cước" in response.lower() and "cấp mới" in response.lower():
            chitiet_dvc = "cấp mới căn cước"
            dichvucong = "Cấp, quản lý thẻ căn cước"
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
            chitiet_dvc = "cấp đổi căn cướcc do hết hạn"
        if "phù hợp" in response and "xác minh" in response.lower() or "xác nhận" in response.lower():
            chitiet_dvc = "xác nhận số"
    if chitiet_dvc == "":
        if "phù hợp" in response.lower() and ("xác minh" in response.lower() or "xác nhận" in response.lower()):
            chitiet_dvc = "xác minh cư trú"
            dichvucong = "Đăng ký, quản lý cư trú"
        if "phù hợp" in response and "tách hộ" in response.lower():
            chitiet_dvc = "tách hộ"
            dichvucong = "Đăng ký, quản lý cư trú"
        response = removeTT(response)
        return response
    response = removeTT(response)
    return response


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

@app.route("/capmoicancuoc", methods=["GET","POST"])
def capcancuoct14():
    global hoso
    global nguoi
    msg = request.get_json()
    key = ["Số điện thoại", "Trường hợp", "Người cần họ và tên", "Người cần ngày sinh", "Người cần giới tính", "Người cần số định danh", "Quan hệ với người khai", "Lý do cấp"]
    hoso = dict(zip(key,msg.split(";;")))
    print(hoso)
    tuoi = timtuoi(hoso["Người cần ngày sinh"])
    if (tuoi > 13):
        kq = VneID.Capmoi_CC_tren14(hoso)
    else:
        kq = VneID.Capmoi_CC_duoi14(hoso)
    result = {
        'message': kq,
    }
    if (kq == "thanhcong"):
        VneID.ChonngaycapCC()
        hab = send_messageG("Đã thực hiện xong dịch vụ công này. Quay về trạng thái tìm dịch vụ công lúc bắt đầu")
    return jsonify(result)


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
    kq = 0
    kq = chucnang.scanlientuc(msg)
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
    time.sleep(8)
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
    time.sleep(8)
    result["message"] = VneID.kiemtrattin()
    if (result["message"]!="guithanhcong"):
        return jsonify(result)
    hab = send_messageG("Tôi đã làm xong dịch vụ công Tách hộ. Hãy bắt đầu lại từ đầu, giúp tôi tìm dịch vụ công khác. " + prompt.khoidong)
    result['message'] = 'guithanhcong'
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
