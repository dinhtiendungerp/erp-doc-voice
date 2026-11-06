# Email và tin nhắn

Đọc khi soạn email, tin Zalo, Teams, hướng dẫn xử lý sự cố hay câu trả lời cho thắc mắc nghiệp vụ của người dùng. Gồm nhóm 26, 34, 36. Giọng email chi tiết hơn nằm ở skill `mail-voice`.

## 26. Email viết như tài liệu

Email và tài liệu là hai thể loại khác nhau. Email có heading đánh số, có sáu mục, có danh sách tám câu hỏi thì không ai đọc.

Với email: bỏ heading, viết thành đoạn văn liền mạch, giữ đúng phần phản biện và đề xuất bước tiếp theo, tối đa ba bốn câu hỏi. Phần chi tiết để dành cho FDD.

Giọng cũng khác: email dùng giọng nói chuyện với người thật, có "nhờ anh tạo giúp em", "nhé ạ", "anh cho em xin thêm". Kết thư ngắn, không dựng khối chữ ký trang trọng. Chi tiết xem skill `mail-voice`.

**Email gửi kèm file không kể lại nội dung file.** Bị bắt khi gửi WBS khách A cho anh Phong, qua hai lượt: "gì dài dòng quá vậy", rồi "nhờ anh xác nhận giúp em hai việc => ko cần". Bản nháp đầu có tổng ngày công chia theo vai trò, ba dòng chi tiết 20 MD làm với WMS kèm mã hạng mục và ngày, phương án Tasklet, lịch go-live, bốn việc nhờ xác nhận và hạn trả lời. Bản PM chốt còn bốn câu:

> Em gửi anh file **KhachA_WMS_WBS_v1.1.xlsx**. Tổng khối lượng là 103.5 MD. Trong đó, 20 MD làm việc cùng WMS em tách riêng ở sheet Tổng quan để anh tiện trao đổi. Hỗ trợ sau go-live em để 3 MD, phát sinh sau đó sẽ đi qua ticket.
>
> Có gì chưa rõ anh cứ trao đổi lại với em.

Ba điều rút ra:

- **Email chỉ giữ con số người nhận cần để quyết định, và chỉ đường tới chỗ còn lại trong file.** Chi tiết đã có trong file thì email nói nó nằm ở sheet nào, không chép lại.
- **Không tự thêm việc nhờ người nhận làm.** Người dùng không giao việc đòi xác nhận thì email không có danh sách xác nhận và hạn trả lời. Các điểm mở của dự án là chỗ của biên bản họp hay sheet điểm cần chốt, không phải email gửi file.
- **Không đưa lập luận nội bộ vào email gửi khách.** Vì sao chọn phương án nào, lịch đối tác sẽ đổi ra sao, là chuyện nội bộ hoặc chuyện của tài liệu phương án.

Kiểm tra: bỏ câu này đi, người nhận mở file ra có hiểu sai hay làm sai gì không? Không thì bỏ.

**Bị chê "dài dòng" thì xem phần nào dài: email hay lời mình viết kèm trong chat.** Email gửi WMS file đặc tả và mapping tích hợp khách A, 15/10/2026, PM soạn cho Trang gửi. Bản nháp đầu có đủ các ý được giao, kèm năm ghi chú trong chat (xưng hô, Cc đề xuất, hạn trả lời, file PDF cũ trên SharePoint, bản Excel trong máy đã cũ). PM nói "dài dòng quá vậy". Tôi cắt email còn bốn câu, bỏ tên cột cần điền, danh sách nội dung tài liệu API, chữ API v2.0. Bản PM chốt gần như bản nháp đầu:

> Dear chị Linh,
>
> NaviWorld gửi hai file tài liệu tích hợp Business Central với WMS:
> - khách A_WMS_Integration Specification_v1.0.docx: tài liệu đặc tả tích hợp
> - khách A_WMS_Integration Mapping_v1.0.xlsx: mapping trường, mỗi message một sheet
>
> Với các message chiều BC qua WMS, có đề cập các field mà BC sẽ gửi, để WMS tham khảo khi thiết kế API nhận. Nhờ WMS điền tên field tương ứng vào cột "Trường WMS" và "Ghi chú của WMS" trong file Excel, đồng thời gửi giúp em tài liệu API của WMS (tên trường, đường dẫn API, cách xác thực, cấu trúc response).
>
> Với các message chiều WMS qua BC, WMS gọi API v2.0 của BC theo endpoint và ví dụ request, response trong tài liệu đặc tả.
>
> Theo lịch của WMS, hai bên viết đặc tả tích hợp từ 15-21/10, review và ký từ 22-23/10. Nhờ WMS gửi lại file Excel và tài liệu API trước ngày 21/10 nhé.
>
> Có gì chưa rõ chị cứ trao đổi lại với em.

Năm điều rút ra:

- **Ý người giao việc đã liệt kê thì email giữ đủ.** Kể cả danh sách ngắn trong ngoặc như "tên trường, đường dẫn API, cách xác thực, cấu trúc response": đó là thứ người nhận phải gửi lại, thiếu thì họ gửi thiếu hoặc hỏi lại. Phần thừa nằm ở năm ghi chú trong chat. Bản nháp giao kèm tối đa một hai dòng, chỉ điều người dùng phải sửa trước khi gửi.
- **Email cho đối tác kỹ thuật dùng chữ nói chuyện.** "BC", "field", "15-21/10", "22-23/10". Quy ước viết đủ "Business Central", "trường", "từ 15/10 tới 21/10" là của tài liệu, không áp cho email. Tên cột trong file thì chép đúng chữ trong file ("Trường WMS").
- **Hỏi ai đứng tên gửi trước khi chọn xưng hô.** Email này PM soạn cho Trang gửi, nên "chị" là cách Trang gọi Linh, không phải cách PM gọi. Bản nháp mặc định người gửi là PM, lại không biết gọi Linh là anh hay chị nên viết "WMS cứ trao đổi lại với em". PM sửa thành "chị cứ trao đổi lại với em". Chưa rõ người gửi hay xưng hô thì hỏi người dùng một câu, không lấy tên công ty thay đại từ để né. "Nhờ WMS điền", "Nhờ WMS gửi lại" vẫn giữ, vì đó là việc của cả bên WMS.
- **Lời chào một người nhận chính.** Bản nháp chào "chị Linh, anh Hùng", PM chỉ chào chị Linh, đầu mối phân tích nghiệp vụ. Người còn lại nằm ở To hoặc Cc.
- **Mốc lịch ghi đủ việc hai bên làm ở mốc đó**: "review và ký từ 22-23/10", không chỉ "ký". PM cũng bỏ câu chỉ thư mục SharePoint, email chỉ còn tên hai file.

## 34. Đoạn kết tóm tắt lại bài

Viết xong phần nội dung rồi thêm một đoạn kể lại những gì vừa nói: "Như vậy, tài liệu đã trình bày...", "Với các bước trên, người dùng có thể...". Nhóm 13 bắt chữ "Tóm lại" ở cuối đoạn; nhóm này bắt cả đoạn kết, kể cả khi không có chữ "Tóm lại" nào.

Cách kết đúng tùy loại tài liệu:

- **Email**: kết bằng việc cần ai làm, trước ngày nào. "Anh xác nhận giúp em danh sách Location trước thứ Sáu nhé ạ."
- **FDD, FRD, Quick Guide, tài liệu bàn giao**: dừng ở mục hoặc bước cuối cùng. Không thêm đoạn kết.
- **Báo cáo, biên bản**: kết bằng điểm còn mở và bên chịu trách nhiệm, không kết bằng nhận định chung.
- **Bài viết chia sẻ** (Confluence, bài đăng): dừng ở chi tiết đắt nhất, hoặc một câu hỏi ngắn nếu thật sự muốn người đọc phản hồi. Không dùng câu hỏi mở trong tài liệu gửi khách hàng.

Kiểm tra: xóa đoạn cuối đi, người đọc có mất thông tin gì không? Không thì xóa.

## 36. Hướng dẫn xử lý sự cố cho người dùng viết như báo cáo phân tích

Sau khi tìm ra nguyên nhân một lỗi, bản giải thích cho người trong nhóm dự án có số field, cơ chế BC, hai kịch bản, các bẫy khi làm. Đem nguyên bản đó làm hướng dẫn cho người dùng hay key user là sai thể loại. Người dùng chỉ cần biết hai thứ: gặp tình huống nào thì làm, và làm gì.

Bị bắt ở lỗi gửi IC SO từ khách B sang công ty con. Bản phân tích có hai bảng kèm số field (125, 126, 123...), thêm mục Validate Field, IC Direction, IC Status và thứ tự áp field. PM tự viết lại thành hướng dẫn gửi người dùng như sau:

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
- **Giá trị thay đổi theo từng đơn thì ghi bằng tên chung** ("mã IC", "mã hàng"), không lấy giá trị của một ca test (khách B, SP0000123). Đây là hướng dẫn dùng lại nhiều lần, khác với ví dụ minh hoạ ở nhóm 25.
- **Không giải thích cơ chế.** Chuyện vì sao BC không tự gán thì để dành cho Issue Log hay tài liệu nội bộ.
- **Giọng tin nhắn gửi người dùng**: "anh chị", "nhé", "mấy field này". Cùng giọng với nhóm 26.

Lưu ý ranh giới: bỏ phần giải thích, không có nghĩa là bỏ một bước mà thiếu nó thì làm sẽ hỏng. Bước nào bắt buộc (ví dụ phải tắt Validate Field thì package mới áp được) thì thêm đúng một dòng hành động, vẫn không giải thích vì sao. Có điểm như vậy thì chỉ ra cho PM, đừng tự chèn cả đoạn lý do vào hướng dẫn của PM.

Kiểm tra: người dùng làm theo được mà không phải hỏi lại không? Bỏ một dòng đi thì họ có làm sai không? Không làm sai thì bỏ dòng đó.

**Cùng nhóm: trả lời một thắc mắc nghiệp vụ của người dùng.** Bị bắt ở khách B, phiếu nhập không undo được vì hàng đã chuyển kho, hàng hư trả nhà cung cấp mà không có hóa đơn. Kế toán hỏi: "k có hóa đơn thì sao chị làm Purchase Invoice được". Bản nháp có ba đoạn: PO treo số lượng đã nhận chưa có hóa đơn, công nợ âm; ba bước ghi số PPR cụ thể, giữ VAT08, cùng đơn giá, cùng ngày; rồi TK 133110 và một cặp PPI/PPCM tháng trước làm bằng chứng. PM tự viết lại như sau:

> PI trên BC không hẳn là ghi nhận hóa đơn GTGT đâu chị. Đây là chứng từ để kết thúc quy trình mua hàng, nếu chị đã phát sinh nhập kho rồi mà không undo được thì bắt buộc phải làm PI để kết thúc quy trình, chứ ko là ko đóng sổ được đâu.
>
> Về quy trình thì vẫn phải làm theo các bước như trên, còn về chi tiết, không muốn nó lên bảng kê đầu vào thì chị làm các phần sau giúp em
> 1. Chỗ Vendor Invoice No. trên PI và Vendor Cr. Memo No. trên PCM chị ghi cùng một số, ví dụ số PO, miễn sao giống nhau và không để trống là đc
> 2. Khi in bảng kê VAT Input, tick vô Exclude Reverse. Các cặp cùng số ở mục 1, cùng giá trị trong kỳ sẽ không lên bảng kê

Năm điểm khác bản nháp:

- **Gỡ đúng chỗ hiểu lầm bằng khái niệm nghiệp vụ.** Người hỏi đang đồng nhất PI với hóa đơn đỏ. Câu đầu tách hai thứ đó ra ("không hẳn là ghi nhận hóa đơn GTGT"), rồi nói PI dùng để làm gì bằng ngôn ngữ kế toán: kết thúc quy trình mua hàng, không làm thì không đóng sổ được. Không kể cơ chế BC (số lượng treo trên PO, công nợ âm).
- **Không nhắc lại quy trình đã gửi.** "vẫn phải làm theo các bước như trên", chỉ thêm phần chi tiết đúng mối lo của người hỏi (không lên bảng kê).
- **Ghi quy tắc, không ghi một giá trị cụ thể.** "cùng một số, ví dụ số PO, miễn sao giống nhau và không để trống" thay cho "ghi PPR-0000-00001". Ví dụ lấy thứ người dùng quen tra (số PO), không lấy số chứng từ do mình chọn. Nêu giá trị cụ thể thì người đọc hỏi ngay "sao phải là số đó".
- **Kết quả của report nói bằng một vế, không kèm bằng chứng.** "các cặp cùng số, cùng giá trị trong kỳ sẽ không lên bảng kê". Phần đã chạy report ba tháng, đếm dòng, cặp PPI/PPCM mẫu, TK 133110 là để người tư vấn tự chắc chắn, không đưa cho người dùng.
- **Không kể chuyện sửa lời trước đó.** Gợi ý cũ (đổi sang KKKNT) chưa gửi khách thì không cần câu "chị bỏ qua cách em nói trước".

Kiểm tra: câu đầu có trả lời đúng câu người dùng hỏi không, hay đang trả lời câu mình muốn giải thích? Có con số nào người dùng sẽ hỏi lại "sao lại là số này" không?

**Cùng nhóm: tin nhắn Zalo hướng dẫn dùng một tính năng.** Tình huống ở khách B: chị Thu hỏi một item dùng nhiều BOM được không. PM đã trả lời là dùng BOM Version, chị hỏi tiếp có phải mỗi lần tạo lệnh là chọn lại rồi refresh không. Bản nháp máy viết có câu dẫn "Vì vậy chị làm như sau:", ba bullet, và câu kết "Như vậy chị không phải mở thêm item mới nữa." PM sửa thành:

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

**Cùng nhóm: tin nhắn Zalo giải thích một con số khách thấy lạ.** Tình huống ở khách A, 20/10/2026: key user chụp Item Ledger Entries, hỏi "sao dòng trên là huỷ dòng dưới mà giá vốn nó khác nhau vậy e". Đã đọc code statement posting của LS để chắc nguyên nhân. Bản tôi soạn:

> Dạ anh, khi trả hàng trên POS, kể cả trả theo hóa đơn gốc, LS Central chỉ liên kết ở mức giao dịch bán lẻ. Lúc post statement, dòng trả vào kho như một lần nhập lại, không đi theo dòng bán cũ. Nên giá vốn dòng trả lấy theo giá vốn mã hàng tại ngày trả (1,250,000), không lấy lại 1,180,000 của ngày bán. Chênh lệch là do giá vốn mã này đã đổi giữa hai ngày. Số lượng tồn vẫn đúng ạ.

PM gửi:

> Dạ khi trả hàng trên POS, kể cả trả theo bill gốc, LS nó chỉ link ở mức giao dịch bán lẻ. Lúc post statement, dòng trả vào kho như một lần nhập lại, ko đi theo gd bán cũ. Nên giá vốn dòng trả lấy theo giá vốn mã hàng tại ngày trả (1,250,000), không lấy lại 1,180,000 của ngày bán

Bốn chỗ khác bản nháp:

- **Dừng ở câu đã trả lời xong.** Khách hỏi vì sao giá vốn khác. Câu có hai con số đã là câu trả lời, nên câu kết ở đó. "Chênh lệch là do giá vốn đã đổi giữa hai ngày" chỉ nói lại câu trước bằng chữ khác. "Số lượng tồn vẫn đúng ạ" là trấn an điều khách không hỏi, lại gợi ra một mối lo khách chưa có.
- **Dùng từ khách và nghề dùng hằng ngày, không dùng từ chuẩn hóa của tài liệu.** "bill gốc" chứ không "hóa đơn gốc" (ở bán lẻ, hóa đơn dễ hiểu nhầm là hóa đơn VAT), "link" chứ không "liên kết", "gd bán cũ" chứ không "dòng bán cũ". Tên sản phẩm gọi ngắn như người trong nghề: "LS nó", không "LS Central".
- **Không chèn lại xưng hô khi tin nhắn đang nối tiếp một câu hỏi.** "Dạ" là đủ, bỏ "anh" ngay sau, vì khách vừa hỏi và tin nhắn trả lời nằm ngay dưới.
- **Viết tắt kiểu chat được dùng trong Zalo**: "ko", "gd", không có dấu chấm cuối. Chỉ áp cho tin nhắn, không áp cho email hay tài liệu (nhóm 36).

Kiểm tra: câu cuối có đang nói lại câu trước, hoặc trấn an một điều khách không hỏi không? Có từ nào khách không tự nói ra khi hỏi (hóa đơn, liên kết, LS Central) mà đổi được sang từ họ quen không?

**Cùng nhóm: tin nhắn Zalo hỏi lại khách để làm rõ một yêu cầu customize.** Tình huống ở một dự án retail, tháng 10/2026: key user nhờ thêm action rã BOM cả batch Item Journal (Document No. theo một tiền tố riêng, recipe LS lồng nhiều cấp). Bản tôi soạn có năm câu hỏi, câu nào cũng kèm gợi ý, thêm câu xin batch mẫu, mở bằng "Em có xem sơ bộ yêu cầu của chị". PM gửi bản sau:

> để hiểu đúng chị xác nhận giúp em mấy ý nha:
>
> 1. Trong recipe của BTP có component lại là BTP khác có recipe? Trường hợp đó, chị có muốn rã hết tới cấp cuối cùng ko? Có trường hợp ngoại lệ mà ko muốn rã ko?
> 2. Cùng một NVL rã ra từ nhiều BTP, hoặc NVL đó đã có sẵn trong batch của Item Journal, thì chị muốn cộng gộp thành 1 dòng (group by) hay giữ riêng từng dòng (line by line)?
> 3. Dimension chuẩn hỏi trên từng dòng. Chạy cả batch thì chị muốn hỏi 1 lần rồi áp cho tất cả, hay hỏi riêng từng mã gốc?
>
> Còn để phát triển theo yc này, nhờ chị trao đổi nội bộ rồi thông qua anh Nam gửi yêu cầu qua mail hoặc ticket giúp em nhé.

Năm chỗ khác bản nháp:

- **Chỉ hỏi điều khách phải quyết và câu trả lời làm đổi thiết kế.** Câu "có ghi mã gốc vào Description không" là ý mình tự thêm, khách không nêu. Câu "mã không có recipe thì để nguyên đúng không" thì consultant tự quyết được. Cả hai bị bỏ. Câu xin batch mẫu cũng bỏ: hỏi mẫu là việc của bước phân tích sau khi có yêu cầu chính thức.
- **Câu hỏi mở, không gài sẵn ví dụ của mình.** Bản nháp viết "ví dụ BTP đó có kiểm tồn riêng, hoặc BOM Method khác Explode at Posting". PM tách thành hai câu: mặc định có rã hết không, rồi có ngoại lệ nào không. Gợi ý trước thì khách dễ chọn theo gợi ý thay vì nói trường hợp thật của họ.
- **Phương án lựa chọn kèm tên kỹ thuật ngắn trong ngoặc**: "(group by)", "(line by line)". Hai chữ đó dùng lại được khi viết FDD và trao đổi với dev. Dùng "component", "batch của Item Journal" như trên màn hình.
- **Hỏi để hiểu, không hứa làm.** Bỏ câu "làm được chị". Khách chưa gửi yêu cầu qua kênh chính thức thì tin nhắn chỉ làm rõ nhu cầu, câu cuối chỉ kênh gửi yêu cầu (trao đổi nội bộ, qua người phụ trách bên khách, mail hoặc ticket).
- **Mở thẳng vào việc nhờ**: "để hiểu đúng chị xác nhận giúp em", không kể "em có xem sơ bộ".

Kiểm tra: từng câu hỏi, nếu khách trả lời thì thiết kế có đổi không? Có câu nào mình tự quyết được không? Có câu nào đang gợi sẵn đáp án không? Có câu nào hứa làm khi yêu cầu chưa đi qua kênh chính thức không?

**Cùng nhóm: tin nhắn Teams nội bộ đề xuất giải pháp cho người trong nhóm dự án.** Tình huống ở khách B, tháng 09/2026: kho xuất sai lô so với hệ thống. Chị Hoa (consultant phụ trách) gợi ý upload lô thực tế bằng Excel lên Warehouse Shipment trước khi post. Bản nháp máy viết có sáu đoạn: lý do cách của chị vướng, đề xuất, "em đã test trên sandbox" kèm kết quả, phần kiểm soát trả hàng, điều kiện phía kho, và câu hẹn viết FDD. PM gửi bản sau:

> Chị Hoa ơi em có trao đổi với chị Mai thì cách up lot bằng Excel lên Warehouse Shipment trước khi post vẫn vướng chỗ cũ á chị, kho phải có hàng gấp cho xe thì họ xuất đại theo FEFO :D mà hầu như các đơn đều rush nên ko có thông tin lot theo thực tế trước post á, kể cả trên excel, thông thường họ ghi nhanh trên giấy.
>
> Nên chỗ này chị xem giải pháp như vầy coi đc ko nhé ạ. Kho vẫn post xuất theo lot hệ thống gợi ý để có hóa đơn đi hàng. Trong ngày, chị Mai upload file Excel lô thực tế (số phiếu xuất, mã hàng, lot thực tế, số lượng, bin), hệ thống theo 1 số logic mà mình custom, tự động sinh thêm 1 cặp lot điều chỉnh dựa theo lot đã post thông qua Item Journal, Entry Type = Sales. Ví dụ:
> - xuất bán lot A: 10pcs
> - Item Journal: sales -10pcs lot A và dùng apply to entry, Source Type = Customer, Source No = mã khách hàng
> - Item Journal: sales 10pcs lot B và dùng Source Type = Customer, Source No = mã khách hàng

Sáu chỗ khác bản nháp:

- **Lý do bác một gợi ý thì dẫn đúng người đã xác nhận, và tả đúng hành vi đã thấy ở hiện trường.** "em có trao đổi với chị Mai", "xuất đại theo FEFO", "hầu như các đơn đều rush", "họ ghi nhanh trên giấy". Bản nháp viết chung chung "lúc gấp thì họ xuất đại" và thêm lý do hóa đơn phải đi cùng hàng, điều người nhận đã biết. Máy không được tự bịa câu "em đã trao đổi với X" khi không biết; chỗ đó để người dùng điền.
- **Người nhận là consultant thì nói bằng cơ chế BC, không nói "hệ thống tự sửa".** Item Journal, Entry Type = Sales, apply to entry, Source Type, Source No. Với người cùng nghề, cơ chế cụ thể thuyết phục hơn lời mô tả kết quả, và cho họ phản biện được ngay. Cùng ý với nhóm 21: hạ mức kỹ thuật là cho khách, không phải cho đồng nghiệp.
- **Ví dụ số dạng bút toán thì để bullet được.** Mỗi dòng là một bút toán, không phải một câu nói với người đọc, nên không trái với quy tắc bullet của tin nhắn Zalo ở trên.
- **Đề xuất cho người phụ trách thì hỏi ý, không trình bày như việc đã xong.** "chị xem giải pháp như vầy coi đc ko nhé ạ", không có "em đã test", không hẹn viết FDD. Người phụ trách còn phải chốt hướng, báo trước kết quả test và bước tiếp theo là đi trước họ một bước.
- **Một tin nhắn một ý.** Phần kiểm soát trả hàng và điều kiện phía kho bị bỏ, để dành cho lượt sau hoặc cho FDD. Tin nhắn chỉ trả lời đúng gợi ý chị Hoa vừa đưa.
- **Dùng từ team dùng**: "lot" chứ không "lô", "pcs", "rush", "up". Giọng nội bộ: "á chị", "coi đc ko", có thể có ":D".

Kiểm tra: tin nhắn gửi người phụ trách có câu nào báo việc mình đã làm hay hẹn việc mình sẽ làm khi họ chưa gật đầu không? Người nhận là consultant mà câu giải pháp chỉ có "hệ thống tự xử lý", không có chứng từ, field hay giá trị nào không?

**Cùng nhóm: hướng dẫn xử lý tạm một sự cố vận hành, gửi người trực hệ thống.** Tình huống ở một dự án retail, tháng 10/2026: job Data Director đẩy dữ liệu lên BC SaaS bị treo OnHold trên host SRV-LSC, chưa rõ nguyên nhân gốc. PM nhờ "gửi phản hồi cho khách hàng để xử lý tạm và detect nguyên nhân nếu gặp lại". Bản nháp đầu là email bốn mục (hiện tượng, kết quả kiểm tra, xử lý tạm, theo dõi), có Event Viewer, lưu ý bảo mật log, câu hẹn nâng cấp bản DD. Bị nhắc "ngắn gọn thôi", bản thứ hai vẫn là email có tiêu đề, "Dear anh/chị", câu báo "em đã release, dữ liệu đã đồng bộ đủ". PM gửi bản sau:

> Như trao đổi, các job đồng bộ giao dịch bị treo trên host SRV-LSC ở trạng thái OnHold, nên dữ liệu không lên được BC. Nguyên nhân gốc chưa xác định được vì lúc xảy ra lỗi chưa bật log chi tiết.
> Nếu gặp lại, em xử lý tạm như sau:
>
> 1. Mở Job Monitor, kết nối tới host SRV-LSC, port 16860.
> 2. Chuột phải từng dòng đang OnHold (company A và company B), chọn Release Jobs off Hold. Nhớ là chọn từ cũ nhất đến mới nhất. Lúc release theo dõi nếu các job Hold mà tự chuyển sang được Processing thì em ko cần bấm release thủ công nữa nhé.
> 3. Không chọn Cancel Job vì job sẽ bị hủy, dữ liệu sẽ không được đồng bộ.
>
> Trước khi release, vô màn hình Job Monitor và gửi anh file log trong C:\ProgramData\LS Retail\Data Director\Log trên máy SRV-LSC. Anh đã bật log chi tiết sẵn, có log là xác định được nguyên nhân.

Sáu chỗ khác bản nháp:

- **Người làm theo hướng dẫn là ai thì viết cho người đó.** "Khách hàng" trong lời nhờ thật ra là người trực hệ thống bên khách, người đã cùng xử lý sự cố, nên xưng "anh - em" và viết như tin nhắn, không tiêu đề, không "Dear", không "Thanks & Best Regards". Chưa rõ người nhận và kênh gửi (email hay chat) thì hỏi một câu trước khi soạn.
- **Người nhận đã cùng xử lý thì mở bằng "Như trao đổi", không kể lại việc mình đã làm.** Bỏ câu "em đã release, dữ liệu đã đồng bộ đủ" và đoạn "kết nối lên BC và dữ liệu đều bình thường". Chỉ giữ một câu hiện tượng và một câu nói thẳng là chưa rõ nguyên nhân, kèm lý do.
- **Hướng dẫn thao tác có thứ tự thì đánh số.** Bullet chỉ hợp với các mục ngang hàng.
- **Hướng dẫn vận hành phải có thứ tự xử lý và điểm dừng.** Bản nháp chỉ có "release các dòng OnHold". PM thêm hai thứ chỉ người đã ngồi xử lý mới biết: làm từ job cũ nhất đến mới nhất, và khi thấy job tự chuyển sang Processing thì dừng, không bấm thủ công nữa. Người trực cần biết làm tới đâu thì thôi, không chỉ cần biết bấm vào đâu.
- **Việc nhờ thu thập cho lần sau chỉ giữ thứ đủ để chẩn đoán.** Bỏ Event Viewer, lưu ý bảo mật, câu hẹn nâng cấp phiên bản. Còn lại một việc là gửi file log, kèm một câu lý do để người nhận chịu làm ("có log là xác định được nguyên nhân").
- **Giọng nội bộ**: "Nhớ là", "ko cần", "vô màn hình", "nhé".

Kiểm tra: người trực đọc xong có biết bắt đầu từ dòng nào, khi nào thì dừng, và trước khi làm phải lấy gì gửi lại không? Có câu nào kể việc mình đã làm mà người nhận đã chứng kiến không?

**Cùng nhóm: hướng dẫn kế toán khách sửa chứng từ đã post.** Tình huống ngày 12/10/2026: kế toán khách post 5 phiếu item journal hàng hủy nhưng để trống Gen. Bus. Posting Group, nên tiền vào 621 thay vì 632. Anh hỏi đảo lại thế nào vì không reverse được. Bản tôi soạn có bảng 14 dòng (phiếu, mã hàng, kho, số lượng, Item Ledger Entry No.), dặn chọn đơn vị cơ sở, dặn khai Lot "nếu mã có quản lý Lot", thêm bước điền Applies-to Entry cho dòng xuất lại, đoạn kiểm G/L kèm tổng tiền, và câu nhắc "từ giờ nhớ chọn DISPOSAL". PM gửi bản sau:

> Các phiếu đã post thì mình đảo trên Item Journal, làm 2 bước sau.
>
> B1 - Đảo phiếu cũ
> 1. Với mỗi dòng trong bảng bên dưới, anh tạo một dòng Positive Adjmt. Posting Date 07/10, Item, Location, Quantity giống dòng cũ. Gen. Bus. Posting Group để trống như dòng cũ.
> 2. Ở field Applies-from Entry, anh điền số Item Ledger Entry của dòng cũ. Field này nếu đang ẩn, bật bằng Personalize.
> 3. Post. Dòng nhập lại sẽ lấy đúng giá vốn lúc xuất, nên bút toán đảo khớp, vd: N152200/155200, C621310/621320.
>
> B2 - Post lại đúng tài khoản
> 1. Anh tạo lại các dòng Negative Adjmt. như cũ, và chọn Gen. Bus. Posting Group = DISPOSAL.
> 2. Post. Kết quả: Nợ 632200, Có 152200/155200.
>
> Ở cả 2 bước, nhớ điền lại dimension cho 3 dòng: [...] => xem ILE để biết chi tiết
>
> Sau đó anh chạy Adjust Cost - Item Entries.

Sáu chỗ khác bản nháp:

- **Không chép lại dữ liệu người nhận tự xem được trên hệ thống.** Bảng 14 dòng bị bỏ, dimension từng dòng chỉ còn "xem ILE để biết chi tiết". Người nhận đang ngồi trước BC, mở Item Ledger Entries là có đủ số, chính xác hơn bảng chép tay và không lệch khi có dòng mới. Tin nhắn chỉ nói làm gì và tra ở đâu.
- **Không thêm bước không bắt buộc.** Bước điền Applies-to Entry cho dòng xuất lại chỉ để số vào 632 khớp tròn với số đã đảo. PM hỏi "sao phải thêm bước này chi", và bỏ. Hỏi từng bước: bỏ bước này thì làm có hỏng không? Không hỏng thì bỏ, dù nó làm kết quả đẹp hơn. Cùng lúc phải trả lời được câu hỏi kỹ thuật đi kèm (dòng nhập có Applies-from còn open không) bằng cơ chế thật, không đoán.
- **Không ghi nhánh mình chưa kiểm.** Câu "mã nào có quản lý Lot thì khai Lot" có mặt vì tôi không biết mã nào có Lot. Đó là chỗ phải tra trước (Item Tracking Code trên mặt hàng), không phải chỗ đẩy điều kiện cho người đọc tự lo (nhóm 7, 38). Tương tự, "Field này nếu đang ẩn" thay cho "Trường này ẩn sẵn": không khẳng định điều mình không thấy trên màn hình của họ.
- **Viết theo ký hiệu của người đọc.** Kế toán đọc "N152200/155200, C621310/621320" nhanh hơn "Nợ 152200/155200, Có 621310/621320". Gọi "field" như người dùng BC nói, không gọi "trường". Nhãn bước theo cách PM hay viết trong chat: "B1 - ", "B2 - ", không dùng "Lượt 1".
- **Trả lời đúng câu được hỏi, không thêm phần kiểm và phần nhắc.** Anh Khoa hỏi cách đảo. Đoạn kiểm G/L kèm tổng tiền và câu "từ giờ nhớ chọn DISPOSAL" bị bỏ: người hỏi đã biết nguyên nhân từ tin trước, và kế toán tự biết kiểm sổ (nhóm 15, 34).
- **Bỏ chi tiết mặc định.** "Unit of Measure chọn đơn vị cơ sở" bị bỏ, vì dòng journal tự lấy Base UoM của mặt hàng.

Cùng lần này, trước khi soạn tin, tôi còn sai ở khâu kiểm dữ kiện: đưa Inventory Posting Group vào danh sách cần xem trong khi câu hỏi chỉ về tài khoản đối ứng, bảo xem General Posting Setup thay vì xem bút toán đã post (PM: "lỡ may post xong đổi setup sao"), rồi bảo xem cột Gen. Bus. Posting Group trên G/L Entries trong khi bút toán giá vốn kho không ghi cột đó. Muốn biết đã post vào đâu thì xem entry đã post (G/L Entries, Value Entries). Setup chỉ cho biết cấu hình hiện tại, dùng để giải thích vì sao và để biết từ giờ post sẽ vào đâu.

Kiểm tra: tin nhắn có bảng hay danh sách số nào người nhận mở BC là thấy không? Có bước nào bỏ đi mà vẫn làm đúng không? Có câu "nếu..." nào mình kiểm được mà chưa kiểm không?
