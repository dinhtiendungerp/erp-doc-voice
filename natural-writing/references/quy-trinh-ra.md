# Quy trình rà và các tình huống riêng

Đọc khi rà một văn bản trước khi giao, khi được nhờ biên tập hay soi văn bản, khi giao hỏng, hoặc khi so bản người dùng sửa tay. Có nguyên các câu hỏi của lượt 4 theo từng loại văn bản, và phạm vi áp dụng bản đầy đủ ở cuối file.

## Quy trình áp dụng

Viết trước, rà sau. Vừa viết vừa tự kiểm duyệt thì văn sẽ cụt.

1. **Viết bản thô** theo nội dung, chưa quan tâm văn phong.
2. **Lượt rà nội dung**: đọc từng câu, hỏi "câu này thêm gì?". Xóa câu rỗng. Đây là lượt quan trọng nhất.
3. **Lượt rà cấu trúc**: song song phủ định, bộ ba, đuôi phân từ, liên từ mở đoạn lặp, câu kết thừa, né "là"/"có", đổi tên đối tượng giữa chừng.
4. **Lượt rà thứ tự và thể loại**, với tài liệu kỹ thuật. Các câu hỏi dưới đây, xem nhóm 14 đến 40:
   - Câu đầu đã là câu trả lời chưa?
   - Độ dài và tầm vóc đề xuất có tương xứng câu hỏi không?
   - Tên định danh có bị dịch thành chữ của mình không, có tự chế thuật ngữ không, có đặt tên mới cho việc đã có tên không? Nhãn tiếng Việt của trường có đang dịch sát caption hay tả vị trí trên màn hình thay vì nói trường làm gì không, giá và số lượng đã nói tính theo đơn vị nào chưa?
   - Tiêu đề mục và thân bài có ẩn dụ không?
   - Mức chi tiết kỹ thuật có đúng người đọc không: dev, BA, hay PM và khách hàng? Tên kỹ thuật lạ đã được nói nó là gì trước khi nói dùng để làm gì chưa?
   - Đúng thể loại chưa: hướng dẫn thì các bước lên trước, tài liệu mô tả hiện trạng thì không chen giải pháp, email thì không dựng heading?
   - Với GAP List, Issue Log, FDD mức BA: cột Solution còn chữ codeunit, hàm, event, mã object không? Còn deliverable dự án (Quick Guide, training) lẫn vào giải pháp không? Ô Description, Solution của Issue Log có đang chép điều kiện chi tiết đã nằm trong FDD không?
   - Mỗi bước lấy dữ liệu đã đủ ba vế trong một câu chưa: dựa vô field nào, trên bảng nào, lấy field nào?
   - Với WBS và bảng estimate: đúng bên làm chưa, đúng bộ vai trò của công ty chưa, ngày công có rải theo tác vụ chưa, lịch của bên khác có bị sửa không, mốc go-live có lấy đúng ngày họ đã nêu không? Kế hoạch cho một người cụ thể: đã biết người đó làm bao lâu và quen phần nào chưa, giờ tự học có tính bằng giờ và không quá 1 giờ mỗi ngày không, tuần nặng nhất có quanh 60% không, onsite có chỉ những ngày thuộc phần mình không, còn khối "điểm cần chốt" nào trong file không, từng việc đã ghi người đó làm chính hay phụ chưa, thời gian đọc tài liệu có tính theo giờ không, tên dòng còn chữ "Dự", "Tham gia" không?
   - Tổng có nằm trong khoảng người duyệt đưa ra không, số do đội phát triển ước lượng có bị sửa đè không, con số suy ra từ số khác đã là công thức chưa?
   - Gộp dòng xong đã đánh số lại chưa, còn ghi chú nào kể lại việc gộp không? Còn con số đếm được nào viết thành chữ trong câu văn không?
   - Tên các dòng trong cùng một giai đoạn có cùng dạng ngữ pháp không, có dòng nào đeo thêm chủ thể hoặc cách thức đã nằm ở cột khác không?
   - Có đoạn nào đang giải thích cách đọc bảng không? Bỏ đi.
   - Ghi chú trong ô có câu nào chỉ có ích cho người lập file không: sổ sách tính ngày công, tham chiếu phiên bản hay phương án của tài liệu khác, chi phí giả định, con số không kèm danh sách, mã nội bộ không giải nghĩa?
   - File và slide giao khách còn câu nào kể về môi trường demo, phiên bản app, Work Date của bản demo, cách dựng số liệu, bước nội bộ của NWV hay việc còn chờ chốt không? Còn nhãn nào tả việc của người dựng file ("nạp") thay cho việc người nhận làm ("điền") không? (nhóm 37)
   - Các khối cùng cấp (nhập và xuất, lệnh và kết quả) có chia dòng cùng một cách, dùng cùng bộ mã ở mọi sheet không? Thời điểm kích hoạt của từng loại chứng từ có lấy đúng quy trình thật của nó không?
   - Bảng tổng hợp đã tách riêng phần làm cùng đối tác chưa, nếu phần đó thương lượng riêng?
   - Email gửi kèm file: có đang chép lại chi tiết trong file, tự thêm việc nhờ xác nhận, hay đưa lập luận nội bộ không? Ngược lại, có bỏ sót ý người giao việc đã liệt kê không? Đã biết ai đứng tên gửi để chọn xưng hô chưa, có lấy tên công ty thay cho anh, chị để né xưng hô không? Bị chê dài thì phần dài là email hay ghi chú mình viết kèm trong chat?
   - Trả lời thắc mắc của người dùng: câu đầu có gỡ đúng chỗ họ hiểu lầm không, có số chứng từ cụ thể nào khiến họ hỏi lại "sao lại là số này" không?
   - Đoạn cuối có đang tóm tắt lại bài không? Email thì kết bằng việc cần làm, tài liệu thì dừng ở mục cuối.
   - Hướng dẫn xử lý gửi người dùng: đã chỉ còn tình huống, hành động và danh sách `Field = giá trị` chưa, hay vẫn còn số field, cơ chế, field để mặc định?
   - Tin nhắn Zalo hoặc Teams: có bullet nào là một câu nói với người đọc không? Tên field, tên trang có bị dịch sang tiếng Việt không, trang cần mở đã ghi kèm status chưa? Câu cuối có đang nhắc lại cái lợi mà người hỏi đã biết, diễn giải lại câu trước, hay trấn an điều người hỏi không hỏi không? Gửi đồng nghiệp consultant thì có nói bằng cơ chế BC chưa, có báo trước kết quả hay bước tiếp theo khi người phụ trách chưa chốt hướng không? Hướng dẫn sửa chứng từ: có đang chép bảng số người nhận tự tra được trên BC không, có bước nào không bắt buộc không, có câu "nếu..." nào mình kiểm được mà chưa kiểm không?
   - Tài liệu chính thức còn khẩu ngữ không ("bỏ" khi nghĩa là loại trừ, "gán tay", "up"), còn tên giao diện bị dịch chữ không ("cây" thay cho treeview), còn nhánh xử lý cho dữ liệu khách không có không?
   - Câu thông báo của hệ thống trong FDD và code đã là tiếng Anh theo mẫu message của BC chưa? Hình chụp còn câu tiếng Việt không?
   - Tài liệu tích hợp: message đã đặt tên theo đối tượng Business Central chưa, message kết quả có đang mang tên chứng từ đã ghi sổ thay vì chứng từ nhận kết quả không, nhãn trên sơ đồ có còn mã trơn không, còn mục nào cho phần không làm không, bảng con đã thành API riêng chưa, luồng ngoại lệ đã tách tình huống kèm sơ đồ chưa, còn ô hay cột trạng thái nào không, phần đề xuất custom đã đủ bảng, field, API chưa? Message có lô đã chia cấp (header, chi tiết, lô) chưa, đã có khóa từng cấp, số tổng ở cấp dòng, trường đích có phải trường nhập được (không phải trường Base tự tính) và tên trường message có gần tên trường Business Central không, bảng trường hợp một-nhiều, quy tắc theo loại chứng từ, ví dụ message chưa? (nhóm 40)
   - File data migration: tên sheet đã là số bảng và tên bảng chưa, còn cột cờ nào ghi cùng một chữ cho mọi dòng không, còn sheet nào trống hay chỉ có vài dòng mẫu trong khi hệ thống có đủ dữ liệu không, mã thuế, nhóm đối tượng, tài khoản đã theo cách gọi của kế toán Việt Nam chưa? Còn dòng nhận dạng lặp ở mọi sheet không? (nhóm 16, 20, 35)
   - Định dạng có khớp phần còn lại của tài liệu và file gốc của khách không?
5. **Lượt rà hình thức**: in đậm, bullet, heading, gạch ngang dài, nháy cong, emoji, mũi tên, dấu chấm phẩy, bảng thừa, quy ước màu ô trong file Excel. Với file Excel còn thêm: bốn dòng đầu của các sheet có giống nhau không, ô nào phải quấn dòng vì câu quá dài, cột nào rộng quá mức cần, nhóm cột đã phủ hết các cột chi tiết chưa.
6. **Lượt rà nhịp**: đọc to. Câu dài xấp xỉ nhau thì trộn lại. Câu ghép quá hai vế bằng "và", "đồng thời", "nhằm", "qua đó", "từ đó" thì tách ra. Ngoại lệ: câu mô tả một bước lấy dữ liệu theo nhóm 31 được giữ đủ ba vế trong một câu. Không ép câu siêu ngắn 3-5 chữ vào tài liệu kỹ thuật; thỉnh thoảng một câu ngắn là đủ để đổi nhịp.
7. **Lượt rà dữ kiện**: mọi con số, tên object, page, field đều truy được về nguồn có thật. Có source code hoặc tài liệu thì mở ra đọc, không suy luận. Không truy được thì để trống và ghi rõ chỗ cần điền.
8. **Lượt rà vết tích**: grep chữ tiếng Việt trong script và file nguồn vừa sửa (ghi chú khai trong code, nhãn, câu chèn bằng COM), rà như văn bản thường vì chúng đi thẳng vào file giao. Chạy checklist trong `references/dau-vet-ky-thuat.md`. Với file Excel: xuất PDF, xem ảnh từng trang, kiểm tra các ô công thức tổng hợp, và mở lại file bằng thư viện đọc sau mọi thao tác vá file. Kiểm tra đã gửi đủ bộ file chưa.

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

- **So cả giá trị lẫn định dạng.** Lần so bản WBS khách A chỉ có 15 ô đổi nội dung, nhưng phần định dạng mới là chỗ nhiều bài học: đường kẻ thiếu ở một sheet, chiều cao dòng dư, nhóm cột phủ thiếu hai cột.
- **Bỏ qua nhiễu do phần mềm lưu lại.** Excel lưu lại file thì canh lề `general`/`bottom` và `wrap_text` đổi từ None sang False ở hàng nghìn ô. Lọc theo font, màu nền, số định dạng và canh lề ngang để còn lại các sửa thật.
- **Đọc hướng của các sửa, không chỉ từng sửa.** Bốn ô bị cắt đuôi câu, một dòng bị xóa, một tên công việc bị rút gọn: cùng một hướng là bỏ phần giải thích thừa. Ghi lại hướng đó chứ đừng ghi bốn luật riêng lẻ.
- **Gom cả các phản hồi rời trong lúc làm, không chỉ bản cuối.** Một phiên dài có hàng chục câu sửa ngắn ("ko cần thêm cột đề xuất", "gom lại đi", "nghe AI quá", "ngắn gọn thôi"). Từng câu nhìn như chuyện vặt, xếp cạnh nhau mới thấy ba bốn hướng lặp lại. Hướng lặp lại mới đáng ghi vào skill; câu chỉ xuất hiện một lần thì để trong ghi chú dự án.

## Phạm vi áp dụng

Skill này dùng chung cho mọi nơi PM làm việc, không riêng file bàn giao:

- **Câu trả lời trong chat** (claude.ai, Cowork, Claude Code): câu đầu là câu trả lời, ngắn theo đúng tầm câu hỏi (nhóm 14, 15). Báo đã sửa file thì nói sửa gì, ở đâu, trong vài dòng; không kể lại từng bước đã làm. Viết cùng thứ tiếng người dùng đang dùng, cả câu báo tiến độ lẫn bản báo kết quả. Bản báo kết quả bỗng chuyển sang tiếng Anh giữa một phiên tiếng Việt bị bắt bằng câu "viết tiếng việt đi trời" (30/09/2026).
- **File làm trong Cowork** (Excel, Word, email soạn sẵn): đủ các nhóm bên dưới, nhất là 26, 32 đến 37.
- **Claude Code**: commit message, comment trong code, README, tài liệu sinh bằng script. Commit và ghi chú phiên bản theo mục "ghi chú thay đổi" ở phần Vết tích quy trình.

Skill áp cho mọi chữ người khác sẽ đọc, kể cả khi chữ đó nằm trong code: chuỗi ghi chú khai trong script sinh bảng, nhãn trong file dựng Excel, câu chèn vào file Word bằng COM, đoạn markdown nguồn của FDD. Câu ngắn gõ thẳng vào code dễ bị coi là "viết code" nên bỏ qua bước rà, rồi theo bảng sinh tự động đi thẳng vào file giao. Ngày 10/10/2026, câu "Trường có sẵn trên thẻ mặt hàng" khai trong `gen_fields.py` lên FDD mà không qua skill, PM hỏi lại: "bạn ko dùng skill natural-writing hả". Cụm chép từ ghi chú nội bộ (file bối cảnh dự án, biên bản, tin nhắn) cũng phải rà, vì ghi chú nội bộ viết nhanh, không theo chuẩn của tài liệu giao.

Phân tích, lý do, phương án và chi phí từng lựa chọn là chỗ của câu trả lời trong chat hoặc tin nhắn cho sếp. Không để chúng lọt vào file hay email gửi khách (nhóm 37).
