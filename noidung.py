<!-- DÁN ĐOẠN NÀY vào templates/index.html: ngay SAU thẻ </section> của phần video, và TRƯỚC thẻ </main> -->

<!-- ============ SỐ LIỆU TÓM TẮT (tính từ abc-12.csv) ============ -->
<div style="display: flex; gap: 20px; margin-bottom: 24px; justify-content: center; flex-wrap: wrap;">
    <div style="background: rgba(18, 20, 29, 0.8); border-left: 4px solid #ef4444; padding: 15px 25px; border-radius: 8px; flex: 1; min-width: 200px;">
        <span style="color: #9ca3af; font-size: 13px;">Giá đóng cửa cả năm</span>
        <h3 style="color: #ef4444; margin: 5px 0 0 0; font-size: 22px;">11.000 → 4.560 (−58,5%)</h3>
    </div>
    <div style="background: rgba(18, 20, 29, 0.8); border-left: 4px solid #a855f7; padding: 15px 25px; border-radius: 8px; flex: 1; min-width: 200px;">
        <span style="color: #9ca3af; font-size: 13px;">Tháng dao động mạnh nhất</span>
        <h3 style="color: #a855f7; margin: 5px 0 0 0; font-size: 22px;">Tháng 12 (biên độ 5.586)</h3>
    </div>
    <div style="background: rgba(18, 20, 29, 0.8); border-left: 4px solid #3b82f6; padding: 15px 25px; border-radius: 8px; flex: 1; min-width: 200px;">
        <span style="color: #9ca3af; font-size: 13px;">Giá thấp nhất cả năm</span>
        <h3 style="color: #3b82f6; margin: 5px 0 0 0; font-size: 22px;">1.783 (ngày thứ 252)</h3>
    </div>
</div>

<!-- ============ PHÂN TÍCH THEO THÁNG ============ -->
<section style="background: #1e2130; padding: 20px; border-radius: 10px; margin-bottom: 24px;">
    <h2 style="color: #4da6ff; border-bottom: 2px solid #4da6ff; padding-bottom: 8px; margin-top: 0;">Thống kê giá theo tháng</h2>

    <div style="text-align: center;">
        <img src="/static/images/monthly_analysis.png" alt="Biểu đồ cột giá trung bình và boxplot giá theo tháng"
             style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #333; margin: 15px 0;">
    </div>

    <div style="color: #cccccc; font-size: 14px; line-height: 1.7; background: #12141d; padding: 14px 16px; border-radius: 6px; text-align: left;">
        <h3 style="color: #fff; font-size: 1rem; margin: 0 0 6px 0;">Biểu đồ cột: giá trung bình mỗi tháng</h3>
        <p style="margin: 0 0 12px 0;">Tháng 1 có giá trung bình cao nhất năm (8.824,42 VND). Giá giảm liên tục qua các tháng 2, 3, 4 và xuống 3.158,58 VND vào tháng 5. Từ tháng 6 đến tháng 8 giá đi ngang quanh 3.700–3.950 VND, sau đó chạm đáy ở tháng 9 (2.950,78 VND). Từ tháng 10 giá hồi phục lên 5.048,17 VND (tháng 11) và 5.217,04 VND (tháng 12).</p>

        <h3 style="color: #fff; font-size: 1rem; margin: 0 0 6px 0;">Boxplot: phân bố giá và mức dao động</h3>
        <p style="margin: 0 0 8px 0;">Mỗi hộp chứa 50% mức giá ở giữa (từ Q1 đến Q3), vạch ngang trong hộp là trung vị, hai râu kéo tới các giá còn trong vùng thông thường, các chấm tròn là điểm ngoại lai. Biểu đồ dùng toàn bộ 7 mức giá của mỗi ngày.</p>
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Tháng 12 dao động mạnh nhất:</strong> hộp và râu dài nhất, biên độ 5.586,08 VND (từ 2.725,74 đến 8.311,82), độ lệch chuẩn cao nhất (1.313,51). Giá có một đợt tăng nóng cuối tháng rồi quay đầu giảm.</li>
            <li><strong>Tháng 1 đứng thứ hai</strong> với biên độ 5.155,74 VND và độ lệch chuẩn 1.067,08, vì giá giảm mạnh ngay trong tháng. Tháng 1 có các điểm ngoại lai phía trên, cao nhất 12.086,85 VND, cũng là giá cao nhất cả năm.</li>
            <li><strong>Dao động nhỏ nhất:</strong> tháng 5 và tháng 6 (độ lệch chuẩn khoảng 491–498), hộp nhỏ và hẹp. Tháng 5, 6, 7 có các điểm ngoại lai phía trên, tức vài phiên giá bật cao hơn mức thông thường.</li>
        </ul>
    </div>
</section>

<!-- ============ PHÂN BỐ GIÁ 2 QUÝ ĐẦU VS 2 QUÝ CUỐI ============ -->
<section style="background: #1e2130; padding: 20px; border-radius: 10px; margin-bottom: 24px;">
    <h2 style="color: #4da6ff; border-bottom: 2px solid #4da6ff; padding-bottom: 8px; margin-top: 0;">Phân bố giá: hai quý đầu và hai quý cuối năm</h2>

    <div style="text-align: center;">
        <img src="/static/images/histogram_quarters.png" alt="Histogram phân bố giá nửa đầu năm và nửa cuối năm"
             style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #333; margin: 15px 0;">
    </div>

    <div style="color: #cccccc; font-size: 14px; line-height: 1.7; background: #12141d; padding: 14px 16px; border-radius: 6px; text-align: left;">
        <p style="margin: 0 0 8px 0;">Hai histogram được vẽ chồng lên nhau: màu xanh là hai quý đầu (Q1–Q2), màu cam là hai quý cuối (Q3–Q4), phần nâu là vùng hai nhóm trùng nhau. Mỗi nhóm tự chia 30 khoảng nên độ rộng cột hơi khác nhau.</p>
        <ul style="margin: 0; padding-left: 20px;">
            <li><strong>Hai quý đầu:</strong> phân bố lệch phải với đuôi dài đến khoảng 12.000 VND. Giá trung bình 5.252, trung vị 4.615, độ lệch chuẩn 2.153. Vùng giá 7.000–12.000 VND chỉ xuất hiện ở nhóm này, chủ yếu do các tháng đầu năm giá còn cao.</li>
            <li><strong>Hai quý cuối:</strong> giá tập trung dày ở vùng 3.000–5.000 VND. Giá trung bình 4.129, trung vị 3.978, độ lệch chuẩn 1.131, tức ít phân tán hơn nhiều. Giá cao nhất chỉ 8.312 VND, nhưng nhóm này có vùng giá thấp 1.800–2.400 VND mà hai quý đầu không có (chủ yếu ở tháng 9).</li>
            <li><strong>Kết luận:</strong> giá nửa cuối năm thấp hơn và ổn định hơn nửa đầu năm. Nửa đầu năm giá xuất phát cao rồi sụt mạnh nên trải rộng hơn.</li>
        </ul>
    </div>
</section>