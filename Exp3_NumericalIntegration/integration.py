import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    """被积函数 f(x) = sqrt(1-x^2)"""
    return np.sqrt(1 - x**2)

def rectangle_method(f, a, b, N):
    """矩形法（左矩形法）计算积分"""
    h = (b - a) / N
    result = 0
    for i in range(N):
        result += f(a + i * h)
    return result * h

def trapezoid_method(f, a, b, N):
    """梯形法计算积分"""
    h = (b - a) / N
    result = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        result += f(a + i * h)
    return result * h

def calculate_errors(a, b, exact_value):
    """计算不同N值下各方法的误差"""
    N_values = [10, 100, 1000, 10000]
    h_values = []
    rect_errors = []
    trap_errors = []
    
    for N in N_values:
        h = (b - a) / N
        h_values.append(h)
        rect_result = rectangle_method(f, a, b, N)
        trap_result = trapezoid_method(f, a, b, N)
        rect_errors.append(abs(rect_result - exact_value) / abs(exact_value))
        trap_errors.append(abs(trap_result - exact_value) / abs(exact_value))
    
    return N_values, h_values, rect_errors, trap_errors

def plot_errors(h_values, rect_errors, trap_errors):
    """绘制误差-步长关系图"""
    plt.loglog(h_values, rect_errors, label="Rectangle Method Error", marker='o')
    plt.loglog(h_values, trap_errors, label="Trapezoid Method Error", marker='s')
    plt.loglog(h_values, [h**2 for h in h_values], label="Theoretical Convergence (h^2)", linestyle='--')
    plt.xlabel("Step Size h")
    plt.ylabel("Relative Error")
    plt.title("Error vs Step Size")
    plt.legend()
    plt.grid(True, which="both", linestyle="--")
    plt.show()

def print_results(N_values, rect_results, trap_results, exact_value):
    """打印计算结果表格"""
    print(f"{'N':<10}{'矩形法结果':<20}{'梯形法结果':<20}{'精确值':<20}")
    for i in range(len(N_values)):
        print(f"{N_values[i]:<10}{rect_results[i]:<20.10f}{trap_results[i]:<20.10f}{exact_value:<20.10f}")

def time_performance_test(a, b, max_time=1.0):
    """测试在限定时间内各方法能达到的最高精度"""
    N = 10
    while True:
        start_time = time.time()
        rectangle_method(f, a, b, N)
        rect_time = time.time() - start_time
        
        start_time = time.time()
        trapezoid_method(f, a, b, N)
        trap_time = time.time() - start_time
        
        if rect_time > max_time and trap_time > max_time:
            break
        N *= 2
    
    print(f"在 {max_time} 秒内，矩形法和梯形法的最大分割数为: {N // 2}")

def calculate_convergence_rate(h_values, errors):
    """计算收敛阶数"""
    log_h = np.log(h_values)
    log_errors = np.log(errors)
    slope, _ = np.polyfit(log_h, log_errors, 1)
    return slope

def main():
    """主函数"""
    a, b = -1.0, 1.0  # 积分区间
    exact_value = 0.5 * np.pi  # 精确值
    
    print(f"计算积分 ∫_{a}^{b} √(1-x²) dx")
    print(f"精确值: {exact_value:.10f}")
    
    # 计算不同N值下的结果
    N_values = [10, 100, 1000, 10000]
    rect_results = []
    trap_results = []
    
    for N in N_values:
        rect_results.append(rectangle_method(f, a, b, N))
        trap_results.append(trapezoid_method(f, a, b, N))
    
    # 打印结果
    print_results(N_values, rect_results, trap_results, exact_value)
    
    # 计算误差
    _, h_values, rect_errors, trap_errors = calculate_errors(a, b, exact_value)
    
    # 绘制误差图
    plot_errors(h_values, rect_errors, trap_errors)
    
    # 计算收敛阶数
    rect_rate = calculate_convergence_rate(h_values, rect_errors)
    trap_rate = calculate_convergence_rate(h_values, trap_errors)
    
    print("\n收敛阶数分析:")
    print(f"矩形法: {rect_rate:.2f}")
    print(f"梯形法: {trap_rate:.2f}")
    print(rect_errors)
    print(trap_errors)
    
    # 时间性能测试
    time_performance_test(a, b)

if __name__ == "__main__":
    main()
