# Tài liệu tích hợp và mô tả logic lấy dữ liệu

Đọc khi viết tài liệu luồng tích hợp, đặc tả API, mapping trường, sơ đồ trình tự, hoặc mô tả cách lấy dữ liệu từ bảng. Gồm nhóm 31 và 40.

## 31. Mô tả logic lấy dữ liệu vòng vo

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

## 40. Tài liệu luồng tích hợp viết theo danh sách message, không theo cách người dùng làm

Rút từ tài liệu luồng tích hợp Business Central với WMS của khách A, 02/10/2026. PM trả về một loạt phản hồi trên bản v1.1. Xếp cạnh nhau thì ra bảy hướng:

| Bản giao | PM phản hồi | Hướng |
|---|---|---|
| Mũi tên trên sơ đồ trình tự ghi "M01, M02, M03, M05" | "ghi vầy trong lưu đồ sequence thì sao hiểu đc" | Nhãn trên sơ đồ phải đọc được khi đứng một mình |
| Mục "Kho và vị trí lưu trữ" giải thích vì sao không làm interface | "ko làm thì bỏ ra luôn chứ đề cập vô chi" | Không làm thì không viết |
| Item gửi kèm đơn vị tính trong một bảng, Customer gửi kèm Ship-to Address trong một bảng | "thiếu api Item UOM, thiếu Ship-to Address", "các api cho phép depend" | Bảng con trên Business Central là API riêng |
| Reopen PO, xóa Warehouse Receipt, hoàn tác gộp trong một sơ đồ, mỗi việc ba bước | "phân tích các tình huống và vẽ sequence phù hợp" | Luồng ngoại lệ phải tách tình huống |
| Hàng bán trả lại một đoạn "giống nhập hàng mua" | "sao ko thấy bạn đưa thông tin chi tiết, diagram gì vậy" | Luồng giống vẫn cần mục riêng |
| Điều chỉnh tồn ghi trạng thái "Chưa bàn" | "bàn rồi chứ chưa bàn gì" | Không gắn nhãn trạng thái khi không chắc |
| Hai mục riêng cho lệnh sản xuất và lệnh có phân bổ nguyên liệu tươi, message tên "Kết quả tiêu hao" | "đều là Released Production Order mà, gộp đi", "Output Journal, Consumption Journal" | Gộp và đặt tên theo đối tượng Business Central |

Cách viết rút ra:

- **Đặt tên message theo đối tượng Business Central.** Chiều Business Central gửi đi: tên đối tượng gửi đi (Item, Item Unit of Measure, Warehouse Receipt, Released Production Order). Chiều WMS trả về: tên chứng từ đang mở mà Business Central ghi kết quả vào rồi tự ghi sổ (kết quả nhận hàng trên Warehouse Receipt, Consumption Journal, Output Journal, Item Reclass Journal), không phải chứng từ đã ghi sổ sinh ra sau đó. Bản v1.2 đặt tên I02 là "Posted Whse. Receipt" và bị PM chê "có gì đó sai sai": WMS không gửi một phiếu đã ghi sổ, nó trả số lượng thực nhận và chi tiết lô để Business Central ghi vào Warehouse Receipt rồi tự ghi sổ. Mô tả đúng trình tự đó trong câu mở của mục. Mã ngắn (M01, P02) đi kèm để tra bảng, không đứng thay tên. Tên tự đặt như "kết quả tiêu hao" đứng một mình thì người đọc phải hỏi lại là ghi sổ vào đâu (nhóm 20).
- **Nhãn mũi tên trên sơ đồ trình tự là một câu ngắn có động từ và đối tượng.** "Gửi Item kèm danh sách Item Unit of Measure", "Gửi hủy lệnh nhập kho". Sơ đồ là thứ người ta chụp màn hình gửi đi, rời khỏi bảng mã. Kiểm tra: che bảng mã đi, sơ đồ còn hiểu được không?
- **Không làm thì không viết.** Phần đã chốt không tích hợp (kho và vị trí, Reason Code, số lô thành phẩm, cách Business Central tính tiêu hao theo định mức) không có mục, không có câu giải thích vì sao không làm. Viết ra thì người đọc tưởng còn việc. Ghi chú nội bộ thì để trong file bối cảnh dự án.
- **Mỗi bảng con trên Business Central là một API riêng, kèm câu nói rõ API cho phép gửi lồng.** Item kèm Item Unit of Measure, Customer kèm Ship-to Address. Một API riêng và một API lồng trong API cha là hai thiết kế khác nhau với bên nhận.
- **Luồng ngoại lệ phải tách theo tình huống, mỗi tình huống có bảng và sơ đồ.** Mở lại chứng từ, xóa phiếu, hoàn tác, trả hàng. Bảng tình huống năm cột: Tình huống, Người dùng làm, Business Central, WMS, Kết quả. Sơ đồ chia dải theo từng tình huống, số bước đếm lại từ 1 trong mỗi dải. Một câu "Reopen thì gửi hủy, WMS từ chối thì báo lỗi" là chưa phân tích: còn tình huống đã nhận một phần, đang nhận dở, cần nhận thêm, kỳ đã khóa.
- **Luồng giống luồng khác vẫn có mục riêng đủ sơ đồ, dữ liệu khác biệt và tình huống.** Câu "giống nhập hàng mua" chỉ là câu mở đầu. Ngay sau đó nêu điểm khác: Sales Return Order kế thừa lô, hạn dùng, liên kết bút toán gốc từ phiếu xuất, nên lệnh nhập kho đã có lô. Người đọc phụ trách hàng trả không đọc mục nhập hàng mua.
- **Gộp mục theo chứng từ Business Central, không theo biến thể nghiệp vụ.** Lệnh sản xuất thường, lệnh có phân bổ nguyên liệu tươi, lệnh đổi mã đều là Released Production Order: một mục, ba phần nhỏ. Hai mục tách nhau thì người đọc tưởng hai luồng tích hợp.
- **Không đưa ô trạng thái, cột trạng thái vào tài liệu luồng tích hợp.** Bản v1.1 gắn "Chưa bàn" cho thứ đã bàn, bản v1.2 đổi sang "Đã chốt ngày..." ở đầu mỗi mục và cột Trạng thái trong bảng, PM bỏ cả hai. Chốt hay chưa là chuyện quản lý, chỗ của biên bản và bảng điểm cần làm rõ. Phần mình bổ sung ghi chữ "Đề xuất" ở cột ý nghĩa của đúng dòng đó là đủ. Nội dung không thấy trong biên bản chưa chắc là chưa bàn: tìm trong WBS, CR trước khi kết luận (S03 đối chiếu tồn đã nằm trong WBS v1.1).
- **Thấy thiếu một API thì đưa thiết kế đủ để dev làm, không viết một đoạn đề xuất.** Bản v1.2 có S03 là một đoạn văn liệt kê sáu trường. PM: "đề xuất cho tôi việc custom trên BC thì thêm bảng gì, field nào, từ đó đưa api cho infolog gọi". Bản đúng có sơ đồ luồng, bảng Field, Kiểu, Dùng để cho từng bảng mới, bảng các lần gọi API (WMS gửi gì, Business Central làm gì), bảng trường message và cách Business Central xử lý.
- **Nhãn lặp nhiều lần thì viết gọn theo cách người dùng gọi.** "Business Central gửi WMS" lặp ở mọi dòng cột Chiều, PM đổi thành "BC qua WMS", "WMS qua BC". Đây là ngoại lệ có chủ ý cho quy tắc không viết tắt BC: chỉ áp cho nhãn chiều và cho tên lane, tên hệ thống trong lưu đồ (anh PM 07/10/2026: "trong lưu đồ, để tiết kiệm diện tích thì nên viết BC"). Câu văn vẫn viết đủ "Business Central gửi sang WMS".
- **Tên nhóm trong bảng trường theo cách dev và đối tác gọi cấu trúc message:** Message header, Chi tiết. Không dùng "Đầu message", "Đầu phiếu", "Dòng".

Lượt phản hồi trên bản v1.3 (02/10/2026). PM: "sao bạn đọc được cả source code mà có thể làm tài liệu api ở mức quá nông cạn như vậy". Bảng trường v1.3 là một danh sách phẳng, mỗi dòng một cặp dòng phiếu và lô. Nó không trả lời được câu hỏi đầu tiên của dev: một dòng phiếu có nhiều lô thì gửi thế nào. Những điều tài liệu API phải có:

- **Cấu trúc message theo cấp, đúng với cách Business Central lưu dữ liệu.** Lô nằm ở Item Tracking Lines (Reservation Entry) trên dòng chứng từ gốc, không nằm trên dòng phiếu kho. Vì vậy message có ba cấp: message header, chi tiết (lines), lô (trackingLines trong từng dòng). Dòng nhóm của bảng trường ghi rõ mỗi line ứng với cái gì ("Chi tiết (lines): mỗi line là một dòng phiếu nhập kho"). Không viết "phần tử", "mỗi phần tử chi tiết": PM bắt "nghe AI quá vậy, từ chuyên ngành là gì" (07/10/2026). Dùng đúng tên trong JSON: line, lines, trackingLine.
- **Khóa ở từng cấp.** Lô Business Central đã gửi đi thì phải có khóa để nhận về đúng record. PM chỉ định dùng Entry No. của bảng 337, Business Central gửi vào trường Line No của WMS, WMS trả lại khi gửi kết quả.
- **Số tổng ở cấp dòng.** PM: "cho tôi số tổng của Document No, Source No, Source Line No, ví dụ lot1: 10, lot2: 5, tổng là 15 để truyền vô Quantity to Ship hay Quantity to Receive". Ghi trường đích, kèm ví dụ số trong cột ý nghĩa.
- **Trường đích phải là trường người dùng nhập được trên Business Central, và tên trường message đặt gần tên đó.** Bản v1.4 ghi số tổng vào "Warehouse Receipt Line: Qty. to Receive (Base)" và đặt tên totalQuantityBase, lô thì tên quantityBase ghi vào Qty. to Handle (Base). PM: "Qty. to Receive (Base) trên Warehouse Receipt Line đâu có input vô field này được", "field trong message là quantityBase, nó cũng phải giống hoặc gần giống với BC chứ, thì nó cũng là qtyToHandleBase". Trường (Base) của dòng chứng từ do Business Central tự tính từ số lượng và Qty. per Unit of Measure. Bản đúng: qtyToReceive, qtyToShip, quantity, outputQuantity kèm unitOfMeasureCode ở cấp dòng, qtyToHandleBase ở cấp lô. Chọn trường đích như vậy kéo theo phải xử lý quy đổi đơn vị: phiếu gửi đi kèm Qty. per Unit of Measure, Business Central kiểm số dòng quy đổi bằng tổng lô, và trường hợp lẻ không tròn đơn vị là điểm cần chốt. Kiểm: mở trang Business Central, trường đích có nhập được không? Tên trường message đọc lên có nhận ra trường Business Central không?
- **Mỗi trường chiều về phải trả lời được: Business Central chưa biết giá trị này à, và có dùng nó không?** Bản v1.5 bắt WMS gửi unitOfMeasureCode trong kết quả nhận hàng. PM: "cái này trên WR sao bắt truyền về BC chi nữa", đơn vị của dòng Business Central đã có. Cùng lần đó PM gạch vendorLotNo, productionNote của lô, rồi dặn "tương tự với các phần còn lại": rà mọi message chiều về, bỏ trường Business Central đã biết hoặc không dùng.
- **"Bắt buộc" phải đúng với mọi cách người dùng thao tác, không chỉ luồng chuẩn.** Bản v1.5 ghi entryNo bắt buộc với Sales Return Order vì dòng lấy từ Get Posted Document Lines to Reverse có sẵn lô. PM: "trường hợp ngta get xong xóa tracking thì sao". Trước khi ghi "bắt buộc", hỏi: người dùng có thể xóa, sửa, bỏ qua bước tạo ra dữ liệu này không? Có thì ghi "có điều kiện" và mô tả nhánh còn lại.
- **Bảng trường hợp quan hệ một-nhiều.** Một dòng nhiều lô. Nhiều dòng phiếu kho cùng một dòng chứng từ gốc (dòng đã tách). Một lô trên nhiều pallet. Lô đã có trên chứng từ nhưng không có trong lần gửi này. Nhận một phần. Mặt hàng không theo dõi lô. Với mỗi trường hợp ghi đối tác gửi gì, Business Central làm gì.
- **Quy tắc theo loại chứng từ gốc.** Cùng một message, mỗi loại chứng từ ghi lô theo cách khác nhau. Transfer Order chỉ được sửa Qty. to Handle theo Entry No., không thêm lô. Purchase Order thì thêm lô mới. Viết thành bảng: loại chứng từ, đối tác gửi gì, Business Central làm gì.
- **Một ví dụ message ngắn** cho trường hợp khó nhất (dòng tách, nhiều lô). Mỗi dòng ví dụ phải vừa khung, không để ngắt giữa chừng.
- **Thiết kế mới thì tự thiết kế, không lấy lớp tích hợp cũ làm mẫu.** Tôi định đọc lớp API của WMS cũ để chép cấu trúc, PM chặn lại: "sao bạn phải đọc lớp API WMS cũ, đây là infolog, làm lại mới hoàn toàn mà". Đọc code là để lấy dữ kiện về Business Central của khách: bảng, trường, trường riêng, cách chuẩn xử lý lô. Không đọc để sao chép một interface cũ.
- **Nhãn trường dùng đúng chữ PM gọi:** Source No. là "số chứng từ gốc", Source Line No. là "số thứ tự dòng trên chứng từ gốc" (cùng hướng "nguồn" thành "gốc" ở nhóm 38). Trường không ai dùng tới thì bỏ, ví dụ người thao tác trên WMS (infologUser).
- **Trường có sẵn trên Business Central thì dùng trường đó.** Trước khi đề xuất "trường mới", tra trường trên đối tượng Business Central và mã nguồn. Bản v1.1 đề xuất cờ khóa lô mới trong khi Item Card đã có Auto Block Lot on WR.
- **Quyết định người dùng nêu trong phiên thắng biên bản, WBS, CR cũ.** Ghi ngay vào file bối cảnh dự án, rồi rà cả tài liệu theo quyết định đó (nhóm 27, mục "sửa một chỗ mà không rà cả họ").

Lượt 05/10/2026: Trang sửa thẳng bản v1.6 trên SharePoint, không bật Track Changes, kèm một comment. PM nhờ review rồi "theo bạn thấy hợp lý thì đề xuất rồi làm", "phân tích và sửa các phần còn lại". Cách làm rút ra:

- **Bản người khác sửa thẳng thì so với bản gốc để tìm chỗ sửa.** Mở file bằng Word, lưu bản sao, so text theo từng ô bảng, vì diff phẳng không cho thấy một dòng chuyển từ message header xuống Chi tiết.
- **Mỗi chỗ sửa xếp vào một trong ba nhóm.** Giữ: hợp với chốt và với code. Sửa lại: trái chốt đã ghi trong file bối cảnh (Trang đổi trường đích về Qty. to Receive (Base), trong khi chốt 02/10 là Qty. to Receive). Làm rõ rồi tự quyết: tra code để chọn nguồn đúng (ngày ETD, ETA Trang ghi "Purchase Order line", code có sẵn trường ETD, ETA riêng trên Warehouse Receipt Line), rồi ghi lý do trong chat.
- **Một sửa đúng ở một message thì áp cho message đối xứng và cho mọi message cùng quy tắc.** Đưa loại chứng từ gốc xuống Chi tiết ở I01 thì O01 cũng vậy. Bỏ tách dòng Warehouse Receipt thì bỏ luôn trường hợp tách dòng ở O02. Quy tắc một lô một hạn dùng thêm ở I02 thì rà luôn S01, S02, P03 và bảng lỗi.
- **Bỏ một trường mà quy tắc khác còn dựa vào nó thì giữ trường đó.** Trang bỏ "Loại chứng từ gốc" ở I01 nhưng lại thêm quy tắc Entry No. theo loại chứng từ. Giữ trường, chuyển xuống đúng cấp.
- **Đề xuất bỏ một gap thì tra code xem gap đó phục vụ luồng nào** trước khi đồng ý, rồi chỉ ra phần việc kéo theo (ẩn nút, tắt tách dòng thuộc phần gỡ Tasklet).
- **Bản mới đưa lên chỗ chung thì đặt tên file mới, không ghi đè bản của người khác.**

Lượt QA toàn bộ luồng 06/10/2026 ("có điểm nào chưa smooth, cần con người can thiệp không, bất đồng nhất giữa các quy trình tương đương không"). Bốn chỗ hay sót khi tự rà tài liệu luồng:

- **Một quy tắc nằm ở nhiều chỗ: chữ bước, hình, bảng trường, bảng lỗi.** Bảng ghi lô cho nhận lô khác, nhưng bước quy trình, hình trình tự và bảng lỗi vẫn ghi "kiểm lô khớp". Sửa quy tắc thì grep cả bốn chỗ, kể cả nhãn trong file dựng hình.
- **Luồng đối xứng phải có cùng bộ mục.** Nhập, xuất, hàng trả đều có bảng tình huống, riêng chuyển kho không có. Đặt các luồng cạnh nhau, mục nào luồng này có mà luồng kia thiếu thì bổ sung, rồi tra code xem chức năng chuẩn tương ứng có tồn tại không (Undo Transfer Shipment có trong Business Central 27).
- **Cùng một loại thao tác thì cùng một cách gọi.** Hủy, đóng phiếu kho gọi WMS trước và cho WMS từ chối khi còn lần quét chưa đóng, còn đổi trạng thái lệnh sản xuất lại đi qua tác vụ nền. Thao tác nào làm WMS mất việc đang dở thì phải gọi đồng bộ như nhau.
- **"Con người can thiệp" gồm cả thiết lập Business Central làm chặn ghi sổ.** Liệt kê thiết lập nào sai thì tích hợp lỗi mà WMS không tự sửa được (Require Put-away, Pick, Prod. Consump. Whse. Handling, Over-Receipt Required Approval, Allow Posting, Shipping Advice), kiểm tên trường trong code chuẩn trước khi ghi.
