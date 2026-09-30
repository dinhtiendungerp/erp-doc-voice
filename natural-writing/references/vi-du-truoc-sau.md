# Ví dụ sửa trước / sau

Các ví dụ lấy từ ngữ cảnh tài liệu tư vấn Business Central và LS Central. Nguyên tắc chung: mỗi lần sửa đều **thay câu đánh giá bằng câu dữ kiện**, không phải chỉ đổi từ.

Mục lục:
1. Mở đầu FDD / FRD
2. Mô tả yêu cầu và giải pháp
3. Email gửi khách hàng
4. Email nội bộ / nhờ dev
5. Quick Guide
6. Nội dung slide
7. Báo cáo tình hình dự án
8. Né động từ "là"/"có" và đổi tên đối tượng
9. Giải thích logic code cho người dùng nghiệp vụ
10. Tài liệu kỹ thuật bàn giao trên Confluence
11. Thư ngắn gửi khách hàng
12. Tài liệu tích hợp gửi khách hàng và đối tác
13. Email trao đổi phương án với khách
14. Tài liệu kiến trúc và mô tả nhu cầu cho BA
15. Hướng dẫn xử lý sự cố gửi người dùng

---

## 1. Mở đầu FDD / FRD

**Trước**

> Trong bối cảnh chuyển đổi số ngày càng mạnh mẽ, việc quản lý dữ liệu bán hàng đóng vai trò then chốt đối với doanh nghiệp bán lẻ. Tài liệu này không chỉ mô tả yêu cầu nghiệp vụ mà còn cung cấp một cái nhìn toàn diện về giải pháp, qua đó giúp các bên liên quan có được sự thống nhất trong quá trình triển khai.

Bốn dấu hiệu trong ba dòng: mở bài rỗng, thổi phồng, song song phủ định, đuôi phân từ rỗng. Bỏ hết thì còn lại gần như không có gì - đó chính là bằng chứng đoạn này không mang thông tin.

**Sau**

> Tài liệu mô tả yêu cầu và thiết kế cho GAP SPF-014: đồng bộ đơn hàng Shopify về LS Central. Phạm vi gồm mapping trường dữ liệu, xử lý combo, và cách xử lý đơn lỗi. Không bao gồm phần thanh toán và hoàn tiền, đã tách sang SPF-018.

---

## 2. Mô tả yêu cầu và giải pháp

**Trước**

> Hệ thống cần cung cấp khả năng theo dõi tồn kho theo lô một cách hiệu quả, đảm bảo tính chính xác và kịp thời của dữ liệu, từ đó nâng cao hiệu quả quản lý kho.

**Sau**

> Hệ thống theo dõi tồn kho theo Lot No. và hạn sử dụng. Khi xuất hàng, POS chặn lô đã quá hạn và gợi ý lô có hạn gần nhất.

Chú ý: "một cách hiệu quả", "đảm bảo tính chính xác", "từ đó nâng cao hiệu quả" đều bị xóa mà không mất thông tin nào, vì chúng vốn không mang thông tin.

**Trước**

> Giải pháp đề xuất là phát triển một extension mạnh mẽ và linh hoạt, cho phép tích hợp liền mạch giữa BC và hệ thống ecommerce, mang lại trải nghiệm tối ưu cho người dùng cuối.

**Sau**

> Giải pháp là một extension chạy trên BC, gọi API Shopify theo lịch 15 phút một lần. Người dùng cuối thao tác trên Sales Order như đơn hàng nhập tay, không cần vào màn hình riêng.

---

## 3. Email gửi khách hàng

**Trước**

> Kính gửi anh Nam,
>
> Trước tiên, chúng tôi xin gửi lời cảm ơn chân thành đến anh và đội ngũ vì sự phối hợp trong thời gian qua. Điều quan trọng cần lưu ý là tiến độ dự án hiện đang được đảm bảo, tuy nhiên vẫn còn một số vấn đề cần được giải quyết. Hơn nữa, chúng tôi rất mong nhận được sự hỗ trợ từ phía anh.
>
> Trân trọng,

**Sau**

> Kính gửi anh Nam,
>
> Em cập nhật tình hình UAT tuần này. Module Purchase đã test xong 34/34 case, pass 31, còn 3 case fail liên quan đến duyệt PR nhiều cấp - em đã log issue và dev đang xử lý, dự kiến xong thứ Sáu.
>
> Nhờ anh hỗ trợ hai việc: xác nhận danh sách user cho vòng UAT module Sales, và cho em xin file danh mục nhà cung cấp cập nhật đến tháng 7.
>
> Trân trọng,

**Trước**

> Cảm ơn anh đã phản hồi. Chúng tôi ghi nhận ý kiến của anh và sẽ xem xét một cách kỹ lưỡng. Hy vọng thông tin trên hữu ích với anh. Anh có cần em bổ sung thêm gì không ạ?

Hai câu cuối là vết chatbot điển hình. Người viết thật kết email bằng một hành động cụ thể.

**Sau**

> Cảm ơn anh đã phản hồi. Em sẽ rà lại phần tính giá và gửi anh bản cập nhật trước trưa mai.

---

## 4. Email nội bộ / nhờ dev

**Trước**

> Chào bạn, mình cần nhờ bạn hỗ trợ xử lý một vấn đề. Hiện tại hệ thống đang gặp lỗi trong quá trình đồng bộ, điều này ảnh hưởng không nhỏ đến tiến độ. Rất mong bạn có thể ưu tiên xử lý sớm nhất có thể. Cảm ơn bạn rất nhiều!

**Sau**

> Chào bạn, KOT ở Web KDS tự chuyển sang VOID sau khoảng 30 giây, không thao tác gì. Xảy ra ở station BAR, các station khác bình thường. Mình nghi Station Flow cấu hình sai nhưng chưa loại trừ được. Log mình để ở thư mục dùng chung, file ngày 06/08.
>
> Khách demo thứ Tư nên nhờ bạn xem giúp trước thứ Ba.

---

## 5. Quick Guide

**Trước**

> ### Tạo Purchase Request
>
> **Bước 1: Truy cập** - Người dùng truy cập vào màn hình Purchase Request.
> **Bước 2: Tạo mới** - Người dùng nhấn nút New để tạo mới một Purchase Request.
> **Bước 3: Điền thông tin** - Người dùng điền đầy đủ các thông tin cần thiết một cách chính xác.

Ba lỗi: bullet dạng "**Nhãn:** giải thích", nội dung giải thích chỉ lặp lại nhãn, và bước 3 không nói gì (thông tin nào? chính xác là thế nào?).

**Sau**

> ### Tạo Purchase Request
>
> 1. Vào **Purchase Requests**, chọn **New**.
> 2. Chọn Requester và Location. Hệ thống lấy Dimension mặc định theo Location, sửa được nếu cần.
> 3. Ở tab Lines, nhập Item No. và Quantity. Trường Expected Receipt Date bắt buộc, nếu bỏ trống thì không gửi duyệt được.
> 4. Chọn **Send Approval Request**.

---

## 6. Nội dung slide

**Trước** (một slide, ba bullet)

> - Giải pháp toàn diện, đáp ứng mọi nhu cầu bán lẻ
> - Tích hợp liền mạch, mạnh mẽ và linh hoạt
> - Nâng tầm trải nghiệm khách hàng

Ba bullet, ba tính từ mỗi bullet, không có gì kiểm chứng được. Slide này nói được với bất kỳ phần mềm nào trên thị trường.

**Sau**

> - Một hệ thống cho POS, kho và kế toán - không cần đối soát giữa các phần mềm
> - Đơn Shopify về LS Central trong 15 phút, tồn kho trừ ngay
> - Đã chạy tại 14 siêu thị, 60 quầy thu ngân

---

## 7. Báo cáo tình hình dự án

**Trước**

> Nhìn chung, dự án đang tiến triển tích cực. Đội ngũ đã có những nỗ lực đáng kể trong việc hoàn thiện các hạng mục, qua đó góp phần đảm bảo tiến độ chung. Tuy nhiên, vẫn còn một số thách thức cần được quan tâm giải quyết trong thời gian tới.

**Sau**

> Tuần này hoàn thành cấu hình module Inventory và import xong master data Item (4.812 dòng, 37 dòng lỗi đang chờ khách confirm).
>
> Chậm so với kế hoạch: cấu hình Warehouse lùi một tuần vì chưa chốt được sơ đồ Bin của kho Bình Dương.
>
> Cần khách quyết trước 12/08: sơ đồ Bin, và có dùng Directed Put-away hay không.

---

## 8. Né động từ "là"/"có" và đổi tên đối tượng

Hai lỗi này ít lộ hơn các lỗi trên nhưng phá hoại tài liệu kỹ thuật nhiều hơn, vì người đọc không còn chắc hai câu đang nói về cùng một thứ.

**Trước**

> Purchase Request đóng vai trò là chứng từ đề nghị mua hàng nội bộ. Nền tảng cho phép người dùng khởi tạo yêu cầu và gửi duyệt. Công cụ này sở hữu khả năng phân quyền theo nhiều cấp. Giải pháp mang lại sự linh hoạt trong việc cấu hình luồng duyệt.

Bốn câu, bốn tên gọi khác nhau cho cùng một thứ, và không câu nào dùng "là" hay "có".

**Sau**

> Purchase Request là chứng từ đề nghị mua hàng nội bộ. Người dùng tạo Purchase Request rồi gửi duyệt. Purchase Request có luồng duyệt nhiều cấp, cấu hình trong Approval Workflow.

Ba câu, một tên gọi, thông tin nhiều hơn.

**Trước**

> Tính năng này được xem như một bước tiến, sở hữu khả năng xử lý đồng thời nhiều luồng và mang lại hiệu năng vượt trội.

**Sau**

> Tính năng này chạy song song tối đa 8 luồng. Trên bộ dữ liệu 50.000 dòng, thời gian xử lý giảm từ 40 phút xuống 7 phút.

---

## 9. Giải thích logic code cho người dùng nghiệp vụ

Ngữ cảnh: giải thích cách BC phân bổ item charge, phần lẻ rơi vào dòng nào.

**Trước**

> Có hai cơ chế khác nhau, cả hai đều đọc từ code trên: Phần lẻ về lượng (0.00001) rơi vào dòng 2, không phải dòng cuối. Lý do là ở dòng 2 giá trị thô 0.333335 nằm đúng nửa, và hàm Round của AL mặc định làm tròn nửa lên, nên thành 0.33334.

Vấn đề không nằm ở từ ngữ mà ở thứ tự: kết luận bị chôn sau phần dẫn nguồn, người đọc đọc hết vẫn không nắm được quy tắc chung.

**Sau**

> Code không có bước "dồn phần lẻ" vào một dòng. Nó tính lần lượt từng dòng theo thứ tự Line No., mỗi dòng lấy tỷ lệ của mình nhân với phần CÒN LẠI, rồi trừ đi. Dòng cuối cùng nhận nguyên phần còn lại.

Câu đầu là câu trả lời. Bảng số và trích code xuống sau.

### Kèm theo: đừng dịch tên tham số

**Trước**

> Amount to Assign = Round( Qty vừa tính / Qty còn lại × Amount còn lại , 1 đồng )

Viết "1 đồng" làm người đọc tưởng đây là con số ghi cứng trong code, và tưởng dòng đầu tiên không áp tham số này.

**Sau**

> Amount to Assign = Round( Qty vừa tính / Qty còn lại × Amount còn lại , `Currency."Amount Rounding Precision"` )
>
> Code không ghi cứng số 1. Giá trị đó lấy từ G/L Setup, và áp cho cả ba dòng chứ không riêng dòng nào.

## 10. Tài liệu kỹ thuật bàn giao trên Confluence

Tiêu đề mục:

| Trước | Sau |
|---|---|
| Giải phẫu một API page | Đọc một API page: từng thuộc tính làm gì |
| Hợp đồng của Custom API | Custom API nhận gì, trả gì |
| Trường lệnh actionCode | B8. `actionCode`: chạy nghiệp vụ bằng một lệnh PATCH |
| Trường trạng thái nút | B7. Các trường `canXxx`: Business Central quyết định nút nào được bấm |
| Trình kết nối ánh xạ entity set thế nào | 2.1. Mỗi entity set là một nguồn dữ liệu riêng |

Câu trong thân bài:

**Trước**

> Thiếu một trong hai thì extension không biên dịch được.

**Sau**

> Thiếu một trong hai gói này thì lệnh build báo lỗi thiếu symbol ngay dòng đầu.

**Trước**

> tăng trường version

**Sau**

> Bước 2. Tăng số phiên bản: sửa số ở dòng `version` lên cao hơn số đang cài.

Về bố cục: bản đầu giải thích kỹ nhưng đọc vô không biết làm gì trước. Sửa bằng cách tách Phần A các bước làm lên trước, Phần B tham chiếu xuống sau, mở đầu bài bằng bảng "cần gì thì đọc mục nào".

## 11. Thư ngắn gửi khách hàng

Ngữ cảnh: giới thiệu một app nội bộ cho phòng CNTT của khách.

**Trước** (khoảng 450 chữ, bốn tiêu đề in đậm)

> Chúng tôi gửi Anh/Chị ứng dụng này cùng toàn bộ tài liệu và mã nguồn để Phòng KHCN có một nền tảng tham khảo khi tự phát triển tiếp.
>
> ... Rất mong ứng dụng và bộ tài liệu này giúp ích cho Phòng KHCN.

Ba lỗi: tiêu đề in đậm chia mục trong một lá thư ngắn, câu dài với các cụm thừa ("toàn bộ", "một nền tảng tham khảo khi"), và câu kết chúc tụng rỗng.

**Sau** (khoảng 200 chữ, không tiêu đề)

> Gửi Anh/Chị app này cùng tài liệu và mã nguồn để dùng làm nền phát triển tiếp.
>
> Nói rõ trước: app này không thuộc gói GAP, không nằm trong hạng mục bên em phải bàn giao.

Bỏ hẳn câu kết "Rất mong ... giúp ích". Thư kết thúc ở thông tin cuối cùng, không cần đuôi.

---

## 12. Tài liệu tích hợp gửi khách hàng và đối tác

Ngữ cảnh: bộ tài liệu Word, Excel, PPT đánh giá ảnh hưởng khi chuyển WMS từ Tasklet sang Infolog, gửi cả khách hàng lẫn đối tác để chốt phạm vi.

Thuật ngữ, xem thêm mục 9 trong `cum-tu-can-tranh.md`:

| Trước | Sau |
|---|---|
| Đối tượng ngoài cụm phải sửa phẫu thuật | Hai mươi đối tượng ngoài cụm MobileWMS phải sửa trong file |
| bộ bản tin chuẩn của Infolog | bộ message chuẩn của Infolog |
| Nội dung tích hợp gói gọn ở sáu thông tin | Dữ liệu trao đổi gồm sáu thông tin |
| Đầu pallet / Dòng pallet | Pallet / Chi tiết pallet |
| Hệ chủ | Nguồn dữ liệu |
| Ảnh chụp tồn kho (Inventory snapshot) | Số tồn tại thời điểm chốt |
| Không chốt thì không khóa được phạm vi | Không chốt thì không chốt được phạm vi |

Mức chi tiết kỹ thuật, người đọc là PM và ban lãnh đạo:

**Trước**

> Cod65637 Split QC Order dùng trực tiếp bảng MOB License Plate Content. 8 đối tượng tableextension/pageextension extends MOB… 67 event subscriber.

**Sau**

> Gói QC đang gắn trực tiếp vào cấu trúc dữ liệu pallet của Tasklet. Khối chức năng kho dựng trên nền Tasklet. Khoảng 8% khối lượng tùy biến có liên kết tới Tasklet.

Giọng khi nhận xét tài liệu của đối tác:

**Trước**

> Đề xuất Infolog ghi Go-live "Week 23" nhưng UAT ở Week 27-32 và tổng 7-8 tháng, cần Infolog làm rõ mốc thật.

**Sau**

> Đưa vào mục "Điểm cần thống nhất về lịch" như một điểm cần làm rõ khi hai bên chốt lịch chung. Nhãn "Vấn đề phát hiện" đổi thành "Điểm cần làm rõ".

Ký hiệu mũi tên:

| Trước | Sau |
|---|---|
| Gỡ Tasklet ⇒ phải gỡ hết tham chiếu | Gỡ Tasklet thì phải gỡ hết tham chiếu |
| Lệch quy đổi ⇒ lệch tồn | Sai quy đổi đơn vị tính dẫn tới lệch tồn |
| đổi Lot ⇒ QC tự về HOLD | đổi lô thì trạng thái chất lượng tự về chờ kiểm |

## 13. Email trao đổi phương án với khách

Ngữ cảnh: trả lời một khách hàng về yêu cầu phát triển mới trên thiết bị cầm tay, khi chưa có estimate.

**Trước** (email dài, sáu mục đánh số, danh sách tám câu hỏi)

> Bên em đã rà soát sơ bộ quy trình và hệ thống. Trước khi bàn tới giải pháp và chi phí, em xin trao đổi với anh vài điểm về bản thân yêu cầu.
>
> ### 2. Bắn lại pallet ID là kiểm soát chồng lên chính bước 1, không phải khép kín vòng kiểm soát
>
> ... Trân trọng, [Tên] / [Công ty]

**Sau** (đoạn văn liền mạch, bốn câu hỏi, chi tiết để dành FDD)

> Em đã rà soát sơ bộ quy trình xuất hàng hiện tại. Trước khi bàn tới chi phí, em có vài điểm muốn trao đổi với anh.
>
> ... nhờ anh tạo giúp em ticket analysis để đội dev estimate nhé ạ. Anh cho em xin thêm mẫu phiếu đang dùng. Có gì chưa rõ anh cứ trao đổi lại với em.
>
> Thanks & Best Regards,

Rào đón:

**Trước**

> đây mới là hướng sơ bộ em đưa ra cho anh dễ hình dung, chưa phải phương án cuối cùng bên em sẽ làm. Phương án chính thức phải đợi đội dev phân tích và estimate xong mới chốt được, và lúc đó có thể khác với những gì em mô tả bên dưới.

**Sau**

> đây là hướng tiếp cận sơ bộ, đưa ra để anh và bộ phận kho có cơ sở chọn mục tiêu trước. Còn cách làm cụ thể và chi phí thì phải đợi đội dev phân tích, estimate xong mới chốt được.

---

## 14. Tài liệu kiến trúc và mô tả nhu cầu cho BA

Ngữ cảnh: trao đổi về giải pháp eSign cho chứng từ in trên BC, người đọc là BA.

Mức trình bày:

**Trước**

> Table "ABC ESS Print Document" (header)
> Print Doc No. Code[20] -- No. Series riêng, vd XKHO-26-00001
> Source Table No. Integer -- 32 (ILE), 110 (Sales Shpt Hdr)
>
> codeunit 74110 "ABC ESS e-Sign Facade" { procedure Sign(var RecRef: RecordRef) … }

**Sau**

> | Cột thêm | Dùng để | Ví dụ |
> |---|---|---|
> | Kho đi / Kho đến | Riêng cho Transfer | SX đến VT khác VT đến SX |

Vẫn nhắc tên bảng và tên cột khi cần, nhưng bỏ kiểu dữ liệu, bỏ cú pháp AL, bỏ code block.

Phạm vi đề xuất:

**Trước**

> Trụ 1: Thay Document Type enum bằng e-Sign Document Profile. Trụ 2: Sign Rule Matrix. Trụ 3: Tách đối tượng ký khỏi bản ghi BC. Trụ 4: Generic action surface. (kèm ba bảng cấu trúc dữ liệu và lộ trình năm giai đoạn)

**Sau**

> Rõ. Tôi bỏ phần kiến trúc dài ở trên sang một bên, trình bày lại theo hướng phạm vi nhỏ, làm được ngay.

Thể loại tài liệu:

**Trước**

> Tôi khuyên đổi key thành Document Type, Report ID, Line No. Tôi khuyên bỏ, vì Workflow User Group mà anh chọn đã làm sẵn việc đó. (kèm bảng Field | Kiểu | Lookup | Ghi chú)

**Sau**

> Tài liệu này chỉ mô tả hiện trạng và nhu cầu, không đề xuất giải pháp.
>
> Bốn phần: hệ thống hiện có, hiện trạng tại khách hàng, nhu cầu, dữ kiện đã kiểm chứng và câu hỏi chưa có đáp án.

---

## 15. Hướng dẫn xử lý sự cố gửi người dùng

Ngữ cảnh: SO bên SKV gửi IC sang Hàng gửi bán. Khách hàng chưa được gán IC Partner nên gửi IC báo lỗi, hoặc gửi đi thì PO ra toàn dòng Comment. Cách xử lý là sửa đơn bằng config package. Người đọc là người dùng và key user.

**Trước** (bản phân tích, đúng nội dung nhưng sai người đọc)

> **2. Đầu phiếu chưa có IC.** Ngoài dòng như trên, cập nhật thêm bảng 36 Sales Header:
>
> | Bảng 36 Sales Header | Giá trị |
> |---|---|
> | 1 Document Type, 3 No. | khoá |
> | 125 Sell-to IC Partner Code | `YSKH` |
> | 126 Bill-to IC Partner Code | `YSKH` |
> | 129 IC Direction | `Outgoing` (thường đã sẵn) |
> | 123 Send IC Document | `Yes` |
> | 124 IC Status | giữ `New` |
>
> Hai bẫy: Không được bỏ field 125, vì BC chỉ tạo giao dịch Outbox khi Sell-to IC Partner Code có giá trị... Đặt Validate Field = No, vì package áp field theo số thứ tự nên field 123 được validate trước 125...

**Sau** (Dũng tự viết)

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

Những gì đã bỏ: số field, bảng, cột khoá, field để mặc định (IC Direction, IC Status), giá trị của ca test (YSKH), phần giải thích bẫy. Những gì còn lại: tình huống người dùng nhận ra được, một câu hành động, và đúng năm field phải sửa. Bước nào thiếu thì làm hỏng (ví dụ Validate Field = No) thì thêm một dòng hành động, không kèm lý do. Xem nhóm 36.

## 16. Tin nhắn Zalo hướng dẫn dùng tính năng

Ngữ cảnh: chị Hân (YSKH) đang dùng mỗi item một BOM, công thức đổi thì phải mở item mới. Chị hỏi một item dùng nhiều BOM được không, rồi hỏi tiếp có phải mỗi lần tạo lệnh là chọn lại rồi refresh không. Người đọc là key user, đọc trên Zalo.

**Trước** (máy viết)

> Đúng rồi chị, mặc định BC luôn lấy version đã Certified có ngày bắt đầu gần nhất tính tới ngày của lệnh sản xuất. Nếu không có version nào hợp lệ thì nó lấy công thức gốc trên BOM.
>
> Vì vậy chị làm như sau:
> - Item vẫn giữ 1 mã, 1 Production BOM. Công thức A, B, C tạo thành 3 version trong BOM đó, cả 3 đều chuyển Certified. Version nào dùng nhiều nhất thì để ngày bắt đầu mới nhất, nó sẽ là mặc định.
> - Lệnh nào cần công thức khác thì chị mở lệnh sản xuất, ở phần Lines đổi cột Production BOM Version Code sang B hoặc C, rồi bấm Refresh Production Order.
> - Lúc refresh nhớ bỏ tick "Lines", chỉ để tick "Component Need". Nếu tick Lines thì BC tính lại dòng và trả về version mặc định.
>
> Như vậy chị không phải mở thêm item mới nữa. Muốn so sánh 3 công thức thì chị vào Production BOM Version Comparison là thấy hết.

**Sau** (Dũng sửa)

> Dạ đúng rồi chị, mặc định BC luôn lấy version đã Certified có Starting Date gần nhất tính tới ngày của lệnh sản xuất. Nếu không có version nào hợp lệ thì nó lấy BOM gốc
>
> Để dùng cho nhu cầu trên chị làm như vầy nhé: Item vẫn giữ 1 mã, 1 Production BOM. Công thức A, B, C tạo thành 3 version trong BOM đó, cả 3 đều chuyển Certified. Version nào dùng nhiều nhất thì để Starting Date mới nhất, nó sẽ là mặc định.
> Lệnh nào cần công thức khác thì trên Released Production Order, ở phần Lines đổi cột Production BOM Version Code sang B hoặc C, rồi bấm Refresh Production Order. Lúc refresh nhớ bỏ tick "Lines", chỉ để tick "Component Need". Nếu tick Lines thì BC tính lại dòng và trả về version mặc định.
>
> Ngoài ra, nếu muốn so sánh 3 công thức thì chị vào Production BOM Version Comparison là thấy đc á

Những gì đã đổi: bullet gộp thành đoạn, "ngày bắt đầu" trả về "Starting Date", "mở lệnh sản xuất" thành "trên Released Production Order", "công thức gốc trên BOM" thành "BOM gốc" theo đúng từ chị dùng. Câu kết nhắc lại cái lợi đã bị bỏ, phần so sánh chuyển thành một ý thêm mở bằng "Ngoài ra". Thêm "Dạ" ở đầu, câu dẫn nối vào nhu cầu của chị. Nội dung kỹ thuật giữ nguyên. Xem nhóm 36.

## Điều rút ra chung

Trong hầu hết các ví dụ trên, bản "sau" đều **ngắn hơn hoặc bằng** bản "trước" nhưng chứa nhiều dữ kiện hơn. Ngoại lệ là khi phải trả lại tên định danh thật đã bị lược đi, lúc đó bản sau dài hơn nhưng truy nguồn được. Nếu bản sửa dài hơn mà không thêm dữ kiện, tức là mới đổi từ chứ chưa chữa bệnh.

Câu hỏi kiểm tra cuối cùng cho mọi đoạn văn: **đoạn này có thể dán nguyên vào tài liệu của một dự án khác, một khách hàng khác, một sản phẩm khác mà vẫn đúng không?** Nếu có, viết lại.
