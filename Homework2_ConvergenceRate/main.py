import math
def counter_a(n):
    l1 = []
    for i in range(1, n+1):
        current_elem = 0.0
        for j in range(i+1):
            current_elem += (4*(-1)**j)/(2*j+1)
        l1.append(abs(current_elem - math.pi))
    return l1
def counter_b(n):
    l1 = []
    for i in range(1, n+1):
        current_elem = 0.0
        for j in range(i+1):
            current_elem += (16*((-1)**j)*0.2**(2*j+1))/(2*j+1) - (4*((-1)**j)*0.0041841**(2*j+1))/(2*j+1)
        l1.append(abs(current_elem - math.pi))
    return l1
def counter_c(n):
    l1 = []
    for i in range(1, n+1):
        current_elem = 0.0
        for j in range(1, i+1):
            current_elem += math.sqrt(6*(1/(j**2)))
        l1.append(abs(current_elem - math.pi))
    return l1
def count_of_zeros(numbers):
    l1 = []
    for elem in numbers:
        cnt = 0
        str_number = str(elem)[2:]
        for i in str_number:
            if i == '0':
                cnt += 1
            else:
                break
        l1.append(cnt)
    return(l1)
n = 100
print(count_of_zeros(counter_a(n)))
print(count_of_zeros(counter_b(n)))
print(count_of_zeros(counter_b(n)))
