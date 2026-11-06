# FDD, GAP List, Issue Log và việc giao cho dev

Đọc khi viết FDD, GAP List, Issue Log, ticket DevOps, README hoặc tin nhắn gửi dev kèm code mẫu. Gồm nhóm 30, 38, 39 và các ý riêng cho FDD, ticket, bản mẫu code.

## 30. GAP List và FDD mức BA trượt sang giọng dev

Bị bắt ở GAP List khách D (Recipe Version theo ngày), sau khi đã được nhắc "mô tả dưới góc độ BA". Ba lỗi cụ thể:

- **Mở giải pháp bằng cấu trúc code.** "Codeunit NWV Recipe Version Mgt. có ba hàm và một bảng trạng thái:" rồi liệt kê hàm. Người ký GAP List là khách hàng, họ không cần biết có mấy hàm. Viết: "Thêm chức năng Xử lý version theo ngày, gồm action trên Recipe Card, bảng lịch sử và bảng trạng thái", rồi mô tả từng thứ làm gì bằng lời.
- **Dẫn object ID vào cột Solution hoặc tên Business Process.** "(Cod60004, Rep60005)" thay vì "tool Item Positive Posting hiện có". Object ID chỉ để ở sheet Object List hoặc Ghi chú kỹ thuật cho dev.
- **Đưa deliverable dự án vào giải pháp.** "Quick Guide cho Data: tạo version mới, đóng version cũ" không phải giải pháp phần mềm; nó thuộc kế hoạch triển khai. Bỏ khỏi cột Solution.

Cùng lần đó, ba từ bị bắt vì nghe như máy dịch: "nạp" (nạp version, version đang nạp), "hiện hành", "nội dung version". Đã đưa vào bảng nhóm 20. Với BA thì nói "xử lý version", "hiện tại", "dữ liệu của version".

Kiểm tra trước khi giao GAP List: đọc cột Solution như thể mình là khách hàng. Gặp chữ "codeunit", "hàm", "subscriber", "event", mã object thì hạ xuống mức chức năng; gặp tài liệu, training, quick guide thì chuyển sang phần kế hoạch.

FDD giao đội phát triển của NaviWorld cũng viết ở mức này, vì khách xem được folder Design. Bị bắt ngày 12/10/2026 ở FDD tích hợp khách A: "sao lại dùng từ subscriber, codeunit trong FDD". Câu đã lên FDD là "Gọi codeunit ghi sổ chuẩn với SetSuppressCommit(true) và gọi thẳng, không bắt lỗi bằng if Codeunit.Run hay TryFunction", đề xuất tiếp theo còn thêm "subscriber", "cờ đang ghi sổ". FDD giữ quy tắc theo chức năng: "Ghi số lượng, lô và ghi sổ nằm trong cùng một lần xử lý, không lưu dữ liệu giữa chừng, kể cả bên trong chức năng ghi sổ chuẩn. Ghi sổ lỗi thì hoàn lại toàn bộ." Tên codeunit, hàm, tham số, cách gọi đưa vào file ghi chú kỹ thuật cho dev (nội bộ, không nằm trong folder khách). Tên đối tượng, field, trang chuẩn (Warehouse Receipt, Qty. to Receive, Item Tracking Lines) vẫn giữ trong FDD.

Issue Log phải gọn hơn FDD một bậc. Bị bắt ngày 01/10/2026, hai lượt liền: "cột Description viết lại cho ngắn gọn thôi", rồi "cột NaviWorld Solution / Remark cũng viết ngắn lại". Bản dài kể đủ các điều kiện loại lot (hết hạn dùng, Blocked, Inspection Status, Sales Expiration Date, Minimum Sales Shelf Life, lot đã gán cho phiếu khác) và cả câu báo kết quả sau khi bấm nút. Bản sửa gom lại thành "loại trừ lot không được bán". Description còn hai khối Hiện trạng và Cần sửa, mỗi khối hai ba dòng. Điều kiện chi tiết đã nằm trong FDD thì Issue Log không chép lại.

## 38. Khẩu ngữ lọt vào tài liệu chính thức

Rút từ FDD Actual Lot của khách B, 30/09/2026. PM tự sửa năm chỗ trong bản giao. Không chỗ nào đổi nội dung, chỉ đổi từ:

| Bản giao | PM sửa | Vì sao |
|---|---|---|
| lấy trong Bin của dòng, bỏ lot không được bán | lấy trong Bin của dòng, loại trừ lot không được bán | "bỏ" là khẩu ngữ, nghe như vứt đi. Nói về điều kiện lọc thì dùng "loại trừ" |
| Lot đã gán tay trước đó | Lot đã gán thủ công trước đó | "gán tay" là cách nói trong chat |
| Item Tracking Lines cho Sales Line nguồn | Item Tracking Lines cho Sales Line gốc | Dòng bán mà dòng Warehouse Shipment đi ra từ đó là dòng gốc. "nguồn" dễ lẫn với Source, nguồn nhập, nguồn gốc lot |
| dựng cây truy xuất như trang Item Tracing rồi áp Actual Lot Entries vào cây | dựng dạng truy xuất treeview như trang Item Tracing rồi áp Actual Lot Entries vào treeview | Thứ hiện trên màn hình có tên nghề là treeview, team gọi vậy. "cây" là dịch chữ (nhóm 20) |
| Lot không có Expiration Date xếp cuối. | (xóa) | Thành phẩm khách B lot nào cũng có hạn dùng. Nhánh xử lý cho dữ liệu không có ở khách là chuyện của code |

Ba hướng rút ra:

- **Tài liệu chính thức trang trọng hơn tin nhắn một bậc.** FDD, tài liệu đề xuất, biên bản, tài liệu bàn giao: động từ khẩu ngữ phải đổi sang từ chuẩn. "bỏ" thành "loại trừ" (khi lọc) hoặc "loại bỏ" (khi xóa khỏi mẫu in, khỏi chuỗi), "gán tay" thành "gán thủ công", "up" thành "tải lên", "xuất đại" thành "xuất không theo lot gợi ý". "bỏ qua" theo nghĩa hệ thống không xử lý một dòng thì giữ. Không áp ngược lại: tin nhắn Zalo, Teams vẫn giữ giọng nói chuyện (nhóm 36).
- **Thứ trên giao diện gọi bằng tên nghề, kể cả khi đó là tiếng Anh.** treeview, FactBox, FastTab, action bar, request page. Không dịch thành "cây", "hộp thông tin", "thẻ".
- **Không ghi nhánh cho dữ liệu khách không có.** Viết một điều kiện biên thì hỏi: dữ liệu thật của khách có rơi vào nhánh này không? Không thì để trong code, không đưa vào tài liệu.

PM chỉ sửa ở phần đầu tài liệu. Các chỗ cùng loại ở phần sau vẫn phải sửa theo: rà cả tài liệu theo gốc từ "bỏ ", "tay", "nguồn", "cây" rồi quyết từng chỗ.

## 39. Câu thông báo của hệ thống viết bằng tiếng Anh

PM yêu cầu ngày 30/09/2026: mọi câu thông báo trong FDD và trong code phải bằng tiếng Anh, dù thân tài liệu viết tiếng Việt. Gồm câu lỗi, câu thông báo kết quả, câu hỏi xác nhận, và chữ hệ thống tự ghi vào cột trên trang (cột Error, cột thông tin trên treeview). BC của khách chạy giao diện tiếng Anh. Câu tiếng Việt lẫn vào thì dev phải tự dịch, và người dùng thấy hai thứ tiếng trên một màn hình.

Viết theo văn phong message chuẩn của BC:

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Thiếu giá trị | "%1 must have a value." | "Actual Lot No. must have a value." |
| Không tồn tại | "%1 %2 does not exist." | "Posted Sales Shipment %1 does not exist." |
| Không được làm | "%1 cannot be ..." hoặc "You cannot ..." | "Entry %1 is a reversal entry and cannot be reversed." |
| Hỏi xác nhận | "Do you want to ...?" | "Do you want to reverse the %1 selected entries?" |
| Kết quả | câu ngắn, số đứng đầu | "%1 line(s) imported: %2 Ready, %3 with errors." |
| Chỉ cách sửa | câu mệnh lệnh ngắn nối sau câu lỗi | "Sales Order %1 has %2 posted shipments with item %3 (%4). Enter the Posted Shipment No." |

- Giữ nguyên %1, %2 và tên field đúng caption tiếng Anh.
- Câu đã có trong app đang chạy thì chép đúng như vậy (ví dụ "Sign Successfully" của eSign), không viết câu mới cho cùng một thông báo.
- Hình chụp còn câu tiếng Việt thì chụp lại, hoặc ẩn cột đó nếu người dùng không muốn dựng lại. Không để hình và chữ trong tài liệu nói hai thứ tiếng.
- Thân tài liệu, chú thích hình, bảng mô tả vẫn tiếng Việt. Chỉ câu hệ thống hiện ra là tiếng Anh.

## Thuật ngữ và mục Giải pháp tổng thể trong FDD

- Không dịch thuật ngữ kỹ thuật sang tiếng Việt. Viết "header", "line", "lines", "trackingLines", "request", "response", không viết "phần đầu", "các dòng", "phần đầu phiếu" khi nói về message hoặc chứng từ Business Central (người phụ trách khách A nhắc nhiều lần, bắt lại ở FDD 07/10/2026). Ví dụ: "WMS gửi header, lines và trackingLines trong một request", không viết "WMS gửi phần đầu, các dòng và các lô".
- Mục "Giải pháp tổng thể" của FDD viết gạch đầu dòng, mỗi ý một dòng. Đoạn văn dài gom nhiều ý thì người đọc phải tự tách.

## Viết cho đội phát triển khi tư vấn đưa code

README, ghi chú gửi kèm mã nguồn bản mẫu không viết theo giọng "dev đọc code đã kiểm, làm đúng yêu cầu, không phải nghiên cứu lại từ đầu". Đội phát triển nhạy cảm khi bộ phận chức năng đưa code, câu kiểu đó đọc như chỉ việc cho dev (bị nhắc 07/10/2026). Viết bản mẫu là công cụ kiểm thiết kế: nêu nó chứng minh được điểm nào chạy trên chuẩn, giới hạn của nó (chưa cài gói nào, phần nào giả lập), và nói rõ cách tổ chức code, hiện thực do đội phát triển quyết định. Bỏ các câu ra lệnh cho bản thật ("bản thật làm trên...", "dải id theo...").

Tin nhắn chat gửi link repo cho dev (12/10/2026). Bản tôi soạn có bốn đoạn: lý do dựng bản mẫu, "anh xem cho vui thôi", lệch thì lấy FDD, ngày công vẫn theo anh ước lượng. PM tự viết lại:

> Anh ơi em thấy vụ gọi api 2 lần nó cũng gặp lại vấn đề là dữ liệu đã insert rồi, thì đến đoạn gọi api post lỗi. Lúc làm FDD có mấy chỗ em không chắc chạy được ko giống như cái yc là rollback khi post lỗi, nên em dựng thử mẫu trên mt demo để xem thử. Chạy thử thì thấy ok, với lại cũng cần điều chỉnh thêm mấy chỗ về logic, em có cập nhật vào FDD á.
>
> Anh xem thử các case đã test coi còn lủng gì ko nha [link], với lại trong này em cũng có để code dựng mẫu, anh xem thử coi dùng lại đc gì ko nha, em làm để kiểm luồng nên code chắc chưa chuẩn, chưa tính performance. Anh cứ làm theo cách của anh nha, cái này chỉ để trực quan hơn nhu cầu của FDD thôi á.

Năm chỗ khác:

- **Mở bằng vấn đề kỹ thuật cụ thể dev đang quan tâm**, không mở bằng "em gửi anh repo". Câu đầu nói đúng tình huống lỗi (gọi API hai lần, dữ liệu đã insert rồi bước post lỗi), nên dev thấy ngay bản mẫu trả lời câu hỏi gì.
- **Nhờ dev soi test case, không nhờ dev đọc code.** "coi còn lủng gì ko" đặt dev vào vai người rà, người giỏi hơn mình ở phần kỹ thuật. Code chỉ là phần phụ: "coi dùng lại đc gì ko".
- **Tự hạ đúng mức, không hạ quá.** "code chắc chưa chuẩn, chưa tính performance" là đủ khiêm tốn. "xem cho vui thôi" thì hạ giá trị chính thứ mình nhờ người ta xem (nhóm 23).
- **Không đặt luật cho dev trong tin nhắn.** Bỏ "lệch thì lấy FDD", "ngày công vẫn theo anh ước lượng", danh sách thư mục nên xem, CHANGELOG. Mấy câu đó đọc như phòng thủ hoặc giao việc. Mục đích nói một câu: "chỉ để trực quan hơn nhu cầu của FDD".
- **Giọng chat nội bộ với dev**: xưng em gọi anh, "á", "nha", "ko", "đc", "yc", "mt", và giữ từ dev dùng (api, insert, post, rollback, case, performance). Không chia đoạn theo ý như email, không bullet.

Kiểm tra: dev đọc câu đầu có biết ngay bản mẫu giải quyết vấn đề gì của họ không? Có câu nào đang dặn dev phải làm gì không?

## Ticket DevOps nhờ trưởng nhóm dev assign

Rút từ một sub-ticket của khách A, 29/10/2026. Bản đầu tôi viết như tài liệu thiết kế cho một dev cụ thể: tiêu đề có tên dev, ba phần "Phần 1. Hiện trạng", "Phần 2. Yêu cầu", "Phần 3. Lưu ý", bảng mapping từng field kèm số dòng code LS, mục rủi ro. PM trả về kèm ba ticket mẫu và câu "chưa đọc skill natural-writing à". Cách viết trong các ticket mẫu:

- **Chưa biết dev nào làm thì gửi trưởng nhóm, không tự gán.** "Dear anh @<trưởng nhóm dev>," rồi "Nhờ anh giúp em assign nhân sự hỗ trợ case này với nhé:". Tiêu đề theo mẫu `<ticket cha> - Bổ sung tính năng_<chủ đề>` (yêu cầu mới) hoặc `<ticket cha>_<dev> - <chủ đề>` (khi đã biết dev).
- **Ba khối, viết liền, không đánh "Phần N".** "Hiện trạng:" một đoạn có số chứng từ, giờ, câu lỗi thật. "Nguyên nhân" nếu đã biết. "Yêu cầu sửa" hoặc "Yêu cầu bổ sung" đánh số, ý con gạch đầu dòng. Cuối là dòng "GAP liên quan" hoặc dữ liệu đối chiếu, file đính kèm.
- **Yêu cầu nói làm gì và lấy từ đâu, không dẫn số dòng code.** "Staff ID, Shift No.: từ Sales Entry" là đủ. Tên event, tên field giữ, số dòng và mục "lưu ý cho dev" thì bỏ: dev tự đọc code. Bảng mapping nhiều cột chỉ dùng khi ticket thật sự là bảng.
- **Không đưa phân tích rủi ro của mình vào ticket.** Nghi ngờ giải pháp không bắt được case nào thì nói với PM trong chat.
