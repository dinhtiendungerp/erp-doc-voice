# erp-doc-voice

Agent skill giúp viết tài liệu tư vấn ERP bằng tiếng Việt mà không mang giọng văn AI.

Skill này khác các công cụ "humanize" thông thường ở hai điểm. Thứ nhất, nó viết cho tiếng Việt, có xử lý những thứ chỉ tiếng Việt mới gặp như dấu nháy cong do Word tự đổi, gạch ngang dài, và phép lịch sự khi xưng hô với khách hàng. Thứ hai, ngoài bộ dấu hiệu chung, nó có 24 nhóm rút ra từ chính các tài liệu dự án bị trả về sửa lại, nên bắt được những lỗi mà danh sách từ ngữ không bắt được.

## Skill làm gì

Hai việc:

- **Viết và biên tập.** Áp lên bất kỳ đoạn văn xuôi nào gửi cho người đọc: email, FDD/FRD, Quick Guide, biên bản họp, nội dung slide, tài liệu bàn giao, commit message.
- **Soi văn bản.** Chấm một văn bản theo thang yếu, trung bình, mạnh, kèm bằng chứng trích dẫn và ghi rõ giới hạn của việc phán đoán.

## 37 nhóm dấu hiệu

Chia làm hai phần.

**Nhóm 1 đến 13** lấy từ [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) do WikiProject AI Cleanup duy trì: thổi phồng ý nghĩa, phân tích rỗng ở đuôi câu, giọng quảng cáo, song song phủ định, né động từ "là" và "có", bộ ba, và các nhóm khác.

**Nhóm 14 đến 37** rút từ tài liệu dự án thật, không có trong bài gốc vì bài đó viết cho văn bách khoa:

| Nhóm | Lỗi |
|---|---|
| 14 | Chôn kết luận xuống dưới |
| 15 | Trả lời dài khi câu hỏi hẹp |
| 16 | Dịch tên định danh trong code thành chữ của mình |
| 17 | Ẩn dụ văn chương làm tiêu đề mục |
| 18 | Hệ quả trừu tượng thay vì hiện tượng quan sát được |
| 19 | Tài liệu hướng dẫn viết theo lối giải thích |
| 20 | Tự chế thuật ngữ nghiệp vụ |
| 21 | Viết sai tầm người đọc |
| 22 | Giọng bắt bẻ đối tác |
| 23 | Rào đón tự hạ giá trị nội dung mình vừa viết |
| 24 | Rút gọn tới mức mất nghĩa |
| 25 | Định nghĩa trừu tượng thay vì ví dụ số cụ thể |
| 26 | Email viết như tài liệu |
| 27 | Không đồng bộ với phần còn lại của tài liệu |
| 28 | Đề xuất vượt xa phạm vi được hỏi |
| 29 | Đưa giải pháp khi chỉ được yêu cầu mô tả hiện trạng |
| 30 | GAP List và FDD mức BA trượt sang giọng dev |
| 31 | Mô tả logic lấy dữ liệu vòng vo |
| 32 | Bảng phân rã công việc, ước lượng và tiến độ |
| 33 | Ghi chú giải thích cách đọc bảng |
| 34 | Đoạn kết tóm tắt lại bài |
| 35 | Trình bày file Excel bàn giao |
| 36 | Hướng dẫn xử lý sự cố cho người dùng viết như báo cáo phân tích |
| 37 | Ghi chú viết cho người lập file, không cho người nhận |

Ví dụ nhóm 16. Viết `Round(số tiền, 1 đồng)` thay vì `Currency."Amount Rounding Precision"` làm người đọc tưởng con số 1 được ghi cứng trong code, và tưởng dòng đầu tiên không áp tham số đó. Tên thật tra ngược được, chữ tự đặt thì không.

Ví dụ nhóm 21. Cùng một sự việc, viết cho dev là "Cod65637 Split QC Order dùng trực tiếp bảng MOB License Plate Content", viết cho PM là "gói QC đang gắn trực tiếp vào cấu trúc dữ liệu pallet của Tasklet". Sai tầm người đọc thì tài liệu đúng nội dung vẫn không dùng được.

## Nguyên tắc nền

Bài Wikipedia gốc mở đầu bằng một cảnh báo mà hầu hết bản tóm tắt bỏ qua: các dấu hiệu liệt kê ra là triệu chứng, không phải căn bệnh. Sửa triệu chứng mà giữ nguyên bệnh chỉ làm văn khó bị phát hiện hơn chứ không tốt hơn.

Căn bệnh là mô hình ngôn ngữ kéo mọi chủ đề về mức trung bình, thay chi tiết riêng và cụ thể bằng phát biểu chung chung đúng với mọi trường hợp. Nên câu hỏi rà quan trọng nhất không phải "có từ cấm không" mà là:

> Câu này thêm dữ kiện, con số, tên riêng, điều kiện, hệ quả cụ thể nào mà câu trước chưa có? Nếu không, xóa.

Và câu kiểm tra cuối cho cả đoạn: dán nguyên đoạn này sang tài liệu của một dự án khác, khách hàng khác, sản phẩm khác mà vẫn đúng không? Nếu vẫn đúng, viết lại.

## Cấu trúc

```
natural-writing/
├── SKILL.md                        774 dòng, 37 nhóm dấu hiệu và quy trình rà 8 bước
└── references/
    ├── cum-tu-can-tranh.md         11 nhóm từ và cụm từ, tiếng Việt và tiếng Anh, kèm từ thay thế
    ├── dau-vet-ky-thuat.md         9 nhóm vết định dạng và mã đánh dấu của từng chatbot
    └── vi-du-truoc-sau.md          14 ví dụ sửa trước và sau trong ngữ cảnh tài liệu ERP
team-skill/
├── router-SKILL.md                 SKILL.md của bản upload, mỗi lần gọi tải natural-writing/ từ repo
├── build.py                        đóng gói router và bản chụp natural-writing/ thành zip
└── natural-writing.zip             file upload cho Claude.ai, Cowork, Claude Desktop
.claude-plugin/
├── plugin.json                     khai báo plugin cho Claude Code
└── marketplace.json                để chạy /plugin marketplace add
```

SKILL.md luôn được nạp khi skill kích hoạt. Ba file trong `references/` chỉ đọc khi cần, theo hướng dẫn ghi ở cuối SKILL.md.

## Cài đặt

Claude Code, cài dạng plugin:

```
/plugin marketplace add dinhtiendungerp/erp-doc-voice
/plugin install erp-doc-voice@erp-doc-voice
```

Cài qua plugin thì skill mang tên `erp-doc-voice:natural-writing`. Muốn tự nhận bản mới mỗi khi repo có commit thì bật auto-update: gõ `/plugin`, vào tab Marketplaces, chọn `erp-doc-voice`, bật Enable auto-update. Không bật thì cập nhật tay trong terminal:

```
claude plugin marketplace update erp-doc-voice
claude plugin update erp-doc-voice@erp-doc-voice
```

Skills CLI, cài cho mọi dự án:

```
npx skills add dinhtiendungerp/erp-doc-voice --global
```

Claude.ai, Cowork, Claude Desktop: tải [team-skill/natural-writing.zip](team-skill/natural-writing.zip) rồi upload trong phần Skills của Settings. Bản này không chứa quy tắc viết. Mỗi lần được gọi, nó tải `natural-writing/` mới nhất từ repo, nên repo cập nhật thì không phải upload lại. Muốn tải được thì môi trường phải ra được `raw.githubusercontent.com`, qua chạy code có mạng hoặc công cụ tải web. Không ra được thì skill dùng bản chụp đóng sẵn trong zip và báo ngày chụp.

Cài tay: copy thư mục `natural-writing/` vào thư mục skill của agent đang dùng, thường là `~/.claude/skills/`.

Tên thư mục và trường `name` trong SKILL.md phải giữ nguyên là `natural-writing`. Tên repo đặt khác được, nhưng tên skill là thứ agent dùng để nhận diện.

## Dùng

Skill tự kích hoạt khi sinh ra văn xuôi cho người đọc. Gọi thẳng cũng được:

```
/natural-writing

[dán đoạn văn vào đây]
```

Hoặc nói bằng lời thường: "viết lại cho tự nhiên", "nghe AI quá", "đừng dùng mấy từ AI", "rà văn phong giúp tôi", "soi xem đoạn này có dấu hiệu AI không".

## Giới hạn

Skill có một mục riêng về chuyện này, tóm tắt lại ở đây vì nó quan trọng.

Không dấu hiệu đơn lẻ nào là bằng chứng. Người viết thật cũng dùng gạch ngang dài, cũng liệt kê ba ý. Sức mạnh nằm ở mật độ và tổ hợp. Nghiên cứu mà bài Wikipedia dẫn cho thấy người bình thường phân biệt văn AI với văn người không hơn gì đoán mò, người dùng LLM nhiều đạt khoảng 90%, tức là cứ 10 lần khẳng định thì sai 1. Phần mềm phát hiện AI có tỉ lệ lỗi không nhỏ.

Nếu né sạch mọi thứ trong danh sách thì câu văn sẽ cụt lủn và đều tăm tắp, mà kiểu gượng đó cũng là một dấu vết.

## Cập nhật nội dung

Sửa trong `natural-writing/`, đóng gói lại bản chụp trong zip, rồi commit và push cả hai:

```
python team-skill/build.py
```

Người dùng bản zip nhận nội dung mới ở lần gọi skill kế tiếp, chậm nhất khoảng 5 phút vì GitHub lưu đệm file raw. Người dùng plugin nhận khi auto-update chạy hoặc khi chạy lệnh update ở trên.

`plugin.json` cố ý không có trường `version`. Có trường này thì Claude Code giữ mọi người ở bản đã cài cho tới khi đổi số, push bao nhiêu commit cũng vậy. Không có thì phiên bản tính theo commit.

## Nguồn và giấy phép

Nhóm 1 đến 13 dựa trên [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), do [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) duy trì, phát hành theo CC BY-SA 4.0.

Nhóm 14 đến 37, các ví dụ và toàn bộ phần tiếng Việt là nội dung mới, phát hành theo MIT. Xem file LICENSE.
