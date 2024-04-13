from datetime import datetime

print("By yzxz&&ChatGPT3.5")

def calculate_time_difference(time1_str, time2_str):
    try:
        # 将输入的时间字符串转换为 datetime 对象
        time1 = datetime.strptime(time1_str, '%H:%M:%S.%f')
        time2 = datetime.strptime(time2_str, '%H:%M:%S.%f')

        # 计算时间差值
        time_diff = abs(time1 - time2)
        print("----------------------")
        if(time1<time2):
            print("提前")
        else:
            print("延后")
        
        # 打印时间差值
        print(str(time_diff)[:-4])
        print("----------------------")


    except ValueError:
        print('输入的时间格式不正确，请确保格式为 H:MM:SS.FF')

# 主循环，持续进行多轮检测
while True:
    # 输入两个时间字符串
    time1_input = input('请输入本部分与视频相对应的开始时间')
    time2_input = input('请输入字幕原来的时间')

    # 调用函数计算并打印时间差值
    calculate_time_difference(time1_input, time2_input)

    # 是否继续进行下一轮检测
    continue_input = input('是否继续进行下一轮检测 输入y以继续 ')
    if continue_input.lower() != 'y':
        break  # 如果输入不是 'y'，则退出循环
    print("----------------------")