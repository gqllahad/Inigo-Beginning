from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Changed : Chosen_algo
#Changed: Strinvar() Chosen_algo


main = Tk()
main.title("| CPU Scheduling")
main.state("zoomed")
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)
main.config(bg="#0e4517")

#Nonpreemptive Algorithm
def fcfs(listo):
    t = 0
    ganntt = []
    completed = {}
    occurance = []

    while len(listo) != 0:
        available = [job for job in listo if job[0] <= t]

        if len(available) == 0:
            ganntt.append('Idle')
            occurance.append(t)
            t += 1

        else:
            available.sort(key=lambda x: x[0])

            processing = available[0]
            ganntt.append(processing[2])
            occurance.append(t)
            arrive = processing[0]
            burst = processing[1]

            t += processing[1]

            listo.remove(processing)

            jid = processing[2]
            ct = t
            tt = ct - int(arrive)
            wt = tt - int(burst)
            completed[jid] = [arrive,burst,ct, tt, wt]

    return ganntt, completed, t, occurance


def sjf(listo):
    for x in range(len(listo)):
        sub = listo[x][0]
        listo[x][0] = listo[x][1]
        listo[x][1] = sub

    t = 0
    gantt = []
    completed = {}
    occurance = []
    listo.sort()

    while len(listo) != 0:
        available = [job for job in listo if job[1] <= t]

        if len(available) == 0:
            gantt.append("Idle")
            occurance.append(t)
            t += 1

        else:
            available.sort(key=lambda x: x[0])

            process = available[0]
            gantt.append(process[2])
            occurance.append(t)
            arrive = process[1]
            burst = process[0]
            t += process[0]

            jid = process[2]
            ct = t
            tt = ct - arrive
            wt = tt - burst
            completed[jid] = [arrive,burst,ct, tt, wt]

            listo.remove(process)
    return gantt, completed, t, occurance


def npp(listo):
    for x in range(len(listo)):
        sub = listo[x][2]
        listo[x][2] = listo[x][0]
        listo[x][0] = sub

    t = 0
    gantt = []
    complete = {}
    occurance = []

    while len(listo) != 0:
        available = [job for job in listo if job[2] <= t]

        if len(available) == 0:
            gantt.append("Idle")
            occurance.append(t)
            t += 1

        else:
            available.sort()

            process = available[0]
            gantt.append(process[3])
            occurance.append(t)
            arrive = process[2]
            burst = process[1]
            prio = process[0]
            t += process[1]

            jid = process[3]
            ct = t
            tt = ct - process[2]
            wt = tt - process[1]
            complete[jid] = [arrive,burst,prio,ct, tt, wt]

            listo.remove(process)

    return gantt, complete, t, occurance


#Preemptive Algo

def srjf(listo):
    for x in range(len(listo)):
        sub = listo[x][1]
        listo[x][1] = listo[x][0]
        listo[x][0] = sub

    original_burst = {srj[2]: srj[0] for srj in listo}

    t = 0
    gantt = []
    occurs = []
    complete = {}

    while len(listo) != 0:
        available = [job for job in listo if job[1] <= t]

        if len(available) == 0:
            gantt.append("Idle")
            occurs.append(t)
            t += 1
            continue

        else:

            available.sort()
            process = available[0]
            gantt.append(process[2])
            occurs.append(t)
            t += 1
            listo.remove(process)

            process[0] -= 1

            if process[0] == 0:
                jid = process[2]
                arrive = process[1]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                complete[jid] = [arrive, original_burst[jid], ct, tt, wt]
                continue

            else:
                listo.append(process)

    return gantt, complete, t, occurs


def pp(listo):

    for x in range(len(listo)):
        sub = listo[x][2]
        listo[x][2] = listo[x][0]
        listo[x][0] = sub

    original_burst = {ps[3]: ps[1] for ps in listo}

    t = 0
    gantt = []
    complete = {}
    occurs = []

    while len(listo) != 0:

        available = [job for job in listo if job[2] <= t]

        if len(available) == 0:
            gantt.append("Idle")
            occurs.append(t)
            t += 1
            continue

        else:
            available.sort()
            process = available[0]
            gantt.append(process[3])
            occurs.append(t)
            arrive = process[2]
            prio = process[0]
            t += 1
            listo.remove(process)

            process[1] -= 1

            if process[1] == 0:
                jid = process[3]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                complete[jid] = [arrive,original_burst[jid],prio,ct,tt,wt]
                continue

            else:
                listo.append(process)

    return gantt, complete, t, occurs


def rrs(listo, quantum):

    t = 0
    gantt = []
    complete = {}
    occuranse = []

    original_burst = {rnd[2]: rnd[1] for rnd in listo}

    listo.sort()

    while len(listo) != 0:
        available = [job for job in listo if job[0] <= t]

        if len(available) == 0:
            gantt.append('Idle')
            occuranse.append(t)
            t += 1
            continue

        else:
            process = available[0]
            gantt.append(process[2])
            occuranse.append(t)
            listo.remove(process)

            rbt = process[1]

            if rbt <= quantum:
                t += rbt
                jid = process[2]
                arrive = process[0]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                complete[jid] = [arrive, original_burst[jid], ct, tt, wt]
                continue

            else:
                t += quantum
                process[1] -= quantum
                listo.append(process)

    return gantt, complete, t, occuranse

#Main functions
def algo():
    chosen_algo.set(cb_algo.get())

    if chosen_algo.get() not in cb_algo_val:
        messagebox.showerror(title="Error!", message="Please be serious!")
        cb_algo.delete(0, END)
        return

    def cur_table():

        def black():
            table.destroy()
            cb_jobs.delete(0, END)
            main.deiconify()
            main.state("zoomed")

        def shoot():

            if chosen_algo.get() == "Round Robin":
                try:
                    quantum = int(quantum_var.get())

                except ValueError:
                    messagebox.showerror(title="Value Error boss!", message="Please insert a number not some weird data!")
                    return

            for indx, arr in enumerate(arrive_time_entry):

                try:
                    arrival_time = int(arr.get())

                except ValueError:
                    messagebox.showerror(title="Invalid input!", message="Please use numbers in Burst time!")
                    txt_arrive.delete(0, END)
                    return

                if arrival_time == "" or arrival_time < 1:
                    messagebox.showerror(title="Kulang sa Burst time!!",
                                         message="Please fill up all the burst time rows!!")
                    return

            for indx, bt in enumerate(burst_time_entry):

                try:
                    burst_time = int(bt.get())

                except ValueError:
                    messagebox.showerror(title="Invalid input!", message="Please use numbers in Burst time!")
                    txt_burst.delete(0, END)
                    return

                if burst_time == "" or burst_time < 1:
                    messagebox.showerror(title="Kulang sa Burst time!!", message="Please fill up all the burst time rows!!")
                    return

            if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                for indx, pri in enumerate(prio_entry):

                    try:
                        priority = int(pri.get())

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please use numbers in priority!")
                        txt_prio.delete(0,END)
                        return

                    if priority == "":
                        messagebox.showerror(title="Kulang sa Priority!!", message="Please fill up all the priority rows!! bitch")
                        return


            #complete table baby
            table.withdraw()
            comp = Tk()
            comp.title(f"| {chosen_algo.get()}")

            comp.state("zoomed")

            window_width = comp.winfo_screenwidth()
            window_length = comp.winfo_screenheight()
            comp.geometry(f"{window_width}x{window_length}")

            def return_table():
                table.deiconify()
                table.state("zoomed")
                comp.destroy()

            #change
            def change_algo():

                def letsgo():
                    chosen_algo.set(algo_dropdown.get())

                    if chosen_algo.get() == "Round Robin":
                        change.withdraw()

                        def change_rr():
                            quantum_var.set(txt_quantum_change.get())

                            rr_change.destroy()
                            change.destroy()
                            comp.destroy()
                            shoot()

                        def change_cancel():
                            rr_change.destroy()
                            change.deiconify()

                        rr_change = Toplevel()
                        rr_change.title("Quantum Input")
                        rr_change.config(bg=colour)

                        lbl_quantum_change = Label(rr_change, text="Enter Quantum : ", font="Georgia 50", padx=20, pady=10, bg=colour)
                        lbl_quantum_change.grid(row=0, column=0)

                        txt_quantum_change = Entry(rr_change, width=20, bg="#d3cbc0",font="Georgia 20", textvariable=quantum_var)
                        txt_quantum_change.grid(row=0, column=1)

                        bt_change_rr = Button(rr_change, text="Done", bd=5, relief=RAISED,font="Georgia 25", padx=20, pady=10, command=change_rr, bg=field_colour)
                        bt_change_rr.grid(row=1, column=1, sticky="nsew")

                        bt_cancel_change_rr = Button(rr_change, text="Return", bd=5, font="Georgia 25", relief=RAISED, padx=20, pady=10, command=change_cancel)
                        bt_cancel_change_rr.grid(row=1, column=2, sticky="nsew")

                        rr_change.mainloop()

                    elif len(prio_entry) == 0 and chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority" and old_algo in prio_algo:
                        def prio_add():
                            prio_tk.destroy()
                            change.destroy()
                            comp.destroy()
                            shoot()

                        def prio_cancel():
                            prio_tk.destroy()
                            change.deiconify()

                        change.withdraw()

                        prio_tk = Toplevel()
                        prio_tk.title("Priority Change")
                        prio_tk.config(bg="#0e4517")

                        #prio_tk.grab_set()

                        lbl_boo = Label(prio_tk, text="|Add Priority", font="Garamond 25", bg="#0e4517")
                        lbl_boo.grid(row=0, column=0, sticky="nsew")

                        for b in range(jobs):
                            lbl_change_job = Label(prio_tk, text=f"Job {b + 1}", font="Georgia 10",bg="#0e4517",
                                              fg=field_colour)
                            lbl_change_job.grid(row=b + 1, column=0, sticky="ew")

                            prio_var = StringVar()
                            prio_entry.append(prio_var)

                            txt_prio_change = Entry(prio_tk, width=20, textvariable=prio_var, bg="#d3cbc0",
                                             font="Georgia 15")
                            txt_prio_change.grid(row=b + 1, column=1, sticky="ew")

                            txt_prio_change.delete(0, END)

                        bt_prio_done = Button(prio_tk, text="Done", bd=5, padx=20, pady=10, font="Georgia 10", command=prio_add, bg=field_colour)
                        bt_prio_done.grid(row=jobs + 1, column=1, sticky="nsew")

                        bt_prio_cancel = Button(prio_tk, text="Cancel", bd=5, padx=20, pady=10, font="Georgia 10",
                                              command=prio_cancel)
                        bt_prio_cancel.grid(row=jobs + 1, column=2, sticky="ew")

                        prio_tk.mainloop()

                    else:
                        change.destroy()
                        comp.destroy()
                        shoot()

                def cancel_change():
                    #comp.deiconify()
                    change.destroy()

                prio_algo = ["First Come First Serve", "Shortest Remaining Job First", "Shortest Job First", "Round Robin"]

                old_algo = chosen_algo.get()
                #comp.withdraw()
                process_list.clear()

                change = Toplevel(comp)
                change.title("Changing Algorithm..")
                change.config(bg=colour)

                change.grab_set()

                lbl_change_title = Label(change, text="| Change Algorithm", font="Garamond 50", padx=20, pady=10, bg=colour)
                lbl_change_title.grid(row=0, column=0, sticky=W)

                lbl_algo_dropdown = Label(change, text="Select algorith to change into : ", padx=20, pady=10, font="Georgia 25", bg=colour)
                lbl_algo_dropdown.grid(row=1, column=0)

                algo_dropdown = ttk.Combobox(change, values=cb_algo_val, textvariable=chosen_algo, width=25,
                                             state="readonly", background=colour)
                algo_dropdown.grid(row=1, column=1)

                bt_change = Button(change, text="Done", font="Georgia 20", bd=5, command=letsgo, bg=field_colour)
                bt_change.grid(row=2, column=1, sticky="nsew")

                bt_change_cancel = Button(change, text='Return',font="Georgia 20", bd=5, command=cancel_change)
                bt_change_cancel.grid(row=2, column=2, sticky="ew")

                change.wait_window()

            # Timelines
            #Final TImeline baby
            def time(gantt, complete, t, occ, color, shared):
                time_unit_width = 50
                canvas_width = max(1200, 50 + t * time_unit_width + 25)#800

                scroll_frame = Frame(shared, bg=color)
                scroll_frame.grid(row=2, column=0, sticky="nsew")

                h_scrollbar = Scrollbar(scroll_frame, orient="horizontal")
                h_scrollbar.grid(row=1,column=0, sticky="ew")

                canva = Canvas(scroll_frame, width=1200, height=200, background=color, highlightthickness=0,
                               scrollregion=(0, 0, canvas_width, 200))
                canva.grid(row=0, column=0, sticky="nsew")

                gantt_canvas = Canvas(scroll_frame, width=450, height=200, background=color, highlightthickness=0,
                                      scrollregion=(0, 0, canvas_width, 200))
                gantt_canvas.grid(row=2, column=0, sticky="nsew")

                canva.configure(xscrollcommand=h_scrollbar.set)
                gantt_canvas.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.configure(command=lambda *args: [canva.xview(*args), gantt_canvas.xview(*args)])

                canva.create_line(50, 50, canvas_width - 50, 50, fill="Black", width=3)

                for x in range(t + 1):
                    x_pos = 50 + x * time_unit_width
                    canva.create_line(x_pos, 45, x_pos, 50, fill="red", width=1)
                    canva.create_text(x_pos, 65, text=f"{x}")

                arrival_pos = {}
                completion_pos = {}

                for job, details in complete.items():
                    if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                        arrival_time = details[0]
                        completion_time = details[3]
                    else:
                        arrival_time = details[0]
                        completion_time = details[2]

                    if arrival_time not in arrival_pos:
                        arrival_pos[arrival_time] = 0
                    else:
                        arrival_pos[arrival_time] += 1

                    if completion_time not in completion_pos:
                        completion_pos[completion_time] = 0
                    else:
                        completion_pos[completion_time] += 1

                    vertical_space = arrival_pos[arrival_time] * 20
                    vertical_space_cmp = completion_pos[completion_time] * 20

                    x_arrival = arrival_time * time_unit_width + 50
                    canva.create_text(x_arrival, 80 + vertical_space, text=f"{job}", fill="blue")

                    x_final = 50 + t * time_unit_width
                    canva.create_text(50 + completion_time * time_unit_width, 100 + vertical_space_cmp, text=f"{job}",
                                      fill="red")
                    canva.create_text(x_final, 65, text=str(t), fill="black", font="Arial 8")

                gantt_canvas.create_line(50, 100, canvas_width - 50, 100, fill="black", width=2)

                for i, start_time in enumerate(occ):
                    end_time = occ[i + 1] if i + 1 < len(occ) else t
                    job_name = gantt[i]

                    x_start = 50 + start_time * time_unit_width
                    x_end = 50 + end_time * time_unit_width

                    fill = "gray" if job_name == "Idle" else "beige"
                    gantt_canvas.create_rectangle(x_start, 80, x_end, 120, fill=fill, outline="black")

                    gantt_canvas.create_text((x_start + x_end) // 2, 100, text=job_name, fill="black", font="Arial 10")
                    gantt_canvas.create_text(x_start, 130, text=str(start_time), fill="black", font="Arial 8")

                gantt_canvas.create_text(x_final, 130, text=str(t), fill="black", font="Arial 8")

            #If Jobs are at minimum
            def time_low(gantt, complete, t, occ, color):
                time_unit_width = 50
                canvas_width = max(1200, 50 + t * time_unit_width + 25)

                scroll_frame = Frame(fr_timeline)
                scroll_frame.grid(row=2, column=0, sticky="nsew")

                h_scrollbar = Scrollbar(scroll_frame, orient="horizontal")
                h_scrollbar.grid(row=1,column=0, sticky="ew")

                canva = Canvas(scroll_frame, width=1200, height=200, background=color, highlightthickness=0,
                               scrollregion=(0, 0, canvas_width, 200))
                canva.grid(row=0, column=0, sticky="nsew")

                gantt_canvas = Canvas(scroll_frame, width=450, height=200, background=color, highlightthickness=0,
                                      scrollregion=(0, 0, canvas_width, 200))
                gantt_canvas.grid(row=2, column=0, sticky="nsew")

                canva.configure(xscrollcommand=h_scrollbar.set)
                gantt_canvas.configure(xscrollcommand=h_scrollbar.set)
                h_scrollbar.configure(command=lambda *args: [canva.xview(*args), gantt_canvas.xview(*args)])

                canva.create_line(50, 50, canvas_width - 50, 50, fill="Black", width=3)

                for x in range(t + 1):
                    x_pos = 50 + x * time_unit_width
                    canva.create_line(x_pos, 45, x_pos, 50, fill="red", width=1)
                    canva.create_text(x_pos, 65, text=f"{x}")

                arrival_pos = {}
                completion_pos = {}

                for job, details in complete.items():
                    if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                        arrival_time = details[0]
                        completion_time = details[3]
                    else:
                        arrival_time = details[0]
                        completion_time = details[2]

                    if arrival_time not in arrival_pos:
                        arrival_pos[arrival_time] = 0
                    else:
                        arrival_pos[arrival_time] += 1

                    if completion_time not in completion_pos:
                        completion_pos[completion_time] = 0
                    else:
                        completion_pos[completion_time] += 1

                    vertical_space = arrival_pos[arrival_time] * 20
                    vertical_space_cmp = completion_pos[completion_time] * 20

                    x_arrival = arrival_time * time_unit_width + 50
                    canva.create_text(x_arrival, 80 + vertical_space, text=f"{job}", fill="blue")

                    x_final = 50 + t * time_unit_width
                    canva.create_text(50 + completion_time * time_unit_width, 100 + vertical_space_cmp, text=f"{job}",
                                      fill="red")
                    canva.create_text(x_final, 65, text=str(t), fill="black", font="Arial 8")

                gantt_canvas.create_line(50, 100, canvas_width - 50, 100, fill="black", width=2)

                for i, start_time in enumerate(occ):
                    end_time = occ[i + 1] if i + 1 < len(occ) else t
                    job_name = gantt[i]

                    x_start = 50 + start_time * time_unit_width
                    x_end = 50 + end_time * time_unit_width

                    fill = "gray" if job_name == "Idle" else "beige"
                    gantt_canvas.create_rectangle(x_start, 80, x_end, 120, fill=fill, outline="black")

                    gantt_canvas.create_text((x_start + x_end) // 2, 100, text=job_name, fill="black", font="Arial 10")
                    gantt_canvas.create_text(x_start, 130, text=str(start_time), fill="black", font="Arial 8")

                gantt_canvas.create_text(x_final, 130, text=str(t), fill="black", font="Arial 8")


            #If jobs are in max(ragne)
            def chart_table(num_job, algo, color, shared):
                width_table = 0

                if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                    width_table = 1000
                else:
                    width_table = 950

                table_chart = Canvas(shared, highlightthickness=0, width=width_table, background=color)
                table_chart.grid(row=0, column=0, sticky="nsew")

                table_scroll = Scrollbar(shared, orient="vertical", command=table_chart.yview, background=color)
                table_scroll.grid(row=0, column=1, sticky="ns")

                table_chart.configure(yscrollcommand=table_scroll.set)

                table_frame = Frame(table_chart, bg=color)
                table_chart.create_window((0, 0), window=table_frame, anchor="nw")

                if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                    lbl_label_after = Label(table_frame, text="Jobs", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after.grid(row=0, column=2, padx=5, pady=5)

                    lbl_label_after_as = Label(table_frame, text="Arrival Time", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_as.grid(row=0, column=3, padx=5, pady=5)

                    lbl_label_after_bt = Label(table_frame, text="Burst Time", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_bt.grid(row=0, column=4, padx=5, pady=5)

                    lbl_label_after_pr = Label(table_frame, text="Priority", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_pr.grid(row=0, column=5, padx=5, pady=5)

                    lbl_label_after_ct = Label(table_frame, text="Completion time", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_ct.grid(row=0, column=6, padx=5, pady=5)

                    lbl_label_after_tt = Label(table_frame, text="Turn-around\nTime", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_tt.grid(row=0, column=7, padx=5, pady=5)

                    lbl_label_after_wt = Label(table_frame, text="Waiting Time", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_wt.grid(row=0, column=8, padx=5, pady=5)

                else:
                    lbl_label_after = Label(table_frame, text="Jobs", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after.grid(row=0, column=2, padx=5, pady=5)

                    lbl_label_after_as = Label(table_frame, text="Arrival Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_as.grid(row=0, column=3, padx=5, pady=5)

                    lbl_label_after_bt = Label(table_frame, text="Burst Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_bt.grid(row=0, column=4, padx=5, pady=5)

                    lbl_label_after_ct = Label(table_frame, text="Completion time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_ct.grid(row=0, column=5, padx=5, pady=5)

                    lbl_label_after_tt = Label(table_frame, text="Turn-around\nTime", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_tt.grid(row=0, column=6, padx=5, pady=5)

                    lbl_label_after_wt = Label(table_frame, text="Waiting Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_wt.grid(row=0, column=7, padx=5, pady=5)

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                    for x in range(num_job):
                        lbl_jobbz = Label(table_frame, text=f"Job {x + 1}", font="Georgia 15", padx=20, pady=10,
                                          bg=colour,
                                          fg=field_colour)
                        lbl_jobbz.grid(row=x + 1, column=2)

                    for x, (job, arr_var) in enumerate(algo.items()):
                        lbl_arrive = Label(table_frame, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour,
                                           fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=3)

                    for x, (job, b_var) in enumerate(algo.items()):
                        lbl_burst = Label(table_frame, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour,
                                          fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=4)

                    for x, (job, pr_var) in enumerate(algo.items()):
                        lbl_prio = Label(table_frame, text=pr_var[2], font="Georgia 15", padx=20, pady=10, bg=color,
                                         fg=field_colour)
                        lbl_prio.grid(row=x + 1, column=5)

                    for x, (job, ct_var) in enumerate(algo.items()):
                        lbl_complete = Label(table_frame, text=ct_var[3], font="Georgia 15", padx=20, pady=10,
                                             bg=colour,
                                             fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=6)

                    for x, (job, tt_var) in enumerate(algo.items()):
                        lbl_turn = Label(table_frame, text=tt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour,
                                         fg=field_colour)
                        tt += tt_var[4]
                        lbl_turn.grid(row=x + 1, column=7)

                    for x, (job, wt_var) in enumerate(algo.items()):
                        lbl_wait = Label(table_frame, text=wt_var[5], font="Georgia 15", padx=20, pady=10, bg=colour,
                                         fg=field_colour)
                        wt += wt_var[5]
                        lbl_wait.grid(row=x + 1, column=8)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(table_frame, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |",
                                         font="Garamond 15",
                                         bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=num_job + 2, column=7)

                    lbl_wt_total = Label(table_frame, text=f"Total Waiting\nTime : {round(total_wt, 2)}",
                                         font="Garamond 15",
                                         bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=num_job + 2, column=8)

                    bt_change_algo = Button(table_frame, text="Change Algorithm", font="Garamond 10", bg=field_colour,
                                            bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=num_job + 3, column=6, sticky="nsew")

                    bt_return_table = Button(table_frame, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=num_job + 3, column=5, sticky="nsew")

                else:
                    for x in range(num_job):
                        lbl_jobbz = Label(table_frame, text=f"Job {x + 1}", font="Georgia 15", padx=20, pady=10, bg=colour,
                                          fg=field_colour)
                        lbl_jobbz.grid(row=x + 1, column=2, sticky="nsew")

                    for x, (job, arr_var) in enumerate(algo.items()):
                        lbl_arrive = Label(table_frame, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour,
                                           fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=3, sticky="nsew")

                    for x, (job, b_var) in enumerate(algo.items()):
                        lbl_burst = Label(table_frame, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour,
                                          fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=4, sticky="nsew")

                    for x, (job, ct_var) in enumerate(algo.items()):
                        lbl_complete = Label(table_frame, text=ct_var[2], font="Georgia 15", padx=20, pady=10, bg=colour,
                                             fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=5, sticky="nsew")

                    for x, (job, tt_var) in enumerate(algo.items()):
                        lbl_turn = Label(table_frame, text=tt_var[3], font="Georgia 15", padx=20, pady=10, bg=colour,
                                         fg=field_colour)
                        tt += tt_var[3]
                        lbl_turn.grid(row=x + 1, column=6, sticky="nsew")

                    for x, (job, wt_var) in enumerate(algo.items()):
                        lbl_wait = Label(table_frame, text=wt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour,
                                         fg=field_colour)
                        wt += wt_var[4]
                        lbl_wait.grid(row=x + 1, column=7, sticky="nsew")

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(table_frame, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15",
                                         bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=num_job + 2, column=6, sticky="nsew")

                    lbl_wt_total = Label(table_frame, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15",
                                         bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=num_job + 2, column=7, sticky="nsew")

                    bt_change_algo = Button(table_frame, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=num_job + 3, column=5, sticky="nsew")

                    bt_return_table = Button(table_frame, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=num_job + 3, column=4, sticky="nsew")

                table_frame.update_idletasks()
                table_chart.config(scrollregion=table_chart.bbox("all"), width=width_table)

            process_list = []

            colour = ""
            field_colour = ""

            if chosen_algo.get() == "First Come First Serve":
                colour = "#434edb"
                field_colour = "#c9c9c4"

            elif chosen_algo.get() == "Shortest Job First":
                colour = "#681171"
                field_colour = "#c9c9c4"

            elif chosen_algo.get() == "Non Pre-emptive Priority":
                colour = "#0f5248"
                field_colour = "#c9c9c4"

            elif chosen_algo.get() == "Shortest Remaining Job First":
                colour = "#322203"
                field_colour = "#c9c9c4"

            elif chosen_algo.get() == "Pre-emptive Priority":
                colour = "#333130"
                field_colour = "#c9c9c4"

            elif chosen_algo.get() == "Round Robin":
                colour = "#1c322c"
                field_colour = "#c9c9c4"

            comp.config(bg=colour)

            fr_timeline = Frame(comp, bg=colour)
            fr_timeline.grid(row=jobs + 6, column=1, columnspan=7, pady=10, sticky="nsew")

            fr_shared = Frame(comp, bg=colour)
            fr_shared.grid(row=0, column=1, sticky="nsew")

            if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                if jobs < 5:
                    lbl_label_after = Label(comp, text="Jobs", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after.grid(row=0, column=1)

                    lbl_label_after_as = Label(comp, text="Arrival Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_as.grid(row=0, column=2)

                    lbl_label_after_bt = Label(comp, text="Burst Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_bt.grid(row=0, column=3)

                    lbl_label_after_pr = Label(comp, text="Priority", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_pr.grid(row=0, column=4)

                    lbl_label_after_ct = Label(comp, text="Completion time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_ct.grid(row=0, column=5)

                    lbl_label_after_tt = Label(comp, text="Turn-around\nTime", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_tt.grid(row=0, column=6)

                    lbl_label_after_wt = Label(comp, text="Waiting Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_wt.grid(row=0, column=7)
            else:
                if jobs < 5:
                    lbl_label_after = Label(comp, text="Jobs", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after.grid(row=0, column=1)

                    lbl_label_after_as = Label(comp, text="Arrival Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_as.grid(row=0, column=2)

                    lbl_label_after_bt = Label(comp, text="Burst Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_bt.grid(row=0, column=3)

                    lbl_label_after_ct = Label(comp, text="Completion time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_ct.grid(row=0, column=4)

                    lbl_label_after_tt = Label(comp, text="Turn-around\nTime", font="Garamond 20", bg=colour,
                                               fg=field_colour)
                    lbl_label_after_tt.grid(row=0, column=5)

                    lbl_label_after_wt = Label(comp, text="Waiting Time", font="Garamond 20", bg=colour, fg=field_colour)
                    lbl_label_after_wt.grid(row=0, column=6)

            for x in range(jobs):
                if jobs < 5:
                    lbl_jobbz = Label(comp, text=f"Job {x + 1}", font="Georgia 15", padx=20, pady=10, bg=colour,
                                      fg=field_colour)
                    lbl_jobbz.grid(row=x + 1, column=1)

                if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
                    process_list.append([int(arrive_time_entry[x].get()), int(burst_time_entry[x].get()), int(prio_entry[x].get()), f"J{x + 1}"])
                else:
                    process_list.append([int(arrive_time_entry[x].get()), int(burst_time_entry[x].get()), f"J{x + 1}"])

            ####################################

            if chosen_algo.get() == "First Come First Serve":
                fcfs_gantt, fcfs_complete, fcfs_time, fcfs_occur = fcfs(process_list)

                sorted_fcfs_complete = {k: fcfs_complete[k] for k in sorted(fcfs_complete)}

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    for x, (job, arr_var) in enumerate(sorted_fcfs_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_fcfs_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, ct_var) in enumerate(sorted_fcfs_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=4)

                    for x, (job, tt_var) in enumerate(sorted_fcfs_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[3]
                        lbl_turn.grid(row=x + 1, column=5)

                    for x, (job, wt_var) in enumerate(sorted_fcfs_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[4]
                        lbl_wait.grid(row=x + 1, column=6)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=5)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=6)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5, command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(fcfs_gantt, fcfs_complete, fcfs_time, fcfs_occur, colour)
                else:
                    chart_table(jobs, sorted_fcfs_complete, colour, fr_shared)

                    time(fcfs_gantt, fcfs_complete, fcfs_time, fcfs_occur, colour, fr_shared)

            if chosen_algo.get() == "Shortest Job First":
                sjf_gantt, sjf_complete, sjf_time, sjf_occur = sjf(process_list)

                sorted_sjf_complete = {k: sjf_complete[k] for k in sorted(sjf_complete)}

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    for x, (job, arr_var) in enumerate(sorted_sjf_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_sjf_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, ct_var) in enumerate(sorted_sjf_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=4)

                    for x, (job, tt_var) in enumerate(sorted_sjf_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[3]
                        lbl_turn.grid(row=x + 1, column=5)

                    for x, (job, wt_var) in enumerate(sorted_sjf_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[4]
                        lbl_wait.grid(row=x + 1, column=6)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=5)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=6)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(sjf_gantt, sjf_complete, sjf_time, sjf_occur, colour)
                else:
                    chart_table(jobs, sorted_sjf_complete, colour, fr_shared)

                    time(sjf_gantt, sjf_complete, sjf_time, sjf_occur, colour, fr_shared)

            if chosen_algo.get() == "Non Pre-emptive Priority":
                npp_gantt, npp_complete, npp_time, npp_occur = npp(process_list)

                sorted_npp_complete = {k: npp_complete[k] for k in sorted(npp_complete)}
                print(sorted_npp_complete)

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    for x, (job, arr_var) in enumerate(sorted_npp_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_npp_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, pr_var) in enumerate(sorted_npp_complete.items()):
                        lbl_prio = Label(comp, text=pr_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_prio.grid(row=x + 1, column=4)

                    for x, (job, ct_var) in enumerate(sorted_npp_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=5)

                    for x, (job, tt_var) in enumerate(sorted_npp_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[4]
                        lbl_turn.grid(row=x + 1, column=6)

                    for x, (job, wt_var) in enumerate(sorted_npp_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[5], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[5]
                        lbl_wait.grid(row=x + 1, column=7)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=6)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=7)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(npp_gantt, npp_complete, npp_time, npp_occur, colour)
                else:
                    chart_table(jobs, npp_complete, colour, fr_shared)

                    time(npp_gantt, npp_complete, npp_time, npp_occur, colour, fr_shared)

            if chosen_algo.get() == "Shortest Remaining Job First":
                srjf_gantt, srjf_complete, srjf_time, srjf_occur = srjf(process_list)

                sorted_srjf_complete = {k: srjf_complete[k] for k in sorted(srjf_complete)}

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    for x, (job, arr_var) in enumerate(sorted_srjf_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_srjf_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, ct_var) in enumerate(sorted_srjf_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=4)

                    for x, (job, tt_var) in enumerate(sorted_srjf_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[3]
                        lbl_turn.grid(row=x + 1, column=5)

                    for x, (job, wt_var) in enumerate(sorted_srjf_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[4]
                        lbl_wait.grid(row=x + 1, column=6)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=5)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=6)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(srjf_gantt, srjf_complete, srjf_time, srjf_occur, colour)
                else:
                    chart_table(jobs, sorted_srjf_complete, colour, fr_shared)

                    time(srjf_gantt, srjf_complete, srjf_time, srjf_occur, colour, fr_shared)

            if chosen_algo.get() == "Pre-emptive Priority":
                pp_gantt, pp_complete, pp_time, pp_occur = pp(process_list)

                sorted_pp_complete = {k: pp_complete[k] for k in sorted(pp_complete)}

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    for x, (job, arr_var) in enumerate(sorted_pp_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_pp_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, pr_var) in enumerate(sorted_pp_complete.items()):
                        lbl_prio = Label(comp, text=pr_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_prio.grid(row=x + 1, column=4)

                    for x, (job, ct_var) in enumerate(sorted_pp_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=5)

                    for x, (job, tt_var) in enumerate(sorted_pp_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[4]
                        lbl_turn.grid(row=x + 1, column=6)

                    for x, (job, wt_var) in enumerate(sorted_pp_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[5], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[5]
                        lbl_wait.grid(row=x + 1, column=7)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=6)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=7)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(pp_gantt, pp_complete, pp_time, pp_occur, colour)
                else:
                    chart_table(jobs, sorted_pp_complete, colour, fr_shared)

                    time(pp_gantt, pp_complete, pp_time, pp_occur, colour, fr_shared)

            if chosen_algo.get() == "Round Robin":
                rr_gantt, rr_complete, rr_time, rr_occur = rrs(process_list, quantum)

                sorted_rr_complete = {k: rr_complete[k] for k in sorted(rr_complete)}

                tt = 0
                total_tt = 0.00

                wt = 0
                total_wt = 0.00

                if jobs < 5:
                    lbl_quantum = Label(comp, text=f"Quantum : {quantum}", font="Georgia 10", padx=20, pady=10, bg=colour, fg=field_colour)
                    lbl_quantum.grid(row=0, column=0, sticky=W)

                    for x, (job, arr_var) in enumerate(sorted_rr_complete.items()):
                        lbl_arrive = Label(comp, text=arr_var[0], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_arrive.grid(row=x + 1, column=2)

                    for x, (job, b_var) in enumerate(sorted_rr_complete.items()):
                        lbl_burst = Label(comp, text=b_var[1], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_burst.grid(row=x + 1, column=3)

                    for x, (job, ct_var) in enumerate(sorted_rr_complete.items()):
                        lbl_complete = Label(comp, text=ct_var[2], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        lbl_complete.grid(row=x + 1, column=4)

                    for x, (job, tt_var) in enumerate(sorted_rr_complete.items()):
                        lbl_turn = Label(comp, text=tt_var[3], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        tt += tt_var[3]
                        lbl_turn.grid(row=x + 1, column=5)

                    for x, (job, wt_var) in enumerate(sorted_rr_complete.items()):
                        lbl_wait = Label(comp, text=wt_var[4], font="Georgia 15", padx=20, pady=10, bg=colour, fg=field_colour)
                        wt += wt_var[4]
                        lbl_wait.grid(row=x + 1, column=6)

                    total_tt = (tt / jobs)
                    total_wt = (wt / jobs)

                    lbl_tt_total = Label(comp, text=f"Total Turn-around\nTime : {round(total_tt, 2)} |", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_tt_total.grid(row=jobs + 2, column=5)

                    lbl_wt_total = Label(comp, text=f"Total Waiting\nTime : {round(total_wt, 2)}", font="Garamond 15", bg=colour, fg=field_colour)
                    lbl_wt_total.grid(row=jobs + 2, column=6)

                    bt_change_algo = Button(comp, text="Change Algorithm", font="Garamond 10", bg=field_colour, bd=5,
                                            command=change_algo)
                    bt_change_algo.grid(row=jobs + 3, column=4, sticky="nsew")

                    bt_return_table = Button(comp, text="Return", font="Garamond 10", bd=5, bg=field_colour, command=return_table)
                    bt_return_table.grid(row=jobs + 3, column=3, sticky="nsew")

                    time_low(rr_gantt, rr_complete, rr_time, rr_occur, colour)
                else:
                    chart_table(jobs, sorted_rr_complete, colour, fr_shared)

                    time(rr_gantt, rr_complete, rr_time, rr_occur, colour, fr_shared)

            comp.mainloop()

        jobss = cb_jobs.get()
        jobs = 0

        if jobss == "Select number of jobs..":
            messagebox.showerror(title="Oops!", message="Please enter an acceptable value!")
            return
        else:
            try:
                jobs = int(jobss)
            except ValueError:
                if jobs <= 1 or jobs not in cb_jobs_val:
                    messagebox.showerror(title="OOps! ayos tayo pre!", message="Please insure to input valid values!")
                    return

        main.withdraw()
        table = Toplevel()
        table.title(" Preparation Table")
        table.config(bg="#0e4517")

        table.state("zoomed")
        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure(0, weight=1)

        #Entries
        arrive_time_entry = []
        burst_time_entry = []
        prio_entry = []

        prep_width = 0

        if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":
            prep_width = 500
        else:
            prep_width = 450

        prep_table = Canvas(table, width=prep_width, bg="#0e4517", highlightthickness=0)
        prep_table.grid(row=0, column=0, sticky="nsew")

        prep_scrollbar = Scrollbar(table, orient="vertical", command=prep_table.yview)
        prep_scrollbar.grid(row=0, column=1, sticky="nse")

        prep_table.configure(yscrollcommand=prep_scrollbar.set)

        fr_table = Frame(table, bg="#0e4517")
        prep_table.create_window((0,0), window=fr_table, anchor="nw")

        lbl_labels_job = Label(fr_table, text="Jobs", font="Georgia 50", bg="#0e4517")
        lbl_labels_job.grid(row=0, column=0, padx=10)

        lbl_labels_arr = Label(fr_table, text="Arrival Time", font="Georgia 50", bg="#0e4517")
        lbl_labels_arr.grid(row=0, column=1, padx=10)

        lbl_labels_bt = Label(fr_table, text="Burst Time", font="Georgia 50", bg="#0e4517")
        lbl_labels_bt.grid(row=0, column=2, padx=10)

        for x in range(jobs):
            lbl_jobb = Label(fr_table, bg="#0e4517", text=f"Job {x + 1}", font="Garamond 40", padx=20, pady=10)
            lbl_jobb.grid(row=x + 1, column=0)

        for y in range(jobs):
            arrive_var = StringVar()
            arrive_time_entry.append(arrive_var)

            txt_arrive = Entry(fr_table, width=20, textvariable=arrive_var, bg="#d3cbc0", font="Georgia 15")
            txt_arrive.grid(row=y + 1, column=1)

            txt_arrive.delete(0, END)

        for a in range(jobs):
            burst_var = StringVar()
            burst_time_entry.append(burst_var)

            txt_burst = Entry(fr_table, width=20, textvariable=burst_var, bg="#d3cbc0", font="Georgia 15")
            txt_burst.grid(row=a + 1, column=2)

            txt_burst.delete(0, END)

        if chosen_algo.get() == "Non Pre-emptive Priority" or chosen_algo.get() == "Pre-emptive Priority":

            lbl_labels_pri = Label(fr_table, text="Priority", font="Georgia 50", bg="#0e4517")
            lbl_labels_pri.grid(row=0, column=3)

            for b in range(jobs):
                prio_var = StringVar()
                prio_entry.append(prio_var)

                txt_prio = Entry(fr_table, width=20, textvariable=prio_var, bg="#d3cbc0", font="Georgia 15")
                txt_prio.grid(row=b + 1, column=3)

                txt_prio.delete(0, END)

        fr_bt_table = Frame(table, bg="#0e4517")
        fr_bt_table.grid(row=jobs+1, column=0)

        bt_sub = Button(table, text="Submit", bg="#662e07",fg="black", font="Garamond 25", bd=5, command=shoot)
        bt_sub.grid(row=jobs + 2, column=0, sticky="nsew")

        bt_back = Button(table, text="Return",bg='#535c57',fg="#c9c9c4", font="Garamond 25", bd=5, command=black)
        bt_back.grid(row=jobs + 2, column=1, sticky="ns")

        fr_table.update_idletasks()
        prep_table.config(scrollregion=prep_table.bbox("all"), width=prep_width)

        table.mainloop()

    def rtrn():

        if chosen_algo.get() == "Round Robin":
            fr_bt_job_select.grid_forget()
            lbl_job_title.grid_forget()
            lbl_job_size.grid_forget()
            fr_jobs.grid_forget()
            lbl_quantum.destroy()
            cb_jobs.grid_forget()
            txt_quantum.destroy()

            lbl_title.grid(row=0, column=0)
            fr_boxtype.grid(row=0, column=0)

        else:
            fr_bt_job_select.destroy()
            fr_jobs.grid_forget()
            lbl_job_title.destroy()
            lbl_job_size.destroy()
            cb_jobs.destroy()

            lbl_title.grid(row=0, column=0)
            fr_boxtype.grid(row=0, column=0)

    lbl_title.grid_forget()
    fr_boxtype.grid_forget()

    fr_jobs = Frame(main, bg="#0e4517")
    fr_jobs.grid(row=0, column=0, sticky="ew")
    fr_jobs.grid_columnconfigure(0, weight=1)
    fr_jobs.grid_rowconfigure(0, weight=1)

    quantum_var = StringVar()

    fr_bt_job_select = Frame(fr_jobs, bg="#0e4517")
    fr_bt_job_select.grid(row=3, column=1, sticky="ew")

    if chosen_algo.get() == "Round Robin":

        lbl_job_title = Label(fr_jobs, text="|Job Selection", font="Garamond 50", padx=20, pady=10,bg="#0e4517")
        lbl_job_title.grid(row=0, column=0)

        lbl_job_size = Label(fr_jobs, text="Choose how many jobs : ", font="Georgia 25", padx=20, pady=10, bg="#0e4517")
        lbl_job_size.grid(row=1, column=0)

        cb_jobs_val = [x for x in range(2, 7778)]
        cb_jobs = ttk.Combobox(fr_jobs, width=50, values=cb_jobs_val, font="Garamond 15")
        cb_jobs.grid(row=1, column=1)
        cb_jobs.set("Select number of jobs..")

        lbl_quantum = Label(fr_jobs, text="Enter quantum : ", font="Georgia 25", padx=20, pady=10, bg="#0e4517")
        lbl_quantum.grid(row=2, column=0)

        txt_quantum = Entry(fr_jobs, width=20, bg="#d3cbc0", textvariable=quantum_var, font="Georgia 15")
        txt_quantum.grid(row=2, column=1)

        bt_submit = Button(fr_jobs, text="Submit", font="Georgia 25", bd=5, command=cur_table, bg="#662e07")
        bt_submit.grid(row=3, column=0, sticky="ew")

        bt_retrn = Button(fr_jobs, text="Return", font="Georgia 25", bd=5, command=rtrn, bg='#535c57')
        bt_retrn.grid(row=3, column=1, sticky="ew")

    else:

        lbl_job_title = Label(fr_jobs, text="|Job Selection", font="Garamond 50",pady=10,bg="#0e4517")
        lbl_job_title.grid(row=0, column=0)

        lbl_job_size = Label(fr_jobs, text="Choose how many jobs : ", font="Georgia 25", pady=10,padx=20, bg="#0e4517")
        lbl_job_size.grid(row=1, column=0)

        cb_jobs_val = [x for x in range(2, 7778)]
        cb_jobs = ttk.Combobox(fr_jobs, width=50, values=cb_jobs_val, background="#746a5d", font="Garamond 13")
        cb_jobs.grid(row=1, column=0, sticky="e")
        cb_jobs.set("Select number of jobs..")

        bt_submit = Button(fr_jobs, text="Submit", font="Georgia 25", bd=5, command=cur_table, bg="#662e07")
        bt_submit.grid(row=2, column=0, sticky="ew")

        bt_retrn = Button(fr_jobs, text="Return", font="Georgia 25", bd=5, command=rtrn, bg='#535c57')
        bt_retrn.grid(row=2, column=1, sticky="e")

#main Window

fr_boxtype = Frame(main, bg="#0e4517")
fr_boxtype.grid(row=0, column=0, sticky="ew")
fr_boxtype.grid_columnconfigure(0, weight=1)
fr_boxtype.grid_rowconfigure(0, weight=1)

lbl_title = Label(fr_boxtype, text="| Algorithm CPU Scheduling |", font="Garamond 50", padx=20, pady=10, bg="#0e4517")
lbl_title.grid(row=0, column=0)

chosen_algo = StringVar()
cb_algo_val = ["First Come First Serve", "Shortest Job First", "Non Pre-emptive Priority", "Shortest Remaining Job First", "Pre-emptive Priority", "Round Robin"]
cb_algo = ttk.Combobox(fr_boxtype, width=25, values=cb_algo_val, textvariable=chosen_algo, background="#0e471b", foreground="#0e471b", font="Garamond 20")
cb_algo.grid(row=1, column=0)
cb_algo.set("Select an Algorithm..")

bt_algo = Button(fr_boxtype, text="Done", font="Garamond 50", pady=10, padx=20, bd=5, command=algo, bg="#9b8d45")
bt_algo.grid(row=2, column=0, sticky="ns")

main.mainloop()
