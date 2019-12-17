import sys
from collections import defaultdict, deque
from math import atan2, gcd


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "16-input.txt"
    num, offset = setup(input_file)
    num = num * 10000
    # num = '12345678'
    # num = '80871224585914546619083218645595'
    #for i in range(100):
    #    num = fft(num)
    #    print(i+1,num[:8])
    #for line in range(4):
    #    print(f"Line number {line}")
    #    for base_pos in range(4):
    #        print(f"Base position {base_pos}")
    #        print(positions_for_base(base_pos,line,4,10))

    base_len = 4
    length = 8
#    for line  in range(8):
#        print(f"Line number {line}")
#        for base_pos in range(4):
#            print(f"Base position {base_pos}")
#            print(positions_for_base(base_pos,line,base_len,length))

    #num = [1,2,3,4,5,6,7,8]
    for i in range(100):
        num = fft_2(num)
    print(num[offset:offset+8])
        
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

def fft_2(num):
    base_pattern = [0,1,0,-1]
    transform = []
    for line in range(len(num)):
        l = 0
        for i in range(len(base_pattern)):
            b = base_pattern[i]
            if b != 0:
                positions = positions_for_base(i,line,4,len(num))
                if positions:
                    s = sum(num[pos] for pos in positions)
                    l += b*s
        if l > 0:
            l = l%10
        else:
            l = (-l)%10
        transform.append(l)
    return transform

def positions_for_base(base_pos,line,base_len,length):
    first = (line+1) * base_pos -1
    begin_clump = first
    positions = []
    while begin_clump < length +base_len:
        for i in range(line+1):
            if begin_clump + i < length:
                positions.append(begin_clump+i)
        begin_clump += (line+1)*base_len
#    if positions:
#        while positions[-1] >= length:
#            positions = positions[:-1]
#        if positions[0] < 0:
#            return positions[1:]
#    else:
    if base_pos == 0:
        return positions[1:]
    return positions
            
    
    


def setup(filename):
    asteroids = []
    with open(filename) as f:
        num_s =f.read().strip()

    num = [int(i) for i in num_s] 
    offset = int(num_s[:7])
    print(num,offset)


    return num, offset


if __name__ == "__main__":
    main()
