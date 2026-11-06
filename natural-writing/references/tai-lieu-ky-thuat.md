# Nhóm 14-25, 27-29: tài liệu kỹ thuật nói chung

Đọc khi viết câu trả lời trong chat, Quick Guide, tài liệu cho dev hoặc khách, và khi đặt tên, đặt nhãn cho trường, bảng, sheet, đầu việc. Bảng từ tự chế và từ thật sự dùng (nhóm 20) nằm ở file này.

## Các nhóm dấu hiệu riêng của tài liệu kỹ thuật

Nhóm này rút ra từ chính các lần bị trả bài trong dự án. Trong tài liệu tư vấn và hướng dẫn kỹ thuật thì đây mới là các lỗi bị bắt nhiều nhất.

### 14. Chôn kết luận xuống dưới

Mở đầu bằng nguồn, bằng bối cảnh, rồi mới tới câu trả lời. Đây là lỗi thứ tự thông tin, không phải lỗi từ ngữ, nên rà từ vựng không phát hiện ra.

- Sai: mở bằng mục "Nguồn code", rồi bảng số, rồi mới tới kết luận.
- Đúng: câu đầu tiên nói thẳng "Code không có bước dồn phần lẻ vào một dòng. Nó tính lần lượt từng dòng theo Line No., dòng cuối nhận nguyên phần còn lại." Dẫn chứng xuống sau.

Quy tắc: câu đầu tiên phải là câu trả lời. Nếu người đọc chỉ đọc một câu rồi bỏ, câu đó phải đủ.

### 15. Trả lời dài khi câu hỏi hẹp

Được hỏi một câu có đáp án ngắn, trả về một báo cáo bốn mục. Câu hỏi "Created By trên BC bây giờ là user nào" cần một bảng hai dòng, không cần phần phương án, phần đã làm, phần giới hạn.

Cách chữa: trả lời đúng câu được hỏi trước. Phần bối cảnh chỉ thêm khi nó đổi câu trả lời, và luôn đứng sau.

### 16. Dịch tên định danh kỹ thuật thành chữ của mình

Đây là lỗi nặng nhất trong nhóm này vì nó phá khả năng truy nguồn.

| Viết sai | Viết đúng |
|---|---|
| Round(..., 1 đồng) | `Currency."Amount Rounding Precision"` |
| tăng trường version | sửa số ở dòng `version` lên cao hơn số đang cài |
| page hộp duyệt | page phiếu chờ duyệt (`approvalInbox`) |
| Trường lệnh actionCode | `actionCode` |
| Trường trạng thái nút | các trường `canXxx` |
| Trình kết nối ánh xạ entity set thế nào | mỗi entity set là một nguồn dữ liệu riêng |

Trường hợp "1 đồng" cho thấy hậu quả: viết tắt tham số thành cách nói dân dã làm người đọc tưởng dòng đầu tiên không áp tham số đó, trong khi code áp cho cả ba dòng.

Quy tắc: tên field, page, tham số, biến trong code thì giữ nguyên tên thật, đặt trong code format. Cần cách gọi tiếng Việt thì đặt tên mô tả rồi để tên thật trong ngoặc ngay sau, không thay hẳn tên thật.

Tên bảng cũng là tên định danh. Bị bắt ở file data migration master data khách C, 02/10/2026: tên sheet đặt thành "A01 Đơn vị tính", "B08 Mặt hàng", PM yêu cầu đổi lại "204 Unit of Measure", "27 Item". Consultant tra bảng bằng số bảng và tên bảng trên Business Central, khi nạp cũng ghép sheet với bảng theo đúng hai thứ đó. Mã A01, B08 là mã tự đặt, không ai tra được.

| Viết sai | Viết đúng |
|---|---|
| tên sheet A01 Đơn vị tính | 204 Unit of Measure |
| tên sheet D04 Tham số mặt hàng | 27 Item (Replenishment) |

Tên tiếng Việt vẫn có, nhưng nằm ở dòng tiêu đề trong sheet và ở danh mục sheet, không thay tên sheet. Sheet name tối đa 31 ký tự và không chứa dấu `/`, nên tên bảng dài thì rút gọn theo kiểu BC hay viết tắt ("Item Vendor Dest. Loc.", "9 Country Region"), không dịch.

### 17. Ẩn dụ văn chương làm tiêu đề mục

Tiêu đề mượn hình ảnh nghe kêu nhưng người đọc không biết mục đó nói gì.

- "Giải phẫu một API page" thành "Đọc một API page: từng thuộc tính làm gì"
- "Hợp đồng của Custom API" thành "Custom API nhận gì, trả gì"

Cùng loại: "bức tranh toàn cảnh", "trái tim của hệ thống", "xương sống", "hành trình dữ liệu", "dưới nắp capo", "bản đồ tài liệu", "lớp nền", "cụm".

Ẩn dụ trong thân bài cũng vậy, và đây là chỗ hay sót vì nó nằm lẫn giữa câu:

- "Đối tượng ngoài cụm phải sửa phẫu thuật" thành "Hai mươi đối tượng ngoài cụm MobileWMS phải sửa trong file"
- "khóa được phạm vi" thành "chốt được phạm vi"
- "Nội dung tích hợp gói gọn ở sáu thông tin" thành "Dữ liệu trao đổi gồm sáu thông tin"
- "Lớp nền cho mọi interface" thành "Phần nền tảng dùng chung cho các interface"
- "Kiểm thử đơn vị cụm pallet và chất lượng" thành "Kiểm thử đơn vị phần pallet và kiểm tra chất lượng"
- "Bản đồ chuyển dữ liệu, quy tắc đối chiếu" thành "Bảng ghi từng dữ liệu cũ nằm ở đâu, chuyển sang trường nào của cấu trúc mới, và cách đối chiếu sau khi chuyển"

### 18. Hệ quả trừu tượng thay vì hiện tượng quan sát được

Viết cái kết luận trừu tượng thay vì viết cái người đọc sẽ nhìn thấy trên màn hình.

- Sai: "Thiếu một trong hai thì extension không biên dịch được."
- Đúng: "Thiếu một trong hai gói này thì lệnh build báo lỗi thiếu symbol ngay dòng đầu."

Hỏi kiểm tra: người đọc gặp tình huống này thì nhìn thấy chính xác cái gì, ở đâu?

### 19. Tài liệu hướng dẫn viết theo lối giải thích

Bài giải thích kỹ nhưng đọc vô không biết phải làm gì trước, làm gì sau. Đúng nội dung, sai thể loại.

Với Quick Guide, tài liệu bàn giao, hướng dẫn cài đặt: tách Phần A các bước làm lên trước, Phần B tham chiếu xuống sau. Mở đầu bằng một bảng ngắn "cần gì thì đọc mục nào". Người đọc đang muốn làm xong việc, không muốn hiểu toàn bộ hệ thống.

### 20. Tự chế thuật ngữ nghiệp vụ

Khác nhóm 16 ở chỗ: nhóm 16 là dịch tên định danh có sẵn trong code, nhóm này là tự nghĩ ra một từ tiếng Việt nghe hợp lý cho một khái niệm mà trong nghề đã có cách gọi riêng.

| Tự chế | Từ thật sự dùng |
|---|---|
| bản tin, bản tin pallet, bộ bản tin chuẩn | message, message pallet, bộ message chuẩn |
| đặc tả bản tin | tài liệu đặc tả tích hợp |
| Mã bản tin gần nhất | Mã message cập nhật gần nhất |
| Hệ chủ | Nguồn dữ liệu |
| Đầu pallet / Dòng pallet | Pallet / Chi tiết pallet |
| Ảnh chụp tồn kho (Inventory snapshot) | Số tồn tại thời điểm chốt |
| Luật kiểm soát | Quy tắc kiểm soát |
| di trú dữ liệu, trích xuất và lưu trữ | chuyển dữ liệu, đưa ra file lưu |
| BẢN ĐỒ TÀI LIỆU | NỘI DUNG TÀI LIỆU |
| tài khoản dịch vụ | tài khoản |
| tác nghiệp, tác nghiệp kho | làm hàng trong kho, từng lần quét, phiếu kho |
| bóc tách yêu cầu, buổi bóc tách | phân tích yêu cầu, buổi phân tích yêu cầu |
| chương trình trích và chuyển dữ liệu | công cụ chuyển dữ liệu |
| diễn tập chuyển dữ liệu | kiểm thử chuyển dữ liệu |
| nhật ký message, nhật ký thao tác, nhật ký quét | log message, log thao tác, log quét |
| biên dịch extension | build extension |
| hai dịch vụ chỉ đọc | hai API chỉ đọc |
| chính sách vị trí | cách quản lý vị trí lưu trữ |
| cụm pallet, cụm chức năng | phần pallet, khối chức năng |
| nạp version, nạp dữ liệu, version đang nạp | xử lý version, chuyển sang version, version đang xử lý |
| nội dung version | dữ liệu của version |
| hiện hành (recipe hiện hành, BOM hiện hành) | hiện tại |
| lọc trùng, gộp trùng | remove duplicate |
| bản ghi | record |
| kết quả tiêu hao, kết quả nhập thành phẩm, điều chỉnh phân loại (dùng làm tên message, tên API) | Consumption Journal, Output Journal, Item Reclass Journal. Tên chính là đối tượng Business Central, phần tiếng Việt chỉ đi kèm để giải nghĩa |
| vị trí (khi nói về Bin của Business Central) | Bin |
| lệnh nhập kho, lệnh xuất kho (Warehouse Receipt, Warehouse Shipment gửi sang WMS) | phiếu nhập kho, phiếu xuất kho |
| Bộ phận quản lý danh mục | Bộ phận quản lý master data |
| số chứng từ nguồn, số dòng chứng từ nguồn (Source No., Source Line No.) | số chứng từ gốc, số thứ tự dòng trên chứng từ gốc |
| Đầu message, Đầu phiếu / Dòng (tên nhóm trong bảng trường) | Message header / Chi tiết |
| hoàn tác phiếu nhập kho (khi "phiếu nhập kho" đã dùng cho phiếu của WMS) | hoàn tác nhận hàng, hoàn tác xuất hàng |
| rewind, engine, cửa sổ khoá, con trỏ, thư viện (nói về master data) | tạm chuyển về version quá khứ, chức năng xử lý, trong lúc kết ca, field ghi version đang xử lý, nơi lưu dữ liệu |
| dãy số, dãy số tự sinh mã (No. Series) | bộ số, bộ số tự sinh mã |
| dòng dãy số, khoảng số của dãy (No. Series Line) | quy tắc của bộ số |
| chiều phân tích, giá trị chiều phân tích (Dimension, Dimension Value) | mã phân tích, chi tiết mã phân tích |
| phần tử, mỗi phần tử chi tiết, số phần tử của mảng | line, mỗi line, số line trong lines |
| Dựng nội dung phiếu, dựng nội dung message | Mapping trường, lấy dữ liệu |
| Chưa nạp, Thứ tự nạp (nhãn trong file khách điền) | Chưa điền, Thứ tự điền. Xem nhóm 37 |
| Cốt lõi, Mở rộng (nhãn mức ưu tiên của đầu việc trong kế hoạch) | Chính, Làm thêm. PM bắt "cốt lõi là gì, nghe AI quá vậy" (08/10/2026). Nhãn phải là chữ người ta nói khi chia việc: việc phải có người làm, việc làm khi còn thời gian |
| trên thẻ mặt hàng, trên thẻ khách hàng, thẻ chứng từ (khi nói trường thuộc đối tượng nào) | trên mặt hàng, của mặt hàng, trên khách hàng. Trường thuộc về đối tượng, thẻ (Item Card) chỉ là trang hiển thị nó. PM sửa "thẻ mặt hàng" thành "mặt hàng" (10/10/2026), cùng gốc với nhãn "Giá bán trên thẻ hàng" ở nhóm 24. Khi hướng dẫn mở đúng trang thì giữ tên trang tiếng Anh: "mở Item Card" |
| Văn phòng (cột Hình thức của WBS, kế hoạch nguồn lực) | Offsite. Cột này chỉ có ba giá trị Onsite, Online, Offsite như cột Method của Project Plan |

Không có quy tắc cứng là giữ tiếng Anh hay dịch sang tiếng Việt. Quy tắc là **dùng đúng từ người trong nghề và khách hàng đang dùng**. "message" giữ tiếng Anh vì cả team gọi vậy. "log" giữ tiếng Anh vì dev và IT vận hành nói vậy, "nhật ký" nghe như sổ ghi chép tay. "build" giữ tiếng Anh vì dev nói vậy, "biên dịch" đúng nghĩa nhưng không ai nói. "ảnh chụp tồn kho" phải bỏ vì đó là bản dịch chữ của snapshot, thay bằng mô tả thật là "số tồn tại thời điểm chốt".

Bốn lỗi phụ hay đi kèm:

- **Từ nghe nặng hơn mức cần.** "luật" thay cho "quy tắc", "di trú" thay cho "chuyển", "chương trình" thay cho "công cụ".
- **Thêm chữ chính xác hóa không cần thiết.** "tài khoản dịch vụ" trong khi "tài khoản" đã đủ hiểu và không sai.
- **Đặt tên mới cho một việc đã có tên trong quy trình.** Chạy thử chuyển dữ liệu trên bản sao dữ liệu thật chính là kiểm thử, đừng gọi là "diễn tập". Người đọc phải dừng lại hỏi "diễn tập là gì" thì từ đó sai.
- **Dùng thuật ngữ ngành đúng chữ nhưng sai chiều.** ASN là chứng từ người bán gửi báo hàng sắp đến. Viết "nhận hàng theo ASN" trong tài liệu cho bên đang nhận hàng thì người đọc hiểu ngược, vì với họ ASN gắn với lúc xuất. Viết thẳng "phiếu nhập kho" (PM đổi từ "lệnh nhập kho" ngày 02/10/2026, kéo theo "phiếu xuất kho").

Mã danh mục cũng là chữ người đọc nhìn thấy hằng ngày, trên từng dòng chứng từ và từng báo cáo thuế. Đề xuất mã cho khách Việt Nam thì đặt theo cách kế toán Việt Nam gọi, không giữ mã của dữ liệu demo BC hay mã tự nghĩ. Bị bắt ở file data migration master data khách C, 02/10/2026:

| Mã bị sửa | Mã PM yêu cầu | Vì sao |
|---|---|---|
| VN10, VN8, VN5 (nhóm thuế mặt hàng) | VAT10, VAT08, VAT05 | Kế toán gọi theo thuế suất, hai chữ số cho dễ sắp xếp |
| VN0 | KCT | "Không chịu thuế" khác "thuế suất 0%" trên hóa đơn và tờ khai, mã phải nói đúng loại |
| DOMESTIC (nhóm thuế, nhóm hạch toán đối tượng) | TN, NN | Trong nước, nước ngoài là cách chia đối tượng của kế toán Việt Nam. DOMESTIC, FOREIGN, EU là mã demo của BC |
| 2110, 5611, 5631, 6194 (tài khoản demo) | 1561, 33311, 1331, 711 | Tài khoản phải theo hệ thống tài khoản kế toán Việt Nam. Số tài khoản demo đưa vào file gửi khách thì kế toán khách đọc không hiểu |

Mã thuộc dữ liệu chuẩn của BC (DOMESTIC, STANDARD, số tài khoản demo) thì không chép sang file đề xuất cho go-live. Thay bằng mã theo thông lệ Việt Nam, rồi ghi rõ phần nào là đề xuất để kế toán khách chốt.

Tên đối tượng của BC cũng vậy khi cần nhãn tiếng Việt cho người làm nghiệp vụ. Dimension dịch từng chữ thành "chiều phân tích", Dimension Value thành "giá trị chiều phân tích". Kế toán Việt Nam gọi là mã phân tích và chi tiết mã phân tích, PM đổi lại đúng như vậy trong file data migration (02/10/2026). Đặt nhãn tiếng Việt cho một đối tượng BC thì lấy từ kế toán, thủ kho Việt Nam đang dùng trên chứng từ và phần mềm kế toán, không dịch từng chữ của tên tiếng Anh.

Kiểm tra: nói từ này ra trong cuộc họp với khách, họ có gật đầu ngay không, hay phải hỏi lại đó là gì?

### 21. Viết sai tầm người đọc

Cùng một nội dung nhưng người đọc khác nhau thì mức chi tiết kỹ thuật phải khác.

- **Tài liệu cho dev, KB kỹ thuật, hướng dẫn cài đặt**: giữ nguyên tên object, field, page, tham số. Áp nhóm 16.
- **Tài liệu cho BA và consultant**: nói ở mức giải pháp. Được nhắc tên bảng, field, page vì đó là ngôn ngữ chung với dev, nhưng **không đưa cú pháp AL và không dùng code block**. Thay định nghĩa object bằng bảng mô tả nghiệp vụ dạng "Cột thêm | Dùng để | Ví dụ".
- **Tài liệu cho PM, khách hàng, ban lãnh đạo**: bỏ tên object, mô tả theo nhóm chức năng nghiệp vụ và theo khối lượng công việc.

| Cho dev | Cho PM |
|---|---|
| Cod65637 Split QC Order dùng trực tiếp bảng MOB License Plate Content | gói QC đang gắn trực tiếp vào cấu trúc dữ liệu pallet của Tasklet |
| 8 đối tượng tableextension/pageextension extends MOB… | khối chức năng kho dựng trên nền Tasklet |
| 67 event subscriber | khoảng 8% khối lượng tùy biến có liên kết tới Tasklet |

Ví dụ mức BA:

| Viết sai (cú pháp AL) | Viết đúng (mức giải pháp) |
|---|---|
| Table "ABC ESS Print Document" (header) / Print Doc No. Code[20] -- No. Series riêng | bảng mô tả: Cột thêm \| Dùng để \| Ví dụ |
| codeunit 74110 "ABC ESS e-Sign Facade" { procedure Sign(var RecRef: RecordRef) … } | mô tả điểm vào chung cho các chứng từ ký, không viết chữ ký hàm |

Hỏi trước khi viết: ai ký vào tài liệu này, và họ cần con số nào để ra quyết định?

Câu "nói cơ bản thôi" là người hỏi đang báo tầm của mình. Bảng công cụ và API gửi PM ngày 30/09/2026 bị hỏi lại "là API gì" ở ba dòng, trong đó có dòng "Microsoft Entra ID (OAuth client credentials) | Lấy token cho Entra app, không cần người đăng nhập". Cột mô tả nói dùng để làm gì nhưng chưa nói nó là gì, lại giải thích một tên lạ bằng hai tên lạ khác (token, Entra app). Bản trả lời lại mở bằng câu nói nó là gì, "dịch vụ đăng nhập của Microsoft (tên cũ Azure AD)", rồi mới tới việc script dùng nó để làm gì.

### 22. Giọng bắt bẻ đối tác

Trong tài liệu gửi khách hàng hoặc đối tác, việc chỉ ra chỗ chưa khớp trong tài liệu của họ dễ trượt thành giọng vạch lỗi.

- Sai: "Đề xuất WMS ghi Go-live Week 23 nhưng UAT ở Week 27-32 và tổng 7-8 tháng, cần WMS làm rõ mốc thật."
- Đúng: đưa vào mục "Điểm cần thống nhất về lịch", nêu là điểm cần làm rõ khi chốt lịch chung.

Cùng cách chữa: nhãn "Vấn đề phát hiện" đổi thành "Điểm cần làm rõ". Nội dung giữ nguyên, chỉ đổi khung từ phán xét sang cùng chốt.

### 23. Rào đón tự hạ giá trị nội dung mình vừa viết

Rào đón đúng mức là cần thiết khi chưa có estimate. Nhưng thêm một vế phủ định chính mình thì người đọc không còn lý do gì để đọc phần bên dưới.

- Sai: "đây mới là hướng sơ bộ ... **và lúc đó có thể khác với những gì em mô tả bên dưới**."
- Đúng: "đây là hướng tiếp cận sơ bộ, đưa ra để anh và bộ phận kho có cơ sở chọn mục tiêu trước. Còn cách làm cụ thể và chi phí thì phải đợi đội dev estimate xong mới chốt được."

Rào một lần, không rào chồng. Cùng nhóm, ở đầu câu trả lời: "Đúng, bạn chỉ ra một lỗ hổng thật của thiết kế hiện tại". Bỏ vế khen, vào thẳng câu trả lời.

### 24. Rút gọn tới mức mất nghĩa

Yêu cầu ngắn gọn áp cho câu văn, không áp cho nhãn và tiêu đề cột. Nhãn phải đủ nghĩa khi đứng một mình, vì người đọc bảng không đọc câu dẫn phía trên.

- Sai: tiêu đề cột "Ghi phần"
- Đúng: "Phần sản lượng được ghi nhận ở mức này"

Nhãn tiếng Việt cho một trường hệ thống cũng phải đủ nghĩa như vậy. Gọi theo việc trường làm trong nghiệp vụ, không dịch sát caption, không tả vị trí trên màn hình. Giá và số lượng thì nói rõ tính theo đơn vị nào. Bốn nhãn PM sửa trong file data migration master data ngày 02/10/2026:

| Trường | Nhãn bị sửa | Nhãn PM sửa | Vì sao |
|---|---|---|---|
| LSC Store Group Setup `Level` | Cấp | Thứ tự ưu tiên | Cửa hàng thuộc nhiều nhóm thì LS xét nhóm có Level lớn hơn trước. "Cấp" dịch caption mà không nói trường dùng để làm gì (nhóm 7) |
| `Address 2` | Địa chỉ (dòng 2) | Địa chỉ (nối dài) | Gọi theo nội dung của ô, không theo vị trí dòng trên form |
| Item `Unit Cost` | Giá vốn đơn vị | Giá vốn theo đơn vị lưu kho | Một mặt hàng có nhiều đơn vị tính, nhãn phải nói giá này tính cho đơn vị nào |
| Item `Unit Price` | Giá bán trên thẻ hàng | Giá bán chung của hàng | Gọi theo nghĩa nghiệp vụ: giá dùng khi mặt hàng chưa có giá ở bảng giá riêng. Thẻ hàng chỉ là chỗ trường nằm |

Tên trường hệ thống vẫn nằm ở một dòng riêng của sheet (nhóm 16), nên nhãn tiếng Việt được giải nghĩa thay vì dịch sát. Kiểm tra: người điền chỉ đọc nhãn, chưa đọc hướng dẫn, thì có biết phải điền gì và điền theo đơn vị nào không?

### 25. Định nghĩa trừu tượng thay vì ví dụ số cụ thể

Khi người đọc nói "vẫn không hiểu", thường không phải vì câu khó mà vì chưa có số để bám vào.

- Sai: "Posting Date là ngày ghi nhận, quyết định kỳ tính thưởng. Document Posting Date là ngày thật của chính chứng từ nguồn..."
- Đúng: dựng ví dụ có mã và ngày thật (BSO-101 ngày 05/07, SO-9001 ngày 20/07), kẻ bảng bốn dòng, chốt bằng một câu: "Nói gọn: Posting Date lấy ngày BSO, Document Posting Date lấy ngày SO."

Công thức: một ví dụ số có tên thật, một bảng nhỏ, một câu chốt.

### 27. Không đồng bộ với phần còn lại của tài liệu

Viết thêm một mục vào tài liệu có sẵn thì mục đó phải theo đúng quy ước đang dùng, không tự dựng cấu trúc riêng.

Trước khi viết thêm: mở một mục cũ ra xem họ dùng gì cho nhãn phụ, cho danh sách, cho bảng, rồi theo đúng như vậy.

Cùng nhóm với file do khách gửi: khách gửi file đã format sẵn thì bản trả lại phải giữ đúng bộ màu, font, kiểu bảng và cách đánh số của họ. Trả về một file trắng trơn hoặc đổi sang bộ màu khác là trả bài.

### 28. Đề xuất vượt xa phạm vi được hỏi

Khác nhóm 15 ở chỗ: nhóm 15 là trả lời dài, nhóm này là đề xuất to. Được hỏi cách làm một việc cụ thể thì trả về kiến trúc bốn trụ cột kèm lộ trình năm giai đoạn.

Quy tắc: trả lời đúng phạm vi được hỏi trước. Nếu thấy có hướng tổng quát hơn thì nói một câu ở cuối, để người đọc tự quyết có muốn nghe không.

### 29. Đưa giải pháp khi chỉ được yêu cầu mô tả hiện trạng

Tài liệu mô tả bối cảnh và nhu cầu là một thể loại riêng, thường viết để chuyển cho người khác thiết kế giải pháp.

Dấu hiệu nhận ra trong bản nháp: "Tôi khuyên đổi key thành...", các bảng field kiểu "Field | Kiểu | Lookup | Ghi chú".

Tài liệu mô tả đúng chỉ có bốn phần: hệ thống hiện có, hiện trạng tại khách hàng, nhu cầu, và dữ kiện đã kiểm chứng kèm câu hỏi chưa có đáp án. Mở đầu nói thẳng phạm vi: "Tài liệu này chỉ mô tả hiện trạng và nhu cầu, không đề xuất giải pháp."

Chỗ nào chưa kiểm chứng được thì đưa vào mục câu hỏi chưa có đáp án, không lấp bằng một đề xuất.
