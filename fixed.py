cnt_exam =  [0] * 9
cnt_no_exam =  [0] * 9
subjects = ['Toán','Văn','Ngoại Ngữ','Lý','Hoá','Sinh','Sử','Địa lý','GDCD']
with open("data_clean.csv" , "r" , encoding="utf8") as file:
    data = file.read().split("\n")

std = data[1:]

counts = [0] * 10
with open("data_clean.csv", "r", encoding="utf8") as file:
    data = file.readline()
    while(data != ""):
        if (data[0] == '0'):
            data = data.split(',')
            cnt = 0
            for i in range(2,len(data)):
                if (data[i] != '-1'):
                    cnt += 1
            counts[cnt] += 1
            score = data[2:]
            for i in range(3):
                if (score[i] != '-1'):
                    cnt_exam[i] +=1
                else:
                    cnt_no_exam[i] +=1
            
            if(data[1] == "khtn"):
                for i in range(3,6):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1
            if(data[1] == "khxh"):
                for i in range(6,9):
                    if (score[i] != '-1'):
                        cnt_exam[i] +=1
                    else:
                        cnt_no_exam[i] += 1
        data = file.readline()

with open("Thisinhdithi.csv", "w", encoding="utf8") as file:
    file.write("Môn,Số lượng thí sinh đi thi\n")

with open("Thisinhkhongdithi.csv", "w", encoding="utf8") as file:
    file.write("Môn,Số lượng thí sinh không đi thi\n")

with open("thisinhthisoluongmon.csv" , "w", encoding="utf8") as file:
    file.write("Nhóm,Số lượng\n")

with open("Thisinhdithi.csv", "a", encoding="utf8") as file:
    for i in range(len(subjects)):
        file.write(subjects[i] + "," + str(cnt_exam[i]) + "\n")

with open("Thisinhkhongdithi.csv", "a", encoding="utf8") as file:
    for i in range(len(subjects)):
        file.write(subjects[i] + "," + str(cnt_no_exam[i]) + "\n")

with open("thisinhthisoluongmon.csv" , "a" , encoding="utf8") as file:
    for i in range(len(counts)):
        file.write(str(i) + "," + str(counts[i]) + "\n")



