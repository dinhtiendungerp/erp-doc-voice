# WBS, kế hoạch và file Excel bàn giao

Đọc khi lập WBS, estimate, kế hoạch nguồn lực, file data migration, slide hay bất kỳ file nào giao khách. Gồm nhóm 32, 33, 35, 37.

## 32. Bảng phân rã công việc, ước lượng và tiến độ

WBS, kế hoạch nguồn lực và bảng estimate có người đọc kỹ từng dòng, vì nó ra tiền và ra cam kết. Bảy lỗi hay bị trả bài:

**Gán việc cho sai bên.** Viết "Chuẩn bị hồ sơ và chủ trì họp chốt phạm vi ba bên" trong khi bên mình chỉ chuẩn bị tài liệu phân tích, còn chủ trì là khách hàng. Trước khi viết một dòng WBS: bên mình làm gì trong dòng này, và bên nào đứng ra tổ chức?

**Tự tách phạm vi chưa ai chốt thành hạng mục riêng.** Người dùng ghi chú thêm một ý trong lúc trao đổi không có nghĩa là phạm vi đã mở rộng. Gộp vào hạng mục đang có.

**Tính ngày công cho mốc.** "Ký biên bản chốt phạm vi" không tiêu ngày công, nó là mốc. Gộp vào hạng mục sinh ra biên bản đó.

**Đưa vào việc không bắt buộc.** Hỏi từng dòng: bỏ dòng này thì có gì hỏng không? Gỡ Tasklet là bắt buộc vì nó chặn đường. Dọn phần tích hợp cũ không còn dùng thì không gỡ cũng chẳng sao.

**Tên cột vai trò tự chế, và hiểu sai cấp của vai trò.** Mỗi công ty có bộ vai trò riêng trong kế hoạch. Hỏi trước nếu chưa biết họ chia thế nào, và hỏi rõ từng tên là một vai trò riêng hay là tác vụ của cùng một vai trò. Phân tích, Thiết kế, Kiểm thử, Deliver, Hỗ trợ vận hành là năm tác vụ của Functional trong một công việc, không phải năm người khác nhau; bảng tổng hợp phải cộng chúng thành một dòng Functional, và các cột đó phải nằm liền nhau dưới một dải tiêu đề chung.

**Rải ngày công theo tác vụ, không dồn mỗi dòng vào một cột.** Một công việc thường đi qua nhiều tác vụ của cùng một người. "Viết đặc tả tích hợp cho 40 interface" là Phân tích 0,5 cộng Thiết kế 2 cộng Kiểm thử 1 cộng Deliver 0,5, không phải 4 ngày đổ hết vào cột Thiết kế. Dùng số lẻ 0,25 và 0,5 khi cần. Các dòng do bên khác làm thì bên mình vẫn có phần nghiệm thu, đừng để trống rồi gồn thành một dòng kiểm thử đứng riêng.

**Tên công việc không nói rõ ai làm và làm gì.** "Kiểm tra kết nối và giám sát đường truyền" đọc xong không biết là việc của hạ tầng hay của lập trình. Viết thành "Tác vụ nền gọi thử WMS theo chu kỳ, báo cho IT khi gọi không được" thì rõ ngay là một hạng mục lập trình.

**Quên phần dev ở giai đoạn sau go-live.** Trực go-live và hỗ trợ tăng cường vẫn cần dev, vì có lỗi thì phải sửa ngay. Đừng đánh dấu không cần lập trình ở những dòng đó.

**Kế hoạch nguồn lực cho một người cụ thể, nhất là người PM đang coaching.** Rút từ kế hoạch T10-T12/2026 của Thảo (08/10/2026), bị sửa ba lượt liền. Chỗ sai không nằm ở chữ mà ở việc dựng kế hoạch trước khi biết người đó là ai và còn rảnh bao nhiêu:

- **Hỏi trình độ trước khi dựng lộ trình học.** Thảo là junior nhưng đã làm ở công ty hơn một năm, quen sản phẩm, đang bắt đầu chuyên sâu. Bản đầu có bài "Làm quen Business Central" và bài nền tảng như cho người mới vào. PM: "không phải mới vô đâu, đưa lộ trình phù hợp hơn". Nói "junior" chưa đủ để chọn mức: hỏi đã làm bao lâu, đã quen phần nào của sản phẩm, rồi mới chọn chủ đề.
- **Thời gian tự học tính bằng giờ, tối đa 1 giờ mỗi ngày làm việc, không quy đổi sang ngày công.** Bản đầu xếp 62 giờ và cộng vào tổng bằng "8 giờ tính 1 ngày". PM: "1 ngày chừng 1 tiếng là quá rồi", rồi "tính theo giờ hay ngày". Cột giờ học đứng riêng, tô cảnh báo khi số giờ của tuần vượt số ngày làm việc của tuần đó.
- **Tải mỗi tuần vừa sức, còn chỗ cho dự án khác.** Người đang được coaching vẫn có việc ở dự án khác. Giữ tổng ngày công của tuần nặng nhất quanh 60% số ngày làm việc (bản đầu có tuần 84%). Muốn vậy thì rải việc dài ra nhiều ngày hơn, dời việc nhẹ sang tuần thưa, bỏ việc làm thêm khỏi tuần dày, chứ không nén việc chính. Người được coaching viết bản nháp, người hướng dẫn rà, nên cột người hướng dẫn ghi "hỗ trợ", "rà", không ghi như hai người chia nhau làm.
- **Đúng phạm vi được giao.** PM và Thảo chỉ làm Procurement & Replenishment, nên bỏ buổi demo Merchandising và mọi chữ "Supply Chain" chung. Onsite chỉ ghi những ngày thuộc phần mình (2,5 ngày đào tạo, 2,5 ngày UAT), không ghi cả tuần.
- **Việc sau khung thời gian vẫn ghi.** Hỗ trợ go-live dự kiến một tuần (01/03 tới 05/03/2027) nằm ngoài T10-T12. Cho vào nhóm riêng, ghi trên mốc và hình, nhưng không cộng vào tổng của khung. Tổng của dòng phải là tổng các cột tuần, không phải tổng cả cột ngày công.
- **Không để danh sách điểm cần chốt trong file mà người khác sẽ xem.** Bản đầu có khối "Điểm cần chốt" hỏi Thảo dành mấy ngày, đi onsite cả tuần hay không. PM: "bỏ qua đi, làm như tài liệu gửi khách hàng". Câu hỏi đó hỏi PM trong chat. Trong file chỉ còn kế hoạch, và lời hỏi của người lập file đi theo nhóm 26 và 37.
- **Không để cột chờ người khác điền.** Bản sau còn cột "Dự án khác (ngày)" để Thảo tự ghi số ngày bận ở dự án khác, kèm công thức trừ đi. PM: "bạn để cột này chi vậy, làm gì có thời gian mà điền". Kế hoạch giao đi phải tự đủ: bỏ cột, bỏ công thức phụ thuộc vào nó, và để cột "Còn trống" chỉ lấy số ngày làm việc trừ số ngày của dự án này. Ô nhập tay chỉ giữ ở cột người nhận chắc chắn cập nhật hằng tuần, như cột Trạng thái.
- **Ngày bắt đầu là ngày làm việc kế tiếp, không phải ngày đang lập file.** Bản đầu bắt đầu 07/10 khi file lập xong vào cuối ngày cuối tuần. PM: "bắt đầu công việc của Thảo từ ngày 12 nhé". Khi người dùng nói hôm nay đã cuối ngày hoặc cuối tuần, đặt ngày bắt đầu là thứ Hai tuần sau, bỏ các việc và các tuần đã trôi qua, cho cột tuần đầu là một tuần đủ năm ngày. Việc cần làm trước buổi họp đầu tiên (đọc tài liệu) dồn vào ngày ngay trước buổi đó.
- **Ghi vai trò của người đó ở từng việc: chính hay phụ.** Bản đầu cho mọi việc nhãn "Chính" và viết như Thảo làm hết, kể cả buổi demo mà PM và chị Lan trình bày onsite và nháp tài liệu PM viết. PM sửa từng dòng: "việc này là phụ thôi", "tương tự" cho Fit/Gap, workshop xác nhận, hướng dẫn khách C điền master data, cấu hình và nhập master data. Việc phụ là việc người hướng dẫn làm chính, người được coaching ghi chú, hỗ trợ phần được giao. Cột "Mức tham gia" có ba giá trị Chính, Phụ, Làm thêm; Phụ giảm ngày công và cột người hướng dẫn ghi người đó làm phần chính. Mức ưu tiên của việc và vai trò của người trong việc là hai thứ khác nhau, đừng dùng một nhãn cho cả hai.
- **Việc đã rõ thì ghi đúng sản phẩm người đó giao, theo chữ người dùng.** Buổi demo: "note những điểm cần lưu ý", không phải "ghi biên bản" cho một buổi mà người khác trình bày. Bản máy tự thêm biên bản và câu trả lời theo mã khảo sát cho mọi buổi họp.
- **Thời gian đọc tài liệu cho người quen sản phẩm tính theo giờ.** PM: "đọc tài liệu và xem lại màn hình demo, 2 tiếng thôi". Bản đầu ghi một ngày. Đọc, xem lại, chuẩn bị câu hỏi cho người đã làm cùng sản phẩm hơn một năm là khoảng 2 giờ, tức 0,25 ngày công. Hỏi lại số giờ thật nếu không chắc, vì việc nhỏ ghi một ngày là cách làm tổng phình ra.
- **Tên dòng không dùng "Dự", "Tham gia"** (đã có ở phần tên dòng của nhóm này). Bản này vẫn lọt "Dự buổi demo", "Dự các workshop" dù skill đã cấm. Rà tên dòng bằng checklist trước khi giao, không chỉ rà văn.
- **Hỗ trợ go-live theo WBS thì tách onsite và online.** Hỏi "một tuần go-live" mà WBS chia 3 ngày onsite và 2 ngày hỗ trợ từ xa thì ghi hai dòng, 3 ngày onsite và 2 ngày online, không gộp thành 5 ngày onsite. PM xác nhận đúng theo WBS.

Bốn điều về con số:

- **Ước lượng phải phản ánh cách làm hiện tại.** Bảng estimate lập theo năng suất của mười năm trước sẽ bị bắt ngay bằng câu "sao thời gian làm còn nhiều vậy".
- **Việc hành chính thì đừng đẩy lên ngày.** Lập kế hoạch cutover và danh sách kiểm tra là 0,25 ngày, không phải một ngày rưỡi.
- **Số ngày kéo dài của một nhánh phải tương xứng với số ngày công.** Một nhánh 5 ngày công mà kéo 25 ngày lịch thì người đọc hỏi ngay. Có lý do thật (chờ đầu ra của bên khác, người làm không toàn thời gian) thì viết lý do đó vào cột ghi chú.
- **Không đòi ai ước lượng khi chưa có căn cứ.** Để trống cột ngày công của dev khi chưa có thiết kế là đúng, nhưng phải nói rõ khi nào điền được: đưa hẳn một hạng mục "Đội phát triển ước lượng trên thiết kế và đặc tả đã ký" vào giai đoạn thiết kế, phụ thuộc các hạng mục thiết kế.
- **Dự phòng phải có, nhưng viết cho ra dáng quản lý rủi ro** chứ không phải cho ra dáng đoán mò. Nêu mức theo độ rõ của từng phần phạm vi, nêu căn cứ, nêu điều kiện sử dụng và ngưỡng phải báo cáo.

**Về lịch của bên khác: không sửa.** Trong kế hoạch chung, ngày và số ngày của đối tác giữ nguyên như họ gửi, ghi "Theo kế hoạch <tên bên đó>" ở cột ghi chú. Cần rút ngắn thì rút ở nhánh của mình. Mốc go-live cũng vậy: **lấy đúng ngày đối tác và khách hàng đã nêu**, xếp nhánh của mình cho vừa, rồi nói điều kiện để giữ được mốc đó và điểm nào còn phải chốt. Tự đẩy go-live lùi một hai tháng rồi đưa ra như một đề xuất là việc cần tránh. Trước khi đề xuất bất kỳ ngày go-live nào, mở kế hoạch của họ ra xem họ đã ghi ngày nào.

Ba điều về cách đặt tên dòng công việc, rút từ lần PM sửa tay bản WBS khách A tháng 09/2026:

- **Tên dòng là tên của việc, không phải cách mình tham gia việc đó.** "Dự buổi bóc tách yêu cầu tích hợp do WMS chủ trì" bị đổi thành "Phân tích yêu cầu tích hợp". Động từ chỉ cách dự phần (dự, tham gia, phối hợp cùng, hỗ trợ bên...) làm dòng đó đọc như lịch họp chứ không như một hạng mục công việc.
- **Không nhét vào tên dòng thông tin đã có ở cột khác.** Bên chủ trì đã nằm ở cột Ghi chú, hình thức làm đã nằm ở cột Nơi làm, ngày đã nằm ở sheet tiến độ. Lặp lại trong tên dòng chỉ làm cột Công việc dài thêm và lệch nhịp với các dòng còn lại.
- **Các dòng trong cùng một giai đoạn phải cùng một dạng ngữ pháp.** Giai đoạn Phân tích mà ba dòng là cụm danh từ, dòng thứ tư là một câu kể có chủ ngữ, thì dòng thứ tư lộ ra ngay.

Quy tắc này không mâu thuẫn với lỗi "tên công việc không nói rõ ai làm và làm gì" ở trên. Chỗ đó nói về dòng mà bản chất công việc còn mơ hồ, phải viết rõ để biết nó thuộc hạ tầng hay lập trình. Chỗ này nói về dòng đã rõ bản chất, chỉ bị đeo thêm chủ thể và cách thức.

Ba điều về cách chia dòng, rút từ sheet danh mục công việc phát triển của WBS khách A tháng 09/2026:

- **Các khối cùng cấp phải chia dòng theo cùng một cách.** Khối nhập kho gộp ba chứng từ nguồn vào một dòng và có dòng kết quả cất hàng, trong khi khối xuất kho tách ba dòng và không có dòng kết quả soạn hàng, thì người đọc bắt được ngay. Nhập và xuất, lệnh và kết quả, sản xuất và các khối kho là những cặp phải soi cạnh nhau: cùng cách tách theo chứng từ nguồn, cùng có hoặc cùng không có bước kho tương ứng. Sheet chi tiết và bảng danh mục ở sheet khác phải dùng cùng một bộ mã. Sửa kiểu này thì cứ áp cho các khối còn lại, không cần hỏi lại từng khối.
- **Đối xứng về cách chia dòng, không đối xứng về thời điểm kích hoạt.** Đơn mua, đơn bán, lệnh chuyển kho đẩy sang WMS khi chuyển sang Released, gồm cả bấm Release tay lẫn duyệt qua workflow. Production Order thì không vận hành bằng nút Release; người dùng bấm nút gửi sang WMS. Chép một trigger cho mọi loại chứng từ là sai. Thời điểm kích hoạt lấy từ quy trình thật của từng chứng từ.
- **Một nút đẩy nhiều lệnh thì ngày công của các lệnh đi sau nhỏ hơn lệnh đầu.** Ba lệnh từ một Production Order đi chung một lần đẩy nên chia 1, 0,5, 0,5 chứ không 1, 1, 1.

Bốn điều nữa về con số, rút từ phản hồi của sếp trên cùng bản WBS:

- **Bảng tổng hợp tách theo bên sẽ thương lượng phần đó, không chỉ theo vai trò.** Ngày công làm cùng đối tác (phân tích yêu cầu, ký đặc tả, kiểm thử tích hợp) đứng thành nhóm riêng có cộng riêng, kèm mã hạng mục và ngày theo lịch đối tác, để người bán hàng tự đem đi thương lượng. Dòng WBS gộp cả phần tự làm lẫn phần làm cùng đối tác thì tách ra hai dòng trước khi tổng hợp.
- **Hỗ trợ sau go-live để khối lượng nhỏ, phần sau đi ticket.** Theo cách NaviWorld đang chào: 3 MD, ghi một câu là phát sinh sau đó tiếp nhận qua ticket.
- **So phương án thì tách phần việc chung và phần riêng của từng phương án.** Giữ Tasklet để tra cứu không làm giảm phần xây bảng pallet mới, vì tích hợp vẫn đi qua bảng mới. Chỉ phần riêng mới được đem ra so. Gộp cả hai vào thì con số tiết kiệm bị thổi phồng và bị bắt ngay.
- **Con số tăng giữa hai bản thì giải thích bằng số trong file đã gửi, trong chat hoặc tin nhắn cho sếp.** Mở bản cũ ra lấy đúng số (bản v1.0 ghi Dev 42, trong khi sếp nhắc 45,5), chỉ từng dòng tăng và lý do. Lời giải thích không đi vào file.

Bốn điều về ngân sách và con số phái sinh, rút từ lần chốt tổng của cùng bản WBS:

- **Con số tổng người duyệt đưa ra là ràng buộc, không phải kết quả tính ra.** "130 tổng là quá nhiều", rồi "80 tới 100 là hợp lý", rồi "sếp bắt loanh quanh 80 tới 85". Nghe xong thì cắt cho vừa khoảng đó rồi mới nói đã cắt ở đâu, đừng giải thích vì sao con số cũ hợp lý.
- **Cắt bằng cách hạ đều nhiều dòng nhỏ, không bằng cách bỏ một dòng lớn.** Hạ 0,25 tới 0,5 ở mười lăm dòng thì bảng vẫn đủ hạng mục. Bỏ hẳn một giai đoạn thì lần sau phát sinh không có chỗ ghi. Các dòng người duyệt đã chốt bằng lời (SIT ba ngày tại chỗ, UAT một ngày, hỗ trợ sau go-live sáu ngày) thì giữ nguyên, và nói rõ chỗ nào còn cắt được nếu cần thêm.
- **Ngày công do đội phát triển ước lượng thì ghi đúng như họ đưa.** Không sửa đè, không thêm cột đề xuất của mình bên cạnh. Muốn đổi thì hỏi họ, hoặc đợi người chủ bảng cho phép gộp dòng. Phần được phép điều chỉnh là phần của chính mình. Cùng nguyên tắc với lịch của đối tác ở trên.
- **Mọi con số suy ra từ số khác phải là công thức, không phải số gõ tay.** Cột Tổng, cột lấy từ sheet khác, dòng quản lý dự án tính 15% tổng Functional và Dev, số đếm interface tính bằng COUNTIF. Gõ tay thì sau ba lần sửa sẽ lệch, mà lệch ở bảng ra tiền thì không ai tha.

**Gộp dòng thì đánh số lại, và không để lại dấu vết của việc gộp.** Ba interface gộp thành một dòng phát triển thì mã phải liền mạch lại từ đầu, không giữ mã cũ rồi ghi chú "Gồm interface I01, I04, I05". Ghi chú đó là lời kể quá trình làm, không phải thông tin người nhận cần. Cần liệt kê đủ từng cái thì để ở bảng danh mục riêng, đánh số con (I01.1, I01.2).

**Số đếm được thì để bảng tự đếm.** "35 interface" viết thành chữ trong câu dẫn, rồi bảng sửa còn 33, thì câu đó thành sai mà không ai thấy. Đặt một dòng tổng dùng COUNTIF dưới bảng, và bỏ con số ra khỏi câu văn ở mọi chỗ khác.

Cuối cùng: **tài liệu bàn giao không chứa ghi chú dạng log.** Không có mục "So với bản trước", không giải thích vì sao con số đổi, không kể lại quá trình trao đổi. Người nhận chỉ cần bản hiện tại đúng.

## 33. Ghi chú giải thích cách đọc bảng

Đặt dưới tiêu đề sheet hoặc dưới bảng một đoạn kể lại bảng có bao nhiêu dòng, cột nào tính bằng công thức, ô màu nào nghĩa là gì, cột nào để ai điền. Người đọc nhìn bảng là thấy hết những thứ đó.

- Sai: "63 công việc trong 12 giai đoạn. Ngày công tách theo bảy vai trò, cột Tổng tính bằng công thức. Cột Dev để trống cho đội phát triển điền, ô tô xám là việc không cần lập trình."
- Đúng: không có đoạn nào cả. Tiêu đề sheet, hàng tiêu đề cột và màu ô đã nói đủ.

Chỉ giữ lại câu mô tả khi nó mang thông tin không đọc được từ bảng: một quy ước không hiển nhiên, một điều kiện áp cho cả sheet, một việc người đọc phải làm. Thước đo: bỏ câu này đi thì người đọc có hiểu sai cái gì không? Không thì bỏ.

Cùng loại trong văn xuôi: "Bảng dưới đây liệt kê...", "Như đã thể hiện ở bảng trên...", "Hình sau minh họa...". Đặt bảng vào đúng chỗ rồi để nó tự nói.

Một biến thể riêng của file nhiều sheet: **dòng "Cấu trúc file" kể sheet nào chứa gì.** Tên sheet nằm ngay trên thanh tab, người đọc bấm một cái là biết. Dòng này bị PM xóa khỏi trang tổng quan của bản WBS khách A.

## 35. Trình bày file Excel bàn giao

Nhóm này rút ra từ việc đặt bản máy sinh cạnh bản PM chỉnh tay. Nội dung gần như giữ nguyên, cái bị sửa là trình bày. Sáu điểm:

**Khối tiêu đề bốn dòng áp cho mọi sheet, kể cả trang tổng quan.** Dòng 1 tên sheet, dòng 2 dòng nhận dạng dự án, dòng 3 ngày cập nhật, dòng 4 là một đường kẻ màu cát cao 1,5 tới 4 điểm chạy suốt chiều ngang bảng. Sheet nào thiếu đường kẻ đó là thấy ngay, vì các sheet đứng cạnh nhau trong cùng một file.

**Ô trong bảng thông tin chỉ cao một dòng chữ.** Ở trang tổng quan, mọi dòng đều 17,5 điểm và không ô nào quấn dòng. Ô phải quấn hai dòng nghĩa là câu trong ô quá dài, cắt câu chứ không tăng chiều cao dòng. Đây là chỗ giao với nhóm 3: cái bị cắt luôn là mệnh đề giải thích bám đuôi.

| Máy viết | Người sửa |
|---|---|
| Tích hợp Microsoft Dynamics 365 Business Central với WMS, thay thế Tasklet Mobile WMS | Tích hợp Microsoft Dynamics 365 Business Central với WMS |
| Phần việc phía Business Central do NaviWorld thực hiện, và tiến độ đề xuất ghép với kế hoạch WMS | Phần việc phía Business Central do NaviWorld thực hiện |
| Quản lý dự án, tính 15% tổng Functional và Dev | Quản lý dự án |

Dòng cuối cho thấy cùng một nguyên tắc với nhóm 33: cách tính đã nằm trong công thức của ô bên cạnh, viết lại thành chữ là thừa.

**Độ rộng cột đặt theo nội dung thật, không đặt cho rộng rãi.** Cột nội dung của trang tổng quan bị hạ từ 76 xuống 52,6 ký tự. Cột rộng gấp đôi câu dài nhất làm bảng loãng ra và đẩy các cột số ra xa mắt.

**Chiều cao dòng bám sát nội dung.** Hàm ước lượng chiều cao trong script hay tính dư một dòng, và dòng dư đó nhân lên sáu chục dòng thì bảng dài thêm cả trang. Bốn dòng trong bản WBS bị hạ từ 40,5 xuống 26 và từ 66,75 xuống 52.

**Gộp cột và gộp dòng bằng Outline Group, và gộp hết chứ đừng gộp một nửa.** Bản máy sinh gộp bốn cột Functional nhưng bỏ sót hai cột Dev và Quản trị; PM kéo nhóm phủ cả sáu cột ngày công, để thu lại còn đúng cột Tổng. Dòng chi tiết gộp dưới dòng giai đoạn, giai đoạn có nhóm con thì thêm một cấp nữa. Nút gộp đặt phía trên và bên trái, tức summaryBelow và summaryRight đều tắt.

**Cùng một quy ước thì áp cho cả file.** Đường kẻ dòng 4, cách tô màu ô, cách đặt nhóm cột, kiểu chữ tiêu đề: đặt một lần trong hàm dựng chung, đừng viết riêng cho từng sheet. Phần lớn lỗi trình bày bị bắt là do một sheet được dựng bằng nhánh code riêng nên thiếu mất một chi tiết mà các sheet khác đều có.

Tên giai đoạn và tiêu đề mục viết một thứ tiếng. "G1. Phân tích (Analysis phase)" bị cắt còn "G1. Phân tích": bản tiếng Anh trong ngoặc là dấu vết của việc đối chiếu với khung mẫu, không phải thông tin cho người đọc.

**File Excel bàn giao theo brandkit Aqua Blue và Warm Sand.** Font Aptos, tiêu đề Aptos Display, hàng tiêu đề bảng `4BACC6` chữ trắng, dòng phân mục `DAEEF3`, đường nhấn `C89B72`, dòng xen kẽ `F6F8F8`, ô cần điền `FCF4EA`, chữ `27343A`, tắt gridline. Quy ước gốc và code mẫu ở dự án khách A (`docs/context/brandkit.md`, `docs/src/build3.py`). File dựng theo bảng màu riêng của script bị trả với câu "sao không định dạng theo brandkit excel".

**File data migration master data.** Rút từ file khách C, 02/10/2026, hai lượt phản hồi liền nhau:

- Không thêm cột cờ ghi cùng một chữ cho mọi dòng, như cột "Ghi chú" ghi "Mẫu", "Đề xuất". PM: "thừa quá". Dữ liệu điền sẵn thì nói một lần ở sheet hướng dẫn rằng người nhận rà, sửa, bổ sung nó. Không kể dữ liệu được dựng từ đâu, kể cả ở dòng mục đích (nhóm 37).
- Hệ thống đã có dữ liệu thì điền đủ, không chỉ vài dòng mẫu. PM: "master data bạn đưa vô hệ thống nhiều lắm mà, đưa hết vô".
- Không để sheet trống. Hệ thống chưa có dữ liệu thì đề xuất theo vai trò hoặc theo nhóm có sẵn, ví dụ mỗi nhóm thu mua một nhân viên thu mua. Số nhạy cảm như số tài khoản ngân hàng thì ghi giá trị lộ rõ là demo (`DEMO-NCC0012`), không bịa số trông như thật.
- Sheet ít cột vẫn phải đọc được: độ rộng cột tính theo nội dung, tiêu đề không bị cắt ngang, câu mục đích gộp sang các cột trống bên phải cho đủ rộng. PM gọi bản chưa làm việc này là "trình bày như bản nháp".
- Không lặp dòng nhận dạng ở từng sheet. PM bỏ dòng "<Tên khách>, data migration master data, bản 1.1 ngày 02/10/2026. Bảng 204 Unit of Measure trên Business Central." ở mọi sheet: tên tab đã nói bảng nào (nhóm 33), phiên bản nằm ở tên file, ngày cập nhật ghi một lần ở sheet danh mục ("Cập nhật: 02/10/2026"). Khối tiêu đề bốn dòng ở đầu nhóm này rút từ bản WBS bốn sheet, không áp nguyên cho file nhiều sheet cùng dạng. Bộ slide cũng vậy: dòng chân trang ghi tên dự án và tên giải pháp ở mọi slide bị bỏ với câu "thừa quá" (01/10/2026). Thông tin đã có cột riêng ở sheet danh mục cũng không chép lại lên đầu từng sheet: dòng "Người điền: OPS-01, KT-02 · Yêu cầu dữ liệu: DL-26 · Dòng 4 tới 8: ..." bị rút còn "Dòng 4 tới 8: bắt buộc, kiểu dữ liệu, hướng dẫn, tên trường trên hệ thống, kết quả kiểm tra" (02/10/2026). Dòng đầu sheet chỉ giữ phần giúp đọc chính sheet đó.
- Tên sheet là số bảng và tên bảng trên hệ thống (nhóm 16), mã đề xuất theo cách kế toán Việt Nam gọi (nhóm 20).
- Nhãn cột gọi theo việc trường làm và nói rõ đơn vị tính (nhóm 24). Nhãn trạng thái gọi theo việc người điền làm, và file không kể chuyện bản demo hay bước nội bộ của NWV (nhóm 37).

Kiểm tra trước khi giao: mở file lên, nhìn bốn dòng đầu của từng sheet xem có giống nhau không; bấm nút gộp của từng nhóm cột xem thu lại còn đúng những cột cần đọc không; tìm ô nào cao bất thường so với các ô cùng bảng.

## 37. Ghi chú viết cho người lập file, không cho người nhận

Nhóm 33 bắt đoạn giải thích cách đọc bảng. Nhóm này bắt ghi chú trong từng ô: cột Ghi chú, cột Phụ thuộc, dòng tổng cộng, bảng giả định. Người lập file hay để lại ở đó những câu chỉ có ích cho chính mình lúc tính toán. Bị bắt trên bản WBS khách A tháng 09/2026, với phản hồi "sao lại đưa mấy thông tin kiểu này vô file gửi khách", rồi "sao vẫn còn mấy kiểu ghi chú này".

Thước đo cho mỗi ghi chú: người nhận đọc câu này thì biết thêm việc gì phải làm, điểm gì phải chốt, ngày nào phải có mặt, hay ràng buộc nghiệp vụ nào? Không trả lời được thì bỏ. Năm kiểu không qua được:

| Kiểu | Ví dụ đã bị bắt | Vì sao sai |
|---|---|---|
| Sổ sách tính ngày công | "Chỉ tính ngày công Dev.", "Nằm trong 20 ngày công làm việc với WMS", "Tính 15% tổng ngày công Functional và Dev, công thức tự tính", "Chỉ gồm các hạng mục có phát sinh lập trình" ở dòng tổng | Nói con số được cộng ở đâu, tính thế nào. Công thức trong ô đã làm việc đó |
| Tham chiếu tài liệu khác, phiên bản, mã phương án | "Theo PA1 trong tài liệu phương án xử lý Tasklet v1.1", "Áp dụng cho mọi phương án xử lý Tasklet" | Người nhận phải mở file khác mới hiểu, và tên phiên bản sai ngay khi file kia đổi bản |
| Chi phí giả định | "Khách A chọn PA2 thì cộng thêm 5,5 ngày công" | Là nội dung thương lượng, không phải phạm vi đang báo. Đưa vào file ước lượng là tự mở cửa cho mặc cả |
| Con số không có chi tiết đi kèm | "rà 21 quy tắc kiểm soát", "chốt 59 điểm cần quyết định", "20 màn hình chuẩn" | Trong file không có danh sách, đọc xong không biết là những gì. Số đếm lấy từ file khác còn dễ lệch (59 ở đây, 57 ở file tích hợp) |
| Mã nội bộ không giải nghĩa | "Q-A1.", "(Q-I3)", phụ thuộc "Q-B1, Q-L1" | Mã của một bảng khác, người nhận không tra được. Có nội dung thì giữ nội dung, bỏ mã. Phụ thuộc thì ghi thẳng thứ phụ thuộc: "danh sách kho và danh sách mặt hàng lô ảo từ khách A" |

Nhiều ghi chú không cần xóa mà cần viết lại cho đúng phần người nhận quan tâm:

- "15 ngày theo hạng mục G.1, nằm trong 20 ngày công làm việc với WMS" viết thành "Có mặt cùng WMS trong 15 ngày theo hạng mục G.1, 23/11 tới 11/12/2026". Giữ ngày, bỏ phép cộng.
- "Ngày công Dev ước lượng sau khi khách A đánh dấu danh sách, khoảng 3 tới 5 ngày nếu giữ gần hết" viết thành "Chờ khách A chọn các màn hình và báo cáo pallet giữ lại sau go-live". Giữ việc khách A phải làm, bỏ con số giả định.
- "Phương án lùi là bật lại Tasklet trong 48 giờ. Khách A chọn PA2 thì cộng thêm 5,5 ngày công" viết thành "Phương án lùi là bật lại luồng quét Tasklet trong 48 giờ đầu sau cutover".

Không nhầm với các ghi chú nghiệp vụ có chữ "chỉ": "Chỉ nhận trạng thái, không nhận chi tiết kết quả kiểm tra" nói phạm vi của interface, giữ lại.

Sửa kiểu này thì rà cả file bằng năm kiểu trên, không chỉ sửa đúng câu bị chỉ ra, vì câu tương tự thường nằm ở sheet khác.

**Cùng nhóm: file và slide giao khách kể chuyện mình dựng nó ra sao.** Bị bắt ở bộ slide POC ngày 01/10/2026 ("đưa mấy tt này vô slide làm gì", "sao đưa thông tin này vô chi", "sao lại đưa dạng code vô") và ở file data migration master data ngày 02/10/2026 ("không đưa thông tin kiểu vầy vô file data migration"). Người nhận cần dữ liệu và cách hệ thống chạy. Môi trường demo, số liệu dựng ra sao, NWV làm bước nào là chuyện của người làm file, để nói trong chat, trong buổi họp, hoặc ghi vào file bối cảnh dự án.

| Kiểu | Ví dụ đã bị bắt |
|---|---|
| Cách dựng dữ liệu demo | "Demo khai Việt Nam và Hàn Quốc cho NCC nhập khẩu.", "Danh sách lấy từ website <tên khách>", "số dựng cho demo", "Tên NCC trong demo ghi giả định" |
| Môi trường và phiên bản của bản demo | tên và số phiên bản hai app kèm câu "chỉ cài trên sandbox", "ngày làm việc 19/09/2026" (Work Date của bản demo) |
| Bước nội bộ, ai làm gì | "NWV đề xuất ..., <tên khách> thay bằng ...", "NWV đổi sang số ID khi nạp" |
| Tên tài nguyên kỹ thuật | tên job, tên dịch vụ dạng code như `<tên dự án>-quet-uc2`, `<tên dự án>-nhac-post` |
| Việc còn chờ chốt | "UC8 và UC9 chờ <tên khách> chốt phạm vi", "... cần làm rõ trước khi đề xuất cách làm" |
| Quá trình mình kiểm chứng | "Tooltip trên màn hình ghi số nhỏ ưu tiên hơn, nhưng code LS xét số lớn trước" |

Dòng cuối bảng cho thấy cách sửa: file chỉ giữ kết luận người nhận dùng được, "số lớn hơn được xét trước". Việc tooltip ghi ngược với code thì báo trong chat.

**Cùng nhóm: nhãn trên slide chiếu cho khách viết như câu nhắc người trình bày.** Bộ slide khảo sát ngày 25/10/2026 đặt khung câu hỏi với nhãn "HỎI <tên khách> TẠI SLIDE NÀY" và ô "Hỏi <tên khách>: <mã câu>". PM bắt: "như kiểu câu bài mẫu cho speaker vậy, đây là slide để show cho người dùng luôn mà". Bản sửa "NWV MONG <tên khách> XÁC NHẬN" lại bị chê "nghe gì kèo dưới vậy". Nhãn chốt là "CẦN <tên khách> XÁC NHẬN", ô câu hỏi viết "Cần <tên khách> xác nhận: ...". Slide khách xem trong buổi họp và nhận lại sau buổi, nên nhãn nói điều hai bên cần chốt, không nhắc người trình bày phải hỏi gì, và không xin. Câu nhắc người trình bày để trong notes, notes thì không cần sửa.

Nhãn trong file cũng phải là chữ của người nhận. Khách điền file, NWV mới là bên nạp file lên hệ thống bằng configuration package. PM sửa hai nhãn ở sheet danh mục của file data migration, rà theo gốc từ "nạp" thì ra thêm ba chỗ cùng họ:

| Bản giao | Bản sửa | Vì sao |
|---|---|---|
| Chưa nạp (trạng thái), Thứ tự nạp (cột) | Chưa điền, Thứ tự điền | PM sửa. Khách điền file, không nạp gì |
| NWV người nạp, Ngày nạp, Đã nạp (cột và trạng thái việc của NWV) | Người phụ trách NWV, Ngày đưa lên hệ thống, Đã đưa lên hệ thống | Sửa theo khi rà cả họ chữ "nạp". Cột việc của NWV ghi rõ là của NWV và gọi theo kết quả khách thấy trên hệ thống |

Kiểm tra: đọc từng nhãn và từng câu trong file như người nhận. Câu nào nói về bản demo, về cách dựng, về việc của NWV mà người nhận không phải làm gì với nó thì bỏ. Nhãn nào tả việc của người dựng file thì đổi sang việc người nhận làm. Trước khi build bản giao, grep các chữ "nạp", "demo", "dựng", "giả định", "sandbox" trên toàn file nguồn.

**Cùng nhóm: tài liệu bàn giao cho đồng nghiệp kỹ thuật sẽ tiếp quản.** Rút từ tài liệu bàn giao agent NaVisio, 30/10/2026, gửi một đồng nghiệp đang dựng nền tảng agent riêng. PM đánh dấu bốn chỗ cần sửa:

| Chỗ bị sửa | PM nói | Vì sao |
|---|---|---|
| Hình ví dụ là lưu đồ đề nghị thanh toán | "chụp ví dụ liên quan tới SCM đi, cái này của kế toán mà" | Agent và cả bộ thử nghiệm xoay quanh SCM. Ví dụ phải lấy từ đúng mảng nghiệp vụ chính, không lấy cái có sẵn trong tay |
| Mục "So với nhu cầu thật": quét phiên, tỉ lệ đáp ứng, khoảng trống, những gì đã sửa hôm nay | "bỏ luôn phần này đi" | Đó là đánh giá nội bộ và nhật ký của người làm agent. Người tiếp quản cần agent hiện nay là gì |
| Đoạn code mẫu dựng agent, lời khuyên cách so output, tin Foundry ngừng designer | "bỏ 2 phần này" | Người nhận là người giỏi hơn mình ở phần đó. Bảng ánh xạ thành phần là đủ, phần còn lại là dạy lại họ (nhóm 21, 28) |
| Mục "Việc còn mở": nạp credits, deploy image, bật Entra, chạy eval | (cùng câu trên) | Việc của người giao, không phải của người nhận. Nói trong chat với người chịu trách nhiệm |

Kiểm tra trước khi giao tài liệu bàn giao: mỗi mục trả lời được câu "người tiếp quản dùng mục này để làm gì?". Mục nói về quá trình mình làm, việc mình còn nợ, hay cách người nhận nên làm nghề của họ thì bỏ. Hình ví dụ lấy từ mảng nghiệp vụ chính của hệ thống.
