from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect 4")
root.geometry("1200x800")
root.minsize(1200, 800)
root.maxsize(1200, 800)
w = 1200
h = 715
c = Canvas(root, width=1200, height=800)
c.pack()
c.create_rectangle(0,85,1200,800,fill="#0373fc")

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)

def reset():
    global color_lists
    print('reset')
    color_lists = [["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white"]]
    global check_turn 
    check_turn = "red"
    global b1,b2,b3,b4,b5,b6,b7
    b1 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b1))
    b2 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b2))
    b3 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b3))
    b4 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b4))
    b5 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b5))
    b6 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b6))
    b7 = Button(root, text = " ", font = ("Helvetica", 20), height = 2, width = 10, bg = "orange", command = lambda: b_click(b7))

    b1.place(x=1,y=0)
    b2.place(x=171.42,y=0)
    b3.place(x=171.42*2,y=0)
    b4.place(x=171.42*3,y=0)
    b5.place(x=171.42*4,y=0)
    b6.place(x=171.42*5,y=0)
    b7.place(x=171.42*6,y=0)

    draw_circles()


def draw_circles():
    for r in range (1,8):
        for co in range (1,7):
            c.create_oval(w/7 * (r-1) + 15, (h/6 * (co-1))+85, w/7 * r - 15, (h/6 * co)+85, fill = color_lists[r-1][co-1])


def b_click(b):
    global check_turn
    global color_lists
    if b == b1:
        count = len(color_lists[0])-1
        for i in reversed(color_lists[0]):
            if i == "white":
                color_lists[0][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red"
                if "white" not in color_lists[0]:
                    b1.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()
    
    elif b == b2:
        count = len(color_lists[1])-1
        for i in reversed(color_lists[1]):
            if i == "white":
                color_lists[1][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red" 
                if "white" not in color_lists[1]:
                    b2.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()

    elif b == b3:
        count = len(color_lists[2])-1
        for i in reversed(color_lists[2]):
            if i == "white":
                color_lists[2][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red"
                if "white" not in color_lists[2]:
                    b3.config(state=DISABLED)
                break 
            count-=1
        draw_circles()
        check_win()

    elif b == b4:
        count = len(color_lists[3])-1
        for i in reversed(color_lists[3]):
            if i == "white":
                color_lists[3][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red" 
                if "white" not in color_lists[3]:
                    b4.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()

    elif b == b5:
        count = len(color_lists[4])-1
        for i in reversed(color_lists[4]):
            if i == "white":
                color_lists[4][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red" 
                if "white" not in color_lists[4]:
                    b5.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()

    elif b == b6:
        count = len(color_lists[5])-1
        for i in reversed(color_lists[5]):
            if i == "white":
                color_lists[5][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red" 
                if "white" not in color_lists[5]:
                    b6.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()

    elif b == b7:
        count = len(color_lists[6])-1
        for i in reversed(color_lists[6]):
            if i == "white":
                color_lists[6][count] = check_turn
                if check_turn == "red":
                    check_turn = "yellow"
                else:
                    check_turn = "red" 
                if "white" not in color_lists[6]:
                    b7.config(state=DISABLED)
                break
            count-=1
        draw_circles()
        check_win()

def check_win():
    global winner
    winner = False
    countRow = 0
    countCol = 0
    for c in range(0,7):
        for r in color_lists[countRow]:
            currElement = r
            if countCol+3 < 7:
                if currElement == "red" and color_lists[countRow][countCol+1] == "red" and color_lists[countRow][countCol+2] == "red" and color_lists[countRow][countCol+3] == "red":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Red Wins!!")
                    disable_all_buttons()
                elif currElement == "yellow" and color_lists[countRow][countCol+1] == "yellow" and color_lists[countRow][countCol+2] == "yellow" and color_lists[countRow][countCol+3] == "yellow":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Yellow Wins!!")
                    disable_all_buttons()
            if countRow+3 < 6:
                if currElement == "red" and color_lists[countRow+1][countCol] == "red" and color_lists[countRow+2][countCol] == "red" and color_lists[countRow+3][countCol] == "red":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Red Wins!!")
                    disable_all_buttons()
                elif currElement == "yellow" and color_lists[countRow+1][countCol] == "yellow" and color_lists[countRow+2][countCol] == "yellow" and color_lists[countRow+3][countCol] == "yellow":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Yellow Wins!!")
                    disable_all_buttons()
            if countRow+3<6 and countCol+3<7:
                if currElement == "red" and color_lists[countRow+1][countCol+1] == "red" and color_lists[countRow+2][countCol+2] == "red" and color_lists[countRow+3][countCol+3] == "red":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Red Wins!!")
                    disable_all_buttons()
                elif currElement == "yellow" and color_lists[countRow+1][countCol+1] == "yellow" and color_lists[countRow+2][countCol+2] == "yellow" and color_lists[countRow+3][countCol+3] == "yellow":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Yellow Wins!!")
                    disable_all_buttons()
            if countRow+3<6 and countCol-3<7:
                if currElement == "red" and color_lists[countRow+1][countCol-1] == "red" and color_lists[countRow+2][countCol-2] == "red" and color_lists[countRow+3][countCol-3] == "red":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Red Wins!!")
                    disable_all_buttons()
                elif currElement == "yellow" and color_lists[countRow+1][countCol-1] == "yellow" and color_lists[countRow+2][countCol-2] == "yellow" and color_lists[countRow+3][countCol-3] == "yellow":
                    winner = True
                    messagebox.showerror("Connect 4", "CONGRATULATIONS! Yellow Wins!!")
                    disable_all_buttons()   
            countCol+=1 
        
        countRow+=1
        countCol = 0
            
#create menu
my_menu = Menu(root)
root.config(menu = my_menu)

#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label = "Reset Game", command = reset)\

reset()
root.mainloop()
