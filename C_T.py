ct=input("(1):華氏~攝氏  (2):攝氏~華氏 :\n")
if ct=="1":
    tem=float(input("請輸入現在溫度: "))
    print("攝氏", (tem-32) * 9/5,"度")
else:
    tem=float(input("請輸入現在溫度: "))
    print("華氏",tem * 9/5 + 32,"度")