---
name: "natural-writing"
description: "Viết và biên tập văn bản sao cho không mang dấu vết văn AI, cho cả tiếng Việt và tiếng Anh. Gồm 37 nhóm dấu hiệu - 13 nhóm theo Wikipedia:Signs of AI writing và 24 nhóm riêng cho tài liệu kỹ thuật, trong đó có WBS và estimate, ngân sách và con số phái sinh, ghi chú giải thích bảng, ghi chú viết cho người lập file thay vì người nhận, email gửi kèm file, trình bày file Excel bàn giao, hướng dẫn xử lý sự cố, trả lời thắc mắc nghiệp vụ và tin nhắn Zalo hướng dẫn người dùng. Áp dụng cho câu trả lời trong chat, file làm trong Cowork, và commit, comment, tài liệu sinh bằng script trong Claude Code. LUÔN dùng khi sinh ra văn xuôi hoặc file cho người đọc, kể cả khi người dùng không nhắc tới văn phong."
---

# Viết như người, không như máy

## Nguyên tắc quan trọng nhất

Bài gốc mở đầu bằng một cảnh báo mà hầu hết bản tóm tắt trên mạng bỏ qua: **các dấu hiệu liệt kê ra là triệu chứng, không phải căn bệnh.** Sửa triệu chứng mà giữ nguyên bệnh chỉ làm văn khó bị phát hiện hơn chứ không tốt hơn.

Căn bệnh là gì? Mô hình ngôn ngữ đoán từ tiếp theo theo xác suất, nên nó **kéo mọi chủ đề về mức trung bình**: chi tiết riêng, hiếm, cụ thể bị thay bằng phát biểu chung chung, tích cực, đúng với mọi chủ đề. Bài gốc ví như tấm chân dung đang mờ dần từ ảnh chụp sắc nét thành phác thảo chung chung, trong khi lời chú thích lại hô to hơn rằng đây là nhân vật đặc biệt. Chủ thể vừa mờ đi vừa được thổi phồng lên.

Vì vậy tiêu chí số một khi rà một đoạn văn không phải "có từ cấm không" mà là:

> Câu này thêm dữ kiện, con số, tên riêng, điều kiện, hệ quả cụ thể nào mà câu trước chưa có? Nếu không, xóa.

Và câu kiểm tra cuối cùng cho cả đoạn: **dán nguyên đoạn này sang tài liệu của một dự án khác, khách hàng khác, sản phẩm khác mà vẫn đúng không?** Nếu vẫn đúng, viết lại.

## Cách hiệu chỉnh mức độ

Bài gốc nói rõ: không dấu hiệu đơn lẻ nào là bằng chứng. Người viết thật cũng dùng gạch ngang dài, cũng liệt kê ba ý, cũng viết "tuy nhiên". Sức mạnh nằm ở **mật độ và tổ hợp**, không ở từng dấu hiệu.

Hệ quả cho việc viết: **ưu tiên diệt câu rỗng và cấu trúc lặp; nới tay với từ vựng đơn lẻ.** Một chữ "quan trọng" đặt đúng chỗ không sao. Ba đoạn liên tiếp mở đầu bằng "Bên cạnh đó" mới là vấn đề.

Cảnh báo ngược cũng nằm trong bài: nếu né sạch mọi thứ trong danh sách, câu văn sẽ cụt lủn và đều tăm tắp, mà kiểu gượng đó cũng là một dấu vết. Chỉ nên ép chặt vài thứ, phần còn lại xử lý bằng biên tập.

## Phạm vi áp dụng

Skill này dùng chung cho mọi nơi Dũng làm việc, không riêng file bàn giao:

- **Câu trả lời trong chat** (claude.ai, Cowork, Claude Code): câu đầu là câu trả lời, ngắn theo đúng tầm câu hỏi (nhóm 14, 15). Báo đã sửa file thì nói sửa gì, ở đâu, trong vài dòng; không kể lại từng bước đã làm.
- **File làm trong Cowork** (Excel, Word, email soạn sẵn): đủ các nhóm bên dưới, nhất là 26, 32 đến 37.
- **Claude Code**: commit message, comment trong code, README, tài liệu sinh bằng script. Commit và ghi chú phiên bản theo mục "ghi chú thay đổi" ở phần Vết tích quy trình.

Phân tích, lý do, phương án và chi phí từng lựa chọn là chỗ của câu trả lời trong chat hoặc tin nhắn cho sếp. Không để chúng lọt vào file hay email gửi khách (nhóm 37).

## Các nhóm dấu hiệu về nội dung

### 1. Thổi phồng ý nghĩa, di sản, xu thế

Gán tầm quan trọng lớn cho việc bình thường, hoặc nối chủ đề vào một bức tranh rộng hơn mà không có nguồn. Bài gốc ghi nhận mô hình làm điều này ngay cả với chủ đề tầm thường như từ nguyên hay số liệu dân số.

- Sai: Tính năng này đóng vai trò then chốt, khẳng định vị thế của LS Central trong ngành bán lẻ.
- Đúng: Tính năng này cho phép POS hoạt động offline tối đa 72 giờ.

Một biến thể: đặt chủ thể vào giữa các "cuộc tranh luận rộng hơn" hoặc nói rằng nó "đặt ra câu hỏi" về điều gì đó lớn lao.

Cách chữa: thay mệnh đề đánh giá bằng dữ kiện kiểm chứng được. Không có dữ kiện thì bỏ câu.

### 2. Nhấn mạnh có sẵn khuôn về mức độ được công nhận

Đây là nhóm bài gốc ghi nhận là **đặc trưng của các mô hình từ 2025 trở đi**. Thay vì trình bày nội dung, văn AI chứng minh chủ thể đáng chú ý bằng cách liệt kê nó đã xuất hiện ở đâu và loại nguồn nào: "được đưa tin trên nhiều báo lớn", "duy trì sự hiện diện tích cực trên mạng xã hội".

Trong bối cảnh tư vấn, nhóm này biến thành: "giải pháp được nhiều doanh nghiệp lớn tin dùng", "được đánh giá cao trên các diễn đàn", "đã được triển khai rộng rãi".

Cách chữa: nêu thẳng nội dung. Không phải "được nhiều khách hàng đánh giá cao" mà "ba khách hàng ngành F&B đang chạy module này từ 2024".

### 3. Phân tích rỗng ở đuôi câu

Mệnh đề phân từ bám đuôi để bình luận về ý nghĩa: "qua đó giúp tối ưu quy trình", "từ đó nâng cao trải nghiệm", "góp phần khẳng định", "ensuring seamless integration", "highlighting its importance".

Bài gốc lưu ý mô hình mới có tìm kiếm web sẽ gắn những nhận định này vào một nguồn có tên thật, bất kể nguồn đó có nói gì gần với vậy hay không. Đây là chỗ nguy hiểm: nhìn có vẻ được dẫn nguồn tử tế.

- Sai: Hệ thống cho phép in tem tại kho, qua đó giúp nâng cao hiệu quả vận hành.
- Đúng: Hệ thống cho phép in tem tại kho, bỏ được bước dán tem thủ công ở khâu đóng gói.

### 4. Giọng quảng cáo

Văn kỹ thuật trượt sang giọng brochure du lịch hoặc thông cáo báo chí. Hiện tượng này xảy ra ngay cả khi đã yêu cầu giọng trung tính, và có trường hợp bản sửa ghi là "đã bỏ giọng quảng cáo" nhưng thực tế lại thêm vào.

Cách chữa: hỏi "ai đo được điều này?". "Liền mạch" không đo được. "Đồng bộ tồn kho trong vòng 5 phút" đo được.

### 5. Biên tập hộ người đọc

"Điều quan trọng cần lưu ý là", "Đáng chú ý rằng", "Không thể không nhắc đến", "It is worth noting that". Xóa vế mở đầu, giữ nội dung. Nếu nội dung quan trọng thật thì vị trí của nó trong bài đã nói lên điều đó.

### 6. Quy chiếu mơ hồ và phóng đại số nguồn

"Nhiều chuyên gia cho rằng", "theo các báo cáo ngành", "giới chuyên môn nhận định". Ngoài việc mơ hồ, bài gốc chỉ ra một lỗi nữa: **phóng đại số lượng nguồn**. Trình bày quan điểm của một nguồn như thể là quan điểm phổ biến, nhắc tới "các nhà nghiên cứu" trong khi chỉ dẫn một người.

Cách chữa: nêu đích danh ai, ở đâu, khi nào. Trong tài liệu dự án: "Chị Hà (Kế toán trưởng) nêu tại workshop ngày 12/03".

### 7. Suy đoán khi thiếu nguồn

Khi không tìm được thông tin, mô hình không im lặng mà viết rằng thông tin "không được ghi nhận rộng rãi", rồi vẫn đoán tiếp về nội dung "có khả năng" là gì. Cả hai vế đều là bịa: kể cả khẳng định rằng thông tin không tồn tại.

Trong tài liệu tư vấn, đây là dạng nguy hiểm nhất. Nếu không tra được một field, một page, một tham số, phải ghi rõ "chưa xác nhận, cần kiểm tra trên môi trường" chứ không viết một câu nghe hợp lý.

**Khi đã có source code hoặc tài liệu trong tay thì phải đọc, không được suy luận.** Lỗi này bị bắt nhiều lần ở nhiều dự án khác nhau, với cùng một phản ứng: "tôi nói bạn đọc code giải thích chứ không phải suy luận", "có đọc code không mà đưa ra gợi ý trật lất", "trên BC hiện tại làm gì có cái này, check lại code xem". Suy luận từ kinh nghiệm về cách BC thường hoạt động nghe rất trôi và sai rất khó phát hiện, vì nó đúng ở đa số trường hợp và sai đúng ở trường hợp đang hỏi. Mở file ra, tìm đúng dòng, lấy đúng tên và giá trị, rồi mới viết.

Cùng gốc: **đọc ảnh chụp tin nhắn bị cắt rồi tự điền phần còn thiếu.** Một dòng Zalo bị cắt ngang được đọc thành "ACP không gỡ" rồi dựng cả lập luận lên đó, trong khi ý thật là NaviWorld vẫn tham gia chuyển tồn và go-live, đang chờ hãng trả lời. Câu bị cắt thì hỏi lại, không đoán.

Một biến thể hay gặp: thấy trong code có cờ hoặc trường mang tên gợi tới một chức năng thì kết luận chức năng đó đang chạy. Có cờ `"Show on COA"` không có nghĩa là có mẫu in giấy chứng nhận chất lượng. Phải tìm tiếp xem có report nào in không, có layout nào không. Không có thì viết thẳng là chưa có, và đó là yêu cầu mới chứ không phải chuyển chỗ làm.

### 8. Kết luận kiểu dàn ý về "thách thức và triển vọng"

Khuôn: "Dù có [loạt từ tích cực], [chủ thể] vẫn đối mặt một số thách thức..." rồi kết bằng đánh giá lạc quan mơ hồ hoặc suy đoán về các sáng kiến tương lai.

Bài gốc nhấn: dấu hiệu nằm ở **cái khuôn**, không phải ở việc nhắc tới khó khăn. Nói về rủi ro dự án là chuyện bình thường và cần thiết. Vấn đề là mục rủi ro không nêu rủi ro nào cụ thể.

## Các nhóm dấu hiệu về ngôn ngữ

### 9. Song song phủ định

"Không phải X, mà là Y" và "Không chỉ X mà còn Y". Có thể trải qua hai câu: câu đầu nêu một điều, câu sau lật lại bằng "tuy nhiên".

- Sai: Đây không đơn thuần là một bản nâng cấp, mà là một thay đổi về cách vận hành.
- Đúng: Bản nâng cấp này đổi cách tính giá vốn, nên kế toán phải chốt tồn trước khi chạy.

Giữ tối đa một lần trong cả tài liệu, khi phép tương phản thật sự cần thiết.

### 10. Né động từ "là" và "có"

Một nghiên cứu bài gốc dẫn cho thấy tần suất "is"/"are" trong văn học thuật giảm hơn 10% trong năm 2023, và khi cho mô hình sửa lại 10.000 tóm tắt, hai từ này xuất hiện ít hơn hẳn.

| Văn AI | Văn người |
|---|---|
| đóng vai trò là / được xem như / thể hiện | là |
| sở hữu / mang lại / cung cấp / được trang bị | có |
| tiến hành thực hiện | làm |
| được biết đến với tên gọi | tên là |
| serves as / stands as / functions as | is |
| boasts / features / offers | has |

Cũng thuộc nhóm này: mở đầu định nghĩa bằng "đề cập đến" hay "refers to" như thể đang định nghĩa một cụm từ chứ không phải mô tả sự vật.

Cách chữa: viết "Sales Order là chứng từ..." chứ không "Sales Order đóng vai trò là chứng từ...".

### 11. Tránh lặp từ một cách máy móc

Mô hình có cơ chế phạt lặp từ, nên nó đổi cách gọi cùng một thứ ở mỗi câu. Trong văn tài liệu kỹ thuật đây là lỗi nặng: cùng một đối tượng mà gọi lần lượt là "hệ thống", "nền tảng", "giải pháp", "công cụ", "phần mềm" thì người đọc không biết có phải cùng một thứ không.

Quy tắc cho tài liệu BC/LS Central: **một đối tượng, một tên, dùng nguyên từ đầu đến cuối.** Sales Order là Sales Order ở mọi câu, không đổi thành "đơn bán", "phiếu bán hàng", "chứng từ bán".

Lưu ý: người Việt viết văn thường cũng được dạy tránh lặp từ, nên dấu hiệu này yếu khi đứng một mình.

### 12. Bộ ba và dải giả

Bộ ba: mọi danh sách đúng ba mục, mọi mô tả xếp ba tính từ. Bài gốc nói mô hình dùng cấu trúc này để làm cho phân tích hời hợt trông có vẻ đầy đủ.

Dải giả: "từ X đến Y" gợi ý một phổ nhưng thực chất là hai thứ rời rạc ghép lại.

Cách chữa: đếm. Ba mục thì cắt còn hai hoặc thêm mục thứ tư có thật.

### 13. Liên từ và câu kết lặp

Mở đoạn bằng "Hơn nữa", "Bên cạnh đó", "Ngoài ra", "Mặt khác" theo nhịp đều. Kết bằng "Tóm lại", "Nhìn chung", "Qua đó có thể thấy" kể cả khi đoạn quá ngắn để cần tóm tắt.

Lưu ý hiệu chỉnh: bài gốc xếp "liên từ đứng riêng lẻ" vào nhóm **dấu hiệu không đáng tin**. Chỉ đáng ngờ khi lặp thành nhịp.

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
| rewind, engine, cửa sổ khoá, con trỏ, thư viện (nói về master data) | tạm chuyển về version quá khứ, chức năng xử lý, trong lúc kết ca, field ghi version đang xử lý, nơi lưu dữ liệu |

Không có quy tắc cứng là giữ tiếng Anh hay dịch sang tiếng Việt. Quy tắc là **dùng đúng từ người trong nghề và khách hàng đang dùng**. "message" giữ tiếng Anh vì cả team gọi vậy. "log" giữ tiếng Anh vì dev và IT vận hành nói vậy, "nhật ký" nghe như sổ ghi chép tay. "build" giữ tiếng Anh vì dev nói vậy, "biên dịch" đúng nghĩa nhưng không ai nói. "ảnh chụp tồn kho" phải bỏ vì đó là bản dịch chữ của snapshot, thay bằng mô tả thật là "số tồn tại thời điểm chốt".

Bốn lỗi phụ hay đi kèm:

- **Từ nghe nặng hơn mức cần.** "luật" thay cho "quy tắc", "di trú" thay cho "chuyển", "chương trình" thay cho "công cụ".
- **Thêm chữ chính xác hóa không cần thiết.** "tài khoản dịch vụ" trong khi "tài khoản" đã đủ hiểu và không sai.
- **Đặt tên mới cho một việc đã có tên trong quy trình.** Chạy thử chuyển dữ liệu trên bản sao dữ liệu thật chính là kiểm thử, đừng gọi là "diễn tập". Người đọc phải dừng lại hỏi "diễn tập là gì" thì từ đó sai.
- **Dùng thuật ngữ ngành đúng chữ nhưng sai chiều.** ASN là chứng từ người bán gửi báo hàng sắp đến. Viết "nhận hàng theo ASN" trong tài liệu cho bên đang nhận hàng thì người đọc hiểu ngược, vì với họ ASN gắn với lúc xuất. Viết thẳng "lệnh nhập kho".

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

### 22. Giọng bắt bẻ đối tác

Trong tài liệu gửi khách hàng hoặc đối tác, việc chỉ ra chỗ chưa khớp trong tài liệu của họ dễ trượt thành giọng vạch lỗi.

- Sai: "Đề xuất Infolog ghi Go-live Week 23 nhưng UAT ở Week 27-32 và tổng 7-8 tháng, cần Infolog làm rõ mốc thật."
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

### 25. Định nghĩa trừu tượng thay vì ví dụ số cụ thể

Khi người đọc nói "vẫn không hiểu", thường không phải vì câu khó mà vì chưa có số để bám vào.

- Sai: "Posting Date là ngày ghi nhận, quyết định kỳ tính thưởng. Document Posting Date là ngày thật của chính chứng từ nguồn..."
- Đúng: dựng ví dụ có mã và ngày thật (BSO-101 ngày 05/07, SO-9001 ngày 20/07), kẻ bảng bốn dòng, chốt bằng một câu: "Nói gọn: Posting Date lấy ngày BSO, Document Posting Date lấy ngày SO."

Công thức: một ví dụ số có tên thật, một bảng nhỏ, một câu chốt.

### 26. Email viết như tài liệu

Email và tài liệu là hai thể loại khác nhau. Email có heading đánh số, có sáu mục, có danh sách tám câu hỏi thì không ai đọc.

Với email: bỏ heading, viết thành đoạn văn liền mạch, giữ đúng phần phản biện và đề xuất bước tiếp theo, tối đa ba bốn câu hỏi. Phần chi tiết để dành cho FDD.

Giọng cũng khác: email dùng giọng nói chuyện với người thật, có "nhờ anh tạo giúp em", "nhé ạ", "anh cho em xin thêm". Kết thư ngắn, không dựng khối chữ ký trang trọng. Chi tiết xem skill `mail-voice`.

**Email gửi kèm file không kể lại nội dung file.** Bị bắt khi gửi WBS ACP cho anh Lâm, qua hai lượt: "gì dài dòng quá vậy", rồi "nhờ anh xác nhận giúp em hai việc => ko cần". Bản nháp đầu có tổng ngày công chia theo vai trò, ba dòng chi tiết 20 MD làm với Infolog kèm mã hạng mục và ngày, phương án Tasklet, lịch go-live, bốn việc nhờ xác nhận và hạn trả lời. Bản Dũng chốt còn bốn câu:

> Em gửi anh file **ACP_Infolog_WBS_v1.1.xlsx**. Tổng khối lượng là 103.5 MD. Trong đó, 20 MD làm việc cùng Infolog em tách riêng ở sheet Tổng quan để anh tiện trao đổi. Hỗ trợ sau go-live em để 3 MD, phát sinh sau đó sẽ đi qua ticket.
>
> Có gì chưa rõ anh cứ trao đổi lại với em.

Ba điều rút ra:

- **Email chỉ giữ con số người nhận cần để quyết định, và chỉ đường tới chỗ còn lại trong file.** Chi tiết đã có trong file thì email nói nó nằm ở sheet nào, không chép lại.
- **Không tự thêm việc nhờ người nhận làm.** Người dùng không giao việc đòi xác nhận thì email không có danh sách xác nhận và hạn trả lời. Các điểm mở của dự án là chỗ của biên bản họp hay sheet điểm cần chốt, không phải email gửi file.
- **Không đưa lập luận nội bộ vào email gửi khách.** Vì sao chọn phương án nào, lịch đối tác sẽ đổi ra sao, là chuyện nội bộ hoặc chuyện của tài liệu phương án.

Kiểm tra: bỏ câu này đi, người nhận mở file ra có hiểu sai hay làm sai gì không? Không thì bỏ.

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

### 30. GAP List và FDD mức BA trượt sang giọng dev

Bị bắt ở GAP List Ampersand (Recipe Version theo ngày), sau khi đã được nhắc "mô tả dưới góc độ BA". Ba lỗi cụ thể:

- **Mở giải pháp bằng cấu trúc code.** "Codeunit NWV ISG Recipe Version Mgt. có ba hàm và một bảng trạng thái:" rồi liệt kê hàm. Người ký GAP List là khách hàng, họ không cần biết có mấy hàm. Viết: "Thêm chức năng Xử lý version theo ngày, gồm action trên Recipe Card, bảng lịch sử và bảng trạng thái", rồi mô tả từng thứ làm gì bằng lời.
- **Dẫn object ID vào cột Solution hoặc tên Business Process.** "(Cod60004, Rep60005)" thay vì "tool Item Positive Posting hiện có". Object ID chỉ để ở sheet Object List hoặc Ghi chú kỹ thuật cho dev.
- **Đưa deliverable dự án vào giải pháp.** "Quick Guide cho Data: tạo version mới, đóng version cũ" không phải giải pháp phần mềm; nó thuộc kế hoạch triển khai. Bỏ khỏi cột Solution.

Cùng lần đó, ba từ bị bắt vì nghe như máy dịch: "nạp" (nạp version, version đang nạp), "hiện hành", "nội dung version". Đã đưa vào bảng nhóm 20. Với BA thì nói "xử lý version", "hiện tại", "dữ liệu của version".

Kiểm tra trước khi giao GAP List: đọc cột Solution như thể mình là khách hàng. Gặp chữ "codeunit", "hàm", "subscriber", "event", mã object thì hạ xuống mức chức năng; gặp tài liệu, training, quick guide thì chuyển sang phần kế hoạch.

### 31. Mô tả logic lấy dữ liệu vòng vo

Bị bắt bốn lượt liên tiếp khi giải thích cách lấy diễn giải CTKM từ LS Central, với nhận xét "diễn đạt vẫn rất khó hiểu". Lỗi không nằm ở từ vựng mà ở cách dựng câu: tách chỗ dữ liệu nằm ra khỏi thứ cần lấy, bắt người đọc tự ghép lại.

Mẫu câu đúng, do chính người đọc viết lại:

> Dựa vô field `Store No.` + `POS Terminal No.` + `Transaction No.` trên LSC Trans. Discount Entry (99001642), lấy 2 field: `Offer Type`, `Offer No.`. Rồi remove duplicate theo `Offer No.`.

Bản bị chê, cùng một nội dung:

> Đọc LSC Trans. Discount Entry (99001642), lọc theo `Store No.` + `POS Terminal No.` + `Transaction No.`. Cần 3 field: `Offer Type`, `Offer No.`, `Discount Amount`.

Bốn điểm khác nhau:

- **Một câu, một thao tác, đủ ba vế: dựa vô field nào, trên bảng nào, lấy field nào.** Bản chê tách thành hai câu, câu đầu nói bảng và điều kiện lọc, câu sau mới nói field, nên người đọc phải nhớ ngược lại.
- **Dùng từ nghề, không dịch.** "remove duplicate" chứ không "lọc trùng" hay "gộp theo". Xem thêm nhóm 20.
- **Bỏ động từ thừa ở đầu câu.** "Đọc", "Cần", "Ta sẽ lấy" không thêm gì. Vào thẳng "Dựa vô".
- **Tên bảng luôn kèm ID trong ngoặc**, viết một lần ở chỗ nó xuất hiện lần đầu trong bước đó.

Ba lỗi hay đi kèm, bị bắt trong cùng lần:

**Kéo field không phục vụ câu hỏi.** Câu hỏi là lấy diễn giải, nhưng bản nháp lấy thêm `Discount Amount`, cộng dồn, rồi dựng cả bảng tiền giảm. Phản hồi: "cộng discount amount làm gì, tôi đã bảo là chỉ cần diễn giải thôi". Cùng gốc với nhóm 28, nhưng ở mức field chứ không ở mức đề xuất.

**Lẫn giá trị ví dụ vào phát biểu logic.** Viết "lấy field `Description` = PARTNER DRINK" trong khi PARTNER DRINK chỉ là giá trị của một giao dịch trong ảnh chụp màn hình. Logic là "lấy field `Description`", hết. Giá trị cụ thể để riêng ở phần ví dụ.

**Tự dựng giả định về đầu ra.** Bản nháp tự nghĩ ra chuyện ghép nhiều CTKM thành một chuỗi để nhét vào một ô của hóa đơn điện tử, trong khi thực tế bao nhiêu CTKM thì bấy nhiêu dòng trên hóa đơn. Cấu trúc đầu ra là thứ phải hỏi, không phải thứ được suy ra.

Kiểm tra trước khi giao: đọc từng bước, hỏi "người làm theo bước này có phải quay lên đọc lại bước trước không?". Phải quay lên thì gộp vế lại thành một câu.

### 32. Bảng phân rã công việc, ước lượng và tiến độ

WBS, kế hoạch nguồn lực và bảng estimate có người đọc kỹ từng dòng, vì nó ra tiền và ra cam kết. Bảy lỗi hay bị trả bài:

**Gán việc cho sai bên.** Viết "Chuẩn bị hồ sơ và chủ trì họp chốt phạm vi ba bên" trong khi bên mình chỉ chuẩn bị tài liệu phân tích, còn chủ trì là khách hàng. Trước khi viết một dòng WBS: bên mình làm gì trong dòng này, và bên nào đứng ra tổ chức?

**Tự tách phạm vi chưa ai chốt thành hạng mục riêng.** Người dùng ghi chú thêm một ý trong lúc trao đổi không có nghĩa là phạm vi đã mở rộng. Gộp vào hạng mục đang có.

**Tính ngày công cho mốc.** "Ký biên bản chốt phạm vi" không tiêu ngày công, nó là mốc. Gộp vào hạng mục sinh ra biên bản đó.

**Đưa vào việc không bắt buộc.** Hỏi từng dòng: bỏ dòng này thì có gì hỏng không? Gỡ Tasklet là bắt buộc vì nó chặn đường. Dọn phần tích hợp cũ không còn dùng thì không gỡ cũng chẳng sao.

**Tên cột vai trò tự chế, và hiểu sai cấp của vai trò.** Mỗi công ty có bộ vai trò riêng trong kế hoạch. Hỏi trước nếu chưa biết họ chia thế nào, và hỏi rõ từng tên là một vai trò riêng hay là tác vụ của cùng một vai trò. Phân tích, Thiết kế, Kiểm thử, Deliver, Hỗ trợ vận hành là năm tác vụ của Functional trong một công việc, không phải năm người khác nhau; bảng tổng hợp phải cộng chúng thành một dòng Functional, và các cột đó phải nằm liền nhau dưới một dải tiêu đề chung.

**Rải ngày công theo tác vụ, không dồn mỗi dòng vào một cột.** Một công việc thường đi qua nhiều tác vụ của cùng một người. "Viết đặc tả tích hợp cho 40 interface" là Phân tích 0,5 cộng Thiết kế 2 cộng Kiểm thử 1 cộng Deliver 0,5, không phải 4 ngày đổ hết vào cột Thiết kế. Dùng số lẻ 0,25 và 0,5 khi cần. Các dòng do bên khác làm thì bên mình vẫn có phần nghiệm thu, đừng để trống rồi gồn thành một dòng kiểm thử đứng riêng.

**Tên công việc không nói rõ ai làm và làm gì.** "Kiểm tra kết nối và giám sát đường truyền" đọc xong không biết là việc của hạ tầng hay của lập trình. Viết thành "Tác vụ nền gọi thử Infolog theo chu kỳ, báo cho IT khi gọi không được" thì rõ ngay là một hạng mục lập trình.

**Quên phần dev ở giai đoạn sau go-live.** Trực go-live và hỗ trợ tăng cường vẫn cần dev, vì có lỗi thì phải sửa ngay. Đừng đánh dấu không cần lập trình ở những dòng đó.

Bốn điều về con số:

- **Ước lượng phải phản ánh cách làm hiện tại.** Bảng estimate lập theo năng suất của mười năm trước sẽ bị bắt ngay bằng câu "sao thời gian làm còn nhiều vậy".
- **Việc hành chính thì đừng đẩy lên ngày.** Lập kế hoạch cutover và danh sách kiểm tra là 0,25 ngày, không phải một ngày rưỡi.
- **Số ngày kéo dài của một nhánh phải tương xứng với số ngày công.** Một nhánh 5 ngày công mà kéo 25 ngày lịch thì người đọc hỏi ngay. Có lý do thật (chờ đầu ra của bên khác, người làm không toàn thời gian) thì viết lý do đó vào cột ghi chú.
- **Không đòi ai ước lượng khi chưa có căn cứ.** Để trống cột ngày công của dev khi chưa có thiết kế là đúng, nhưng phải nói rõ khi nào điền được: đưa hẳn một hạng mục "Đội phát triển ước lượng trên thiết kế và đặc tả đã ký" vào giai đoạn thiết kế, phụ thuộc các hạng mục thiết kế.
- **Dự phòng phải có, nhưng viết cho ra dáng quản lý rủi ro** chứ không phải cho ra dáng đoán mò. Nêu mức theo độ rõ của từng phần phạm vi, nêu căn cứ, nêu điều kiện sử dụng và ngưỡng phải báo cáo.

**Về lịch của bên khác: không sửa.** Trong kế hoạch chung, ngày và số ngày của đối tác giữ nguyên như họ gửi, ghi "Theo kế hoạch <tên bên đó>" ở cột ghi chú. Cần rút ngắn thì rút ở nhánh của mình. Mốc go-live cũng vậy: **lấy đúng ngày đối tác và khách hàng đã nêu**, xếp nhánh của mình cho vừa, rồi nói điều kiện để giữ được mốc đó và điểm nào còn phải chốt. Tự đẩy go-live lùi một hai tháng rồi đưa ra như một đề xuất là việc cần tránh. Trước khi đề xuất bất kỳ ngày go-live nào, mở kế hoạch của họ ra xem họ đã ghi ngày nào.

Ba điều về cách đặt tên dòng công việc, rút từ lần Dũng sửa tay bản WBS ACP tháng 09/2026:

- **Tên dòng là tên của việc, không phải cách mình tham gia việc đó.** "Dự buổi bóc tách yêu cầu tích hợp do Infolog chủ trì" bị đổi thành "Phân tích yêu cầu tích hợp". Động từ chỉ cách dự phần (dự, tham gia, phối hợp cùng, hỗ trợ bên...) làm dòng đó đọc như lịch họp chứ không như một hạng mục công việc.
- **Không nhét vào tên dòng thông tin đã có ở cột khác.** Bên chủ trì đã nằm ở cột Ghi chú, hình thức làm đã nằm ở cột Nơi làm, ngày đã nằm ở sheet tiến độ. Lặp lại trong tên dòng chỉ làm cột Công việc dài thêm và lệch nhịp với các dòng còn lại.
- **Các dòng trong cùng một giai đoạn phải cùng một dạng ngữ pháp.** Giai đoạn Phân tích mà ba dòng là cụm danh từ, dòng thứ tư là một câu kể có chủ ngữ, thì dòng thứ tư lộ ra ngay.

Quy tắc này không mâu thuẫn với lỗi "tên công việc không nói rõ ai làm và làm gì" ở trên. Chỗ đó nói về dòng mà bản chất công việc còn mơ hồ, phải viết rõ để biết nó thuộc hạ tầng hay lập trình. Chỗ này nói về dòng đã rõ bản chất, chỉ bị đeo thêm chủ thể và cách thức.

Ba điều về cách chia dòng, rút từ sheet danh mục công việc phát triển của WBS ACP tháng 09/2026:

- **Các khối cùng cấp phải chia dòng theo cùng một cách.** Khối nhập kho gộp ba chứng từ nguồn vào một dòng và có dòng kết quả cất hàng, trong khi khối xuất kho tách ba dòng và không có dòng kết quả soạn hàng, thì người đọc bắt được ngay. Nhập và xuất, lệnh và kết quả, sản xuất và các khối kho là những cặp phải soi cạnh nhau: cùng cách tách theo chứng từ nguồn, cùng có hoặc cùng không có bước kho tương ứng. Sheet chi tiết và bảng danh mục ở sheet khác phải dùng cùng một bộ mã. Sửa kiểu này thì cứ áp cho các khối còn lại, không cần hỏi lại từng khối.
- **Đối xứng về cách chia dòng, không đối xứng về thời điểm kích hoạt.** Đơn mua, đơn bán, lệnh chuyển kho đẩy sang WMS khi chuyển sang Released, gồm cả bấm Release tay lẫn duyệt qua workflow. Production Order thì không vận hành bằng nút Release; người dùng bấm nút gửi sang Infolog. Chép một trigger cho mọi loại chứng từ là sai. Thời điểm kích hoạt lấy từ quy trình thật của từng chứng từ.
- **Một nút đẩy nhiều lệnh thì ngày công của các lệnh đi sau nhỏ hơn lệnh đầu.** Ba lệnh từ một Production Order đi chung một lần đẩy nên chia 1, 0,5, 0,5 chứ không 1, 1, 1.

Bốn điều nữa về con số, rút từ phản hồi của sếp trên cùng bản WBS:

- **Bảng tổng hợp tách theo bên sẽ thương lượng phần đó, không chỉ theo vai trò.** Ngày công làm cùng đối tác (phân tích yêu cầu, ký đặc tả, kiểm thử tích hợp) đứng thành nhóm riêng có cộng riêng, kèm mã hạng mục và ngày theo lịch đối tác, để người bán hàng tự đem đi thương lượng. Dòng WBS gộp cả phần tự làm lẫn phần làm cùng đối tác thì tách ra hai dòng trước khi tổng hợp.
- **Hỗ trợ sau go-live để khối lượng nhỏ, phần sau đi ticket.** Theo cách NaviWorld đang chào: 3 MD, ghi một câu là phát sinh sau đó tiếp nhận qua ticket.
- **So phương án thì tách phần việc chung và phần riêng của từng phương án.** Giữ Tasklet để tra cứu không làm giảm phần xây bảng pallet mới, vì tích hợp vẫn đi qua bảng mới. Chỉ phần riêng mới được đem ra so. Gộp cả hai vào thì con số tiết kiệm bị thổi phồng và bị bắt ngay.
- **Con số tăng giữa hai bản thì giải thích bằng số trong file đã gửi, trong chat hoặc tin nhắn cho sếp.** Mở bản cũ ra lấy đúng số (bản v1.0 ghi Dev 42, trong khi sếp nhắc 45,5), chỉ từng dòng tăng và lý do. Lời giải thích không đi vào file.

Bốn điều về ngân sách và con số phái sinh, rút từ lần chốt tổng của cùng bản WBS:

- **Con số tổng người duyệt đưa ra là ràng buộc, không phải kết quả tính ra.** "130 tổng là quá nhiều", rồi "80 tới 100 là hợp lý", rồi "sếp bắt loanh quanh 80 tới 85". Nghe xong thì cắt cho vừa khoảng đó rồi mới nói đã cắt ở đâu, đừng giải thích vì sao con số cũ hợp lý.
- **Cắt bằng cách hạ đều nhiều dòng nhỏ, không bằng cách bỏ một dòng lớn.** Hạ 0,25 tới 0,5 ở mười lăm dòng thì bảng vẫn đủ hạng mục. Bỏ hẳn một giai đoạn thì lần sau phát sinh không có chỗ ghi. Các dòng người duyệt đã chốt bằng lời (SIT ba ngày tại chỗ, UAT một ngày, hỗ trợ sau go-live sáu ngày) thì giữ nguyên, và nói rõ chỗ nào còn cắt được nếu cần thêm.
- **Ngày công do đội phát triển ước lượng thì ghi đúng như họ đưa.** Không sửa đè, không thêm cột đề xuất của mình bên cạnh. Muốn đổi thì hỏi họ, hoặc đợi người chủ bảng cho phép gộp dòng. Phần được phép điều chỉnh là phần của chính mình. Cùng nguyên tắc với lịch của đối tác ở trên.
- **Mọi con số suy ra từ số khác phải là công thức, không phải số gõ tay.** Cột Tổng, cột lấy từ sheet khác, dòng quản lý dự án tính 15% tổng Functional và Dev, số đếm interface tính bằng COUNTIF. Gõ tay thì sau ba lần sửa sẽ lệch, mà lệch ở bảng ra tiền thì không ai tha.

**Gộp dòng thì đánh số lại, và không để lại dấu vết của việc gộp.** Ba interface gộp thành một dòng phát triển thì mã phải liền mạch lại từ đầu, không giữ mã cũ rồi ghi chú "Gồm interface I01, I04, I05". Ghi chú đó là lời kể quá trình làm, không phải thông tin người nhận cần. Cần liệt kê đủ từng cái thì để ở bảng danh mục riêng, đánh số con (I01.1, I01.2).

**Số đếm được thì để bảng tự đếm.** "35 interface" viết thành chữ trong câu dẫn, rồi bảng sửa còn 33, thì câu đó thành sai mà không ai thấy. Đặt một dòng tổng dùng COUNTIF dưới bảng, và bỏ con số ra khỏi câu văn ở mọi chỗ khác.

Cuối cùng: **tài liệu bàn giao không chứa ghi chú dạng log.** Không có mục "So với bản trước", không giải thích vì sao con số đổi, không kể lại quá trình trao đổi. Người nhận chỉ cần bản hiện tại đúng.

### 33. Ghi chú giải thích cách đọc bảng

Đặt dưới tiêu đề sheet hoặc dưới bảng một đoạn kể lại bảng có bao nhiêu dòng, cột nào tính bằng công thức, ô màu nào nghĩa là gì, cột nào để ai điền. Người đọc nhìn bảng là thấy hết những thứ đó.

- Sai: "63 công việc trong 12 giai đoạn. Ngày công tách theo bảy vai trò, cột Tổng tính bằng công thức. Cột Dev để trống cho đội phát triển điền, ô tô xám là việc không cần lập trình."
- Đúng: không có đoạn nào cả. Tiêu đề sheet, hàng tiêu đề cột và màu ô đã nói đủ.

Chỉ giữ lại câu mô tả khi nó mang thông tin không đọc được từ bảng: một quy ước không hiển nhiên, một điều kiện áp cho cả sheet, một việc người đọc phải làm. Thước đo: bỏ câu này đi thì người đọc có hiểu sai cái gì không? Không thì bỏ.

Cùng loại trong văn xuôi: "Bảng dưới đây liệt kê...", "Như đã thể hiện ở bảng trên...", "Hình sau minh họa...". Đặt bảng vào đúng chỗ rồi để nó tự nói.

Một biến thể riêng của file nhiều sheet: **dòng "Cấu trúc file" kể sheet nào chứa gì.** Tên sheet nằm ngay trên thanh tab, người đọc bấm một cái là biết. Dòng này bị Dũng xóa khỏi trang tổng quan của bản WBS ACP.

### 34. Đoạn kết tóm tắt lại bài

Viết xong phần nội dung rồi thêm một đoạn kể lại những gì vừa nói: "Như vậy, tài liệu đã trình bày...", "Với các bước trên, người dùng có thể...". Nhóm 13 bắt chữ "Tóm lại" ở cuối đoạn; nhóm này bắt cả đoạn kết, kể cả khi không có chữ "Tóm lại" nào.

Cách kết đúng tùy loại tài liệu:

- **Email**: kết bằng việc cần ai làm, trước ngày nào. "Anh xác nhận giúp em danh sách Location trước thứ Sáu nhé ạ."
- **FDD, FRD, Quick Guide, tài liệu bàn giao**: dừng ở mục hoặc bước cuối cùng. Không thêm đoạn kết.
- **Báo cáo, biên bản**: kết bằng điểm còn mở và bên chịu trách nhiệm, không kết bằng nhận định chung.
- **Bài viết chia sẻ** (Confluence, bài đăng): dừng ở chi tiết đắt nhất, hoặc một câu hỏi ngắn nếu thật sự muốn người đọc phản hồi. Không dùng câu hỏi mở trong tài liệu gửi khách hàng.

Kiểm tra: xóa đoạn cuối đi, người đọc có mất thông tin gì không? Không thì xóa.

### 35. Trình bày file Excel bàn giao

Nhóm này rút ra từ việc đặt bản máy sinh cạnh bản Dũng chỉnh tay. Nội dung gần như giữ nguyên, cái bị sửa là trình bày. Sáu điểm:

**Khối tiêu đề bốn dòng áp cho mọi sheet, kể cả trang tổng quan.** Dòng 1 tên sheet, dòng 2 dòng nhận dạng dự án, dòng 3 ngày cập nhật, dòng 4 là một đường kẻ màu cát cao 1,5 tới 4 điểm chạy suốt chiều ngang bảng. Sheet nào thiếu đường kẻ đó là thấy ngay, vì các sheet đứng cạnh nhau trong cùng một file.

**Ô trong bảng thông tin chỉ cao một dòng chữ.** Ở trang tổng quan, mọi dòng đều 17,5 điểm và không ô nào quấn dòng. Ô phải quấn hai dòng nghĩa là câu trong ô quá dài, cắt câu chứ không tăng chiều cao dòng. Đây là chỗ giao với nhóm 3: cái bị cắt luôn là mệnh đề giải thích bám đuôi.

| Máy viết | Người sửa |
|---|---|
| Tích hợp Microsoft Dynamics 365 Business Central với Infolog WMS, thay thế Tasklet Mobile WMS | Tích hợp Microsoft Dynamics 365 Business Central với Infolog WMS |
| Phần việc phía Business Central do NaviWorld thực hiện, và tiến độ đề xuất ghép với kế hoạch Infolog | Phần việc phía Business Central do NaviWorld thực hiện |
| Quản lý dự án, tính 15% tổng Functional và Dev | Quản lý dự án |

Dòng cuối cho thấy cùng một nguyên tắc với nhóm 33: cách tính đã nằm trong công thức của ô bên cạnh, viết lại thành chữ là thừa.

**Độ rộng cột đặt theo nội dung thật, không đặt cho rộng rãi.** Cột nội dung của trang tổng quan bị hạ từ 76 xuống 52,6 ký tự. Cột rộng gấp đôi câu dài nhất làm bảng loãng ra và đẩy các cột số ra xa mắt.

**Chiều cao dòng bám sát nội dung.** Hàm ước lượng chiều cao trong script hay tính dư một dòng, và dòng dư đó nhân lên sáu chục dòng thì bảng dài thêm cả trang. Bốn dòng trong bản WBS bị hạ từ 40,5 xuống 26 và từ 66,75 xuống 52.

**Gộp cột và gộp dòng bằng Outline Group, và gộp hết chứ đừng gộp một nửa.** Bản máy sinh gộp bốn cột Functional nhưng bỏ sót hai cột Dev và Quản trị; Dũng kéo nhóm phủ cả sáu cột ngày công, để thu lại còn đúng cột Tổng. Dòng chi tiết gộp dưới dòng giai đoạn, giai đoạn có nhóm con thì thêm một cấp nữa. Nút gộp đặt phía trên và bên trái, tức summaryBelow và summaryRight đều tắt.

**Cùng một quy ước thì áp cho cả file.** Đường kẻ dòng 4, cách tô màu ô, cách đặt nhóm cột, kiểu chữ tiêu đề: đặt một lần trong hàm dựng chung, đừng viết riêng cho từng sheet. Phần lớn lỗi trình bày bị bắt là do một sheet được dựng bằng nhánh code riêng nên thiếu mất một chi tiết mà các sheet khác đều có.

Tên giai đoạn và tiêu đề mục viết một thứ tiếng. "G1. Phân tích (Analysis phase)" bị cắt còn "G1. Phân tích": bản tiếng Anh trong ngoặc là dấu vết của việc đối chiếu với khung mẫu, không phải thông tin cho người đọc.

Kiểm tra trước khi giao: mở file lên, nhìn bốn dòng đầu của từng sheet xem có giống nhau không; bấm nút gộp của từng nhóm cột xem thu lại còn đúng những cột cần đọc không; tìm ô nào cao bất thường so với các ô cùng bảng.

### 36. Hướng dẫn xử lý sự cố cho người dùng viết như báo cáo phân tích

Sau khi tìm ra nguyên nhân một lỗi, bản giải thích cho người trong nhóm dự án có số field, cơ chế BC, hai kịch bản, các bẫy khi làm. Đem nguyên bản đó làm hướng dẫn cho người dùng hay key user là sai thể loại. Người dùng chỉ cần biết hai thứ: gặp tình huống nào thì làm, và làm gì.

Bị bắt ở lỗi gửi IC SO từ SKV sang Hàng gửi bán. Bản phân tích có hai bảng kèm số field (125, 126, 123...), thêm mục Validate Field, IC Direction, IC Status và thứ tự áp field. Dũng tự viết lại thành hướng dẫn gửi người dùng như sau:

> Trong trường hợp anh chị không gán IC Partner trong Customer thì lúc send SO IC báo lỗi này. Thì dùng config package update cho mấy field này nhé.
>
> Sales Header:
> - Sell-to IC Partner Code = mã IC
> - Bill-to IC Partner Code = mã IC
> - Send IC Document = Yes
>
> Sales Line:
> - IC Partner Ref. Type = Item
> - IC Partner Reference = mã hàng

Cách viết đó có sáu điểm:

- **Một câu tình huống, một câu hành động, rồi vào danh sách.** Tình huống nói bằng thứ người dùng thấy và bằng việc họ đã làm hoặc chưa làm ("không gán IC Partner trong Customer", "send SO IC báo lỗi này"). Không mở bằng nguyên nhân kỹ thuật.
- **Chỉ ghi field phải đổi, theo dạng `Field = giá trị`, nhóm theo bảng.** Field để mặc định hoặc đã đúng sẵn (IC Direction, IC Status) thì không ghi. Khoá chứng từ cũng không ghi, vì ai làm config package cũng biết.
- **Tên field để nguyên như trên màn hình, không kèm số field.** Số field có ích cho dev, còn người dùng tìm field theo tên.
- **Giá trị thay đổi theo từng đơn thì ghi bằng tên chung** ("mã IC", "mã hàng"), không lấy giá trị của một ca test (YSKH, SV37900019). Đây là hướng dẫn dùng lại nhiều lần, khác với ví dụ minh hoạ ở nhóm 25.
- **Không giải thích cơ chế.** Chuyện vì sao BC không tự gán thì để dành cho Issue Log hay tài liệu nội bộ.
- **Giọng tin nhắn gửi người dùng**: "anh chị", "nhé", "mấy field này". Cùng giọng với nhóm 26.

Lưu ý ranh giới: bỏ phần giải thích, không có nghĩa là bỏ một bước mà thiếu nó thì làm sẽ hỏng. Bước nào bắt buộc (ví dụ phải tắt Validate Field thì package mới áp được) thì thêm đúng một dòng hành động, vẫn không giải thích vì sao. Có điểm như vậy thì chỉ ra cho Dũng, đừng tự chèn cả đoạn lý do vào hướng dẫn của Dũng.

Kiểm tra: người dùng làm theo được mà không phải hỏi lại không? Bỏ một dòng đi thì họ có làm sai không? Không làm sai thì bỏ dòng đó.

**Cùng nhóm: trả lời một thắc mắc nghiệp vụ của người dùng.** Bị bắt ở SKV, phiếu nhập không undo được vì hàng đã chuyển kho, hàng hư trả nhà cung cấp mà không có hóa đơn. Kế toán hỏi: "k có hóa đơn thì sao chị làm Purchase Invoice được". Bản nháp có ba đoạn: PO treo số lượng đã nhận chưa có hóa đơn, công nợ âm; ba bước ghi số PPR cụ thể, giữ VAT08, cùng đơn giá, cùng ngày; rồi TK 133110 và một cặp PPI/PPCM tháng trước làm bằng chứng. Dũng tự viết lại như sau:

> PI trên BC không hẳn là ghi nhận hóa đơn GTGT đâu chị. Đây là chứng từ để kết thúc quy trình mua hàng, nếu chị đã phát sinh nhập kho rồi mà không undo được thì bắt buộc phải làm PI để kết thúc quy trình, chứ ko là ko đóng sổ được đâu.
>
> Về quy trình thì vẫn phải làm theo các bước như trên, còn về chi tiết, không muốn nó lên bảng kê đầu vào thì chị làm các phần sau giúp em
> 1. Chỗ Vendor Invoice No. trên PI và Vendor Cr. Memo No. trên PCM chị ghi cùng một số, ví dụ số PO, miễn sao giống nhau và không để trống là đc
> 2. Khi in bảng kê VAT Input, tick vô Exclude Reverse. Các cặp cùng số ở mục 1, cùng giá trị trong kỳ sẽ không lên bảng kê

Năm điểm khác bản nháp:

- **Gỡ đúng chỗ hiểu lầm bằng khái niệm nghiệp vụ.** Người hỏi đang đồng nhất PI với hóa đơn đỏ. Câu đầu tách hai thứ đó ra ("không hẳn là ghi nhận hóa đơn GTGT"), rồi nói PI dùng để làm gì bằng ngôn ngữ kế toán: kết thúc quy trình mua hàng, không làm thì không đóng sổ được. Không kể cơ chế BC (số lượng treo trên PO, công nợ âm).
- **Không nhắc lại quy trình đã gửi.** "vẫn phải làm theo các bước như trên", chỉ thêm phần chi tiết đúng mối lo của người hỏi (không lên bảng kê).
- **Ghi quy tắc, không ghi một giá trị cụ thể.** "cùng một số, ví dụ số PO, miễn sao giống nhau và không để trống" thay cho "ghi PPR-2608-00511". Ví dụ lấy thứ người dùng quen tra (số PO), không lấy số chứng từ do mình chọn. Nêu giá trị cụ thể thì người đọc hỏi ngay "sao phải là số đó".
- **Kết quả của report nói bằng một vế, không kèm bằng chứng.** "các cặp cùng số, cùng giá trị trong kỳ sẽ không lên bảng kê". Phần đã chạy report ba tháng, đếm dòng, cặp PPI/PPCM mẫu, TK 133110 là để người tư vấn tự chắc chắn, không đưa cho người dùng.
- **Không kể chuyện sửa lời trước đó.** Gợi ý cũ (đổi sang KKKNT) chưa gửi khách thì không cần câu "chị bỏ qua cách em nói trước".

Kiểm tra: câu đầu có trả lời đúng câu người dùng hỏi không, hay đang trả lời câu mình muốn giải thích? Có con số nào người dùng sẽ hỏi lại "sao lại là số này" không?

**Cùng nhóm: tin nhắn Zalo hướng dẫn dùng một tính năng.** Tình huống ở YSKH: chị Hân hỏi một item dùng nhiều BOM được không. Dũng đã trả lời là dùng BOM Version, chị hỏi tiếp có phải mỗi lần tạo lệnh là chọn lại rồi refresh không. Bản nháp máy viết có câu dẫn "Vì vậy chị làm như sau:", ba bullet, và câu kết "Như vậy chị không phải mở thêm item mới nữa." Dũng sửa thành:

> Dạ đúng rồi chị, mặc định BC luôn lấy version đã Certified có Starting Date gần nhất tính tới ngày của lệnh sản xuất. Nếu không có version nào hợp lệ thì nó lấy BOM gốc
>
> Để dùng cho nhu cầu trên chị làm như vầy nhé: Item vẫn giữ 1 mã, 1 Production BOM. Công thức A, B, C tạo thành 3 version trong BOM đó, cả 3 đều chuyển Certified. Version nào dùng nhiều nhất thì để Starting Date mới nhất, nó sẽ là mặc định.
> Lệnh nào cần công thức khác thì trên Released Production Order, ở phần Lines đổi cột Production BOM Version Code sang B hoặc C, rồi bấm Refresh Production Order. Lúc refresh nhớ bỏ tick "Lines", chỉ để tick "Component Need". Nếu tick Lines thì BC tính lại dòng và trả về version mặc định.
>
> Ngoài ra, nếu muốn so sánh 3 công thức thì chị vào Production BOM Version Comparison là thấy đc á

Có sáu chỗ sửa:

- **Tin nhắn không dùng bullet khi mỗi ý là một câu hoàn chỉnh nói với người đọc.** Ba bullet đều bắt đầu bằng "chị..." được gộp thành một đoạn liền. Danh sách chỉ giữ khi các mục là giá trị rời để nhập vào, như dạng `Field = giá trị` ở trên.
- **Giữ tên field và tên trang như trên màn hình, kể cả trong câu văn.** Viết "Starting Date", không viết "ngày bắt đầu". Người dùng tìm theo nhãn tiếng Anh trên màn hình, gặp chữ tiếng Việt thì phải tự dịch ngược lại.
- **Chỉ đúng trang mở ra, kèm status.** "mở lệnh sản xuất" bị đổi thành "trên Released Production Order". BC có danh sách lệnh riêng cho từng status, nên viết chung là "lệnh sản xuất" thì người dùng không biết mở danh sách nào.
- **Dùng đúng từ người hỏi đã dùng.** Chị hỏi về "BOM", nên viết "BOM gốc" chứ không phải "công thức gốc trên BOM".
- **Bỏ câu kết nhắc lại cái lợi mà người hỏi đã biết.** Không mở thêm item mới chính là điều chị đang hỏi, nói lại chỉ làm tin nhắn dài thêm (nhóm 34). Tin nhắn kết ở phần thêm tùy chọn, mở bằng "Ngoài ra".
- **Giọng Zalo với người lớn hơn**: mở bằng "Dạ", dùng "như vầy nhé", "là thấy đc á". Câu dẫn nối vào nhu cầu của người hỏi ("Để dùng cho nhu cầu trên"), không dùng câu chuyển chung chung như "Vì vậy chị làm như sau".

Kiểm tra: đọc tin nhắn trên khung chat điện thoại. Có dấu đầu dòng nào đứng trước một câu nói với người đọc không? Có chữ nào người dùng phải dịch ngược ra tiếng Anh mới tìm được trên màn hình không?

### 37. Ghi chú viết cho người lập file, không cho người nhận

Nhóm 33 bắt đoạn giải thích cách đọc bảng. Nhóm này bắt ghi chú trong từng ô: cột Ghi chú, cột Phụ thuộc, dòng tổng cộng, bảng giả định. Người lập file hay để lại ở đó những câu chỉ có ích cho chính mình lúc tính toán. Bị bắt trên bản WBS ACP tháng 09/2026, với phản hồi "sao lại đưa mấy thông tin kiểu này vô file gửi khách", rồi "sao vẫn còn mấy kiểu ghi chú này".

Thước đo cho mỗi ghi chú: người nhận đọc câu này thì biết thêm việc gì phải làm, điểm gì phải chốt, ngày nào phải có mặt, hay ràng buộc nghiệp vụ nào? Không trả lời được thì bỏ. Năm kiểu không qua được:

| Kiểu | Ví dụ đã bị bắt | Vì sao sai |
|---|---|---|
| Sổ sách tính ngày công | "Chỉ tính ngày công Dev.", "Nằm trong 20 ngày công làm việc với Infolog", "Tính 15% tổng ngày công Functional và Dev, công thức tự tính", "Chỉ gồm các hạng mục có phát sinh lập trình" ở dòng tổng | Nói con số được cộng ở đâu, tính thế nào. Công thức trong ô đã làm việc đó |
| Tham chiếu tài liệu khác, phiên bản, mã phương án | "Theo PA1 trong tài liệu phương án xử lý Tasklet v1.1", "Áp dụng cho mọi phương án xử lý Tasklet" | Người nhận phải mở file khác mới hiểu, và tên phiên bản sai ngay khi file kia đổi bản |
| Chi phí giả định | "ACP chọn PA2 thì cộng thêm 5,5 ngày công" | Là nội dung thương lượng, không phải phạm vi đang báo. Đưa vào file ước lượng là tự mở cửa cho mặc cả |
| Con số không có chi tiết đi kèm | "rà 21 quy tắc kiểm soát", "chốt 59 điểm cần quyết định", "20 màn hình chuẩn" | Trong file không có danh sách, đọc xong không biết là những gì. Số đếm lấy từ file khác còn dễ lệch (59 ở đây, 57 ở file tích hợp) |
| Mã nội bộ không giải nghĩa | "Q-A1.", "(Q-I3)", phụ thuộc "Q-B1, Q-L1" | Mã của một bảng khác, người nhận không tra được. Có nội dung thì giữ nội dung, bỏ mã. Phụ thuộc thì ghi thẳng thứ phụ thuộc: "danh sách kho và danh sách mặt hàng lô ảo từ ACP" |

Nhiều ghi chú không cần xóa mà cần viết lại cho đúng phần người nhận quan tâm:

- "15 ngày theo hạng mục G.1, nằm trong 20 ngày công làm việc với Infolog" viết thành "Có mặt cùng Infolog trong 15 ngày theo hạng mục G.1, 23/11 tới 11/12/2026". Giữ ngày, bỏ phép cộng.
- "Ngày công Dev ước lượng sau khi ACP đánh dấu danh sách, khoảng 3 tới 5 ngày nếu giữ gần hết" viết thành "Chờ ACP chọn các màn hình và báo cáo pallet giữ lại sau go-live". Giữ việc ACP phải làm, bỏ con số giả định.
- "Phương án lùi là bật lại Tasklet trong 48 giờ. ACP chọn PA2 thì cộng thêm 5,5 ngày công" viết thành "Phương án lùi là bật lại luồng quét Tasklet trong 48 giờ đầu sau cutover".

Không nhầm với các ghi chú nghiệp vụ có chữ "chỉ": "Chỉ nhận trạng thái, không nhận chi tiết kết quả kiểm tra" nói phạm vi của interface, giữ lại.

Sửa kiểu này thì rà cả file bằng năm kiểu trên, không chỉ sửa đúng câu bị chỉ ra, vì câu tương tự thường nằm ở sheet khác.

## Dấu hiệu về hình thức

Nhóm này dễ sửa nhất và cũng lộ nhất. Chi tiết đầy đủ nằm ở `references/dau-vet-ky-thuat.md`.

- In đậm rải khắp nơi, đặc biệt là in đậm mọi lần xuất hiện của một thuật ngữ. Quy tắc đang áp: **chỉ in đậm ở nhãn đầu mục và phần dẫn đầu bullet**. Không in đậm giữa câu trong đoạn văn, không in đậm trong ô bảng.
- Bullet dạng "**Thuật ngữ:** câu giải thích lặp lại chính thuật ngữ đó".
- Danh sách ở chỗ hai câu văn xuôi là đủ.
- Heading Title Case tiếng Anh; heading rập khuôn: "Thách thức", "Triển vọng", "Kết luận", "Key Features".
- Emoji trong tiêu đề hoặc đầu bullet.
- Gạch ngang dài `—` ở chỗ dấu phẩy, ngoặc đơn hoặc hai chấm hợp hơn. Mô hình thường đặt **dấu cách hai bên**, trái với quy ước sắp chữ.
- Dấu nháy cong `’ “ ”` lẫn vào văn thuần. Đây là dấu hiệu yếu vì Word và macOS tự đổi.
- Bảng nhỏ không cần thiết, chỗ hai câu văn là đủ.
- Nhảy cấp heading, hoặc chèn đường kẻ ngang trước mỗi heading.
- Mọi mục trong danh sách dài xấp xỉ bằng nhau, cấu trúc song song hoàn hảo.

Với văn tiếng Việt: dùng `-` thay cho `—`, không dùng `→` và `⇒`. Thay mũi tên bằng từ nối thật, vì mũi tên giấu mất quan hệ giữa hai vế.

- "Gỡ Tasklet ⇒ phải gỡ hết tham chiếu" viết thành "Gỡ Tasklet thì phải gỡ hết tham chiếu"
- "Lệch quy đổi ⇒ lệch tồn" viết thành "Sai quy đổi đơn vị tính dẫn tới lệch tồn"
- "đổi Lot ⇒ QC tự về HOLD" viết thành "đổi lô thì trạng thái chất lượng tự về chờ kiểm"

Ba thứ khác bị bắt trong bản WBS ACP: **dấu chấm phẩy** (tách câu ra hoặc dùng dấu phẩy), **chữ "trực"** ở mọi dạng (trực go-live, trực tuyến, trực tiếp - viết "hỗ trợ go-live", "từ xa", "tới"), và **"lỗi mức chặn"** (viết "lỗi làm dừng quy trình").

Với bảng Excel bàn giao: ô để người khác điền và ô không áp dụng phải phân biệt được bằng mắt: ô cần điền tô một màu nhạt, ô không áp dụng tô xám. Một cột trống trơn không cho biết là chưa điền hay không cần điền. Màu ô tự nói được điều đó, không cần thêm câu giải thích (xem nhóm 33). Cột thuộc cùng một vai trò thì để liền nhau và gộp dưới một dải tiêu đề chung. Phần bố cục còn lại xem nhóm 35.

## Vết tích quy trình

Nhóm này là bằng chứng gần như chắc chắn, và phải xóa sạch trước khi giao tài liệu:

- Lời hội thoại sót lại: "Hy vọng nội dung này hữu ích", "Bạn có muốn tôi bổ sung phần nào không", "Certainly! Here's the revised version".
- Câu rào đón về giới hạn kiến thức hoặc mốc cập nhật dữ liệu.
- Placeholder chưa điền: `[Tên công ty]`, `[Insert date]`, `INSERT_URL_HERE`, ngày dạng `2025-XX-XX`.
- Mã đánh dấu nội bộ của từng chatbot lọt vào văn bản.
- **Sửa văn phong nhưng chỉ sửa một nơi.** Với tài liệu sinh bằng script, cùng một cụm từ thường nằm ở nhiều file nguồn: file nội dung và chuỗi hardcode trong file dựng. Sau khi sửa, grep cụm từ đó trên toàn bộ file nguồn trước khi build lại.
- **Sửa một chỗ mà không rà cả họ chỗ cùng loại.** Người dùng bắt một từ thì họ đang bắt cả họ từ đó: bỏ "trực" là bỏ luôn "trực tuyến" và "trực tiếp", đổi một tên giai đoạn là đổi cả bảy, cắt đuôi giải thích ở một ô là cắt ở mọi ô cùng bảng. Sửa xong thì grep lại toàn bộ file nguồn theo gốc từ, đừng chỉ sửa đúng chỗ được chỉ.
- **Chữ tiếng Việt mất dấu trong file xuất ra.** Nội dung trong chat có dấu đầy đủ nhưng khi sinh file bằng script thì thành "PHAN BO ITEM CHARGE". Lỗi nằm ở khâu sinh file, đọc lại bản trong chat sẽ không thấy. Mở file vừa xuất ra và kiểm tra tên sheet, tiêu đề cột trước khi giao.
- **Công thức trỏ sai cột sau khi chèn thêm cột.** Thêm một cột vào giữa bảng thì mọi COUNTIF, SUMIF, tham chiếu theo chữ cái cột ở sheet khác đều lệch một cột và vẫn chạy, chỉ ra kết quả 0. Sau khi chèn cột, mở lại các ô tổng hợp và kiểm tra giá trị.
- **SUMIF và COUNTIF ép mã dạng "x.y" về số.** Tiêu chí "5.1" và "5.10" bị Excel đọc thành cùng một số 5,1 nên cộng chéo hai dòng, ra tổng lớn hơn thật. Mã hạng mục dạng "x.y" làm khóa tra cứu thì dùng SUMPRODUCT so sánh chuỗi.
- **SUMPRODUCT phải nhận các mảng cùng kích thước.** Nhân một mảng một cột với vùng bốn cột thì LibreOffice tự giãn và ra số, còn Excel trả #VALUE!. Cộng từng cột lại thành một mảng một cột: `SUMPRODUCT((A=mã)*(F+G+H+I))`.
- **LibreOffice mở được không có nghĩa là Excel mở được.** Hai lỗi đã gặp đều thuộc loại này: công thức SUMPRODUCT ở trên, và việc vá thẳng XML trong file xlsx. Thứ tự thẻ con của `sheetPr` bắt buộc là `tabColor`, `outlinePr`, `pageSetUpPr`; chèn `outlinePr` lên trước `tabColor` thì LibreOffice vẫn mở bình thường còn Excel báo "Repaired" và bỏ sạch nội dung của cả file. Vá XML xong phải parse lại toàn bộ phần XML trong gói, kiểm thứ tự thẻ, rồi mở lại file bằng thư viện đọc trước khi gửi.
- **Bước recalc bằng LibreOffice xóa một số thiết lập trình bày**, trong đó có `outlinePr`. Thiết lập nào bị mất thì phải đặt lại sau bước recalc, không phải trước.
- **Báo đã sửa nhưng bản người dùng mở vẫn là bản cũ.** Bị bắt bằng câu "sao vẫn còn": bản sạch chỉ nằm ở phía mình, bước chép xuống thư mục của người dùng báo thành công nhưng chép một bản cũ hơn. Sau khi ghi file vào thư mục người dùng, đọc lại chính file ở đó và tìm lại đúng các cụm vừa bỏ. File đang mở trong Excel có AutoSave thì dặn đóng không lưu rồi mở lại, không thì Excel lưu đè bản cũ lên.
- **Gửi kèm những file người ta không cần.** File nguồn, script sinh tài liệu, file ghi chú nội bộ thì lưu lại, không đưa vào danh sách bàn giao. Chỉ gửi đúng thứ người ta yêu cầu.
- **Gửi thiếu file trong bộ nhiều file.** Dự án có hai ba file đi kèm nhau thì lần nào cũng gửi đủ bộ, kể cả khi chỉ sửa một file. Người nhận không nhớ file nào là bản mới nhất và sẽ hỏi lại.

Bài gốc còn có một mục rất đáng học: **ghi chú thay đổi**. Ghi chú do AI viết hay trấn an thái quá rằng thay đổi đã "đảm bảo tuân thủ", "cải thiện tính trung lập", và hay nhắc tới cả những phần **không** bị sửa. Người viết thật ghi ngắn và cụ thể: sửa gì, ở đâu, vì sao. Áp dụng cho commit message, ghi chú phiên bản tài liệu, và email báo đã cập nhật.

## Đặc điểm văn người viết

Phần này nói cái **nên làm** chứ không phải cái nên tránh:

1. **Dùng "là" và "có" trần trụi.** "Có ba trường hợp", "Nó là bản ghi tồn kho".
2. **Dùng từ thường thay vì từ trang trọng đồng nghĩa.** "viết" thay "chấp bút", "dùng" thay "sử dụng", "thử" thay "tiến hành thử nghiệm". Với tiếng Việt cần cân nhắc phép lịch sự khi viết cho khách hàng.
3. **Dám nói khẳng định dứt khoát.** "chỉ có một cách", "đây là lần đầu tiên", "cách tốt nhất là".
4. **Dùng từ đệm và từ nhấn.** "chắc", "hình như", "khá", "hơi", "nói chung", "thường thì".
5. **Thỉnh thoảng viết dài dòng một cách rất người.** "do đó mà", "để mà", "cái việc là".
6. **Nhịp câu không đều.** Câu năm chữ xen giữa câu bốn mươi chữ. Mỗi câu mang một, tối đa hai ý; ý thứ ba sang câu mới.

## Quy trình áp dụng

Viết trước, rà sau. Vừa viết vừa tự kiểm duyệt thì văn sẽ cụt.

1. **Viết bản thô** theo nội dung, chưa quan tâm văn phong.
2. **Lượt rà nội dung**: đọc từng câu, hỏi "câu này thêm gì?". Xóa câu rỗng. Đây là lượt quan trọng nhất.
3. **Lượt rà cấu trúc**: song song phủ định, bộ ba, đuôi phân từ, liên từ mở đoạn lặp, câu kết thừa, né "là"/"có", đổi tên đối tượng giữa chừng.
4. **Lượt rà thứ tự và thể loại**, với tài liệu kỹ thuật. Hai mươi hai câu hỏi, xem nhóm 14 đến 37:
   - Câu đầu đã là câu trả lời chưa?
   - Độ dài và tầm vóc đề xuất có tương xứng câu hỏi không?
   - Tên định danh có bị dịch thành chữ của mình không, có tự chế thuật ngữ không, có đặt tên mới cho việc đã có tên không?
   - Tiêu đề mục và thân bài có ẩn dụ không?
   - Mức chi tiết kỹ thuật có đúng người đọc không: dev, BA, hay PM và khách hàng?
   - Đúng thể loại chưa: hướng dẫn thì các bước lên trước, tài liệu mô tả hiện trạng thì không chen giải pháp, email thì không dựng heading?
   - Với GAP List, Issue Log, FDD mức BA: cột Solution còn chữ codeunit, hàm, event, mã object không? Còn deliverable dự án (Quick Guide, training) lẫn vào giải pháp không?
   - Mỗi bước lấy dữ liệu đã đủ ba vế trong một câu chưa: dựa vô field nào, trên bảng nào, lấy field nào?
   - Với WBS và bảng estimate: đúng bên làm chưa, đúng bộ vai trò của công ty chưa, ngày công có rải theo tác vụ chưa, lịch của bên khác có bị sửa không, mốc go-live có lấy đúng ngày họ đã nêu không?
   - Tổng có nằm trong khoảng người duyệt đưa ra không, số do đội phát triển ước lượng có bị sửa đè không, con số suy ra từ số khác đã là công thức chưa?
   - Gộp dòng xong đã đánh số lại chưa, còn ghi chú nào kể lại việc gộp không? Còn con số đếm được nào viết thành chữ trong câu văn không?
   - Tên các dòng trong cùng một giai đoạn có cùng dạng ngữ pháp không, có dòng nào đeo thêm chủ thể hoặc cách thức đã nằm ở cột khác không?
   - Có đoạn nào đang giải thích cách đọc bảng không? Bỏ đi.
   - Ghi chú trong ô có câu nào chỉ có ích cho người lập file không: sổ sách tính ngày công, tham chiếu phiên bản hay phương án của tài liệu khác, chi phí giả định, con số không kèm danh sách, mã nội bộ không giải nghĩa?
   - Các khối cùng cấp (nhập và xuất, lệnh và kết quả) có chia dòng cùng một cách, dùng cùng bộ mã ở mọi sheet không? Thời điểm kích hoạt của từng loại chứng từ có lấy đúng quy trình thật của nó không?
   - Bảng tổng hợp đã tách riêng phần làm cùng đối tác chưa, nếu phần đó thương lượng riêng?
   - Email gửi kèm file: có đang chép lại chi tiết trong file, tự thêm việc nhờ xác nhận, hay đưa lập luận nội bộ không?
   - Trả lời thắc mắc của người dùng: câu đầu có gỡ đúng chỗ họ hiểu lầm không, có số chứng từ cụ thể nào khiến họ hỏi lại "sao lại là số này" không?
   - Đoạn cuối có đang tóm tắt lại bài không? Email thì kết bằng việc cần làm, tài liệu thì dừng ở mục cuối.
   - Hướng dẫn xử lý gửi người dùng: đã chỉ còn tình huống, hành động và danh sách `Field = giá trị` chưa, hay vẫn còn số field, cơ chế, field để mặc định?
   - Tin nhắn Zalo hoặc Teams: có bullet nào là một câu nói với người đọc không? Tên field, tên trang có bị dịch sang tiếng Việt không, trang cần mở đã ghi kèm status chưa? Câu cuối có đang nhắc lại cái lợi mà người hỏi đã biết không?
   - Định dạng có khớp phần còn lại của tài liệu và file gốc của khách không?
5. **Lượt rà hình thức**: in đậm, bullet, heading, gạch ngang dài, nháy cong, emoji, mũi tên, dấu chấm phẩy, bảng thừa, quy ước màu ô trong file Excel. Với file Excel còn thêm: bốn dòng đầu của các sheet có giống nhau không, ô nào phải quấn dòng vì câu quá dài, cột nào rộng quá mức cần, nhóm cột đã phủ hết các cột chi tiết chưa.
6. **Lượt rà nhịp**: đọc to. Câu dài xấp xỉ nhau thì trộn lại. Câu ghép quá hai vế bằng "và", "đồng thời", "nhằm", "qua đó", "từ đó" thì tách ra. Ngoại lệ: câu mô tả một bước lấy dữ liệu theo nhóm 31 được giữ đủ ba vế trong một câu. Không ép câu siêu ngắn 3-5 chữ vào tài liệu kỹ thuật; thỉnh thoảng một câu ngắn là đủ để đổi nhịp.
7. **Lượt rà dữ kiện**: mọi con số, tên object, page, field đều truy được về nguồn có thật. Có source code hoặc tài liệu thì mở ra đọc, không suy luận. Không truy được thì để trống và ghi rõ chỗ cần điền.
8. **Lượt rà vết tích**: chạy checklist trong `references/dau-vet-ky-thuat.md`. Với file Excel: xuất PDF, xem ảnh từng trang, kiểm tra các ô công thức tổng hợp, và mở lại file bằng thư viện đọc sau mọi thao tác vá file. Kiểm tra đã gửi đủ bộ file chưa.

## Khi được nhờ biên tập văn bản có sẵn

Khi người dùng đưa một đoạn văn và nhờ "viết lại cho tự nhiên", "sửa văn", "cho mượt", việc cần làm là sắp xếp lại câu chữ, không phải viết thêm.

- **Giữ đúng ý và ví dụ gốc.** Không thêm dữ kiện, con số, tên riêng mà bản gốc không có.
- **Không thêm câu nhận định, câu triết lý, câu mở bài hay đoạn kết.** Bản gốc không có thì bản sửa cũng không có.
- **Không bỏ ý của người viết** chỉ vì nó nghe thô. Sửa cách nói, giữ nội dung.
- **Thấy thiếu ý hoặc ý chưa rõ thì hỏi**, hoặc ghi chú ngắn bên ngoài văn bản. Không tự lấp vào trong bản sửa.

Kiểm tra sau khi sửa: đặt hai bản cạnh nhau, đánh dấu từng ý trong bản sửa về đúng câu gốc. Ý nào không truy được về bản gốc thì xóa. Đây cũng là chỗ nhóm 4 cảnh báo: bản sửa ghi "đã bỏ giọng quảng cáo" nhưng thực tế lại thêm vào.

## Khi được nhờ soi một văn bản

Trả lời theo mức độ, không phán xanh rờn. Ba việc phải làm:

**Nêu bằng chứng cụ thể.** Trích đoạn, chỉ tên dấu hiệu, đếm số lần. Kết luận theo thang: dấu hiệu yếu (vài từ vựng lẻ), trung bình (cấu trúc lặp có hệ thống, nhiều nhóm cùng xuất hiện), mạnh (vết hội thoại sót lại, mã đánh dấu chatbot, nguồn bịa, placeholder chưa điền).

**Nói rõ giới hạn.** Bài gốc dẫn nghiên cứu cho thấy người bình thường phân biệt văn AI với văn người không hơn gì đoán mò; người dùng LLM nhiều đạt khoảng 90%, tức là cứ 10 lần khẳng định thì sai 1. Phần mềm phát hiện AI có tỉ lệ lỗi không nhỏ và bị đánh lừa bởi việc diễn đạt lại hay đổi định dạng.

**Không dùng các dấu hiệu vô hiệu**: ngữ pháp hoàn hảo, trộn giọng trang trọng với suồng sã, văn "khô như máy", văn "hàn lâm bóng bẩy", liên từ đứng lẻ, nội dung không dẫn nguồn, định dạng đúng chuẩn. Nếu người viết giải thích được vì sao họ viết vậy hoặc sai vậy, đó là bằng chứng nghiêng về phía người.

## Khi mình làm hỏng thứ đã giao

Giao một file mà người dùng mở lên không ra gì, hoặc một con số sai lọt tới tay sếp họ. Cách trả lời sai là xin lỗi dài rồi giao bản mới. Bốn việc, theo thứ tự:

- **Một câu nhận, không hai câu.** "Lỗi là do tôi" rồi đi thẳng vào nguyên nhân. Không "thành thật xin lỗi vì sự bất tiện".
- **Nguyên nhân kỹ thuật cụ thể, đủ để người đọc kiểm được.** "Bước chèn lại thiết lập nút gộp đặt thẻ sai vị trí, trong khi thứ tự bắt buộc là tabColor rồi outlinePr rồi pageSetUpPr" chứ không "có lỗi trong quá trình xử lý file".
- **Vì sao lượt kiểm trước không bắt được.** Đây là phần người đọc cần nhất, vì nó cho biết lần sau còn sót nữa không. "LibreOffice vẫn mở được nên lúc kiểm tôi không thấy."
- **Lần này kiểm thêm bằng cách nào.** Nêu đúng các bước đã chạy, không hứa suông là sẽ cẩn thận hơn.

Không gộp phần này vào cùng một câu với phần mô tả bản mới. Sửa lỗi xong thì nói lỗi, rồi mới nói bản mới có gì.

## Khi so bản người dùng sửa tay với bản mình giao

Người dùng gửi lại file đã chỉnh là nguồn học tốt nhất, vì nó cho biết cái gì bị sửa chứ không phải cái gì đáng lẽ nên sửa. Cách đọc:

- **So cả giá trị lẫn định dạng.** Lần so bản WBS ACP chỉ có 15 ô đổi nội dung, nhưng phần định dạng mới là chỗ nhiều bài học: đường kẻ thiếu ở một sheet, chiều cao dòng dư, nhóm cột phủ thiếu hai cột.
- **Bỏ qua nhiễu do phần mềm lưu lại.** Excel lưu lại file thì canh lề `general`/`bottom` và `wrap_text` đổi từ None sang False ở hàng nghìn ô. Lọc theo font, màu nền, số định dạng và canh lề ngang để còn lại các sửa thật.
- **Đọc hướng của các sửa, không chỉ từng sửa.** Bốn ô bị cắt đuôi câu, một dòng bị xóa, một tên công việc bị rút gọn: cùng một hướng là bỏ phần giải thích thừa. Ghi lại hướng đó chứ đừng ghi bốn luật riêng lẻ.
- **Gom cả các phản hồi rời trong lúc làm, không chỉ bản cuối.** Một phiên dài có hàng chục câu sửa ngắn ("ko cần thêm cột đề xuất", "gom lại đi", "nghe AI quá", "ngắn gọn thôi"). Từng câu nhìn như chuyện vặt, xếp cạnh nhau mới thấy ba bốn hướng lặp lại. Hướng lặp lại mới đáng ghi vào skill; câu chỉ xuất hiện một lần thì để trong ghi chú dự án.

## Tài liệu kèm theo

- `references/cum-tu-can-tranh.md` - 11 nhóm từ và cụm từ cần tránh, tách tiếng Việt và tiếng Anh, kèm phương án thay thế: từ hoa mỹ, vết hội thoại, tên định danh bị dịch, thuật ngữ tự chế, ẩn dụ tiêu đề, nhãn mang giọng phán xét, rào đón chồng. Đọc khi biên tập văn bản dài hoặc khi cần từ thay thế cụ thể.
- `references/dau-vet-ky-thuat.md` - 9 nhóm vết định dạng và mã đánh dấu của từng chatbot, checklist tìm kiếm trước khi giao tài liệu, các lỗi trích dẫn đặc trưng, và checklist kiểm tra mất dấu tiếng Việt trong file do script sinh ra. Đọc khi dọn tài liệu, khi soi văn bản, và trước khi giao bất kỳ file nào được sinh bằng script.
- `references/vi-du-truoc-sau.md` - 16 ví dụ sửa trước/sau trong ngữ cảnh tài liệu tư vấn ERP, phủ FDD/FRD, email khách hàng và nội bộ, Quick Guide, slide, báo cáo, giải thích code cho người dùng nghiệp vụ, tài liệu bàn giao Confluence, tài liệu tích hợp gửi đối tác, tài liệu mức BA, hướng dẫn xử lý sự cố gửi người dùng, và tin nhắn Zalo hướng dẫn dùng tính năng. Đọc khi cần mẫu cụ thể cho loại tài liệu đang viết.