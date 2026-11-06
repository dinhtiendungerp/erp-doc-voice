---
name: "natural-writing"
description: "Viết và biên tập văn bản sao cho không mang dấu vết văn AI, cho cả tiếng Việt và tiếng Anh. Gồm 40 nhóm dấu hiệu - 13 nhóm theo Wikipedia:Signs of AI writing và 27 nhóm riêng cho tài liệu kỹ thuật, trong đó có WBS và estimate, ngân sách và con số phái sinh, ghi chú giải thích bảng, ghi chú viết cho người lập file thay vì người nhận, email gửi kèm file, trình bày file Excel bàn giao, hướng dẫn xử lý sự cố, trả lời thắc mắc nghiệp vụ, tin nhắn Zalo hướng dẫn người dùng, khẩu ngữ lọt vào tài liệu chính thức, câu thông báo hệ thống viết tiếng Anh và tài liệu luồng tích hợp, sơ đồ trình tự. Áp dụng cho câu trả lời trong chat, file làm trong Cowork, và commit, comment, tài liệu sinh bằng script trong Claude Code. LUÔN dùng khi sinh ra văn xuôi hoặc file cho người đọc, kể cả văn bản ngắn (comment cho dev, ticket DevOps, tin Zalo, Teams, chữ trên slide, nhãn kế hoạch, tiêu đề cột, commit message) và kể cả khi người dùng không nhắc tới văn phong."
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

Skill áp cho mọi chữ người khác sẽ đọc, dài hay ngắn, nên file này đọc mỗi lần viết. Văn bản ngắn dễ bị coi là chuyện nhỏ nên bỏ qua bước rà, và đó là chỗ bị bắt "nghe AI quá" nhiều nhất.

- **Câu trả lời trong chat**: câu đầu là câu trả lời, ngắn theo đúng tầm câu hỏi (nhóm 14, 15). Báo đã sửa file thì nói sửa gì, ở đâu, trong vài dòng. Viết cùng thứ tiếng người dùng đang dùng.
- **Văn bản ngắn**: comment cho dev, ticket, tin nhắn, chữ trên slide, nhãn kế hoạch, tiêu đề cột, commit message. Một nhãn như "Cốt lõi" hay "Chưa nạp" là đủ lộ văn máy.
- **Chữ nằm trong code**: chuỗi khai trong script sinh bảng, nhãn trong file dựng Excel, câu chèn vào file Word, markdown nguồn của FDD. Chúng đi thẳng vào file giao.
- **File giao** (Excel, Word, slide, email soạn sẵn): đủ các nhóm, nhất là 26, 32 đến 37.

Phân tích, lý do, phương án và chi phí từng lựa chọn là chỗ của câu trả lời trong chat hoặc tin nhắn cho sếp. Không để chúng lọt vào file hay email gửi khách (nhóm 37). Bản đầy đủ của mục này nằm cuối `references/quy-trinh-ra.md`.

## Viết cho ai

Cùng một nội dung, người đọc khác nhau thì mức chi tiết kỹ thuật khác nhau (nhóm 21). Hỏi trước khi viết: ai ký vào tài liệu này, và họ cần con số nào để ra quyết định? Tên kỹ thuật lạ thì nói nó là gì trước, rồi mới nói nó dùng để làm gì.

| Người đọc | Viết thế nào |
|---|---|
| Dev: tài liệu kỹ thuật, KB, hướng dẫn cài đặt, ticket, tin nhắn | Giữ nguyên tên object, field, page, tham số, đặt trong code format (nhóm 16). Ticket nói làm gì và lấy từ đâu, không dẫn số dòng code, không dặn dev cách làm. Tin nhắn dùng giọng chat nội bộ và từ dev dùng. |
| BA và consultant: FDD, GAP List, Issue Log, tin nhắn nội bộ | Mức giải pháp. Được nhắc tên bảng, field, page chuẩn, nhưng không cú pháp AL, không code block, không codeunit, hàm, subscriber, mã object. Tin nhắn cho đồng nghiệp consultant thì nói bằng cơ chế BC: chứng từ, field, giá trị. |
| PM, khách hàng, ban lãnh đạo | Bỏ tên object. Nói theo nhóm chức năng nghiệp vụ, khối lượng công việc và con số họ cần để quyết định. |
| Người dùng, key user | Tình huống, hành động, `Field = giá trị`. Tên field, tên trang giữ như trên màn hình, không giải thích cơ chế (nhóm 36). |

## 40 nhóm dấu hiệu

Mỗi dòng là tên nhóm và cách chữa. Ví dụ và các lần bị bắt nằm ở file ghi trong tiêu đề.

### Nội dung và ngôn ngữ, nhóm 1-13 (`references/noi-dung-ngon-ngu.md`)
- **1. Thổi phồng ý nghĩa, di sản, xu thế**: thay câu đánh giá bằng dữ kiện kiểm chứng được.
- **2. Nhấn mạnh có sẵn khuôn về mức độ được công nhận**: nêu thẳng nội dung thay cho "được nhiều doanh nghiệp tin dùng".
- **3. Phân tích rỗng ở đuôi câu**: thay "qua đó giúp nâng cao..." bằng việc cụ thể làm được hay bỏ được.
- **4. Giọng quảng cáo**: chỉ giữ điều đo được.
- **5. Biên tập hộ người đọc**: xóa vế "điều quan trọng cần lưu ý là", giữ nội dung.
- **6. Quy chiếu mơ hồ và phóng đại số nguồn**: nêu đích danh ai, ở đâu, khi nào.
- **7. Suy đoán khi thiếu nguồn**: có code hay tài liệu thì mở ra đọc, không tra được thì ghi "chưa xác nhận".
- **8. Kết luận kiểu dàn ý về "thách thức và triển vọng"**: nêu rủi ro cụ thể, bỏ cái khuôn.
- **9. Song song phủ định**: "không phải X mà là Y" tối đa một lần trong cả tài liệu.
- **10. Né động từ "là" và "có"**: viết "là", "có", "làm" thay cho "đóng vai trò là", "sở hữu", "tiến hành thực hiện".
- **11. Tránh lặp từ một cách máy móc**: một đối tượng, một tên, dùng nguyên từ đầu đến cuối.
- **12. Bộ ba và dải giả**: đếm lại, ba mục thì cắt còn hai hoặc thêm mục thứ tư có thật.
- **13. Liên từ và câu kết lặp**: không mở đoạn đều nhịp bằng "Bên cạnh đó", không kết bằng "Tóm lại".

### Tài liệu kỹ thuật, nhóm 14-25 và 27-29 (`references/tai-lieu-ky-thuat.md`)
- **14. Chôn kết luận xuống dưới**: câu đầu tiên là câu trả lời.
- **15. Trả lời dài khi câu hỏi hẹp**: trả lời đúng câu hỏi trước, bối cảnh chỉ thêm khi nó đổi câu trả lời.
- **16. Dịch tên định danh kỹ thuật thành chữ của mình**: giữ tên field, page, bảng, tham số như trong hệ thống.
- **17. Ẩn dụ văn chương làm tiêu đề mục**: tiêu đề và thân bài nói thẳng nội dung, không "bức tranh toàn cảnh", "xương sống".
- **18. Hệ quả trừu tượng thay vì hiện tượng quan sát được**: viết điều người đọc thấy trên màn hình.
- **19. Tài liệu hướng dẫn viết theo lối giải thích**: các bước làm lên trước, phần tham chiếu xuống sau.
- **20. Tự chế thuật ngữ nghiệp vụ**: dùng đúng từ người trong nghề và khách đang dùng, bảng từ thay thế nằm ở nhóm này.
- **21. Viết sai tầm người đọc**: chọn mức kỹ thuật theo bảng "Viết cho ai".
- **22. Giọng bắt bẻ đối tác**: "Vấn đề phát hiện" đổi thành "Điểm cần làm rõ".
- **23. Rào đón tự hạ giá trị nội dung mình vừa viết**: rào một lần, không phủ định chính mình.
- **24. Rút gọn tới mức mất nghĩa**: nhãn và tiêu đề cột phải đủ nghĩa khi đứng một mình.
- **25. Định nghĩa trừu tượng thay vì ví dụ số cụ thể**: một ví dụ số có tên thật, một bảng nhỏ, một câu chốt.
- **27. Không đồng bộ với phần còn lại của tài liệu**: theo quy ước và định dạng đang có, kể cả file khách gửi.
- **28. Đề xuất vượt xa phạm vi được hỏi**: trả lời đúng phạm vi, hướng rộng hơn chỉ một câu ở cuối.
- **29. Đưa giải pháp khi chỉ được yêu cầu mô tả hiện trạng**: tài liệu mô tả không chen đề xuất.

### FDD, GAP List, Issue Log, nhóm 30, 38, 39 (`references/fdd-gap-issue-log.md`)
- **30. GAP List và FDD mức BA trượt sang giọng dev**: bỏ codeunit, hàm, subscriber, mã object khỏi phần khách đọc, Issue Log gọn hơn FDD một bậc.
- **38. Khẩu ngữ lọt vào tài liệu chính thức**: "bỏ", "gán tay", "up" đổi sang từ chuẩn, tên giao diện giữ tên nghề.
- **39. Câu thông báo của hệ thống viết bằng tiếng Anh**: theo mẫu message chuẩn của BC, thân tài liệu vẫn tiếng Việt.

### WBS, kế hoạch và file Excel, nhóm 32, 33, 35, 37 (`references/wbs-excel.md`)
- **32. Bảng phân rã công việc, ước lượng và tiến độ**: đúng bên làm, số suy ra là công thức, không sửa lịch và số của bên khác.
- **33. Ghi chú giải thích cách đọc bảng**: bỏ, để tiêu đề, cột và màu ô tự nói.
- **35. Trình bày file Excel bàn giao**: theo brandkit, khối tiêu đề thống nhất giữa các sheet, ô một dòng, cột vừa nội dung.
- **37. Ghi chú viết cho người lập file, không cho người nhận**: file và slide giao khách chỉ giữ điều người nhận phải làm hoặc phải biết. Nhãn khung câu hỏi trên slide chiếu cho khách là "Cần <khách> xác nhận", không phải câu nhắc người trình bày ("Hỏi <khách> tại slide này") hay giọng xin ("NWV mong <khách> xác nhận").

### Email và tin nhắn, nhóm 26, 34, 36 (`references/email-tin-nhan.md`)
- **26. Email viết như tài liệu**: không heading, email gửi kèm file không kể lại nội dung file.
- **34. Đoạn kết tóm tắt lại bài**: email kết bằng việc cần làm, tài liệu dừng ở mục cuối.
- **36. Hướng dẫn xử lý sự cố cho người dùng viết như báo cáo phân tích**: chỉ tình huống, hành động và `Field = giá trị`. Nhóm này có các mẫu tin Zalo, Teams đã được sửa.

### Tích hợp, nhóm 31, 40 (`references/tich-hop.md`)
- **31. Mô tả logic lấy dữ liệu vòng vo**: một câu đủ ba vế, dựa vô field nào, trên bảng nào, lấy field nào.
- **40. Tài liệu luồng tích hợp viết theo danh sách message, không theo cách người dùng làm**: đặt tên message theo đối tượng BC, tách tình huống, chia cấp message.

### Hình thức và vết tích (`references/hinh-thuc-vet-tich.md`)
- Chỉ in đậm ở nhãn đầu mục và phần dẫn đầu bullet. Không gạch ngang dài, không mũi tên `→` `⇒`, không dấu chấm phẩy, không `•` làm ký tự ngăn cách, không emoji.
- Xóa sạch vết hội thoại ("Hy vọng nội dung này hữu ích"), placeholder chưa điền, câu rào về giới hạn kiến thức.
- Bị bắt một chữ thì grep cả họ chữ đó trên mọi file nguồn. Chỉ báo xong sau khi mở lại đúng file đã lưu. Commit và ghi chú thay đổi ghi sửa gì, ở đâu, vì sao.

## Đang viết loại gì thì đọc file nào

Đọc file đúng loại trước khi viết, không đợi tới lúc rà. Các file nằm trong `references/`.

| Đang viết | Đọc |
|---|---|
| FDD, GAP List, Issue Log | `fdd-gap-issue-log.md`, thêm nhóm 16, 20, 24 ở `tai-lieu-ky-thuat.md` |
| Excel bàn giao, WBS, estimate, kế hoạch nguồn lực, data migration | `wbs-excel.md`, thêm phần lỗi công thức và thuộc tính file ở `hinh-thuc-vet-tich.md` |
| Email | nhóm 26, 34 ở `email-tin-nhan.md`, skill `mail-voice` |
| Tin Zalo, Teams, ticket DevOps, tin nhắn cho dev | nhóm 36 ở `email-tin-nhan.md`, hai mục cuối của `fdd-gap-issue-log.md` |
| Tài liệu tích hợp, đặc tả API, sơ đồ trình tự | `tich-hop.md`, thêm nhóm 20 ở `tai-lieu-ky-thuat.md` |
| Slide và file giao khách | nhóm 35, 37 ở `wbs-excel.md`, nhóm 17 ở `tai-lieu-ky-thuat.md` |
| Hướng dẫn người dùng, Quick Guide, hướng dẫn xử lý sự cố | nhóm 36 ở `email-tin-nhan.md`, nhóm 19, 25 ở `tai-lieu-ky-thuat.md` |
| Câu trả lời trong chat | nhóm 14, 15, 28 ở `tai-lieu-ky-thuat.md`, mục Phạm vi áp dụng ở `quy-trinh-ra.md` |
| Commit, comment trong code, README | mục ghi chú thay đổi ở `hinh-thuc-vet-tich.md`, mục viết cho đội phát triển ở `fdd-gap-issue-log.md` |
| Biên tập hoặc soi văn bản dài | `noi-dung-ngon-ngu.md`, `quy-trinh-ra.md`, `cum-tu-can-tranh.md` |

## Quy trình rà

Viết trước, rà sau. Vừa viết vừa tự kiểm duyệt thì văn sẽ cụt.

1. **Viết bản thô** theo nội dung, chưa quan tâm văn phong.
2. **Lượt rà nội dung**: đọc từng câu, hỏi "câu này thêm gì?". Xóa câu rỗng. Đây là lượt quan trọng nhất.
3. **Lượt rà cấu trúc**: song song phủ định, bộ ba, đuôi phân từ, liên từ mở đoạn lặp, câu kết thừa, né "là"/"có", đổi tên đối tượng giữa chừng.
4. **Lượt rà thứ tự và thể loại**: câu đầu đã là câu trả lời chưa, độ dài có đúng tầm câu hỏi không, đúng thể loại và đúng người đọc chưa. Câu hỏi riêng cho từng loại văn bản nằm ở `references/quy-trinh-ra.md`.
5. **Lượt rà hình thức**: in đậm, bullet, heading, gạch ngang dài, nháy cong, emoji, mũi tên, dấu chấm phẩy, bảng thừa. File Excel thêm bốn dòng đầu các sheet, ô quấn dòng, độ rộng cột, nhóm cột.
6. **Lượt rà nhịp**: đọc to, trộn câu dài với câu ngắn, tách câu ghép quá hai vế. Câu lấy dữ liệu theo nhóm 31 giữ đủ ba vế.
7. **Lượt rà dữ kiện**: mọi con số, tên object, page, field truy được về nguồn có thật. Có code hoặc tài liệu thì mở ra đọc, không suy luận.
8. **Lượt rà vết tích**: grep chữ tiếng Việt trong script và file nguồn, chạy checklist ở `references/dau-vet-ky-thuat.md`, mở lại file đã lưu để đọc, gửi đủ bộ file.

## Bốn tình huống riêng

Nguyên văn từng mục nằm ở `references/quy-trinh-ra.md`.

- **Khi được nhờ biên tập văn bản có sẵn**: sắp xếp lại câu chữ, không viết thêm. Giữ đúng ý và ví dụ gốc, không thêm dữ kiện, câu nhận định, mở bài hay đoạn kết, không bỏ ý chỉ vì nghe thô. Thiếu ý thì hỏi. Sửa xong, đặt hai bản cạnh nhau, ý nào không truy được về bản gốc thì xóa.
- **Khi được nhờ soi một văn bản**: trích đoạn, chỉ tên dấu hiệu, đếm số lần, rồi kết luận theo thang yếu, trung bình, mạnh. Nói rõ giới hạn của việc nhận ra văn AI, và không dựa vào dấu hiệu vô hiệu như ngữ pháp hoàn hảo hay liên từ đứng lẻ.
- **Khi mình làm hỏng thứ đã giao**: một câu nhận lỗi, rồi nguyên nhân kỹ thuật cụ thể, vì sao lượt kiểm trước không bắt được, lần này kiểm thêm bằng cách nào. Nói lỗi xong mới nói bản mới có gì.
- **Khi so bản người dùng sửa tay với bản mình giao**: so cả giá trị lẫn định dạng, lọc nhiễu do phần mềm lưu lại, đọc hướng chung của các sửa, gom cả các phản hồi rời trong phiên. Hướng lặp lại mới ghi vào skill.

## Tài liệu kèm theo

- `references/cum-tu-can-tranh.md` - 12 nhóm từ và cụm từ cần tránh, tách tiếng Việt và tiếng Anh, kèm phương án thay thế: từ hoa mỹ, vết hội thoại, tên định danh bị dịch, thuật ngữ tự chế, ẩn dụ tiêu đề, nhãn mang giọng phán xét, rào đón chồng, chữ của người dựng file lọt vào file giao khách. Đọc khi biên tập văn bản dài hoặc khi cần từ thay thế cụ thể.
- `references/dau-vet-ky-thuat.md` - 9 nhóm vết định dạng và mã đánh dấu của từng chatbot, checklist tìm kiếm trước khi giao tài liệu, các lỗi trích dẫn đặc trưng, và checklist kiểm tra mất dấu tiếng Việt trong file do script sinh ra. Đọc khi dọn tài liệu, khi soi văn bản, và trước khi giao bất kỳ file nào được sinh bằng script.
- `references/vi-du-truoc-sau.md` - 17 ví dụ sửa trước/sau trong ngữ cảnh tài liệu tư vấn ERP, phủ FDD/FRD, email khách hàng và nội bộ, Quick Guide, slide, báo cáo, giải thích code cho người dùng nghiệp vụ, tài liệu bàn giao Confluence, tài liệu tích hợp gửi đối tác, tài liệu mức BA, hướng dẫn xử lý sự cố gửi người dùng, và tin nhắn Zalo hướng dẫn dùng tính năng. Đọc khi cần mẫu cụ thể cho loại tài liệu đang viết.
