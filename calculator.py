from tkinter import *
from tkinter import messagebox, ttk


operators = ["+", "-", "*", "/"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


main = Tk()
main.title("Calculator")
chosen_operator = StringVar()
chosen_numbers = IntVar()
user_num = []
user_num_2 = []


def get_numbers():
    user_number = chosen_numbers.get()
    user_operator = chosen_operator.get()

    if user_operator == "":
        user_num.append(user_number)
        #lt_screen.config(lt_screen.insert(END, user_number))

    else:
        lbl_operator.config(text=user_operator)
        user_num_2.append(user_number)
        #lt_screen_2.config(lt_screen_2.insert(END, user_number))

    main.after(100, lambda: chosen_numbers.set(None))


def back_space():
    user_operator = chosen_operator.get()

    if user_operator == "":
        user_num.pop()
        lt_screen.delete(END)

    else:
        if len(user_num_2) <= 0:
            lbl_operator.config(text="")
            chosen_operator.set("")
        else:
            lt_screen_2.delete(END)
            user_num_2.pop()


def clear_screen():
    lbl_operator.config(text="")
    lt_screen_result.delete(END)
    for x in range(len(user_num)):
        lt_screen.delete(END)
    for x in range(len(user_num_2)):
        lt_screen_2.delete(END)
    user_num.clear()
    user_num_2.clear()


def checker_operator():
    if len(user_num) <= 0:
        messagebox.showwarning(title="Nope!", message="That's an operator pls try again!")
        user_num.clear()
        main.after(100, lambda: chosen_operator.set(""))
        return


def get_number():
    user_operator = chosen_operator.get()
    user_answer = 0

    user_num_str = [str(number) for number in user_num]
    user_num_str_2 = [str(numbers) for numbers in user_num_2]

    user_num_join = ''.join(user_num_str)
    user_num_join_2 = ''.join(user_num_str_2)

    if user_operator == "+":
        lt_screen_result.delete(END)
        lt_screen.config(lt_screen.insert(END, user_num_join))
        lt_screen_2.config(lt_screen_2.insert(END, user_num_join_2))
        user_answer = (int(user_num_join) + int(user_num_join_2))
        lt_screen_result.insert(END, user_answer)

    elif user_operator == "-":
        lt_screen_result.delete(END)
        lt_screen.config(lt_screen.insert(END, user_num_join))
        lt_screen_2.config(lt_screen_2.insert(END, user_num_join_2))
        user_answer = (int(user_num_join) - int(user_num_join_2))
        lt_screen_result.insert(END,user_answer)

    elif user_operator == "*":
        lt_screen_result.delete(END)
        lt_screen.config(lt_screen.insert(END, user_num_join))
        lt_screen_2.config(lt_screen_2.insert(END, user_num_join_2))
        user_answer = (int(user_num_join) * int(user_num_join_2))
        lt_screen_result.insert(END, user_answer)

    elif user_operator == "/":
        lt_screen_result.delete(END)
        lt_screen.config(lt_screen.insert(END, user_num_join))
        lt_screen_2.config(lt_screen_2.insert(END, user_num_join_2))
        user_answer = (int(user_num_join) / int(user_num_join_2))
        lt_screen_result.insert(END, user_answer)

    else:
        messagebox.showerror(title="Error! Operator!", message="There's no such operator pls try again!")
        return

    main.after(100, lambda: chosen_operator.set(""))


lt_screen = Listbox(main, width=10, height=10, font="Impact 20", bg="Beige")
lt_screen.grid(row=0, column=0, sticky=W)
lt_screen.config(height=lt_screen.size())

lbl_operator = Label(main, text="", font="Impact 15", padx=25, pady=10)
lbl_operator.grid(row=0, column=1)

lt_screen_2 = Listbox(main, width=10, height=10, font="Impact 20", bg="Beige")
lt_screen_2.grid(row=0, column=2, sticky=W)
lt_screen_2.config(height=lt_screen_2.size())

lt_screen_result = Listbox(main, width=11, height=10, font="Impact 20", bg="Beige")
lt_screen_result.grid(row=0, column=3)
lt_screen_result.config(height=lt_screen_result.size())

bt_back = Button(main, text="<<", font="Impact 20", width=5, padx=25, bd=10, fg="Black", activeforeground="Black", bg="Grey", activebackground="Grey", command=back_space)
bt_back.grid(row=6, column=100)

bt_clear = Button(main, text="Clear", font="Impact 20", width=5, padx=25, bd=10, fg="Black", activeforeground="Black", bg="Grey", activebackground="Grey", command=clear_screen)
bt_clear.grid(row=6, column=1)

for i in range(len(operators)):
    sign = Radiobutton(main, text=operators[i], variable=chosen_operator,
                       value=operators[i], padx=25, font="Impact 20", width=5, indicatoron=0,
                       bd=10, fg="Black", activeforeground="Black", bg="Lime", activebackground="Lime", command=checker_operator)

    sign.grid(row=(i+1), column=100)

bt_equals = Button(main, text="=", font="Impact 20", width=5, padx=25, bd=10, fg="Black", activeforeground="Black", bg="Grey", activebackground="Grey", command=get_number)
bt_equals.grid(row=6, column=2)

#numbers indicator
colm = 1
raw = 0

for j in range(len(numbers)):
    num = Radiobutton(main, text=numbers[j], variable=chosen_numbers,
                      value=numbers[j], padx=25, font="Impact 20", width=5, indicatoron=0, bd=10,
                      fg="Black", activeforeground="Black", bg="White", activebackground="White", command=get_numbers)

    if raw == 5:
        raw = 1
    else:
        raw += 1

    if j == 5:
        colm += 1

    num.grid(row=raw, column=colm)


main.mainloop()
