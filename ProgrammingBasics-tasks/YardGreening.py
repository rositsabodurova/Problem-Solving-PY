area = float(input())

initial_price = area * 7.61
discount = initial_price * 0.18
final_price = initial_price - discount

print("The final price is: " + "%.2f" % final_price + " lv.")
print("The discount is: " + "%.2f" % discount + " lv.")