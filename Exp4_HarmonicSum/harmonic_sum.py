import numpy as np
import matplotlib.pyplot as plt

def sum_up(N):
    """从小到大计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从小到大求和
    # 提示: 使用循环从1加到N，每次加上1/n
    s = 0.0
    for n in range(1, N+1):
        s += 1.0 / n
    return s


def sum_down(N):
    """从大到小计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从大到小求和
    # 提示: 使用循环从N减到1，每次加上1/n
    s = 0.0
    for n in range(N, 0, -1):
        s += 1.0 / n
    return s


def calculate_relative_difference(N):
    """计算两种方法的相对差异
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 相对差异值
    """
    # 学生在此实现相对差异计算
    # 提示: 使用公式 |S_up - S_down| / ((S_up + S_down)/2)
    s_up = sum_up(N)
    s_down = sum_down(N)
    diff = abs(s_up - s_down)
    avg = (s_up + s_down) / 2
    return diff / avg if avg != 0 else 0.0



def plot_differences():
    """绘制相对差异随N的变化"""
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用np.logspace生成N值
    # 2. 计算每个N对应的相对差异
    # 3. 使用plt.loglog绘制双对数坐标图
    Ns = np.logspace(1, 4, 50, dtype=int)
    Ns = np.unique(Ns)  # 去除重复的N值
    diffs = [calculate_relative_difference(N) for N in Ns]
    
    plt.loglog(Ns, diffs, 'b-', label='Relative Difference')
    plt.xlabel('N (log scale)')
    plt.ylabel('Relative Difference (log scale)')
    plt.title('Relative Difference Between sum_up and sum_down')
    plt.grid(True)
    plt.legend()
    plt.show()


def print_results():
    """打印典型N值的计算结果"""
    # 学生在此实现结果打印
    # 提示:
    # 1. 选择几个典型N值(如10,100,1000,10000)
    # 2. 计算并格式化输出两种方法的和及相对差异
    N_values = [10, 100, 1000, 10000]
    for N in N_values:
        s_up = sum_up(N)
        s_down = sum_down(N)
        rel_diff = calculate_relative_difference(N)
        print(f"N = {N}:")
        print(f"  sum_up   = {s_up:.10f}")
        print(f"  sum_down = {s_down:.10f}")
        print(f"  Relative Difference = {rel_diff:.4e}\n")


def main():
    """主函数"""
    # 打印计算结果
    print_results()
    
    # 绘制误差图
    plot_differences()

if __name__ == "__main__":
    main()
