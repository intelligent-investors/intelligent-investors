"""
Module này cung cấp một hàm để tính điểm z (z-score) cho một mức xác suất cho trước.

Điểm z là số độ lệch chuẩn mà một điểm dữ liệu nằm xa so với trung bình của một 
phân phối chuẩn hóa (phân phối chuẩn có trung bình là 0 và độ lệch chuẩn là 1).
Nó chỉ ra mức độ và hướng mà một giá trị lệch so với trung bình.

Điểm z cho một mức xác suất p được tính bằng cách sử dụng hàm phân phối tích lũy (CDF) ngược 
của phân phối chuẩn:

z = \Phi^{-1}(p)

trong đó:
- \Phi^{-1} là hàm CDF ngược (còn được gọi là hàm lượng tử).
- p là mức xác suất (một giá trị giữa 0 và 1).

Hàm phân phối tích lũy (CDF) cho một phân phối chuẩn được định nghĩa như sau:

\Phi(Z) = P(Z \leq z)

trong đó:
- \Phi(Z) là xác suất mà biến ngẫu nhiên chuẩn Z nhỏ hơn hoặc bằng z.
- Z là biến ngẫu nhiên với phân phối chuẩn (trung bình là 0 và độ lệch chuẩn là 1).
- z là giá trị quan tâm (theo số độ lệch chuẩn từ trung bình).

Nói cách khác, CDF cho biết xác suất mà một biến ngẫu nhiên phân phối chuẩn nhỏ 
hơn hoặc bằng một giá trị nhất định z.
Hàm CDF ngược, còn gọi là hàm lượng tử, cho biết giá trị z cho một mức xác suất 
cho trước p.
"""

from scipy.stats import norm

def z_score(probability_level: float) -> float:
    """Tính điểm z cho một mức xác suất cho trước.

    Tham số:
        probability_level (float): Mức xác suất (một giá trị giữa 0 và 1).
    
    Trả về:
        float: Điểm z tương ứng với mức xác suất đó.

    Ví dụ:
        >>> z_score(0.995)
        2.5758293035489004
        
        >>> z_score(0.5)
        0.0

        >>> z_score(0.025)
        -1.959963984540054
    """
    return norm.ppf(probability_level)

if __name__ == '__main__':
    probability_levels = [0.5, 0.90, 0.95, 0.99, 0.995]
    for level in probability_levels:
        z = norm.ppf(level)
        print(f"z_score cho mức xác suất {level:.3f}: {z:.6f}")