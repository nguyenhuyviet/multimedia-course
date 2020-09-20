import math

def prob(n, p, N):
    return (math.factorial(N) / (math.factorial(n) * math.factorial(N-n))) * (p ** n) * ((1 - p) ** (N - n))

def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))

def sumProb(N, p):
    result = 0
    for i in range(0, N + 1):
        result = result + prob(i, p, N)
    return result
    ''' 
        Thay p = 0.5 và 
        N = 5 => result = 1.0;
        N = 10 => result = 1.0;
        N = 20 => result = 1.0;
        N = 100 => result = 1.0;

        Ta thấy N càng lớn thì kết quả càng tiến sát tới 1
        Vì vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binomial  bằng 1.
    '''


def approxEntropy(N, p):
    result = 0
    for i in range(0, N + 1):
        result += prob(i, p, N) * infoMeasure(i, p, N)
    return result

    ''' 
        
    '''

if __name__ == "__main__":
    print(approxEntropy(10,0.5))
    print(approxEntropy(100,0.5))
    print(approxEntropy(-100,0.5))
