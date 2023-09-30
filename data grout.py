data = {
    "100-90": 25,
    "42-01": 48,
    "55-09": 12,
    "128-64": 71,
    "002-22": 18,
    "321-54": 19,
    "097-32": 33,
    "065-135": 64,
    "99-043": 80,
    "111-99": 11,
    "123-019": 5,
    "109-890": 72,
    "132-123": 27,
    "32-908": 27,
    "008-09": 25, 
    "055-967": 35,
    "897-99": 44,
    "890-98": 56,
    "344-32": 65,
    "43-955": 59,
    "001-233": 9,
    "089-111": 15,
    "090-090": 17,
    "56-777": 23,
    "44-909": 27,
    "13-111": 21,
    "87-432": 15,
    "87-433": 14,
    "87-434": 23,
    "87-435": 11,
    "87-436": 12,
    "87-437": 16,
    "94-121": 15,
    "94-122": 35,
    "80-089": 10,
    "87-456": 8,
    "87-430": 40
}
age = int(input())
#your code goes her

#your code goes here
price_adult = 20
price_discount = 5
overall_earnings = 0
overall_earnings_new = 0

for i in data.values():
    if i >= 18 and i >= age:
        overall_earnings += price_adult
        overall_earnings_new += price_adult
    elif i < 18 and i < age:
        overall_earnings += price_discount
        overall_earnings_new += price_discount
    else:
        overall_earnings += price_discount
        overall_earnings_new += price_adult

increase = ((overall_earnings_new-overall_earnings)*100)/overall_earnings
print(int(increase))