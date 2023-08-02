import tkinter

Test_Result = ["100% 하남잡니다", 
               "하남자입니다..", 
               "하남자와 보통 사람의 사이입니다.",
               "보통 사람입니다..", 
               "상남자가 되시려면 분발하세요", 
               "상남자에 근접합니다.", 
               "이 정도면 상남자입니다",
               "上남자 그 자체입니다."]

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    percent = int(100 * pts / 7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "체크하신 상남자 지수는 "+ str(percent) + "%입니다\n" + Test_Result[pts])


root = tkinter.Tk()
root.title("상남자 지수 진단 게임")
root.resizable(False,False)
cvs = tkinter.Canvas(root, width=800, height=600)
cvs.pack()
pic = tkinter.PhotoImage(file="highmale.png")
cvs.create_image(400,300, image=pic)
button = tkinter.Button(text="진단하기", font=("궁서체", 32), bg="gray", command=click_btn)
button.place(x=400,y=480)
text = tkinter.Text(width=40, height=5, font=("궁서체", 16))
text.place(x=320, y=30)

bvar = [None] *7
cbtn = [None]*7
ITEM = ["고기반찬 없으면 밥을 안 먹습니다", "저축을 안 합니다", "글을 못 읽습니다", "야채는 절대 안 먹습니다", "집에서 팬티만 입습니다", "현금만 씁니다", "머리카락이 3cm 이하입니다"]

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("궁서체", 12), variable=bvar[i], bg="white")
    cbtn[i].place(x=400, y=160 + 40 * i)
root.mainloop()