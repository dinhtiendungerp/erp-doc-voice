---
name: natural-writing
description: Viết và biên tập văn bản sao cho không mang dấu vết văn AI, cho cả tiếng Việt và tiếng Anh. Gồm 29 nhóm dấu hiệu - 13 nhóm theo Wikipedia:Signs of AI writing và 16 nhóm riêng cho tài liệu kỹ thuật (chôn kết luận, trả lời dài hơn câu hỏi, dịch tên định danh trong code thành chữ của mình, tự chế thuật ngữ, ẩn dụ làm tiêu đề, viết sai tầm người đọc, email viết như tài liệu, đề xuất vượt phạm vi được hỏi). LUÔN dùng khi sinh ra bất kỳ đoạn văn xuôi nào cho người đọc - email, FDD/FRD, Quick Guide, biên bản, đề xuất, nội dung slide, tài liệu bàn giao, báo cáo, tài liệu training, commit message - kể cả khi người dùng không nhắc tới văn phong. Cũng dùng khi người dùng nói "viết lại cho tự nhiên", "nghe AI quá", "đừng dùng mấy từ AI", "bỏ giọng AI", "humanize", "ngắn gọn thôi", "dài dòng quá", "lòng vòng quá", "rà văn phong", đưa một đoạn văn nhờ biên tập, nhờ soi xem văn bản có dấu hiệu AI không, hoặc dọn văn bản dán từ chatbot sang Word, Confluence, Excel hay PowerPoint.
---

# Viết như người, không như máy

## Nguyên tắc quan trọng nhất

Bài gốc mở đầu bằng một cảnh báo mà hầu hết bản tóm tắt trên mạng bỏ qua: **các dấu hiệu liệt kê ra là triệu chứng, không phải căn bệnh.** Sửa triệu chứng mà giữ nguyên bệnh chỉ làm văn khó bị phát hiện hơn chứ không tốt hơn.

Căn bệnh là gì? Mô hình ngôn ngữ đoán từ tiếp theo theo xác suất, nên nó **kéo mọi chủ đề về mức trung bình**: chi tiết riêng, hiếm, cụ thể bị thay bằng phát biểu chung chung, tích cực, đúng với mọi chủ đề. Bài gốc ví như tấm chân dung đang mờ dần từ ảnh chụp sắc nét thành phác thảo chung chung, trong khi lời chú thích lại hô to hơn rằng đây là nhân vật đặc biệt. Chủ thể vừa mờ đi vừa được thổi phồng lên.

Vì vậy tiêu chí số một khi rà một đoạn văn không phải "có từ cấm không" mà là:

> Câu này thêm dữ kiện, con số, tên riêng, điều kiện, hệ quả cụ thể nào mà câu trước chưa có? Nếu không, xóa.

Và câu kiểm tra cuối cùng cho cả đoạn: **dán nguyên đoạn này sang tài liệu của một dự án khác, khách hàng khác, sản phẩm khác mà vẫn đúng không?** Nếu vẫn đúng, viết lại.

## Cách hiệu chỉnh mức độ

Bài gốc nói rõ: không dấu hiệu đơn lẻ nào là bằng chứng. Người viết thật cũng dùng gạch ngang dài, cũng liệt kê ba ý, cũng viết "tuy nhiên". Bản thân trang thảo luận của bài có biên tập viên nói rằng gạch ngang dài giờ không còn đáng để soi nữa. Sức mạnh nằm ở **mật độ và tổ hợp**, không ở từng dấu hiệu.

Hệ quả cho việc viết: **ưu tiên diệt câu rỗng và cấu trúc lặp; nới tay với từ vựng đơn lẻ.** Một chữ "quan trọng" đặt đúng chỗ không sao. Ba đoạn liên tiếp mở đầu bằng "Bên cạnh đó" mới là vấn đề.

Cảnh báo ngược cũng nằm trong bài: nếu né sạch mọi thứ trong danh sách, câu văn sẽ cụt lủn và đều tăm tắp, mà kiểu gượng đó cũng là một dấu vết. Chỉ nên ép chặt vài thứ, phần còn lại xử lý bằng biên tập.

## Các nhóm dấu hiệu về nội dung

### 1. Thổi phồng ý nghĩa, di sản, xu thế

Gán tầm quan trọng lớn cho việc bình thường, hoặc nối chủ đề vào một bức tranh rộng hơn mà không có nguồn. Bài gốc ghi nhận mô hình làm điều này ngay cả với chủ đề tầm thường như từ nguyên hay số liệu dân số, đôi khi còn rào trước rằng chủ đề không mấy quan trọng rồi vẫn nói về tầm quan trọng của nó.

- Sai: Tính năng này đóng vai trò then chốt, khẳng định vị thế của LS Central trong ngành bán lẻ.
- Đúng: Tính năng này cho phép POS hoạt động offline tối đa 72 giờ.

Một biến thể: đặt chủ thể vào giữa các "cuộc tranh luận rộng hơn" hoặc nói rằng nó "đặt ra câu hỏi" về điều gì đó lớn lao.

Cách chữa: thay mệnh đề đánh giá bằng dữ kiện kiểm chứng được. Không có dữ kiện thì bỏ câu.

### 2. Nhấn mạnh có sẵn khuôn về mức độ được công nhận

Đây là nhóm bài gốc ghi nhận là **đặc trưng của các mô hình từ 2025 trở đi**, và tôi đã bỏ sót ở bản trước. Thay vì trình bày nội dung, văn AI chứng minh chủ thể đáng chú ý bằng cách liệt kê nó đã xuất hiện ở đâu và loại nguồn nào: "được đưa tin trên nhiều báo lớn", "được các tạp chí chuyên ngành nhắc đến", "duy trì sự hiện diện tích cực trên mạng xã hội".

Trong bối cảnh tư vấn, nhóm này biến thành: "giải pháp được nhiều doanh nghiệp lớn tin dùng", "được đánh giá cao trên các diễn đàn", "đã được triển khai rộng rãi". Nói về việc có nguồn thay vì nói nội dung nguồn đó chứa gì.

Cách chữa: nêu thẳng nội dung. Không phải "được nhiều khách hàng đánh giá cao" mà "ba khách hàng ngành F&B đang chạy module này từ 2024".

### 3. Phân tích rỗng ở đuôi câu

Mệnh đề phân từ bám đuôi để bình luận về ý nghĩa: "qua đó giúp tối ưu quy trình", "từ đó nâng cao trải nghiệm", "góp phần khẳng định", "ensuring seamless integration", "highlighting its importance", "reflecting the commitment".

Bài gốc lưu ý mô hình mới có tìm kiếm web sẽ gắn những nhận định này vào một nguồn có tên thật, bất kể nguồn đó có nói gì gần với vậy hay không. Đây là chỗ nguy hiểm: nhìn có vẻ được dẫn nguồn tử tế.

- Sai: Hệ thống cho phép in tem tại kho, qua đó giúp nâng cao hiệu quả vận hành.
- Đúng: Hệ thống cho phép in tem tại kho, bỏ được bước dán tem thủ công ở khâu đóng gói.

### 4. Giọng quảng cáo

Văn kỹ thuật trượt sang giọng brochure du lịch hoặc thông cáo báo chí. Bài gốc nêu điều đáng chú ý: hiện tượng này xảy ra ngay cả khi đã yêu cầu giọng trung tính, và có trường hợp bản sửa ghi là "đã bỏ giọng quảng cáo" nhưng thực tế lại thêm vào.

Cách chữa: hỏi "ai đo được điều này?". "Liền mạch" không đo được. "Đồng bộ tồn kho trong vòng 5 phút" đo được.

### 5. Biên tập hộ người đọc

"Điều quan trọng cần lưu ý là", "Đáng chú ý rằng", "Không thể không nhắc đến", "It is worth noting that". Xóa vế mở đầu, giữ nội dung. Nếu nội dung quan trọng thật thì vị trí của nó trong bài đã nói lên điều đó.

### 6. Quy chiếu mơ hồ và phóng đại số nguồn

"Nhiều chuyên gia cho rằng", "theo các báo cáo ngành", "giới chuyên môn nhận định". Ngoài việc mơ hồ, bài gốc chỉ ra một lỗi nữa: **phóng đại số lượng nguồn**. Trình bày quan điểm của một nguồn như thể là quan điểm phổ biến, nhắc tới "các nhà nghiên cứu" trong khi chỉ dẫn một người, hoặc dùng "chẳng hạn như" trước một danh sách thực chất đã liệt kê hết.

Cách chữa: nêu đích danh ai, ở đâu, khi nào. Trong tài liệu dự án: "Chị Hà (Kế toán trưởng) nêu tại workshop ngày 12/03".

### 7. Suy đoán khi thiếu nguồn

Khi không tìm được thông tin, mô hình không im lặng mà viết rằng thông tin "không được ghi nhận rộng rãi", rồi vẫn đoán tiếp về nội dung "có khả năng" là gì và vì sao nó quan trọng. Cả hai vế đều là bịa: kể cả khẳng định rằng thông tin không tồn tại.

Trong tài liệu tư vấn, đây là dạng nguy hiểm nhất. Nếu không tra được một field, một page, một tham số, phải ghi rõ "chưa xác nhận, cần kiểm tra trên môi trường" chứ không viết một câu nghe hợp lý.

**Khi đã có source code hoặc tài liệu trong tay thì phải đọc, không được suy luận.** Đây là lỗi bị bắt hai lần ở hai dự án khác nhau, với cùng một phản ứng: "tôi nói bạn đọc code giải thích chứ không phải suy luận" và "có đọc code không mà đưa ra gợi ý trật lất". Suy luận từ kinh nghiệm về cách BC thường hoạt động nghe rất trôi và sai rất khó phát hiện, vì nó đúng ở đa số trường hợp và sai đúng ở trường hợp đang hỏi. Mở file ra, tìm đúng dòng, lấy đúng tên và giá trị, rồi mới viết.

### 8. Kết luận kiểu dàn ý về "thách thức và triển vọng"

Khuôn: "Dù có [loạt từ tích cực], [chủ thể] vẫn đối mặt một số thách thức..." rồi kết bằng đánh giá lạc quan mơ hồ hoặc suy đoán về các sáng kiến tương lai. Thường nằm cuối tài liệu có cấu trúc cứng nhắc, đôi khi thêm hẳn một mục "Triển vọng tương lai".

Bài gốc nhấn: dấu hiệu nằm ở **cái khuôn**, không phải ở việc nhắc tới khó khăn. Nói về rủi ro dự án là chuyện bình thường và cần thiết. Vấn đề là mục rủi ro không nêu rủi ro nào cụ thể.

## Các nhóm dấu hiệu về ngôn ngữ

### 9. Song song phủ định

"Không phải X, mà là Y" và "Không chỉ X mà còn Y". Có thể trải qua hai câu: câu đầu nêu một điều, câu sau lật lại bằng "tuy nhiên". Grok còn hay dùng dạng đảo ngược: "X chứ không phải Y".

- Sai: Đây không đơn thuần là một bản nâng cấp, mà là một thay đổi về cách vận hành.
- Đúng: Bản nâng cấp này đổi cách tính giá vốn, nên kế toán phải chốt tồn trước khi chạy.

Giữ tối đa một lần trong cả tài liệu, khi phép tương phản thật sự cần thiết.

### 10. Né động từ "là" và "có"

Nhóm này tôi bỏ sót ở bản trước, và nó là một trong những dấu hiệu định lượng được rõ nhất. Một nghiên cứu bài gốc dẫn cho thấy tần suất "is"/"are" trong văn học thuật giảm hơn 10% trong năm 2023, và khi cho mô hình sửa lại 10.000 tóm tắt, hai từ này xuất hiện ít hơn hẳn.

Mô hình thay câu đơn giản bằng câu trang trọng hơn:

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

Lưu ý hiệu chỉnh: bài gốc xếp "liên từ đứng riêng lẻ" vào nhóm **dấu hiệu không đáng tin**, vì văn nghị luận của người cũng dùng nhiều và nhiều sách văn phong chấp nhận. Chỉ đáng ngờ khi lặp thành nhịp.

## Các nhóm dấu hiệu riêng của tài liệu kỹ thuật

Nhóm này rút ra từ chính các lần bị trả bài trong dự án. Chúng không nằm trong bài Wikipedia gốc vì bài đó viết cho văn bách khoa, nhưng trong tài liệu tư vấn và hướng dẫn kỹ thuật thì đây mới là các lỗi bị bắt nhiều nhất.

### 14. Chôn kết luận xuống dưới

Mở đầu bằng nguồn, bằng bối cảnh, bằng "hai cơ chế khác nhau", rồi mới tới câu trả lời. Người đọc đọc hết vẫn không biết câu trả lời là gì. Đây là lỗi thứ tự thông tin, không phải lỗi từ ngữ, nên rà từ vựng không phát hiện ra.

- Sai: mở bằng mục "Nguồn code", rồi bảng số, rồi mới tới kết luận về việc phần lẻ rơi vào dòng nào.
- Đúng: câu đầu tiên nói thẳng "Code không có bước dồn phần lẻ vào một dòng. Nó tính lần lượt từng dòng theo Line No., dòng cuối nhận nguyên phần còn lại." Dẫn chứng và bảng số xuống sau.

Quy tắc: câu đầu tiên phải là câu trả lời. Nếu người đọc chỉ đọc một câu rồi bỏ, câu đó phải đủ.

### 15. Trả lời dài khi câu hỏi hẹp

Được hỏi một câu có đáp án ngắn, trả về một báo cáo bốn mục. Câu hỏi "Created By trên BC bây giờ là user nào" cần một bảng hai dòng, không cần phần phương án, phần đã làm, phần giới hạn.

Cách chữa: trả lời đúng câu được hỏi trước, hết một câu hoặc một bảng nhỏ. Phần bối cảnh chỉ thêm khi nó đổi câu trả lời, và luôn đứng sau.

### 16. Dịch tên định danh kỹ thuật thành chữ của mình

Đây là lỗi nặng nhất trong nhóm này vì nó phá khả năng truy nguồn, và nhiều lần kéo theo mô tả sai.

| Viết sai | Viết đúng |
|---|---|
| Round(..., 1 đồng) | `Currency."Amount Rounding Precision"` |
| tăng trường version | sửa số ở dòng `version` lên cao hơn số đang cài |
| page hộp duyệt | page phiếu chờ duyệt (`approvalInbox`) |
| Trường lệnh actionCode | `actionCode` |
| Trường trạng thái nút | các trường `canXxx` |
| Trình kết nối ánh xạ entity set thế nào | mỗi entity set là một nguồn dữ liệu riêng |

Trường hợp "1 đồng" cho thấy hậu quả: viết tắt tham số thành cách nói dân dã làm người đọc tưởng dòng đầu tiên không áp tham số đó, trong khi code áp cho cả ba dòng.

Quy tắc: tên field, tên page, tên tham số, tên biến trong code thì giữ nguyên tên thật, đặt trong code format. Cần một cách gọi tiếng Việt cho dễ đọc thì đặt tên mô tả rồi để tên thật trong ngoặc ngay sau, như "page phiếu chờ duyệt (`approvalInbox`)", chứ không thay hẳn tên thật. Muốn giải thích thì viết thêm một mệnh đề sau tên thật, không thay thế nó. Khi đọc code để giải thích, lấy đúng tên và giá trị trong code, không suy luận rồi đặt tên mới.

### 17. Ẩn dụ văn chương làm tiêu đề mục

Tiêu đề mượn hình ảnh nghe kêu nhưng người đọc không biết mục đó nói gì.

- "Giải phẫu một API page" → "Đọc một API page: từng thuộc tính làm gì"
- "Hợp đồng của Custom API" → "Custom API nhận gì, trả gì"

Cùng loại: "bức tranh toàn cảnh", "trái tim của hệ thống", "xương sống", "hành trình dữ liệu", "dưới nắp capo", "bản đồ tài liệu". Tiêu đề trong tài liệu kỹ thuật nên nói thẳng nội dung mục, dạng câu hỏi người đọc đang có trong đầu thì càng tốt.

Ẩn dụ trong thân bài cũng vậy, và đây là chỗ hay sót vì nó nằm lẫn giữa câu:

- "Đối tượng ngoài cụm phải sửa phẫu thuật" → "Hai mươi đối tượng ngoài cụm MobileWMS phải sửa trong file"
- "khóa được phạm vi" → "chốt được phạm vi"
- "Nội dung tích hợp gói gọn ở sáu thông tin" → "Dữ liệu trao đổi gồm sáu thông tin"

### 18. Hệ quả trừu tượng thay vì hiện tượng quan sát được

Viết cái kết luận trừu tượng thay vì viết cái người đọc sẽ nhìn thấy trên màn hình.

- Sai: "Thiếu một trong hai thì extension không biên dịch được."
- Đúng: "Thiếu một trong hai gói này thì lệnh build báo lỗi thiếu symbol ngay dòng đầu."

Câu đúng cho người đọc biết họ sẽ thấy gì và tìm gì. Câu sai chỉ cho biết một phán quyết. Hỏi kiểm tra: người đọc gặp tình huống này thì nhìn thấy chính xác cái gì, ở đâu?

### 19. Tài liệu hướng dẫn viết theo lối giải thích

Bài giải thích kỹ nhưng đọc vô không biết phải làm gì trước, làm gì sau. Đúng nội dung, sai thể loại.

Với Quick Guide, tài liệu bàn giao, hướng dẫn cài đặt: tách Phần A các bước làm lên trước, Phần B tham chiếu xuống sau. Mở đầu bài bằng một bảng ngắn "cần gì thì đọc mục nào". Người đọc tài liệu hướng dẫn đang muốn làm xong việc, không muốn hiểu toàn bộ hệ thống.

### 20. Tự chế thuật ngữ nghiệp vụ

Khác nhóm 16 ở chỗ: nhóm 16 là dịch tên định danh có sẵn trong code, nhóm này là tự nghĩ ra một từ tiếng Việt nghe hợp lý cho một khái niệm mà trong nghề đã có cách gọi riêng. Người đọc phải dừng lại đoán, và thường đoán sai.

| Tự chế | Từ thật sự dùng |
|---|---|
| bản tin, bản tin pallet, bộ bản tin chuẩn | message, message pallet, bộ message chuẩn |
| đặc tả bản tin | tài liệu đặc tả tích hợp |
| Mã bản tin gần nhất | Mã message cập nhật gần nhất |
| Hệ chủ | Nguồn dữ liệu |
| Đầu pallet / Dòng pallet | Pallet / Chi tiết pallet |
| Ảnh chụp tồn kho (Inventory snapshot) | Số tồn tại thời điểm chốt |
| Luật kiểm soát | Quy tắc kiểm soát |
| di trú dữ liệu, trích xuất và lưu trữ | chuyển dữ liệu, trích ra file lưu |
| BẢN ĐỒ TÀI LIỆU | NỘI DUNG TÀI LIỆU |
| tài khoản dịch vụ | tài khoản |

Không có quy tắc cứng là giữ tiếng Anh hay dịch sang tiếng Việt. Quy tắc là **dùng đúng từ người trong nghề và khách hàng đang dùng**. "message" giữ tiếng Anh vì cả team gọi vậy. "ảnh chụp tồn kho" phải bỏ vì đó là bản dịch chữ của snapshot, không ai nói thế, thay bằng mô tả thật là "số tồn tại thời điểm chốt".

Hai lỗi phụ hay đi kèm:

- **Từ nghe nặng hơn mức cần.** "luật" thay cho "quy tắc", "di trú" thay cho "chuyển".
- **Thêm chữ chính xác hóa không cần thiết.** "tài khoản dịch vụ" trong khi "tài khoản" đã đủ hiểu và không sai.

Kiểm tra: nói từ này ra trong cuộc họp với khách, họ có gật đầu ngay không, hay phải hỏi lại đó là gì?

### 21. Viết sai tầm người đọc

Cùng một nội dung nhưng người đọc khác nhau thì mức chi tiết kỹ thuật phải khác. Đây là chỗ nhóm 16 dễ bị áp dụng nhầm.

- **Tài liệu cho dev, KB kỹ thuật, hướng dẫn cài đặt**: giữ nguyên tên object, tên field, tên page, tên tham số. Áp nhóm 16.
- **Tài liệu cho BA và consultant**: nói ở mức giải pháp. Được nhắc tên bảng, tên field, tên page vì đó là ngôn ngữ chung với dev, nhưng **không đưa cú pháp AL và không dùng code block**. Thay định nghĩa object bằng bảng mô tả nghiệp vụ dạng "Cột thêm | Dùng để | Ví dụ".
- **Tài liệu cho PM, khách hàng, ban lãnh đạo**: bỏ tên object, mô tả theo nhóm chức năng nghiệp vụ và theo khối lượng công việc.

Ví dụ cùng một sự việc:

| Cho dev | Cho PM |
|---|---|
| Cod65637 Split QC Order dùng trực tiếp bảng MOB License Plate Content | gói QC đang gắn trực tiếp vào cấu trúc dữ liệu pallet của Tasklet |
| 8 đối tượng tableextension/pageextension extends MOB… | khối chức năng kho dựng trên nền Tasklet |
| 67 event subscriber | khoảng 8% khối lượng tùy biến có liên kết tới Tasklet |

Ví dụ mức BA:

| Viết sai (cú pháp AL) | Viết đúng (mức giải pháp) |
|---|---|
| Table "ABC ESS Print Document" (header) / Print Doc No. Code[20] -- No. Series riêng / Source Table No. Integer -- 32 (ILE), 110 (Sales Shpt Hdr) | bảng mô tả: Cột thêm \| Dùng để \| Ví dụ, với dòng "Kho đi / Kho đến \| Riêng cho Transfer \| SX đến VT khác VT đến SX" |
| codeunit 74110 "ABC ESS e-Sign Facade" { procedure Sign(var RecRef: RecordRef) … } | mô tả điểm vào chung cho các chứng từ ký, không viết chữ ký hàm |

Hỏi trước khi viết: ai ký vào tài liệu này, và họ cần con số nào để ra quyết định?

### 22. Giọng bắt bẻ đối tác

Trong tài liệu gửi khách hàng hoặc đối tác, việc chỉ ra chỗ chưa khớp trong tài liệu của họ dễ trượt thành giọng vạch lỗi, nhất là khi hai bên chưa chốt gì cả.

- Sai: "Đề xuất Infolog ghi Go-live Week 23 nhưng UAT ở Week 27-32 và tổng 7-8 tháng, cần Infolog làm rõ mốc thật."
- Đúng: đưa vào mục "Điểm cần thống nhất về lịch", nêu là điểm cần làm rõ khi chốt lịch chung.

Cùng cách chữa: nhãn "Vấn đề phát hiện" đổi thành "Điểm cần làm rõ", tên sheet "Vấn đề và câu hỏi tiến độ" đổi thành "Điểm cần thống nhất về lịch". Nội dung giữ nguyên, chỉ đổi khung từ phán xét sang cùng chốt.

### 23. Rào đón tự hạ giá trị nội dung mình vừa viết

Rào đón đúng mức là cần thiết khi chưa có estimate. Nhưng thêm một vế phủ định chính mình thì người đọc không còn lý do gì để đọc phần bên dưới.

- Sai: "đây mới là hướng sơ bộ ... Phương án chính thức phải đợi đội dev phân tích và estimate xong mới chốt được, **và lúc đó có thể khác với những gì em mô tả bên dưới**."
- Đúng: "đây là hướng tiếp cận sơ bộ, đưa ra để anh và bộ phận kho có cơ sở chọn mục tiêu trước. Còn cách làm cụ thể và chi phí thì phải đợi đội dev phân tích, estimate xong mới chốt được."

Bản đúng vẫn rào đủ, nhưng nói rõ phần sơ bộ này dùng để làm gì. Rào một lần, không rào chồng.

Cùng nhóm, ở đầu câu trả lời: "Đúng, bạn chỉ ra một lỗ hổng thật của thiết kế hiện tại". Bỏ vế khen, vào thẳng câu trả lời.

### 24. Rút gọn tới mức mất nghĩa

Yêu cầu ngắn gọn áp cho câu văn, không áp cho nhãn và tiêu đề cột. Nhãn phải đủ nghĩa khi đứng một mình, vì người đọc bảng không đọc câu dẫn phía trên.

- Sai: tiêu đề cột "Ghi phần"
- Đúng: "Phần sản lượng được ghi nhận ở mức này"

### 25. Định nghĩa trừu tượng thay vì ví dụ số cụ thể

Khi người đọc nói "vẫn không hiểu", thường không phải vì câu khó mà vì chưa có số để bám vào.

- Sai: "Posting Date là ngày ghi nhận, quyết định kỳ tính thưởng. Document Posting Date là ngày thật của chính chứng từ nguồn của dòng đó, chỉ để đối chiếu. Ý nghĩa của cặp này là cho thấy độ lệch..."
- Đúng: dựng ví dụ có mã và ngày thật (BSO-101 ngày 05/07, SO-9001 ngày 20/07), kẻ bảng bốn dòng, chốt bằng một câu: "Nói gọn: Posting Date lấy ngày BSO, Document Posting Date lấy ngày SO."

Công thức: một ví dụ số có tên thật, một bảng nhỏ, một câu chốt.

### 26. Email viết như tài liệu

Email và tài liệu là hai thể loại khác nhau. Email có heading đánh số, có sáu mục, có danh sách tám câu hỏi thì không ai đọc.

Với email: bỏ heading, viết thành đoạn văn liền mạch, giữ đúng phần phản biện và đề xuất bước tiếp theo, tối đa ba bốn câu hỏi. Phần chi tiết để dành cho FDD và nói rõ là sẽ có trong FDD.

Giọng cũng khác: email dùng giọng nói chuyện với người thật, có "nhờ anh tạo giúp em", "nhé ạ", "anh cho em xin thêm", "Có gì chưa rõ anh cứ trao đổi lại với em". Kết thư ngắn, không dựng khối chữ ký trang trọng.

Chi tiết văn phong email xem skill `mail-voice`.

### 27. Không đồng bộ với phần còn lại của tài liệu

Viết thêm một mục vào tài liệu có sẵn thì mục đó phải theo đúng quy ước đang dùng, không tự dựng cấu trúc riêng.

Ví dụ đã gặp: mục 12 của FDD dùng Heading 4 và Heading 5 làm nhãn phụ, đoạn đánh số tay "1. 2. 3.", khối công thức căn bằng dấu cách, trong khi mục 1 đến 11 dùng đoạn in đậm làm nhãn phụ và bullet gạch đầu dòng.

Trước khi viết thêm vào tài liệu có sẵn: mở một mục cũ ra xem họ dùng gì cho nhãn phụ, cho danh sách, cho bảng, rồi theo đúng như vậy.

### 28. Đề xuất vượt xa phạm vi được hỏi

Khác nhóm 15 ở chỗ: nhóm 15 là trả lời dài, nhóm này là đề xuất to. Được hỏi cách làm một việc cụ thể thì trả về kiến trúc bốn trụ cột kèm lộ trình năm giai đoạn. Người đọc không đánh giá được là nó có hiệu quả không, nên không dùng được gì cả.

- Sai: bốn trụ ("Thay Document Type enum bằng e-Sign Document Profile", "Sign Rule Matrix", "Tách đối tượng ký khỏi bản ghi BC", "Generic action surface") kèm ba bảng cấu trúc dữ liệu, khi câu hỏi chỉ là ký được trên Posted Sales Shipment.
- Đúng: một phương án tối thiểu, phạm vi nhỏ, làm được ngay, đúng đối tượng được hỏi.

Quy tắc: trả lời đúng phạm vi được hỏi trước. Nếu thấy có hướng tổng quát hơn thì nói một câu ở cuối rằng có hướng đó, để người đọc tự quyết có muốn nghe không. Không dựng sẵn cả kiến trúc rồi mới hỏi.

### 29. Đưa giải pháp khi chỉ được yêu cầu mô tả hiện trạng

Tài liệu mô tả bối cảnh và nhu cầu là một thể loại riêng, thường viết để chuyển cho người khác thiết kế giải pháp. Chen đề xuất vào đó làm hỏng mục đích của nó và ràng người đọc sau vào một hướng chưa ai chốt.

Dấu hiệu nhận ra trong bản nháp: "Tôi khuyên đổi key thành...", "Tôi khuyên bỏ, vì...", các bảng field kiểu "Field | Kiểu | Lookup | Ghi chú".

Tài liệu mô tả đúng chỉ có bốn phần: hệ thống hiện có, hiện trạng tại khách hàng, nhu cầu, và dữ kiện đã kiểm chứng kèm câu hỏi chưa có đáp án. Mở đầu nói thẳng phạm vi: "Tài liệu này chỉ mô tả hiện trạng và nhu cầu, không đề xuất giải pháp."

Chỗ nào chưa kiểm chứng được thì đưa vào mục câu hỏi chưa có đáp án, không lấp bằng một đề xuất.

## Dấu hiệu về hình thức

Nhóm này dễ sửa nhất và cũng lộ nhất. Chi tiết kỹ thuật đầy đủ nằm ở `references/dau-vet-ky-thuat.md`.

- In đậm rải khắp nơi, đặc biệt là in đậm mọi lần xuất hiện của một thuật ngữ. Quy tắc đang áp: **chỉ in đậm ở nhãn đầu mục và phần dẫn đầu bullet** dạng "Bước 1 - ", "H1 - ". Không in đậm giữa câu trong đoạn văn, không in đậm trong ô bảng.
- Bullet dạng "**Thuật ngữ:** câu giải thích lặp lại chính thuật ngữ đó". Bài gốc gọi đây là danh sách có tiêu đề nội dòng, và ghi nhận nó gần như không tồn tại trong văn người viết.
- Danh sách ở chỗ hai câu văn xuôi là đủ.
- Heading Title Case tiếng Anh; heading rập khuôn: "Thách thức", "Triển vọng", "Kết luận", "Key Features".
- Emoji trong tiêu đề hoặc đầu bullet.
- Gạch ngang dài `—` ở chỗ dấu phẩy, ngoặc đơn hoặc hai chấm hợp hơn. Đặc điểm nhận dạng cụ thể: mô hình thường đặt **dấu cách hai bên** gạch ngang dài, trái với quy ước sắp chữ mà người quen dùng gạch ngang dài đều biết. Ngược lại, mô hình lại bỏ qua gạch nối ngắn `–` ở chỗ cần nó, ví dụ khoảng năm hay tỉ số.
- Dấu nháy cong `’ “ ”` lẫn vào văn thuần. Lưu ý: đây là dấu hiệu yếu, vì Word và macOS tự đổi nháy thẳng thành nháy cong, và nhiều nhà xuất bản dùng nháy cong theo chuẩn. Bài gốc cũng ghi nhận Gemini và Claude thường không dùng nháy cong.
- Bảng nhỏ không cần thiết, chỗ hai câu văn là đủ.
- Nhảy cấp heading (bắt đầu từ cấp 3), hoặc chèn đường kẻ ngang trước mỗi heading.
- Mọi mục trong danh sách dài xấp xỉ bằng nhau, cấu trúc song song hoàn hảo.

Với văn tiếng Việt: dùng `-` thay cho `—`, không dùng `→` và `⇒`. Thay mũi tên bằng từ nối thật, vì mũi tên giấu mất quan hệ giữa hai vế. (Trong chính tài liệu skill này, mũi tên chỉ dùng để ghi trước/sau trong ví dụ, không phải mẫu để bắt chước.)

- "Gỡ Tasklet ⇒ phải gỡ hết tham chiếu" → "Gỡ Tasklet thì phải gỡ hết tham chiếu"
- "Lệch quy đổi ⇒ lệch tồn" → "Sai quy đổi đơn vị tính dẫn tới lệch tồn"
- "đổi Lot ⇒ QC tự về HOLD" → "đổi lô thì trạng thái chất lượng tự về chờ kiểm"

## Vết tích quy trình

Nhóm này là bằng chứng gần như chắc chắn, và phải xóa sạch trước khi giao tài liệu:

- Lời hội thoại sót lại: "Hy vọng nội dung này hữu ích", "Bạn có muốn tôi bổ sung phần nào không", "Dưới đây là bản đã chỉnh sửa", "Certainly! Here's the revised version".
- Câu rào đón về giới hạn kiến thức hoặc mốc cập nhật dữ liệu.
- Placeholder chưa điền: `[Tên công ty]`, `[Insert date]`, `INSERT_URL_HERE`, ngày dạng `2025-XX-XX`.
- Mã đánh dấu nội bộ của từng chatbot lọt vào văn bản. Xem `references/dau-vet-ky-thuat.md` để biết mã của từng loại và cách tìm.
- **Sửa văn phong nhưng chỉ sửa một nơi.** Với tài liệu sinh bằng script, cùng một cụm từ thường nằm ở nhiều file nguồn: file nội dung (`content.json`) và chuỗi hardcode trong file dựng (`build_docx.js`, script Excel, script PPT). Sửa trong file nội dung rồi phát hành lại mà cụm từ cũ vẫn còn là do còn bản hardcode. Sau khi sửa, grep cụm từ đó trên toàn bộ file nguồn trước khi build lại.
- **Chữ tiếng Việt mất dấu trong file xuất ra.** Nội dung trong chat có dấu đầy đủ nhưng khi sinh file bằng script thì thành "PHAN BO ITEM CHARGE", "Dong thu 2 hay bi lech", tên sheet "4. VD khong deu". Lỗi nằm ở khâu sinh file chứ không phải khâu viết, nên đọc lại bản trong chat sẽ không thấy. Mở file vừa xuất ra và kiểm tra tên sheet, tiêu đề cột, phần diễn giải trước khi giao.

Bài gốc còn có một mục rất đáng học cho công việc hằng ngày: **ghi chú thay đổi**. Ghi chú do AI viết hay trấn an một cách tự giác thái quá rằng thay đổi đã "đảm bảo tuân thủ", "cải thiện tính trung lập", và hay nhắc tới cả những phần **không** bị sửa ("vẫn giữ nguyên cấu trúc cũ trong khi..."). Người viết thật ghi ngắn và cụ thể: sửa gì, ở đâu, vì sao. Áp dụng cho commit message, ghi chú phiên bản tài liệu, và email báo đã cập nhật.

## Đặc điểm văn người viết

Đây là phần hữu ích nhất của bài gốc và cũng là phần dễ bỏ qua nhất, vì nó nói cái **nên làm** chứ không phải cái nên tránh. Các đặc điểm sau phổ biến ở văn người hơn hẳn văn AI:

1. **Dùng "là" và "có" trần trụi.** "Có ba trường hợp", "Nó là bản ghi tồn kho".
2. **Dùng từ thường thay vì từ trang trọng đồng nghĩa.** "viết" thay "chấp bút", "dùng" thay "sử dụng"/"tận dụng", "thử" thay "tiến hành thử nghiệm", "chuyển" thay "di dời", "gửi" thay "tiến hành gửi". Với tiếng Việt cần cân nhắc phép lịch sự: một số từ trang trọng là bắt buộc khi viết cho khách hàng, nên áp dụng có chọn lọc.
3. **Dám nói khẳng định dứt khoát.** "chỉ có một cách", "đây là lần đầu tiên", "cách tốt nhất là". Văn AI né tuyệt đối hóa nên hay lửng lơ.
4. **Dùng từ đệm và từ nhấn.** "chắc", "hình như", "khá", "hơi", "nói chung", "thường thì". Văn AI ít khi hạ giọng kiểu này.
5. **Thỉnh thoảng viết dài dòng một cách rất người.** "do đó mà", "để mà", "cái việc là". Không cần cố tình thêm, nhưng cũng đừng cắt sạch.
6. **Nhịp câu không đều.** Câu năm chữ xen giữa câu bốn mươi chữ.

## Quy trình áp dụng

Viết trước, rà sau. Vừa viết vừa tự kiểm duyệt thì văn sẽ cụt.

1. **Viết bản thô** theo nội dung, chưa quan tâm văn phong.
2. **Lượt rà nội dung**: đọc từng câu, hỏi "câu này thêm gì?". Xóa câu rỗng. Đây là lượt quan trọng nhất và không lượt nào khác thay thế được.
3. **Lượt rà cấu trúc**: song song phủ định, bộ ba, đuôi phân từ, liên từ mở đoạn lặp, câu kết thừa, né "là"/"có", đổi tên đối tượng giữa chừng.
4. **Lượt rà thứ tự và thể loại**, với tài liệu kỹ thuật. Bảy câu hỏi, xem nhóm 14 đến 29:
   - Câu đầu đã là câu trả lời chưa?
   - Độ dài và tầm vóc đề xuất có tương xứng câu hỏi không?
   - Tên định danh có bị dịch thành chữ của mình không, có tự chế thuật ngữ không?
   - Tiêu đề mục và thân bài có ẩn dụ không?
   - Mức chi tiết kỹ thuật có đúng người đọc không: dev, BA, hay PM và khách hàng?
   - Đúng thể loại chưa: hướng dẫn thì các bước lên trước, tài liệu mô tả hiện trạng thì không chen giải pháp, email thì không dựng heading?
   - Định dạng có khớp phần còn lại của tài liệu không?
5. **Lượt rà hình thức**: in đậm, bullet, heading, gạch ngang dài, nháy cong, emoji, mũi tên, bảng thừa.
6. **Lượt rà nhịp**: đọc to. Câu dài xấp xỉ nhau thì trộn lại.
7. **Lượt rà dữ kiện**: mọi con số, tên object, tên page, tên field đều truy được về nguồn có thật. Có source code hoặc tài liệu thì mở ra đọc, không suy luận. Không truy được thì để trống và ghi rõ chỗ cần điền.
8. **Lượt rà vết tích**: chạy checklist trong `references/dau-vet-ky-thuat.md`, nhất là khi văn bản đi qua bước dán từ chatbot sang Word, Confluence hay PowerPoint, và khi tài liệu được sinh ra bằng script.

## Khi được nhờ soi một văn bản

Trả lời theo mức độ, không phán xanh rờn. Ba việc phải làm:

**Nêu bằng chứng cụ thể.** Trích đoạn, chỉ tên dấu hiệu, đếm số lần. Kết luận theo thang: dấu hiệu yếu (vài từ vựng lẻ), trung bình (cấu trúc lặp có hệ thống, nhiều nhóm cùng xuất hiện), mạnh (vết hội thoại sót lại, mã đánh dấu chatbot, nguồn bịa, placeholder chưa điền).

**Nói rõ giới hạn.** Bài gốc dẫn nghiên cứu cho thấy người bình thường phân biệt văn AI với văn người không hơn gì đoán mò; người dùng LLM nhiều đạt khoảng 90%, tức là cứ 10 lần khẳng định thì sai 1. Phần mềm phát hiện AI có tỉ lệ lỗi không nhỏ và bị đánh lừa bởi việc diễn đạt lại hay đổi định dạng. Thêm nữa, văn người đang bị ảnh hưởng ngược từ LLM nên hai bên ngày càng giống nhau.

**Không dùng các dấu hiệu vô hiệu.** Bài gốc liệt kê riêng những thứ hay bị dùng để buộc tội mà không có giá trị: ngữ pháp hoàn hảo (nhiều người viết chuyên nghiệp cũng vậy), trộn giọng trang trọng với suồng sã, văn "khô như máy", văn "hàn lâm bóng bẩy", liên từ đứng lẻ, nội dung không dẫn nguồn, và định dạng đúng chuẩn. Một dấu hiệu nữa nên nhớ: nếu người viết giải thích được vì sao họ viết vậy hoặc sai vậy, đó là bằng chứng nghiêng về phía người.

## Tài liệu kèm theo

- `references/cum-tu-can-tranh.md` - 11 nhóm từ và cụm từ cần tránh, tách tiếng Việt và tiếng Anh, kèm phương án thay thế: từ hoa mỹ, vết hội thoại, tên định danh bị dịch, thuật ngữ tự chế, ẩn dụ tiêu đề, nhãn mang giọng phán xét, rào đón chồng. Có ghi chú về việc từ vựng AI thay đổi theo từng thế hệ mô hình. Đọc khi biên tập văn bản dài hoặc khi cần từ thay thế cụ thể.
- `references/dau-vet-ky-thuat.md` - 9 nhóm vết định dạng và mã đánh dấu của từng chatbot, checklist tìm kiếm trước khi giao tài liệu, các lỗi trích dẫn đặc trưng, và checklist kiểm tra mất dấu tiếng Việt trong file do script sinh ra. Đọc khi dọn tài liệu, khi soi văn bản, và trước khi giao bất kỳ file nào được sinh bằng script.
- `references/vi-du-truoc-sau.md` - 14 ví dụ sửa trước/sau trong ngữ cảnh tài liệu tư vấn ERP, phủ FDD/FRD, email khách hàng và nội bộ, Quick Guide, slide, báo cáo, giải thích code cho người dùng nghiệp vụ, tài liệu bàn giao Confluence, tài liệu tích hợp gửi đối tác, và tài liệu mức BA. Đọc khi cần mẫu cụ thể cho loại tài liệu đang viết.
