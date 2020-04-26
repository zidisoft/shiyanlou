import csv
import sys
import json

def calculator(income):
    start_point = 5000  # 起征点
    social_insurance_point = 0.08 + 0.02 + 0.005 + 0.06  # 社保比例
    # 需要缴税的那部分工资
    tax_part = income * (1 - social_insurance_point) - start_point  
    if tax_part <= 0:
        tax = 0 
    elif tax_part <= 3000:
        tax = tax_part * 0.03
    elif tax_part <= 12000:
        tax = tax_part * 0.1 - 210 
    elif tax_part <= 25000:
        tax = tax_part * 0.2 - 1410
    elif tax_part <= 35000:
        tax = tax_part * 0.25 - 2660
    elif tax_part <= 55000:
        tax = tax_part * 0.3 - 4410
    elif tax_part <= 80000:
        tax = tax_part * 0.35 - 7160
    else:
        tax = tax_part * 0.45 - 15160
    salary = income * (1 - social_insurance_point) - tax
    return '{:.2f}'.format(salary)

def output(data):
    '''
    将字典存入文件
    '''
    # 将字典转换为 json 格式
    json_str = json.dumps(data)

    # 打开 sys.argv[2] 路径的文件，属性为 'w',写入 json_str
    with open(sys.argv[2],'w') as f:
        f.write(json_str)

def main():
    '''
    main() 函数
    '''
    # 新建字典 result待存入 ID : 税后收入
    result = {}
    # 通过 sys.argv[1] 拿到 csv 文件的路径
    data_file = sys.argv[1]
    # 读取 csv 文件，计算税后收入，并存入字典
    usr_csv = csv.reader(open(data_file))
    data_list = list(usr_csv)

    print(data_list)
    for item in data_list:
        id, income = item[0],float(item[1])
        income = calculator(income)
        result[id] = income

    output(result)

if __name__ == '__main__':
    main()
