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
import argparse
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

def probability_level(z: float) -> float:
    """Tính mức xác suất cho một z-score đã cho.

    Args:
        z (float): The z-score.
    
    Returns:
        float: Mức xác suất tương ứng với z-score đó.

    Examples:
        >>> probability_level(2.5758293035489004)
        0.995
        
        >>> probability_level(0.0)
        0.5

        >>> probability_level(-1.959963984540054)
        0.025
    """
    return norm.cdf(z)

def main():    
    parser = argparse.ArgumentParser(description="Tính toán z-score hoặc mức xác suất.")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-p', '--probability', type=float, help="Tính z-score cho một mức xác suất cho trước.")
    group.add_argument('-z', '--zscore', type=float, help="Tính mức xác suất cho một z-score cho trước.")
    args = parser.parse_args()

    if args.probability is not None:
        if 0 < args.probability < 1:
            z = z_score(args.probability)
            print(f"z-score cho mức xác suất {args.probability:.3f}: {z:.6f}")
        else:
            print("Lỗi: Mức xác suất phải nằm trong khoảng từ 0 đến 1.")
    elif args.zscore is not None:
        p = probability_level(args.zscore)
        print(f"Mức xác suất cho z-score {args.zscore:.6f}: {p:.6f}")
    else:
        probability_levels = [0.5, 0.90, 0.95, 0.99, 0.995]
        for level in probability_levels:
            z = norm.ppf(level)
            print(f"z_score cho mức xác suất {level:.3f}: {z:.6f}")
        
        z_scores = [0.0, 1.2815515655446004, 1.6448536269514722, 1.959963984540054, 2.3263478740408408, 2.5758293035489004]
        for z in z_scores:
            p = probability_level(z)
            print(f"Mức xác suất cho z_score {z:.6f}: {p:.6f}")

if __name__ == '__main__':
    main()