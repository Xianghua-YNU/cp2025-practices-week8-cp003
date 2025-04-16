# Import necessary libraries for numerical computation and plotting
import numpy as np
import matplotlib.pyplot as plt

def sum_S1(N):
    """计算第一种形式的级数和：交错级数
    S_N^(1) = sum_{n=1}^{2N} (-1)^n * n/(n+1)
    """
    result = 0.0
    for n in range(1, 2*N + 1):  # Loop from 1 to 2N inclusive
        result += (-1)**n * n / (n + 1)  # Alternating series term
    return result

def sum_S2(N):
    """计算第二种形式的级数和：两项求和相减
    S_N^(2) = -sum_{n=1}^N (2n-1)/(2n) + sum_{n=1}^N (2n)/(2n+1)
    """
    sum1 = sum2 = 0.0  # Initialize both sums
    for n in range(1, N + 1):  # Loop from 1 to N inclusive
        sum1 += (2*n - 1) / (2*n)  # First sum term (odd numerators)
        sum2 += (2*n) / (2*n + 1)   # Second sum term (even numerators)
    return -sum1 + sum2  # Combine the sums with proper signs

def sum_S3(N):
    """计算第三种形式的级数和：直接求和
    S_N^(3) = sum_{n=1}^N 1/(2n(2n+1))
    """
    result = 0.0
    for n in range(1, N + 1):  # Loop from 1 to N inclusive
        result += 1.0 / (2*n * (2*n + 1))  # Simplified series term
    return result

def calculate_relative_errors(N_values):
    """计算相对误差"""
    err1 = []  # To store errors between S1 and S3
    err2 = []  # To store errors between S2 and S3
    
    for N in N_values:  # Calculate errors for each N value
        s1 = sum_S1(N)  # Compute S1
        s2 = sum_S2(N)  # Compute S2
        s3 = sum_S3(N)  # Compute S3 (reference value)
        
        # Calculate relative errors and store them
        err1.append(abs((s1 - s3) / s3))  # Relative error S1 vs S3
        err2.append(abs((s2 - s3) / s3))  # Relative error S2 vs S3
    
    return err1, err2

def plot_errors(N_values, err1, err2):
    """绘制误差分析图"""
    plt.figure(figsize=(10, 6))  # Create figure with specified size
    
    # Plot both error series with different markers and styles
    plt.loglog(N_values, err1, 'o-', label='S1 Error', alpha=0.7)  # S1 error with circle markers
    plt.loglog(N_values, err2, 's--', label='S2 Error', alpha=0.7)  # S2 error with square markers
    
    # Configure plot appearance
    plt.grid(True, which="both", ls="-", alpha=0.2)  # Add grid lines
    plt.xlabel('N')  # X-axis label
    plt.ylabel('Relative Error')  # Y-axis label
    plt.title('Relative Errors vs N')  # Plot title
    plt.legend()  # Show legend
    
    # Save and display the plot
    plt.savefig('series_sum_errors.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_results():
    """打印典型N值的计算结果"""
    N_values = [10, 100, 1000, 10000]  # Selected N values for printing
    
    print("\n计算结果:")
    # Print header row
    print("N\tS1\t\tS2\t\tS3\t\tErr1\t\tErr2")
    print("-" * 80)  # Divider line
    
    for N in N_values:  # Calculate and print results for each N
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs((s1 - s3) / s3)  # Relative error S1 vs S3
        err2 = abs((s2 - s3) / s3)  # Relative error S2 vs S3
        # Print formatted results
        print(f"{N}\t{s1:.8f}\t{s2:.8f}\t{s3:.8f}\t{err1:.2e}\t{err2:.2e}")

def main():
    """主函数"""
    # 生成N值序列 (Generate N values on a logarithmic scale)
    N_values = np.logspace(0, 4, 50, dtype=int)  # 50 points from 10^0 to 10^4
    
    # 计算误差 (Calculate relative errors)
    err1, err2 = calculate_relative_errors(N_values)
    
    # 打印结果 (Print selected results)
    print_results()
    
    # 绘制误差图 (Plot the error analysis)
    plot_errors(N_values, err1, err2)

if __name__ == "__main__":
    main()  # Execute the main function when run as a script
