
equivalent_principal = 15160  # 等额本金
equality_interest = 11715  # 等额本息
delta = 25.37  # 等额本金，每个月减25.37元

total = 2170000
equivalent_principal_total = total + 1648000
equality_interest_total = total + 2047000


def gap_principal(month):  # 计算贷款month个月后，等额本金月缴费金额数据
    paid_sum = 0
    for i in range(month):
        paid_sum += equivalent_principal - delta * i
        if i == month - 1:
            money_by_month = equivalent_principal - delta * i
            print("%d个月后，等额本金月缴费金额为：%d" % (month, money_by_month))
    print("%d个月后，等额本金累积已缴费金额为：%d" % (month, paid_sum))
    return paid_sum


def equivalent_principal_remain(month):  # 等额本金剩余本金
    remain_money = 0
    for i in range(month + 1):
        remain_money = total - i * 6028
    print("%d个月后，等额本金剩余本金金额为：%d" % (month, remain_money))
    return remain_money


def equality_interest_remain(month):  # 等额本息剩余本金
    remain_money = 0
    capital_base = 2583.35
    interest_base = 9132.08
    gap_base = 10.87

    for i in range(month + 1):
        if i == 0:
            remain_money = total - capital_base
        elif i == 1:
            capital_base += gap_base
            remain_money -= capital_base
        else:
            capital_base += gap_base + 0.05 * (i - 1)
            remain_money -= capital_base
    print("%d个月后，等额本息月缴费金额为：%d" % (month, equality_interest))
    print("%d个月后，等额本息累积已缴费金额为：%d" % (month, equality_interest * month))
    print("%d个月后，等额本息剩余本金金额为：%d" % (month, remain_money))
    return remain_money


print("\n")


def cal_paid(month):
    print("***" * 10 + " " + str(month) + " 期 " + " 开始 " + "***" * 10)
    gap_principal(month)
    equivalent_principal_remain(month)

    equality_interest_remain(month)
    print("***" * 10 + " " + str(month) + " 期 " + " 结束 " + "***" * 10)
    print("\n")


month_10 = 10 * 12  # 贷款10年
month_137 = 137  # 137期，等额本金月供为 11709
month_15 = 15 * 12  # 贷款15年

cal_paid(month_10)
cal_paid(month_137)
cal_paid(month_15)


# 1447000
# 1768000
