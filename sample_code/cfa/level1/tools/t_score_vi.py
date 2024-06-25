"""
Mô-đun này cung cấp các hàm để tính điểm t cho một mức xác suất cho trước
và bậc tự do, cũng như mức xác suất cho một điểm t cho trước.

Điểm t là một giá trị được suy ra từ phân phối t của Student, được sử dụng 
trong các phân tích thống kê để ước tính tham số của tổng thể khi kích thước mẫu 
nhỏ và độ lệch chuẩn của tổng thể không được biết. Phân phối t 
tương tự như phân phối chuẩn chuẩn nhưng có đuôi dày hơn, có nghĩa là 
nó có xu hướng tạo ra các giá trị rơi xa khỏi trung bình của nó.

Điểm t cho một mức xác suất \( p \) và bậc tự do \( df \) được 
tính bằng cách sử dụng hàm phân phối tích lũy ngược (CDF) của 
phân phối t:

t = T^{-1}(p, df)

trong đó:
- T^{-1} là hàm phân phối tích lũy ngược (còn được gọi là hàm phân vị) của 
  phân phối t.
- p là mức xác suất (một giá trị giữa 0 và 1).
- df là bậc tự do.

Hàm phân phối tích lũy (CDF) cho phân phối t được định nghĩa như sau:

T(t, df) = P(T \leq t)

trong đó:
- T(t, df) là xác suất rằng biến ngẫu nhiên phân phối t với bậc tự do df 
  nhỏ hơn hoặc bằng t.
- T là một biến ngẫu nhiên có phân phối t.
- t là giá trị quan tâm.

Nói cách khác, CDF chỉ ra xác suất rằng một biến ngẫu nhiên phân phối t 
nhỏ hơn hoặc bằng một giá trị t cho trước. Hàm phân phối tích lũy ngược, còn được gọi 
là hàm phân vị, cung cấp giá trị t cho một mức xác suất p 
và bậc tự do df.
"""
import argparse
from scipy.stats import t

def t_score(probability_level: float, degrees_of_freedom: int) -> float:
    """Tính toán điểm t cho một mức xác suất và bậc tự do cho trước.

    Tham số:
        probability_level (float): Mức xác suất (một giá trị giữa 0 và 1).
        degrees_of_freedom (int): Bậc tự do.
    
    Trả về:
        float: Điểm t tương ứng với mức xác suất và bậc tự do đó.

    Ví dụ:
        >>> t_score(0.975, 10)
        2.2281388519649385
        
        >>> t_score(0.5, 20)
        0.0

        >>> t_score(0.025, 15)
        -2.131449545559323
    """
    return t.ppf(probability_level, degrees_of_freedom)


def probability_level_t(t_value: float, degrees_of_freedom: int) -> float:
    """Tính toán mức xác suất cho một điểm t và bậc tự do cho trước.

    Tham số:
        t_value (float): Điểm t.
        degrees_of_freedom (int): Bậc tự do.
    
    Trả về:
        float: Mức xác suất tương ứng với điểm t và bậc tự do đó.

    Ví dụ:
        >>> probability_level_t(2.2281388519649385, 10)
        0.975
        
        >>> probability_level_t(0.0, 20)
        0.5

        >>> probability_level_t(-2.131449545559323, 15)
        0.025
    """
    return t.cdf(t_value, degrees_of_freedom)

def main():
    parser = argparse.ArgumentParser(description="Tính toán điểm t hoặc mức xác suất cho một bậc tự do cho trước.")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-p', '--probability', type=float, help="Tính toán điểm t cho một mức xác suất cho trước.")
    group.add_argument('-t', '--tscore', type=float, help="Tính toán mức xác suất cho một điểm t cho trước.")
    parser.add_argument('-d', '--degrees', type=int, help="Bậc tự do.")
    args = parser.parse_args()

    if args.probability is not None and args.degrees is not None:
        if 0 < args.probability < 1:
            t_val = t_score(args.probability, args.degrees)
            print(f"Điểm t cho mức xác suất {args.probability:.3f} với {args.degrees} bậc tự do: {t_val:.6f}")
        else:
            print("Lỗi: Mức xác suất phải nằm trong khoảng từ 0 đến 1.")
    elif args.tscore is not None and args.degrees is not None:
        p = probability_level_t(args.tscore, args.degrees)
        print(f"Mức xác suất cho điểm t {args.tscore:.6f} với {args.degrees} bậc tự do: {p:.6f}")
    else:
        # Ví dụ mặc định nếu không có đối số nào được cung cấp
        default_degrees = 10  # Bậc tự do ví dụ
        probability_levels = [0.5, 0.90, 0.95, 0.975, 0.99, 0.995]
        print(f"Ví dụ mặc định với {default_degrees} bậc tự do:")
        for level in probability_levels:
            t_val = t.ppf(level, default_degrees)
            print(f"Điểm t cho mức xác suất {level:.3f}: {t_val:.6f}")

        t_scores = [0.0, 1.2815515655446004, 1.6448536269514722, 1.959963984540054, 2.3263478740408408, 2.5758293035489004]
        for t_val in t_scores:
            p = t.cdf(t_val, default_degrees)
            print(f"Mức xác suất cho điểm t {t_val:.6f}: {p:.6f}")

if __name__ == '__main__':
    main()