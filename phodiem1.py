import pandas as pd
# with open("data_new_fix.csv", "r", encoding="utf8") as file:
subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa lý","GDCD"]

path = "data_clean.csv"
data = pd.read_csv(path)

for i in subject:
    subject_ = i
    print(i)
    tmp1 = list(data[i])
    cnt = 0
    scores = []
    for i in range(len(tmp1)):
        if (tmp1[i] != -1.0 and tmp1[i] != 0.0):
            scores.append(tmp1[i])
    tmp = list(set(scores))
    tmp.sort()
    scores_dict = []
    for i in range(len(tmp)):
        scores_dict.append([tmp[i],0])

    scores_dict = dict(scores_dict)
    for i in range(len(scores)):
        scores_dict[scores[i]] += 1

    with open("phodiemmon" + str(subject_) + ".csv" , "a", encoding="utf8") as file:
        file.write("Điểm,Tần suất\n")
        for key, value in scores_dict.items():
            file.write(str(key) + "," + str(value) + "\n")