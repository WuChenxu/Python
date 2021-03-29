import time

def main():
    num = int(input("请输入整数值:"))
    result = 0
    start_time = time.time()

    for i in range(num+1):
        result += i
    print("从1到%d累加的计算结果为%d"%(num,result))
    end_time = time.time()
    print("总共用时%s"%(end_time-start_time))
    
if __name__ == "__main__":
    main()
