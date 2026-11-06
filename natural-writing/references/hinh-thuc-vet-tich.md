# Hình thức, vết tích quy trình và đặc điểm văn người viết

Đọc ở lượt rà hình thức và lượt rà vết tích, và trước khi giao bất kỳ file nào sinh bằng script. Có cả lỗi công thức Excel, font trong hình, thuộc tính file Office và cách viết commit, ghi chú thay đổi.

## Dấu hiệu về hình thức

Nhóm này dễ sửa nhất và cũng lộ nhất. Chi tiết đầy đủ nằm ở `references/dau-vet-ky-thuat.md`.

- In đậm rải khắp nơi, đặc biệt là in đậm mọi lần xuất hiện của một thuật ngữ. Quy tắc đang áp: **chỉ in đậm ở nhãn đầu mục và phần dẫn đầu bullet**. Không in đậm giữa câu trong đoạn văn, không in đậm trong ô bảng.
- Bullet dạng "**Thuật ngữ:** câu giải thích lặp lại chính thuật ngữ đó".
- Danh sách ở chỗ hai câu văn xuôi là đủ.
- Heading Title Case tiếng Anh; heading rập khuôn: "Thách thức", "Triển vọng", "Kết luận", "Key Features".
- Emoji trong tiêu đề hoặc đầu bullet.
- Gạch ngang dài `—` ở chỗ dấu phẩy, ngoặc đơn hoặc hai chấm hợp hơn. Mô hình thường đặt **dấu cách hai bên**, trái với quy ước sắp chữ.
- Dấu chấm giữa `•` làm ký tự ngăn cách trong header trang, dòng phụ đề sheet ("KHÁCH A • TÍCH HỢP", "Bản 1.2 • 02/10/2026"). PM: "không dùng •, dùng -". Grep cả file dựng (header, footer, hàm dựng sheet), không chỉ file nội dung.
- Dấu nháy cong `’ “ ”` lẫn vào văn thuần. Đây là dấu hiệu yếu vì Word và macOS tự đổi.
- Bảng nhỏ không cần thiết, chỗ hai câu văn là đủ.
- Nhảy cấp heading, hoặc chèn đường kẻ ngang trước mỗi heading.
- Mọi mục trong danh sách dài xấp xỉ bằng nhau, cấu trúc song song hoàn hảo.

Với văn tiếng Việt: dùng `-` thay cho `—`, không dùng `→` và `⇒`. Thay mũi tên bằng từ nối thật, vì mũi tên giấu mất quan hệ giữa hai vế.

- "Gỡ Tasklet ⇒ phải gỡ hết tham chiếu" viết thành "Gỡ Tasklet thì phải gỡ hết tham chiếu"
- "Lệch quy đổi ⇒ lệch tồn" viết thành "Sai quy đổi đơn vị tính dẫn tới lệch tồn"
- "đổi Lot ⇒ QC tự về HOLD" viết thành "đổi lô thì trạng thái chất lượng tự về chờ kiểm"

Ba thứ khác bị bắt trong bản WBS khách A: **dấu chấm phẩy** (tách câu ra hoặc dùng dấu phẩy), **chữ "trực"** ở mọi dạng (trực go-live, trực tuyến, trực tiếp - viết "hỗ trợ go-live", "từ xa", "tới"), và **"lỗi mức chặn"** (viết "lỗi làm dừng quy trình").

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
- **Hình sinh bằng script có chữ chồng lên nhau.** Chú giải sơ đồ khách A đặt bốn mục cách đều nhau theo một khoảng gõ tay, nhãn dài hơn khoảng đó nên chữ đè lên mũi tên kế bên. Lượt kiểm trước chỉ xem ảnh ghép nhiều trang ở độ phân giải thấp nên không thấy, PM bắt bằng "hình bị lỗi r nè". Vị trí chữ trong hình phải tính từ độ rộng chữ đo được, và mỗi hình phải xem một lần ở đúng cỡ chèn trong tài liệu.
- **Font Calibri trong matplotlib làm mất chữ tiếng Việt có dấu.** Ở cỡ chữ lẻ (9,5; 10,5) các ký tự có dấu biến mất, chỉ còn vài dấu lơ lửng. Đã gặp ở hình timeline kế hoạch nguồn lực (08/10/2026). Dùng Segoe UI hoặc Arial, rồi xem lại ảnh đúng cỡ thật trước khi chèn. Dòng phụ đề dài cũng phải đo: một câu dài hơn khung hình bị cắt cụt ở mép phải, rút ngắn hoặc tách sang dòng khác.
- **Thuộc tính Title của file Office hiện trên thanh tiêu đề Excel, thay cho tên file.** Script ghi Title theo tên lúc dựng ("..._v1.1") rồi file bị đổi tên thành "_v1.0", người dùng mở ra vẫn thấy "_v1.1" và không biết đang mở bản nào. Để Title trống (quy tắc chung là trống hoặc đúng tên file). Số phiên bản chỉ nằm ở tên file, và mỗi bản giao dùng tên mới chưa từng dùng, vì file cùng tên bị Excel đang mở khóa hoặc bị ghi đè bằng bản cũ qua AutoSave.
- **Công thức trỏ sai cột sau khi chèn thêm cột.** Thêm một cột vào giữa bảng thì mọi COUNTIF, SUMIF, tham chiếu theo chữ cái cột ở sheet khác đều lệch một cột và vẫn chạy, chỉ ra kết quả 0. Sau khi chèn cột, mở lại các ô tổng hợp và kiểm tra giá trị.
- **SUMIF và COUNTIF ép mã dạng "x.y" về số.** Tiêu chí "5.1" và "5.10" bị Excel đọc thành cùng một số 5,1 nên cộng chéo hai dòng, ra tổng lớn hơn thật. Mã hạng mục dạng "x.y" làm khóa tra cứu thì dùng SUMPRODUCT so sánh chuỗi.
- **SUMPRODUCT phải nhận các mảng cùng kích thước.** Nhân một mảng một cột với vùng bốn cột thì LibreOffice tự giãn và ra số, còn Excel trả #VALUE!. Cộng từng cột lại thành một mảng một cột: `SUMPRODUCT((A=mã)*(F+G+H+I))`.
- **LibreOffice mở được không có nghĩa là Excel mở được.** Hai lỗi đã gặp đều thuộc loại này: công thức SUMPRODUCT ở trên, và việc vá thẳng XML trong file xlsx. Thứ tự thẻ con của `sheetPr` bắt buộc là `tabColor`, `outlinePr`, `pageSetUpPr`; chèn `outlinePr` lên trước `tabColor` thì LibreOffice vẫn mở bình thường còn Excel báo "Repaired" và bỏ sạch nội dung của cả file. Vá XML xong phải parse lại toàn bộ phần XML trong gói, kiểm thứ tự thẻ, rồi mở lại file bằng thư viện đọc trước khi gửi.
- **Bước recalc bằng LibreOffice xóa một số thiết lập trình bày**, trong đó có `outlinePr`. Thiết lập nào bị mất thì phải đặt lại sau bước recalc, không phải trước.
- **Báo đã sửa nhưng bản người dùng mở vẫn là bản cũ.** Bị bắt bằng câu "sao vẫn còn": bản sạch chỉ nằm ở phía mình, bước chép xuống thư mục của người dùng báo thành công nhưng chép một bản cũ hơn. Sau khi ghi file vào thư mục người dùng, đọc lại chính file ở đó và tìm lại đúng các cụm vừa bỏ. File đang mở trong Excel có AutoSave thì dặn đóng không lưu rồi mở lại, không thì Excel lưu đè bản cũ lên. Lần kế hoạch Thảo (08/10/2026) tôi báo "đã đổi nhãn" khi mới thấy script chạy xong, chưa mở file ra đọc nhãn, và lệnh in kiểm tra của tôi lỗi font console nên cũng không kiểm được. Bản người dùng mở vẫn là bản cũ, bị hỏi lại ba lần ("sao vẫn vậy"). Báo xong chỉ sau khi đọc lại nhãn trong chính file đã lưu, ghi PYTHONIOENCODING=utf-8 khi in tiếng Việt từ Python trên Windows.
- **Gửi kèm những file người ta không cần.** File nguồn, script sinh tài liệu, file ghi chú nội bộ thì lưu lại, không đưa vào danh sách bàn giao. Chỉ gửi đúng thứ người ta yêu cầu.
- **Gửi thiếu file trong bộ nhiều file.** Dự án có hai ba file đi kèm nhau thì lần nào cũng gửi đủ bộ, kể cả khi chỉ sửa một file. Người nhận không nhớ file nào là bản mới nhất và sẽ hỏi lại.

Bài gốc còn có một mục rất đáng học: **ghi chú thay đổi**. Ghi chú do AI viết hay trấn an thái quá rằng thay đổi đã "đảm bảo tuân thủ", "cải thiện tính trung lập", và hay nhắc tới cả những phần **không** bị sửa. Người viết thật ghi ngắn và cụ thể: sửa gì, ở đâu, vì sao. Áp dụng cho commit message, ghi chú phiên bản tài liệu, và email báo đã cập nhật.

## Đặc điểm văn người viết

Phần này nói cái **nên làm** chứ không phải cái nên tránh:

1. **Dùng "là" và "có" trần trụi.** "Có ba trường hợp", "Nó là bút toán tồn kho".
2. **Dùng từ thường thay vì từ trang trọng đồng nghĩa.** "viết" thay "chấp bút", "dùng" thay "sử dụng", "thử" thay "tiến hành thử nghiệm". Với tiếng Việt cần cân nhắc phép lịch sự khi viết cho khách hàng.
3. **Dám nói khẳng định dứt khoát.** "chỉ có một cách", "đây là lần đầu tiên", "cách tốt nhất là".
4. **Dùng từ đệm và từ nhấn.** "chắc", "hình như", "khá", "hơi", "nói chung", "thường thì".
5. **Thỉnh thoảng viết dài dòng một cách rất người.** "do đó mà", "để mà", "cái việc là".
6. **Nhịp câu không đều.** Câu năm chữ xen giữa câu bốn mươi chữ. Mỗi câu mang một, tối đa hai ý; ý thứ ba sang câu mới.
