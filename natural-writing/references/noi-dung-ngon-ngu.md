# Nhóm 1-13: dấu hiệu về nội dung và ngôn ngữ

Đọc khi biên tập hoặc soi một đoạn văn xuôi, nhất là văn bản dài, bài chia sẻ, phần mở đầu FDD và email có câu đánh giá. Mười ba nhóm này theo bài Wikipedia:Signs of AI writing, kèm cách chữa cho tài liệu tư vấn.

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

Cách chữa: nêu đích danh ai, ở đâu, khi nào. Trong tài liệu dự án: "Chị Vy (Kế toán trưởng) nêu tại workshop ngày 12/03".

### 7. Suy đoán khi thiếu nguồn

Khi không tìm được thông tin, mô hình không im lặng mà viết rằng thông tin "không được ghi nhận rộng rãi", rồi vẫn đoán tiếp về nội dung "có khả năng" là gì. Cả hai vế đều là bịa: kể cả khẳng định rằng thông tin không tồn tại.

Trong tài liệu tư vấn, đây là dạng nguy hiểm nhất. Nếu không tra được một field, một page, một tham số, phải ghi rõ "chưa xác nhận, cần kiểm tra trên môi trường" chứ không viết một câu nghe hợp lý.

**Khi đã có source code hoặc tài liệu trong tay thì phải đọc, không được suy luận.** Lỗi này bị bắt nhiều lần ở nhiều dự án khác nhau, với cùng một phản ứng: "tôi nói bạn đọc code giải thích chứ không phải suy luận", "có đọc code không mà đưa ra gợi ý trật lất", "trên BC hiện tại làm gì có cái này, check lại code xem". Suy luận từ kinh nghiệm về cách BC thường hoạt động nghe rất trôi và sai rất khó phát hiện, vì nó đúng ở đa số trường hợp và sai đúng ở trường hợp đang hỏi. Mở file ra, tìm đúng dòng, lấy đúng tên và giá trị, rồi mới viết.

Cùng gốc: **đọc ảnh chụp tin nhắn bị cắt rồi tự điền phần còn thiếu.** Một dòng Zalo bị cắt ngang được đọc thành "Khách A không gỡ" rồi dựng cả lập luận lên đó, trong khi ý thật là NaviWorld vẫn tham gia chuyển tồn và go-live, đang chờ hãng trả lời. Câu bị cắt thì hỏi lại, không đoán.

Một biến thể hay gặp: thấy trong code có cờ hoặc trường mang tên gợi tới một chức năng thì kết luận chức năng đó đang chạy. Có cờ `"Show on COA"` không có nghĩa là có mẫu in giấy chứng nhận chất lượng. Phải tìm tiếp xem có report nào in không, có layout nào không. Không có thì viết thẳng là chưa có, và đó là yêu cầu mới chứ không phải chuyển chỗ làm.

Cùng gốc, khi viết nhãn và hướng dẫn cho từng trường trong file data migration (02/10/2026). Trường `Level` của LSC Store Group Setup bị dịch theo caption thành "Cấp", kèm mô tả "Tự lấy theo nhóm". Định nghĩa trường trong table nói khác: chỉ `Type` tự điền (`Editable = false`, gán trong `OnValidate` của `Store Group`), còn `Level` do người dùng nhập. PM đổi nhãn thành "Thứ tự ưu tiên", và code xác nhận đúng như vậy: Item Distribution sắp nhóm cửa hàng theo `Level` giảm dần rồi lấy nhóm đầu tiên có thiết lập (nhóm 24). Mô tả một trường cho người điền thì mở định nghĩa trường trong table trước (Editable, OnValidate, TableRelation), rồi tìm chỗ code dùng trường đó. Caption và tooltip chỉ là điểm bắt đầu.

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
