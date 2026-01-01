from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from datetime import datetime, timedelta
from PIL import Image, ImageTk, ImageDraw
import MySQLdb

#NOte!! Sari_store Main!! is Tk,  toplevel atm pag nag error balik Tk still in progress sa errors!

# accounts
main_database = {}
admin_accounts = {}
user_accounts = {}

main_connection = MySQLdb.connect(host="localhost", user="root", password="", db="sari_accounts")

#Database accounts
db_user = {}

#Table orders!
sql_food_table_create = f"CREATE TABLE IF NOT EXISTS food (food_id int AUTO_INCREMENT PRIMARY KEY, food_name varchar(255) UNIQUE KEY, food_price decimal(10,2), category varchar (255)) AUTO_INCREMENT = 1000;"
sql_nonfood_table_create = f"CREATE TABLE IF NOT EXISTS nonfood (nonfood_id int AUTO_INCREMENT PRIMARY KEY, nonfood_name varchar(255) UNIQUE KEY, nonfood_price decimal(10,2), category varchar (255)) AUTO_INCREMENT = 2000;"
sql_etc_table_create = f"CREATE TABLE IF NOT EXISTS etc (etc_id int AUTO_INCREMENT PRIMARY KEY, etc_name varchar(255) UNIQUE KEY, etc_price decimal(10,2), category varchar (255)) AUTO_INCREMENT = 3000;"

sql_food_insert = f"INSERT IGNORE INTO food (food_name, food_price, category) values(\"Gardenia\", 30.00, \"Pantry\"), (\"CocoLumber\", 60.00, \"Pantry\"), (\"ChocolateBread\", 45.00, \"Pantry\"), (\"GarlicBread\", 75.00, \"Pantry\"), (\"PandecocoExtreme\",89.00, \"Pantry\"), (\"BavarianTasty\", 90.00, \"Pantry\"), (\"Coke\", 15.00, \"Beverage\"), (\"Sprite\", 15.00, \"Beverage\"), (\"Pepsi\", 15.00, \"Beverage\"), (\"PocariSweat\", 15.00, \"Beverage\"), (\"RootBeer\", 50.00, \"Beverage\"), (\"JackDaniels\", 200.00, \"Beverage\"), (\"Emperador\", 150.00, \"Beverage\"), (\"Nestea\", 5.00, \"Beverage\");"
sql_nonfood_insert = f"INSERT IGNORE INTO nonfood (nonfood_name, nonfood_price, category) values(\"Wings\", 29.00, \"Laundry\"), (\"Pride\", 100.00, \"Laundry\"), (\"SurfFabcon\", 20.00, \"Laundry\"), (\"Ariel\", 49.00, \"Laundry\"), (\"Uppy\", 59.00, \"Laundry\"), (\"Lunox\", 29.00, \"Laundry\"), (\"Bathwash\", 69.00, \"Laundry\"), (\"Mr.Muscles\", 120.00, \"Cleaning\"), (\"Zonrox\", 99.00, \"Cleaning\"), (\"SulfuricAcid\", 200.00, \"Cleaning\"), (\"HydrogenMonoxide\", 250.00, \"Cleaning\"), (\"Brush\", 45.00, \"Cleaning\"), (\"ToiletCleaners\", 90.00, \"Cleaning\"), (\"Molotov\", 500.00, \"Cleaning\");"
sql_etc_insert = f"INSERT IGNORE INTO etc (etc_name, etc_price, category) values(\"BallPoint\", 2.00, \"School\"), (\"NoteBook\", 3.00, \"School\"), (\"PadPaper\", 2.00, \"School\"), (\"Marker\", 4.00, \"School\"), (\"SprayPaint\", 5.00, \"School\");"

# Log-out
def reopen(master):
    master.deiconify()
    master.state("zoomed")
    txt_username.delete(0, END)
    txt_password.delete(0, END)

# Sari store
def sari_store(**kwargs):
    root = Toplevel() #Tk to dati!
    root.title("| 2pacShakur SariShop")
    root.config(bg="#47761E")
    root.attributes("-fullscreen", True)

    username_main = StringVar()

    username_main.set(txt_username.get())

    sari_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pacshakur logo.png")
    twosari_pac = sari_pac.resize((500, 100), Image.Resampling.LANCZOS)
    background_saripac = ImageTk.PhotoImage(twosari_pac)

    icon_lnd = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\laundrysupp.jpg")
    icon_lnd_pac = icon_lnd.resize((75, 70), Image.Resampling.LANCZOS)
    laundry_icon = ImageTk.PhotoImage(icon_lnd_pac)

    icon_pnt = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pantrysupp.jpg")
    icon_pnt_pac = icon_pnt.resize((75, 70), Image.Resampling.LANCZOS)
    pantry_icon = ImageTk.PhotoImage(icon_pnt_pac)

    icon_bev = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\bevsupp.jpg")
    icon_bev_pac = icon_bev.resize((120, 100), Image.Resampling.LANCZOS)
    beverage_icon = ImageTk.PhotoImage(icon_bev_pac)

    icon_cl = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\cleaningsupp.jpg")
    icon_cl_pac = icon_cl.resize((120, 100), Image.Resampling.LANCZOS)
    cl_icon = ImageTk.PhotoImage(icon_cl_pac)

    icon_sc = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\schoolsupp.jpg")
    icon_sc_pac = icon_sc.resize((150, 100), Image.Resampling.LANCZOS)
    school_icon = ImageTk.PhotoImage(icon_sc_pac)

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    def before_reopen():
        root.withdraw()

        reopen(main)

    # Admin acc system
    def administrator_account():
        def add_item(location):
            def done():
                item_add = txt_add_item.get()
                cost = txt_add_item_cost.get()

                try:
                    cost_ft = float(cost)

                except:
                    messagebox.showerror(title="Error!", message="Please be sure to put an integer!")
                    txt_add_item_cost.delete(0, END)
                    return

                cost_length = len(str(cost_ft))
                item_to_add = f"{item_add}          ${cost}.00"
                item_to_dict = f"\n{item_add}"

                sql_add_item_cursor = main_connection.cursor()

                if location == "":
                    messagebox.showerror(title="Error", message="Please try again! make sure you select a category first!")
                    return

                if len(item_add) > 10 or item_add == "":
                    messagebox.showerror(title="Error!", message="Please fill in the blank / Make sure you only write 10 characters!")
                    return

                if not cost.isdigit() and cost_length > 4:
                    messagebox.showerror(title="Error", message="Please try again, make sure to write only 3 digit numbers / It's blank fill in pls!")
                    return

                if location == "Laundry(Section)":
                    sql_add_item = f"INSERT INTO nonfood (nonfood_name, nonfood_price, category) values(%s, %s, %s)"
                    sql_add_value = (item_add, cost_ft, "Laundry")

                    lt_laundry_values.append(item_to_add)
                    dict_all_orders[item_to_dict] = cost_ft
                    sql_add_item_cursor.execute(sql_add_item, sql_add_value)
                    main_connection.commit()

                if location == "Pantry(Section)":
                    sql_add_item = f"INSERT INTO food (food_name, food_price, category) values(%s, %s, %s)"
                    sql_add_value = (item_add, cost_ft, "Pantry")

                    lt_pantry_values.append(item_to_add)
                    dict_all_orders[item_to_dict] = cost_ft
                    sql_add_item_cursor.execute(sql_add_item, sql_add_value)
                    main_connection.commit()

                if location == "Beverages(Section)":
                    sql_add_item = f"INSERT INTO food (food_name, food_price, category) values(%s, %s, %s)"
                    sql_add_value = (item_add, cost_ft, "Beverage")

                    lt_beverages_values.append(item_to_add)
                    dict_all_orders[item_to_dict] = cost_ft
                    sql_add_item_cursor.execute(sql_add_item, sql_add_value)
                    main_connection.commit()

                if location == "Cleaning(Section)":
                    sql_add_item = f"INSERT INTO nonfood (nonfood_name, nonfood_price, category) values(%s, %s, %s)"
                    sql_add_value = (item_add, cost_ft, "Cleaning")

                    lt_cleaning_values.append(item_to_add)
                    dict_all_orders[item_to_dict] = cost_ft
                    sql_add_item_cursor.execute(sql_add_item, sql_add_value)
                    main_connection.commit()

                if location == "SchoolSupplies(Section)":
                    sql_add_item = f"INSERT INTO etc (etc_name, etc_price, category) values(%s, %s, %s)"
                    sql_add_value = (item_add, cost_ft, "School")

                    lt_school_values.append(item_to_add)
                    dict_all_orders[item_to_dict] = cost_ft
                    sql_add_item_cursor.execute(sql_add_item, sql_add_value)
                    main_connection.commit()

                fr_where.destroy()
                txt_add_item_cost.destroy()
                txt_add_item.destroy()
                bt_where.destroy()

            fr_where = Frame(root, bg="#47761E")
            fr_where.grid(row=6, column=1)

            lbl_add_item = Label(fr_where, bg="#47761E", fg="white", text="Name of the Product : ", font="Georgia 10", padx=20, pady=10)
            lbl_add_item.grid(row=6, column=0)

            txt_add_item = Entry(fr_where, font="Georgia 15", bg="#F8F9FA")
            txt_add_item.grid(row=6, column=1)

            lbl_add_item_cost = Label(fr_where, bg="#47761E", fg="white", font="Georgia 10", text="Cost of the Product (3 digits max) ($) : ")
            lbl_add_item_cost.grid(row=7, column=0)

            txt_add_item_cost = Entry(fr_where, font="Georgia 15", width=7, bg="#F8F9FA")
            txt_add_item_cost.grid(row=7, column=1)

            bt_where = Button(fr_where, text="Add", fg="White", activeforeground="White", bg="#28A745", activebackground="#28A745", bd=5, relief=RAISED, padx=20, pady=10, command=done)
            bt_where.grid(row=6, column=3)

        def edit_item():
            def done():
                to_edit_item = txt_edit_item.get()
                to_edit_cost = txt_edit_cost.get()
                edited_item = f"{to_edit_item}          ${to_edit_cost}.00"

                try:
                    edit_cost_ft = float(to_edit_cost)
                except:
                    messagebox.showerror(title="Error!", message="Please be sure to put an integer!")
                    txt_edit_cost.delete(0, END)
                    return

                edit_cost_length = len(str(edit_cost_ft))
                sql_edit_cursor = main_connection.cursor()

                if len(to_edit_item) > 10 or to_edit_item == "":
                    messagebox.showerror(title="Error!", message="Please fill in the blank / Make sure you only write 10 characters!")
                    return

                if not to_edit_cost.isdigit() or edit_cost_length > 4:
                    messagebox.showerror(title="Error", message="Please try again, make sure to write only 3 digit numbers / It's blank fill in pls!")
                    return

                if lt_laundry.curselection():
                    selected_item = lt_laundry.curselection()
                    selected_index = selected_item[0]
                    selected_product_index = lt_laundry.get(selected_index)
                    selected_product = selected_product_index.split()[0]
                    sql_edit_name_query = f"UPDATE nonfood SET nonfood_name = %s WHERE nonfood_name = %s"
                    sql_edit_price_query = f"UPDATE nonfood SET nonfood_price = %s WHERE nonfood_name = %s"

                    sql_edit_name_value = (to_edit_item, selected_product)
                    sql_edit_price_value = (edit_cost_ft, selected_product)

                    for item_select in lt_laundry.curselection():
                        lt_laundry.delete(item_select)
                        lt_laundry.insert(item_select, edited_item)
                        lt_laundry_values[selected_index] = edited_item
                        dict_all_orders[selected_index] = edit_cost_ft

                    sql_edit_cursor.execute(sql_edit_name_query, sql_edit_name_value)
                    sql_edit_cursor.execute(sql_edit_price_query, sql_edit_price_value)

                    main_connection.commit()

                    txt_edit_item.delete(0, END)
                    txt_edit_cost.delete(0, END)

                elif lt_pantry.curselection():
                    selected_item = lt_pantry.curselection()
                    selected_index = selected_item[0]
                    selected_product_index = lt_laundry.get(selected_index)
                    selected_product = selected_product_index.split()[0]

                    sql_edit_name_query = f"UPDATE food SET food_name = %s WHERE food_name = %s"
                    sql_edit_price_query = f"UPDATE food SET food_price = %s WHERE food_name = %s"

                    sql_edit_name_value = (edited_item, selected_product)
                    sql_edit_price_value = (edit_cost_ft, selected_product)

                    for item_select in lt_pantry.curselection():
                        lt_pantry.delete(item_select)
                        lt_pantry.insert(item_select, edited_item)
                        lt_pantry_values[selected_index] = edited_item
                        dict_all_orders[selected_index] = edit_cost_ft

                    sql_edit_cursor.execute(sql_edit_name_query, sql_edit_name_value)
                    sql_edit_cursor.execute(sql_edit_price_query, sql_edit_price_value)

                    main_connection.commit()

                    txt_edit_item.delete(0, END)
                    txt_edit_cost.delete(0, END)

                elif lt_beverages.curselection():
                    selected_item = lt_beverages.curselection()
                    selected_index = selected_item[0]
                    selected_product_index = lt_laundry.get(selected_index)
                    selected_product = selected_product_index.split()[0]

                    sql_edit_name_query = f"UPDATE food SET food_name = %s WHERE food_name = %s"
                    sql_edit_price_query = f"UPDATE food SET food_price = %s WHERE food_name = %s"

                    sql_edit_name_value = (edited_item, selected_product)
                    sql_edit_price_value = (edit_cost_ft, selected_product)

                    for item_select in lt_beverages.curselection():
                        lt_beverages.delete(item_select)
                        lt_beverages.insert(item_select, edited_item)
                        lt_beverages_values[selected_index] = edited_item
                        dict_all_orders[selected_index] = edit_cost_ft

                    sql_edit_cursor.execute(sql_edit_name_query, sql_edit_name_value)
                    sql_edit_cursor.execute(sql_edit_price_query, sql_edit_price_value)

                    main_connection.commit()

                    txt_edit_item.delete(0, END)
                    txt_edit_cost.delete(0, END)

                elif lt_cleaning.curselection():
                    selected_item = lt_cleaning.curselection()
                    selected_index = selected_item[0]
                    selected_product_index = lt_laundry.get(selected_index)
                    selected_product = selected_product_index.split()[0]

                    sql_edit_name_query = f"UPDATE nonfood SET nonfood_name = %s WHERE nonfood_name = %s"
                    sql_edit_price_query = f"UPDATE nonfood SET nonfood_price = %s WHERE nonfood_name = %s"

                    sql_edit_name_value = (edited_item, selected_product)
                    sql_edit_price_value = (edit_cost_ft, selected_product)

                    for item_select in lt_cleaning.curselection():
                        lt_cleaning.delete(item_select)
                        lt_cleaning.insert(item_select, edited_item)
                        lt_cleaning_values[selected_index] = edited_item
                        dict_all_orders[selected_index] = edit_cost_ft

                    sql_edit_cursor.execute(sql_edit_name_query, sql_edit_name_value)
                    sql_edit_cursor.execute(sql_edit_price_query, sql_edit_price_value)

                    main_connection.commit()

                    txt_edit_item.delete(0, END)
                    txt_edit_cost.delete(0, END)

                elif lt_school.curselection():
                    selected_item = lt_school.curselection()
                    selected_index = selected_item[0]
                    selected_product_index = lt_laundry.get(selected_index)
                    selected_product = selected_product_index.split()[0]

                    sql_edit_name_query = f"UPDATE etc SET etc_name = %s WHERE etc_name = %s"
                    sql_edit_price_query = f"UPDATE etc SET etc_price = %s WHERE etc_name = %s"

                    sql_edit_name_value = (edited_item, selected_product)
                    sql_edit_price_value = (edit_cost_ft, selected_product)

                    for item_select in lt_school.curselection():
                        lt_school.delete(item_select)
                        lt_school.insert(item_select, edited_item)
                        lt_school_values[selected_index] = edited_item
                        dict_all_orders[selected_index] = edit_cost_ft

                    sql_edit_cursor.execute(sql_edit_name_query, sql_edit_name_value)
                    sql_edit_cursor.execute(sql_edit_price_query, sql_edit_price_value)

                    main_connection.commit()

                    txt_edit_item.delete(0, END)
                    txt_edit_cost.delete(0, END)
                else:
                    messagebox.showerror(title="Error!", message="Please choose an item to edit to!!")
                    return

                lbl_edit_item.destroy()
                lbl_edit_cost.destroy()
                txt_edit_item.destroy()
                txt_edit_cost.destroy()
                bt_edit.destroy()

            fr_edit_item = Frame(root, bg="#47761E")
            fr_edit_item.grid(row=6, column=1)

            lbl_edit_item = Label(fr_edit_item, bg="#47761E",fg="white", font="Georgia 10", text="Name of product (Edit) : ")
            lbl_edit_item.grid(row=6, column=0)

            txt_edit_item = Entry(fr_edit_item, font="Georgia 15", bg="#F8F9FA")
            txt_edit_item.grid(row=6, column=1)

            lbl_edit_cost = Label(fr_edit_item, bg="#47761E", fg="white", text="Enter Cost of the product to (Edit : Digits only!) : ", font="Georgia 10")
            lbl_edit_cost.grid(row=7, column=0)

            txt_edit_cost = Entry(fr_edit_item, font="Georgia 15", width=7, bg="#F8F9FA")
            txt_edit_cost.grid(row=7, column=1)

            bt_edit = Button(fr_edit_item, text="Edit", padx=20, pady=10, fg="White", activeforeground="White", bg="#007BFF", activebackground="#007BFF", bd=5, relief=RAISED, command=done)
            bt_edit.grid(row=6, column=3)

        #remove_stock
        def delete_item():
            sql_remove_cursor = main_connection.cursor()

            def delete():
                lt_laundry_current = lt_laundry.curselection()
                lt_pantry_current = lt_pantry.curselection()
                lt_beverages_current = lt_beverages.curselection()
                lt_cleaning_current = lt_cleaning.curselection()
                lt_school_current = lt_school.curselection()

                if lt_laundry_current:
                    selected_index = lt_laundry_current[0]
                    selected_key = lt_laundry.get(selected_index).strip().split()

                    sql_nf_remove_stock = f"UPDATE nonfood SET stock = %s WHERE nonfood_name = %s"
                    sql_nf_value = (0, selected_key[0])

                    sql_remove_cursor.execute(sql_nf_remove_stock, sql_nf_value)
                    main_connection.commit()

                    # sql_delete_query = f"DELETE FROM nonfood WHERE nonfood_name = %s"
                    #
                    # sql_delete_value = (selected_key[0],)
                    #
                    # for index in reversed(lt_laundry_current):
                    #     lt_laundry_values.pop(index)
                    #     lt_laundry.delete(index)
                    # dict_all_orders.pop(selected_item, None)
                    # lt_laundry.config(height=lt_laundry.size())
                    #
                    # sql_delete_cursor.execute(sql_delete_query, sql_delete_value)
                    # main_connection.commit()

                elif lt_pantry_current:
                    selected_index = lt_pantry_current[0]
                    selected_key = lt_pantry.get(selected_index).strip().split()

                    sql_f_remove_stock = f"UPDATE food SET stock = %s WHERE food_name = %s"
                    sql_f_value = (0, selected_key[0])

                    sql_remove_cursor.execute(sql_f_remove_stock, sql_f_value)
                    main_connection.commit()

                elif lt_beverages_current:
                    selected_index = lt_beverages_current[0]
                    selected_key = lt_beverages.get(selected_index).strip().split()

                    sql_f_remove_stock = f"UPDATE food SET stock = %s WHERE food_name = %s"
                    sql_f_value = (0, selected_key[0])

                    sql_remove_cursor.execute(sql_f_remove_stock, sql_f_value)
                    main_connection.commit()

                elif lt_cleaning_current:
                    selected_index = lt_cleaning_current[0]
                    selected_key = lt_cleaning.get(selected_index).strip().split()

                    sql_nf_remove_stock = f"UPDATE nonfood SET stock = %s WHERE nonfood_name = %s"
                    sql_nf_value = (0, selected_key[0])

                    sql_remove_cursor.execute(sql_nf_remove_stock, sql_nf_value)
                    main_connection.commit()

                elif lt_school_current:
                    selected_index = lt_school_current[0]
                    selected_key = lt_school.get(selected_index).strip().split()

                    sql_etc_remove_stock = f"UPDATE etc SET stock = %s WHERE etc_name = %s"
                    sql_etc_value = (0, selected_key[0])

                    sql_remove_cursor.execute(sql_etc_remove_stock, sql_etc_value)
                    main_connection.commit()

                else:
                    messagebox.showerror(title="Error!", message="Please select an item to delete before you press it again!")
                    return

                bt_delete.destroy()

            fr_delete_item = Frame(root, bg="#47761E")
            fr_delete_item.grid(row=10, column=1)

            bt_delete = Button(fr_delete_item, text="Out of stock!", fg="White", activeforeground="White", bg="#DC3545", activebackground="#DC3545", padx=20, pady=10, bd=5, relief=RAISED, command=delete, font="Garamond 10")
            bt_delete.grid(row=10, column=1)

        #restock
        def stock_item():
            sql_stock_cursor = main_connection.cursor()

            def stocked():
                def stocking():

                    food_name = ""
                    nonfood_name = ""
                    etc_name = ""

                    total_stock = txt_stock.get()

                    try:
                        total_stock = int(total_stock)
                    except ValueError:
                        messagebox.showerror(title="Error!", message="Please be sure to input a digit!")
                        return

                    if stock_category == "NonFood":
                        nonfood_name = cb_nf.get()

                        sql_nf_stock = f"UPDATE nonfood SET stock = %s WHERE nonfood_name = %s"
                        sql_nf_value = (total_stock, nonfood_name)

                        sql_stock_cursor.execute(sql_nf_stock, sql_nf_value)
                        main_connection.commit()

                        messagebox.showinfo(title="Validated!",
                                            message=f"The product : {etc_name} has been re-stocked by {total_stock}!")

                    elif stock_category == "Food":
                        food_name = cb_f.get()

                        sql_f_stock = f"UPDATE food SET stock = %s WHERE food_name = %s"
                        sql_f_value = (total_stock, food_name)

                        sql_stock_cursor.execute(sql_f_stock, sql_f_value)
                        main_connection.commit()

                        messagebox.showinfo(title="Validated!",
                                            message=f"The product : {food_name} has been re-stocked by {total_stock}!")

                    elif stock_category == "Etc":
                        etc_name = cb_etc.get()

                        sql_etc_stock = f"UPDATE etc SET stock = %s WHERE etc_name = %s"
                        sql_etc_value = (total_stock, etc_name)

                        sql_stock_cursor.execute(sql_etc_stock, sql_etc_value)
                        main_connection.commit()

                        messagebox.showinfo(title="Validated!", message=f"The product : {etc_name} has been re-stocked by {total_stock}!")

                    else:
                        messagebox.showerror(title="Error!", message="Please make sure you input a valid value!")
                        return

                    stocks.destroy()
                    restock.destroy()

                def stock_return():
                    stocks.destroy()

                stock_category = cb_outofstocks.get()

                stocks = Toplevel(root)
                stocks.title("Re-stocking..")
                stocks.config(bg="#47761E")

                stocks.grab_set()

                lbl_stock_title = Label(stocks, text="|Re-stocking..", font="Garamond 20", bg="#47761E")
                lbl_stock_title.grid(row=0, column=0)

                lbl_stock = Label(stocks, text="Select item you want to re-stock : ", font="Garamond 15", bg="#47761E")
                lbl_stock.grid(row=1, column=0)

                cb_f = ttk.Combobox(stocks, width=10, values=food_item)
                cb_nf = ttk.Combobox(stocks, width=10, values=nonfood_item)
                cb_etc = ttk.Combobox(stocks, width=10, values=etc_item)

                lbl_stock = Label(stocks, text="Enter how many stocks : ", font='Garamond 15', bg="#47761E")
                lbl_stock.grid(row=2, column=0)

                txt_stock = Entry(stocks, font="Garamond 15")
                txt_stock.grid(row=2, column=1)

                bt_stocked = Button(stocks, text="Done", font="Garamond 10", bd=5, relief=RAISED, command=stocking, bg="green")
                bt_stocked.grid(row=3, column=1, sticky="ew", pady=10)

                bt_stocked_return = Button(stocks, text="Return", font="Garamond 10", bd=5, relief=RAISED, command=stock_return)
                bt_stocked_return.grid(row=3, column=0, sticky="ew", pady=10)

                if stock_category == "NonFood":
                    if len(nonfood_item) == 0:
                        messagebox.showerror(title="All products are fine!", message="All Products are fine right now!")
                        stocks.destroy()
                    else:
                        cb_nf.grid(row=1, column=1)

                elif stock_category == "Food":
                    if len(food_item) == 0:
                        messagebox.showerror(title="All products are fine!", message="All Products are fine right now!")
                        stocks.destroy()
                    else:
                        cb_f.grid(row=1, column=1)

                elif stock_category == "Etc":
                    if len(etc_item) == 0:
                        messagebox.showerror(title="All products are fine!", message="All Products are fine right now!")
                        stocks.destroy()
                    else:
                        cb_etc.grid(row=1, column=1)

                else:
                    messagebox.showerror(title="Error!",
                                         message="Please select an item to re-stock before you press it again!")
                    return

                stocks.wait_window()

            def return_stock():
                restock.destroy()

            restock = Toplevel()
            restock.title("Re-stock item")
            restock.config(bg="#47761E")

            restock.grab_set()

            sql_stock_get_cursor = main_connection.cursor()

            food_item = []
            nonfood_item = []
            etc_item = []

            sql_stock_get_cursor.execute("SELECT food_name FROM food WHERE stock = 0 or stock = 1")
            sql_stock_food = sql_stock_get_cursor.fetchall()

            for rows in sql_stock_food:
                food_item.append(str(rows[0]))

            sql_stock_get_cursor.execute("SELECT nonfood_name FROM nonfood WHERE stock = 0 or stock = 1")
            sql_stock_nonfood = sql_stock_get_cursor.fetchall()

            for rows in sql_stock_nonfood:
                nonfood_item.append(rows[0])

            sql_stock_get_cursor.execute("SELECT etc_name, stock FROM etc WHERE stock = 0 or stock = 1")
            sql_stock_etc = sql_stock_get_cursor.fetchall()

            for rows in sql_stock_etc:
                etc_item.append(rows[0])

            lbl_outofstock = Label(restock, text="Select category you want to re-stock : ", font="Garamond 15", bg="#47761E")
            lbl_outofstock.grid(row=1, column=0)

            cb_stock_val = ["Food", "NonFood", "Etc"]
            cb_outofstocks = ttk.Combobox(restock, width=15, values=cb_stock_val, font="Garamond 15")
            cb_outofstocks.grid(row=1, column=1)

            fr_restock_item = Frame(restock, bg="#47761E")
            fr_restock_item.grid(row=2, column=1)

            bt_restock_done = Button(fr_restock_item, text="Done", font="Garamond 15", bd=5, relief=RAISED, command=stocked, bg="beige")
            bt_restock_done.grid(row=2, column=2, sticky="e")

            bt_restock_back = Button(fr_restock_item, text='Return', font="Garamond 15", bd=5, relief=RAISED, command=return_stock)
            bt_restock_back.grid(row=2, column=1, sticky="w")

            restock.wait_window()

        # Show Accounts
        def show_user_accounts():
            user_full_show = ""
            show_acc_cursor = main_connection.cursor()
            show_acc_cursor.execute(f"SELECT username, status FROM {main_database['Table']};")
            show_acc = show_acc_cursor.fetchall()

            if len(user_accounts) == 1 or len(show_acc) == 0:
                messagebox.showerror(title="No accounts!", message="Sorry, No accounts to show!")
                return

            for username, value in user_accounts.items():
                if 'Password' in value:
                    if username == 'Select an account to remove..':
                        pass

            for rows in show_acc:
                user_full_show += f"\n\n\nUsername : {str(rows[0])} | Status : {str(rows[1])}"
            messagebox.showinfo(title="User accounts in Database", message=f"Useraccounts in Database : \n\n{user_full_show}")

        #Search eto next
        def search():
            src = Toplevel(root)
            src.title('Orders History')
            src.config(bg="#a1822f")
            src.geometry("800x470")

            src.grab_set()

            src_width = src.winfo_screenwidth()
            src_height = src.winfo_screenheight()

            winsrc_width = 800
            winsrc_height = 470

            pos_x = (src_width - winsrc_width) // 2
            pos_y = (src_height - winsrc_height) // 2

            src.geometry(f"{winsrc_width}x{winsrc_height}+{pos_x}+{pos_y}")

            def search_done():
                user_search = cb_search.get()
                sql_search_up = f"SELECT order_id, food_items, non_food_items, etc_items, total_amount, payment_method, service_method, order_time FROM check_out_order WHERE username = %s"
                sql_search_value = (user_search,)
                user_all_info = ""

                if user_search not in sql_users_fetchs:
                    messagebox.showerror(title="Nope!", message="Please select a valid user to see!")
                    return

                sql_search_cursor.execute(sql_search_up, sql_search_value)
                user_info = sql_search_cursor.fetchall()

                if not user_info:
                    messagebox.showerror(title="No Orders to be presented!", message="There are no orders yet!")
                    return

                for rows in user_info:
                    user_all_info += f"Order_id : {str(rows[0])} \n_____ Food items _____  {str(rows[1],)} \n\n_____ Non-Food items _____ {str(rows[2],)} \n\n_____ Etc items _____ {str(rows[3],)} \n\n_____________________\n Payment Method : {str(rows[4])} \n Service Method : {str(rows[5])} \n Total Amount : {str(rows[6])} \n Order Date : {str(rows[7])}\n\n"

                messagebox.showinfo(title=f"{user_search} INFO!", message=f"{user_all_info}")

            def search_cancel():
                src.destroy()

            sql_search_cursor = main_connection.cursor()
            sql_search_all_cursor = main_connection.cursor()
            sql_search_all = f"SELECT order_id, username, food_items, non_food_items, etc_items, total_amount, payment_method, service_method, order_time FROM check_out_order"
            sql_search_all_cursor.execute(sql_search_all)
            sql_search_all_order = sql_search_all_cursor.fetchall()
            sql_all_orders = []

            for rows in sql_search_all_order:
                orders = {
                    "order_id": rows[0],
                    "customer_name": rows[1], "food_order": rows[2], "nonfood_order": rows[3], "etc_order": rows[4],
                    "total_amount": rows[5], "payment_method": rows[6], "service": rows[7], "order_date": rows[8]}
                sql_all_orders.append(orders)

            sql_search_cursor.execute(f"SELECT username FROM {main_database['Table']}")
            sql_users_fetchs = [users[0] for users in sql_search_cursor.fetchall()]

            fr_search = Frame(src, bg="#a1822f")
            fr_search.grid(row=0, column=0)

            lbl_search = Label(fr_search, text="Select an account to search onto : ", font="Georgia 25", padx=20, pady=10, bg="#a1822f")
            lbl_search.grid(row=0, column=0)

            cb_search = ttk.Combobox(fr_search, width=15, font="Georgia 15", values=sql_users_fetchs)
            cb_search.grid(row=0, column=1)

            fr_orders = Frame(src, bg="#a1822f")
            fr_orders.grid(row=1, column=0)

            order_text = Text(fr_orders, width=60, height=20, wrap=WORD, font="Georgia 10")
            order_text.grid(row=1, column=0, sticky="nsew")

            orders_scroll = Scrollbar(fr_orders, command=order_text.yview, orient=VERTICAL)
            orders_scroll.grid(row=1, column=1, sticky="ns")

            for orders in sql_all_orders:
                order_text.insert(END, f"Order Id : {orders['order_id']} | username : {orders['customer_name']} "
                                       f"| Total amount : {orders['total_amount']}\n | Payment method : {orders['payment_method']} | Service method : {orders['service']}\n | Date ordered : {orders['order_date']}\n | Food orders : {orders['food_order']}\n | Non-food orders : {orders['nonfood_order']}\n | Etc orders : {orders['etc_order']}\n\n\n")

            src.grid_rowconfigure(2, weight=1)
            order_text.config(yscrollcommand=orders_scroll.set)

            fr_bt_search = Frame(src, bg="#a1822f")
            fr_bt_search.grid(row=4, column=0)

            bt_search_done = Button(fr_bt_search, text="Done", font="Garamond 20", padx=20, relief=RAISED, bd=5, command=search_done)
            bt_search_done.grid(row=1, column=1, pady=20)

            bt_search_cancel = Button(fr_bt_search, text="Cancel", font="Garamond 20", padx=20, bd=5, relief=RAISED, command=search_cancel)
            bt_search_cancel.grid(row=1, column=0, pady=20)

            src.wait_window()

        #delivery
        def deliveries():
            sql_deliver_cursor = main_connection.cursor()
            sql_deliver_cursor.execute(f"SELECT order_id, username, address, contact, buy_date, arrival_date FROM delivery")
            sql_deliver_get = sql_deliver_cursor.fetchall()
            sql_deliver_orders = []

            if sql_deliver_get == 0:
                messagebox.showerror(title="Error!", message="No deliveries!")
                return

            for rows in sql_deliver_get:
                deliver_data = {"order_id": rows[0], "username":rows[1], "address": rows[2], "contact": rows[3],
                                "buy_date": rows[4], "arrival_date": rows[5]}
                sql_deliver_orders.append(deliver_data)

            deliver_info = Toplevel(root)
            deliver_info.title("| Deliveries")
            deliver_info.geometry("800x470")
            deliver_info.config(bg="#000000")

            del_width = deliver_info.winfo_screenwidth()
            del_height = deliver_info.winfo_screenheight()

            windel_width = 800
            windel_height = 470

            pos_x = (del_width - windel_width) // 2
            pos_y = (del_height - windel_height) // 2

            deliver_info.geometry(f"{windel_width}x{windel_height}+{pos_x}+{pos_y}")

            deliver_info.grab_set()

            lbl_deliver_title = Label(deliver_info, text=" | Deliveries", fg="white", font="Garamond 20", bg="#000000")
            lbl_deliver_title.grid(row=0, column=0)

            fr_deliver = Frame(deliver_info, bg="#a1822f")
            fr_deliver.grid(row=1, column=0)

            del_text = Text(fr_deliver, width=60, height=20, wrap=WORD, font="Georgia 10")
            del_text.grid(row=1, column=1, sticky="nsew")

            del_scroll = Scrollbar(fr_deliver, command=del_text.yview, orient=VERTICAL)
            del_scroll.grid(row=1, column=2, sticky="ns")

            for delivers in sql_deliver_orders:
                del_text.insert(END, f"Order ID : {delivers['order_id']} | Username : {delivers['username']}\n"
                                     f"Address : {delivers['address']} | Contact No. : {delivers['contact']}\n Day bought : {delivers['buy_date']} | Arrival Date : {delivers['arrival_date']}\n\n")

            deliver_info.grid_rowconfigure(2, weight=1)
            del_text.config(yscrollcommand=del_scroll.set)

            bt_deliver_return = Button(deliver_info, text="Return", font="Garamond 20", command=deliver_info.destroy, bg="green")
            bt_deliver_return.grid(row=3, column=0, sticky="ew")

            deliver_info.wait_window()

        # Delete accounts
        def delete_user_account():

            delete_acc_cursor = main_connection.cursor()
            sql_update_account = f"UPDATE {main_database['Table']} SET status = %s WHERE username = %s"

            if len(user_accounts) == 1:
                messagebox.showerror(title="Error No accounts!", message="No accounts registered!")
                return

            del_user = Toplevel()
            del_user.title("Status UserAccount Update")
            del_user.config(bg="#47761E")
            del_user.geometry("800x150")

            del_user.grab_set()

            del_width = del_user.winfo_screenwidth()
            del_height = del_user.winfo_screenheight()

            window_width = 800
            window_height = 150

            pos_x = (del_width - window_width) // 2
            pos_y = (del_height - window_height) // 2

            del_user.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

            def delete_account():

                if cb_user_del.get() == 'Select an account to remove..' or cb_user_del.get() == "" or cb_user_del.get() not in user_accounts:
                    messagebox.showerror(title="Error!", message="Please select a proper account to delete!")
                    return

                account_delete = cb_user_del.get()
                account_stats = user_accounts[account_delete]["Status"]

                sql_active_val = ('active', account_delete)
                sql_inactive_val = ('inactive', account_delete)

                if account_stats == "active":
                    user_accounts[account_delete]["Status"] = "inactive"
                    delete_acc_cursor.execute(sql_update_account, sql_inactive_val)
                    main_connection.commit()
                    del_user.destroy()

                if account_stats == "inactive":
                    user_accounts[account_delete]["Status"] = "active"
                    delete_acc_cursor.execute(sql_update_account, sql_active_val)
                    main_connection.commit()
                    del_user.destroy()

                #remove acc!
                # if account_to_delete:
                #     current_account = []
                #
                #     if account_delete in user_accounts:
                #         del user_accounts[account_delete]
                #         to_delete = account_delete
                #
                #         delete_acc_cursor.execute(sql_delete, (to_delete,))
                #         main_connection.commit()
                #
                #         messagebox.showinfo(title="Successfully Updated!", message="The update is successful!")
                #
                #     for ind in cb_user_del['values']:
                #         if ind != account_delete:
                #             current_account.append(ind)
                #
                #     cb_user_del['values'] = current_account
                #
                #     cb_user_del.delete(0, END)

            fr_del_user = Frame(del_user,bg="#47761E")
            fr_del_user.grid(row=1, column=1)

            lbl_del_user = Label(fr_del_user, bg="#47761E", text="Choose Account to Delete : ",
                                 font="Georgia 15", padx=20, pady=10)
            lbl_del_user.grid(row=1, column=0)

            cb_user_del_var = StringVar()
            cb_user_del = ttk.Combobox(fr_del_user, width=25, height=10, textvariable=cb_user_del_var, values=list(user_accounts.keys()), font="Garamond 15")
            cb_user_del.current(0)
            cb_user_del.grid(row=1, column=1)

            bt_del_user = Button(fr_del_user, text="Update Account!", bg="#DC3545", activebackground="#DC3545", font="Garamond 15",
                                 fg="White", activeforeground="White", bd=5, relief=RAISED, command=delete_account)
            bt_del_user.grid(row=2, column=1, sticky=W)

            bt_return_user = Button(fr_del_user, text="Return", bg="Green", activebackground="Green", font="Garamond 15",
                                    fg="White", activeforeground="White", bd=5, relief=RAISED, command=del_user.destroy)
            bt_return_user.grid(row=2, column=2, sticky=E)

            del_user.wait_window()

        #Format
        # def format_user_accounts():
        #     format_db_user = main_connection.cursor()
        #     sql_format = f"TRUNCATE {main_database['Table']};"
        #
        #     if len(user_accounts) == 1:
        #         messagebox.showerror(title="Error no account!", message="No accounts are registered!")
        #         return
        #
        #     account_remove = []
        #     account_to_keep = ["Select an account to remove.."]
        #
        #     decision = messagebox.askyesno(title="ARE YOU SURE!!?", message="This could mean end of the world! You're gonna delete all of the accounts?! For sure!!")
        #     if decision:
        #         for username in user_accounts.keys():
        #             if username not in account_to_keep:
        #                 account_remove.append(username)
        #
        #         for key in account_remove:
        #             user_accounts.pop(key)
        #
        #         format_db_user.execute(sql_format)
        #
        #     else:
        #         return

        tools_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Tools", menu=tools_menu)

        sub_add_menu = Menu(tools_menu, tearoff=0)
        sub_add_menu.add_command(label="Laundry(Section)", command=lambda: add_item("Laundry(Section)"))
        sub_add_menu.add_command(label="Pantry(Section)", command=lambda: add_item("Pantry(Section)"))
        sub_add_menu.add_command(label="Beverages(Section)", command=lambda: add_item("Beverages(Section)"))
        sub_add_menu.add_command(label="Cleaning(Section)", command=lambda: add_item("Cleaning(Section)"))
        sub_add_menu.add_command(label="SchoolSupplies(Section)", command=lambda: add_item("SchoolSupplies(Section)"))
        tools_menu.add_cascade(label="Add Item to..", menu=sub_add_menu)

        tools_menu.add_command(label="Edit Item", command=edit_item)
        tools_menu.add_command(label="Re-stock Item", command=stock_item)
        tools_menu.add_command(label="Remove Item", command=delete_item)

        # account_manage_menu = Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Manage(UserAccounts)", menu=account_manage_menu)
        # account_manage_menu.add_command(label="Show Accounts", command=show_user_accounts)
        # account_manage_menu.add_separator()
        # account_manage_menu.add_command(label="Order History", command=search)
        # account_manage_menu.add_separator()
        # account_manage_menu.add_command(label="Status Update Account", command=delete_user_account)

        bt_createacc = Button(root, text="Deliveries", font="Garamond 15", command=deliveries)
        bt_createacc.grid(row=8, column=5, sticky="nsew")

        bt_showacc = Button(root, text="Show UserAccounts", font="Garamond 15", command=show_user_accounts)
        bt_showacc.grid(row=7, column=5, sticky="nsew")

        bt_orderhistory = Button(root, text="Order History", font="Garamond 15", command=search)
        bt_orderhistory.grid(row=8, column=6,sticky="nsew")

        bt_statupdate = Button(root, text="Status Update",font="Garamond 15", command=delete_user_account)
        bt_statupdate.grid(row=7, column=6,sticky="nsew")



    #User Interface

    def category_check(isle):
        def new_isle():
            #bt_category.config(state=NORMAL)
            #cb_item_selector.current(0)

            bt_bev_cat.config(state=NORMAL)
            bt_laundry_cat.config(state=NORMAL)
            bt_cl_cat.config(state=NORMAL)
            bt_sc_cat.config(state=NORMAL)
            bt_pantry_cat.config(state=NORMAL)

            bt_new.destroy()
            bt_select.destroy()
            bt_order.destroy()

            if category == "Laundry":
                lt_scrollbar.grid_forget()
                lt_laundry.grid_forget()
                bt_cl_cat.config(state=NORMAL)
                bt_sc_cat.config(state=NORMAL)
                bt_pantry_cat.config(state=NORMAL)
                bt_bev_cat.config(state=NORMAL)

            elif category == "Pantry":
                lt_scrollbar.grid_forget()
                lt_pantry.grid_forget()
                bt_bev_cat.config(state=NORMAL)
                bt_laundry_cat.config(state=NORMAL)
                bt_cl_cat.config(state=NORMAL)
                bt_sc_cat.config(state=NORMAL)

            elif category == "Beverages":
                lt_scrollbar.grid_forget()
                lt_beverages.grid_forget()
                bt_laundry_cat.config(state=NORMAL)
                bt_cl_cat.config(state=NORMAL)
                bt_sc_cat.config(state=NORMAL)
                bt_pantry_cat.config(state=NORMAL)

            elif category == "Cleaning":
                lt_scrollbar.grid_forget()
                lt_cleaning.grid_forget()
                bt_sc_cat.config(state=NORMAL)
                bt_pantry_cat.config(state=NORMAL)
                lt_beverages.grid_forget()
                bt_laundry_cat.config(state=NORMAL)

            elif category == "SchoolSupplies":
                lt_scrollbar.grid_forget()
                lt_school.grid_forget()
                bt_pantry_cat.config(state=NORMAL)
                lt_beverages.grid_forget()
                bt_laundry_cat.config(state=NORMAL)
                bt_cl_cat.config(state=NORMAL)

            elif category is None:
                lt_laundry.grid_forget()
                lt_pantry.grid_forget()
                lt_beverages.grid_forget()
                lt_cleaning.grid_forget()
                lt_school.grid_forget()

            lbl_item_view.destroy()

        def money_convert(money_str):
            return float(money_str.replace("$", ""))

        def add_order():
            user_name = username_main.get()
            category_add = isle
            user_stat = kwargs[username_main.get()]["Status"]
            order_cost = ""

            sql_stock_getter_cursor = main_connection.cursor()
            sql_fstock_getter = f"SELECT stock FROM food WHERE food_name = %s"
            sql_nfstock_getter = f"SELECT stock FROM nonfood WHERE nonfood_name = %s"
            sql_etcstock_getter = f"SELECT stock FROM etc WHERE etc_name = %s"

            if user_stat == "inactive":
                messagebox.showerror(title="Oops! Seems like you can't order!", message="I'm sorry but you can't order if you're in inactive mode!")
                return

            if category_add == "":
                messagebox.showerror(title="No order!", message="Please select an order first!")
                return

            if category_add == "Laundry":

                def add_laundry_basket():

                    try:
                        quantity_num = int(cb_quantity.get())
                        if quantity_num < 0 or quantity_num == 0:
                            messagebox.showerror(title="Error in quantity input!", message="Please be sure to put some valid inputs!")
                            return

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please be sure to input a number!")
                        return

                    if quantity_num >= 1:
                        selected_order = lt_laundry.get(selected_item).strip().split()
                        user_order = selected_order[0]
                        order_cost = selected_order[1]

                        kwargs[user_name]['Non-Food'].append(f"\n{user_order} x{quantity_num}")
                        kwargs[user_name]['Orders'].append(f"\n{user_order} x{quantity_num}")

                        kwargs[user_name]['Non-FoodCost'] += (money_convert(order_cost) * quantity_num)
                        kwargs[user_name]['Total'] += (money_convert(order_cost) * quantity_num)
                        lt_laundry.select_clear(0, END)
                        messagebox.showinfo(title=f"You've ordered : {user_order}",
                                            message=f"You've ordered : {user_order} x{quantity_num}")

                    else:
                        messagebox.showerror(title="Out of range!", message="You've enter an out of ranged value!")
                        return

                    quantity_laundry.destroy()

                def cancel_laundry():
                    quantity_laundry.destroy()

                selected_item = lt_laundry.curselection()
                selected_laundry = lt_laundry.get(selected_item).strip().split()
                user_laundry = selected_laundry[0]

                sql_stock_getter_cursor.execute(sql_nfstock_getter, (user_laundry,))
                sql_nf_stock_get = sql_stock_getter_cursor.fetchall()
                nf_stock = 0
                for rows in sql_nf_stock_get:
                    nf_stock = rows[0]

                quantity_laundry = Toplevel(root)
                quantity_laundry.title(f"| Quantity for {user_laundry}")
                quantity_laundry.geometry("470x150")
                quantity_laundry.config(bg="#47761E")

                quantity_laundry.grab_set()

                qua_width = quantity_laundry.winfo_screenwidth()
                qua_height = quantity_laundry.winfo_screenheight()

                window_width = 470
                window_height = 150

                pos_x = (qua_width - window_width) // 2
                pos_y = (qua_height - window_height) // 2

                quantity_laundry.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                lbl_quantity = Label(quantity_laundry, image=background_howpac, highlightthickness=0, bd=0)
                lbl_quantity.grid(row=1, column=0, sticky="nsew")

                cb_quantity_max = [qua for qua in range(1, nf_stock)]
                cb_quantity = ttk.Combobox(quantity_laundry, values=cb_quantity_max, width=20, font="Georgia 15")
                cb_quantity.grid(row=1, column=1)

                bt_laundry_qua = Button(quantity_laundry, image=background_paypac, highlightthickness=0, bd=0,command=add_laundry_basket)
                bt_laundry_qua.grid(row=2, column=1)

                bt_laundry_can = Button(quantity_laundry, image=background_cancelpac,highlightthickness=0, bd=0, command=cancel_laundry)
                bt_laundry_can.grid(row=2, column=0)

                quantity_laundry.wait_window()

            if category_add == "Pantry":

                def add_pantry_basket():

                    try:
                        quantity_num = int(cb_quantity.get())
                        if quantity_num < 0 or quantity_num == 0:
                            messagebox.showerror(title="Error in quantity input!", message="Please be sure to put some valid inputs!")
                            return

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please be sure to input a number!")
                        return

                    if quantity_num >= 1:
                        selected_order = lt_pantry.get(selected_item).strip().split()
                        user_order = selected_order[0]
                        order_cost = selected_order[1]

                        kwargs[user_name]['Food'].append(f"\n{user_order} x{quantity_num}")
                        kwargs[user_name]['Orders'].append(f"\n{user_order} x{quantity_num}")

                        kwargs[user_name]['FoodCost'] += (money_convert(order_cost) * quantity_num)
                        kwargs[user_name]['Total'] += (money_convert(order_cost) * quantity_num)
                        lt_pantry.select_clear(0, END)

                        messagebox.showinfo(title=f"You've ordered : {user_order}",
                                            message=f"You've ordered : {user_order} x{quantity_num}")

                    else:
                        messagebox.showerror(title="Out of range!", message="You've enter an out of ranged value!")
                        return

                    quantity_pantry.destroy()

                def cancel_pantry():
                    quantity_pantry.destroy()

                selected_item = lt_pantry.curselection()
                selected_pantry = lt_pantry.get(selected_item).strip().split()
                user_pantry = selected_pantry[0]

                sql_stock_getter_cursor.execute(sql_fstock_getter, (user_pantry,))
                sql_fstock_get = sql_stock_getter_cursor.fetchall()
                f_stock = 0

                for rows in sql_fstock_get:
                    f_stock = rows[0]

                quantity_pantry = Toplevel(root)
                quantity_pantry.title(f"| Quantity for {user_pantry}")
                quantity_pantry.geometry("470x150")
                quantity_pantry.config(bg="#47761E")

                quantity_pantry.grab_set()

                qua_width = quantity_pantry.winfo_screenwidth()
                qua_height = quantity_pantry.winfo_screenheight()

                window_width = 470
                window_height = 150

                pos_x = (qua_width - window_width) // 2
                pos_y = (qua_height - window_height) // 2

                quantity_pantry.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                lbl_quantity = Label(quantity_pantry, image=background_howpac, highlightthickness=0, bd=0)
                lbl_quantity.grid(row=1, column=0, sticky="nsew")

                cb_quantity_max = [qua for qua in range(1, f_stock)]
                cb_quantity = ttk.Combobox(quantity_pantry, values=cb_quantity_max, width=20, font="Georgia 15")
                cb_quantity.grid(row=1, column=1)

                bt_pantry_qua = Button(quantity_pantry,  image=background_paypac, highlightthickness=0, bd=0,
                                        command=add_pantry_basket)
                bt_pantry_qua.grid(row=2, column=1)

                bt_pantry_can = Button(quantity_pantry, image=background_cancelpac,highlightthickness=0, bd=0,
                                        command=cancel_pantry)
                bt_pantry_can.grid(row=2, column=0)

                quantity_pantry.wait_window()

            if category_add == "Beverages":

                def add_bev_basket():

                    try:
                        quantity_num = int(cb_quantity.get())
                        if quantity_num < 0 or quantity_num == 0:
                            messagebox.showerror(title="Error in quantity input!", message="Please be sure to put some valid inputs!")
                            return

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please be sure to input a number!")
                        return

                    if quantity_num >= 1:
                        selected_order = lt_beverages.get(selected_item).strip().split()
                        user_order = selected_order[0]
                        order_cost = selected_order[1]

                        kwargs[user_name]['Food'].append(f"\n{user_order} x{quantity_num}")
                        kwargs[user_name]['Orders'].append(f"\n{user_order} x{quantity_num}")

                        kwargs[user_name]['FoodCost'] += (money_convert(order_cost) * quantity_num)
                        kwargs[user_name]['Total'] += (money_convert(order_cost) * quantity_num)
                        lt_beverages.select_clear(0, END)

                        messagebox.showinfo(title=f"You've ordered : {user_order}",
                                            message=f"You've ordered : {user_order} x{quantity_num}")

                    else:
                        messagebox.showerror(title="Out of range!", message="You've enter an out of ranged value!")
                        return

                    quantity_bev.destroy()

                def cancel_bev():
                    quantity_bev.destroy()

                selected_item = lt_beverages.curselection()
                selected_bev = lt_beverages.get(selected_item).strip().split()
                user_bev = selected_bev[0]

                sql_stock_getter_cursor.execute(sql_fstock_getter, (user_bev,))
                sql_fstock_get = sql_stock_getter_cursor.fetchall()
                f_stock = 0

                for rows in sql_fstock_get:
                    f_stock = rows[0]

                quantity_bev = Toplevel(root)
                quantity_bev.title(f"| Quantity for {user_bev}")
                quantity_bev.geometry("470x150")
                quantity_bev.config(bg="#47761E")

                quantity_bev.grab_set()

                qua_width = quantity_bev.winfo_screenwidth()
                qua_height = quantity_bev.winfo_screenheight()

                window_width = 470
                window_height = 150

                pos_x = (qua_width - window_width) // 2
                pos_y = (qua_height - window_height) // 2

                quantity_bev.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                lbl_quantity = Label(quantity_bev,image=background_howpac, highlightthickness=0, bd=0)
                lbl_quantity.grid(row=1, column=0, sticky="nsew")

                cb_quantity_max = [qua for qua in range(1, f_stock)]
                cb_quantity = ttk.Combobox(quantity_bev, values=cb_quantity_max, width=20, font="Georgia 15")
                cb_quantity.grid(row=1, column=1)

                bt_bev_qua = Button(quantity_bev,  image=background_paypac, highlightthickness=0, bd=0,
                                       command=add_bev_basket)
                bt_bev_qua.grid(row=2, column=1)

                bt_bev_can = Button(quantity_bev, image=background_cancelpac,highlightthickness=0, bd=0,
                                       command=cancel_bev)
                bt_bev_can.grid(row=2, column=0)

                quantity_bev.wait_window()

            if category_add == "Cleaning":

                def add_cl_basket():

                    try:
                        quantity_num = int(cb_quantity.get())
                        if quantity_num < 0 or quantity_num == 0:
                            messagebox.showerror(title="Error in quantity input!",
                                                 message="Please be sure to put some valid inputs!")
                            return

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please be sure to input a number!")
                        return

                    if quantity_num >= 1:
                        selected_order = lt_cleaning.get(selected_item).strip().split()
                        user_order = selected_order[0]
                        order_cost = selected_order[1]

                        kwargs[user_name]['Non-Food'].append(f"\n{user_order} x{quantity_num}")
                        kwargs[user_name]['Orders'].append(f"\n{user_order} x{quantity_num}")

                        kwargs[user_name]['Non-FoodCost'] += (money_convert(order_cost) * quantity_num)
                        kwargs[user_name]['Total'] += (money_convert(order_cost) * quantity_num)
                        lt_beverages.select_clear(0, END)

                        messagebox.showinfo(title=f"You've ordered : {user_order}",
                                            message=f"You've ordered : {user_order} x{quantity_num}")

                    else:
                        messagebox.showerror(title="Out of range!", message="You've enter an out of ranged value!")
                        return

                    quantity_cl.destroy()

                def cancel_cl():
                    quantity_cl.destroy()

                selected_item = lt_cleaning.curselection()
                selected_cl = lt_cleaning.get(selected_item).strip().split()
                user_cl = selected_cl[0]

                sql_stock_getter_cursor.execute(sql_nfstock_getter, (user_cl,))
                sql_nf_stock_get = sql_stock_getter_cursor.fetchall()
                nf_stock = 0
                for rows in sql_nf_stock_get:
                    nf_stock = rows[0]

                quantity_cl = Toplevel(root)
                quantity_cl.title(f"| Quantity for {user_cl}")
                quantity_cl.geometry("470x150")
                quantity_cl.config(bg="#47761E")

                quantity_cl.grab_set()

                qua_width = quantity_cl.winfo_screenwidth()
                qua_height = quantity_cl.winfo_screenheight()

                window_width = 470
                window_height = 150

                pos_x = (qua_width - window_width) // 2
                pos_y = (qua_height - window_height) // 2

                quantity_cl.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                lbl_quantity = Label(quantity_cl, image=background_howpac, highlightthickness=0, bd=0)
                lbl_quantity.grid(row=1, column=0, sticky="nsew")

                cb_quantity_max = [qua for qua in range(1, nf_stock)]
                cb_quantity = ttk.Combobox(quantity_cl, values=cb_quantity_max, width=20, font="Georgia 15")
                cb_quantity.grid(row=1, column=1)

                bt_cl_qua = Button(quantity_cl,  image=background_paypac, highlightthickness=0, bd=0,
                                    command=add_cl_basket)
                bt_cl_qua.grid(row=2, column=1)

                bt_cl_can = Button(quantity_cl, image=background_cancelpac,highlightthickness=0, bd=0,
                                    command=cancel_cl)
                bt_cl_can.grid(row=2, column=0)

                quantity_cl.wait_window()

            if category_add == "SchoolSupplies":

                def add_sp_basket():

                    try:
                        quantity_num = int(cb_quantity.get())
                        if quantity_num < 0 or quantity_num == 0:
                            messagebox.showerror(title="Error in quantity input!",
                                                 message="Please be sure to put some valid inputs!")
                            return

                    except ValueError:
                        messagebox.showerror(title="Invalid input!", message="Please be sure to input a number!")
                        return

                    if quantity_num >= 1:
                        selected_order = lt_school.get(selected_item).strip().split()
                        user_order = selected_order[0]
                        order_cost = selected_order[1]

                        kwargs[user_name]['ETC.'].append(f"\n{user_order} x{quantity_num}")
                        kwargs[user_name]['Orders'].append(f"\n{user_order} x{quantity_num}")

                        kwargs[user_name]['EtcCost'] += (money_convert(order_cost) * quantity_num)
                        kwargs[user_name]['Total'] += (money_convert(order_cost) * quantity_num)
                        lt_school.select_clear(0, END)

                        messagebox.showinfo(title=f"You've ordered : {user_order}",
                                        message=f"You've ordered : {user_order} x{quantity_num}")

                    else:
                        messagebox.showerror(title="Out of range!", message="You've enter an out of ranged value!")
                        return

                    quantity_sp.destroy()

                def cancel_sp():
                    quantity_sp.destroy()

                selected_item = lt_school.curselection()
                selected_sp = lt_school.get(selected_item).strip().split()
                user_sp = selected_sp[0]

                sql_stock_getter_cursor.execute(sql_etcstock_getter, (user_sp,))
                sql_etcstock_get = sql_stock_getter_cursor.fetchall()
                etc_stock = 0

                for rows in sql_etcstock_get:
                    etc_stock = rows[0]

                quantity_sp = Toplevel(root)
                quantity_sp.title(f"| Quantity for {user_sp}")
                quantity_sp.geometry("470x150")
                quantity_sp.config(bg="#47761E")

                quantity_sp.grab_set()

                qua_width = quantity_sp.winfo_screenwidth()
                qua_height = quantity_sp.winfo_screenheight()

                window_width = 470
                window_height = 150

                pos_x = (qua_width - window_width) // 2
                pos_y = (qua_height - window_height) // 2

                quantity_sp.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                lbl_quantity = Label(quantity_sp, image=background_howpac, highlightthickness=0, bd=0)
                lbl_quantity.grid(row=1, column=0, sticky="nsew")

                cb_quantity_max = [qua for qua in range(1, etc_stock)]
                cb_quantity = ttk.Combobox(quantity_sp, values=cb_quantity_max, width=20, font="Georgia 15")
                cb_quantity.grid(row=1, column=1)

                bt_sp_qua = Button(quantity_sp,  image=background_paypac, highlightthickness=0, bd=0,
                                    command=add_sp_basket)
                bt_sp_qua.grid(row=2, column=1)

                bt_sp_can = Button(quantity_sp, image=background_cancelpac,highlightthickness=0, bd=0,
                                    command=cancel_sp)
                bt_sp_can.grid(row=2, column=0)

                quantity_sp.wait_window()

        def selection():

            category_address = isle

            if category_address == "Laundry":
                item_selected_idx = lt_laundry.curselection()

                if not item_selected_idx:
                    messagebox.showerror(title="No selected Product", message="Please choose a product first before selecting!")
                    return

                item_selected = lt_laundry.get(item_selected_idx).strip().split()
                item_select = item_selected[0]

                if item_select == "SurfFabcon":
                    lbl_item_view.config(image=background_surfpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Wings":
                    lbl_item_view.configure(image=background_wingspac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Uppy":
                    lbl_item_view.configure(image=background_uppypac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Bathwash":
                    lbl_item_view.configure(image=background_bathpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Pride":
                    lbl_item_view.configure(image=background_pridpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Ariel":
                    lbl_item_view.configure(image=background_arielpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Lunox":
                    lbl_item_view.configure(image=background_lunoxpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                else:
                    lbl_item_view.configure(image=background_laundryquepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

            if category_address == "Pantry":
                item_selected_idx = lt_pantry.curselection()

                if not item_selected_idx:
                    messagebox.showerror(title="No selected Product", message="Please choose a product first before selecting!")
                    return

                item_selected = lt_pantry.get(item_selected_idx).strip().split()
                item_select = item_selected[0]

                if item_select == "Gardenia":
                    lbl_item_view.configure(image=background_gardepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "ChocolateBread":
                    lbl_item_view.configure(image=background_chocopac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "GarlicBread":
                    lbl_item_view.configure(image=background_garpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "PandecocoExtreme":
                    lbl_item_view.configure(image=background_panpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "BavarianTasty":
                    lbl_item_view.configure(image=background_bavpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "CocoLumber":
                    lbl_item_view.configure(image=background_cocopac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                else:
                    lbl_item_view.configure(image=background_pantryquepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

            if category_address == "Beverages":
                item_selected_idx = lt_beverages.curselection()

                if not item_selected_idx:
                    messagebox.showerror(title="No selected Product", message="Please choose a product first before selecting!")
                    return

                item_selected = lt_beverages.get(item_selected_idx).strip().split()
                item_select = item_selected[0]

                if item_select == "PocariSweat":
                    lbl_item_view.configure(image=background_pcpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Emperador":
                    lbl_item_view.configure(image=background_eppac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Coke":
                    lbl_item_view.configure(image=background_ckpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Pepsi":
                    lbl_item_view.configure(image=background_peppac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Sprite":
                    lbl_item_view.configure(image=background_spritepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "RootBeer":
                    lbl_item_view.configure(image=background_rbpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "JackDaniels":
                    lbl_item_view.configure(image=background_jdpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Nestea":
                    lbl_item_view.configure(image=background_nespac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                else:
                    lbl_item_view.configure(image=background_bevquepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

            if category_address == "Cleaning":
                item_selected_idx = lt_cleaning.curselection()

                if not item_selected_idx:
                    messagebox.showerror(title="No selected Product", message="Please choose a product first before selecting!")
                    return

                item_selected = lt_cleaning.get(item_selected_idx).strip().split()
                item_select = item_selected[0]

                if item_select == "Mr.Muscles":
                    lbl_item_view.configure(image=background_mrpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "HydrogenMonoxide":
                    lbl_item_view.configure(image=background_hypac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Molotov":
                    lbl_item_view.configure(image=background_molpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "ToiletCleaners":
                    lbl_item_view.configure(image=background_clpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Zonrox":
                    lbl_item_view.configure(image=background_zonpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "SulfuricAcid":
                    lbl_item_view.configure(image=background_monpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Brush":
                    lbl_item_view.configure(image=background_brpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Molotov":
                    lbl_item_view.configure(image=background_molpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                else:
                    lbl_item_view.configure(image=background_clquepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

            if category_address == "SchoolSupplies":
                item_selected_idx = lt_school.curselection()

                if not item_selected_idx:
                    messagebox.showerror(title="No selected Product", message="Please choose a product first before selecting!")
                    return

                item_selected = lt_school.get(item_selected_idx).strip().split()
                item_select = item_selected[0]

                if item_select == "NoteBook":
                    lbl_item_view.configure(image=background_notepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "Marker":
                    lbl_item_view.configure(image=background_marpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "BallPoint":
                    lbl_item_view.configure(image=background_penpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "PadPaper":
                    lbl_item_view.configure(image=background_padpac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                elif item_select == "SprayPaint":
                    lbl_item_view.configure(image=background_spraypac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

                else:
                    lbl_item_view.configure(image=background_spquepac)
                    if kwargs != admin_accounts:
                        bt_order.grid(row=1, column=2, sticky="ew")

        #Stock checker
        #laundry
        def on_select_lnd(event):
            selected_indices = lt_laundry.curselection()

            if selected_indices:
                selected_index = selected_indices[0]
                selected_items = lt_laundry.get(selected_index)

                item_name = selected_items.split(" ")[0]

                sql_nonfood_get_cursor.execute("SELECT stock FROM nonfood WHERE nonfood_name = %s", (item_name,))
                stock = sql_nonfood_get_cursor.fetchone()

                if stock and stock[0] <= 1:
                    lt_laundry.itemconfig(selected_index, {"fg": "gray"})
                    lt_laundry.select_clear(selected_index)

        #Cleaning
        def on_select_cl(event):
            selected_indices = lt_cleaning.curselection()

            if selected_indices:
                selected_index = selected_indices[0]
                selected_items = lt_cleaning.get(selected_index)

                item_name = selected_items.split(" ")[0]

                sql_nonfood_get_cursor.execute("SELECT stock FROM nonfood WHERE nonfood_name = %s", (item_name,))
                stock = sql_nonfood_get_cursor.fetchone()

                if stock and stock[0] <= 1:
                    lt_cleaning.itemconfig(selected_index, {"fg": "gray"})
                    lt_cleaning.select_clear(selected_index)

        #Pantry
        def on_select_pant(event):
            selected_indices = lt_pantry.curselection()

            if selected_indices:
                selected_index = selected_indices[0]
                selected_items = lt_pantry.get(selected_index)

                item_name = selected_items.split(" ")[0]

                sql_food_get_cursor.execute("SELECT stock FROM food WHERE food_name = %s", (item_name,))
                stock = sql_food_get_cursor.fetchone()

                if stock and stock[0] <= 1:
                    lt_pantry.itemconfig(selected_index, {"fg": "gray"})
                    lt_pantry.select_clear(selected_index)

        #beverages
        def on_select_bev(event):
            selected_indices = lt_beverages.curselection()

            if selected_indices:
                selected_index = selected_indices[0]
                selected_items = lt_beverages.get(selected_index)

                item_name = selected_items.split(" ")[0]

                sql_food_get_cursor.execute("SELECT stock FROM food WHERE food_name = %s", (item_name,))
                stock = sql_food_get_cursor.fetchone()

                if stock and stock[0] <= 1:
                    lt_beverages.itemconfig(selected_index, {"fg": "gray"})
                    lt_beverages.select_clear(selected_index)

        #school
        def on_select_sc(event):
            selected_indices = lt_school.curselection()

            if selected_indices:
                selected_index = selected_indices[0]
                selected_items = lt_school.get(selected_index)

                item_name = selected_items.split(" ")[0]

                sql_etc_get_cursor.execute("SELECT stock FROM etc WHERE etc_name = %s", (item_name,))
                stock = sql_etc_get_cursor.fetchone()

                if stock and stock[0] <= 1:
                    lt_school.itemconfig(selected_index, {"fg": "gray"})
                    lt_school.select_clear(selected_index)

        category = isle

        fr_item_view = Frame(root, bg="#47761E", width=700, height=700)
        fr_item_view.grid(row=3, column=6, sticky="e")

        lbl_item_view = Label(fr_item_view, highlightthickness=0, bd=5)
        lbl_item_view.grid(row=0, column=2)

        fr_order_cancel = Frame(root, bg="#47761E")
        fr_order_cancel.grid(row=4, column=1)

        #inigojones
        bt_select = Button(fr_order_cancel, image=background_selectpac,command=selection, highlightthickness=0, bd=4)
        bt_select.grid(row=5, column=2, sticky=W, pady=20, padx=10)

        bt_order = Button(fr_item_view, image=background_orderpac, highlightthickness=0, bd=4, command=add_order)

        if kwargs == admin_accounts:
            bt_order.destroy()

        bt_new = Button(fr_order_cancel, image=background_newpac ,command=new_isle, bd=4, highlightthickness=0)
        bt_new.grid(row=5, column=3, sticky=E, pady=20, padx=10)

        if category == "Laundry":

            sql_nonfood_get_cursor = main_connection.cursor()

            sql_nonfood_get_cursor.execute("SELECT nonfood_name, stock FROM nonfood")
            sql_nonfood_stock = sql_nonfood_get_cursor.fetchall()

            if lt_laundry.size() == 0:
                for item in lt_laundry_values:
                    lt_laundry.insert(END, item)
            elif lt_laundry_values not in lt_laundry.get(0, END):
                for items in lt_laundry_values:
                    if items not in lt_laundry.get(0, END):
                        lt_laundry.insert(END, items)

            disable_items = []
            for id, (name, stock) in enumerate(sql_nonfood_stock):
                if stock <= 1:
                    disable_items.append(id)

            #otids na
            lt_laundry.grid(row=3, column=0)
            #lt_laundry.config(height=lt_laundry.size())
            lt_laundry.bind("<<ListboxSelect>>", on_select_lnd)
            lt_scrollbar.grid(row=3, column=1)

            lt_laundry.config(yscrollcommand=lt_scrollbar.set)
            bt_pantry_cat.config(state=DISABLED)
            bt_bev_cat.config(state=DISABLED)
            bt_cl_cat.config(state=DISABLED)
            bt_sc_cat.config(state=DISABLED)

        if category == "Pantry":

            sql_food_get_cursor = main_connection.cursor()

            sql_food_get_cursor.execute("SELECT food_name, stock FROM food")
            sql_food_stock = sql_food_get_cursor.fetchall()

            if lt_pantry.size() == 0:
                for item in lt_pantry_values:
                    lt_pantry.insert(END, item)
            elif lt_pantry_values not in lt_pantry.get(0, END):
                for items in lt_pantry_values:
                    if items not in lt_pantry.get(0, END):
                        lt_pantry.insert(END, items)

            disable_items_pant = []
            for id, (name, stock) in enumerate(sql_food_stock):
                if stock <= 1:
                    if name in lt_pantry_values:
                        disable_items_pant.append(id)

            lt_pantry.grid(row=3, column=0)
            #lt_pantry.config(height=lt_pantry.size())
            lt_pantry.bind("<<ListboxSelect>>", on_select_pant)
            lt_scrollbar.grid(row=3, column=1)

            lt_pantry.config(yscrollcommand=lt_scrollbar.set)
            lt_scrollbar.config(command=lt_pantry.yview)

            bt_laundry_cat.config(state=DISABLED)
            bt_bev_cat.config(state=DISABLED)
            bt_cl_cat.config(state=DISABLED)
            bt_sc_cat.config(state=DISABLED)

        if category == "Beverages":

            sql_food_get_cursor = main_connection.cursor()

            sql_food_get_cursor.execute("SELECT food_name, stock FROM food")
            sql_food_stock = sql_food_get_cursor.fetchall()

            if lt_beverages.size() == 0:
                for item in lt_beverages_values:
                    lt_beverages.insert(END, item)
            elif lt_beverages_values not in lt_beverages.get(0, END):
                for item in lt_beverages_values:
                    if item not in lt_beverages.get(0, END):
                        lt_beverages.insert(END, item)

            disable_items_bev = []
            for id, (name, stock) in enumerate(sql_food_stock):
                if stock <= 1:
                    if name in lt_beverages_values:
                        disable_items_bev.append(id)

            lt_beverages.grid(row=3, column=0)
            #lt_beverages.config(height=lt_beverages.size())
            lt_beverages.bind("<<ListboxSelect>>", on_select_bev)
            lt_scrollbar.grid(row=3, column=1)

            lt_beverages.config(yscrollcommand=lt_scrollbar.set)
            lt_scrollbar.config(command=lt_beverages.yview)

            bt_cl_cat.config(state=DISABLED)
            bt_sc_cat.config(state=DISABLED)
            bt_laundry_cat.config(state=DISABLED)
            bt_pantry_cat.config(state=DISABLED)

        if category == "Cleaning":

            sql_nonfood_get_cursor = main_connection.cursor()

            sql_nonfood_get_cursor.execute("SELECT nonfood_name, stock FROM nonfood")
            sql_nonfood_stock = sql_nonfood_get_cursor.fetchall()

            if lt_cleaning.size() == 0:
                for item in lt_cleaning_values:
                    lt_cleaning.insert(END, item)
            elif lt_cleaning_values not in lt_cleaning.get(0, END):
                for item in lt_cleaning_values:
                    if item not in lt_cleaning.get(0, END):
                        lt_cleaning.insert(END, item)

            disable_items_cl = []
            for id, (name, stock) in enumerate(sql_nonfood_stock):

                if stock <= 1:
                    if name in lt_cleaning_values:
                        disable_items_cl.append(id)

            lt_cleaning.grid(row=3, column=0)
            #lt_cleaning.config(height=lt_cleaning.size())
            lt_cleaning.bind("<<ListboxSelect>>", on_select_cl)
            lt_scrollbar.grid(row=3, column=1)

            lt_cleaning.config(yscrollcommand=lt_scrollbar.set)
            lt_scrollbar.config(command=lt_cleaning.yview)

            bt_sc_cat.config(state=DISABLED)
            bt_laundry_cat.config(state=DISABLED)
            bt_pantry_cat.config(state=DISABLED)
            bt_bev_cat.config(state=DISABLED)

        if category == "SchoolSupplies":

            sql_etc_get_cursor = main_connection.cursor()

            sql_etc_get_cursor.execute("SELECT etc_name, stock FROM etc")
            sql_etc_stock = sql_etc_get_cursor.fetchall()

            if lt_school.size() == 0:
                for item in lt_school_values:
                    lt_school.insert(END, item)
            elif lt_school_values not in lt_school.get(0, END):
                for item in lt_school_values:
                    if item not in lt_school.get(0, END):
                        lt_school.insert(END, item)

            disable_items_sc = []
            for id, (name, stock) in enumerate(sql_etc_stock):
                if stock <= 1:
                    if name in lt_school_values:
                        disable_items_sc.append(id)

            lt_school.grid(row=3, column=0)
            #lt_school.config(height=lt_school.size())
            lt_school.bind("<<ListboxSelect>>", on_select_sc)
            lt_scrollbar.grid(row=3, column=1)

            lt_school.config(yscrollcommand=lt_scrollbar.set)
            lt_scrollbar.config(command=lt_school.yview)

            bt_laundry_cat.config(state=DISABLED)
            bt_pantry_cat.config(state=DISABLED)
            bt_bev_cat.config(state=DISABLED)
            bt_cl_cat.config(state=DISABLED)

    # RemoveItem
    def remove_item_food(location):

        def quantity_convert(quan_str):
            return int(quan_str.replace("x", ""))

        if location == "Food":
            if len(kwargs[username_main.get()]['Food']) == 0:
                messagebox.showerror(title="Empty na!", message="Your Food section is empty na!")
                return

        if location == "Non-Food":
            if len(kwargs[username_main.get()]['Non-Food']) == 0:
                messagebox.showerror(title="Empty na!", message="Your Non-Food section is empty na!")
                return
        if location == "Etc.":
            if len(kwargs[username_main.get()]['ETC.']) == 0:
                messagebox.showerror(title="Empty na!", message="Your Etc. section is empty na!")
                return

        remove_food = Toplevel()
        remove_food.title("Remove Item")
        remove_food.config(bg="#FD5E53")

        def remove():
            if location == "Food":
                if len(kwargs[username_main.get()]['Food']) == 0:
                    messagebox.showerror(title="Empty na!", message="Your Food section is empty na!")
                    return

                def remove_f_qua():
                    item_qua_minus = cb_food_qua.get()
                    total_item_qua = item_qua - int(item_qua_minus)

                    item_cost = float(next(iter(dict_all_orders[f"\n{item_name}"])))

                    if total_item_qua >= 1:
                        updated_qua = f"\n{item_name} x{total_item_qua}"

                        kwargs[username_main.get()]['Food'][item_select[0]] = updated_qua
                        kwargs[username_main.get()]['Orders'][item_select[0]] = updated_qua

                    else:

                        kwargs[username_main.get()]['Food'].pop(item_select[0])
                        kwargs[username_main.get()]['Orders'].pop(item_select[0])

                    kwargs[username_main.get()]['FoodCost'] -= (item_cost * int(item_qua_minus))
                    kwargs[username_main.get()]['Total'] -= (item_cost * int(item_qua_minus))

                    lt_remove_food.delete(0, END)

                    for item in kwargs[username_main.get()]['Food']:
                        lt_remove_food.insert(END, item)

                    lt_remove_food.config(height=lt_remove_food.size())
                    remove_food_qua.destroy()
                    remove_food.deiconify()

                def remove_f_can():
                    remove_food_qua.destroy()
                    remove_food.deiconify()

                remove_food.withdraw()

                item_select = lt_remove_food.curselection()
                item_information = lt_remove_food.get(item_select).strip().split()
                item_name = item_information[0]
                item_qua = quantity_convert(item_information[1])

                remove_food_qua = Toplevel(root)
                remove_food_qua.title("Remove Food Order")

                remove_food_qua.grab_set()

                lbl_remove_food_title = Label(remove_food_qua, text="|Remove Food quantity",
                                                 font="Georgia 20")
                lbl_remove_food_title.grid(row=0, column=0)

                lbl_remove_food_qua = Label(remove_food_qua, text="How much quantity : ", font="Georgia 15")
                lbl_remove_food_qua.grid(row=1, column=0)

                cb_food_qua_val = [x for x in range(1, item_qua + 1)]
                cb_food_qua = ttk.Combobox(remove_food_qua, values=cb_food_qua_val, width=15)
                cb_food_qua.grid(row=1, column=1)

                bt_food_qua = Button(remove_food_qua, text="Done", font="Georgia 10", bd=5, command=remove_f_qua)
                bt_food_qua.grid(row=2, column=1, sticky="nsew")

                bt_food_qua_can = Button(remove_food_qua, text="Cancel", font="Georgia 10", bd=5,
                                            command=remove_f_can)
                bt_food_qua_can.grid(row=2, column=2, sticky="nsew")

                remove_food_qua.wait_window()

            if location == "Non-Food":
                if len(kwargs[username_main.get()]['Non-Food']) == 0:
                    messagebox.showerror(title="Empty na!", message="Your Food section is empty na!")
                    remove_food.destroy()

                def remove_nf_qua():
                    item_qua_minus = cb_nonfood_qua.get()
                    total_item_qua = item_qua - int(item_qua_minus)

                    item_cost = float(next(iter(dict_all_orders[f"\n{item_name}"])))

                    if total_item_qua >= 1:
                        updated_qua = f"\n{item_name} x{total_item_qua}"

                        kwargs[username_main.get()]['Non-Food'][item_select[0]] = updated_qua
                        kwargs[username_main.get()]['Orders'][item_select[0]] = updated_qua

                    else:
                        kwargs[username_main.get()]['Non-Food'].pop(item_select[0])
                        kwargs[username_main.get()]['Orders'].pop(item_select[0])

                    kwargs[username_main.get()]['Non-FoodCost'] -= (item_cost * int(item_qua_minus))
                    kwargs[username_main.get()]['Total'] -= (item_cost * int(item_qua_minus))

                    lt_remove_non_food.delete(0, END)

                    for item in kwargs[username_main.get()]['Non-Food']:
                        lt_remove_non_food.insert(END, item)

                    lt_remove_non_food.config(height=lt_remove_non_food.size())
                    remove_nonfood_qua.destroy()
                    remove_food.deiconify()

                def remove_nf_can():
                    remove_nonfood_qua.destroy()
                    remove_food.deiconify()

                remove_food.withdraw()

                item_select = lt_remove_non_food.curselection()
                item_information = lt_remove_non_food.get(item_select).strip().split()
                item_name = item_information[0]
                item_qua = quantity_convert(item_information[1])

                remove_nonfood_qua = Toplevel(root)
                remove_nonfood_qua.title("Remove Non-Food Quantity")

                remove_nonfood_qua.grab_set()

                lbl_remove_nonfood_title = Label(remove_nonfood_qua, text="|Remove Non Food quantity", font="Georgia 20")
                lbl_remove_nonfood_title.grid(row=0, column=0)

                lbl_remove_nonfood_qua = Label(remove_nonfood_qua, text="How much quantity : ", font="Georgia 15")
                lbl_remove_nonfood_qua.grid(row=1, column=0)

                cb_nonfood_qua_val = [x for x in range(1, item_qua+1)]
                cb_nonfood_qua = ttk.Combobox(remove_nonfood_qua, values=cb_nonfood_qua_val, width=15)
                cb_nonfood_qua.grid(row=1, column=1)

                bt_nonfood_qua = Button(remove_nonfood_qua, text="Done", font="Georgia 10", bd=5, command=remove_nf_qua)
                bt_nonfood_qua.grid(row=2, column=1, sticky="nsew")

                bt_nonfood_qua_can = Button(remove_nonfood_qua, text="Cancel", font="Georgia 10", bd=5, command=remove_nf_can)
                bt_nonfood_qua_can.grid(row=2, column=2, sticky="nsew")

                remove_nonfood_qua.wait_window()

            if location == "Etc.":
                if len(kwargs[username_main.get()]['ETC.']) == 0:
                    messagebox.showerror(title="Empty na!", message="Your Food section is empty na!")
                    remove_food.destroy()

                def remove_etc_quan():
                    item_qua_minus = cb_etc_qua.get()
                    total_item_qua = item_qua - int(item_qua_minus)

                    item_cost = float(next(iter(dict_all_orders[f"\n{item_name}"])))

                    if total_item_qua >= 1:
                        updated_qua = f"\n{item_name} x{total_item_qua}"

                        kwargs[username_main.get()]['ETC.'][item_select[0]] = updated_qua
                        kwargs[username_main.get()]['Orders'][item_select[0]] = updated_qua

                    else:

                        kwargs[username_main.get()]['ETC.'].pop(item_select[0])
                        kwargs[username_main.get()]['Orders'].pop(item_select[0])

                    kwargs[username_main.get()]['EtcCost'] -= (item_cost * int(item_qua_minus))
                    kwargs[username_main.get()]['Total'] -= (item_cost * int(item_qua_minus))

                    lt_remove_etc.delete(0, END)

                    for item in kwargs[username_main.get()]['ETC.']:
                        lt_remove_etc.insert(END, item)

                    lt_remove_etc.config(height=lt_remove_etc.size())
                    remove_etc_qua.destroy()
                    remove_food.deiconify()

                def remove_etc_can():
                    remove_etc_qua.destroy()
                    remove_food.deiconify()

                remove_food.withdraw()

                item_select = lt_remove_etc.curselection()
                item_information = lt_remove_etc.get(item_select).strip().split()
                item_name = item_information[0]
                item_qua = quantity_convert(item_information[1])

                remove_etc_qua = Toplevel(root)
                remove_etc_qua.title("Remove ETC. Order")

                remove_etc_qua.grab_set()

                lbl_remove_etc_title = Label(remove_etc_qua, text="|Remove ETC. quantity",
                                                 font="Georgia 20")
                lbl_remove_etc_title.grid(row=0, column=0)

                lbl_remove_etc_qua = Label(remove_etc_qua, text="How much quantity : ", font="Georgia 15")
                lbl_remove_etc_qua.grid(row=1, column=0)

                cb_etc_qua_val = [x for x in range(1, item_qua + 1)]
                cb_etc_qua = ttk.Combobox(remove_etc_qua, values=cb_etc_qua_val, width=10)
                cb_etc_qua.grid(row=1, column=1)

                bt_etc_qua = Button(remove_etc_qua, text="Done", font="Georgia 10", bd=5, command=remove_etc_quan)
                bt_etc_qua.grid(row=2, column=1, sticky="nsew")

                bt_etc_qua_can = Button(remove_etc_qua, text="Cancel", font="Georgia 10", bd=5,
                                         command=remove_etc_can)
                bt_etc_qua_can.grid(row=2, column=2, sticky="nsew")

                remove_etc_qua.wait_window()

        fr_remove_food = Frame(remove_food, bg="#FD5E53")
        fr_remove_food.grid(row=1, column=0)

        if location == "Food":
            lbl_food = Label(fr_remove_food, text="| Food Items", font="Garamond 20", bg="#FD5E53", padx=20, pady=10)
            lbl_food.grid(row=0, column=0)

            lt_remove_food_value = []

            for val in kwargs[username_main.get()]['Food']:
                lt_remove_food_value.append(val)

            lt_remove_food = Listbox(fr_remove_food, font="Georgia 15",
                                     width=15, height=10,
                                     bg="beige",
                                     selectmode=NORMAL)

            for item in lt_remove_food_value:
                lt_remove_food.insert(END, item)
            lt_remove_food.grid(row=1, column=0)
            lt_remove_food.config(height=lt_remove_food.size())

        if location == "Non-Food":
            lbl_non_food = Label(fr_remove_food, text="| Non-Food Items", font="Garamond 20", padx=20, pady=10)
            lbl_non_food.grid(row=0, column=0)

            lt_remove_non_food_value = []

            for val in kwargs[username_main.get()]['Non-Food']:
                lt_remove_non_food_value.append(val)

            lt_remove_non_food = Listbox(fr_remove_food, font="Georgia 15",
                                         width=15, height=10,
                                         bg="beige",
                                         selectmode=NORMAL)

            for item in lt_remove_non_food_value:
                lt_remove_non_food.insert(END, item)
            lt_remove_non_food.grid(row=1, column=0)
            lt_remove_non_food.config(height=lt_remove_non_food.size())

        if location == "Etc.":
            lbl_etc = Label(fr_remove_food, text="| Etc. Items ", font="Garamond 20", padx=20, pady=10)
            lbl_etc.grid(row=0, column=0)

            lt_remove_etc_value = []

            for val in kwargs[username_main.get()]['ETC.']:
                lt_remove_etc_value.append(val)

            lt_remove_etc = Listbox(fr_remove_food, font="Georgia 15",
                                    width=15, height=10,
                                    bg="beige",
                                    selectmode=NORMAL)

            for item in lt_remove_etc_value:
                lt_remove_etc.insert(END, item)
            lt_remove_etc.grid(row=1, column=0)
            lt_remove_etc.config(height=lt_remove_etc.size())

        fr_bt_remove = Frame(remove_food, bg="#FD5E53")
        fr_bt_remove.grid(row=3, column=0)

        bt_remove = Button(fr_bt_remove, text="Remove", font="Garamond 10",
                           bg="#DC3545", activebackground="#DC3545",
                           fg="White", activeforeground="White",
                           padx=20, pady=10,
                           bd=5, relief=RAISED, command=remove)
        bt_remove.grid(row=3, column=0, sticky=W)

        bt_return = Button(fr_bt_remove, text="Return", font="Garamond 10",
                           bg="Green", activebackground="Green",
                           fg="White", activeforeground="White",
                           padx=20, pady=10,
                           bd=5, relief=RAISED, command=remove_food.destroy)
        bt_return.grid(row=3, column=1, sticky=E)

        remove_food.mainloop()

    # check balance
    def check_balance():
        messagebox.showinfo(title="Checking Balance..", message="Username : " + str(username_main.get()) + "\n______________________________\nCurrent Balance : $" + str(kwargs[username_main.get()]['Money']) + "\nCurrent Credits : $" + str(kwargs[username_main.get()]['Credit']) + "\n______________________________")

    #Show Orders Functions
    def show_order(location):
        ordered_foods = ""
        ordered_non_foods = ""
        etc_ordered = ""
        all_ordered_items = ""

        if location == "Food":
            if len(kwargs[username_main.get()]['Food']) == 0:
                messagebox.showerror(title="Empty!", message="Your Food Section is Empty!")
                return

            for item in kwargs[username_main.get()]['Food']:
                ordered_foods += f"\n{item}"

            messagebox.showinfo(title="Food Orders", message="[Foods]\n∙" + ordered_foods + "\n__________\n\n$" + str(kwargs[username_main.get()]['FoodCost']))

        if location == "Non-Food":
            if len(kwargs[username_main.get()]['Non-Food']) == 0:
                messagebox.showerror(title="Empty!", message="Your Non-Food Section is Empty!")
                return

            for item in kwargs[username_main.get()]["Non-Food"]:
                ordered_non_foods += f"\n{item}"

            messagebox.showinfo(title="Non-Food Orders", message="[Non-Foods]\n∙" + ordered_non_foods+ "\n__________\n\n$" + str(kwargs[username_main.get()]['Non-FoodCost']))

        if location == "Etc.":
            if len(kwargs[username_main.get()]['ETC.']) == 0:
                messagebox.showerror(title="Empty!", message="Your Etc. Section is Empty!")
                return

            for item in kwargs[username_main.get()]["ETC."]:
                etc_ordered += f"\n{item}"

            messagebox.showinfo(title="Etc.", message="[Etc.]\n∙" + etc_ordered + "\n__________\n\n$" + str(kwargs[username_main.get()]['EtcCost']))

        if location == "all":
            if len(kwargs[username_main.get()]['Orders']) == 0:
                messagebox.showerror(title="Empty!", message="Your Basket is Empty!")
                return

            for item in kwargs[username_main.get()]['Orders']:
                all_ordered_items += f"\n{item}"

            messagebox.showinfo(title="All Orders", message="[All Orders]\n∙" + all_ordered_items + "\n__________\n\n$" + str(kwargs[username_main.get()]['Total']))

    # Clear Functions
    def clear_orders(location):
        if location == "Food":
            if not kwargs[username_main.get()]['Food']:
                messagebox.showerror(title="Empty!", message="This is Empty!")
                return

            clear = messagebox.askyesno(title="Sure??", message="Are you sure you want to clear (All Food) items you ordered? ")

            if clear:
                for item_remove in kwargs[username_main.get()]['Food']:
                    kwargs[username_main.get()]['Orders'].remove(item_remove)

                kwargs[username_main.get()]['Food'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['FoodCost']
                kwargs[username_main.get()]['FoodCost'] = 0.0
            else:
                return

        if location == "Non-Food":
            if not kwargs[username_main.get()]['Non-Food']:
                messagebox.showerror(title="Empty!", message="This is Empty!")
                return

            clear = messagebox.askyesno(title="Sure??",
                                        message="Are you sure you want to clear (All Non-Food) items you ordered? ")

            if clear:
                for item_remove in kwargs[username_main.get()]['Non-Food']:
                    kwargs[username_main.get()]['Orders'].remove(item_remove)

                kwargs[username_main.get()]['Non-Food'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['Non-FoodCost']
                kwargs[username_main.get()]['Non-FoodCost'] = 0.0
            else:
                return

        if location == "Etc.":
            if not kwargs[username_main.get()]['ETC.']:
                messagebox.showerror(title="Empty!", message="This is Empty!")
                return

            clear = messagebox.askyesno(title="Sure??",
                                        message="Are you sure you want to clear (All Etc.) items you ordered? ")

            if clear:
                for item_remove in kwargs[username_main.get()]['ETC.']:
                    kwargs[username_main.get()]['Orders'].remove(item_remove)

                kwargs[username_main.get()]['ETC.'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['EtcCost']
                kwargs[username_main.get()]['EtcCost'] = 0.0
            else:
                return

        if location == "all":
            if not kwargs[username_main.get()]['Food'] or not kwargs[username_main.get()]['Non-Food'] or not kwargs[username_main.get()]['ETC.']:
                messagebox.showerror(title="Empty!", message="Your basket is so Empty! / Please clear the category you want not all of it!")
                return

            clear = messagebox.askyesno(title="Sure??",
                                        message="Are you sure you want to clear (All) the items you ordered? ")

            if clear:
                kwargs[username_main.get()]['Food'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['FoodCost']
                kwargs[username_main.get()]['FoodCost'] = 0.0

                kwargs[username_main.get()]['Non-Food'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['Non-FoodCost']
                kwargs[username_main.get()]['Non-FoodCost'] = 0.0

                kwargs[username_main.get()]['ETC.'].clear()
                kwargs[username_main.get()]['Total'] -= kwargs[username_main.get()]['EtcCost']
                kwargs[username_main.get()]['EtcCost'] = 0.0

                kwargs[username_main.get()]['Orders'].clear()
                kwargs[username_main.get()]['Total'] = 0.0

            else:
                return

    # Check-out
    def check_out():

        check_out_cursor = main_connection.cursor()
        sql_checkout_money = f"UPDATE {main_database['Table']} SET money = %s WHERE username = %s"
        sql_checkout_credits = f"UPDATE {main_database['Table']} SET credits = %s WHERE username = %s"
        order_date = datetime.now()

        #update stocks baby
        sql_stock_update_cursor = main_connection.cursor()
        sql_fstock_update = f"UPDATE food SET stock = %s WHERE food_name = %s"
        sql_nfstock_update = f"UPDATE nonfood SET stock = %s WHERE nonfood_name = %s"
        sql_etcstock_update = f"UPDATE etc SET stock = %s WHERE etc_name = %s"

        sql_stock_get_cursor = main_connection.cursor()
        sql_fstock_get = f"SELECT stock FROM food WHERE food_name = %s"
        sql_nfstock_get = f"SELECT stock FROM nonfood WHERE nonfood_name = %s"
        sql_etcstock_get = f"SELECT stock FROM etc WHERE etc_name = %s"

        #deliveries
        sql_delivery_cursor = main_connection.cursor()
        sql_delivery_insert = f"INSERT INTO delivery (username, address, contact, arrival_date, buy_date) values (%s, %s, %s, %s, NOW())"

        if len(kwargs[username_main.get()]['Orders']) == 0:
            messagebox.showerror(title="Empty!", message="Your Basket is Empty!")
            return

        choice = messagebox.askyesno(title="You sure?", message="Are you sure you want to check-out now? ")

        if choice:
            #root.withdraw()
            bill_out = Toplevel(root)
            bill_out.title("Bill-Out")
            bill_out.config(bg="#E6E6FA")

            bill_out.grab_set()

            ordered_items_food = ""
            ordered_items_non_food = ""
            ordered_items_etc = ""

            def credited_points(total_amount, credit_points, base_rate=10, bonus_points_threshold=250, bonus_rate=50):

                base_points = total_amount // base_rate

                bonus_points = bonus_rate if total_amount >= bonus_points_threshold else 0

                total_points = credit_points + base_points + bonus_points

                return total_points

            def delivery_week():
                today = datetime.now()
                next_week = today + timedelta(weeks=1)
                return next_week

            def return_baby():
                bill_out.destroy()

            def submit_payment():
                payment_method = cb_credit.get()
                service_method = cb_service.get()
                payment_input = txt_much.get()

                def new_start():
                    messagebox.showinfo(title="Welcome Back!", message=f"Welcome back {username_main.get()} !")
                    bill_out.destroy()
                    receipt_new.destroy()

                def end_game():
                    bill_out.destroy()
                    receipt_new.destroy()
                    before_reopen()

                def view_deliver():
                    messagebox.showinfo(title="Delivery Info", message=delivery_info)

                input_money = 0
                delivery_info = ""
                user_address = ""
                user_contact = ""

                try:
                    input_money = float(payment_input)
                except:
                    messagebox.showerror(title="Input money",message="Please make sure you input numbers!!!")
                    txt_much.delete(0, END)
                    return

                if payment_method == "Select a method.." or payment_method == "" or payment_method not in cb_credit['values']:
                    messagebox.showerror(title="Error!", message="Please select a proper method of payment.")
                    return

                if service_method == "Select a service.." or service_method == "" or service_method not in cb_service['values']:
                    messagebox.showerror(title="Error!", message="Please select a proper method of service.")
                    return

                if not payment_input.isdigit() or payment_input == "":
                    messagebox.showerror(title="Error!", message="Please input a designated amount!")
                    return

                if payment_method == "Cash":
                    if input_money < kwargs[username_main.get()]['Total'] or input_money > kwargs[username_main.get()]['Money']:
                        messagebox.showerror(title="Insufficient Balance", message="Seems like you're short. Please Make sure you are enough! (Also why not try credit?)")
                        txt_much.delete(0, END)
                        return

                    if service_method == "Delivery":

                        deliver = messagebox.askyesno(title="Delivery!",
                                                      message="If you want it delivered, it cost $150 delivery fee. Still want it? ")
                        if deliver:

                            def delivery_submit():

                                nonlocal input_money
                                nonlocal delivery_info
                                nonlocal user_address
                                nonlocal user_contact

                                user_address = txt_address.get()
                                user_contact = txt_contact.get()

                                delivery_info += f"Deliver to : {user_address}\nContact No. : {user_contact}\n__________\n\nExpected delivery arrival : {delivery_week()}\n"

                                if kwargs[username_main.get()]['Food']:
                                    for items in kwargs[username_main.get()]['Food']:
                                        product_order = items.strip().split()
                                        item_name = product_order[0]
                                        item_quantity = product_order[1]

                                        sql_stock_get_cursor.execute(sql_fstock_get, (item_name,))
                                        stock_items = sql_stock_get_cursor.fetchall()

                                        for row in stock_items:
                                            sql_f_value = ((row[0] - int(item_quantity[1:])), item_name)
                                            sql_stock_update_cursor.execute(sql_fstock_update, sql_f_value)

                                if kwargs[username_main.get()]['Non-Food']:
                                    for items in kwargs[username_main.get()]['Non-Food']:
                                        product_order_non = items.strip().split()
                                        item_name_non = product_order_non[0]
                                        item_quantity_non = product_order_non[1]

                                        sql_stock_get_cursor.execute(sql_fstock_get, (item_name_non,))
                                        stock_items_non = sql_stock_get_cursor.fetchall()

                                        for row in stock_items_non:
                                            sql_nf_value = ((row[0] - int(item_quantity_non[1:])), item_name_non)
                                            sql_stock_update_cursor.execute(sql_nfstock_update, sql_nf_value)

                                if kwargs[username_main.get()]['ETC.']:
                                    for items in kwargs[username_main.get()]['ETC.']:
                                        product_order_etc = items.strip().split()
                                        item_name_etc = product_order_etc[0]
                                        item_quantity_etc = product_order_etc[1]

                                        sql_stock_get_cursor.execute(sql_etcstock_get, (item_name_etc,))
                                        stock_items_etc = sql_stock_get_cursor.fetchall()

                                        for row in stock_items_etc:
                                            sql_etc_value = ((row[0] - int(item_quantity_etc[1:])), item_name_etc)
                                            sql_stock_update_cursor.execute(sql_etcstock_update, sql_etc_value)

                                kwargs[username_main.get()]['Total'] += 150

                                input_money += 150

                                kwargs[username_main.get()]['Money'] -= kwargs[username_main.get()]['Total']
                                sql_last_money = kwargs[username_main.get()]['Money']
                                sql_combine_last = (sql_last_money, username_main.get())

                                check_out_cursor.execute(sql_checkout_money, sql_combine_last)
                                main_connection.commit()
                                delivery.destroy()

                            estimated_sum = kwargs[username_main.get()]['Total']
                            estimated_sum += 150

                            if kwargs[username_main.get()]['Money'] < estimated_sum:
                                messagebox.showerror(title="Insufficient Balance!",
                                                     message="You don't have enough money for a delivery!")
                                return

                            delivery = Toplevel()
                            delivery.title("900x600")
                            delivery.config(bg="#47761E")

                            delivery.grab_set()

                            fr_deliver = Frame(delivery, bg="#47761E")
                            fr_deliver.grid(row=1, column=1)

                            lbl_deliver_title = Label(fr_deliver, text="| Delivery Info", font="Garamond 30", padx=20, bg="#47761E")
                            lbl_deliver_title.grid(row=0, column=0, sticky="nsew")

                            lbl_deliver_block = Label(fr_deliver, text="Address : ", font="Garamond 20", padx=20, bg="#47761E")
                            lbl_deliver_block.grid(row=1, column=0, sticky="nsew")

                            txt_address = Entry(fr_deliver, font="Garamond 20")
                            txt_address.grid(row=1, column=1, sticky="nsew")

                            lbl_contact = Label(fr_deliver, text="Enter your contact number : ", font="Garamond 20", bg="#47761E",
                                                padx=20)
                            lbl_contact.grid(row=2, column=0, sticky="nsew")

                            txt_contact = Entry(fr_deliver, font="Garamond 20")
                            txt_contact.grid(row=2, column=1, sticky="nsew")

                            bt_submit_deliver = Button(fr_deliver, text="Submit", font="Garamond 15", bd=5,
                                                       relief=RAISED, command=delivery_submit)
                            bt_submit_deliver.grid(row=3, column=1, sticky="ew")

                            delivery.wait_window()

                        else:
                            return

                    if service_method == "Take-out":

                        if kwargs[username_main.get()]['Food']:
                            for items in kwargs[username_main.get()]['Food']:
                                product_order = items.strip().split()
                                item_name = product_order[0]
                                item_quantity = product_order[1]

                                sql_stock_get_cursor.execute(sql_fstock_get, (item_name,))
                                stock_items = sql_stock_get_cursor.fetchall()

                                for row in stock_items:
                                    sql_f_value = ((row[0] - int(item_quantity[1:])), item_name)
                                    sql_stock_update_cursor.execute(sql_fstock_update, sql_f_value)

                        if kwargs[username_main.get()]['Non-Food']:
                            for items in kwargs[username_main.get()]['Non-Food']:
                                product_order_non = items.strip().split()
                                item_name_non = product_order_non[0]
                                item_quantity_non = product_order_non[1]

                                sql_stock_get_cursor.execute(sql_nfstock_get, (item_name_non,))
                                stock_items_non = sql_stock_get_cursor.fetchall()

                                for row in stock_items_non:
                                    sql_nf_value = ((row[0] - int(item_quantity_non[1:])), item_name_non)
                                    sql_stock_update_cursor.execute(sql_nfstock_update, sql_nf_value)

                        if kwargs[username_main.get()]['ETC.']:
                            for items in kwargs[username_main.get()]['ETC.']:
                                product_order_etc = items.strip().split()
                                item_name_etc = product_order_etc[0]
                                item_quantity_etc = product_order_etc[1]

                                sql_stock_get_cursor.execute(sql_etcstock_get, (item_name_etc,))
                                stock_items_etc = sql_stock_get_cursor.fetchall()

                                for row in stock_items_etc:
                                    sql_etc_value = ((row[0] - int(item_quantity_etc[1:])), item_name_etc)
                                    sql_stock_update_cursor.execute(sql_etcstock_update, sql_etc_value)

                        kwargs[username_main.get()]['Money'] -= kwargs[username_main.get()]['Total']
                        sql_last_money_takeout = kwargs[username_main.get()]['Money']
                        sql_combine_takeout = (sql_last_money_takeout, username_main.get())

                        check_out_cursor.execute(sql_checkout_money, sql_combine_takeout)
                        main_connection.commit()

                if payment_method == "Credit":
                    if input_money < kwargs[username_main.get()]['Total'] or input_money > kwargs[username_main.get()]['Credit']:
                        messagebox.showerror(title="Insufficient Balance", message="Seems like you're short. Please Make sure you are enough! (Also why not try cash?)")
                        txt_much.delete(0, END)
                        return

                    if service_method == "Delivery":

                        deliver = messagebox.askyesno(title="Delivery!", message="If you want it delivered, it cost $150 delivery fee. Still want it? ")

                        if deliver:

                            def deliver_submit_cr():

                                nonlocal input_money
                                nonlocal delivery_info
                                nonlocal user_address
                                nonlocal user_contact

                                user_address = txt_address_cr.get()
                                user_contact = txt_contact_cr.get()

                                delivery_info += f"Deliver to : {user_address}\nContact No. : {user_contact}\n__________\n\nExpected delivery arrival : {delivery_week()}\n"

                                if kwargs[username_main.get()]['Food']:
                                    for items in kwargs[username_main.get()]['Food']:
                                        product_order = items.strip().split()
                                        item_name = product_order[0]
                                        item_quantity = product_order[1]

                                        sql_stock_get_cursor.execute(sql_fstock_get, (item_name,))
                                        stock_items = sql_stock_get_cursor.fetchall()

                                        for row in stock_items:
                                            sql_f_value = ((row[0] - int(item_quantity[1:])), item_name)
                                            sql_stock_update_cursor.execute(sql_fstock_update, sql_f_value)

                                if kwargs[username_main.get()]['Non-Food']:
                                    for items in kwargs[username_main.get()]['Non-Food']:
                                        product_order_non = items.strip().split()
                                        item_name_non = product_order_non[0]
                                        item_quantity_non = product_order_non[1]

                                        sql_stock_get_cursor.execute(sql_fstock_get, (item_name_non,))
                                        stock_items_non = sql_stock_get_cursor.fetchall()

                                        for row in stock_items_non:
                                            sql_nf_value = ((row[0] - int(item_quantity_non[1:])), item_name_non)
                                            sql_stock_update_cursor.execute(sql_nfstock_update, sql_nf_value)

                                if kwargs[username_main.get()]['ETC.']:
                                    for items in kwargs[username_main.get()]['ETC.']:
                                        product_order_etc = items.strip().split()
                                        item_name_etc = product_order_etc[0]
                                        item_quantity_etc = product_order_etc[1]

                                        sql_stock_get_cursor.execute(sql_etcstock_get, (item_name_etc,))
                                        stock_items_etc = sql_stock_get_cursor.fetchall()

                                        for row in stock_items_etc:
                                            sql_etc_value = ((row[0] - int(item_quantity_etc[1:])), item_name_etc)
                                            sql_stock_update_cursor.execute(sql_etcstock_update, sql_etc_value)

                                kwargs[username_main.get()]['Total'] += 150

                                input_money += 150

                                kwargs[username_main.get()]['Credit'] -= kwargs[username_main.get()]['Total']
                                sql_credit_delivery = kwargs[username_main.get()]['Credit']
                                sql_combine_delivery = (sql_credit_delivery, username_main.get())

                                check_out_cursor.execute(sql_checkout_credits, sql_combine_delivery)
                                main_connection.commit()
                                delivery_credits.destroy()

                            estimated_sum = kwargs[username_main.get()]['Total']
                            estimated_sum += 150

                            if kwargs[username_main.get()]['Credit'] < estimated_sum:
                                messagebox.showerror(title="Insufficient Balance!",
                                                     message="You don't have enough money for a delivery!")
                                return

                            delivery_credits = Toplevel()
                            delivery_credits.title("900x600")
                            delivery_credits.config(bg="#47761E")

                            delivery_credits.grab_set()

                            fr_deliver_cr = Frame(delivery_credits, bg="#47761E")
                            fr_deliver_cr.grid(row=1, column=1)

                            lbl_delivercr_title = Label(fr_deliver_cr, text="| Delivery Info", font="Garamond 30", padx=20,
                                                      bg="#47761E")
                            lbl_delivercr_title.grid(row=0, column=0, sticky="nsew")

                            lbl_delivercr_block = Label(fr_deliver_cr, text="Address : ", font="Garamond 20", padx=20,
                                                      bg="#47761E")
                            lbl_delivercr_block.grid(row=1, column=0, sticky="nsew")

                            txt_address_cr = Entry(fr_deliver_cr, font="Garamond 20")
                            txt_address_cr.grid(row=1, column=1, sticky="nsew")

                            lbl_contact_cr = Label(fr_deliver_cr, text="Enter your contact number : ", font="Garamond 20",
                                                bg="#47761E",
                                                padx=20)
                            lbl_contact_cr.grid(row=2, column=0, sticky="nsew")

                            txt_contact_cr = Entry(fr_deliver_cr, font="Garamond 20")
                            txt_contact_cr.grid(row=2, column=1, sticky="nsew")

                            bt_submit_deliver_cr = Button(fr_deliver_cr, text="Submit", font="Garamond 15", bd=5,
                                                       relief=RAISED, command=deliver_submit_cr)
                            bt_submit_deliver_cr.grid(row=3, column=1, sticky="ew")

                            delivery_credits.wait_window()

                        else:
                            return

                    if service_method == "Take-out":

                        if kwargs[username_main.get()]['Food']:
                            for items in kwargs[username_main.get()]['Food']:
                                product_order = items.strip().split()
                                item_name = product_order[0]
                                item_quantity = product_order[1]

                                sql_stock_get_cursor.execute(sql_fstock_get, (item_name,))
                                stock_items = sql_stock_get_cursor.fetchall()

                                for row in stock_items:
                                    sql_f_value = ((row[0] - int(item_quantity[1:])), item_name)
                                    sql_stock_update_cursor.execute(sql_fstock_update, sql_f_value)

                        if kwargs[username_main.get()]['Non-Food']:
                            for items in kwargs[username_main.get()]['Non-Food']:
                                product_order_non = items.strip().split()
                                item_name_non = product_order_non[0]
                                item_quantity_non = product_order_non[1]

                                sql_stock_get_cursor.execute(sql_fstock_get, (item_name_non,))
                                stock_items_non = sql_stock_get_cursor.fetchall()

                                for row in stock_items_non:
                                    sql_nf_value = ((row[0] - int(item_quantity_non[1:])), item_name_non)
                                    sql_stock_update_cursor.execute(sql_nfstock_update, sql_nf_value)

                        if kwargs[username_main.get()]['ETC.']:
                            for items in kwargs[username_main.get()]['ETC.']:
                                product_order_etc = items.strip().split()
                                item_name_etc = product_order_etc[0]
                                item_quantity_etc = product_order_etc[1]

                                sql_stock_get_cursor.execute(sql_etcstock_get, (item_name_etc,))
                                stock_items_etc = sql_stock_get_cursor.fetchall()

                                for row in stock_items_etc:
                                    sql_etc_value = ((row[0] - int(item_quantity_etc[1:])), item_name_etc)
                                    sql_stock_update_cursor.execute(sql_etcstock_update, sql_etc_value)

                        kwargs[username_main.get()]['Credit'] -= kwargs[username_main.get()]['Total']
                        sql_credit_takeout = kwargs[username_main.get()]['Credit']
                        sql_combine_takeout_credit = (sql_credit_takeout, username_main.get())

                        check_out_cursor.execute(sql_checkout_credits, sql_combine_takeout_credit)
                        main_connection.commit()

                food_items = ", ".join(kwargs[username_main.get()]['Food'])
                non_food_items = ", ".join(kwargs[username_main.get()]['Non-Food'])
                etc_items = ", ".join(kwargs[username_main.get()]['ETC.'])
                total_amount = kwargs[username_main.get()]['Total']
                payment_method = cb_credit.get()
                service_method = cb_service.get()

                formatted_date = order_date.strftime("%Y-%m-%d %H:%M:%S")
                sql_insert_order = """
                            INSERT INTO check_out_order (username, food_items, non_food_items, etc_items, total_amount, payment_method, service_method, order_time)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                            """
                order_data = (
                username_main.get(), food_items, non_food_items, etc_items, total_amount, payment_method, service_method)

                if service_method == "Delivery":

                    delivery_date = (username_main.get(), user_address, user_contact, delivery_week())

                    sql_delivery_cursor.execute(sql_delivery_insert, delivery_date)

                check_out_cursor.execute(sql_insert_order, order_data)
                main_connection.commit()

                # History Receipt
                for items in kwargs[username_main.get()]['Food']:
                    kwargs[username_main.get()]['OrderHistoryFood'].append(items)

                for items in kwargs[username_main.get()]['Non-Food']:
                    kwargs[username_main.get()]['OrderHistoryNon-Food'].append(items)

                for items in kwargs[username_main.get()]['ETC.']:
                    kwargs[username_main.get()]['OrderHistoryEtc.'].append(items)

                kwargs[username_main.get()]['TotalHistory'] = kwargs[username_main.get()]['Total']

                receipt_new = Toplevel()
                receipt_new.title("Receipt")
                receipt_new.config(bg="#E6E6FA")

                receipt_new.grab_set()

                fr_receipt = Frame(receipt_new, bg="#E6E6FA")
                fr_receipt.grid(row=1, column=1)

                lbl_receipt_title = Label(fr_receipt, text=f"| Thankyou for Trusting, {username_main.get()}!!",
                                         font="Garamond 17", bg="#E6E6FA", padx=20, pady=10)
                lbl_receipt_title.grid(row=0, column=0)

                lbl_receipt_food = Label(fr_receipt, bg="#E6E6FA", text=f"Food items ordered:{ordered_items_food}", font="Georgia 10",
                                    padx=20, pady=10)
                lbl_receipt_food.grid(row=1, column=0)

                lbl_receipt_non_food = Label(fr_receipt, bg="#E6E6FA", text=f"Non-Food items ordered:{ordered_items_non_food}",
                                         font="Georgia 10",
                                         padx=20, pady=10)
                lbl_receipt_non_food.grid(row=1, column=1)

                lbl_receipt_etc = Label(fr_receipt, bg="#E6E6FA", text=f"Etc. items ordered:{ordered_items_etc}",
                                         font="Georgia 10",
                                         padx=20, pady=10)
                lbl_receipt_etc.grid(row=1, column=2)

                # CreditPoints Earned!
                points_rate = 10
                bonus_threshold = 250
                bonus_points = 50

                earned_points = credited_points(kwargs[username_main.get()]['Total'], kwargs[username_main.get()]['Credit'], points_rate, bonus_threshold, bonus_points)
                kwargs[username_main.get()]['Credit'] = earned_points
                sql_credit_points = kwargs[username_main.get()]['Credit']
                sql_credit_combine = (sql_credit_points, username_main.get())

                check_out_cursor.execute(sql_checkout_credits, sql_credit_combine)
                main_connection.commit()

                change = round(input_money - kwargs[username_main.get()]['Total'], 2)

                lbl_end_receipt = Label(fr_receipt, bg="#E6E6FA",
                                        text=f"\n________________________________________________\nChange : ${change}\nTotal Purchased : ${str(kwargs[username_main.get()]['Total'])}\n\nOrdered Date : {formatted_date}\nTotal Credits earned : {earned_points}",
                                        font="Georiga 15", padx=20, pady=10)
                lbl_end_receipt.grid(row=2, column=1)

                fr_new_end = Frame(receipt_new, bg="#E6E6FA")
                fr_new_end.grid(row=3, column=1)

                bt_deliver_info = Button(fr_new_end, text="View Delivery Info",
                                         font="Garamond 15", bd=5, relief=RAISED, command=view_deliver, bg="green")

                if service_method == "Delivery":
                    bt_deliver_info.grid(row=3, column=4, sticky="ew")

                bt_new_start = Button(fr_new_end, text="Order Again?", font="Georgia 15", bg="#72C3DC",
                                      bd=5, relief=RAISED, command=new_start)
                bt_new_start.grid(row=3, column=2, sticky="ew")

                bt_end = Button(fr_new_end, text="Exit", font="Georgia 15", bg="#1B2A49",
                                      bd=5, relief=RAISED, command=end_game)
                bt_end.grid(row=3, column=3, sticky="ew")

                kwargs[username_main.get()]['Food'].clear()
                kwargs[username_main.get()]['Non-Food'].clear()
                kwargs[username_main.get()]['ETC.'].clear()
                kwargs[username_main.get()]['Orders'].clear()
                kwargs[username_main.get()]['FoodCost'] = 0.0
                kwargs[username_main.get()]['Non-FoodCost'] = 0.0
                kwargs[username_main.get()]['EtcCost'] = 0.0
                kwargs[username_main.get()]['Total'] = 0.0

                receipt_new.wait_window()

            for item in kwargs[username_main.get()]['Food']:
                ordered_items_food += f"\n-{item}"

            for item in kwargs[username_main.get()]['Non-Food']:
                ordered_items_non_food += f"\n-{item}"

            for item in kwargs[username_main.get()]['ETC.']:
                ordered_items_etc += f"\n-{item}"

            fr_order = Frame(bill_out, bg="#E6E6FA")
            fr_order.grid(row=1, column=1)

            lbl_orders_food = Label(fr_order, bg="#E6E6FA", text=f"Food items ordered:{ordered_items_food}", font="Georgia 10",
                                    padx=20, pady=10)
            lbl_orders_food.grid(row=1, column=1)

            lbl_orders_non_food = Label(fr_order, bg="#E6E6FA", text=f"Non-Food items ordered:{ordered_items_non_food}", font="Georgia 10",
                                    padx=20, pady=10)
            lbl_orders_non_food.grid(row=1, column=2)

            lbl_orders_etc = Label(fr_order, bg="#E6E6FA", text=f"Etc. items ordered:{ordered_items_etc}", font="Georgia 10",
                                    padx=20, pady=10)
            lbl_orders_etc.grid(row=1, column=3)

            lbl_total_cost = Label(fr_order, bg="#E6E6FA", text=f"\n__________________________________________________\n Total : ${str(kwargs[username_main.get()]['Total'])}")
            lbl_total_cost.grid(row=2, column=2)

            fr_pay = Frame(bill_out, bg="#E6E6FA")
            fr_pay.grid(row=4, column=1)

            lbl_much = Label(fr_pay, bg="#E6E6FA", text="Please enter the amount of payment : ", font="Georgia 15",
                             padx=20, pady=10)
            lbl_much.grid(row=3, column=0)

            txt_much = Entry(fr_pay)
            txt_much.grid(row=3, column=1)

            lbl_balance = Label(fr_pay, font="Georgia 8", bg="#E6E6FA", padx=20, pady=10, text=f"Total Cash : {str(kwargs[username_main.get()]['Money'])}\nTotal Credits : {str(kwargs[username_main.get()]['Credit'])}")
            lbl_balance.grid(row=3, column=2)

            lbl_credit = Label(fr_pay, bg="#E6E6FA", text="Please Choose method of payment : ", font="Georgia 15",
                               padx=20, pady=10)
            lbl_credit.grid(row=4, column=0)

            cb_credit_var = StringVar()
            cb_credit_value = ["Select a method..", "Cash", "Credit"]
            cb_credit = ttk.Combobox(fr_pay, width=15, values=cb_credit_value, textvariable=cb_credit_var)
            cb_credit.current(0)
            cb_credit.grid(row=4, column=1)

            lbl_service = Label(fr_pay, text="Please Choose a service method : ", font="Georgia 15",
                                padx=20, pady=10,bg="#E6E6FA")
            lbl_service.grid(row=5, column=0)

            cb_sevice_var = StringVar()
            cb_service_value = ["Select a service..", "Delivery", "Take-out"]
            cb_service = ttk.Combobox(fr_pay, width=15, values=cb_service_value, textvariable=cb_sevice_var)
            cb_service.current(0)
            cb_service.grid(row=5, column=1)

            bt_pay = Button(fr_pay, text="Submit Payment", font="Garamond 15", bg="#4CAF50",
                            bd=5, relief=RAISED, command=submit_payment)
            bt_pay.grid(row=6, column=1, sticky=W)

            bt_return = Button(fr_pay, text="Return", font="Garamond 15", bd=5, relief=RAISED, command=return_baby)
            bt_return.grid(row=6, column=2, sticky=E)

            bill_out.wait_window()

        else:
            return


    #deliveries (customer)
    def pending_deliveries():
        sql_delivery_cursor = main_connection.cursor()
        sql_delivery_query = f"SELECT order_id, address, contact, buy_date, arrival_date FROM delivery WHERE username = %s"
        sql_delivery_cursor.execute(sql_delivery_query, (username_main.get(),))
        sql_delivery = sql_delivery_cursor.fetchall()
        sql_deliver_pend = []

        if sql_delivery == 0:
            messagebox.showerror(title="Error!", message="No deliveries!")
            return

        for rows in sql_delivery:
            deliver_data = {"order_id": rows[0], "address": rows[1], "contact": rows[2],
                            "buy_date": rows[3], "arrival_date": rows[4]}
            sql_deliver_pend.append(deliver_data)

        deliver_pend_info = Toplevel(root)
        deliver_pend_info.title("| Deliveries")
        deliver_pend_info.geometry("800x470")
        deliver_pend_info.config(bg="#000000")

        pend_width = deliver_pend_info.winfo_screenwidth()
        pend_height = deliver_pend_info.winfo_screenheight()

        winpen_width = 800
        winpen_height = 470

        pos_x = (pend_width - winpen_width) // 2
        pos_y = (pend_height - winpen_height) // 2

        deliver_pend_info.geometry(f"{winpen_width}x{winpen_height}+{pos_x}+{pos_y}")

        deliver_pend_info.grab_set()

        lbl_deliver_title = Label(deliver_pend_info, text=" | Deliveries", fg="white", font="Garamond 20", bg="#000000")
        lbl_deliver_title.grid(row=0, column=0)

        fr_deliver = Frame(deliver_pend_info, bg="#a1822f")
        fr_deliver.grid(row=1, column=0)

        pend_text = Text(fr_deliver, width=60, height=20, wrap=WORD, font="Georgia 10")
        pend_text.grid(row=1, column=1, sticky="nsew")

        del_scroll = Scrollbar(fr_deliver, command=pend_text.yview, orient=VERTICAL)
        del_scroll.grid(row=1, column=2, sticky="ns")

        for delivers in sql_deliver_pend:
            pend_text.insert(END, f"Order ID : {delivers['order_id']} | "
                                 f"Address : {delivers['address']}\n | Contact No. : {delivers['contact']}\n Day bought : {delivers['buy_date']} | Arrival Date : {delivers['arrival_date']}\n\n")

        deliver_pend_info.grid_rowconfigure(2, weight=1)
        pend_text.config(yscrollcommand=del_scroll.set)

        bt_deliver_return = Button(deliver_pend_info, text="Return", font="Garamond 20", command=deliver_pend_info.destroy,
                                   bg="green")
        bt_deliver_return.grid(row=3, column=0, sticky="ew")

        deliver_pend_info.wait_window()

    #Purchase History
    def purchase_history():

        history = Toplevel(root)
        history.title("Previews Purchase")
        history.config(bg="#98FF98")
        history.geometry("800x470")

        history.grab_set()

        history_width = history.winfo_screenwidth()
        history_height = history.winfo_screenheight()

        winhis_width = 800
        winhis_height = 470

        pos_x = (history_width - winhis_width) // 2
        pos_y = (history_height - winhis_height) // 2

        history.geometry(f"{winhis_width}x{winhis_height}+{pos_x}+{pos_y}")

        sql_search_all_cursor_user = main_connection.cursor()
        sql_search_all_user = f"SELECT order_id, food_items, non_food_items, etc_items, total_amount, payment_method, service_method, order_time FROM check_out_order WHERE username = %s"
        sql_search_all_cursor_user.execute(sql_search_all_user, (username_main.get(),))
        sql_search_all_order_user = sql_search_all_cursor_user.fetchall()
        sql_all_orders_user = []

        for rows in sql_search_all_order_user:
            orders = {
                "order_id": rows[0],
                "food_order": rows[1], "nonfood_order": rows[2], "etc_order": rows[3],
                "total_amount": rows[4], "payment_method": rows[5], "service": rows[6], "order_date": rows[7]}
            sql_all_orders_user.append(orders)

        lbl_purchase_history = Label(history, text="| Purchase History", font="Garamond 20", bg="#98FF98")
        lbl_purchase_history.grid(row=0, column=0, sticky="nsew")

        fr_orders_user = Frame(history, bg="#98FF98")
        fr_orders_user.grid(row=1, column=1, sticky="nsew")

        order_text_user = Text(fr_orders_user, width=60, height=20, wrap=WORD, font="Georgia 10")
        order_text_user.grid(row=1, column=0, sticky="nsew")

        orders_scroll_user = Scrollbar(fr_orders_user, command=order_text_user.yview, orient=VERTICAL)
        orders_scroll_user.grid(row=1, column=1, sticky="ns")

        for orders in sql_all_orders_user:
            order_text_user.insert(END, f"Order Id : {orders['order_id']} "
                                   f"| Total amount : {orders['total_amount']}\n | Payment method : {orders['payment_method']} | Service method : {orders['service']}\n | Date ordered : {orders['order_date']}\n | Food orders : {orders['food_order']}\n | Non-food orders : {orders['nonfood_order']}\n | Etc orders : {orders['etc_order']}\n\n\n")

        history.grid_rowconfigure(0, weight=1)
        order_text_user.config(yscrollcommand=orders_scroll_user.set)

        bt_get_back = Button(fr_orders_user, text="Return", font="Garamond 20", bg="#FF6347",
                             padx=20, pady=10, bd=5, relief=RAISED, command=history.destroy)
        bt_get_back.grid(row=2, column=0, sticky="ew")
        history.wait_window()

    #Change Info (customer)
    def change_info():

        def update_acc():

            double_check = Toplevel()
            double_check.title("Confirmation..")
            double_check.config(bg="#000000")

            def confirm_pass():
                entered_pass = txt_pass_confirm.get()

                if entered_pass != kwargs[username_main.get()]['Password']:
                    messagebox.showerror(title="Opps!", message="Wrong password!")
                    return

                else:
                    double_check.destroy()

                    username_update = str_user.get()
                    password_update = str_pass.get()
                    old_username = username_main.get()

                    sql_update_cursor = main_connection.cursor()

                    sql_update_user = f"UPDATE {main_database['Table']} SET username = %s WHERE username = %s"
                    sql_update_pass = f"UPDATE {main_database['Table']} SET password = %s WHERE username = %s"
                    update_values_user = (username_update, username_main.get())
                    update_values_pass = (password_update, username_update)

                    if username_main.get() != username_update:
                        user_accounts[username_update] = user_accounts[username_main.get()]

                        kwargs[username_update] = kwargs.pop(username_main.get())

                        old_username = username_main.get()

                        sql_update_cursor.execute(sql_update_user, update_values_user)
                        username_main.set(username_update)

                        main_connection.commit()

                    if kwargs[username_main.get()]['Password'] != password_update:
                        user_accounts[username_main.get()]['Password'] = password_update

                        sql_update_cursor.execute(sql_update_pass, update_values_pass)
                        kwargs[username_update]['Password'] = password_update

                        main_connection.commit()

                    username_main.set(username_main.get())
                    str_pass.set(kwargs[username_update]['Password'])

                    messagebox.showinfo(title="Successfully Updated!", message="The update is successful!")
                    update_info.destroy()

            def confirm_return():
                double_check.destroy()

            lbl_enter_pass = Label(double_check, text="Confirmation", bg="#000000")
            lbl_enter_pass.grid(row=0, column=0)

            lbl_pass_confirm = Label(double_check, image=passground_twopac, highlightthickness=0, bd=0)
            lbl_pass_confirm.grid(row=1, column=0)

            txt_pass_confirm = Entry(double_check, font="Georgia 15", width=15)
            txt_pass_confirm.grid(row=1, column=1)

            bt_confirm = Button(double_check, image=background_donepac, highlightthickness=0, bd=5, command=confirm_pass)
            bt_confirm.grid(row=3, column=1)

            bt_confirm_cancel = Button(double_check, image=background_cancelpac, highlightthickness=0, bd=5, command=confirm_return)
            bt_confirm_cancel.grid(row=3, column=0)

            double_check.mainloop()

        def return_acc():
            update_info.destroy()

        update_info = Toplevel(root)
        update_info.title("Updating Info")
        update_info.config(bg="#000000")

        update_info.grab_set()

        lbl_title_update = Label(update_info, image=background_upppac, highlightthickness=0, bd=0)
        lbl_title_update.grid(row=0, column=0)

        lbl_current_user = Label(update_info, image=userground_twopac, highlightthickness=0, bd=0)
        lbl_current_user.grid(row=1, column=0)

        str_user = StringVar(value=username_main.get())
        txt_current_user = Entry(update_info, font='Georgia 15', textvariable=str_user)
        txt_current_user.grid(row=1, column=1)

        lbl_current_user = Label(update_info, image=passground_twopac, highlightthickness=0, bd=0)
        lbl_current_user.grid(row=2, column=0)

        str_pass = StringVar(value=kwargs[username_main.get()]['Password'])
        txt_current_user = Entry(update_info, font='Georgia 15', textvariable=str_pass, show="*")
        txt_current_user.grid(row=2, column=1)

        fr_bt_update = Frame(update_info, bg="#000000")
        fr_bt_update.grid(row=3, column=2)

        bt_update = Button(fr_bt_update, image=background_uppac, highlightthickness=0, bd=5, command=update_acc)
        bt_update.grid(row=0, column=2, padx=20, pady=10)

        bt_cancel = Button(fr_bt_update, image=background_cancelpac, highlightthickness=0, bd=5, command=return_acc)
        bt_cancel.grid(row=0, column=1, padx=20, pady=10)

        update_info.wait_window()

    #status updating
    def status_update():

        status = Toplevel(root)
        status.title("Update Status")
        status.grab_set()

        def status_up():

            if cb_switch_var.get() and current_status == "active":
                kwargs[username_main.get()]["Status"] = "inactive"
                sql_status_cursor.execute(sql_status_update, inactive)
                main_connection.commit()
                status.destroy()
            else:
                kwargs[username_main.get()]["Status"] = "active"
                sql_status_cursor.execute(sql_status_update, active)
                main_connection.commit()
                status.destroy()

        def return_stat():
            status.destroy()

        stat_width = status.winfo_screenwidth()
        stat_height = status.winfo_screenheight()

        windstat_width = 300
        windstat_height = 120

        pos_x = (stat_width - windstat_width) // 2
        pos_y = (stat_height - windstat_height) // 2

        status.geometry(f"{windstat_width}x{windstat_height}+{pos_x}+{pos_y}")

        sql_status_cursor = main_connection.cursor()
        sql_status_update = f"UPDATE customers SET status = %s WHERE username = %s"
        current_status = kwargs[username_main.get()]["Status"]
        inactive = ("inactive", username_main.get())
        active = ("active", username_main.get())

        lbl_status_title = Label(status, text="Status : ")
        lbl_status_title.grid(row=0, column=0)

        cb_switch_var = BooleanVar(value=False)
        bg_color = "green" if current_status == "active" else "red"

        cb_status_update = Checkbutton(status, text=current_status, bg=bg_color, fg="white", activeforeground="white", activebackground="Green",
        variable=cb_switch_var, font="Arial 12", width=10, height=2,indicatoron=False, command=status_up)
        cb_status_update.grid(row=1, column=2, sticky="nsew")

        bt_status_return = Button(status, image=background_cancelpac, bd=5, highlightthickness=0, command=return_stat)
        bt_status_return.grid(row=1, column=1, sticky="nsew")

        status.wait_window()

    #shopinfoi
    def shop_abouts():
        about = Toplevel()
        about.title("About 2PacSarShop")

        def db_done():
            sql_abt_query = f"DESCRIBE {main_database['Table']}"

            sql_abt_cursor.execute(sql_abt_query)
            sql_desc_fetch = sql_abt_cursor.fetchall()

            messagebox.showinfo(message=sql_desc_fetch)

        sql_abt_cursor = main_connection.cursor()

        fr_about = Frame(about, bg="#9888B7")
        fr_about.grid(row=1, column=1)

        lbl_about_title = Label(fr_about, bg="#9888B7", font="Georgia 10", padx=20, pady=10, text="| 2PacSarShop\n\n_________________________________________________________\n"
                                               "-Started as an dependent sari-store, living below means and thriving to success in order to obtain what is rightful!"
                                               "\n   Down to earth Store, through hard-ships and short-comings will prevail for the latter."
                                                "\n _________________________________________________________\n"
                                               "This Project presented has a total of near 1.5k line of codes.\n"
                                               "A sari-sari store shop, that's what our project is all about.\n"
                                               "This sariStore has a 2 way account systems (Administrator) and (User)."
                                               "\nWe just add a little changes about how sari-sari store works.\n"
                                               "To be completely honest the operation of this store is just pure intuitions so don't expect much. Thankyou!\n"
                                               "_____________________________________________________________________________\n"
                                               "Spread awareness to peers whom underestimated!!\n\nFor more info's:\nwww.2pacshakur.com/home")
        lbl_about_title.grid(row=1, column=0)

        bt_db_abt = Button(fr_about, text="Database Abouts", font="Garamond 15", padx=20, pady=10, bd=5, relief=RAISED, command=db_done)
        bt_db_abt.grid(row=2, column=1)

        about.mainloop()

    def group_members():
        group_mem = Toplevel()
        group_mem.title("Group Imperial : Sari-Sari Store")

        fr_group = Frame(group_mem, bg="#9888B7")
        fr_group.grid(row=1, column=1)

        lbl_group = Label(fr_group, bg="#9888B7", font="Georgia 10", padx=20, pady=10, text="| 2pacSariShop Founders\n"
                                         "___________________________________________________\n"
                                         "Members: \n"
                                         "∙Madrigal, Iñigo Jones A.\n"
                                         "∙Padit, Joshua\n"
                                         "∙Nacar, Cristian\n"
                                         "∙Imperial, Jhowen\n"
                                         "∙Reaño, Cristelle\n∙Royo, Austine\n"
                                         "___________________________________________________\n"
                                         "BSIT-2D (Group Imperial)")
        lbl_group.grid(row=1, column=0)

        group_mem.mainloop()

    about_us_menu = Menu(menu_bar, tearoff=0)
    about_us_menu.add_command(label="About Intentions", command=shop_abouts)
    about_us_menu.add_separator()
    about_us_menu.add_command(label="Group Members", command=group_members)

    account_menu = Menu(menu_bar, tearoff=0)

    if kwargs == admin_accounts:
        administrator_account()
        menu_bar.add_cascade(label="About us", menu=about_us_menu)
    else:
        user_orders_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Orders", menu=user_orders_menu)

        sub_show_basket_menu = Menu(user_orders_menu, tearoff=0)
        sub_show_basket_menu.add_command(label="Food", command=lambda: show_order("Food"))
        sub_show_basket_menu.add_command(label="Non-Food", command=lambda: show_order("Non-Food"))
        sub_show_basket_menu.add_command(label="Etc.", command=lambda: show_order("Etc."))
        sub_show_basket_menu.add_separator()
        sub_show_basket_menu.add_command(label="All Orders", command=lambda: show_order("all"))
        user_orders_menu.add_cascade(label="Show Basket", menu=sub_show_basket_menu)
        user_orders_menu.add_separator()

        sub_remove_menu = Menu(user_orders_menu, tearoff=0)
        user_orders_menu.add_cascade(label="Remove", menu=sub_remove_menu)
        sub_remove_menu.add_separator()
        sub_remove_menu.add_command(label="Remove item (Food)", command=lambda: remove_item_food("Food"))
        sub_remove_menu.add_command(label="Remove item (Non-Food)", command=lambda: remove_item_food("Non-Food"))
        sub_remove_menu.add_command(label="Remove item (Etc.)", command=lambda: remove_item_food("Etc."))

        clear_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Clear Basket", menu=clear_menu)
        clear_menu.add_command(label="Food", command=lambda: clear_orders("Food"))
        clear_menu.add_command(label="Non-Food", command=lambda: clear_orders("Non-Food"))
        clear_menu.add_command(label="Etc.", command=lambda: clear_orders("Etc."))
        clear_menu.add_separator()
        clear_menu.add_command(label="Clear All", command=lambda: clear_orders("all"))

        account_menu.add_command(label="Check-Balance", command=check_balance)
        account_menu.add_command(label="Check-Purchase History", command=purchase_history)
        account_menu.add_command(label="Deliveries", command=pending_deliveries)
        account_menu.add_command(label="Update Info", command=change_info)
        account_menu.add_command(label="Status Update", command=status_update)

        menu_bar.add_cascade(label="About us", menu=about_us_menu)
        menu_bar.add_cascade(label="Account Settings", menu=account_menu)


    #account_menu.add_command(label="Log-out", command=before_reopen)

    lbl_title_store = Label(root, image=background_saripac, highlightthickness=0, bd=0)
    lbl_title_store.grid(row=0, column=1)

    fr_front = Frame(root, bg="#47761E")
    fr_front.grid(row=2, column=1)

    bt_laundry_cat = Button(fr_front, image=laundry_icon, command=lambda : category_check("Laundry"), highlightthickness=0, bd=0)
    bt_laundry_cat.grid(row=0, column=1, padx=20)

    bt_pantry_cat = Button(fr_front, image=pantry_icon, highlightthickness=0, bd=0,
                            command=lambda: category_check("Pantry"))
    bt_pantry_cat.grid(row=0, column=2, padx=20)

    bt_bev_cat = Button(fr_front, image=beverage_icon, bd=0, highlightthickness=0,
                            command=lambda: category_check("Beverages"))
    bt_bev_cat.grid(row=0, column=3, padx=20)

    bt_cl_cat = Button(fr_front, image=cl_icon, highlightthickness=0, bd=0,
                            command=lambda: category_check("Cleaning"))
    bt_cl_cat.grid(row=0, column=4, padx=20)

    bt_sc_cat = Button(fr_front, image=school_icon, bd=0, highlightthickness=0,
                            command=lambda: category_check("SchoolSupplies"))
    bt_sc_cat.grid(row=0, column=5, padx=20)

    bt_logout = Button(root, image=background_outpac, highlightthickness=0, bd=5, command=before_reopen)
    bt_logout.grid(row=0, column=6, sticky="e", padx=20, pady=10)

    if kwargs == user_accounts:
        bt_checkout = Button(root, image = background_checkpac, highlightthickness = 0, bd = 5,  command=check_out)
        bt_checkout.grid(row=0, column=5, sticky="e", padx=20, pady=10)

    lbl_bot = Label(root, text="2pacShakurSariShop@gmail.com", font="Georiga 9", fg="light gray", bg="#47761E",
                    padx=20, pady=10)
    lbl_bot.grid(row=10, column=5, sticky=S)

    # Listbox
    fr_lt_frame = Frame(root, bg="#47761E")
    fr_lt_frame.grid(row=3, column=1)

    lt_laundry = Listbox(fr_lt_frame, font="Georgia 20",
                         width=30,
                         height=10,
                         bg="#f3efca",
                         selectmode=NORMAL)

    lt_pantry = Listbox(fr_lt_frame, font="Georgia 20",
                        width=30,
                        height=10,
                        bg="#f3efca",
                        selectmode=NORMAL)

    lt_beverages = Listbox(fr_lt_frame, font="Georgia 20",
                           width=30,
                           height=10,
                           bg="#f3efca",
                           selectmode=NORMAL)

    lt_cleaning = Listbox(fr_lt_frame, font="Georgia 20",
                          width=30,
                          height=10,
                          bg="#f3efca",
                          selectmode=NORMAL)

    lt_school = Listbox(fr_lt_frame, font="Georgia 20",#15
                          width=30,
                          height=10,
                          bg="#f3efca",
                          selectmode=NORMAL)

    lt_scrollbar = Scrollbar(fr_lt_frame, orient=VERTICAL, command=lt_laundry.yview)

    root.mainloop()

#dito na baby (this part will focusing in sql query giving category for non_food items like (laundry, claening) in the sql para makuha yung specific na catergory bitch ahh)
# Items
sql_product_cursor = main_connection.cursor()

sql_product_cursor.execute(f"SELECT nonfood_name, nonfood_price, category FROM nonfood")
sql_nonfood = sql_product_cursor.fetchall()

sql_product_cursor.execute(f"SELECT food_name, food_price, category FROM food")
sql_food = sql_product_cursor.fetchall()

sql_product_cursor.execute(f"SELECT etc_name, etc_price, category FROM etc")
sql_etc = sql_product_cursor.fetchall()

lt_laundry_values = []
lt_cleaning_values = []
lt_pantry_values = []
lt_beverages_values = []
lt_school_values = []

for rows in sql_nonfood:
    if rows[2] == "Laundry":
        lt_laundry_values.append(f"{str(rows[0])}          ${rows[1]}")
    else:
        lt_cleaning_values.append(f"{str(rows[0])}          ${rows[1]}")


for rows in sql_food:
    if rows[2] == "Pantry":
        lt_pantry_values.append(f"{str(rows[0])}          ${rows[1]}")
    else:
        lt_beverages_values.append(f"{str(rows[0])}          ${rows[1]}")

for rows in sql_etc:
    lt_school_values.append(f"{str(rows[0])}          ${rows[1]}")

# lt_laundry_values = ["Wings          $29.00", "Pride          $100.00", "SurfFabcon          $20.00",
#                      "Ariel          $49.00", "Uppy          $59.00",
#                      "Lunox          $29.00", "Bathwash          $69.00"]

# lt_pantry_values = ["Gardenia          $30.00", "CocoLumber          $60.00",
#                     "ChocolateBread          $45.00", "GarlicBread          $75.00",
#                     "PandecocoExtreme          $89.00", "BavarianTasty          $90.00"]
#
# lt_beverages_values = ["Coke          $15.00", "Pepsi          $15.00",
#                        "Sprite          $15.00", "PocariSweat          $15.00",
#                        "RootBeer          $50.00", "JackDaniels          $200.00",
#                        "Emperador          $150.00", "Nestea          $5.00"]
#
# lt_cleaning_values = ["Mr.Muscles          $120.00", "Zonrox          $99.00",
#                       "SulfuricAcid          $200.00", "HydrogenMonoxide          $250.00",
#                       "Brush          $45.00", "ToiletCleaners          $90.00", "Molotov          $500.00"]
#
# lt_school_values = ["BallPoint          $2.00", "NoteBook          $3.00", "PadPaper          $2.00",
#                     "Marker          $4.00", "SprayPaint          $5.00"]

dict_all_orders = {"\nWings":29.00, "\nSurfFabcon":20.00, "\nAriel":49.00, "\nPride":100.00, "\nUppy":59.00, "\nLunox":29.00, "\nBathwash":69.00,
                        "\nGardenia":30.00, "\nCocoLumber":60.00, "\nChocolateBread":45.00, "\nGarlicBread":75.00, "\nPandecocoExtreme": 89.00, "\nBavarianTasty":90.00,
                        "\nCoke":15.00, "\nPepsi":15.00, "\nSprite":15.00, "\nPocariSweat":15.00, "\nRootBeer":50.00, "\nJackDaniels":200.00, "\nEmperador":150.00, "\nNestea":5.00,
                        "\nMr.Muscles":120.00, "\nZonrox":99.00, "\nSulfuricAcid":200.00, "\nHydrogenMonoxide":250.00, "\nBrush": 45.00, "\nToiletCleaners":90.00, "\nMolotov":500.00,
                   "\nBallPoint":2.00, "\nNoteBook":3.00, "\nPadPaper":2.00, "\nMarker":4.00, "\nSprayPaint":5.00}

#login phase
def sign_up():
    sign = Toplevel()
    sign.geometry("550x300")
    sign.title("Sign-Up")
    sign.config(bg="#000000")

    acc_cursor = main_connection.cursor()
    sql_add_acc = f"INSERT INTO {main_database['Table']} (username, Password, money, credits, status) values(%s, %s, %s, %s, %s)"

    def done():
        new_user = txt_new_user.get()
        new_password = txt_new_pass.get()
        new_pin = txt_new_pin.get()

        if len(new_pin) > 5:
            messagebox.showwarning(title="Too much!", message="Please be sure to only put 4 digit pin!")
            return

        try:
            new_pin = int(new_pin)

        except ValueError:
            messagebox.showerror(title="Wrong value pin!", message="Pin must contain digits/numbers only!")
            return

        sql_sign_cursor = main_connection.cursor()

        sql_sign_query = f"SELECT username, password FROM {main_database['Table']}"
        sql_sign_cursor.execute(sql_sign_query)
        sql_sign_all = sql_sign_cursor.fetchall()

        for rows in sql_sign_all:
            db_user[str(rows[0])] = str(rows[1])

        if new_user == "" or new_password == "" or new_pin == "":
            messagebox.showwarning(title="No username/password", message="Please fill out the form properly!")
            return

        if new_user in admin_accounts:
            messagebox.showwarning(title="Nope!", message="That's an admin account!")
            txt_new_user.delete(0, END)
            txt_new_pass.delete(0, END)
            return

        if new_user in user_accounts or new_user in db_user:
            messagebox.showwarning(title="Account already!", message="Account is already created! Try again")
            txt_new_user.delete(0, END)
            txt_new_pass.delete(0, END)
            return
        else:
            user_accounts[new_user] = {"Password": new_password,
                                       "Money": 1000.00,
                                       "Credit": 100.00,
                                       "Orders": [],
                                       "OrderHistoryFood": [],
                                       "OrderHistoryNon-Food": [],
                                       "OrderHistoryEtc.": [],
                                       "TotalHistory": 0.0,
                                       "Non-Food": [],
                                       "Non-FoodCost": 0.0,
                                       "Food": [],
                                       "FoodCost": 0.0,
                                       "ETC.": [],
                                       "EtcCost": 0.0,
                                       "Total": 0.0,
                                       "Status": "active",
                                       "Pin": new_pin}

            sql_acc_values = new_user, user_accounts[new_user]["Password"], user_accounts[new_user]["Money"], user_accounts[new_user]["Credit"], user_accounts[new_user]["Status"]

            acc_cursor.execute(sql_add_acc, sql_acc_values)
            main_connection.commit()

            messagebox.showinfo(title="Success!", message=f"You've successfully created an account! {new_user}")
            sign.destroy()

    def cancel():
        sign.destroy()

    sign_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\Signin font.png")
    twosign_pac = sign_pac.resize((100, 50), Image.Resampling.LANCZOS)
    signground_twopac = ImageTk.PhotoImage(twosign_pac)

    lbl_sign_title = Label(sign, image=signground_twopac, highlightthickness=0, bd=0)
    lbl_sign_title.grid(row=0, column=0, sticky="w", padx=20)

    lbl_new_user = Label(sign,
                         text="Enter your desired username : ",
                         font="Georgia 10",
                         padx=20, pady=10, bg="#000000", fg="#f3efca"
                         )
    lbl_new_user.grid(row=1, column=0)

    lbl_new_pass = Label(sign,
                         text="Enter your desired password : ",
                         font="Georgia 10",
                         padx=20, pady=20, bg="#000000", fg="#f3efca"
                         )
    lbl_new_pass.grid(row=2, column=0)

    txt_new_user = Entry(sign,
                         font="Georgia 10", bg="#f3efca"
                         )
    txt_new_user.grid(row=1, column=1)

    txt_new_pass = Entry(sign,
                         font="Georgia 10", bg="#f3efca"
                         )
    txt_new_pass.grid(row=2, column=1)

    lbl_new_pin = Label(sign,
                         text="Enter your desired pin (4 Digits only) : ",
                         font="Georgia 10",
                         padx=20, pady=20, bg="#000000", fg="#f3efca"
                         )
    lbl_new_pin.grid(row=3, column=0)

    txt_new_pin = Entry(sign,
                         font="Georgia 10", bg="#f3efca"
                         )
    txt_new_pin.grid(row=3, column=1)

    bt_sign_frame = Frame(sign, bg="#000000")
    bt_sign_frame.grid(row=4, column=1)

    bt_done = Button(bt_sign_frame, image=background_donepac,
                     command=done, highlightthickness=0, bd=0)
    bt_done.grid(row=4, column=2, sticky=W, padx=20)

    bt_cancel = Button(bt_sign_frame, image=background_cancelpac,
                       command=cancel, highlightthickness=0, bd=0)
    bt_cancel.grid(row=4, column=1, sticky=E, padx=20)

    sign.mainloop()


def log_in():
    log_username = txt_username.get()
    log_password = txt_password.get()

    log_count = login_count.get()

    sql_log_cursor = main_connection.cursor()
    sql_status_cursor = main_connection.cursor()

    sql_login_query = f"SELECT username, password, status, pin FROM {main_database['Table']}"
    sql_status_update = f"UPDATE {main_database['Table']} SET status = %s WHERE username = %s"
    sql_log_cursor.execute(sql_login_query)
    sql_login_all = sql_log_cursor.fetchall()
    sql_status_val = ('active', log_username)

    for rows in sql_login_all:
        db_user[str(rows[0])] = {"Password": str(rows[1]), "Status": str(rows[2]), "Pin": int(rows[3])}

    if log_username in admin_accounts and admin_accounts[log_username] == log_password:
        messagebox.showinfo(title="Welcome Admin!!", message=f"You've logged into administrator account!")
        login_count.set(0)
        main.withdraw()
        sari_store(**admin_accounts)

    if log_username in user_accounts and log_password == user_accounts[log_username]['Password'] or log_username in db_user and log_password == db_user[log_username]['Password']:

        if db_user[log_username]['Status'] == 'inactive':
            status_issue = messagebox.askyesnocancel(title="You're inactive",
                                                     message="You're account is inactive. If you want to reactivate it please click yes.")

            if status_issue:
                sql_status_cursor.execute(sql_status_update, sql_status_val)
                main_connection.commit()
            else:
                return

        messagebox.showinfo(title="Access Granted", message=f"Welcome  to 2pac's Sari store {txt_username.get()}!")
        login_count.set(0)
        main.withdraw()
        sari_store(**user_accounts)

    else:
        log_count += 1
        login_count.set(log_count)

        if log_count == 3:
            forgot = messagebox.askyesnocancel(title="Forgot your password?", message="Forgot your password?")

            if forgot:

                def forgot_done():

                    def new_passwow():
                        new_password = txt_new_forgot_pass.get()
                        sql_forgot_val = (new_password, user_forgot_name)

                        db_user[user_forgot_name]['Password'] = new_password
                        user_accounts[user_forgot_name]['Password'] = new_password
                        sql_forgot_cursor.execute(sql_forgot_pass, sql_forgot_val)
                        main_connection.commit()
                        login_count.set(0)
                        new_pass.destroy()
                        forgot_pass.destroy()

                    if not txt_user_pin.get() in db_user:
                        messagebox.showerror(title="username name error!", message="ooops! username doesn't match!")
                        txt_user_pin.delete(0, END)
                        return

                    if  int(txt_pin.get()) != db_user[txt_user_pin.get()]["Pin"]:
                        messagebox.showerror(title="Error!", message="Oopps! the pin doesn't match please try again!")
                        txt_pin.delete(0, END)
                        return

                    user_forgot_name = txt_user_pin.get()
                    user_pin = db_user[user_forgot_name]["Pin"]

                    sql_forgot_cursor = main_connection.cursor()
                    sql_forgot_pass = f"UPDATE customers SET password = %s WHERE username = %s"

                    new_pass = Toplevel()
                    new_pass.title("Enter new pass!")
                    new_pass.geometry("550x100")
                    new_pass.config(bg="#47761E")

                    n_width = new_pass.winfo_screenwidth()
                    n_height = new_pass.winfo_screenheight()

                    winn_width = 550
                    winn_height = 100

                    pos_x = (n_width - winn_width) // 2
                    pos_y = (n_height - winn_height) // 2

                    new_pass.geometry(f"{winn_width}x{winn_height}+{pos_x}+{pos_y}")

                    new_pass.grab_set()

                    lbl_new_forgot_pass = Label(new_pass, text="Enter new password : ", font="Garamond 20", padx=20, bg="#47761E")
                    lbl_new_forgot_pass.grid(row=0, column=0, sticky="nsew")

                    txt_new_forgot_pass = Entry(new_pass, font="Garamond 20")
                    txt_new_forgot_pass.grid(row=0, column=1)

                    bt_new_pass = Button(new_pass, text="Done", font="Garamond 20", padx=20, bd=5, relief=RAISED,
                                         command=new_passwow, bg="beige")
                    bt_new_pass.grid(row=1, column=1)

                    new_pass.wait_window()

                def forget_back():
                    login_count.set(0)
                    forgot_pass.destroy()

                forgot_pass = Toplevel(main)
                forgot_pass.title("Retrieving Password")
                forgot_pass.geometry("450x200")
                forgot_pass.config(bg="#47761E")

                forgot_pass.grab_set()

                f_width = forgot_pass.winfo_screenwidth()
                f_height = forgot_pass.winfo_screenheight()

                winf_width = 450
                winf_height = 150

                pos_x = (f_width - winf_width) // 2
                pos_y = (f_height - winf_height) // 2

                forgot_pass.geometry(f"{winf_width}x{winf_height}+{pos_x}+{pos_y}")

                lbl_user_pin = Label(forgot_pass, text="Enter your username : ", font="Garamond 20", padx=20,bg="#47761E")
                lbl_user_pin.grid(row=0, column=0, sticky="nsew")

                txt_user_pin = Entry(forgot_pass, font="Garamond 20", width=10)
                txt_user_pin.grid(row=0, column=1)

                lbl_pin = Label(forgot_pass, text="Enter your 4 digit pin : ", font="Garamond 20", padx=20, bg="#47761E")
                lbl_pin.grid(row=1, column=0, sticky="nsew")

                txt_pin = Entry(forgot_pass, font="Garamond 20", width=10)
                txt_pin.grid(row=1, column=1)

                fr_forgot = Frame(forgot_pass, bg="#47761E")
                fr_forgot.grid(row=2, column=1)

                bt_pin = Button(fr_forgot, text="Done", font="Garamond 15", bd=5, relief=RAISED, command=forgot_done, bg="beige")
                bt_pin.grid(row=2, column=1, sticky="e", pady=20)

                bt_pin_back = Button(fr_forgot, text="Return", font="Garamond 15", bd=5, relief=RAISED, command=forget_back, bg="red")
                bt_pin_back.grid(row=2, column=0, sticky="w", pady=20)

                forgot_pass.wait_window()

            else:
                login_count.set(0)
                return
        else:
            messagebox.showerror(title="Access Denied!", message="Access Denied, please make sure you know your account!")
            return


def exit_now():

    def back():
        exit_baby.destroy()

    def agree():
        main.destroy()
        exit_baby.quit()

    exit_baby = Toplevel(main)
    exit_baby.title("Now You're Leaving!!")
    exit_baby.geometry("870x570")
    exit_baby.config(bg="#000000")

    exit_baby.grab_set()

    exit_width = exit_baby.winfo_screenwidth()
    exit_height = exit_baby.winfo_screenheight()

    winex_width = 870
    winex_height = 570

    pos_x = (exit_width - winex_width) // 2
    pos_y = (exit_height - winex_height) // 2

    exit_baby.geometry(f"{winex_width}x{winex_height}+{pos_x}+{pos_y}")

    lbl_pac_bye = Label(exit_baby, text="Are you sure you want to leave??", font="Garamond 15", padx=20, bg="#000000", fg="white")
    lbl_pac_bye.grid(row=1, column=2, sticky="nsew", pady=30)

    lbl_pac_bye = Label(exit_baby, image=background_crypac)
    lbl_pac_bye.grid(row=0, column=2, sticky="nsew")

    lbl_pac_no = Button(exit_baby, image=background_nopac, command=agree)
    lbl_pac_no.grid(row=2, column=5, sticky=E)

    lbl_pac_yes = Button(exit_baby, image=background_yespac, command=back)
    lbl_pac_yes.grid(row=2, column=0, sticky=W)

    exit_baby.wait_window()

#cursors
table_create_cursor = main_connection.cursor()
sql_log_info_cursor = main_connection.cursor()

table_create_cursor.execute(sql_food_table_create)
table_create_cursor.execute(sql_nonfood_table_create)
table_create_cursor.execute(sql_etc_table_create)
main_database['Table'] = "customers"

#fetching orders
sql_login_elements = f"SELECT money, credits, Password, username, status FROM customers"
sql_log_info_cursor.execute(sql_login_elements)
sql_login_info = sql_log_info_cursor.fetchall()

sql_orders_cursor = main_connection.cursor()

#Insert ng mga orders pare
sql_orders_cursor.execute(sql_food_insert)
sql_orders_cursor.execute(sql_nonfood_insert)
sql_orders_cursor.execute(sql_etc_insert)

#Fetching ng orders pare
sql_food_elements = f"SELECT food_id, food_name, food_price from food"
sql_orders_cursor.execute(sql_food_elements)
sql_food_info = sql_orders_cursor.fetchall()

sql_nonfood_elements = f"SELECT nonfood_id, nonfood_name, nonfood_price from nonfood"
sql_orders_cursor.execute(sql_nonfood_elements)
sql_nonfood_info = sql_orders_cursor.fetchall()

sql_etc_elements = f"SELECT etc_id, etc_name, etc_price from etc"
sql_orders_cursor.execute(sql_etc_elements)
sql_etc_info = sql_orders_cursor.fetchall()

user_accounts['Select an account to remove..'] = {'Password': '(Default User Account)'}

for food in sql_food_info:
    dict_all_orders[str(f"\n{food[1]}")] = {float(food[2])}

for nonfood in sql_nonfood_info:
    dict_all_orders[str(f"\n{nonfood[1]}")] = {float(nonfood[2])}

for etc in sql_etc_info:
    dict_all_orders[str(f"\n{etc[1]}")] = {float(etc[2])}

for rows in sql_login_info:
    user_accounts[rows[3]] = {'Password': str(rows[2]), 'Money': float(rows[0]),
                              'Credit': float(rows[1]),
                              "Orders": [],
                              "OrderHistoryFood": [],
                              "OrderHistoryNon-Food": [],
                              "OrderHistoryEtc.": [],
                              "TotalHistory": 0.0,
                              "Non-Food": [],
                              "Non-FoodCost": 0.0,
                              "Food": [],
                              "FoodCost": 0.0,
                              "ETC.": [],
                              "EtcCost": 0.0,
                              "Total": 0.0,
                              "Status": str(rows[4])}
admin_accounts["admin"] = "123"
main_connection.commit()


main = Tk()
main.title("Log-in")
main.config(bg="#000000")
main.state("zoomed")

main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)

login_count = IntVar()

#Exit buttons
cry_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\cry.jpg")
twocry_pac = cry_pac.resize((450, 300), Image.Resampling.LANCZOS)
background_crypac = ImageTk.PhotoImage(twocry_pac)

yes_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\download (3).jpg")
twoyes_pac = yes_pac.resize((200, 200), Image.Resampling.LANCZOS)
background_yespac = ImageTk.PhotoImage(twoyes_pac)

no_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\download (2).jpg")
twono_pac = no_pac.resize((200, 200), Image.Resampling.LANCZOS)
background_nopac = ImageTk.PhotoImage(twono_pac)

#Done/Cancel Buttons
done_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\done.png")
twodone_pac = done_pac.resize((100, 50), Image.Resampling.LANCZOS)
background_donepac = ImageTk.PhotoImage(twodone_pac)

cancel_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\cancel.png")
twocancel_pac = cancel_pac.resize((100, 50), Image.Resampling.LANCZOS)
background_cancelpac = ImageTk.PhotoImage(twocancel_pac)

how_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\quantity howmany.png")
twohow_pac = how_pac.resize((200, 50), Image.Resampling.LANCZOS)
background_howpac = ImageTk.PhotoImage(twohow_pac)

up_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\update.png")
twoup_pac = up_pac.resize((100, 50), Image.Resampling.LANCZOS)
background_uppac = ImageTk.PhotoImage(twoup_pac)

upp_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\updateacc.png")
twoupp_pac = upp_pac.resize((200, 50), Image.Resampling.LANCZOS)
background_upppac = ImageTk.PhotoImage(twoupp_pac)

new_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\newcat.png")
twonew_pac = new_pac.resize((200, 100), Image.Resampling.LANCZOS)
background_newpac = ImageTk.PhotoImage(twonew_pac)

select_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\select.png")
twoselect_pac = select_pac.resize((150, 100), Image.Resampling.LANCZOS)
background_selectpac = ImageTk.PhotoImage(twoselect_pac)

order_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\addorder2.png")
twoorder_pac = order_pac.resize((350, 100), Image.Resampling.LANCZOS)
background_orderpac = ImageTk.PhotoImage(twoorder_pac)

pay_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pay.png")
twopay_pac = pay_pac.resize((150, 100), Image.Resampling.LANCZOS)
background_paypac = ImageTk.PhotoImage(twopay_pac)

check_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\checkout.png")
twocheck_pac = check_pac.resize((100, 50), Image.Resampling.LANCZOS)
background_checkpac = ImageTk.PhotoImage(twocheck_pac)

out_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\logout.png")
twoout_pac = out_pac.resize((100, 50), Image.Resampling.LANCZOS)
background_outpac = ImageTk.PhotoImage(twoout_pac)


#Laundry Items
surf_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\surf finale.jpg")
twosurf_pac = surf_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_surfpac = ImageTk.PhotoImage(twosurf_pac)

wings_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\wings finale.png")
twowings_pac = wings_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_wingspac = ImageTk.PhotoImage(twowings_pac)

lunox_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\lunox.jpg")
twolunox_pac = lunox_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_lunoxpac = ImageTk.PhotoImage(twolunox_pac)

uppy_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\uppy finale.png")
twouppy_pac = uppy_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_uppypac = ImageTk.PhotoImage(twouppy_pac)

bath_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\bathwash.jpg")
twobath_pac = bath_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_bathpac = ImageTk.PhotoImage(twobath_pac)

ariel_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\ariel.jpg")
twoariel_pac = ariel_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_arielpac = ImageTk.PhotoImage(twoariel_pac)

prid_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pride finale.jpg")
twoprid_pac = prid_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_pridpac = ImageTk.PhotoImage(twoprid_pac)

launque_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pac og.jpg")
twoquelaundry_pac = launque_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_laundryquepac = ImageTk.PhotoImage(twoquelaundry_pac)

#Pantry Items

garde_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\gard.jpg")
twogarde_pac = garde_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_gardepac = ImageTk.PhotoImage(twogarde_pac)

choco_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\chocobread.jpg")
twochoco_pac = choco_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_chocopac = ImageTk.PhotoImage(twochoco_pac)

bav_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\bavariantasty.jpg")
twobav_pac = bav_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_bavpac = ImageTk.PhotoImage(twobav_pac)

pan_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pandecoco.jpg")
twopan_pac = pan_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_panpac = ImageTk.PhotoImage(twopan_pac)

coco_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\Coco Bread.jpg")
twococo_pac = coco_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_cocopac = ImageTk.PhotoImage(twococo_pac)

gar_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\garlicbread.jpg")
twogar_pac = gar_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_garpac = ImageTk.PhotoImage(twogar_pac)

pantryque_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pac og4.jpg")
twopantryque_pac = pantryque_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_pantryquepac = ImageTk.PhotoImage(twopantryque_pac)

#Beverages Item

jd_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\jd.jpg")
twojd_pac = jd_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_jdpac = ImageTk.PhotoImage(twojd_pac)

pep_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pepsi.jpg")
twopep_pac = pep_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_peppac = ImageTk.PhotoImage(twopep_pac)

ck_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\coke.jpg")
twock_pac = ck_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_ckpac = ImageTk.PhotoImage(twock_pac)

sprite_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\sprite.jpg")
twosprite_pac = sprite_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_spritepac = ImageTk.PhotoImage(twosprite_pac)

rb_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\rootbeer.jpg")
tworb_pac = rb_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_rbpac = ImageTk.PhotoImage(tworb_pac)

ep_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\empi.jpg")
twoep_pac = ep_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_eppac = ImageTk.PhotoImage(twoep_pac)

pc_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pocari.jpg")
twopc_pac = pc_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_pcpac = ImageTk.PhotoImage(twopc_pac)

nes_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\nestea.jpg")
twones_pac = nes_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_nespac = ImageTk.PhotoImage(twones_pac)

bevque_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pac og3.jpg")
twobevque_pac = bevque_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_bevquepac = ImageTk.PhotoImage(twobevque_pac)


#Cleaning Items

br_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\brush.jpg")
twobr_pac = br_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_brpac = ImageTk.PhotoImage(twobr_pac)

mr_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\mr.jpg")
twomr_pac = mr_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_mrpac = ImageTk.PhotoImage(twomr_pac)

hy_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\hydro.jpg")
twohy_pac = hy_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_hypac = ImageTk.PhotoImage(twohy_pac)

mon_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\sulfur.jpg")
twomon_pac = mon_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_monpac = ImageTk.PhotoImage(twomon_pac)

zon_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\zonrox finale.png")
twozon_pac = zon_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_zonpac = ImageTk.PhotoImage(twozon_pac)

cl_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\cleaning.jpg")
twocl_pac = cl_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_clpac = ImageTk.PhotoImage(twocl_pac)

mol_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\molotov.jpg")
twomol_pac = mol_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_molpac = ImageTk.PhotoImage(twomol_pac)

clque_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pac og2.jpg")
twoclque_pac = clque_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_clquepac = ImageTk.PhotoImage(twoclque_pac)


#school Items

pen_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\pen finale.jpg")
twopen_pac = pen_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_penpac = ImageTk.PhotoImage(twopen_pac)

mar_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\marker.jpg")
twomar_pac = mar_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_marpac = ImageTk.PhotoImage(twomar_pac)

pad_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\padpaper.jpg")
twopad_pac = pad_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_padpac = ImageTk.PhotoImage(twopad_pac)

note_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\notebook.jpg")
twonote_pac = note_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_notepac = ImageTk.PhotoImage(twonote_pac)

spray_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\spray finale.jpg")
twospray_pac = spray_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_spraypac = ImageTk.PhotoImage(twospray_pac)

spque_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\default.jpg")
twospque_pac = spque_pac.resize((350, 200), Image.Resampling.LANCZOS)
background_spquepac = ImageTk.PhotoImage(twospque_pac)

log_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2fuck.png")
back_pac = log_pac.resize((850, 700), Image.Resampling.LANCZOS)
background_pac = ImageTk.PhotoImage(back_pac)

two_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\2pacmalala.png")
twoback_pac = two_pac.resize((370, 700), Image.Resampling.LANCZOS)
background_twopac = ImageTk.PhotoImage(twoback_pac)

log_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\LogIn Font2.png")
twolog_pac = log_pac.resize((100, 50), Image.Resampling.LANCZOS)
logground_twopac = ImageTk.PhotoImage(twolog_pac)

user_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\USERNAME.png")
twouser_pac = user_pac.resize((150, 50), Image.Resampling.LANCZOS)
userground_twopac = ImageTk.PhotoImage(twouser_pac)

pass_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\PASSWORD.png")
twopass_pac = pass_pac.resize((150, 50), Image.Resampling.LANCZOS)
passground_twopac = ImageTk.PhotoImage(twopass_pac)

signbt_pac = Image.open(r"C:\Users\HP_USER\Pictures\DBMS_PROJECT\Signin font2.png")
twosignbt_pac = signbt_pac.resize((100, 50), Image.Resampling.LANCZOS)
signgroundbt_twopac = ImageTk.PhotoImage(twosignbt_pac)

lbl_background = Label(main, image=background_pac, highlightthickness=0, bd=0)
lbl_background.grid(row=0, column=0, sticky="e")

second_pac = Canvas(main, width=400, height=150, highlightthickness=0)#400x150
second_pac.grid(row=0, column=0, sticky="sw")

lbl_mainlop = Label(second_pac, image=background_twopac, highlightthickness=0, bd=0)
lbl_mainlop.grid(row=0, column=0, sticky="sw")

login_canva = Canvas(main, width=450, height=250, highlightthickness=0, bg="#76b5c5")
login_canva.grid(row=0, column=0, sticky="w")

fr_login_canva = Frame(login_canva, highlightthickness=0, bg="#000000")
fr_login_canva.grid(row=0, column=0, sticky="w")

lbl_username = Label(fr_login_canva, image=userground_twopac, highlightthickness=0, bd=0)
lbl_username.grid(row=1, column=0)

txt_username = Entry(fr_login_canva,
                     font="Georgia 15", bg="#f3efca")
txt_username.grid(row=1, column=1)

lbl_password = Label(fr_login_canva, image=passground_twopac, highlightthickness=0, bd=0)
lbl_password.grid(row=2, column=0)

txt_password = Entry(fr_login_canva,
                     font="Georgia 15", bg="#f3efca",
                     show="*")
txt_password.grid(row=2, column=1)

bt_front_log = Frame(fr_login_canva,
                     bg="#000000")
bt_front_log.grid(row=3, column=1)

bt_login = Button(bt_front_log, image=logground_twopac, command=log_in, highlightthickness=0, bd=5)
bt_login.grid(row=0, column=2, sticky=W, padx=20)

bt_Signup = Button(bt_front_log, image=signgroundbt_twopac, command=sign_up, highlightthickness=0, bd=5)
bt_Signup.grid(row=0, column=1, sticky=E, padx=20)

bt_exit = Button(main, text="Exit", font="Garamond 15", bg="#000000", fg="white", command=exit_now)
bt_exit.grid(row=0, column=4, sticky="e")

main.mainloop()
