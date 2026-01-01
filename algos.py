#fifo (old)
# while len(listo) != 0:
    #     if listo[0][0] > t:
    #         t += 1
    #         ganntt.append("Idle")
    #         continue
    #     else:
    #         process = listo.pop(0)
    #         ganntt.append(process[3])
    #         t += process[1]
    #         jid = process[3]
    #         ct = t
    #         tt = ct - process[0]
    #         wt = tt - process[1]
    #         completed[jid] = [ct, tt, wt]


def fcfs(listo):
    t = 0
    ganntt = []
    completed = {}
    listo.sort()

    while len(listo) != 0:
        pwede_na = []

        for cpu in listo:
            at = cpu[0]

            if at <= t:
                pwede_na.append(cpu)

        if len(pwede_na) == 0:
            t += 1
            pwede_na.append('idle')

        else:
            pwede_na.sort()

            processing = pwede_na[0]
            ganntt.append(processing[3])
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

    print(ganntt)
    print(completed)
    print(t)


def sjf(listo):
    for x in range(len(listo)):
        sub = listo[x][0]
        listo[x][0] = listo[x][1]
        listo[x][1] = sub

    t = 0
    gantt = []
    completed = {}
    listo.sort()

    while len(listo) != 0:
        available = []

        for cpu in listo:
            at = cpu[1]
            if at <= t:
                available.append(cpu)

        if len(available) == 0:
            t += 1
            gantt.append("idle")

        else:
            available.sort()

            process = available[0]

            gantt.append(process[3])
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

    print(gantt)
    print(completed)
    print(t)


def npp(listo):
    for x in range(len(listo)):
        sub = listo[x][2]
        listo[x][2] = listo[x][0]
        listo[x][0] = sub

    t = 0
    gantt = []
    complete = {}

    while len(listo) != 0:
        available = []

        for cpu in listo:
            arr = cpu[2]

            if arr <= t:
                available.append(cpu)

        if len(available) == 0:
            gantt.append("idle")
            t += 1

        else:
            available.sort()

            process = available[0]
            gantt.append(process[3])
            arrive = process[2]
            burst = process[1]
            prio = process[0]
            t += process[1]

            listo.remove(process)

            jid = process[3]
            ct = t
            tt = ct - process[2]
            wt = tt - process[1]
            complete[jid] = [arrive,burst,prio,ct, tt, wt]

    print(gantt)
    print(complete)


def pp(listo):

    for x in range(len(listo)):
        sub = listo[x][2]
        listo[x][2] = listo[x][0]
        listo[x][0] = sub

    original_burst = {ps[3] : ps[1] for ps in listo}

    t = 0
    gantt = []
    complete = {}

    while len(listo) != 0:

        available = []

        for cpu in listo:
            arr = cpu[2]
            if arr <= t:
                available.append(cpu)

        if len(available) == 0:
            gantt.append("idle")
            t += 1
            continue

        else:
            available.sort()
            process = available[0]
            gantt.append(process[3])
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

    print(gantt)
    print(complete)
    print(t)


def srjf(listo):
    for x in range(len(listo)):
        sub = listo[x][1]
        listo[x][1] = listo[x][0]
        listo[x][0] = sub

    original_burst = {srj[3]: srj[0] for srj in listo}

    t = 0
    gantt = []
    complete = {}

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
            gantt.append(process[3])
            t += 1
            listo.remove(process)

            process[0] -= 1

            if process[0] == 0:
                jid = process[3]
                arrive = process[1]
                prio = process[2]
                ct = t
                tt = ct - arrive
                wt = tt - original_burst[jid]
                complete[jid] = [arrive, original_burst[jid], prio, ct, tt, wt]
                continue

            else:
                listo.append(process)

    print(t)
    print(gantt)
    print(complete)


def rrs(listo, rr):

    t = 0
    gantt = []
    complete = {}

    original_burst = {rnd[3] : rnd[1] for rnd in listo}

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
                complete[jid] = [arrive,original_burst[jid],prio, ct, tt, wt]
                continue

            else:
                t += rr
                process[1] -= rr
                listo.append(process)

    print(gantt)
    print(complete)

    

def rr(listo, quantum):
    t = 0
    gantt = []
    complete = {}
    process_queue = listo.copy()
    original_burst = {rnd[3]: rnd[1] for rnd in listo}

    # Sort by arrival time
    process_queue.sort()

    while len(process_queue) != 0:
        # Fetch the first process in the queue
        process = process_queue.pop(0)
        arrival, burst, prio, jid = process

        # If the process hasn't arrived yet, idle
        if arrival > t:
            gantt.append("idle")
            t += 1
            process_queue.insert(0, process)  # Re-insert the process to wait
            continue

        # Append to Gantt chart
        gantt.append([jid])

        # Simulate process execution
        execution_time = min(quantum, burst)
        burst -= execution_time
        t += execution_time

        if jid not in complete:
            complete[jid] = [arrival, original_burst[jid], prio, None, None, None]

        if burst == 0:  # Process completes
            ct = t
            tt = ct - arrival
            wt = tt - original_burst[jid]
            complete[jid][3] = ct
            complete[jid][4] = tt
            complete[jid][5] = wt
        else:
            # Re-queue the process with remaining burst time
            process_queue.append([arrival, burst, prio, jid])
    print(gantt)
    print(complete)


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
    print(gantt)
    print(complete)


processlist = [[5, 6, 4, "JA"],
               [3, 19, 1, "JB"],
               [12, 21, 0, "JC"],
               [7, 17, 2, "JD"],
               [9, 12, 3, "JE"]]

hoho = [[1,12,0, "A"], [2, 2, 2, "B"], [9, 8, 0, "C"], [12, 10, 3, "D"], [0, 6, 3, "E"]]

#fcfs(hoho)
#sjf(hoho)
npp(hoho)
#pp(hoho)
#srjf(hoho)
#rr(hoho, 3)
#rrs(hoho, 3)
#rrsy(hoho, 3)