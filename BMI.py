body=[{"Str":"非常嚴重肥胖", "Thershole":40},{"Str":"嚴重肥胖", "Thershole":35},{"Str":"中等肥胖", "Thershole":30},{"Str":"體重過重", "Thershole":25},{"Str":"標準體重", "Thershole":18.5},{"Str":"體重過輕", "Thershole":16},{"Str":"體重嚴重不足", "Thershole":15},{"Str":"非常嚴重地體重不足", "Thershole":0}]

h=float(input("請輸入您的身高（單位：公分）："))
if (h>=246):
    print("你是世界上最高的人了")
elif (h<=54.6):
    print("你是嬰幼兒或世界上最矮的成年人")

h=(h/100)**2

w=float(input("請輸入您的體重（單位：公斤）："))
if (w>=635):
    print("你是世界上最重的人了")
elif (w<=20):
    print("你是嬰幼兒或世界上最輕的人了")

bmi=w/h
    
for i in body:
    if bmi>i["Thershole"]:
        print("你的BMI值為"+"%5.2f"%bmi+"。狀態為："+i["Str"]+"。")
        break
    else:
        continue  

