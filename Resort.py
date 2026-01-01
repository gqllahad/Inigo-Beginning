from tkinter import *
from tkinter import messagebox, Menu, ttk


admin_account = {}
user_account = {}

resort_price = {"Adult": 350, "Kids": 250}
hotel_price = {"PerHour": 150, "PerDay": 3600, "DeluxePerHour": 500, "DeluxePerDay": 12000}


def administrator_account():
    admin = Tk()
    admin.title('Create Administrator Account')
    admin.geometry("425x250")

    def add_admin():
        admin_user = txt_admin_user.get()
        admin_pass = txt_admin_pass.get()

        if admin_user == "" or admin_pass == "":
            messagebox.showerror(title="Error!", message="Please fill up the blank!")
            return

        admin_account[admin_user] = admin_pass
        admin.destroy()

    fr_admin = Frame(admin)
    fr_admin.grid(row=1, column=0)

    lbl_admin_title = Label(fr_admin, text="| Admin Create", font="Garamond 20", padx=20, pady=10)
    lbl_admin_title.grid(row=0, column=0)

    lbl_admin_user = Label(fr_admin, text="Enter desired username : ", font="Georgia 10", padx=20, pady=10)
    lbl_admin_user.grid(row=1, column=0)

    txt_admin_user = Entry(fr_admin, width=25)
    txt_admin_user.grid(row=1, column=1)

    lbl_admin_pass = Label(fr_admin, text="Enter desired password : ", font="Georgia 10", padx=20, pady=10)
    lbl_admin_pass.grid(row=2, column=0)

    txt_admin_pass = Entry(fr_admin, width=25)
    txt_admin_pass.grid(row=2, column=1)

    fr_admin = Frame(admin)
    fr_admin.grid(row=3, column=0)

    bt_admin = Button(fr_admin, text="Create", bd=5, relief=RAISED, padx=20, pady=10, command=add_admin)
    bt_admin.grid(row=3, column=0, sticky=W)

    bt_admin_cancel = Button(fr_admin, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10, command=quit)
    bt_admin_cancel.grid(row=3, column=1, sticky=E)

    admin.mainloop()


def sign_up():
    sign = Toplevel()
    sign.title("Sign-up Account")
    sign.geometry("425x250")

    def add_accont():
        user_name = txt_sign_user.get()
        pass_word = txt_sign_pass.get()

        if user_name in admin_account:
            messagebox.showerror(title="Error!", message="That account is already an administrator!")
            return

        if user_name == "" or pass_word == "":
            messagebox.showerror(title="No User/Pass, please make sure you fill up all the blanks!")
            return

        if user_name in user_account:
            messagebox.showerror(title="Error!", message="That account is already an existing account!")
            return

        user_account[user_name] = {'Password': pass_word,
                                   'InfoResort': [{}],
                                   'InfoHotel': [{}],
                                   'TotalResort': 0,
                                   'TotalHotel': 0,
                                   'Total': 0}
        sign.destroy()

    def cancel():
        sign.destroy()

    fr_signup = Frame(sign)
    fr_signup.grid(row=1, column=0)

    lbl_sign_title = Label(fr_signup, text="| Sign-up", font="Garamond 20", padx=20, pady=10)
    lbl_sign_title.grid(row=0, column=0)

    lbl_sign_user = Label(fr_signup, text="Enter desired username : ", font="Georgia 10", padx=20, pady=10)
    lbl_sign_user.grid(row=1, column=0)

    txt_sign_user = Entry(fr_signup, width=25)
    txt_sign_user.grid(row=1, column=1)

    lbl_sign_pass = Label(fr_signup, text="Enter desired password : ", font="Georgia 10", padx=20, pady=10)
    lbl_sign_pass.grid(row=2, column=0)

    txt_sign_pass = Entry(fr_signup, width=25)
    txt_sign_pass.grid(row=2, column=1)

    fr_sign_but = Frame(sign)
    fr_sign_but.grid(row=3, column=0)

    bt_signup = Button(fr_sign_but, text="Sign-up", bd=5, relief=RAISED, padx=20, pady=10, command=add_accont)
    bt_signup.grid(row=3, column=0, sticky=W)

    bt_signup_cancel = Button(fr_sign_but, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10, command=cancel)
    bt_signup_cancel.grid(row=3, column=1, sticky=E)

    sign.mainloop()


def main_postema(**kwargs):
    page = Tk()
    page.title("Main Page")

    username = txt_user.get()

    def resort_postema():
        root = Toplevel()
        root.title("Reservation")

        user_names = txt_user.get()

        def submit():
            first_name = txt_name.get()
            last_name = txt_last.get()
            user_age = str(cb_age.get())
            user_time = cb_time.get()

            sched_day = cb_day.get()
            sched_month = cb_month.get()
            sched_year = cb_year.get()
            user_sched = sched_month + "/" + sched_day + "/" + sched_year

            if first_name == "" or last_name == "":
                messagebox.showerror(title="Error!", message="Please insert a info first!")
                return

            if user_age == "Input age.." or cb_age.current() == -1:
                messagebox.showerror(title="age error!", message="Please make sure you input your age!")
                return

            if sched_day == "" or sched_month == "" or sched_year == "":
                messagebox.showerror(title="No Schedule!", message="Please be sure to set up a date!")
                return

            if user_time not in cb_time_val or user_time == "Select a time.." or user_time == "":
                messagebox.showerror(title="Time Error!", message="Please make sure you select a scheduled time!")
                return
            else:
                kwargs[user_names]['InfoResort'].append({'Firstname': first_name,
                                                   'Lastname': last_name,
                                                   'Age': int(user_age),
                                                   'Time': user_time,
                                                   'Schedule': user_sched})

            print(kwargs[user_names]['InfoResort'][1])

            txt_name.delete(0, END)
            txt_last.delete(0, END)
            cb_time.set("Select a time..")
            cb_age.delete(0, END)
            cb_month.delete(0, END)
            cb_day.delete(0, END)
            cb_year.delete(0, END)
            root.withdraw()

            resort_decide = messagebox.askyesno(title="You want to go again?", message="You want to add another one?")

            if resort_decide:
                root.deiconify()
            else:
                root.destroy()

        fr_list = Frame(root)
        fr_list.grid(row=1, column=1)

        lbl_survey = Label(fr_list, text="Please Fill up the survey : ", font="Georgia 15", padx=20, pady=10)
        lbl_survey.grid(row=1, column=0)

        lbl_name = Label(fr_list, text="Firstname : ", font="Georgia 10", pady=10, padx=20)
        lbl_name.grid(row=2, column=0)

        txt_name = Entry(fr_list, width=20)
        txt_name.grid(row=2, column=1)

        lbl_last = Label(fr_list, text="Lastname : ", font="Georgia 10", pady=10, padx=20)
        lbl_last.grid(row=3, column=0)

        txt_last = Entry(fr_list, width=20)
        txt_last.grid(row=3, column=1)

        lbl_age = Label(fr_list, text="Age : ", font="Georgia 10", pady=10, padx=20)
        lbl_age.grid(row=4, column=0)

        cb_var = IntVar()
        cb_val = [x for x in range(101)]
        cb_age = ttk.Combobox(fr_list, width=5, textvariable=cb_var, values=cb_val)
        cb_age.grid(row=4, column=1)

        lbl_date = Label(fr_list, text="Date of reservation (Month) (Day) (Year) : ", font="Georgia 10", padx=20,
                         pady=10)
        lbl_date.grid(row=5, column=0)

        cb_day_var = StringVar()
        cb_month_var = StringVar()
        cb_year_var = StringVar()

        cb_day_val = [x for x in range(1, 32)]
        cb_month_val = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                        "October", "November", "December"]
        cb_year_val = [x for x in range(2024, 2050)]

        cb_month = ttk.Combobox(fr_list, textvariable=cb_month_var, width=5, values=cb_month_val)
        cb_month.grid(row=5, column=1)

        cb_day = ttk.Combobox(fr_list, textvariable=cb_day_var, width=5, values=cb_day_val)
        cb_day.grid(row=5, column=2)

        cb_year = ttk.Combobox(fr_list, textvariable=cb_year_var, width=5, values=cb_year_val)
        cb_year.grid(row=5, column=3)

        lbl_time = Label(fr_list, text="Daytime or Overnight : ", font="Georgia 10", padx=20, pady=10)
        lbl_time.grid(row=6, column=0)

        cb_time_var = StringVar()
        cb_time_val = ["Select a time..", "Daytime", "Overnight"]
        cb_time = ttk.Combobox(fr_list, textvariable=cb_time_var, width=10, values=cb_time_val)
        cb_time.current(0)
        cb_time.grid(row=6, column=1)

        fr_buttons = Frame(root)
        fr_buttons.grid(row=7, column=1)

        bt_submit = Button(fr_buttons, text="Submit", padx=20, pady=10, bd=5, relief=RAISED, command=submit)
        bt_submit.grid(row=7, column=0, sticky=W)

        bt_cancel = Button(fr_buttons, text="Cancel", padx=20, pady=10, bd=5, relief=RAISED)
        bt_cancel.grid(row=7, column=1, sticky=E)

        root.mainloop()

    def hotel_postema():
        hotel = Toplevel()
        hotel.title("Hotel Reservation")

        user_name = txt_user.get()

        def hotel_submit():
            Fname = txt_fname.get()
            Lname = txt_lname.get()
            room_type = cb_room_type.get()

            duration_hour = int(cb_stay_hour.get())
            duration_day = int(cb_stay.get())

            date_day = cb_day.get()
            date_month = cb_month.get()
            date_year = cb_year.get()
            date_arrival = date_month + "/" + date_day + "/" + date_year

            company_count = int(cb_ppl.get())

            if Fname == "" or Lname == "":
                messagebox.showerror(title="No Firstname/ Lastname", message="Make sure you fill up all the requirements!/ That Name is already exists!")
                return
            if room_type == "" or room_type == "Select a room type..":
                messagebox.showerror(title="No RoomType", message="Make sure you fill up the room type section!")
                return
            if duration_hour == 0 and duration_day == 0:
                messagebox.showerror(title="No Duration", message="Make sure you fill up the duration of stay section!")
                return
            if date_day == "" or date_month == "" or date_year == "":
                messagebox.showerror(title="No Scheduled date!", message="Make sure you fill up the scheduled date section!")
                return
            if company_count == 0:
                messagebox.showerror(title="No Head count!", message="Make sure you fill up the Head count section!")
                return

            if room_type == "Regular" and company_count > 7:
                messagebox.showerror(title="Sorry too much!", message="Sorry but you have to change roomtype to economy!")
                return

            if Fname in kwargs[user_name]['InfoHotel'] or Lname in kwargs[user_name]['InfoHotel']:
                messagebox.showerror(title="Already exist!", message="That name is already exists in the accounts!")
                return

            else:
                kwargs[user_name]['InfoHotel'].append({"Firstname": Fname,
                                                       "Lastname": Lname,
                                                       "RoomType": room_type,
                                                       "DurationDay": duration_day,
                                                       "DurationHours": duration_hour,
                                                       "Schedule": date_arrival,
                                                       "Company": company_count})

                print(kwargs[user_name]['InfoHotel'][1])

            txt_fname.delete(0, END)
            txt_lname.delete(0, END)
            cb_room_type.set("Select a room type..")
            cb_stay.delete(0, END)
            cb_stay_hour.delete(0, END)
            cb_day.delete(0, END)
            cb_month.delete(0, END)
            cb_year.delete(0, END)
            cb_ppl.delete(0, END)
            hotel.withdraw()

            hotel_decide = messagebox.askyesno(title="Want to go another?", message="Do you want to add another one?")

            if hotel_decide:
                hotel.deiconify()
            else:
                hotel.destroy()

        fr_hotel = Frame(hotel)
        fr_hotel.grid(row=0, column=1)

        lbl_hotel_title = Label(fr_hotel, text="| Postema Hotel", font="Garamond 20", padx=20, pady=10)
        lbl_hotel_title.grid(row=0, column=0)

        lbl_hotel_fname = Label(fr_hotel, text="Enter First Name : ", font='Georgia 10', padx=20, pady=10)
        lbl_hotel_fname.grid(row=1, column=0)

        txt_fname = Entry(fr_hotel, font="Georgia 10")
        txt_fname.grid(row=1, column=1)

        lbl_hotel_lname = Label(fr_hotel, text="Enter Last Name : ", font='Georgia 10', padx=20, pady=10)
        lbl_hotel_lname.grid(row=2, column=0)

        txt_lname = Entry(fr_hotel, font="Georgia 10")
        txt_lname.grid(row=2, column=1)

        lbl_room_type = Label(fr_hotel, text="Room Type : ", font="Georgia 10", padx=20, pady=10)
        lbl_room_type.grid(row=3, column=0)

        cb_room_type_var = StringVar()
        cb_room_type_val = ["Select a room type..", "Regular", "Deluxe", "Economy"]
        cb_room_type = ttk.Combobox(fr_hotel, width=12, textvariable=cb_room_type_var, values=cb_room_type_val)
        cb_room_type.current(0)
        cb_room_type.grid(row=3, column=1)

        lbl_stay = Label(fr_hotel, text="Stay Duration (Day/s) (Hour/s): ", font="Georgia 10", padx=20, pady=10)
        lbl_stay.grid(row=4, column=0)

        cb_stay_var = StringVar()
        cb_stay_val = [x for x in range(0, 32)]
        cb_stay = ttk.Combobox(fr_hotel, width=5, textvariable=cb_stay_var, values=cb_stay_val)
        cb_stay.current(0)
        cb_stay.grid(row=4, column=1)

        cb_stay_hour_var = StringVar()
        cb_stay_hour_val = [x for x in range(0, 25)]
        cb_stay_hour = ttk.Combobox(fr_hotel, width=5, textvariable=cb_stay_hour_var, values=cb_stay_hour_val)
        cb_stay_hour.current(0)
        cb_stay_hour.grid(row=4, column=2)

        lbl_date = Label(fr_hotel, text="Date of reservation (Month) (Day) (Year) : ", font="Georgia 10", padx=20,
                         pady=10)
        lbl_date.grid(row=5, column=0)

        cb_day_var = StringVar()
        cb_month_var = StringVar()
        cb_year_var = StringVar()

        cb_day_val = [x for x in range(1, 32)]
        cb_month_val = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                        "October", "November", "December"]
        cb_year_val = [x for x in range(2024, 2050)]

        cb_month = ttk.Combobox(fr_hotel, textvariable=cb_month_var, width=5, values=cb_month_val)
        cb_month.grid(row=5, column=1)

        cb_day = ttk.Combobox(fr_hotel, textvariable=cb_day_var, width=5, values=cb_day_val)
        cb_day.grid(row=5, column=2)

        cb_year = ttk.Combobox(fr_hotel, textvariable=cb_year_var, width=5, values=cb_year_val)
        cb_year.grid(row=5, column=3)

        lbl_ppl = Label(fr_hotel, text="Company Count : ", font="Georgia 10", padx=20, pady=10)
        lbl_ppl.grid(row=6, column=0)

        cb_ppl_var = StringVar()
        cb_ppl_val = [x for x in range(0, 20)]
        cb_ppl = ttk.Combobox(fr_hotel, width=5, textvariable=cb_ppl_var, values=cb_ppl_val)
        cb_ppl.current(0)
        cb_ppl.grid(row=6, column=1)

        fr_hotel_bt = Frame(hotel)
        fr_hotel_bt.grid(row=7, column=1)

        bt_hotel_submit = Button(fr_hotel_bt, text="Submit", bd=5, relief=RAISED, padx=20, pady=10, command=hotel_submit)
        bt_hotel_submit.grid(row=7, column=0, sticky=W)

        bt_hotel_cancel = Button(fr_hotel_bt, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10)
        bt_hotel_cancel.grid(row=7, column=1, sticky=E)

        hotel.mainloop()

    def check_out():
        if len(kwargs[username]['InfoResort']) == 1 and len(kwargs[username]['InfoHotel']) == 1:
            messagebox.showerror(title="NO Reservation filled in!", message="Please input a reservation information first!")
            return

        decision = messagebox.askyesno(title="You sure?", message="Are you sure your done in reservation information?")

        if decision:

            check = Toplevel()
            check.title("Check-out")

            for x in range(len(kwargs[username]['InfoResort'])):
                if x == 0:
                    pass
                else:
                    resort = kwargs[username]['InfoResort'][x]
                    if resort['Age'] < 18:
                        kwargs[username]['TotalResort'] += resort_price['Kids']
                    else:
                        kwargs[username]['TotalResort'] += resort_price['Adult']
                    print(kwargs[username]['TotalResort'])

            for y in range(len(kwargs[username]['InfoHotel'])):
                if y == 0:
                    pass
                else:
                    hotel = kwargs[username]['InfoHotel'][y]

                    if hotel['RoomType'] == "Deluxe":
                        DayTotal = hotel['DurationDay'] * hotel_price['DeluxePerDay']
                        HoursTotal = hotel['DurationHours'] * hotel_price['DeluxePerHour']

                        hotel['TotalHotel'] = DayTotal + HoursTotal

                    elif hotel['RoomType'] == "Regular" or hotel['RoomType'] == "Economy":
                        RegDayTotal = hotel['DurationDay'] * hotel_price['PerDay']
                        RegHoursTotal = hotel['DurationHours'] * hotel_price['PerHour']

                        kwargs[username]['TotalHotel'] += RegDayTotal + RegHoursTotal

                    else:
                        messagebox.showerror(title="Error!", message="Nope! Not it!")
                        return

                    total_accumulation = kwargs[username]['TotalResort'] + kwargs[username]['TotalHotel']
                    kwargs[username]['Total'] += total_accumulation
                    print(kwargs[username]['TotalHotel'])
                    print(kwargs[username]['TotalResort'])
                    print(kwargs[username]['Total'])

            check.mainloop()

        else:
            messagebox.showerror(title="No Informations are filled!", message="Please fill out the information form!")
            return

    def edit_reserve():
        edit = Toplevel()
        edit.title("Edit Reservation")

        def cancel_submit():
            edit.destroy()

        def edit_submit():
            choice = cb_choice.get()
            edit.withdraw()

            if choice == "Select a category to edit.." or choice == "":
                messagebox.showerror(title='Error!', message="Please choice an appropriate category!")
                return

            if choice == "Resort Reservation":

                if len(kwargs[username]['InfoResort']) == 1:
                    messagebox.showerror(title="Empty!", message="You don't have a reservation!")
                    return

                main_edit_resort = Toplevel()
                main_edit_resort.title("Editing..")

                def cancel_editing():
                    main_edit_resort.destroy()
                    edit.deiconify()

                def name_edit():
                    name_to_edit_resort = cb_select_name.get()

                    if name_to_edit_resort not in resort_firstname_val or name_to_edit_resort == "":
                        messagebox.showerror(title="No such name!", message="Please select a appropriate name!")
                        return

                    lt_users_items = []

                    for index in range(len(kwargs[username]['InfoResort'])):
                        if name_to_edit_resort in kwargs[username]['InfoResort'][index].values():
                            lbl_select_name.destroy()
                            cb_select_name.grid_forget()
                            bt_submit_editing.destroy()
                            bt_cancel_editing.destroy()

                            for key, value in kwargs[username]['InfoResort'][index].items():
                                lt_users_items.append(value)

                            for about in lt_users_items:
                                lt_items_to_edit.insert(END, about)

                            lbl_labels.grid(row=1, column=0)

                            lt_items_to_edit.grid(row=1, column=1)
                            lt_items_to_edit.config(height=lt_items_to_edit.size())

                            bt_submit_edited.grid(row=4, column=0, sticky=W)
                            bt_cancel_edited.grid(row=4, column=1, sticky=E)

                def edit_now():
                    item_index = lt_items_to_edit.curselection()
                    name_index = cb_select_name.current()

                    if item_index:
                        selected_index = item_index[0]

                        if selected_index == 0:
                            edit_name = Toplevel()
                            edit_name.title("Edit Name")

                            def edit_name_now():
                                name_edited = txt_edit_name.get()

                                if name_edited == "":
                                    messagebox.showerror(title="Error!", message="Please Input a name first!")
                                    return

                                edit_name_wow = kwargs[username]['InfoResort'][name_index + 1]
                                edit_name_wow['Firstname'] = name_edited

                                for item_select in lt_items_to_edit.curselection():
                                    lt_items_to_edit.delete(item_select)
                                    lt_items_to_edit.insert(item_select, name_edited)

                                edit_name.destroy()

                            lbl_edit_name_title = Label(edit_name, text="| Edit First Name", font="Garamond 20", padx=20, pady=10)
                            lbl_edit_name_title.grid(row=0, column=0)

                            lbl_edit_name = Label(edit_name, text="Input name you want to edit : ", font="Georgia 10", padx=20, pady=10)
                            lbl_edit_name.grid(row=1, column=0)

                            txt_edit_name = Entry(edit_name)
                            txt_edit_name.grid(row=1, column=1)

                            bt_edit_name = Button(edit_name, text="Done", bd=5, relief=RAISED, padx=20, pady=10, command=edit_name_now)
                            bt_edit_name.grid(row=2, column=1)

                            edit_name.mainloop()

                        if selected_index == 1:
                            edit_lname = Toplevel()
                            edit_lname.title("Edit LastName")

                            def edit_lname_now():
                                lname_edited = txt_edit_lname.get()

                                if lname_edited == "":
                                    messagebox.showerror(title="Error!", message="Please Input a name first!")
                                    return

                                edit_lname_wow = kwargs[username]['InfoResort'][name_index + 1]
                                edit_lname_wow['Lastname'] = lname_edited

                                for item_select in lt_items_to_edit.curselection():
                                    lt_items_to_edit.delete(item_select)
                                    lt_items_to_edit.insert(item_select, lname_edited)

                                edit_lname.destroy()

                            lbl_edit_lname_title = Label(edit_lname, text="| Edit Last Name", font="Garamond 20",
                                                        padx=20, pady=10)
                            lbl_edit_lname_title.grid(row=0, column=0)

                            lbl_edit_lname = Label(edit_lname, text="Input lastname you want to edit : ", font="Georgia 10",
                                                  padx=20, pady=10)
                            lbl_edit_lname.grid(row=1, column=0)

                            txt_edit_lname = Entry(edit_lname)
                            txt_edit_lname.grid(row=1, column=1)

                            bt_edit_lname = Button(edit_lname, text="Done", bd=5, relief=RAISED, padx=20, pady=10,
                                                   command=edit_lname_now)
                            bt_edit_lname.grid(row=2, column=1)

                            edit_lname.mainloop()

                        if selected_index == 2:
                            edit_age = Toplevel()
                            edit_age.title("Edit Age")

                            def edit_age_done():
                                item_edit = cb_edit_age.get()

                                edit_age_now = kwargs[username]['InfoResort'][name_index + 1]
                                edit_age_now['Age'] = item_edit

                                for item_select in lt_items_to_edit.curselection():
                                    lt_items_to_edit.delete(item_select)
                                    lt_items_to_edit.insert(item_select, item_edit)

                                edit_age.destroy()

                            lbl_edit_age_title = Label(edit_age, text="| Edit Age", font="Garamond 20",
                                                        padx=20, pady=10)
                            lbl_edit_age_title.grid(row=0, column=0)

                            lbl_item_edit = Label(edit_age, font="Georgia 10", text="Input what you want : ", padx=20,
                                                  pady=10)
                            lbl_item_edit.grid(row=1, column=0)

                            cb_edit_age_val = [x for x in range(1,99)]
                            cb_edit_age = ttk.Combobox(edit_age, width=5, values=cb_edit_age_val)
                            cb_edit_age.grid(row=1, column=1)

                            bt_edit_age = Button(edit_age, text="Done", bd=5, relief=RAISED, padx=20, pady=10, command=edit_age_done)
                            bt_edit_age.grid(row=2, column=1)

                            edit_age.mainloop()

                        if selected_index == 3:
                            edit_time = Toplevel()
                            edit_time.title("Edit Time")

                            def edit_time_now():
                                editted_time = cb_edit_time.get()

                                if editted_time == 'Select time..' or editted_time == "":
                                    messagebox.showerror(title="Error!", message="Please input a valid option!")
                                    return

                                edit_time_wow = kwargs[username]['InfoResort'][name_index + 1]
                                edit_time_wow['Time'] = editted_time

                                for item_select in lt_items_to_edit.curselection():
                                    lt_items_to_edit.delete(item_select)
                                    lt_items_to_edit.insert(item_select, editted_time)

                                edit_time.destroy()

                            lbl_edit_time_title = Label(edit_time, text="| Edit Time", font="Garamond 20",
                                                        padx=20, pady=10)
                            lbl_edit_time_title.grid(row=0, column=0)

                            lbl_edit_time = Label(edit_time, text="Enter time edit : ", font="Georgia 10", padx=20, pady=10)
                            lbl_edit_time.grid(row=1, column=0)

                            cb_edit_time_val = ['Select time..', 'Daytime', 'Overnight']
                            cb_edit_time = ttk.Combobox(edit_time, width=8, values=cb_edit_time_val)
                            cb_edit_time.grid(row=1, column=1)

                            bt_edit_time = Button(edit_time, text="Done", bd=5, relief=RAISED, padx=20, pady=10, command=edit_time_now)
                            bt_edit_time.grid(row=2, column=1)

                            edit_time.mainloop()

                        if selected_index == 4:
                            edit_sched = Toplevel()
                            edit_sched.title("Edit Schedule")

                            def okay():
                                edit_month = cb_edit_month.get()
                                edit_day = cb_edit_day.get()
                                edit_year = cb_edit_year.get()
                                edit_schedule = edit_month + '/' + edit_day + '/' + edit_year

                                if edit_month not in cb_month_val or edit_day == "" or edit_year == "":
                                    messagebox.showerror(title='Invalid!3', message="None of the options available!")
                                    return

                                edit_schedule_wow = kwargs[username]['InfoResort'][name_index + 1]
                                edit_schedule_wow['Schedule'] = edit_schedule

                                for item_selected in lt_items_to_edit.curselection():
                                    lt_items_to_edit.delete(item_selected)
                                    lt_items_to_edit.insert(item_selected, edit_schedule)

                                edit_sched.destroy()

                            lbl_edit_sched_title = Label(edit_sched, text="| Edit Schedule", font="garamond 20", padx=20, pady=10)
                            lbl_edit_sched_title.grid(row=0, column=0)

                            lbl_edit_sched = Label(edit_sched, text="Enter new schedule (Month) (Day) (Year) : ", font="Georgia 10", padx=20, pady=10)
                            lbl_edit_sched.grid(row=1, column=0)

                            fr_edit_sched = Frame(edit_sched)
                            fr_edit_sched.grid(row=1, column=1)

                            cb_day_val = [x for x in range(1, 32)]
                            cb_month_val = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                                            "October", "November", "December"]
                            cb_year_val = [x for x in range(2024, 2050)]

                            cb_edit_month = ttk.Combobox(fr_edit_sched, width=10, values=cb_month_val)
                            cb_edit_day = ttk.Combobox(fr_edit_sched, width=10, values=cb_day_val)
                            cb_edit_year = ttk.Combobox(fr_edit_sched, width=10, values=cb_year_val)

                            cb_edit_month.grid(row=1, column=1)
                            cb_edit_day.grid(row=1, column=2)
                            cb_edit_year.grid(row=1, column=3)

                            fr_bt_edit = Frame(edit_sched)
                            fr_bt_edit.grid(row=2, column=1)

                            bt_ok = Button(fr_bt_edit, text="Done", bd=5, relief=RAISED, padx=20, pady=10, command=okay)
                            bt_ok.grid(row=2, column=0, sticky=W)

                            edit_sched.mainloop()

                lbl_editing_title = Label(main_edit_resort, text="| Editing..", font="Garamond 20", padx=20, pady=10)
                lbl_editing_title.grid(row=0, column=0)

                fr_editing = Frame(main_edit_resort)
                fr_editing.grid(row=1, column=1)

                lbl_labels = Label(main_edit_resort, font="Georgia 17", text="Firstname :\n"
                                                                      "Lastname :\n"
                                                                      "Age : \n"
                                                                      "Time : \n"
                                                                      "Schedule : \n"
                                                                       )

                lt_items_to_edit = Listbox(fr_editing, width=15, height=15, bg="Beige", font="Georgia 17")

                lbl_select_name = Label(fr_editing, text="Select the name you want to edit..", font="Georgia 10", padx=20, pady=10)
                lbl_select_name.grid(row=1, column=0)

                resort_firstname_val = []
                for x in range(len(kwargs[username]['InfoResort'])):
                    y = 0
                    if x == 0:
                        pass
                    else:
                        values = list(kwargs[username]['InfoResort'][x].keys())[y]
                        resort_firstname_val.append(kwargs[username]['InfoResort'][x][values])
                        y += 1

                cb_select_name = ttk.Combobox(fr_editing, width=16, values=resort_firstname_val)
                cb_select_name.grid(row=1, column=1)

                fr_editing_bt = Frame(main_edit_resort)
                fr_editing_bt.grid(row=3, column=1)

                bt_submit_editing = Button(fr_editing_bt, text="Submit", bd=5, relief=RAISED, padx=20, pady=10, command=name_edit)
                bt_submit_editing.grid(row=3, column=0, sticky=W)

                bt_cancel_editing = Button(fr_editing_bt, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10, command=cancel_editing)
                bt_cancel_editing.grid(row=3, column=1, sticky=E)

                bt_submit_edited = Button(fr_editing_bt, text="Edit", bd=5, relief=RAISED, padx=20, pady=10, command=edit_now)

                bt_cancel_edited = Button(fr_editing_bt, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10, command=cancel_editing)

                main_edit_resort.mainloop()

            if choice == "Hotel Reservation":

                if len(kwargs[username]['InfoHotel']) == 1:
                    messagebox.showerror(title="Empty!", message="You don't have a reservation!")
                    return

                main_edit_hotel = Toplevel()
                main_edit_hotel.title("Edit Reservation Hotel")

                def cancel_name_hotel():
                    main_edit_hotel.destroy()
                    edit.deiconify()

                def submit_name_hotel():
                    name_to_edit_hotel = cb_select_name_hotel.get()

                    if name_to_edit_hotel not in hotel_firstname_val or name_to_edit_hotel == "":
                        messagebox.showerror(title="No such name!", message="Please select a appropriate name!")
                        return

                    lt_users_items_hotel = []

                    for index in range(len(kwargs[username]['InfoHotel'])):
                        if name_to_edit_hotel in kwargs[username]['InfoHotel'][index].values():
                            lbl_select_name_hotel.destroy()
                            cb_select_name_hotel.grid_forget()
                            bt_submit_editing_hotel.destroy()
                            bt_cancel_editing_hotel.destroy()

                            for key, value in kwargs[username]['InfoHotel'][index].items():
                                lt_users_items_hotel.append(value)

                            for about in lt_users_items_hotel:
                                lt_items_to_edit_hotel.insert(END, about)

                            lbl_labels_hotel.grid(row=1, column=0)

                            lt_items_to_edit_hotel.grid(row=1, column=1)
                            lt_items_to_edit_hotel.config(height=lt_items_to_edit_hotel.size())

                            bt_submit_edited_hotel.grid(row=4, column=0, sticky=W)
                            bt_cancel_edited_hotel.grid(row=4, column=1, sticky=E)

                def submit_hotel():
                    item_index_hotel = lt_items_to_edit_hotel.curselection()
                    index_name_hotel = cb_select_name_hotel.current()

                    if item_index_hotel:
                        selected_index_hotel = item_index_hotel[0]

                        if selected_index_hotel == 0: #fname

                            edit_name_hotel = Toplevel()
                            edit_name_hotel.title("Edit Name")

                            def edit_name_hotel_now():
                                name_edited_hotel = txt_edit_name_hotel.get()

                                if name_edited_hotel == "":
                                    messagebox.showerror(title="Error!", message="Please Input a name first!")
                                    return

                                edit_name_hotel_wow = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                edit_name_hotel_wow['Firstname'] = name_edited_hotel

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, name_edited_hotel)

                                edit_name_hotel.destroy()

                            lbl_edit_name_hotel_title = Label(edit_name_hotel, text="| Edit First Name", font="Garamond 20",
                                                        padx=20, pady=10)
                            lbl_edit_name_hotel_title.grid(row=0, column=0)

                            lbl_edit_name_hotel = Label(edit_name_hotel, text="Input name you want to edit : ",
                                                        font="Georgia 10",
                                                        padx=20, pady=10)
                            lbl_edit_name_hotel.grid(row=1, column=0)

                            txt_edit_name_hotel = Entry(edit_name_hotel)
                            txt_edit_name_hotel.grid(row=1, column=1)

                            bt_edit_name_hotel = Button(edit_name_hotel, text="Done", bd=5, relief=RAISED, padx=20,
                                                        pady=10,
                                                        command=edit_name_hotel_now)
                            bt_edit_name_hotel.grid(row=2, column=1)

                            edit_name_hotel.mainloop()

                        if selected_index_hotel == 1: #lname

                            edit_lname_hotel = Toplevel()
                            edit_lname_hotel.title("Edit LastName")

                            def edit_lname_hotel_now():
                                lname_edited_hotel = txt_edit_lname_hotel.get()

                                if lname_edited_hotel == "":
                                    messagebox.showerror(title="Error!", message="Please Input a name first!")
                                    return

                                edit_lname_hotel_wow = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                edit_lname_hotel_wow['Lastname'] = lname_edited_hotel

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, lname_edited_hotel)

                                edit_lname_hotel.destroy()

                            lbl_edit_lname_hotel_title = Label(edit_lname_hotel, text="| Edit Last Name",
                                                              font="Garamond 20",
                                                              padx=20, pady=10)
                            lbl_edit_lname_hotel_title.grid(row=0, column=0)

                            lbl_edit_lname_hotel = Label(edit_lname_hotel, text="Input name you want to edit : ",
                                                        font="Georgia 10",
                                                        padx=20, pady=10)
                            lbl_edit_lname_hotel.grid(row=1, column=0)

                            txt_edit_lname_hotel = Entry(edit_lname_hotel)
                            txt_edit_lname_hotel.grid(row=1, column=1)

                            bt_edit_lname_hotel = Button(edit_lname_hotel, text="Done", bd=5, relief=RAISED, padx=20,
                                                        pady=10,
                                                        command=edit_lname_hotel_now)
                            bt_edit_lname_hotel.grid(row=2, column=1)

                            edit_lname_hotel.mainloop()

                        if selected_index_hotel == 2: #Roomtype Str
                            edit_room_hotel = Toplevel()
                            edit_room_hotel.title("Edit Room Type")

                            def room_edit():
                                room_edited = cb_room.get()

                                if room_edited not in cb_room_val or room_edited == "":
                                    messagebox.showerror(title="Error!", message="No such thing!")
                                    return

                                value_room = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                value_room['RoomType'] = room_edited

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, room_edited)

                                edit_room_hotel.destroy()

                            lbl_edit_room_title = Label(edit_room_hotel, text="| Edit Room Type", font="Garamond 20", padx=20, pady=10)
                            lbl_edit_room_title.grid(row=0, column=0)

                            lbl_edit_room = Label(edit_room_hotel, text="Select a room type :", font="Georgia 10", padx=20, pady=10)
                            lbl_edit_room.grid(row=1, column=0)

                            cb_room_val = ['Select a room type..', 'Regular', 'Deluxe', 'Economy']
                            cb_room = ttk.Combobox(edit_room_hotel, width=15, values=cb_room_val)
                            cb_room.current(0)
                            cb_room.grid(row=1, column=1)

                            fr_bt_room = Frame(edit_room_hotel)
                            fr_bt_room.grid(row=2, column=1)

                            bt_room = Button(fr_bt_room, text="Done", bd=5, relief=RAISED, pady=10, padx=20, command=room_edit)
                            bt_room.grid(row=2, column=0, sticky=W)

                            edit_room_hotel.mainloop()

                        if selected_index_hotel == 3: #Duration Day Int
                            edit_duration_day = Toplevel()
                            edit_duration_day.title("Edit Duration (Day)")

                            def day_stay():
                                day_stay_edit = int(cb_day_stay.get())

                                if day_stay_edit not in cb_day_stay_val or day_stay_edit == "":
                                    messagebox.showerror(title="Error!", message="Please try again!")
                                    return

                                value_duration_day = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                value_duration_day['DurationDay'] = day_stay_edit

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, day_stay_edit)

                                edit_duration_day.destroy()

                            lbl_edit_day_title = Label(edit_duration_day, text="| Edit Duration (Day)", font="Garamond 20", padx=20, pady=10)
                            lbl_edit_day_title.grid(row=0, column=0)

                            lbl_edit_day = Label(edit_duration_day, text="Select a day to edit : ", font="Georgia 10", padx=20, pady=10)
                            lbl_edit_day.grid(row=1, column=0)

                            cb_day_stay_val = [x for x in range(0, 32)]
                            cb_day_stay = ttk.Combobox(edit_duration_day, width=5, values=cb_day_stay_val)
                            cb_day_stay.grid(row=1, column=1)

                            bt_day_stay = Button(edit_duration_day, text="Done", bd=5, relief=RAISED, padx=10, pady=10, command=day_stay)
                            bt_day_stay.grid(row=2, column=1)

                            edit_duration_day.mainloop()

                        if selected_index_hotel == 4: #Duration Hours Int

                            edit_duration_hour = Toplevel()
                            edit_duration_hour.title("Edit Duration (Hour)")

                            def hour_stay():
                                hour_stay_edit = int(cb_hour_stay.get())

                                if hour_stay_edit  not in cb_hour_stay_val or hour_stay_edit == "":
                                    messagebox.showerror(title="Error!", message="Please try again!")
                                    return

                                value_duration_hour = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                value_duration_hour['DurationHour'] = hour_stay_edit

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, hour_stay_edit)

                                edit_duration_hour.destroy()

                            lbl_edit_hour_title = Label(edit_duration_hour, text="| Edit Duration (Hour)",
                                                       font="Garamond 20", padx=20, pady=10)
                            lbl_edit_hour_title.grid(row=0, column=0)

                            lbl_edit_hour = Label(edit_duration_hour, text="Select a day to edit : ", font="Georgia 10",
                                                 padx=20, pady=10)
                            lbl_edit_hour.grid(row=1, column=0)

                            cb_hour_stay_val = [x for x in range(0, 25)]
                            cb_hour_stay = ttk.Combobox(edit_duration_hour, width=5, values=cb_hour_stay_val)
                            cb_hour_stay.grid(row=1, column=1)

                            bt_hour_stay = Button(edit_duration_hour, text="Done", bd=5, relief=RAISED, padx=10, pady=10,
                                                 command=hour_stay)
                            bt_hour_stay.grid(row=2, column=1)

                            edit_duration_hour.mainloop()

                        if selected_index_hotel == 5: #Schedule Str

                            edit_sched_hotel = Toplevel()
                            edit_sched_hotel.title("Edit Schedule")

                            def okay_hotel():
                                edit_month_hotel = cb_edit_month_hotel.get()
                                edit_day_hotel = cb_edit_day_hotel.get()
                                edit_year_hotel = cb_edit_year_hotel.get()
                                edit_schedule_hotel = edit_month_hotel + '/' + edit_day_hotel + '/' + edit_year_hotel

                                if edit_month_hotel not in cb_month_hotel_val or edit_day_hotel == "" or edit_year_hotel == "":
                                    messagebox.showerror(title='Invalid!3', message="None of the options available!")
                                    return

                                edit_schedule_hotel_wow = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                edit_schedule_hotel_wow['Schedule'] = edit_schedule_hotel

                                for item_selected in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit.delete(item_selected)
                                    lt_items_to_edit.insert(item_selected, edit_schedule_hotel)

                                edit_sched_hotel.destroy()

                            lbl_edit_sched_hotel_title = Label(edit_sched_hotel, text="| Edit Schedule", font="garamond 20",
                                                         padx=20, pady=10)
                            lbl_edit_sched_hotel_title.grid(row=0, column=0)

                            lbl_edit_sched_hotel = Label(edit_sched_hotel, text="Enter new schedule (Month) (Day) (Year) : ",
                                                   font="Georgia 10", padx=20, pady=10)
                            lbl_edit_sched_hotel.grid(row=1, column=0)

                            fr_edit_sched_hotel = Frame(edit_sched_hotel)
                            fr_edit_sched_hotel.grid(row=1, column=1)

                            cb_day_hotel_val = [x for x in range(1, 32)]
                            cb_month_hotel_val = ["January", "February", "March", "April", "May", "June", "July", "August",
                                            "September",
                                            "October", "November", "December"]
                            cb_year_hotel_val = [x for x in range(2024, 2050)]

                            cb_edit_month_hotel = ttk.Combobox(fr_edit_sched_hotel, width=10, values=cb_month_hotel_val)
                            cb_edit_day_hotel = ttk.Combobox(fr_edit_sched_hotel, width=10, values=cb_day_hotel_val)
                            cb_edit_year_hotel = ttk.Combobox(fr_edit_sched_hotel, width=10, values=cb_year_hotel_val)

                            cb_edit_month_hotel.grid(row=1, column=1)
                            cb_edit_day_hotel.grid(row=1, column=2)
                            cb_edit_year_hotel.grid(row=1, column=3)

                            fr_bt_edit_hotel = Frame(edit_sched_hotel)
                            fr_bt_edit_hotel.grid(row=2, column=1)

                            bt_ok_hotel = Button(fr_bt_edit_hotel, text="Done", bd=5, relief=RAISED, padx=20, pady=10, command=okay_hotel)
                            bt_ok_hotel.grid(row=2, column=0, sticky=W)

                            edit_sched_hotel.mainloop()

                        if selected_index_hotel == 6: #Company count Int
                            edit_company = Toplevel()
                            edit_company.title("Edit Company")

                            def company_count():
                                company_edit = int(cb_company.get())

                                if company_edit not in cb_company_val or company_edit == "":
                                    messagebox.showerror(title="Error!", message="Please try again!")
                                    return

                                value_company = kwargs[username]['InfoHotel'][index_name_hotel + 1]
                                value_company['Company'] = company_edit

                                for item_select in lt_items_to_edit_hotel.curselection():
                                    lt_items_to_edit_hotel.delete(item_select)
                                    lt_items_to_edit_hotel.insert(item_select, company_edit)

                                edit_company.destroy()

                            lbl_edit_company_title = Label(edit_company, text="| Edit Company Count",
                                                        font="Garamond 20", padx=20, pady=10)
                            lbl_edit_company_title.grid(row=0, column=0)

                            lbl_edit_company = Label(edit_company, text="Select a day to edit : ", font="Georgia 10",
                                                  padx=20, pady=10)
                            lbl_edit_company.grid(row=1, column=0)

                            cb_company_val = [x for x in range(0, 25)]
                            cb_company = ttk.Combobox(edit_company, width=5, values=cb_company_val)
                            cb_company.grid(row=1, column=1)

                            bt_company = Button(edit_company, text="Done", bd=5, relief=RAISED, padx=10,
                                                  pady=10,
                                                  command=company_count)
                            bt_company.grid(row=2, column=1)

                            edit_company.mainloop()

                lbl_editing_hotel_title = Label(main_edit_hotel, text="| Editing..", font="Garamond 20", padx=20, pady=10)
                lbl_editing_hotel_title.grid(row=0, column=0)

                fr_editing_hotel = Frame(main_edit_hotel)
                fr_editing_hotel.grid(row=1, column=1)

                lbl_labels_hotel = Label(main_edit_hotel, font="Georgia 17", text="Firstname :\n"
                                                                             "Lastname :\n"
                                                                             "RoomType : \n"
                                                                             "Duration (Day) : \n"
                                                                             "Duration (Hours) : \n"
                                                                             "Schedule : \n"
                                                                             "Company : \n")

                lt_items_to_edit_hotel = Listbox(fr_editing_hotel, width=15, height=15, bg="Beige", font="Georgia 17")

                lbl_select_name_hotel = Label(fr_editing_hotel, text="Select the name you want to edit..", font="Georgia 10",
                                        padx=20, pady=10)
                lbl_select_name_hotel.grid(row=1, column=0)

                hotel_firstname_val = []
                for x in range(len(kwargs[username]['InfoHotel'])):
                    y = 0
                    if x == 0:
                        pass
                    else:
                        values = list(kwargs[username]['InfoHotel'][x].keys())[y]
                        hotel_firstname_val.append(kwargs[username]['InfoHotel'][x][values])
                        y += 1

                cb_select_name_hotel = ttk.Combobox(fr_editing_hotel, width=16, values=hotel_firstname_val)
                cb_select_name_hotel.grid(row=1, column=1)

                fr_editing_bt_hotel = Frame(main_edit_hotel)
                fr_editing_bt_hotel.grid(row=3, column=1)

                bt_submit_editing_hotel = Button(fr_editing_bt_hotel, text="Submit", bd=5, relief=RAISED, padx=20, pady=10,
                                           command=submit_name_hotel)
                bt_submit_editing_hotel.grid(row=3, column=0, sticky=W)

                bt_cancel_editing_hotel = Button(fr_editing_bt_hotel, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10,
                                           command=cancel_name_hotel)
                bt_cancel_editing_hotel.grid(row=3, column=1, sticky=E)

                bt_submit_edited_hotel = Button(fr_editing_bt_hotel, text="Edit", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=submit_hotel)

                bt_cancel_edited_hotel = Button(fr_editing_bt_hotel, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=cancel_name_hotel)

                main_edit_hotel.mainloop()

        lbl_edit_title = Label(edit, text="| Edit Reservation", font="Garamond 20", padx=20, pady=10)
        lbl_edit_title.grid(row=0, column=0)

        fr_edit = Frame(edit)
        fr_edit.grid(row=1, column=1)

        lbl_choice = Label(fr_edit, text="Select a Category..", font="Georgia 10", padx=20, pady=10)
        lbl_choice.grid(row=1, column=0)

        cb_choice_var = StringVar()
        cb_choice_val = ["Select a category to edit..", "Resort Reservation", "Hotel Reservation"]
        cb_choice = ttk.Combobox(fr_edit, width=15, textvariable=cb_choice_var, values=cb_choice_val)
        cb_choice.current(0)
        cb_choice.grid(row=1, column=1)

        fr_edit_bt = Frame(edit)
        fr_edit_bt.grid(row=2, column=1)

        bt_choice_submit = Button(fr_edit_bt, text="Submit", bd=5, relief=RAISED, pady=10, padx=20, command=edit_submit)
        bt_choice_submit.grid(row=2, column=0, sticky=W)

        bt_choice_cancel = Button(fr_edit_bt, text="Cancel", bd=5, relief=RAISED, pady=10, padx=20, command=cancel_submit)
        bt_choice_cancel.grid(row=2, column=1, sticky=E)

        edit.mainloop()

    def delete_reserve():

        delete = Toplevel()
        delete.title("| Delete reservation")

        def cancel_main():
            delete.destroy()

        def delete_main_submit():
            category_delete = cb_delete_option.get()

            if category_delete not in cb_delete_option_val or category_delete == "":
                messagebox.showerror(title="Empty!", message="Please enter a valid category!")
                return

            if category_delete == 'Resort Reservation':
                delete.withdraw()

                if len(kwargs[username]['InfoResort']) == 1:
                    messagebox.showerror(title='No reservation!', message="No reservations!")
                    return

                main_delete = Toplevel()
                main_delete.title("Delete a reservation Resort")

                def submit_delete():
                    to_delete_name = cb_delete.get()
                    delete_index = cb_delete.current()

                    if to_delete_name == 'Select a reservation to delete..' or to_delete_name not in resort_delete_val or to_delete_name == "":
                        messagebox.showerror(title="Error!",
                                             message="Please make sure you select an appropriate option!")
                        return

                    del kwargs[username]['InfoResort'][delete_index]
                    cb_delete_option_val.pop(delete_index)

                def cancel_delete():
                    main_delete.destroy()
                    delete.deiconify()

                resort_delete_val = ['Select a reservation to delete..']
                for x in range(len(kwargs[username]['InfoResort'])):
                    y = 0
                    if x == 0:
                        pass
                    else:
                        values = list(kwargs[username]['InfoResort'][x].keys())[y]
                        resort_delete_val.append(kwargs[username]['InfoResort'][x][values])
                        y += 1

                lbl_delete_title = Label(main_delete, text="Delete a reservation", font="Garamond 20", padx=20, pady=10)
                lbl_delete_title.grid(row=0, column=0)

                lbl_delete = Label(main_delete, text="Select a name to remove : ", font="Georgia 10", padx=20, pady=10)
                lbl_delete.grid(row=1, column=0)

                cb_delete = ttk.Combobox(main_delete, width=10, values=resort_delete_val)
                cb_delete.current(0)
                cb_delete.grid(row=1, column=1)

                fr_bt_delete = Frame(main_delete)
                fr_bt_delete.grid(row=2, column=1)

                bt_delete_submit = Button(fr_bt_delete, text="Submit", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=submit_delete)
                bt_delete_submit.grid(row=2, column=0, sticky=W)

                bt_delete_cancel = Button(fr_bt_delete, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=cancel_delete)
                bt_delete_cancel.grid(row=2, column=1, sticky=E)

                main_delete.mainloop()

            if category_delete == 'Hotel Reservation':

                if len(kwargs[username]['InfoHotel']) == 1:
                    messagebox.showerror(title='No reservation!', message="No reservations!")
                    return

                delete_hotel = Toplevel()
                delete_hotel.title("Delete a reservation Hotel")

                def submit_delete_hotel():
                    to_delete_name = cb_delete_hotel.get()
                    delete_index = cb_delete_hotel.current()

                    if to_delete_name == 'Select a reservation to delete..' or to_delete_name not in hotel_delete_val or to_delete_name == "":
                        messagebox.showerror(title="Error!",
                                             message="Please make sure you select an appropriate option!")
                        return

                    del kwargs[username]['InfoHotel'][delete_index]
                    cb_delete_option_val.pop(delete_index)

                def cancel_delete_hotel():
                    delete_hotel.destroy()
                    delete.deiconify()

                hotel_delete_val = ['Select a reservation to delete..']
                for x in range(len(kwargs[username]['InfoHotel'])):
                    y = 0
                    if x == 0:
                        pass
                    else:
                        values = list(kwargs[username]['InfoHotel'][x].keys())[y]
                        hotel_delete_val.append(kwargs[username]['InfoHotel'][x][values])
                        y += 1

                lbl_delete_title = Label(delete_hotel, text="Delete a reservation", font="Garamond 20", padx=20, pady=10)
                lbl_delete_title.grid(row=0, column=0)

                lbl_delete = Label(delete_hotel, text="Select a name to remove : ", font="Georgia 10", padx=20, pady=10)
                lbl_delete.grid(row=1, column=0)

                cb_delete_hotel = ttk.Combobox(delete_hotel, width=10, values=hotel_delete_val)
                cb_delete_hotel.current(0)
                cb_delete_hotel.grid(row=1, column=1)

                fr_bt_delete_hotel = Frame(delete_hotel)
                fr_bt_delete_hotel.grid(row=2, column=1)

                bt_delete_submit = Button(fr_bt_delete_hotel, text="Submit", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=submit_delete_hotel)
                bt_delete_submit.grid(row=2, column=0, sticky=W)

                bt_delete_cancel = Button(fr_bt_delete_hotel, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10,
                                          command=cancel_delete_hotel)
                bt_delete_cancel.grid(row=2, column=1, sticky=E)

                delete_hotel.mainloop()

        lbl_delete_title_main = Label(delete, text="| Delete Reservation", font="Garamond 20", padx=20, pady=10)
        lbl_delete_title_main.grid(row=0, column=0)

        lbl_delete_option = Label(delete, text="Select a category to delete on : ", font="Georgia 10", padx=20, pady=10)
        lbl_delete_option.grid(row=1, column=0)

        cb_delete_option_val = ['Select a category..', 'Resort Reservation', 'Hotel Reservation']
        cb_delete_option = ttk.Combobox(delete, width=17, values=cb_delete_option_val)
        cb_delete_option.current(0)
        cb_delete_option.grid(row=1, column=1)

        fr_bt_delete_main = Frame(delete)
        fr_bt_delete_main.grid(row=2, column=1)

        bt_delete_main_submit = Button(fr_bt_delete_main, text="Submit", bd=5, relief=RAISED, padx=20, pady=10, command=delete_main_submit)
        bt_delete_main_submit.grid(row=2, column=0, sticky=W)

        bt_delete_main_cancel = Button(fr_bt_delete_main, text="Cancel", bd=5, relief=RAISED, padx=20, pady=10, command=cancel_main)
        bt_delete_main_cancel.grid(row=2, column=1, sticky=E)

        delete.mainloop()

    menu_bar_main = Menu(page)
    page.config(menu=menu_bar_main)

    menu_reserve = Menu(menu_bar_main, tearoff=0)
    menu_reserve.add_separator()
    menu_reserve.add_command(label="Resort Reservation", command=resort_postema)
    menu_reserve.add_separator()
    menu_reserve.add_command(label="Hotel Reservation", command=hotel_postema)
    menu_reserve.add_separator()
    menu_bar_main.add_cascade(label="Reservations", menu=menu_reserve)

    menu_checkout = Menu(menu_bar_main, tearoff=0)
    menu_checkout.add_command(label="Submit Reservation", command=check_out)
    menu_checkout.add_separator()
    menu_checkout.add_command(label="Edit Reservation", command=edit_reserve)
    menu_checkout.add_command(label="Delete Reservation", command=delete_reserve)
    menu_bar_main.add_cascade(label="Checkout", menu=menu_checkout)

    lbl_page_title = Label(page, text="| Postema Website", font="Garamond 20", padx=20, pady=10)
    lbl_page_title.grid(row=0, column=0)

    fr_page = Frame(page)
    fr_page.grid(row=1, column=1)

    page.mainloop()

administrator_account()

if not admin_account:
    messagebox.showerror(title="Error! NO admin acc", message="Please create first an admin account!")
    quit()

main = Tk()
main.title("Log-In")
main.geometry("475x250")


def check_login():
    username = txt_user.get()
    password = txt_pass.get()

    if username in admin_account and admin_account[username] == password:
        messagebox.showinfo(title="Wow!", message="Iloveyou admin!")
        main.withdraw()
        main_postema(**admin_account)

    if username in user_account and password == user_account[username]['Password']:
        messagebox.showinfo(title="Congrats!", message="Congratulations manigga!")
        main.withdraw()
        main_postema(**user_account)
    else:
        txt_user.delete(0, END)
        txt_pass.delete(0, END)
        messagebox.showerror(title="Not safe ka!", message="ayso tayo pre!")
        return


menu_bar = Menu(main)
main.config(menu=menu_bar)

log_in = Menu(menu_bar, tearoff=0)
log_in.add_command(label="Administrator Login")
log_in.add_separator()
log_in.add_command(label="Sign-up", command=sign_up)
menu_bar.add_cascade(label="Login options", menu=log_in)

fr_main = Frame(main)
fr_main.grid(row=0, column=1)

lbl_title = Label(fr_main, text="| Postema Resort", font="Garamond 20", padx=20, pady=10)
lbl_title.grid(row=0, column=0)

lbl_user = Label(fr_main, text="Username : ", font="Georgia 10", padx=20, pady=10)
lbl_user.grid(row=1, column=0)

txt_user = Entry(fr_main, width=25)
txt_user.grid(row=1, column=1)

lbl_pass = Label(fr_main, text="Password :", font="Georgia 10", padx=20, pady=10)
lbl_pass.grid(row=2, column=0)

txt_pass = Entry(fr_main, width=25, show='*')
txt_pass.grid(row=2, column=1)

bt_login = Button(fr_main, text="Log-in", bd=5, padx=20, pady=10, relief=RAISED, command=check_login)
bt_login.grid(row=3, column=1)

main.mainloop()

