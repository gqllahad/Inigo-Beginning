from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk
import random
from tkinter import messagebox

main = Tk()
main.title("Flag guesser baby")
#main.geometry("900x700")

flag_af = Image.open(r"C:\Users\HP_USER\Pictures\Flags\Afghanistan.png")
afgani = flag_af.resize((900, 400), Image.Resampling.LANCZOS)
f_afghanistan = ImageTk.PhotoImage(afgani)

flag_ar = Image.open(r"C:\Users\HP_USER\Pictures\Flags\Armenia.png")
arm = flag_ar.resize((900, 400), Image.Resampling.LANCZOS)
f_armenia = ImageTk.PhotoImage(arm)

flag_az = Image.open(r"C:\Users\HP_USER\Pictures\Flags\azerbaijan.png")
az = flag_az.resize((900, 400), Image.Resampling.LANCZOS)
f_azerbaijan = ImageTk.PhotoImage(az)

flag_bh = Image.open(r"C:\Users\HP_USER\Pictures\Flags\bahrain.png")
bh = flag_bh.resize((900, 400), Image.Resampling.LANCZOS)
f_bahrain = ImageTk.PhotoImage(bh)

flag_bang = Image.open(r"C:\Users\HP_USER\Pictures\Flags\bangladesh.png")
bang = flag_bang.resize((900, 400), Image.Resampling.LANCZOS)
f_bangladesh = ImageTk.PhotoImage(bang)

flag_bu = Image.open(r"C:\Users\HP_USER\Pictures\Flags\bhutan.png")
but = flag_bu.resize((900, 400), Image.Resampling.LANCZOS)
f_bhutan = ImageTk.PhotoImage(but)

flag_br = Image.open(r"C:\Users\HP_USER\Pictures\Flags\brunei.png")
brun = flag_br.resize((900, 400), Image.Resampling.LANCZOS)
f_brunei = ImageTk.PhotoImage(brun)

flag_cam = Image.open(r"C:\Users\HP_USER\Pictures\Flags\cambodia.png")
cam = flag_cam.resize((900, 400), Image.Resampling.LANCZOS)
f_cambodia = ImageTk.PhotoImage(cam)

flag_chi = Image.open(r"C:\Users\HP_USER\Pictures\Flags\china.png")
chin = flag_chi.resize((900, 400), Image.Resampling.LANCZOS)
f_china = ImageTk.PhotoImage(chin)

flag_ge = Image.open(r"C:\Users\HP_USER\Pictures\Flags\georgia.png")
george = flag_ge.resize((900, 400), Image.Resampling.LANCZOS)
f_georgia = ImageTk.PhotoImage(george)

flag_hk = Image.open(r"C:\Users\HP_USER\Pictures\Flags\hongkong.png")
hong = flag_hk.resize((900, 400), Image.Resampling.LANCZOS)
f_hongkong = ImageTk.PhotoImage(hong)

flag_in = Image.open(r"C:\Users\HP_USER\Pictures\Flags\india.png")
ind = flag_in.resize((900, 400), Image.Resampling.LANCZOS)
f_india = ImageTk.PhotoImage(ind)

flag_indo = Image.open(r"C:\Users\HP_USER\Pictures\Flags\indonesia.png")
indo = flag_indo.resize((900, 400), Image.Resampling.LANCZOS)
f_indonesia = ImageTk.PhotoImage(indo)

flag_iran = Image.open(r"C:\Users\HP_USER\Pictures\Flags\iran.png")
iran = flag_iran.resize((900, 400), Image.Resampling.LANCZOS)
f_iran = ImageTk.PhotoImage(iran)

flag_iraq = Image.open(r"C:\Users\HP_USER\Pictures\Flags\iraq.png")
iraq = flag_iraq.resize((900, 400), Image.Resampling.LANCZOS)
f_iraq = ImageTk.PhotoImage(iraq)

flag_is = Image.open(r"C:\Users\HP_USER\Pictures\Flags\israel.png")
isra = flag_is.resize((900, 400), Image.Resampling.LANCZOS)
f_israel = ImageTk.PhotoImage(isra)

flag_japs = Image.open(r"C:\Users\HP_USER\Pictures\Flags\japan.png")
japs = flag_japs.resize((900, 400), Image.Resampling.LANCZOS)
f_japan = ImageTk.PhotoImage(japs)

flag_jor = Image.open(r"C:\Users\HP_USER\Pictures\Flags\jordan.png")
jordan = flag_jor.resize((900, 400), Image.Resampling.LANCZOS)
f_jordan = ImageTk.PhotoImage(jordan)

flag_kaz = Image.open(r"C:\Users\HP_USER\Pictures\Flags\kazakhstan.png")
kaz = flag_kaz.resize((900, 400), Image.Resampling.LANCZOS)
f_kazakhstan = ImageTk.PhotoImage(kaz)

flag_kry = Image.open(r"C:\Users\HP_USER\Pictures\Flags\krygyzstan.png")
kry = flag_kry.resize((900, 400), Image.Resampling.LANCZOS)
f_krygyzstan = ImageTk.PhotoImage(kry)

flag_kw = Image.open(r"C:\Users\HP_USER\Pictures\Flags\kuwait.png")
kw = flag_kw.resize((900, 400), Image.Resampling.LANCZOS)
f_kuwait = ImageTk.PhotoImage(kw)

flag_ls = Image.open(r"C:\Users\HP_USER\Pictures\Flags\laos.png")
ls = flag_ls.resize((900, 400), Image.Resampling.LANCZOS)
f_laos = ImageTk.PhotoImage(ls)

flag_leb = Image.open(r"C:\Users\HP_USER\Pictures\Flags\lebanon.png")
leb = flag_leb.resize((900, 400), Image.Resampling.LANCZOS)
f_lebanon = ImageTk.PhotoImage(leb)

flag_mal = Image.open(r"C:\Users\HP_USER\Pictures\Flags\malaysia.png")
mal = flag_mal.resize((900, 400), Image.Resampling.LANCZOS)
f_malaysia = ImageTk.PhotoImage(mal)

flag_div = Image.open(r"C:\Users\HP_USER\Pictures\Flags\maldives.png")
div = flag_div.resize((900, 400), Image.Resampling.LANCZOS)
f_maldives = ImageTk.PhotoImage(div)

flag_mong = Image.open(r"C:\Users\HP_USER\Pictures\Flags\mongolia.png")
mong = flag_mong.resize((900, 400), Image.Resampling.LANCZOS)
f_mongolia = ImageTk.PhotoImage(mong)

flag_mos = Image.open(r"C:\Users\HP_USER\Pictures\Flags\moscow.png")
mos = flag_mos.resize((900, 400), Image.Resampling.LANCZOS)
f_moscow = ImageTk.PhotoImage(mos)

flag_my = Image.open(r"C:\Users\HP_USER\Pictures\Flags\mynmar.png")
my = flag_my.resize((900, 400), Image.Resampling.LANCZOS)
f_myanmar = ImageTk.PhotoImage(my)

flag_nep = Image.open(r"C:\Users\HP_USER\Pictures\Flags\nepal.png")
nep = flag_nep.resize((900, 400), Image.Resampling.LANCZOS)
f_nepal = ImageTk.PhotoImage(nep)

flag_nk = Image.open(r"C:\Users\HP_USER\Pictures\Flags\north korea.png")
nr = flag_nk.resize((900, 400), Image.Resampling.LANCZOS)
f_northkorea = ImageTk.PhotoImage(nr)

flag_om = Image.open(r"C:\Users\HP_USER\Pictures\Flags\oman.png")
om = flag_om.resize((900, 400), Image.Resampling.LANCZOS)
f_oman = ImageTk.PhotoImage(om)

flag_pak = Image.open(r"C:\Users\HP_USER\Pictures\Flags\pakistan.png")
pak = flag_pak.resize((900, 400), Image.Resampling.LANCZOS)
f_pakistan = ImageTk.PhotoImage(pak)

flag_pal = Image.open(r"C:\Users\HP_USER\Pictures\Flags\palestine.png")
pal = flag_pal.resize((900, 400), Image.Resampling.LANCZOS)
f_palestine = ImageTk.PhotoImage(pal)

flag_ph = Image.open(r"C:\Users\HP_USER\Pictures\Flags\philippines.png")
ph = flag_ph.resize((900, 400), Image.Resampling.LANCZOS)
f_philippines = ImageTk.PhotoImage(ph)

flag_q = Image.open(r"C:\Users\HP_USER\Pictures\Flags\qatar.png")
qatar = flag_q.resize((900, 400), Image.Resampling.LANCZOS)
f_qatar = ImageTk.PhotoImage(qatar)

flag_rus = Image.open(r"C:\Users\HP_USER\Pictures\Flags\russia.png")
russ = flag_rus.resize((900, 400), Image.Resampling.LANCZOS)
f_russia = ImageTk.PhotoImage(russ)

flag_saudi = Image.open(r"C:\Users\HP_USER\Pictures\Flags\saudi arabia.png")
saudi = flag_saudi.resize((900, 400), Image.Resampling.LANCZOS)
f_saudiarabia = ImageTk.PhotoImage(saudi)

flag_sk = Image.open(r"C:\Users\HP_USER\Pictures\Flags\south korea.png")
sk = flag_sk.resize((900, 400), Image.Resampling.LANCZOS)
f_southkorea = ImageTk.PhotoImage(sk)

flag_sing = Image.open(r"C:\Users\HP_USER\Pictures\Flags\singapore.png")
sing = flag_sing.resize((900, 400), Image.Resampling.LANCZOS)
f_singapore = ImageTk.PhotoImage(sing)

flag_sr = Image.open(r"C:\Users\HP_USER\Pictures\Flags\sri lanka.png")
sr = flag_sr.resize((900, 400), Image.Resampling.LANCZOS)
f_srilanka = ImageTk.PhotoImage(sr)

flag_sy = Image.open(r"C:\Users\HP_USER\Pictures\Flags\syria.png")
sy = flag_sy.resize((900, 400), Image.Resampling.LANCZOS)
f_syria = ImageTk.PhotoImage(sy)

flag_tai = Image.open(r"C:\Users\HP_USER\Pictures\Flags\taiwan.png")
tai = flag_tai.resize((900, 400), Image.Resampling.LANCZOS)
f_taiwan = ImageTk.PhotoImage(tai)

flag_taj = Image.open(r"C:\Users\HP_USER\Pictures\Flags\tajikistan.png")
taj = flag_taj.resize((900, 400), Image.Resampling.LANCZOS)
f_tajikistan = ImageTk.PhotoImage(taj)

flag_thai = Image.open(r"C:\Users\HP_USER\Pictures\Flags\thailand.png")
thai = flag_thai.resize((900, 400), Image.Resampling.LANCZOS)
f_thailand = ImageTk.PhotoImage(thai)

flag_tl = Image.open(r"C:\Users\HP_USER\Pictures\Flags\timor leste.png")
tl = flag_tl.resize((900, 400), Image.Resampling.LANCZOS)
f_timorleste = ImageTk.PhotoImage(tl)

flag_turk = Image.open(r"C:\Users\HP_USER\Pictures\Flags\turkey.png")
turk = flag_turk.resize((900, 400), Image.Resampling.LANCZOS)
f_turkey = ImageTk.PhotoImage(turk)

flag_tur = Image.open(r"C:\Users\HP_USER\Pictures\Flags\turkmenistan.png")
tur = flag_tur.resize((900, 400), Image.Resampling.LANCZOS)
f_turkmenistan = ImageTk.PhotoImage(tur)

flag_uae = Image.open(r"C:\Users\HP_USER\Pictures\Flags\united arab emirates.png")
uae = flag_uae.resize((900, 400), Image.Resampling.LANCZOS)
f_unitedarabemirates = ImageTk.PhotoImage(uae)

flag_uz = Image.open(r"C:\Users\HP_USER\Pictures\Flags\uzbekistan.png")
uz = flag_uz.resize((900, 400), Image.Resampling.LANCZOS)
f_uzbekistan = ImageTk.PhotoImage(uz)

flag_viet = Image.open(r"C:\Users\HP_USER\Pictures\Flags\vitenam.png")
viet = flag_viet.resize((900, 400), Image.Resampling.LANCZOS)
f_vietnam = ImageTk.PhotoImage(viet)

flag_ye = Image.open(r"C:\Users\HP_USER\Pictures\Flags\yemen.png")
ye = flag_ye.resize((900, 400), Image.Resampling.LANCZOS)
f_yemen = ImageTk.PhotoImage(ye)


flags = {"asia": [[f_afghanistan, "afghanistan"], [f_armenia, "armenia"], [f_azerbaijan, "azerbaijan"],
                  [f_bahrain, "bahrain"], [f_bangladesh, "bangladesh"], [f_bhutan, "bhutan"], [f_brunei, "brunei"],
                  [f_cambodia, "cambodia"], [f_china, "china"], [f_georgia, "georgia"], [f_hongkong, "hongkong"], [f_india, "india"], [f_indonesia, "indonesia"],
                  [f_iran, "iran"], [f_iraq, "iraq"], [f_israel, "israel"], [f_japan, "japan"], [f_jordan, "jordan"],
                  [f_kazakhstan, "kazakhstan"], [f_krygyzstan, "krygyzstan"], [f_kuwait, "kuwait"], [f_laos, "laos"],
                  [f_lebanon, "lebanon"], [f_malaysia, "malaysia"], [f_maldives, "maldives"], [f_mongolia, "mongolia"],
                  [f_moscow, "moscow"], [f_myanmar, "myanmar"], [f_nepal, "nepal"], [f_northkorea, "north korea"], [f_oman, "oman"],
                  [f_pakistan, "pakistan"], [f_palestine, "palestine"], [f_philippines, "philippines"], [f_qatar, "qatar"],
                  [f_russia, "russia"], [f_saudiarabia, "saudi arabia"], [f_singapore, "singapore"], [f_southkorea, "south korea"],
                  [f_srilanka, "sri lanka"], [f_syria, "syria"], [f_taiwan, "taiwan"], [f_tajikistan, "tajikistan"], [f_thailand, "thailand"],
                  [f_turkey, "turkey"], [f_turkmenistan, "turkmenistan"], [f_timorleste, "timorleste"], [f_uzbekistan, "uzbekistan"], [f_unitedarabemirates, "unitedarabemirates"],
                  [f_vietnam, "vietnam"], [f_yemen, "yemen"]]}


def rand_number():
    random_number = random.randint(0, 50)

    return random_number


def choices_return(lst):
    seen = set()

    for i in range(len(lst)):
        if lst[i] in seen:
            lst[i] = rand_number()

        seen.add(lst[i])

    return lst


def play():

    def guess():
        user_guess = answer.get()

        if user_guess != str(flags["asia"][num_flag][1]):
            messagebox.showerror(title="Error", message="Not cool men!")
            user["life"] -= 1

            if user["life"] <= 0:
                messagebox.showinfo(title="GameOVER",
                                    message=f"Gameover baby!\n Total earned points : {user['points']} ")
                fr_play.destroy()
                fr_flag.destroy()
                fr_main.grid(row=1, column=1, sticky="nsew")
                user["life"] = 3
            else:
                fr_play.destroy()
                fr_flag.destroy()
                play()

        else:
            if user["life"] <= 0:
                messagebox.showinfo(title="GameOVER",
                                    message=f"Gameover baby!\n Total earned points : {user['points']} ")
                fr_play.destroy()
                fr_flag.destroy()
                fr_main.grid(row=1, column=1, sticky="nsew")
                user["life"] = 3

            else:
                user['points'] += 1
                messagebox.showinfo(message="noce")
                fr_play.destroy()
                fr_flag.destroy()
                play()

    fr_main.grid_forget()

    num_flag = rand_number()
    alt_choice = [num_flag, rand_number(), rand_number(), rand_number()]
    answer = StringVar()

    x = 1
    y = 0
    ch = list(range(0, 4))
    random.shuffle(ch)

    print(len(flags["asia"]))

    fr_play = Frame(main)
    fr_play.grid(row=1, column=0, sticky="nsew")

    fr_flag = Frame(main)
    fr_flag.grid(row=0, column=0, sticky="nsew")

    lbl_flag = Label(fr_flag, image=flags["asia"][num_flag][0], bd=5, highlightthickness=0)
    lbl_flag.grid(row=0, column=1, sticky="nsew", pady=50)

    for choice in range(len(alt_choice)):

        new_choice = choices_return(alt_choice)

        if y == 2:
            y = 0
            x += 1

        rd_choices = Radiobutton(fr_play, text=flags["asia"][new_choice[ch[choice]]][1], font="Impact 25",
                                 value=flags["asia"][new_choice[ch[choice]]][1], padx=20, indicatoron=0, bd=10, width=25, variable=answer,
                                 command=guess
                                 )

        rd_choices.grid(row=x, column=y, pady=5, sticky="nsew")
        y += 1

    print(answer.get())


def about():
    pass



def ex():
    pass


user = {"points" : 0, "life": 3}

fr_main = Frame(main)
fr_main.grid(row=1, column=1, sticky="nsew")

lbl_title = Label(fr_main, text="| Flag Guesser |", font="Garamond 50", padx=20, pady=10)
lbl_title.grid(row=0, column=1, sticky="ew", pady=25)

bt_play = Button(fr_main, text="Play", font="georgia 25", bd=5, relief=RAISED, command=play)
bt_play.grid(row=1, column=1, sticky="nsew")

bt_rules = Button(fr_main, text="About", font="Georgia 25", bd=5, relief=RAISED)
bt_rules.grid(row=2, column=1, sticky="nsew")

bt_exit = Button(fr_main, text="Exit", font="georgia 25", bd=5, relief=RAISED)
bt_exit.grid(row=3, column=1, sticky="nsew")

main.mainloop()
