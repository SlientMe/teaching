from tkinter import *
class Calc():
    def __init__(self):
        print("我出来了")
        global tk
        tk = Tk()  # 注意不能用self = Tk(),相当于将子类重新赋值了
        tk.geometry('480x500')
        tk.title('计算器')

        self.sv = StringVar()
        self.sv.set('初始状态')
        show_label = Label(tk, textvariable=self.sv, bg='#eeeeee', width=34, height=4,
                           font=('黑体', 18, 'bold',), justify=LEFT, anchor='e')
        show_label.pack(padx=10, pady=10)

        k_area = Frame(width=600, height=450, bg='#cccccc')
        k_area.pack()

        w = 5
        h = 1
        key_1 = Button(k_area, text='1', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_1.grid(row=1, column=0)

        key_2 = Button(k_area, text='2', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_2.grid(row=1, column=1)

        key_3 = Button(k_area, text='3', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_3.grid(row=1, column=2)

        key_4 = Button(k_area, text='4', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_4.grid(row=2, column=0)

        key_5 = Button(k_area, text='5', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_5.grid(row=2, column=1)

        key_6 = Button(k_area, text='6', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_6.grid(row=2, column=2)

        key_7 = Button(k_area, text='7', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_7.grid(row=3, column=0)

        key_8 = Button(k_area, text='8', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_8.grid(row=3, column=1)

        key_9 = Button(k_area, text='9', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_9.grid(row=3, column=2)

        key_0 = Button(k_area, text='0', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_0.grid(row=4, column=1)

        key_point = Button(k_area, text='.', width=w, height=h,
                           bg='yellow', font=('黑体', 30, 'bold'))
        key_point.grid(row=4, column=2)

        key_pms = Button(k_area, text='±', width=w, height=h,
                         bg='yellow', font=('黑体', 30, 'bold'))
        key_pms.grid(row=3, column=3)

        key_close = Button(k_area, text='Close', width=w, height=h, bg='red',
                           font=('黑体', 30, 'bold'))
        key_close.grid(row=4, column=0)

        key_plus = Button(k_area, text='+', width=w, height=h,
                          bg='yellow', font=('黑体', 30, 'bold'))
        key_plus.grid(row=1, column=3)

        key_minus = Button(k_area, text='-', width=w,
                           bg='yellow', font=('黑体', 30, 'bold'))
        key_minus.grid(row=2, column=3)

        key_multiply = Button(k_area, text='x', width=w, height=h,
                              bg='yellow', font=('黑体', 30, 'bold'))
        key_multiply.grid(row=0, column=2)

        key_divide = Button(k_area, text='÷', width=w, height=h,
                            bg='yellow', font=('黑体', 30, 'bold'))
        key_divide.grid(row=0, column=1)

        key_equal = Button(k_area, text='=', width=w, height=h,
                           bg='yellow', font=('黑体', 30, 'bold'))
        key_equal.grid(row=4, column=3)

        key_c = Button(k_area, text='Clear', width=w, height=h,
                       bg='yellow', font=('黑体', 30, 'bold'))
        key_c.grid(row=0, column=0)

        key_del = Button(k_area, text='←', width=w, height=h,
                         bg='yellow', font=('黑体', 30, 'bold'))
        key_del.grid(row=0, column=3)

        tk.mainloop()

c = Calc()