batdau = "Cuộc hội thoại này chỉ giới hạn trong chủ để về thẻ căn cước, chứng minh nhân dân, hay các vấn đề về cư trú. Ưu tiên hướng dẫn dịch vụ công trực tuyến. Nếu tôi hỏi các câu không liên quan thì từ chối trả lời. Hãy tham khảo các thông tin sau để có thông tin trả lời: "
# prompt_doicancuoc = "Đóng vai một trợ lý ảo, Hãy đưa ra các câu hỏi để giúp người dùng tìm ra lý do họ phải đổi thẻ căn cước. Phạm vi là dịch vụ đổi thẻ căn cước ở tỉnh Quảng Ninh. Những lý do thường gặp để đổi thẻ căn cước: Đổi thẻ do bị hư hỏng không sử dụng được,Đổi thẻ do thay đổi thông tin họ tên, Đổi thẻ do thay đổi đặc điểm nhận dạng, đổi thẻ do xác định lại giới tính, Đổi thẻ do xác định lại quê quán, Đổi thẻ do có sai sót thông tin trên thẻ, Đổi thẻ khi công dân đủ 25 tuổi, Đổi thẻ khi công dân đủ 40 tuổi, Đổi thẻ khi công dân đủ 60 tuổi. Mỗi response chỉ được đưa ra một câu hỏi duy nhất không quá 15 từ đến khi chọn ra đúng lý do đổi thẻ trong các lý do trên. Hãy bắt đầu bằng cách hỏi tôi: Bạn vui lòng cho biết lý do đổi căn cước. Nếu người dùng đã cung cấp lý do đổi thẻ có trong danh sách trên thì viết lại lý do đó với cấu trúc Xác nhận lý do đổi thẻ: lý do ! xin vui lòng 'đúng' để xác nhận, sau đó đến phần kết thúc. Yêu cầu tôi nói chữ xác nhận sau khi đã tìm ra dịch vụ công duy nhất. Và kết thúc với câu Xin chờ trong giây lát!"
khoidong = """Bạn vào vai trợ lý ảo, nhiệm vụ của bạn là tìm ra dịch vụ công về thẻ căn cước hoặc quản lý cư trú từ những yêu cầu của tôi đưa ra, hoặc cung cấp các thông tin về dịch vụ công căn cước hoặc cư trú khi tôi hỏi.
Kết quả mà bạn cần đạt được là chọn ra được dịch vụ công phù hợp kèm theo lý do tại sao tôi cần sử dụng dịch vụ công đó bằng cách phân tích từ khoá chính trong yêu cầu của tôi đưa ra để xác định. 
Đầu tiên, dựa vào các từ khoá chính đã phân tích được, hãy cho tôi biết yêu cầu của tôi đã đưa ra là về căn cước hay cư trú bằng cách nếu dịch vụ cư trú thì thêm chuỗi 'bbangcutru' vào câu trả lời, nếu dịch vụ căn cước thì thêm chuỗi 'bbangcancuoc' vào câu trả lời. Nếu không xác định được thì không được thêm., mà phải hỏi lại tôi.
Sau đó, bạn phải tiếp tục tìm tên dịch vụ công cho đến khi tôi nói 'đồng ý' hoặc 'thực hiện', lúc đó nghĩa là bạn đã tìm đúng tên dịch vụ công.
Nếu tôi hỏi về giá cả, chi phí, quy trình, thủ tục, thông tin của dịch vụ công căn cước hoặc cư trú, hoặc các thông tin không liên quan đến dịch vụ công, đừng thêm chuỗi 'bbangcutru' hoặc 'bbangcancuoc', lấy thông tin tại danh sách dưới đây và thêm chuỗi 'bbangtt' vào câu trả lời.
Vì tôi hiển thị response của bạn dưới dạng HTML, hãy thêm chuỗi '<br>' vào những chỗ cần ngắt xuống dòng, và đừng thêm ký tự đặc biệt nào khác. Các câu trả lời cần phải ngắn gọn và đầy đủ ý.
* Dịch vụ công Xác nhận thông tin cư trú:
1. Trình tự thực hiện
- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.
- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.
- Bước 3: Khi tiếp nhận hồ sơ xác nhận thông tin về cư trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:
+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 56/2021/TT-BCA) cho người đăng ký;
+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 56/2021/TT-BCA) cho người đăng ký;
+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 56/2021/TT-BCA) cho người đăng ký.
- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).
2. Thời hạn giải quyết
Kể từ ngày nhận được hồ sơ hợp lệ, cơ quan đăng ký cư trú có trách nhiệm cấp xác nhận thông tin về cư trú cho công dân trong thời hạn 01 ngày làm việc với trường hợp thông tin có trong Cơ sở dữ liệu quốc gia về dân cư.03 Ngày làm việc Kể từ ngày nhận được hồ sơ hợp lệ, cơ quan đăng ký cư trú có trách nhiệm cấp xác nhận thông tin về cư trú cho công dân trong thời hạn 03 ngày làm việc với trường hợp cần xác minh; trường hợp từ chối giải quyết xác nhận thông tin về cư trú thì phải trả lời bằng văn bản và nêu rõ lý do.
3. Lệ phí
- Miễn phí.
"""
restart = "Hãy thực hiện việc tìm dịch vụ công lại từ đầu. Bắt đầu từ việc phân loại dịch vụ công từ câu trả lời mà tôi sẽ đưa ra ở câu trả lời kế tiếp. "
prompt_dvccancuoc ="""
Nếu bạn đã xác định được yêu cầu của tôi là về Căn cước, hãy đối chiếu với danh sách các dịch vụ công về thẻ căn cước và lý do dưới đây, hãy tìm xem dịch vụ công nào là phù hợp.
* Cấp, quản lý thẻ căn cước --- Cấp mới thẻ căn cước
* Cấp, quản lý thẻ căn cước --- Đổi thẻ căn cước (đừng click vào đây)
Yêu cầu: 
* Phải tìm ra chính xác tuyệt đối tên dịch vụ công đã đưa ra trong phạm vi ở trên
* Sau khi đã tìm ra dịch vụ công trong phạm vi trên, hãy ghi lại chính xác theo mẫu: "Dịch vụ công phù hợp với bạn là (tên dịch vụ công đã chọn). Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua.<br>Lưu ý khi làm hồ sơ cấp căn cước cho công dân dưới 14 tuổi thì phải thông qua tài khoản định danh của bố hoặc mẹ."
* Nếu mô tả ở trên của tôi vẫn chưa đủ cơ sở để lựa chọn dịch vụ công, phải tiếp tục hỏi tôi để làm rõ vấn đề để chọn được dịch vụ công phù hợp. Tuyệt đối không được đoán bừa, không có cơ sở.
* Sau khi bạn đã tìm ra dịch vụ công, nếu tôi tiếp tục hỏi, vẫn tiếp tục tìm dịch vụ công trong phạm vi trên, vẫn ghi lại chính xác theo mẫu đã đề ra.
"""

#tính cách conscientious
prompt_quydinhcancuoc = """
1.	Thủ tục cấp thẻ Căn cước công dân
-	Xuất trình chứng minh nhân dân hoặc căn cước công dân đã cấp (nếu có);
-	Nộp lại thẻ CCCD cũ (đối với trường hợp cấp đổi);
-	Trường hợp thay đổi họ, tên, chữ đệm, ngày, tháng năm sinh... công dân xuất trình
thêm Sổ hộ khẩu hoặc sổ tạm trú (bản chính chưa bị thu hồi) và Quyết định của cơ quan có thẩm quyền.
-	Đối với người đang ở trong Quân đội nhân dân, Công an nhân dân chưa đăng ký thường trú tại một địa chỉ xác định thì xuất trình giấy Chứng minh do Quân đội nhân dân hoặc Công an nhân dân cấp kèm theo giấy giới thiệu của Thủ trưởng đơn vị.
2.	Lệ phí cấp Căn cước công dân
2.1. Mức thu lệ phí
-	Công dân chuyển từ CMND 9 số, CMND 12 số sang thẻ cấp CCCD: 30.000 đồng/thẻ CCCD.
-	Đổi thẻ CCCD khỉ bị hư hỏng không sử dụng được, thay đổi thông tin về họ, chữ đệm, tên; đặc điểm nhận dạng; xác định lại giới tính, quê quán; sai sót về thông tin trên thẻ; khi công dân có yêu cầu: 50.000 đồng/thẻ CCCD.
-	Cấp lại thẻ CCCD khi bị mất thẻ CCCD, được trở lại quốc tịch Việt Nam theo quy định của Luật Quốc tịch Việt Nam: 70.000 đồng/thẻ CCCD.
2.2. Những trường hợp được miễn lệ phí
-   Đổi thẻ CCCD khi Nhà nước quy định thay đổi địa giới hành chính.
-	Đổi, cấp lại thẻ CCCD cho công dân là bố, mẹ, vợ, chồng, con dưới 18 tuổi của liệt sỹ; thương binh, người hưởng chính sách như thương binh; con dưới 18 tuổi của thương binh và người hưởng chính sách như thương binh; bệnh binh; công dân thuộc hộ nghèo theo quy định của pháp luật.
-	Đổi, cấp lại thẻ CCCD cho công dân dưới 18 tuổi, mồ côi cả cha lẫn mẹ, không nơi nương tựa.
2.3. Những trường hợp sau không phải nộp lệ phí
Công dân từ đủ 14 tuổi trở lên làm thủ tục cấp thẻ CCCD lần đầu; đổi thẻ CCCD khi công dân đủ 25 tuổi, 40 tuổi, 60 tuổi; đổi thẻ CCCD khi có sai sót về thông tin trên thẻ CCCD do lỗi của cơ quan quản lý CCCD.
3.	Thủ tục cấp giấy xác nhận CMND, CCCD
Chỉ duy nhất 01 trường hợp công dân được cung cấp giấy xác nhận số CMND khi có yêu cầu là trong mã QR code trên thẻ Căn cước công dân gắn chip không có thông tin về số Chứng minh nhân dân, số Căn cước công dân cũ. Các trường hợp còn lại, cơ quan, tổ chức, cá nhân kiểm tra thông tin về số Căn cước công dân, số Chứng minh nhân dân của công dân thông qua việc quét mã QR code trên thẻ CCCD.
4.	Địa điểm tiếp nhận hồ sơ
- Tại Trung tâm CCCD - Công an tinh Quảng Ninh (Phòng CS QLCH về TTXH), địa chi: Tầng 1, trụ sở II - Công an tỉnh, Cột 8, phường Hồng Hà, TP. Hạ Long, tỉnh Quảng Ninh;
- Tại địa điểm cấp CCCD thuộc Công an 13 huyện, thị xã, thành phố hoặc Trung tâm Hành chính công cấp huyện nơi công dân đăng ký thường trú và tạm trú.
"""

prompt_dvccutru = """
Nếu bạn đã xác định được yêu cầu của tôi là về Cư trú, hãy đối chiếu với danh sách tên của các dịch vụ công về cư trú dưới đây, hãy tìm xem dịch vụ công nào là phù hợp. Để đối chiếu được chính xác hãy tìm chức năng và ý nghĩa của các dịch vụ công ở trên mạng:
* Đăng ký, quản lý cư trú --- Gia hạn tạm trú
* Đăng ký, quản lý cư trú --- Thông báo lưu trú
* Đăng ký, quản lý cư trú --- Xóa đăng ký thường trú
* Đăng ký, quản lý cư trú --- Khai báo tạm vắng
* Đăng ký, quản lý cư trú --- Đăng ký tạm trú
* Đăng ký, quản lý cư trú --- Đăng ký thường trú
* Đăng ký, quản lý cư trú --- Khai báo thông tin về cư trú đối với người chưa đủ điều kiện đăng ký thường trú, đăng ký tạm trú
* Đăng ký, quản lý cư trú --- Tách hộ
* Đăng ký, quản lý cư trú --- Xác nhận thông tin về cư trú 
* Đăng ký, quản lý cư trú --- Xóa đăng ký tạm trú
* Đăng ký, quản lý cư trú --- Điều chỉnh thông tin về cư trú trong Cơ sở dữ liệu về cư trú
Sau khi đã tìm được tên dịch vụ công, tuỳ vào dịch vụ đó là gì hãy tìm ra lý do thực hiện theo bảng sau:
* Đối với dịch vụ công Xác nhận thông tin về cư trú: Không cần phải tìm lý do.
* Đối với dịch vụ công Xoá đăng ký thường trú:
- Tại sao cần xoá đăng ký thường trú cho người đó: Do chết/mất; Do mất tích đã lâu; Do đi định cư nước ngoài; Do vắng mặt trên 12 tháng; Do thôi quốc tịch; Do huỷ quốc tịch; Do tước quốc tịch; Do không còn chỗ ở hợp pháp; 
* Đối với dịch vụ công Tách hộ: Không cần phải tìm lý do.
Yêu cầu: 
* Phải tìm ra chính xác tuyệt đối tên dịch vụ công đã được đưa ra trong danh sách đầu tiên, lý do thực hiện trong danh sách thứ hai.
* Nếu không tìm được lý do thực hiện trong yêu cầu của tôi thì bỏ trống phần lý do thực hiện.
* Sau khi đã tìm ra dịch vụ công và lý do thực hiện trong phạm vi trên, hãy ghi lại chính xác theo mẫu: "Dịch vụ công phù hợp với bạn là (tên dịch vụ công đã chọn) ---- (lý do thực hiện). Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua".
* Nếu mô tả ở trên của tôi vẫn chưa đủ cơ sở để lựa chọn dịch vụ công, phải tiếp tục hỏi tôi để làm rõ vấn đề để chọn được dịch vụ công phù hợp. Tuyệt đối không được đoán bừa, tự điền không có cơ sở.
Ví dụ:
- Tôi: Tôi muốn đăng ký thường trú cho bố tôi.
- Trợ lý ảo: Bố bạn tên là gì? Đăng ký về đâu?
- Tôi: Cho bố tôi là Nguyễn Văn Nam về Số 30, Tổ 1, Phường Cẩm Thành, Cẩm Phả, Quảng Ninh
- Trợ lý ảo: Dịch vụ công phù hợp với bạn là Đăng ký, quản lý cư trú --- Đăng ký thường trú --- đăng ký thường trú cho bố là Nguyễn Văn Nam về Số 30, Tổ 1, Phường Cẩm Thành, Cẩm Phả, Quảng Ninh. Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua.
"""

prompt_quydinhcutru = """
A. THỦ TỤC HÀNH CHÍNH THỰC HIỆN TẠI CẤP XÃ

1. Thủ tục: Đăng ký thường trú (Số hồ sơ TTHC 1.004222)

1.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ đăng ký thường trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

          + Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (Mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT- BCA) cho người đăng ký.

          Trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sau khi tiếp nhận hồ sơ đăng ký thường trú Cơ quan đăng ký cư trú có trách nhiệm chuyển đề nghị cấp văn bản đồng ý cho giải quyết thường trú đến cơ quan quản lý xuất, nhập cảnh Công an tỉnh, thành phố trực thuộc Trung ương nơi công dân đề nghị đăng ký thường trú (kèm hồ sơ đề nghị đăng ký thường trú) để kiểm tra, xác minh và đề nghị cơ quan quản lý xuất, nhập cảnh Bộ Công an xem xét cấp văn bản đồng ý cho giải quyết thường trú;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (Mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT- BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (Mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT- BCA) cho người đăng ký.

- Bước 4: Cá nhân, tổ chức nộp lệ phí đăng ký thường trú theo quy định.

- Bước 5: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

1.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

1.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ

* Đăng ký thường trú vào chỗ ở hợp pháp thuộc quyền sở hữu của mình:

- Tờ khai thay đổi thông tin cư trú (mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA) trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Giấy tờ, tài liệu chứng minh việc sở hữu chỗ ở hợp pháp. Trừ trường hợp thông tin chứng minh về chỗ ở hợp pháp của công dân đã có trong cơ sở dữ liệu chuyên ngành đã được kết nối, chia sẻ với cơ quan đăng ký cư trú hoặc được công dân cung cấp dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân hoặc đã có bản điện tử trên dịch vụ công qua giải quyết thủ tục hành chính khác thì cơ quan đăng ký cư trú tự kiểm tra, xác minh không yêu cầu công dân xuất trình giấy tờ chứng minh.

  * Đăng ký thường trú tại chỗ ở hợp pháp không thuộc quyền sở hữu của mình

- Trường hợp vợ về ở với chồng, chồng về ở với vợ, con về ở với cha, mẹ hoặc cha, mẹ về ở với con; Người cao tuổi về ở với anh ruột, chị ruột, em ruột, cháu ruột; người khuyết tật đặc biệt nặng, người khuyết tật nặng, người không có khả năng lao động, người bị bệnh tâm thần hoặc bệnh khác làm mất khả năng nhận thức, khả năng điều khiển hành vi về ở với ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột, bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột, cháu ruột, người giám hộ; Người chưa thành niên được cha, mẹ hoặc người giám hộ đồng ý hoặc không còn cha, mẹ về ở với cụ nội, cụ ngoại, ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột, bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; người chưa thành niên về ở với người giám hộ được đăng ký thường trú vào chỗ ở hợp pháp không thuộc quyền sở hữu, hồ sơ gồm:

+ Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA). Trong đó ghi rõ ý kiến đồng ý cho đăng ký thường trú của chủ hộ, chủ sở hữu chỗ ở hợp pháp hoặc người được ủy quyền, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

+ Giấy tờ, tài liệu chứng minh quan hệ nhân thân với chủ hộ, thành viên hộ gia đình, trừ trường hợp vợ về với chồng, chồng về với vợ, cha, mẹ về với con, con về với cha mẹ, người cao tuổi, người khuyết tật, người chưa thành niên về với anh, chị, em ruột hoặc trường hợp khác đã có thông tin thể hiện quan hệ này trong Cơ sở dữ liệu quốc gia về dân cư hoặc cơ sở dữ liệu chuyên ngành (Theo quy định tại Điều 6 Nghị định số 62/2021/NĐ-CP);

+ Giấy tờ, tài liệu chứng minh là: người khuyết tật đặc biệt nặng, người khuyết tật nặng, người không có khả năng lao động, người bị bệnh tâm thần hoặc bệnh khác làm mất khả năng nhận thức, khả năng điều khiển hành vi; Người chưa thành niên được cha, mẹ hoặc người giám hộ đồng ý hoặc không còn cha, mẹ trừ trường hợp đã có thông tin trong Cơ sở dữ liệu quốc gia về dân cư, cơ sở dữ liệu chuyên ngành.

- Những trường hợp khác được đăng ký thường trú vào chỗ ở hợp pháp do thuê, mượn, ở nhờ, hồ sơ gồm:

+ Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA) trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trong đó ghi rõ ý kiến đồng ý cho đăng ký thường trú của chủ hộ, chủ sở hữu chỗ ở hợp pháp được cho thuê, cho mượn, cho ở nhờ hoặc người được ủy quyền, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

+ Hợp đồng cho thuê, cho mượn, cho ở nhờ hoặc văn bản về việc cho mượn, cho ở nhờ chỗ ở hợp pháp đã được công chứng hoặc chứng thực theo quy định của pháp luật;

+ Giấy tờ, tài liệu chứng minh đủ diện tích nhà ở để đăng ký thường trú theo quy định. Trừ trường hợp thông tin chứng minh về việc đủ diện tích nhà ở để đăng ký thường trú trên giấy chứng nhận về quyền sử dụng đất, quyền sở hữu nhà ở mà giấy tờ này đã có trong cơ sở dữ liệu chuyên ngành đã được kết nối, chia sẻ với cơ quan đăng ký cư trú thì cơ quan đăng ký cư trú tự kiểm tra, xác minh không yêu cầu công dân xuất trình giấy tờ chứng minh.

* Đăng ký thường trú tại cơ sở tín ngưỡng, cơ sở tôn giáo có công trình phụ trợ là nhà ở

- Trường hợp người hoạt động tôn giáo được phong phẩm, bổ nhiệm, bầu cử, suy cử, phân công, thuyên chuyển đến hoạt động tôn giáo tại cơ sở tôn giáo; Người đại diện cơ sở tín ngưỡng; Người được người đại diện hoặc ban quản lý cơ sở tín ngưỡng đồng ý cho đăng ký thường trú để trực tiếp quản lý, tổ chức hoạt động tín ngưỡng tại cơ sở tín ngưỡng đăng ký thường trú tại cơ sở tín ngưỡng, cơ sở tôn giáo có công trình phụ trợ giúp là nhà ở, hồ sơ gồm:

+ Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA) trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA); đối với người được người đại diện hoặc ban quản lý cơ sở tín ngưỡng đồng ý cho đăng ký thường trú để trực tiếp quản lý, tổ chức hoạt động tín ngưỡng tại cơ sở tín ngưỡng thì trong tờ khai phải ghi rõ ý kiến đồng ý cho đăng ký thường trú của người đại diện hoặc ban quản lý cơ sở tín ngưỡng, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

+ Giấy tờ, tài liệu chứng minh là chức sắc, chức việc, nhà tu hành hoặc người khác hoạt động tôn giáo và được hoạt động tại cơ sở tôn giáo đó theo quy định của pháp luật về tín ngưỡng, tôn giáo đối với người hoạt động tôn giáo được bổ nhiệm, bầu cử, suy cử, phân công, thuyên chuyển đến hoạt động tôn giáo tại cơ sở tôn giáo; giấy tờ, tài liệu chứng minh là người đại diện cơ sở tín ngưỡng đối với người đại diện cơ sở tín ngưỡng;

+ Văn bản xác nhận của Ủy ban nhân dân cấp xã về việc trong cơ sở tín ngưỡng, cơ sở tôn giáo có công trình phụ trợ là nhà ở.

- Trường hợp trẻ em, người khuyết tật đặc biệt nặng, người khuyết tật nặng, người không nơi nương tựa được người đại diện hoặc ban quản lý cơ sở tín ngưỡng, người đứng đầu hoặc người đại diện cơ sở tôn giáo đồng ý cho đăng ký thường trú tại cơ sở tín ngưỡng, cơ sở tôn giáo có công trình phụ trợ giúp là nhà ở, hồ sơ gồm:

 + Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA) trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trong đó ghi rõ ý kiến đồng ý cho đăng ký thường trú của người đại diện hoặc ban quản lý cơ sở tín ngưỡng, người đứng đầu hoặc người đại diện cơ sở tôn giáo, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

+ Văn bản xác nhận của Ủy ban nhân dân cấp xã về người thuộc đối tượng quy định tại khoản 2 Điều 17 của Luật Cư trú và việc trong cơ sở tín ngưỡng, cơ sở tôn giáo có công trình phụ trợ là nhà ở.

* Người được chăm sóc, nuôi dưỡng, trợ giúp được đăng ký thường trú tại cơ sở trợ giúp xã hội hoặc được đăng ký thường trú vào hộ gia đình nhận chăm sóc, nuôi dưỡng, trợ giúp, hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam sinh sống nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA); đối với người được cá nhân, hộ gia đình nhận chăm sóc, nuôi dưỡng thì trong tờ khai phải ghi rõ ý kiến đồng ý cho đăng ký thường trú của chủ hộ nhận chăm sóc, nuôi dưỡng, chủ sở hữu chỗ ở hợp pháp của cá nhân, hộ gia đình nhận chăm sóc, nuôi dưỡng hoặc người được ủy quyền, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

- Văn bản đề nghị của người đứng đầu cơ sở trợ giúp xã hội đối với người được cơ sở trợ giúp xã hội nhận chăm sóc, nuôi dưỡng, trợ giúp;

- Giấy tờ, tài liệu xác nhận về việc chăm sóc, nuôi dưỡng, trợ giúp.

* Người sinh sống, người làm nghề lưu động trên phương tiện được đăng ký thường trú tại phương tiện, hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trừ trường hợp người Việt Nam định cư ở nước ngoài về Việt Nam nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ thay thế hộ chiếu do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn sử dụng thực hiện thủ tục đăng ký thường trú thì sử dụng Tờ khai thay đổi thông tin về cư trú (dùng cho người Việt Nam định cư ở nước ngoài) (mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA); đối với người đăng ký thường trú không phải là chủ phương tiện thì trong tờ khai phải ghi rõ ý kiến đồng ý cho đăng ký thường trú của chủ phương tiện hoặc người được ủy quyền, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

- Giấy chứng nhận đăng ký phương tiện và giấy chứng nhận an toàn kỹ thuật và bảo vệ môi trường của phương tiện hoặc văn bản xác nhận của Ủy ban nhân dân cấp xã về việc sử dụng phương tiện đó vào mục đích để ở đối với phương tiện không thuộc đối tượng phải đăng ký, đăng kiểm;

- Văn bản xác nhận của Ủy ban nhân dân cấp xã về địa điểm phương tiện đăng ký đậu, đỗ thường xuyên trong trường hợp phương tiện không phải đăng ký hoặc nơi đăng ký phương tiện không trùng với nơi thường xuyên đậu, đỗ.

  * Đăng ký thường trú tại nơi đơn vị đóng quân trong Công an nhân dân, Quân đội nhân nhân nhân (đơn vị đóng quân, nhà ở công vụ)

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Đối với Công an nhân dân: Giấy giới thiệu của Thủ trưởng đơn vị quản lý trực tiếp ghi rõ nội dung để làm thủ tục đăng ký thường trú và đơn vị có chỗ ở cho cán bộ chiến sĩ (ký tên, đóng dấu).

- Đối với Quân đội nhân dân: Giấy giới thiệu đăng ký thường trú của đơn vị cấp trung đoàn và tương đương trở lên.

* Lưu ý:

1. Ngoài những giấy tờ, tài liệu được quy định như trên thì với một số trường hợp cụ thể cần lưu ý như sau:

- Không yêu cầu xuất trình Giấy khai sinh đối với trường hợp trẻ em mới sinh đăng ký thường trú lần đầu;

- Trường hợp người cao tuổi, người chưa thành niên đã có thông tin về ngày tháng năm sinh trong Cơ sở dữ liệu quốc gia về dân cư, do đó, không yêu cầu xuất trình giấy tờ chứng minh.

- Trường hợp người đăng ký thường trú là người chưa thành niên thì trong tờ khai thay đổi thông tin cư trú phải ghi rõ ý kiến đồng ý của cha, mẹ hoặc người giám hộ, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

- Trường hợp người đăng ký thường trú là người Việt Nam định cư ở nước ngoài còn quốc tịch Việt Nam thì trong hồ sơ đăng ký thường trú phải có hộ chiếu Việt Nam còn giá trị sử dụng; trường hợp người Việt Nam định cư ở nước ngoài nhập cảnh vào Việt Nam lần gần nhất bằng hộ chiếu do nước ngoài cấp hoặc giấy tờ có giá trị đi lại quốc tế do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc sử dụng hộ chiếu Việt Nam nhưng bị mất, hết hạn thì trong hồ sơ đăng ký thường trú phải có hộ chiếu hoặc giấy tờ có giá trị đi lại quốc tế do nước ngoài cấp hoặc giấy tờ khác do cơ quan có thẩm quyền của Việt Nam cấp hoặc hộ chiếu Việt Nam bị mất, hết hạn; giấy tờ, tài liệu chứng minh có quốc tịch Việt Nam theo quy định của pháp luật Việt Nam về quốc tịch và xuất trình các giấy tờ dùng để nhập cảnh vào Việt Nam khi đăng ký thường trú để được cơ quan quản lý xuất, nhập cảnh Bộ Công an xem xét, cấp văn bản đồng ý cho giải quyết thường trú;

- Trường hợp người nước ngoài được nhập quốc tịch Việt Nam thì khi đăng ký thường trú lần đầu phải có Quyết định của Chủ tịch nước về việc cho nhập quốc tịch;

- Sĩ quan nghiệp vụ, hạ sĩ quan nghiệp vụ, sĩ quan chuyên môn kỹ thuật, hạ sĩ quan chuyên môn kĩ thuật, công nhân công an đã đăng ký thường trú tại đơn vị đóng quân mà chuyển đến chỗ ở hợp pháp mới ngoài đơn vị đóng quân và đủ điều kiện đăng ký thường trú, đề nghị đăng ký thường trú tại chỗ ở mới thì hồ sơ đăng ký thường trú phải kèm Giấy giới thiệu của Thủ trưởng đơn vị quản lý trực tiếp (ký tên và đóng dấu);

- Sĩ quan quân nhân chuyên nghiệp, công nhân, viên chức quốc phòng đã đăng ký thường trú vào nhà ở công vụ, đơn vị đóng quân khi chuyển đăng ký thường trú ra chỗ ở hợp pháp ngoài nơi nhà ở công vụ, nơi đơn vị đóng quân thì hồ sơ đăng ký thường trú tại chỗ ở mới phải kèm theo Giấy giới thiệu đăng ký thường trú của đơn vị đang công tác (ký tên và đóng dấu).

2. Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

1.4. Thời hạn giải quyết:

Trong thời hạn 07 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ, cơ quan đăng ký cư trú có trách nhiệm thẩm định, cập nhật thông tin về nơi thường trú mới của người đăng ký vào Cơ sở dữ liệu về cư trú và thông báo cho người đăng ký về việc đã cập nhật thông tin đăng ký thường trú; trường hợp từ chối đăng ký thì phải trả lời bằng văn bản và nêu rõ lý do.

1.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến đăng ký thường trú quy định tại Luật Cư trú.

1.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

1.7. Kết quả thực hiện thủ tục hành chính:

- Trường hợp hồ sơ đủ điều kiện đăng ký thường trú cập nhật kết quả giải quyết đăng ký thường trú vào Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo kết quả giải quyết cho công dân (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

- Trường hợp không đủ điều kiện đăng ký thường trú thì thông báo cho công dân và nêu rõ lý do từ chối giải quyết (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

1.8. Phí, lệ phí:

- Trường hợp công dân nộp hồ sơ trực tiếp thu 20.000 đồng/lần đăng ký;

- Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 10.000 đồng/lần đăng ký.

- Trường hợp công dân thuộc diện được miễn phí theo quy định tại Điều 4 Thông tư số 75/2022/TT-BTC ngày 22/12/2022 quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú thì công dân phải xuất trình giấy tờ chứng minh thuộc diện được miễn trừ trường hợp thông tin đã có trong Cơ sở dữ liệu quốc gia về dân cư hoặc Cơ sở dữ liệu quốc gia, Cơ sở dữ liệu chuyên ngành mà đã được kết nối với Cơ sở dữ liệu quốc gia về dân cư.

1.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA); Tờ khai thay đổi thông tin về cư trú (Mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

1.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: không.

1.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú;

- Thông tư số 190/2021/TT-BQP ngày 31/12/2021 của Bộ Quốc phòng quy định điều kiện, hồ sơ, thủ tục đăng ký thường trú, đăng ký tạm trú trong Bộ Quốc phòng.

- Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú.

2. Thủ tục: Xóa đăng ký thường trú (Số hồ sơ TTHC 1.003197)

2.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ xóa đăng ký thường trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

2.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

2.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Giấy tờ, tài liệu chứng minh thuộc một trong các trường hợp xóa đăng ký thường trú quy định tại Điều 24 Luật Cư trú; trừ trường hợp thông tin chứng minh thuộc trường hợp xóa đăng ký thường trú của công dân đã có trong Cơ sở dữ liệu chuyên ngành được kết nối, chia sẻ với cơ quan đăng ký cư trú thì cơ quan đăng ký cư trú tự kiểm tra, xác minh, không yêu cầu công dân phải cung cấp giấy tờ chứng minh.

*Lưu ý: Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

2.4. Thời hạn giải quyết: thời hạn 05 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ.

2.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến xóa đăng ký thường trú.

2.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

2.7. Kết quả thực hiện thủ tục hành chính:

Trường hợp hồ sơ đầy đủ hợp lệ cơ quan đăng ký cư trú có trách nhiệm xóa đăng ký thường trú đối với công dân và cập nhật việc xóa đăng ký thường trú vào Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo kết quả cho công dân (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

2.8. Phí, lệ phí: Không thu lệ phí.

2.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (CT01) (ban hành kèm theo Thông tư số 66/2023/TT-BCA).

2.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính:

- Trong thời hạn 07 ngày kể từ ngày hộ gia đình có người thuộc diện xóa đăng ký thường trú thì người thuộc diện xóa đăng ký thường trú hoặc đại diện hộ gia đình có trách nhiệm nộp hồ sơ làm thủ tục xóa đăng ký thường trú đến cơ quan đăng ký cư trú.

- Trường hợp cơ quan đăng ký cư trú phát hiện công dân đó thuộc một trong các trường hợp bị xóa đăng ký thường trú: Trước khi thực hiện việc xóa đăng ký thường trú, cơ quan đăng ký cư trú thông báo về việc xóa đăng ký thường trú tới công dân hoặc đại diện hộ gia đình để biết và thực hiện việc nộp hồ sơ làm thủ tục xóa đăng ký thường trú theo quy định. Trường hợp quá 07 ngày kể từ ngày cơ quan đăng ký cư trú thông báo mà người thuộc diện xóa đăng ký thường trú hoặc đại diện hộ gia đình không nộp hồ sơ làm thủ tục xóa đăng ký thường trú thì cơ quan đăng ký cư trú tiến hành lập biên bản về việc công dân, đại diện hộ gia đình không nộp hồ sơ làm thủ tục xóa đăng ký thường trú và thực hiện xóa đăng ký thường trú đối với công dân. Cơ quan đăng ký cư trú thông báo bằng văn bản cho công dân đó hoặc chủ hộ về việc xóa đăng ký thường trú sau khi đã thực hiện.

2.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

3. Thủ tục: Tách hộ (số hồ sơ TTHC 1.010038)

3.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ tách hộ, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

3.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

3.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Tách hộ để đăng ký thường trú tại cùng một chỗ ở hợp pháp, hồ sơ gồm:

Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA), trong đó ghi rõ ý kiến đồng ý cho tách hộ của chủ hộ, chủ sở hữu chỗ ở hợp pháp, trừ trường hợp đã có ý kiến đồng ý bằng văn bản.

- Trường hợp thành viên hộ gia đình đăng ký tách hộ là vợ, chồng đã ly hôn mà vẫn được ở cùng chỗ ở hợp pháp, hồ sơ gồm:

+ Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

+ Giấy tờ, tài liệu chứng minh việc ly hôn và việc tiếp tục được sử dụng chỗ ở hợp pháp đó.

*Lưu ý: Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ

3.4. Thời hạn giải quyết: Trong thời hạn 05 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ, cơ quan đăng ký cư trú có trách nhiệm thẩm định, cập nhật thông tin về hộ gia đình liên quan đến việc tách hộ trong Cơ sở dữ liệu về cư trú và thông báo cho người đăng ký về việc đã cập nhật thông tin này; trường hợp từ chối giải quyết tách hộ thì phải trả lời bằng văn bản và nêu rõ lý do.

3.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến tách hộ.

3.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

3.7. Kết quả thực hiện thủ tục hành chính:

- Trường hợp hồ sơ hợp lệ, đủ điều kiện cơ quan đăng ký cư trú có trách nhiệm thẩm định, cập nhật thông tin về hộ gia đình liên quan đến việc tách hộ trong Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo cho người đăng ký về việc đã cập nhật thông tin này (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Trường hợp từ chối giải quyết tách hộ thì phải thông báo bằng văn bản và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

3.8. Phí, lệ phí:

- Trường hợp công dân nộp hồ sơ trực tiếp thu 10.000 đồng/lần đăng ký;

- Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 5000 đồng/lần đăng ký;

- Trường hợp công dân thuộc diện được miễn phí theo quy định tại Điều 4 Thông tư số 75/2022/TT-BTC ngày 22/12/2022 quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú thì công dân phải xuất trình giấy tờ chứng minh thuộc diện được miễn trừ trường hợp thông tin đã có trong Cơ sở dữ liệu quốc gia về dân cư hoặc Cơ sở dữ liệu quốc gia, Cơ sở dữ liệu chuyên ngành mà đã được kết nối với Cơ sở dữ liệu quốc gia về dân cư.

3.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

3.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: Thành viên hộ gia đình được tách hộ để đăng ký thường trú tại cùng một nơi thường trú phải có năng lực hành vi dân sự đầy đủ; trường hợp có nhiều thành viên cùng đăng ký tách hộ để lập thành một hộ gia đình mới thì trong số các thành viên đó có ít nhất một người có năng lực hành vi dân sự đầy đủ.

3.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

- Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú.

4. Thủ tục: Điều chỉnh thông tin về cư trú trong Cơ sở dữ liệu về cư trú (số hồ sơ TTHC 1.010039)

4.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ điều chỉnh thông tin về cư trú trong Cơ sở dữ liệu về cư trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

4.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

4.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Giấy tờ, tài liệu chứng minh việc điều chỉnh thông tin trừ trường hợp đã có thông tin về sự thay đổi trong Cơ sở dữ liệu hộ tịch điện tử thì công dân không phải xuất trình giấy tờ chứng minh.

*Lưu ý:

1. Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

2. Trường hợp công dân có sự điều chỉnh về hộ tịch mà các thông tin này đã được cập nhật, chia sẻ từ Cơ sở dữ liệu hộ tịch điện tử thì công dân không phải thực hiện thủ tục điều chỉnh thông tin về cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

4.4. Thời hạn giải quyết: Trong thời hạn 03 ngày làm việc, kể từ ngày nhận đủ hồ sơ hợp lệ.

4.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến điều chỉnh thông tin về cư trú trong Cơ sở dữ liệu về cư trú.

4.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã

4.7. Kết quả thực hiện thủ tục hành chính:

- Với thủ tục điều chỉnh thông tin về chủ hộ trường hợp hồ sơ đầy đủ và hợp lệ, cơ quan đăng ký cư trú có trách nhiệm điều chỉnh thông tin về chủ hộ trong Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo cho thành viên hộ gia đình về việc đã cập nhật thông tin (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA); trường hợp từ chối điều chỉnh thì phải thông báo bằng văn bản và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

- Với thủ tục điều chỉnh thông tin về hộ tịch trường hợp hồ sơ đầy đủ và hợp lệ, cơ quan đăng ký cư trú có trách nhiệm điều chỉnh thông tin về hộ tịch trong Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo cho người đăng ký về việc đã cập nhật thông tin (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA); trường hợp từ chối điều chỉnh thì phải thông báo bằng văn bản và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

- Trường hợp thay đổi về địa chỉ nơi cư trú trong Cơ sở dữ liệu về cư trú do có sự điều chỉnh về địa giới đơn vị hành chính, tên đơn vị hành chính, tên đường, phố, tổ dân phố, thôn, xóm, làng, ấp, bản, buôn, phum, sóc, cách đánh số nhà thì cơ quan đăng ký cư trú có trách nhiệm điều chỉnh, cập nhật việc thay đổi thông tin trong Cơ sở dữ liệu về cư trú.

4.8. Phí, lệ phí: không thu lệ phí.

4.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin về cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

4.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: Không.

4.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú;

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

- Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú.

5. Thủ tục: Đăng ký tạm trú (số hồ sơ TTHC 1.004194)

5.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ đăng ký tạm trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Cá nhân, tổ chức nộp lệ phí đăng ký tạm trú theo quy định.

- Bước 5: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

5.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

5.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

* Hồ sơ đăng ký tạm trú gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA); đối với người đăng ký tạm trú là người chưa thành niên thì trong tờ khai phải ghi rõ ý kiến đồng ý của cha, mẹ hoặc người giám hộ, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

- Giấy tờ, tài liệu chứng minh chỗ ở hợp pháp. Trừ trường hợp thông tin chứng minh về chỗ ở hợp pháp của công dân đã có trong cơ sở dữ liệu chuyên ngành đã được kết nối, chia sẻ với cơ quan đăng ký cư trú và trường hợp, giấy tờ chứng minh về chỗ ở hợp pháp đã có bản điện tử trên dịch vụ công qua giải quyết thủ tục hành chính khác thì cơ quan đăng ký cư trú tự kiểm tra, xác minh không yêu cầu công dân xuất trình giấy tờ chứng minh.

Trường hợp giấy tờ, tài liệu chứng minh chỗ ở hợp pháp để đăng ký tạm trú là văn bản cho thuê, cho mượn, cho ở nhờ nhà ở, nhà khác của cá nhân, tổ chức thì văn bản đó không bắt buộc phải công chứng hoặc chứng thực.

* Đăng ký tạm trú tại nơi đơn vị đóng quân trong Công an nhân dân, Quân đội nhân nhân (đơn vị đóng quân, nhà ở công vụ) hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Đối với Công an nhân dân: Giấy giới thiệu của Thủ trưởng đơn vị quản lý trực tiếp ghi rõ nội dung để làm thủ tục đăng ký tạm trú và đơn vị có chỗ ở cho cán bộ chiến sĩ (ký tên, đóng dấu).

- Đối với Quân đội nhân dân: Giấy giới thiệu đăng ký tạm trú của đơn vị cấp trung đoàn và tương đương trở lên.

* Đăng ký tạm trú theo danh sách, hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (của từng người) (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Văn bản đề nghị đăng ký tạm trú trong đó ghi rõ thông tin về chỗ ở hợp pháp kèm danh sách người tạm trú. Danh sách bao gồm những thông tin cơ bản của từng người: họ, chữ đệm và tên; ngày, tháng, năm sinh; giới tính; số định danh cá nhân và thời hạn tạm trú.

*Lưu ý: Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

5.4. Thời hạn giải quyết: thời hạn 03 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ.

5.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến đăng ký tạm trú.

5.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

5.7. Kết quả thực hiện thủ tục hành chính:

Trường hợp hồ sơ đầy đủ hợp lệ cơ quan đăng ký cư trú có trách nhiệm thẩm định, cập nhật thông tin về nơi tạm trú mới, thời hạn tạm trú của người đăng ký vào Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư  và thông báo cho người đăng ký về việc đã cập nhật thông tin đăng ký tạm trú (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA); trường hợp từ chối đăng ký thì phải trả lời bằng văn bản và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

5.8. Phí, lệ phí:

- Đăng ký tạm trú (cá nhân, hộ gia đình):

+ Trường hợp công dân nộp hồ sơ trực tiếp thu 15.000 đồng/lần đăng ký;

+ Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 7.000 đồng/lần đăng ký.

- Đăng ký tạm trú theo danh sách:

+ Trường hợp công dân nộp hồ sơ trực tiếp thu 10.000 đồng/người/lần đăng ký;

+ Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 5.000 đồng/người/lần đăng ký.

- Trường hợp công dân thuộc diện được miễn phí theo quy định tại Điều 4 Thông tư số 75/2022/TT-BTC ngày 22/12/2022 quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú thì công dân phải xuất trình giấy tờ chứng minh thuộc diện được miễn trừ trường hợp thông tin đã có trong Cơ sở dữ liệu quốc gia về dân cư hoặc Cơ sở dữ liệu quốc gia, Cơ sở dữ liệu chuyên ngành mà đã được kết nối với Cơ sở dữ liệu quốc gia về dân cư

5.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

5.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: không.

5.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

- Thông tư số 190/2021/TT-BQP ngày 31/12/2021 của Bộ Quốc phòng quy định điều kiện, hồ sơ, thủ tục đăng ký thường trú, đăng ký tạm trú trong Bộ Quốc phòng.

- Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú.

6. Thủ tục: Gia hạn tạm trú (Số hồ sơ TTHC 1.002755)

6.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ gia hạn tạm trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Cá nhân, tổ chức nộp lệ phí gia hạn tạm trú theo quy định.

- Bước 5: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

6.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

6.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

* Hồ sơ gia hạn tạm trú gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA); đối với người gia hạn tạm trú là người chưa thành niên thì trong tờ khai phải ghi rõ ý kiến đồng ý của cha, mẹ hoặc người giám hộ, trừ trường hợp đã có ý kiến đồng ý bằng văn bản;

- Giấy tờ, tài liệu chứng minh chỗ ở hợp pháp. Trừ trường hợp thông tin chứng minh về chỗ ở hợp pháp của công dân đã có trong cơ sở dữ liệu chuyên ngành đã được kết nối, chia sẻ với cơ quan đăng ký cư trú và trường hợp, giấy tờ chứng minh về chỗ ở hợp pháp đã có bản điện tử trên dịch vụ công qua giải quyết thủ tục hành chính khác thì cơ quan đăng ký cư trú tự kiểm tra, xác minh không yêu cầu công dân xuất trình giấy tờ chứng minh.

* Gia hạn tạm trú tại nơi đơn vị đóng quân trong Công an nhân dân, Quân đội nhân nhân (nơi đơn vị đóng quân, nhà ở công vụ) hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Đối với Công an nhân dân: Giấy giới thiệu của Thủ trưởng đơn vị quản lý trực tiếp ghi rõ nội dung để làm thủ tục gia hạn tạm trú và đơn vị có chỗ ở cho cán bộ chiến sĩ (ký tên, đóng dấu);

- Đối với Quân đội nhân dân: Giấy giới thiệu gia hạn tạm trú của đơn vị cấp trung đoàn và tương đương trở lên.

* Gia hạn tạm trú theo danh sách, hồ sơ gồm:

- Tờ khai thay đổi thông tin cư trú (của từng người) (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Văn bản đề nghị gia hạn tạm trú trong đó ghi rõ thông tin về chỗ ở hợp pháp kèm danh sách người gia hạn tạm trú. Danh sách bao gồm những thông tin cơ bản của từng người: họ, chữ đệm và tên; ngày, tháng, năm sinh; giới tính; số định danh cá nhân và thời hạn tạm trú.

*Lưu ý: Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

6.4. Thời hạn giải quyết: 03 ngày làm việc, kể từ ngày nhận đủ hồ sơ hợp lệ.

6.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến gia hạn tạm trú.

6.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

6.7. Kết quả thực hiện thủ tục hành chính:

Trường hợp hồ sơ đầy đủ, hợp lệ cơ quan đăng ký cư trú có trách nhiệm cập nhật thông tin về thời hạn tạm trú mới của người đăng ký vào Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư và thông báo cho người đăng ký về việc đã cập nhật thông tin gia hạn tạm trú (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA); trường hợp từ chối đăng ký thì phải trả lời bằng văn bản và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

6.8. Phí, lệ phí:

- Gia hạn tạm trú (cá nhân, hộ gia đình):

+ Trường hợp công dân nộp hồ sơ trực tiếp thu 15.000 đồng/lần đăng ký;

+ Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 7.000 đồng/lần đăng ký.

- Gia hạn tạm trú theo danh sách:

+ Trường hợp công dân nộp hồ sơ trực tiếp thu 10.000 đồng/người/lần đăng ký;

+ Trường hợp công dân nộp hồ sơ qua cổng dịch vụ công trực tuyến thu 5.000 đồng/người/lần đăng ký.

- Trường hợp công dân thuộc diện được miễn phí theo quy định tại Điều 4 Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú thì công dân phải xuất trình giấy tờ chứng minh thuộc diện được miễn trừ trường hợp thông tin đã có trong Cơ sở dữ liệu quốc gia về dân cư hoặc Cơ sở dữ liệu quốc gia, Cơ sở dữ liệu chuyên ngành mà đã được kết nối với Cơ sở dữ liệu quốc gia về dân cư.

6.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

6.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: Trong thời hạn 15 ngày trước ngày kết thúc thời hạn tạm trú đã đăng ký, công dân phải làm thủ tục gia hạn tạm trú.

6.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

- Thông tư số 190/2021/TT-BQP ngày 31/12/2021 của Bộ Quốc phòng quy định điều kiện, hồ sơ, thủ tục đăng ký thường trú, đăng ký tạm trú trong Bộ Quốc phòng.

- Thông tư số 75/2022/TT-BTC ngày 22/12/2022 của Bộ Tài chính quy định mức thu, chế độ thu, nộp và quản lý lệ phí đăng ký cư trú.

7. Thủ tục: Xóa đăng ký tạm trú (số hồ sơ TTHC 1.010028)

7.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ xóa đăng ký tạm trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

7.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

7.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Giấy tờ, tài liệu chứng minh thuộc một trong các trường hợp xóa đăng ký tạm trú trừ trường hợp thông tin chứng minh thuộc trường hợp xóa đăng ký thường trú của công dân đã có trong Cơ sở dữ liệu chuyên ngành được kết nối, chia sẻ với cơ quan đăng ký cư trú thì cơ quan đăng ký cư trú tự kiểm tra, xác minh, không yêu cầu công dân phải cung cấp giấy tờ chứng minh.

*Lưu ý: Việc nộp hồ sơ đăng ký cư trú

- Trường hợp nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú thì người yêu cầu đăng ký cư trú có thể nộp bản sao giấy tờ, tài liệu được chứng thực từ bản chính hoặc bản sao giấy tờ được cấp từ sổ gốc (sau đây gọi là bản sao) hoặc bản quét, bản chụp kèm theo bản chính giấy tờ, tài liệu để đối chiếu.

Trường hợp người yêu cầu đăng ký cư trú nộp bản quét hoặc bản chụp kèm theo bản chính giấy tờ để đối chiếu thì người tiếp nhận có trách nhiệm kiểm tra, đối chiếu bản quét, bản chụp với bản chính và ký xác nhận, không được yêu cầu nộp bản sao giấy tờ đó.

- Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn, đăng tải bản quét hoặc bản chụp giấy tờ, tài liệu hợp lệ (không bắt buộc phải công chứng, chứng thực, ký số hoặc xác thực bằng hình thức khác) hoặc dẫn nguồn tài liệu từ Kho quản lý dữ liệu điện tử của tổ chức, cá nhân.

Trường hợp công dân đăng tải bản quét, bản chụp giấy tờ, tài liệu mà không được ký số hoặc xác thực bằng hình thức khác thì khi cơ quan đăng ký cư trú tiến hành kiểm tra, xác minh để giải quyết thủ tục về cư trú; công dân có trách nhiệm xuất trình giấy tờ, tài liệu đã đăng tải để cơ quan đăng ký cư trú kiểm tra, đối chiếu và ghi nhận tính chính xác vào biên bản xác minh. Cơ quan đăng ký cư trú không yêu cầu công dân nộp để lưu giữ giấy tờ đó.

- Bản quét hoặc bản chụp giấy tờ bằng thiết bị điện tử từ giấy tờ được cấp hợp lệ, còn giá trị sử dụng phải bảo đảm rõ nét, đầy đủ, toàn vẹn về nội dung; đã được hợp pháp hóa lãnh sự, dịch sang tiếng Việt theo quy định nếu là giấy tờ do cơ quan có thẩm quyền nước ngoài cấp trừ trường hợp được miễn hợp pháp hóa lãnh sự.

- Trường hợp thông tin giấy tờ chứng minh điều kiện đăng ký cư trú đã được chia sẻ và khai thác từ cơ sở dữ liệu quốc gia, cơ sở dữ liệu chuyên ngành thì cơ quan đăng ký cư trú không được yêu cầu công dân nộp, xuất trình giấy tờ đó để giải quyết đăng ký cư trú.

b) Số lượng hồ sơ: 01 (một) bộ.

7.4. Thời hạn giải quyết: Thời hạn 02 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ.

7.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến thủ tục xóa đăng ký tạm trú.

7.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

7.7. Kết quả thực hiện thủ tục hành chính:

Trường hợp hồ sơ đầy đủ hợp lệ cơ quan đăng ký cư trú có trách nhiệm xóa đăng ký tạm trú đối với công dân và cập nhật việc xóa đăng ký tạm trú vào Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu về cư trú và thông báo kết quả cho công dân (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

7.8. Phí, lệ phí: Không

7.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

7.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính:

- Trong thời hạn 07 ngày kể từ ngày hộ gia đình có người thuộc diện xóa đăng ký tạm trú thì người thuộc diện xóa đăng ký tạm trú hoặc đại diện hộ gia đình có trách nhiệm nộp hồ sơ làm thủ tục xóa đăng ký tạm trú đến cơ quan đăng ký cư trú.

- Trường hợp cơ quan đăng ký cư trú phát hiện công dân đó thuộc một trong các trường hợp bị xóa đăng ký tạm trú: Trước khi thực hiện việc xóa đăng ký tạm trú, cơ quan đăng ký cư trú thông báo về việc xóa đăng ký tạm trú tới công dân hoặc đại diện hộ gia đình để biết và thực hiện việc nộp hồ sơ làm thủ tục xóa đăng ký tạm trú theo quy định. Trường hợp quá 07 ngày kể từ ngày cơ quan đăng ký cư trú thông báo mà người thuộc diện xóa đăng ký tạm trú hoặc đại diện hộ gia đình không nộp hồ sơ làm thủ tục xóa đăng ký tạm trú thì cơ quan đăng ký cư trú tiến hành lập biên bản về việc công dân, đại diện hộ gia đình không nộp hồ sơ làm thủ tục xóa đăng ký tạm trú và thực hiện xóa đăng ký tạm trú đối với công dân. Cơ quan đăng ký cư trú thông báo bằng văn bản cho công dân đó hoặc chủ hộ về việc xóa đăng ký tạm trú sau khi đã thực hiện.

7.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

8. Thủ tục: Khai báo thông tin về cư trú đối với người chưa đủ điều kiện đăng ký thường trú, đăng ký tạm trú (số hồ sơ TTHC 1.010040)

8.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã

- Bước 3: Khi tiếp nhận hồ sơ khai báo thông tin về cư trú đối với người chưa đủ điều kiện đăng ký thường trú, đăng ký tạm trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

8.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

8.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA);

- Giấy tờ, tài liệu khác (nếu có).

b) Số lượng hồ sơ: 01 (một) bộ.

8.4. Thời hạn giải quyết:

- Đối với trường hợp công dân đã có thông tin trong Cơ sở dữ liệu quốc gia về dân cư thì trong thời hạn 05 ngày làm việc kể từ ngày tiếp nhận thông tin khai báo cơ quan đăng ký cư trú phải tiến hành xác minh thông tin.

- Đối với trường hợp công dân chưa có thông tin trong Cơ sở dữ liệu quốc gia về dân cư thì trong thời hạn 30 ngày kể từ ngày tiếp nhận thông tin cơ quan đăng ký cư trú phải tiến hành xác minh thông tin, phức tạp có thể kéo dài nhưng không quá 60 ngày.

Sau khi kiểm tra, xác minh, cơ quan đăng ký cư trú cập nhật thông tin của công dân về nơi ở hiện tại và các thông tin khác vào Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu về cư trú và thông báo cho người đã khai báo về việc đã cập nhật thông tin, cấp xác nhận thông tin về cư trú cho công dân.

8.5. Đối tượng thực hiện thủ tục hành chính: Người chưa đủ điều kiện đăng ký thường trú, đăng ký tạm trú theo quy định tại Điều 19 Luật Cư trú.

8.6. Cơ quan thực hiện thủ tục hành chính: Cơ quan công an cấp xã.

8.7. Kết quả thực hiện thủ tục hành chính:

Đối với trường hợp đủ điều kiện: Cập nhật thông tin của công dân về nơi ở hiện tại và các thông tin khác vào Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu về cư trú và thông báo cho người đã khai báo về việc đã cập nhật thông tin (mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA) và cấp Xác nhận thông tin về cư trú (mẫu CT07 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

8.8. Phí, lệ phí: không thu lệ phí.

8.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

8.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: Không.

8.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

9. Thủ tục: Thông báo lưu trú (số hồ sơ TTHC 2.001159)

9.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức thông báo lưu trú tới cơ quan đăng ký cư trú.

- Bước 2: Cán bộ công an thực hiện tiếp nhận thông báo lưu trú.

9.2. Cách thức thực hiện:

- Trực tiếp tại cơ quan đăng ký cư trú hoặc địa điểm tiếp nhận thông báo lưu trú do cơ quan đăng ký cư trú quy định;

- Thông qua số điện thoại hoặc hộp thư điện tử do cơ quan đăng ký cư trú thông báo hoặc niêm yết;

- Thông qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác;

- Thông qua ứng dụng trên thiết bị điện tử.

9.3. Thành phần, số lượng hồ sơ: không

Khi có người đến lưu trú, đại diện hộ gia đình, cơ sở khám bệnh, chữa bệnh, cơ sở lưu trú du lịch, cơ sở lưu trú ở khu công nghiệp, cơ sở khác có chức năng lưu trú thì phải thực hiện việc thông báo lưu trú cho người đang lưu trú theo một trong các hình thức đã được quy định tại và theo quy định sau đây:

- Chủ hộ hoặc thành viên hộ gia đình, đại diện cơ sở lưu trú ở khu công nghiệp, cơ sở lưu trú du lịch đề nghị người đến lưu trú xuất trình một trong các giấy tờ pháp lý thể hiện thông tin về số định danh cá nhân theo quy định của pháp luật và thực hiện việc thông báo lưu trú với cơ quan đăng ký cư trú;

- Đại diện cơ sở khám bệnh, chữa bệnh có trách nhiệm lập danh sách người đến điều trị nội trú và thực hiện thông báo lưu trú với cơ quan đăng ký cư trú nơi đặt trụ sở cơ sở khám chữa bệnh

9.4. Thời hạn giải quyết: tiếp nhận ngay khi công dân thông báo lưu trú.

9.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, cá nhân, tổ chức có liên quan đến thông báo lưu trú.

9.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

9.7. Kết quả thực hiện thủ tục hành chính: Cập nhật thông tin vào Cơ sở dữ liệu về cư trú.

9.8. Phí, lệ phí: Không.

9.9. Tên mẫu đơn, mẫu tờ khai: Không

9.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính:

Việc thông báo lưu trú được thực hiện trước 23 giờ của ngày bắt đầu lưu trú; trường hợp người đến lưu trú sau 23 giờ thì việc thông báo lưu trú được thực hiện trước 08 giờ ngày hôm sau; trường hợp ông, bà, cha, mẹ, vợ, chồng, con, cháu, anh, chị, em ruột đến lưu trú nhiều lần thì chỉ cần thông báo lưu trú một lần.

9.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

10. Thủ tục: Khai báo tạm vắng (số hồ sơ TTHC 1.003677)

10.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ khai báo tạm vắng trong Cơ sở dữ liệu về cư trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

10.2. Cách thức thực hiện:

- Trường hợp công dân thuộc quy định tại điểm a, điểm b khoản 1 Điều 31 Luật Cư trú nộp hồ sơ trực tiếp tại cơ quan đăng ký cư trú.

- Trường hợp thuộc quy định tại điểm c, điểm d khoản 1 Điều 31 Luật Cư trú thì khai báo tạm vắng qua các hình thức:

+ Trực tiếp tại cơ quan đăng ký cư trú hoặc tại địa điểm tiếp nhận khai báo tạm vắng do cơ quan đăng ký cư trú quy định;

+ Số điện thoại hoặc hộp thư điện tử do cơ quan đăng ký cư trú thông báo hoặc niêm yết;

+ Thông qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác;

+ Ứng dụng trên thiết bị điện tử.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

10.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

- Trường hợp công dân thuộc quy định tại điểm a, điểm b khoản 1 Điều 31 Luật Cư trú, hồ sơ gồm:

+ Đề nghị khai báo tạm vắng;

+ Văn bản đồng ý của cơ quan có thẩm quyền giám sát, quản lý, giáo dục người đó.

- Trường hợp thuộc quy định tại điểm c, điểm d khoản 1 Điều 31 Luật Cư trú, nội dung khai báo tạm vắng gồm: họ và tên, số định danh cá nhân hoặc số Chứng minh nhân dân, số hộ chiếu của người khai báo tạm vắng; lý do tạm vắng; thời gian tạm vắng; địa chỉ nơi đến.

b) Số lượng hồ sơ: 01 (một) bộ.

10.4. Thời hạn giải quyết: Trong thời gian 01 ngày kể từ khi tiếp nhận đề nghị khai báo tạm vắng của công dân; trường hợp phức tạp thì có thể kéo dài hơn nhưng không quá 02 ngày làm việc.

10.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến khai báo tạm vắng.

10.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

10.7. Kết quả thực hiện thủ tục hành chính: Trường hợp hồ sơ đầy đủ, hợp lệ cơ quan đăng ký cư trú có trách nhiệm cập nhật thông tin khai báo tạm vắng của công dân vào Cơ sở dữ liệu về cư trú và thông báo kết quả và cấp Phiếu khai báo tạm vắng cho công dân (Mẫu CT03 và CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

10.8. Phí, lệ phí: Không.

10.9. Tên mẫu đơn, mẫu tờ khai: Không

10.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính:

- Trường hợp người quy định tại điểm d khoản 1 Điều 31 Luật Cư trú  là người chưa thành niên thì người thực hiện khai báo là cha, mẹ hoặc người giám hộ.

- Nội dung khai báo tạm vắng bao gồm họ và tên, số định danh cá nhân hoặc số Chứng minh nhân dân, số hộ chiếu của người khai báo tạm vắng; lý do tạm vắng; thời gian tạm vắng; địa chỉ nơi đến.

10.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú;

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

11. Thủ tục: Xác nhận thông tin về cư trú (số hồ sơ TTHC 1.010041)

11.1. Trình tự thực hiện:

- Bước 1: Cá nhân, tổ chức chuẩn bị hồ sơ theo quy định của pháp luật.

- Bước 2: Cá nhân, tổ chức nộp hồ sơ tại Công an cấp xã.

- Bước 3: Khi tiếp nhận hồ sơ xác nhận thông tin về cư trú, cơ quan đăng ký cư trú kiểm tra tính pháp lý và nội dung hồ sơ:

+ Trường hợp hồ sơ đã đầy đủ, hợp lệ thì tiếp nhận hồ sơ và cấp Phiếu tiếp nhận hồ sơ và hẹn trả kết quả (mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ đủ điều kiện nhưng chưa đủ hồ sơ thì hướng dẫn bổ sung, hoàn thiện và cấp Phiếu hướng dẫn bổ sung, hoàn thiện hồ sơ (mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký;

+ Trường hợp hồ sơ không đủ điều kiện thì từ chối và cấp Phiếu từ chối tiếp nhận, giải quyết hồ sơ (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA) cho người đăng ký.

- Bước 4: Căn cứ theo ngày hẹn trên Phiếu tiếp nhận hồ sơ và hẹn trả kết quả để nhận thông báo kết quả giải quyết thủ tục đăng ký cư trú (nếu có).

11.2. Cách thức thực hiện:

- Nộp hồ sơ trực tiếp tại Công an cấp xã nơi thuận lợi, phù hợp không phụ thuộc vào nơi cư trú của công dân.

- Nộp hồ sơ trực tuyến qua các cổng cung cấp dịch vụ công trực tuyến như: Trực tuyến qua Cổng dịch vụ công quốc gia, Cổng dịch vụ công Bộ Công an, ứng dụng VNeID hoặc dịch vụ công trực tuyến khác theo quy định của pháp luật.

Thời gian tiếp nhận hồ sơ: Giờ hành chính các ngày làm việc từ thứ 2 đến thứ 6 và sáng thứ 7 hàng tuần (trừ các ngày nghỉ lễ, tết theo quy định của
pháp luật).

11.3. Thành phần, số lượng hồ sơ:

a) Thành phần hồ sơ:

Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

*Lưu ý: Trường hợp thực hiện đăng ký cư trú trực tuyến, người yêu cầu đăng ký cư trú khai báo thông tin theo biểu mẫu điện tử được cung cấp sẵn.

b) Số lượng hồ sơ: 01 (một) bộ

11.4. Thời hạn giải quyết: Kể từ ngày nhận được hồ sơ hợp lệ, cơ quan đăng ký cư trú có trách nhiệm cấp xác nhận thông tin về cư trú cho công dân trong thời hạn không quá 1/2 ngày làm việc với trường hợp thông tin có trong Cơ sở dữ liệu quốc gia về dân cư và trong thời hạn 03 ngày làm việc với trường hợp thông tin không có trong Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu về cư trú cần xác minh; trường hợp từ chối giải quyết xác nhận thông tin về cư trú thì phải trả lời bằng văn bản và nêu rõ lý do.

11.5. Đối tượng thực hiện thủ tục hành chính: Cơ quan, tổ chức, cá nhân có liên quan đến xác nhận thông tin về cư trú.

11.6. Cơ quan thực hiện thủ tục hành chính: Công an cấp xã.

11.7. Kết quả thực hiện thủ tục hành chính:

- Trường hợp hồ sơ hợp lệ, đủ điều kiện cơ quan đăng ký cư trú cấp xác nhận thông tin về cư trú (mẫu CT07 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

- Trường hợp từ chối giải quyết xác nhận thông tin về cư trú thì phải có văn bản trả lời và nêu rõ lý do (mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

11.8. Phí, lệ phí: không thu lệ phí.

11.9. Tên mẫu đơn, mẫu tờ khai: Tờ khai thay đổi thông tin cư trú (Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA).

11.10. Yêu cầu, điều kiện thực hiện thủ tục hành chính: không

11.11. Căn cứ pháp lý của thủ tục hành chính:

- Luật Cư trú số 68/2020/QH14 ngày 13/11/2020;

- Nghị định số 62/2021/NĐ-CP ngày 29/6/2021 của Chính phủ quy định chi tiết một số điều của Luật Cư trú.

- Thông tư số 55/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú.

- Thông tư số 56/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú;

- Thông tư số 57/2021/TT-BCA ngày 15/5/2021 của Bộ Công an quy định quy trình đăng ký cư trú.

- Thông tư số 66/2023/TT-BCA ngày 17/11/2023 của Bộ Công an sửa đổi, bổ sung một số điều của Thông tư số 55/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định chi tiết một số điều và biện pháp thi hành Luật Cư trú; Thông tư số 56/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về biểu mẫu trong đăng ký, quản lý cư trú; Thông tư số 57/2021/TT-BCA ngày 15 tháng 5 năm 2021 của Bộ trưởng Bộ Công an quy định về quy trình đăng ký cư trú.

 
PHẦN THỨ BA: CÁC BIỂU MẪU LÀ THÀNH PHẦN HỒ SƠ THỰC HIỆN THỦ TỤC HÀNH CHÍNH TRONG LĨNH VỰC ĐĂNG KÝ CƯ TRÚ

THUỘC THẨM QUYỀN GIẢI QUYẾT CỦA BỘ CÔNG AN

Mẫu CT01 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc

TỜ KHAI THAY ĐỔI THÔNG TIN CƯ TRÚ

Kính gửi(1):......................................................................................................

1. Họ, chữ đệm và tên:....................................................................................................................

2. Ngày, tháng, năm sinh:................./................../ .............................       3. Giới tính:......................

4. Số định danh cá nhân:

5. Số điện thoại liên hệ:...................................... .............6. Email:..........................................

7. Họ, chữ đệm và tên chủ hộ:................................. 8. Mối quan hệ với chủ hộ:..................

9. Số định danh cá nhân của chủ hộ:

10. Nội dung đề nghị(2):..................................................................................................................................................

.........................................................................................................................................................................................................

11. Những thành viên trong hộ gia đình cùng thay đổi:

TT

Họ, chữ đệm

và tên

Ngày, tháng, năm sinh

Giới tính

Số định danh

cá nhân

Mối quan hệ

với chủ hộ

.....,ngày.......tháng....năm.......

Ý KIẾN CỦA CHỦ HỘ(3)

.....,ngày.....tháng....năm...

Ý KIẾN CỦA CHỦ SỞ HỮU CHỖ Ở HỢP PHÁP(4)


(7) Họ và tên: ..................

(7) Số định danh cá nhân:................

.....,ngày......tháng...năm...

Ý KIẾN CỦA CHA, MẸ

HOẶC NGƯỜI GIÁM HỘ(5)

(7) Họ và tên: ..................

(7) Số định danh cá nhân:...............

.....,ngày....tháng...năm...

NGƯỜI KÊ KHAI(6)

Chú thích:

(1) Cơ quan đăng ký cư trú.

(2) Ghi rõ ràng, cụ thể nội dung đề nghị. Ví dụ: đăng ký thường trú; đăng ký tạm trú; tách hộ; xác nhận thông tin về cư trú...

(3) Áp dụng đối với các trường hợp quy định tại khoản 2, khoản 3, khoản 5, khoản 6 Điều 20; khoản 1 Điều 25; điểm a khoản 1 Điều 26 Luật Cư trú. Việc lấy ý kiến của chủ hộ được thực hiện theo các phương thức sau:

a) Chủ hộ ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Chủ hộ xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Chủ hộ có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

 (4) Áp dụng đối với các trường hợp quy định tại khoản 2, khoản 3, khoản 4, khoản 5, khoản 6 Điều 20; khoản 1 Điều 25 Luật Cư trú; điểm a khoản 1 Điều 26 Luật Cư trú. Việc lấy ý kiến của chủ sở hữu chỗ ở hợp pháp được thực hiện theo các phương thức sau:

a) Chủ sở hữu chỗ ở hợp pháp ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Chủ sở hữu chỗ ở hợp pháp xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Chủ sở hữu chỗ ở hợp pháp có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

Ghi chú: Trường hợp chủ sở hữu hợp chỗ ở hợp pháp gồm nhiều cá nhân, tổ chức thì phải có ý kiến đồng ý của tất cả các đồng sở hữu trừ trường hợp đã có thỏa thuận về việc cử đại diện có ý kiến đồng ý; Trường hợp chủ sở hữu chỗ ở hợp pháp xác nhận nội dung đồng ý thông qua ứng dụng VNeID thì công dân phải kê khai thông tin về họ, chữ đệm, tên và số ĐDCN của chủ sở hữu chỗ ở hợp pháp.

(5) Áp dụng đối với trường hợp người chưa thành niên, người hạn chế hành vi dân sự, người không đủ năng lực hành vi dân sự có thay đổi thông tin về cư trú. Việc lấy ý kiến của cha, mẹ hoặc người giám hộ được thực hiện theo các phương thức sau:

a) Cha, mẹ hoặc người giám hộ ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Cha, mẹ hoặc người giám hộ xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Cha, mẹ hoặc người giám hộ có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

(6) Trường hợp nộp trực tiếp người kê khai ký, ghi rõ họ, chữ đệm và tên vào Tờ khai. Trường hợp nộp qua cổng dịch vụ công hoặc ứng dụng VNeID thì người kê khai không phải ký vào mục này.

(7) Chỉ kê khai thông tin khi công dân đề nghị xác nhận nội dung đồng ý thông qua ứng dụng VNeID.

Mẫu CT02 ban hành kèm theo Thông tư số 66/2023/TT-BCA

ngày 17/11/2023 của Bộ trưởng Bộ Công an

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM


Ảnh 4x6

Độc lập – Tự do – Hạnh phúc

TỜ KHAI THAY ĐỔI THÔNG TIN CƯ TRÚ

(Dùng cho công dân Việt Nam định cư ở nước ngoài

không có hộ chiếu Việt Nam còn giá trị sử dụng)

Kính gửi (1):............................................................................................

1. Họ, chữ đệm và tên Việt Nam:.............................................................................................

2. Họ, chữ đệm và tên trong hộ chiếu/giấy tờ do nước ngoài cấp:......................................

......................................................................................................................................................

3. Ngày, tháng, năm sinh:................./................../ .............................     4. Giới tính:.............

5. Dân tộc:...............................................................................................     6. Tôn giáo:.............

7. Số định danh cá nhân/CMND:

8. Số điện thoại (nếu có):....................... 9. E-mail (nếu có):................................................

10. Quốc tịch nước ngoài (nếu có):.........................................................................................

11. Số hộ chiếu/ Giấy tờ đi lại quốc tế do nước ngoài cấp/ Giấy tờ do cơ quan có thẩm quyền Việt Nam cấp:

Số:.......................................................................... ...... Ngày cấp: ............./............/................

Cơ quan cấp:............................................ Có giá trị đến ngày:................./......../..................

12. Nghề nghiệp, nơi làm việc ở nước ngoài trước khi nhập cảnh Việt Nam:...................

......................................................................................................................................................

13. Tóm tắt quá trình sinh sống và làm việc từ khi sinh ra đến nay:

Từ tháng, năm

đến tháng, năm

Chỗ ở

(Ghi rõ ràng, cụ thể địa chỉ chỗ ở)

Nghề nghiệp,

nơi làm việc

14. Họ, chữ đệm và tên, năm sinh, quốc tịch, nghề nghiệp, nơi làm việc, chỗ ở hiện nay của cha, mẹ, vợ, chồng, con:

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

15. Nơi cư trú ở nước ngoài trước khi nhập cảnh Việt Nam:...............................................

......................................................................................................................................................

16. Nơi ở hiện tại ở Việt Nam:..................................................................................................

......................................................................................................................................................

17. Nội dung đề nghị (2):............................................................................................................

......................................................................................................................................................

18. Họ và tên chủ hộ:......................................................19. Quan hệ với chủ hộ:..............

20. Số định danh cá nhân/ CMND của chủ hộ:


Ảnh 4x6

của trẻ em

đi cùng

Tôi xin cam đoan những nội dung khai trên đây là đúng sự thật và chịu hoàn toàn trách nhiệm trước pháp luật về nội dung cam đoan của mình./.

.....,ngày.......tháng....năm.....

Ý KIẾN CỦA CHỦ HỘ (3)

(Ghi rõ nội dung và ký,

ghi rõ họ tên)

.....,ngày.....tháng....năm...

Ý KIẾN CỦA CHỦ SỞ HỮU HOẶC NGƯỜI ĐẠI DIỆN CHỖ Ở HỢP PHÁP (4)

(Ký, ghi rõ họ tên)

.....,ngày......tháng...năm...

Ý KIẾN CỦA CHA, MẸ

HOẶC NGƯỜI GIÁM HỘ (5)

(Ký, ghi rõ họ tên)

..,ngày....tháng...năm...

NGƯỜI ĐỀ NGHỊ (6)

(Ký, ghi rõ họ tên)

                                 (7) Họ và tên: ..................                                                         (7) Họ và tên: ..................        

                                                                    (7) Số định danh cá nhân:................                                         (7) Số định danh cá nhân:................

Chú thích:

(1) Cơ quan đăng ký cư trú.

(2) Ghi rõ ràng, cụ thể nội dung đề nghị.

(3) Áp dụng đối với các trường hợp quy định tại khoản 2, khoản 3, khoản 5, khoản 6 Điều 20; khoản 1 Điều 25; điểm a khoản 1 Điều 26 Luật Cư trú. Việc lấy ý kiến của chủ hộ được thực hiện theo các phương thức sau:

a) Chủ hộ ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Chủ hộ xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Chủ hộ có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

 (4) Áp dụng đối với các trường hợp quy định tại khoản 2, khoản 3, khoản 4, khoản 5, khoản 6 Điều 20; khoản 1 Điều 25 Luật Cư trú; điểm a khoản 1 Điều 26 Luật Cư trú. Việc lấy ý kiến của chủ sở hữu chỗ ở hợp pháp được thực hiện theo các phương thức sau:

a) Chủ sở hữu chỗ ở hợp pháp ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Chủ sở hữu chỗ ở hợp pháp xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Chủ sở hữu chỗ ở hợp pháp có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

Ghi chú: Trường hợp chủ sở hữu hợp chỗ ở hợp pháp gồm nhiều cá nhân, tổ chức thì phải có ý kiến đồng ý của tất cả các đồng sở hữu trừ trường hợp đã có thỏa thuận về việc cử đại diện có ý kiến đồng ý; Trường hợp chủ sở hữu chỗ ở hợp pháp xác nhận nội dung đồng ý thông qua ứng dụng VNeID thì công dân phải kê khai thông tin về họ, chữ đệm, tên và số ĐDCN của chủ sở hữu chỗ ở hợp pháp.

(5) Áp dụng đối với trường hợp người chưa thành niên, người hạn chế hành vi dân sự, người không đủ năng lực hành vi dân sự có thay đổi thông tin về cư trú. Việc lấy ý kiến của cha, mẹ hoặc người giám hộ được thực hiện theo các phương thức sau:

a) Cha, mẹ hoặc người giám hộ ghi rõ nội dung đồng ý và ký, ghi rõ họ tên vào Tờ khai.

b) Cha, mẹ hoặc người giám hộ xác nhận nội dung đồng ý thông qua ứng dụng VNeID hoặc các dịch vụ công trực tuyến khác.

c) Cha, mẹ hoặc người giám hộ có văn bản riêng ghi rõ nội dung đồng ý (văn bản này không phải công chứng, chứng thực).

(6) Trường hợp nộp trực tiếp người kê khai ký, ghi rõ họ, chữ đệm và tên vào Tờ khai. Trường hợp nộp qua cổng dịch vụ công hoặc ứng dụng VNeID thì người kê khai không phải ký vào mục này.

(7) Chỉ kê khai thông tin khi công dân đề nghị xác nhận nội dung đồng ý thông qua ứng dụng VNeID.

Mẫu CT03 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

...............................................(1)

................................................(2)

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc



PHIẾU KHAI BÁO TẠM VẮNG

1. Họ, chữ đệm và tên:.................................................................................................................

2. Ngày, tháng, năm sinh:............/ .........../................3. Giới tính: ............................................

4. Số định danh cá nhân/CMND:

5. Nơi thường trú: ........................................................................................................................

.........................................................................................................................................................

6. Nơi tạm trú: ..............................................................................................................................

.........................................................................................................................................................

7. Nơi ở hiện tại: .......................................................................................................................

.........................................................................................................................................................

8. Tạm vắng từ ngày, tháng, năm:......./............../ ............. đến ngày......../.........../ .................

9. Lý do tạm vắng: .......................................................................................................................

.........................................................................................................................................................

10. Địa chỉ nơi đến (3):..................................................................................................................

..................................................................................................................................................................................................................................................................................................................

.............ngày ........tháng........năm........ ........

NGƯỜI KHAI BÁO

(Ký, ghi rõ họ tên)

 

................ngày ........tháng........năm........ NGƯỜI TIẾP NHẬN KHAI BÁO

(Ký, ghi rõ họ tên)

XÁC NHẬN CỦA CƠ QUAN ĐĂNG KÝ CƯ TRÚ

.................ngày ........tháng........năm……….

THỦ TRƯỞNG CƠ QUAN

(Ký, ghi rõ họ tên và đóng dấu)

(Chữ ký số của Thủ trưởng cơ quan)

 	 	 	 
Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú

(2) Cơ quan đăng ký cư trú

(3) Ghi rõ số nhà, đường phố, tổ dân phố, thôn, xóm, làng, ấp, bản, buôn, phum, sóc; xã/phường/thị trấn; quận/huyện/thị xã/thành phố thuộc tỉnh/thành phố thuộc thành phố trực thuộc Trung ương; tỉnh/thành phố trực thuộc Trung ương.

 
Mẫu CT04 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

...................................(1)

...................................(2)



 
Số:          /PTN

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc

PHIẾU TIẾP NHẬN HỒ SƠ VÀ HẸN TRẢ KẾT QUẢ

Mã hồ sơ:......................

Công an(2):...................................................................................................................................

đã tiếp nhận hồ sơ của Ông/Bà: ..............................................................................................

Số định danh cá nhân/CMND:

Nơi thường trú: ..........................................................................................................................

......................................................................................................................................................

Nơi tạm trú: ................................................................................................................................

......................................................................................................................................................

Nơi ở hiện tại: ............................................................................................................................

......................................................................................................................................................

Số điện thoại:................................................................... Email:..............................................

Nội dung yêu cầu giải quyết: ...................................................................................................

......................................................................................................................................................

Thành phần hồ sơ nộp gồm:

TT

Tên giấy tờ

Hình thức

(bản chính, bản sao hoặc bản chụp)

Ghi chú

Thời gian nhận hồ sơ: ............giờ............phút, ngày................./.............../.............................

Thời gian trả kết quả giải quyết hồ sơ: ............giờ............phút, ngày......../........../............

Hình thức nhận kết quả: Bản giấy o            Bản điện tử o         Tin nhắn SMS o

(Công dân nhận kết quả bản điện tử qua email, thông báo trên ứng dụng VNeID và cổng dịch vụ công; thông báo qua tin nhắn SMS tới số điện thoại đã khai báo)

Đăng ký nhận kết quả Bản giấy tại:.........................................................................................

......................................................................................................................................................

..........., ngày............tháng...........năm...........

CÁN BỘ TIẾP NHẬN(3)

Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú.

(2) Cơ quan đăng ký cư trú.

(3) Cán bộ tiếp nhận có thể ký ghi rõ họ tên hoặc ký số hoặc xác nhận bằng hình thức xác thực khác.

 
Mẫu CT05 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

....................................(1)

....................................(2)

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc

PHIẾU HƯỚNG DẪN BỔ SUNG, HOÀN THIỆN HỒ SƠ

Mã hồ sơ:.....................................................................................................................................

Của Ông/Bà:................................................................................................................................

Số định danh cá nhân/CMND:

Căn cứ quy định của Luật Cư trú và các văn bản quy định chi tiết, hướng dẫn thi hành có liên quan, đề nghị Ông/Bà hoàn thiện hồ sơ như sau(3):

......................................................................................................................................................

......................................................................................................................................................     

......................................................................................................................................................     

......................................................................................................................................................     

......................................................................................................................................................          

Lý do:...........................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

Trong quá trình hoàn thiện hồ sơ nếu có vấn đề vướng mắc, Ông/Bà liên hệ với Công an... ; Số ĐT............................... để được hướng dẫn./.

......., ngày........ tháng....... năm..........

CÁN BỘ TIẾP NHẬN(4)

Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú

(2) Cơ quan đăng ký cư trú

(3) Ghi hướng dẫn đầy đủ, cụ thể một lần về việc kê khai, bổ sung, chỉnh lý thành phần hồ sơ; ví dụ: Bổ sung giấy tờ, tài liệu chứng minh chỗ ở hợp pháp (Hợp đồng thuê nhà....); bổ sung giấy tờ, chứng minh quan hệ nhân thân (giấy khai sinh...); Kê khai lại Mục gì trong biểu mẫu, kê khai như thế nào...

(4) Cán bộ tiếp nhận ký ghi rõ họ tên hoặc ký số hoặc xác nhận bằng hình thức xác thực khác.

 
Mẫu CT06 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

....................................(1)

....................................(2)

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc

PHIẾU TỪ CHỐI TIẾP NHẬN, GIẢI QUYẾT HỒ SƠ

Công an(2):............................................................................................................................

đã tiếp nhận hồ sơ của Ông/Bà: ..............................................................................................

Số định danh cá nhân/CMND:

Mã hồ sơ:..............................................................................................................................

Căn cứ quy định của Luật Cư trú và các văn bản quy định chi tiết, hướng dẫn thi hành có liên quan, Công an(2)................................................................................................................................................. thông báo không tiếp nhận, giải quyết hồ sơ này với lý do cụ thể như sau(3):

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

Trân trọng thông báo đến Ông/Bà được biết./.

                             ............., ngày.............tháng............năm..........

THỦ TRƯỞNG CƠ QUAN ĐĂNG KÝ CƯ TRÚ (4)

Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú

(2) Cơ quan đăng ký cư trú

(3) Ghi rõ ràng, cụ thể lý do không tiếp nhận, giải quyết hồ sơ của công dân và viện dẫn cụ thể quy định của văn bản quy phạm pháp luật được áp dụng; ví dụ: Không bảo đảm điều kiện về diện tích nhà ở tối thiểu để đăng ký thường trú theo quy định tại điểm b khoản 3 Điều 20 Luật Cư trú; Giấy tờ, tài liệu chứng minh chỗ ở hợp pháp không đúng quy định tại điểm ....

(4) Thủ trưởng cơ quan đăng ký cư trú ký ghi rõ họ tên hoặc ký số hoặc xác nhận bằng hình thức xác thực khác.

Mẫu CT07 ban hành kèm theo Thông tư số 66/2023/TT-BCA

 ngày 17/11/2023 của Bộ trưởng Bộ Công an

....................................(1)

....................................(2)



 
Số:             /XN

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc



 
.........., ngày....tháng....năm.........

XÁC NHẬN THÔNG TIN VỀ CƯ TRÚ

Theo đề nghị của Ông/Bà: ......................................................................................................

Số định danh cá nhân:

CÔNG AN (2)                XÁC NHẬN:

I. Họ, chữ đệm và tên của Ông/Bà:.......................................................................................

1. Ngày, tháng, năm sinh:....../…..../...........       2. Giới tính:..................................................

3. Số định danh cá nhân:

4. Dân tộc: ............................. .............................       5. Tôn giáo:...........................................

6. Quê quán:................................................................................................................................

7. Nơi đăng ký khai sinh:..........................................................................................................

8. Nơi thường trú:.......................................................................................................................

......................................................................................................................................................

9. Nơi tạm trú:.............................................................................................................................

......................................................................................................................................................

10. Nơi ở hiện tại:.......................................................................................................................

......................................................................................................................................................

11. Họ, chữ đệm và tên chủ hộ:....................................... 12. Quan hệ với chủ hộ:..............

13. Số định danh cá nhân chủ hộ:

II. Thông tin các thành viên khác trong hộ gia đình:

TT

Họ, chữ đệm

và tên

Ngày, tháng, năm sinh

Giới tính

Số định danh

cá nhân

Quan hệ với chủ hộ

III. Nội dung xác nhận khác (các nơi cư trú trước đây, thời gian sinh sống tại từng nơi cư trú, hình thức đăng ký cư trú và các thông tin về cư trú khác có trong Cơ sở dữ liệu về cư trú, Cơ sở dữ liệu quốc gia về dân cư...):

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

Giấy này có giá trị sử dụng đến hết ngày............tháng........năm...............

THỦ TRƯỞNG CƠ QUAN ĐĂNG KÝ CƯ TRÚ(3)

Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú.

(2) Cơ quan đăng ký cư trú trong cả nước không phụ thuộc vào nơi cư trú của công dân.

(3) Thủ trưởng cơ quan đăng ký cư trú ký ghi rõ họ tên hoặc ký số hoặc xác nhận bằng hình thức xác thực khác.

Mẫu CT08 ban hành kèm theo Thông tư số 66/2023/TT-BCA

ngày 17/11/2023 của Bộ trưởng Bộ Công an

..........................................(1)

.......................................... (2)

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập – Tự do – Hạnh phúc

 

Số:               /TB

.........., ngày.......tháng....năm......

THÔNG BÁO

Về việc ………………………………………………….(3)

Kính gửi Ông/Bà:.....................................................................................................

Công an(2)................................................................................ thông báo đến Ông/Bà:

1. Họ, chữ đệm và tên:...............................................................................................................

2. Ngày, tháng, năm sinh:............../.........../ .....................       3.  Giới tính:................................

4. Số định danh cá nhân/CMND:

5. Nội dung thông báo: .............................................................................................................     

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

......................................................................................................................................................

Công an(2).............................................thông báo cho Ông/Bà biết./.

THỦ TRƯỞNG CƠ QUAN

Chú thích:

(1) Cơ quan cấp trên của cơ quan đăng ký cư trú.

(2) Cơ quan đăng ký cư trú.

(3) Kết quả giải quyết thủ tục về cư trú, hủy bỏ thủ tục về cư trú. Trường hợp hủy bỏ thủ tục về cư trú thì phải gửi kèm Quyết định về việc hủy bỏ thủ tục về cư trú.
"""
prompt_dvccancuoc2 ="""
Nếu bạn đã xác định được yêu cầu của tôi là về Căn cước, hãy đối chiếu với danh sách các dịch vụ công về thẻ căn cước và lý do dưới đây, hãy tìm xem dịch vụ công nào là phù hợp.
* Cấp, quản lý thẻ căn cước --- Cấp lại căn cước do mất: Nếu người dân nói bị mất hay bị rơi thẻ căn cước, lựa chọn luôn dịch vụ công này.
* Cấp, quản lý thẻ căn cước --- Cấp mới thẻ căn cước cho người trên 14 tuổi
* Cấp, quản lý thẻ căn cước --- Cấp mới thẻ căn cước cho người dưới 14 tuổi
* Cấp, quản lý thẻ căn cước --- Đổi Căn cước do bị hư hỏng không sử dụng được: Nếu người dân nói thẻ bị gãy, xước, mờ, lựa chọn dịch vụ công này.
* Cấp, quản lý thẻ căn cước --- Đổi Căn cước do thay đổi thông tin họ tên: Nếu người dân nói thẻ bị sai họ tên, chọn dịch vụ công này.
* Cấp, quản lý thẻ căn cước --- Đổi Căn cước do thay đổi đặc điểm nhận dạng: Nếu người dân nói mặt họ có thay đổi, hoặc mới đi phẫu thuật hoặc thẩm mỹ, chọn dịch vụ công này.
* Cấp, quản lý thẻ căn cước --- Đổi Căn cước do có sai sót thông tin trên Căn cước: Nếu người dân nói thẻ căn cước có thông tin sai ngoại trừ họ tên, lựa chọn dịch vụ công này.
* Cấp, quản lý thẻ căn cước --- Xác nhận số Chứng minh nhân dân, Căn cước công dân: Nếu người dùng muốn xác nhận hoặc xác minh số chứng minh hoặc căn cước thì chọn dịch vụ này.
* Cấp, quản lý thẻ căn cước --- Đổi Căn cước do hết hạn: Nếu người dùng nói thẻ căn cước của mình hết hạn thì chọn dịch vụ công này.
Yêu cầu: 
* Phải tìm ra chính xác tuyệt đối tên dịch vụ công đã đưa ra trong phạm vi ở trên
* Đối với dịch vụ công Cấp, quản lý thẻ căn cước --- Cấp mới thẻ căn cước, cần phải xác định người cần cấp đang ở độ tuổi nào. Hiện có 3 độ tuổi là: Dưới 6 tuổi, Từ 6 đến 14 tuổi, Từ 14 tuổi trở lên.
* Sau khi đã tìm ra dịch vụ công trong phạm vi trên, hãy ghi lại chính xác theo mẫu: "Dịch vụ công phù hợp với bạn là (tên dịch vụ công đã chọn). Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua."
* Nếu mô tả ở trên của tôi vẫn chưa đủ cơ sở để lựa chọn dịch vụ công, phải tiếp tục hỏi tôi để làm rõ vấn đề để chọn được dịch vụ công phù hợp. Tuyệt đối không được đoán bừa, không có cơ sở.
* Sau khi bạn đã tìm ra dịch vụ công, nếu tôi tiếp tục hỏi, vẫn tiếp tục tìm dịch vụ công trong phạm vi trên, vẫn ghi lại chính xác theo mẫu: "Dịch vụ công phù hợp với bạn là (tên dịch vụ công đã chọn). Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua."
- Tôi: Tôi muốn xin cấp lại căn cước
- Trợ lý ảo: Xin hãy cho biết lí do xin cấp lại?
- Tôi: Thẻ của tôi đã hết hạn
- Trợ lý ảo: Dịch vụ công phù hợp với bạn là Cấp, quản lý thẻ căn cước --- Đổi Căn cước do hết hạn. Hãy lựa chọn 'ĐỒNG Ý' để gửi hồ sơ của bạn lên hệ thống, lựa chọn 'HUỶ' để bỏ qua.
"""