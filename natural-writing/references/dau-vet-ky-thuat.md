# Dấu vết kỹ thuật và mã đánh dấu chatbot

Mục lục:
1. Vì sao phần này quan trọng
2. Mã đánh dấu theo từng chatbot
3. Tham số theo dõi trong URL
4. Placeholder và trường bỏ trống
5. Vết Markdown lọt vào nơi khác
6. Lỗi trích dẫn đặc trưng
7. Checklist tìm kiếm trước khi giao tài liệu
8. Dấu hiệu hình thức yếu, dễ báo động giả
9. Mất dấu tiếng Việt trong file do script sinh ra

---

## 1. Vì sao phần này quan trọng

Khác với văn phong (luôn có thể tranh cãi), các dấu vết trong phần này gần như là bằng chứng chắc chắn. Chúng lọt vào tài liệu khi người dùng copy từ giao diện chatbot rồi dán sang Word, Confluence, PowerPoint hoặc trình soạn thảo khác: phần hiển thị trên màn hình trông sạch, nhưng chuỗi ký tự nền đi theo.

Với tài liệu giao khách hàng, một mã `turn0search3` sót lại giữa đoạn văn gây thiệt hại lớn hơn nhiều so với việc dùng thừa vài chữ "quan trọng".

---

## 2. Mã đánh dấu theo từng chatbot

Bài gốc liệt kê theo từng nhà cung cấp, vì mỗi bên có lỗi riêng.

### ChatGPT

- `:contentReference[oaicite:0]{index=0}` chèn vào chỗ đáng lẽ là liên kết nguồn.
- `oai_citation` kèm ký hiệu `‡` và tên miền.
- `citeturn0search0`, số sau `search` tăng dần theo bài. Biến thể ngắn chỉ có số. Thỉnh thoảng lọt vào tên ref: `<ref name="0search12">`.
- Bộ ảnh hiển thị thành `turn0image0turn0image1...`.
- Biến thể khác: `citeturn0news0`, `citeturn1file0`.
- Mã JSON cuối câu: `({"attribution":{"attributableIndex":"1009-1"}})`.
- Dạng đuôi `Example+1` hoặc chuỗi tên nguồn dính liền nhau kiểu `IT Governance+3ISO+3ISO+3`.
- Từ tháng 6/2026 xuất hiện dạng `:::writing{variant="document" id="68427"}`, số 5 chữ số ngẫu nhiên, có thể kèm `:::` đóng ở cuối. Có bản dịch sang ngôn ngữ khác, ví dụ `:::écriture{variante="document" id="28471"}`.

### Gemini

- `[cite: 17]` hoặc `[cite: 19, 20, 21]` ở cuối câu.
- `[span_1](start_span)` và `[span_1](end_span)` bao quanh đoạn văn.

### Grok

- Thẻ kiểu XML: `<grok-card data-id="e8ff4f" data-type="citation_card">`.
- `grok_render_citation_card_json={"cardIds":["3bb883"]}`.

### DeepSeek

- Ngoặc vuông lửng kèm dấu chữ thập: `【85†L261-269】`, đôi khi có dấu cách xen vào giữa.

### Perplexity

- `[attached_file:1]`, `[web:1]` cuối câu.
- URL trỏ về bucket S3 có chứa `ppl-ai-file-upload`.

### Chung nhiều loại

- Ký tự `↩` quanh chú thích cuối trang, vốn là liên kết quay lại bài trên giao diện web.

---

## 3. Tham số theo dõi trong URL

Khi chatbot dẫn nguồn, nó hay gắn tham số vào URL:

| Chuỗi | Nguồn |
|---|---|
| `utm_source=chatgpt.com` | ChatGPT |
| `utm_source=openai` | ChatGPT |
| `utm_source=copilot.com` | Microsoft Copilot |
| `referrer=grok.com` | Grok |

Gemini và Claude ít gắn tham số hơn.

Lưu ý cách hiểu: tham số này chứng minh có dùng chatbot, nhưng không chứng minh chatbot viết ra đoạn văn. Nhiều người dùng AI để tìm nguồn cho văn bản họ tự viết.

Trước khi giao tài liệu, cắt sạch phần từ dấu `?` trở đi trong URL nếu phần đó chỉ là tham số theo dõi.

---

## 4. Placeholder và trường bỏ trống

- Ngoặc vuông chưa điền: `[Tên công ty]`, `[Your Name]`, `[Insert date]`, `[Describe the specific section]`.
- Chuỗi hoa: `INSERT_SOURCE_URL_30`, `PASTE_SPOTIFY_TRACK_URL_HERE`, `SOURCE_PUBLISHER`, `URL`.
- Ngày dạng `2025-XX-XX`, `2022-11-XX`.
- Chú thích ẩn còn sót: `<!-- EDIT BELOW THIS LINE -->`, `<!-- Add if available with citation -->`.

Trong tài liệu tư vấn, dạng nguy hiểm nhất là placeholder trông giống nội dung thật: một tên page, một object ID, một mã tài khoản được sinh ra nghe hợp lý. Không tra được thì để trống và đánh dấu rõ, không đoán.

---

## 5. Vết Markdown lọt vào nơi khác

Chatbot xuất ra Markdown vì hệ thống của nó yêu cầu vậy. Khi dán sang môi trường không hiểu Markdown (Word, Confluence phiên bản cũ, ô ghi chú PowerPoint, email HTML), cú pháp hiện nguyên hình:

- `**đậm**` và `*nghiêng*` hiện ra dạng ký tự.
- `##` đầu dòng, hoặc bị hiểu thành danh sách đánh số.
- `---` biến thành đường kẻ ở chỗ không định.
- Khối mã ba dấu ngã ngược: ```` ```wikitext ````, ```` ```markdown ````.
- Liên kết dạng `[chữ](url)` không được chuyển thành liên kết thật.

Bài gốc lưu ý ngược lại: bản thân Markdown **không** phải dấu hiệu mạnh, vì lập trình viên, người viết kỹ thuật và người dùng Reddit, Discord, Slack, Obsidian, GitHub đều gõ Markdown quen tay. Chỉ đáng ngờ khi Markdown lẫn với cú pháp của môi trường đích một cách sai lệch.

---

## 6. Lỗi trích dẫn đặc trưng

Nhóm này áp dụng khi tài liệu có dẫn nguồn: báo cáo, đề xuất, tài liệu nghiên cứu.

- **Liên kết chết hàng loạt.** Nhiều liên kết 404 hoặc tên miền không tồn tại trong một tài liệu mới, và không tìm thấy trên các trang lưu trữ. Liên kết cũ hỏng dần là bình thường; nhiều liên kết chưa từng tồn tại thì không.
- **DOI dẫn tới bài khác.** DOI trông hợp lệ nhưng thuộc về một bài không liên quan. Bài gốc dẫn ví dụ hai trích dẫn bịa hoàn toàn, trong đó một tác giả đã mất hơn 30 năm trước thời điểm được cho là viết bài.
- **ISBN sai checksum.** Kiểm tra được bằng công thức, và mẫu trích dẫn tự cảnh báo.
- **Trích dẫn sách không có số trang.** Sách có thật, chủ đề hợp lý, nhưng không có số trang thì không kiểm chứng được.
- **Có số trang nhưng trang đó không nói vậy.** Dấu hiệu đi kèm: sách thuộc loại phổ biến trong ngành, và trích dẫn không kèm liên kết tới bản trực tuyến.
- **Ref khai báo nhưng không dùng trong nội dung**, hoặc ngược lại, ref được gọi mà chưa khai báo.

---

## 7. Checklist tìm kiếm trước khi giao tài liệu

Dùng chức năng Find của trình soạn thảo, hoặc `grep` nếu là file văn bản. Tìm lần lượt:

```
contentReference
oaicite
oai_citation
turn0
attributableIndex
:::writing
[cite:
start_span
grok-card
grok_render
【
attached_file
ppl-ai-file-upload
utm_source=
referrer=grok
INSERT_
PASTE_
-XX
[Your
[Tên
```

Và các ký tự:

```
—        gạch ngang dài
–        gạch nối ngắn (kiểm tra có đúng chỗ không)
’ “ ”    nháy cong
↩        mũi tên quay lại
```

Cùng các cụm hội thoại:

```
Hy vọng
Bạn có muốn
Dưới đây là bản
Certainly
Here's the
Let me know
```

Với file Markdown hoặc văn bản thuần, chạy một lượt:

```bash
grep -nE 'contentReference|oaicite|oai_citation|turn0|attributableIndex|:::writing|\[cite:|start_span|grok-card|grok_render|【|attached_file|ppl-ai-file-upload|utm_source=|referrer=grok|INSERT_|PASTE_|-XX' file.md
```

---

## 8. Dấu hiệu hình thức yếu, dễ báo động giả

Không dùng những thứ sau làm bằng chứng khi đứng một mình:

- **Nháy cong.** Word có tính năng smart quotes, macOS và iOS bật mặc định, LanguageTool cũng đổi, và nhiều nhà xuất bản dùng nháy cong theo chuẩn sắp chữ. Gemini và Claude thường không dùng nháy cong.
- **Gạch ngang dài.** Người viết chuyên nghiệp dùng nhiều. Bài gốc ghi nhận GPT-5.1 đã được điều chỉnh để hạn chế dùng. Điểm nhận dạng cụ thể hơn là dấu cách hai bên gạch ngang dài, trái quy ước sắp chữ.
- **Ngữ pháp hoàn hảo.** Nhiều người viết nghề.
- **Định dạng đúng chuẩn.** Người dùng trình soạn thảo trực quan và nút xem trước làm đúng là chuyện thường.
- **Ký tự lạ, thẻ HTML đặt sai chỗ.** Thường do tiện ích trình duyệt kém hoặc lỗi công cụ dịch, không phải chatbot.
- **Nội dung không dẫn nguồn.** Chatbot đời mới có tìm kiếm web nên thường có dẫn nguồn, dù nguồn có thể sai.

---

## 9. Mất dấu tiếng Việt trong file do script sinh ra

Triệu chứng: nội dung trong chat có dấu đầy đủ, nhưng file .xlsx, .docx, .pptx xuất ra thì thành chữ không dấu.

Ví dụ thật: "LOGIC PHAN BO ITEM CHARGE (SALES) - PHUONG AN BY AMOUNT", "Dong thu 2 hay bi lech vi den luot no Qty con lai la 0.66667", tên sheet "4. VD khong deu", "5. Tinh tu dong".

Lỗi nằm ở khâu sinh file, không nằm ở khâu viết, nên đọc lại bản nháp trong chat sẽ không phát hiện ra. Ba chỗ hay bị nhất và cũng hay bị bỏ sót nhất: **tên sheet, tiêu đề cột, phần diễn giải dài**.

Checklist trước khi giao file:

1. Mở file vừa xuất, không tin bản nháp trong chat.
2. Đọc tên sheet hoặc tên slide trước, đây là chỗ hay sót nhất vì nằm ngoài vùng nội dung chính.
3. Đọc dòng tiêu đề và một dòng diễn giải bất kỳ.
4. Nếu đã mất dấu: sửa ở nguồn sinh file rồi xuất lại, không sửa tay trong file.

Cùng nhóm với lỗi này: dấu tiếng Việt bị vỡ thành ký tự lạ do sai encoding, và font không có glyph tiếng Việt làm chữ hiện thành ô vuông trong PDF hoặc PowerPoint.
