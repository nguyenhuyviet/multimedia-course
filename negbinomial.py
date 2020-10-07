import math

def prob(n, p, r):
    return (math.factorial(n - 1) / (math.factorial(r - 1) * math.factorial(n - r))) * (p ** r) * ((1 - p) ** (n - r))

def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))

def sumProb(N, p, r):
    result = 0
    for i in range(r, N + 1):
        result = result + prob(i, p, r)
    return result
    ''' 
        Thay p = 0.5, r = 3 và 
        N = 5 => result = 0.5;
        N = 10 => result = 0.9453125;
        N = 20 => result = 0.9997987747192383;
        N = 100 => result = 1.0;

        Ta thấy N càng lớn thì kết quả càng tiến sát tới 1
        Vì vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố negbinomial   bằng 1.
    '''


def approxEntropy(N, p, r):
    result = 0
    for i in range(r, N + 1):
        result += prob(i, p, r) * infoMeasure(i, p, r)
    return result

    ''' 
        Ta có entropy của nguồn negbinomial với giá trị p = 0.5, r = 3 xấp xỉ 3.11568

        Thay p = 0.5 , r = 3 và         
        N = 15 => approxEntropy(5, 0.5, 3) = 1.2806
        N = 30 => approxEntropy(10, 0.5, 3) = 2.7566
        N = 50 => approxEntropy(50, 0.5, 3) = 3.11565

        Ta thấy N càng lớn thì kết quả càng tiến sát tới  3.11568  = entropy của nguồn negbinomial với p = 1/2
        Vì vậy hàm approxEntropy tính xấp xỉ entropy của nguồn tin negbinomial
    '''

if __name__ == "__main__":
    print(approxEntropy(5, 0.5,3))
    print(approxEntropy(10,0.5,3))
    print(approxEntropy(20,0.5,3))
    print(approxEntropy(50,0.5,3))