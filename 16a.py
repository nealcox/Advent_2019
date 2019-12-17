import sys
from collections import defaultdict, deque
from math import atan2, gcd


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "16-input.txt"
    num = setup(input_file)
    #num = '12345678'
    # num = '80871224585914546619083218645595'
    for i in range(100):
        num = fft(num)
        print(i+1,num[:8])
        
def mult(x,y):
    return x*y

def mult_lists(l1,l2):
    return map(mult,l1,l2)

def fft(num):

    num = [int(i) for i in num]
    out = []

    for i in range(len(num)):
        pattern = pattern_val(i,len(num))
        out.append(str(abs(sum(map(mult,num,pattern)))%10))
    return ''.join(out)
    

def pattern_val(pos_output,length):
    base_pattern = [0,1,0,-1]
    base_len = len(base_pattern)
    output = []
    for i in range(length+2):
        for j in range (pos_output+1):
            output.append(base_pattern[i%base_len])
    return output[1:length+1]


    
    


def setup(filename):
    asteroids = []
    with open(filename) as f:
        num =f.read().strip()
    return num


if __name__ == "__main__":
    main()
