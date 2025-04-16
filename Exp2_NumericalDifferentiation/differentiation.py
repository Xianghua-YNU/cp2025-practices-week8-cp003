import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """定义测试函数 f(x) = x(x-1)
    
    参数:
        x (float): 输入值
        
    返回:
        float: 函数计算结果
    """
    # 学生在此实现函数计算
    return x * (x - 1)

def forward_diff(f, x, delta):
    """前向差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    # 学生在此实现前向差分公式
    # 提示: 使用 (f(x + delta) - f(x)) / delta
    return (f(x + delta) - f(x)) / delta

def central_diff(f, x, delta):
    """中心差分法计算导数
    
    参数:
        f (function): 要求导的函数
        x (float): 求导点
        delta (float): 步长
        
    返回:
        float: 导数的近似值
    """
    # 学生在此实现中心差分公式
    # 提示: 使用 (f(x + delta) - f(x - delta)) / (2 * delta)
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def analytical_derivative(x):
    """解析导数 f'(x) = 2x - 1
    
    参数:
        x (float): 求导点
        
    返回:
        float: 导数的精确值
    """
    # 学生在此实现解析导数公式
    return 2 * x - 1

def calculate_errors(x_point=1.0):
    """计算不同步长下的误差
    
    参数:
        x_point (float): 求导点，默认为1.0
        
    返回:
        tuple: (deltas, forward_errors, central_errors)
            deltas: 步长数组
            forward_errors: 前向差分误差数组
            central_errors: 中心差分误差数组
    """
    # 学生在此实现误差计算
    # 提示:
    # 1. 使用np.logspace生成步长序列
    # 2. 对每个步长计算前向和中心差分
    # 3. 计算相对误差 = |近似值 - 精确值| / |精确值|
    # 步长序列
    deltas = np.logspace(-14, -2, 13)
    
    # 解析解
    true_value = analytical_derivative(x_point)
    
    # 存储结果
    forward_errors = []
    central_errors = []
    
    # 计算不同步长下的误差
    for delta in deltas:
        # 前向差分
        forward_value = forward_diff(f, x_point, delta)
        forward_rel_error = abs((forward_value - true_value) / true_value)
        forward_errors.append(forward_rel_error)
        
        # 中心差分
        central_value = central_diff(f, x_point, delta)
        central_rel_error = abs((central_value - true_value) / true_value)
        central_errors.append(central_rel_error)
    
    return deltas, forward_errors, central_errors

def plot_errors(deltas, forward_errors, central_errors):
    """绘制误差-步长关系图
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用plt.loglog绘制双对数坐标图
    # 2. 添加参考线表示理论收敛阶数
    # 3. 添加图例、标题和坐标轴标签
    plt.figure(figsize=(10, 6))
    
    # 绘制前向差分误差
    plt.loglog(deltas, forward_errors, 'o-', label='Forward Difference')
    
    # 绘制中心差分误差
    plt.loglog(deltas, central_errors, 's-', label='Central Difference')
    
    # 添加参考线
    plt.loglog(deltas, deltas, '--', label='First Order O(h)')
    plt.loglog(deltas, np.array(deltas)**2, '--', label='Second Order O($h^2$)')
    
    # 设置图表
    plt.xlabel('Step Size $\\delta$')  # Fixed escape sequence
    plt.ylabel('Relative Error')
    plt.title('Error vs Step Size in Numerical Differentiation')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    
    # 保存图表
    plt.savefig('error_vs_stepsize.png', dpi=300)
    plt.show()

def print_results(deltas, forward_errors, central_errors):
    """打印计算结果表格
    
    参数:
        deltas (array): 步长数组
        forward_errors (array): 前向差分误差数组
        central_errors (array): 中心差分误差数组
    """
    # 学生在此实现结果打印
    # 提示: 格式化输出步长和对应误差
    print("步长(δ)\t前向差分误差\t中心差分误差")
    print("-" * 50)
    
    for i in range(len(deltas)):
        print(f"{deltas[i]:.2e}\t{forward_errors[i]:.6e}\t{central_errors[i]:.6e}")

def main():
    """主函数"""
    # 学生可以修改测试点
    x_point = 1.0
    
    # 计算误差
    deltas, forward_errors, central_errors = calculate_errors(x_point)
    
    # 打印结果
    print(f"函数 f(x) = x(x-1) 在 x = {x_point} 处的解析导数值: {analytical_derivative(x_point)}")
    print_results(deltas, forward_errors, central_errors)
    
    # 绘制误差图
    plot_errors(deltas, forward_errors, central_errors)
    
    # 以下分析代码可以保留或修改
    forward_best_idx = np.argmin(forward_errors)
    central_best_idx = np.argmin(central_errors)
    
    print("\n最优步长分析:")
    print(f"前向差分最优步长: {deltas[forward_best_idx]:.2e}, 相对误差: {forward_errors[forward_best_idx]:.6e}")
    print(f"中心差分最优步长: {deltas[central_best_idx]:.2e}, 相对误差: {central_errors[central_best_idx]:.6e}")
    
    print("\n收敛阶数分析:")
    mid_idx = len(deltas) // 2
    forward_slope = np.log(forward_errors[mid_idx] / forward_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    central_slope = np.log(central_errors[mid_idx] / central_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    
    print(f"前向差分收敛阶数约为: {forward_slope:.2f}")
    print(f"中心差分收敛阶数约为: {central_slope:.2f}")

if __name__ == "__main__":
    main()
