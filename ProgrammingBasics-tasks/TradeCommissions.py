city = input()
trade_volume = float(input())

commission = 0
is_valid = True

if city == "Sofia":
    if trade_volume < 0:
        print("error")
        is_valid = False
    elif 0 <= trade_volume <= 500:
        commission = trade_volume * 0.05
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.07
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.08
    else:
        commission = trade_volume * 0.12
elif city == "Varna":
    if trade_volume < 0:
        is_valid = False
    elif 0 <= trade_volume <= 500:
        commission = trade_volume * 0.045
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.075
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.10
    else:
        commission = trade_volume * 0.13
elif city == "Plovdiv":
    if trade_volume < 0:
        is_valid = False
    elif 0 <= trade_volume <= 500:
        commission = trade_volume * 0.055
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.08
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.12
    else:
        commission = trade_volume * 0.145
else:
    is_valid = False

if is_valid:
    print(f"{commission:.2f}")
else:
    print("error")