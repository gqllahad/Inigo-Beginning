from tkinter import *
#rectangle loob (left, top, right, bottom)
#line loob (start x(row), start y(column), end x (row), end y(column)

def rr(listo, quantum):
    t = 0
    gantt = []
    complete = {}
    process_queue = listo.copy()
    original_burst = {rnd[3]: rnd[1] for rnd in listo}

    # Sort by arrival time
    process_queue.sort()

    while len(process_queue) > 0:
        # Fetch the first process in the queue
        process = process_queue.pop(0)
        arrival, burst, prio, pid = process

        # If the process hasn't arrived yet, idle
        if arrival > t:
            gantt.append("idle")
            t += 1
            process_queue.insert(0, process)  # Re-insert the process to wait
            continue

        # Append to Gantt chart
        gantt.extend([pid] * min(quantum, burst))

        # Simulate process execution
        execution_time = min(quantum, burst)
        burst -= execution_time
        t += execution_time

        if pid not in complete:
            complete[pid] = [arrival, original_burst[pid], prio, None, None, None]

        if burst == 0:  # Process completes
            ct = t
            tt = ct - arrival
            wt = tt - original_burst[pid]
            complete[pid][3] = ct
            complete[pid][4] = tt
            complete[pid][5] = wt
        else:
            # Re-queue the process with remaining burst time
            process_queue.append([arrival, burst, prio, pid])

    return gantt, complete


def srjf(listo):

    for x in range(len(listo)):
        sub = listo[x][1]
        listo[x][1] = listo[x][0]
        listo[x][0] = sub

    original_burst = {srj[3]: srj[0] for srj in listo}

    t = 0
    gantt = []
    complete = {}
    process_map = {}

    while len(listo) != 0:
        available = []

        for sj in listo:
            arr = sj[1]
            if arr <= t:
                available.append(sj)

        if len(available) == 0:
            gantt.append("idle")
            t += 1
            continue

        else:
            available.sort()
            process = available[0]
            listo.remove(process)

            if process[3] not in process_map:
                process_map[process[3]] = [t, None]

            gantt.append(process[3])
            process[0] -= 1
            t += 1

            if process[0] <= 0:
                jid = process[3]
                arrive = process[1]
                prio = process[2]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                process_map[jid][1] = t
                complete[jid] = [arrive, original_burst[jid],prio,ct, tt, wt]
                continue

            else:
                listo.append(process)


    return gantt, complete, t



def rrs(listo, rr):

    t = 0
    gantt = []
    complete = {}
    occuranse = []

    original_burst = {rnd[3]: rnd[1] for rnd in listo}

    listo.sort()

    while len(listo) != 0:
        available = []

        for cpu in listo:
            at = cpu[0]
            if at <= t:
                available.append(cpu)

        if len(available) == 0:
            gantt.append('idle')
            t += 1
            continue

        else:
            process = available[0]
            gantt.append(process[3])
            occuranse.append(t)
            listo.remove(process)

            rbt = process[1]

            if rbt <= rr:
                t += rbt
                jid = process[3]
                arrive = process[0]
                prio = process[2]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                complete[jid] = [arrive, original_burst[jid],prio, ct, tt, wt]
                continue

            else:
                t += rr
                process[1] -= rr
                listo.append(process)

    return gantt, complete, t, occuranse



def rrsy(listo, rr):
    t = 0
    gantt = []
    complete = {}
    occuranse = []

    # Storing original burst times to calculate turnaround and waiting time later
    original_burst = {rnd[3]: rnd[1] for rnd in listo}

    # Sort the processes by arrival time (if not already sorted)
    listo.sort()

    # Use a queue to process jobs that are ready to execute
    ready_queue = []

    while len(listo) > 0 or len(ready_queue) > 0:
        # Move processes from listo to ready_queue if they have arrived
        while len(listo) > 0 and listo[0][0] <= t:
            ready_queue.append(listo.pop(0))

        # If no processes are ready to run, we add 'idle' time and continue
        if len(ready_queue) == 0:
            gantt.append('idle')
            t += 1
            continue

        # Process the next job in the ready queue
        process = ready_queue.pop(0)
        gantt.append(process[3])  # Add the job to the Gantt chart
        occuranse.append(t)  # Record the current time in the occurrences list
        rbt = process[1]  # Remaining burst time of the process

        # If the process can complete within this round-robin quantum
        if rbt <= rr:
            t += rbt  # Process the job
            jid = process[3]
            arrive = process[0]
            prio = process[2]
            ct = t  # Completion time
            tt = ct - arrive  # Turnaround time
            wt = tt - original_burst[jid]  # Waiting time
            complete[jid] = [arrive, original_burst[jid], prio, ct, tt, wt]
        else:
            # If the process does not complete, reduce the burst time and re-queue it
            t += rr
            process[1] -= rr
            ready_queue.append(process)  # Re-add the process to the end of the ready queue

    return gantt, complete, t, occuranse


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
        available = []

        for cpu in listo:
            at = cpu[1]
            if at <= t:
                available.append(cpu)

        if len(available) == 0:
            gantt.append("idle")
            t += 1

        else:
            available.sort()

            process = available[0]

            gantt.append(process[3])
            occurance.append(t)
            arrive = process[1]
            burst = process[0]
            prio = process[2]
            t += process[0]

            listo.remove(process)

            jid = process[3]
            ct = t
            tt = ct - arrive
            wt = tt - burst
            completed[jid] = [arrive,burst,prio,ct, tt, wt]

    return gantt, completed, t, occurance



def fcfs(listo):
    t = 0
    ganntt = []
    completed = {}
    occurances = []
    listo.sort()

    while len(listo) != 0:
        pwede_na = []

        for cpu in listo:
            at = cpu[0]

            if at <= t:
                ganntt.append(cpu[3])
                pwede_na.append(cpu)

        if len(pwede_na) == 0:
            t += 1
            pwede_na.append('idle')

        else:
            pwede_na.sort()

            processing = pwede_na[0]
            ganntt.append(processing[3])
            occurances.append(t)
            arrive = processing[0]
            burst = processing[1]
            prio = processing[2]

            t += processing[1]

            listo.remove(processing)

            jid = processing[3]
            ct = t
            tt = ct - int(arrive)
            wt = tt - int(burst)
            completed[jid] = [arrive,burst,prio,ct, tt, wt]
    print(occurances)

    return ganntt, completed, t, occurances

#npp_timeline fcfs
def time(gantt, complete, t, occ):
    canva = Canvas(main, width=500, height=500)
    canva.grid(row=1, column=2)

    canva.create_line(50 * 20, 50, 0, 50, fill="Black", width=3)
    for x in range(t + 1):
        canva.create_line(x * 20, x - 50, x * 20, 50, fill="red", width=1)

        canva.create_text(x * 20 + 5, 65, text=f"{x}")

    arrival_pos = {}
    completion_pos = {}

    for job, details in complete.items():
        arrival_time = details[0]
        completion_time = details[3]

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

        x_arrival = arrival_time * 20
        canva.create_text(x_arrival, 80 + vertical_space, text=f"J{job}", fill="blue")
        canva.create_text(completion_time * 20, 100 + vertical_space_cmp, text=f"J{job}", fill="red")


    #gantt

    canba = Canvas(main, width=500, height=200)
    canba.grid(row=1, column=2)

    # for are in range(len(gantt)):
    #     jobs = gantt[are]
    #     start_pos = are * 25

    arrive_time = {}
    end_time = {}

    for idx, (job, details) in enumerate(complete.items()):
        arrive = details[0]
        end = details[3]

        if arrive not in arrive_time:
            arrive_time[arrive] = 0
        else:
            arrive_time[arrive] += 1

        if end not in end_time:
            end_time[end] = 0
        else:
            end_time[end] += 1

        x_arrive = arrive * 20
        x_end = end * 20
        canba.create_text(x_arrive + 10, 30, text=f"{occ[0]}", font="Georgia 7")
        canba.create_text(x_end + 10, 55, text=f"{occ[-1]}", font="Georgia 7")
        canba.create_rectangle(50, 45, 25 * idx, 10)




    # last_job_index = len(gantt)
    #
    # canba.create_rectangle(25 * last_job_index - 50, 45, 25 * last_job_index, 10)
    # canba.create_rectangle(25 * last_job_index - 25, 45, 25 * last_job_index, 10)
    # canba.create_text(25 * last_job_index - 10, 55, text=f"{t}", font="Georgia 7")

#PP ALGO
def timeline(gantt, complete, t):

    canva = Canvas(main, width=10000, height=500)
    canva.grid(row=1, column=0)

    canva.create_line(50 * 20, 50, 0, 50, fill="Black", width=3)
    for x in range(len(gantt)+1):
        canva.create_line(x * 20, x - 50, x * 20, 50, fill="red", width=1)

        canva.create_text(x * 20 + 5, 65, text=f"{x}")

    arrival_pos = {}
    completion_pos = {}

    for job, details in complete.items():
        arrival_time = details[0]
        completion_time = details[3]

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

        x_arrival = arrival_time * 20
        canva.create_text(x_arrival, 80 + vertical_space, text=f"J{job}", fill="blue")
        canva.create_text(completion_time * 20, 100 + vertical_space_cmp, text=f"J{job}", fill="red")

     # Gantt Chart

    arrive_pos = {}

    canba = Canvas(main, width=10000, height=200)
    canba.grid(row=1, column=0)

    for are, jobs in enumerate(gantt):
        start_pos = are * 25

        if jobs not in arrive_pos:
            arrive_pos[jobs] = 0
        else:
            arrive_pos[jobs] += 1

        canba.create_text(are * 25 + 10, 30, text=f"{jobs}", font="Georgia 7")
        canba.create_rectangle(50, 45, 25 * are, 10)
        canba.create_text(start_pos + 10, 55, text=f"{are}", font="Georgia 7")

    last_job_index = len(gantt) + 1

    canba.create_text(last_job_index * 25 - 10, 30, text=f"{gantt[-1]}", font="Georgia 7")
    canba.create_rectangle(25 * last_job_index - 50, 45, 25 * last_job_index, 10)
    canba.create_rectangle(25 * last_job_index - 25, 45, 25 * last_job_index, 10)
    canba.create_text(25 * last_job_index - 10, 55, text=f"{t}", font="Georgia 7")


def round_timeline(gantt, complete, endtime, occ):

    canba = Canvas(main, width=10000, height=200)
    canba.grid(row=1, column=0)

    for are in range(len(gantt)):
        jobs = gantt[are]
        start_pos = are * 25

        canba.create_text(start_pos + 10, 30, text=f"{jobs}", font="Georgia 7")
        canba.create_rectangle(50, 45,  25 * are, 10)

        if are < len(occ):
            canba.create_text(are * 25 + 10, 55, text=f"{occ[are]}", font="Georgia 7")

    last_job_index = len(gantt)

    #canba.create_text(last_job_index * 25 - 10, 30, text=f"{gantt[-1]}", font="Georgia 7")
    #canba.create_text(last_job_index * 25 - 35, 30, text=f"{gantt[-1]}", font="Georgia 7")
    canba.create_rectangle(25 * last_job_index - 50, 45, 25 * last_job_index, 10)
    #canba.create_rectangle(25 * last_job_index - 25, 45, 25 * last_job_index, 10)
    canba.create_text(25 * last_job_index - 10, 55, text=f"{endtime}", font="Georgia 7")
    print(complete)
    print(occ)


main = Tk()

occurance = [1, 4, 6, 7, 9, 24, 49, 25, 50]

hoho = [[1,12,0, "A"], [2, 2, 2, "B"], [9, 8, 0, "C"], [12, 10, 3, "D"], [0, 6, 3, "E"]]
hehe = [[1,4,1, "A"], [2, 5, 2, "B"], [3, 6, 3, "C"]]

#Timeline

finished, wews, t, occur = fcfs(hehe)

print(finished)
print(wews)

time(finished, wews, t, occur)
main.mainloop()
