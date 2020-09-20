import math

def prob(n, p):
    return p * ((1 - p) ** (n - 1))

def infoMeasure(n, p):
    return -math.log2(prob(n, p))

def sumProb(N, p):
    result = 0
    for i in range(1, N + 1):
        result = result + prob(i, p)
    return result
    ''' 
        Thay p = 0.3 và 
        N = 5 => result = 0.8319;
        N = 10 => result = 0.9717;
        N = 20 => result = 0.9992;
        N = 100 => result = 0.9999999999999993;

        Ta thấy N càng lớn thì kết quả càng tiến sát tới 1
        Vì vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1.
    '''


def approxEntropy(N, p):
    result = 0
    for i in range(1, N + 1):
        result += prob(i, p) * infoMeasure(i, p)
    return result

    ''' 
        Thay p = 0.5 và 
        N = 5 => result = 1.78125;
        N = 10 => result = 1.98828125;
        N = 20 => result = 1.999979019165039;
        N = 100 => result = 1.9999999999999998;

        Ta thấy N càng lớn thì kết quả càng tiến sát tới 2  = entropy của nguồn geometric với p = 1/2
        Vì vậy hàm approxEntropy tính xấp xỉ entropy của nguồn tin geometric
    '''



