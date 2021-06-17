from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.geometry("800x800")
root.title("lotto")
root.config(bg="yellow")



class Lotto_machine():
        def __init__(self,slave):
            # Heading and 49 play buttons
            self.heading_label = Label(slave, text = "Pick 6 numbers", font="Consolas", bg="white")
            self.heading_label.place(x=150,y=10)
            self.btn_1 = Button(slave, text ="1", width=3, command=self.one)
            self.btn_1.place(x= 5, y=150)
            self.btn_2 = Button(slave, text="2", width=3, command=self.two)
            self.btn_2.place(x=40,y=150)
            self.btn_3 = Button(slave, text="3", width=3, command = self.three)
            self.btn_3.place(x=75,y=150)
            self.btn_4 = Button(slave,text="4", width=3, command=self.four)
            self.btn_4.place(x=110,y=150)
            self.btn_5 = Button(slave,text="5", width=3, command = self.five)
            self.btn_5.place(x=145,y=150)
            self.btn_6 = Button(slave, text="6", width=3, command = self.six)
            self.btn_6.place(x=180,y=150)
            self.btn_7 = Button(slave, text="7", width=3, command = self.seven)
            self.btn_7.place(x=215,y=150)
            self.btn_8=Button(slave,text="8", width=3, command=self.eight)
            self.btn_8.place(x=5, y=185)
            self.btn_9=Button(slave, text="9", width=3, command=self.nine)
            self.btn_9.place(x=40,y=185)
            self.btn_10 = Button(slave,text="10",width=3, command=self.ten)
            self.btn_10.place(x=75,y=185)
            self.btn_11=Button(slave,text="11",width=3, command = self.eleven)
            self.btn_11.place(x=110,y=185)
            self.btn_12=Button(slave, text="12", width=3, command = self.twelve)
            self.btn_12.place(x=145,y=185)

            self.btn_13 = Button(slave,text="13", width=3, command=self.thirteen)
            self.btn_13.place(x=180,y=185)

            self.btn_14=Button(slave,text="14",width=3, command=self.fourteen)
            self.btn_14.place(x=215,y=185)

            self.btn_15=Button(slave,text="15",width=3, command=self.fifteen)
            self.btn_15.place(x=5,y=220)

            self.btn_16=Button(slave,text="16",width=3, command=self.sixteen)
            self.btn_16.place(x=40,y=220)

            self.btn_17=Button(slave,text="17",width=3, command=self.seventeen)
            self.btn_17.place(x=75,y=220)

            self.btn_18=Button(slave,text="18",width=3, command=self.eighteen)
            self.btn_18.place(x=110,y=220)

            self.btn_19=Button(slave,text="19",width=3, command=self.nineteen)
            self.btn_19.place(x=145,y=220)

            self.btn_20=Button(slave,text="20",width=3, command=self.twenty)
            self.btn_20.place(x=180,y=220)

            self.btn_21=Button(slave,text="21",width=3, command=self.twenty_one)
            self.btn_21.place(x=215,y=220)

            self.btn_22=Button(slave,text="22",width=3, command=self.twenty_two)
            self.btn_22.place(x=5,y=255)

            self.btn_23=Button(slave,text="23",width=3, command=self.twenty_3)
            self.btn_23.place(x=40,y=255)

            self.btn_24=Button(slave,text="24",width=3, command=self.twenty_4)
            self.btn_24.place(x=75,y=255)

            self.btn_25=Button(slave,text="25",width=3, command=self.twenty_5)
            self.btn_25.place(x=110,y=255)

            self.btn_26=Button(slave,text="26",width=3, command=self.twenty_6)
            self.btn_26.place(x=145,y=255)

            self.btn_27=Button(slave,text="27",width=3, command=self.twenty_7)
            self.btn_27.place(x=180,y=255)

            self.btn_28=Button(slave,text="28",width=3, command=self.twenty_8)
            self.btn_28.place(x=215,y=255)

            self.btn_29=Button(slave,text="29",width=3, command=self.twenty_9)
            self.btn_29.place(x=5,y=285)

            self.btn_30=Button(slave,text="24",width=3, command=self.thirty)
            self.btn_30.place(x=40,y=285)

            self.btn_31=Button(slave,text="31",width=3, command=self.thirty_1)
            self.btn_31.place(x=75,y=285)

            self.btn_32=Button(slave,text="32",width=3, command=self.thirty_2)
            self.btn_32.place(x=110,y=285)

            self.btn_33=Button(slave,text="33",width=3, command=self.thirty_3)
            self.btn_33.place(x=145,y=285)

            self.btn_34=Button(slave,text="34",width=3, command=self.thirty_4)
            self.btn_34.place(x=180,y=285)

            self.btn_35=Button(slave,text="35",width=3, command=self.thirty_5)
            self.btn_35.place(x=215,y=285)

            self.btn_36=Button(slave,text="36",width=3, command=self.thirty_6)
            self.btn_36.place(x=5,y=320)

            self.btn_37=Button(slave,text="37",width=3, command=self.thirty_7)
            self.btn_37.place(x=40,y=320)

            self.btn_38=Button(slave,text="38",width=3, command=self.thirty_8)
            self.btn_38.place(x=75,y=320)

            self.btn_39=Button(slave,text="39",width=3, command=self.thirty_9)
            self.btn_39.place(x=110,y=320)

            self.btn_40=Button(slave,text="40",width=3, command=self.fourty)
            self.btn_40.place(x=145,y=320)

            self.btn_41=Button(slave,text="41",width=3, command=self.fourty_1)
            self.btn_41.place(x=180,y=320)

            self.btn_41=Button(slave,text="41",width=3, command=self.fourty_1)
            self.btn_41.place(x=180,y=320)

            self.btn_42=Button(slave,text="42",width=3, command=self.fourty_2)
            self.btn_42.place(x=215,y=320)

            self.btn_43=Button(slave,text="43",width=3, command=self.fourty_3)
            self.btn_43.place(x=5,y=355)

            self.btn_44=Button(slave,text="44",width=3, command=self.fourty_4)
            self.btn_44.place(x=40,y=355)

            self.btn_45=Button(slave,text="45",width=3, command=self.fourty_5)
            self.btn_45.place(x=75,y=355)

            self.btn_46=Button(slave,text="46",width=3, command=self.fourty_6)
            self.btn_46.place(x=110,y=355)

            self.btn_47=Button(slave,text="47",width=3, command=self.fourty_7)
            self.btn_47.place(x=145,y=355)

            self.btn_48=Button(slave,text="48",width=3, command=self.fourty_8)
            self.btn_48.place(x=180,y=355)

            self.btn_49=Button(slave,text="49",width=3, command=self.fourty_9)
            self.btn_49.place(x=215,y=355)


            # all the empty lists where results will be stored.
            self.empty1 =[]
            self.empty2 = []
            self.empty3 = []
            self.compare = []



            # first set of entries


            self.num_label1 =Label(slave, text="Numbers")
            self.num_label1.place(x=360, y=150)
            self.num_entry1=Entry(slave, width=28)
            self.num_entry1.place(x=420,y=150)

            self.draw_label1 = Label(slave, text="Draw")
            self.draw_label1.place(x=360,y=185)
            self.draw_entry1=Entry(slave,width=28)
            self.draw_entry1.place(x=420,y=185)

            self.results_label1 = Label(slave, text="Results", )
            self.results_label1.place(x=360,y=250)
            self.results_entry1=Entry(slave, width=28)
            self.results_entry1.place(x=420,y=250)

            # Second set

            self.num_label2=Label(slave, text="Numbers")
            self.num_label2.place(x=360, y=300)
            self.num_entry2=Entry(slave, width=28)
            self.num_entry2.place(x=420,y=300)

            self.draw_label2 = Label(slave, text="Draw")
            self.draw_label2.place(x=360,y=350)
            self.draw_entry2=Entry(slave,width=28)
            self.draw_entry2.place(x=420,y=350)

            self.results_label2 = Label(slave, text="Results", )
            self.results_label2.place(x=360,y=400)
            self.results_entry2 = Entry(slave, width=28)
            self.results_entry2.place(x=420,y=400)

            # Third set

            self.num_label3 =Label(slave, text="Numbers")
            self.num_label3.place(x=360, y=450)
            self.num_entry3=Entry(slave, width=28)
            self.num_entry3.place(x=420,y=450)
            #self.num_entry3.config(state='readonly')

            self.draw_label3 = Label(slave, text="Draw")
            self.draw_label3.place(x=360,y=500)
            self.draw_entry3=Entry(slave,width=28)
            self.draw_entry3.place(x=420,y=500)

            self.results_label3 = Label(slave, text="Results", )
            self.results_label3.place(x=360,y=550)
            self.results_entry3=Entry(slave, width=28)
            self.results_entry3.place(x=420,y=550)




            #play buttons

            self.play_btn = Button(slave,text="Play",command=self.play)
            self.play_btn.place(x=100,y=400)

            self.play_btn2 = Button(slave, text = "Play")


            # Sample creates a sample without replacement
            self.game_numbers = random.sample(range(1, 49), 6) # creating 6 random numbers

        # Append each number on 1 of the 3 empty list
        def one(self):
            from tkinter import messagebox

            if len(self.empty1) < 7:
                    self.empty1.append(1)
                    self.btn_1.config(state='disable')

            elif  len(self.empty2) < 7:
                    self.empty2.append(1)
                    self.btn_1.config(state='disable')

            else:

                self.empty3.append(1)
                self.btn_1.config(state='disable')



        def two(self):
            if len(self.empty1) < 7:
                self.empty1.append(2)

            elif len(self.empty2) < 7:
                self.empty2.append(2)
            else:
                self.empty3.append(2)

        def three(self):
            if len(self.empty1) < 7:
                self.empty1.append(3)

            elif len(self.empty2) < 7:
                self.empty2.append(3)
            else:
                self.empty3.append(3)

        def four(self):
            if len(self.empty1) < 7:
                self.empty1.append(4)

            elif len(self.empty2) < 7:
                self.empty2.append(4)
            else:
                self.empty3.append(4)


        def five(self):
            if len(self.empty1) < 7:
                self.empty1.append(5)

            elif  len(self.empty2) < 7:
                self.empty2.append(5)
            else:
                self.empty3.append(5)


        def six (self):
            if len(self.empty1) < 7:
                self.empty1.append(6)

            elif len(self.empty2) < 7:
                self.empty2.append(6)
            else:
                self.empty3.append(6)


        def seven (self):
            if len(self.empty1) < 7:
                self.empty1.append(7)

            elif len(self.empty2) < 7:
                self.empty2.append(7)
            else:
                self.empty3.append(7)
        def eight(self):
            if len(self.empty1) < 7:
                self.empty1.append(8)

            elif len(self.empty2) < 7:
                self.empty2.append(8)
            else:
                self.empty3.append(8)


        def nine(self):
            if len(self.empty1) < 7:
                self.empty1.append(9)

            elif  len(self.empty2) < 7:
                self.empty2.append(9)
            else:
                self.empty3.append(9)


        def ten(self):
            if len(self.empty1) < 7:
                self.empty1.append(10)

            elif  len(self.empty2) < 7:
                self.empty2.append(10)
            else:
                self.empty3.append(10)



        def eleven(self):
            if len(self.empty1) < 7:
                self.empty1.append(11)

            elif  len(self.empty2) < 7:
                self.empty2.append(11)
            else:
                self.empty3.append(11)


        def twelve(self):
            if len(self.empty1) < 7:
                self.empty1.append(12)

            elif  len(self.empty2) < 7:
                self.empty2.append(12)
            else:
                self.empty3.append(12)


        def thirteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(13)

            elif len(self.empty2) < 7:
                self.empty2.append(13)
            else:
                self.empty3.append(13)



        def fourteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(14)

            elif  len(self.empty2) < 7:
                self.empty2.append(14)
            else:
                self.empty3.append(14)


        def fifteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(15)

            elif  len(self.empty2) < 7:
                self.empty2.append(15)
            else:
                self.empty3.append(15)

        def sixteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(16)

            elif len(self.empty2) < 7:
                self.empty2.append(16)
            else:
                self.empty3.append(16)

        def seventeen(self):
            if len(self.empty1) < 7:
                self.empty1.append(17)

            elif len(self.empty2) < 7:
                self.empty2.append(17)
            else:
                self.empty3.append(17)

        def eighteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(18)

            elif len(self.empty2) < 7:
                self.empty2.append(18)
            else:
                self.empty3.append(18)

        def nineteen(self):
            if len(self.empty1) < 7:
                self.empty1.append(19)

            elif len(self.empty2) < 7:
                self.empty2.append(19)
            else:
                self.empty3.append(19)

        def twenty(self):
            if len(self.empty1) < 7:
                self.empty1.append(20)

            elif  len(self.empty2) < 7:
                self.empty2.append(20)
            else:
                self.empty3.append(20)

        def twenty_one(self):
            if len(self.empty1) < 7:
                self.empty1.append(21)

            elif len(self.empty2) < 7:
                self.empty2.append(21)
            else:
                self.empty3.append(21)


        def twenty_two(self):
            if len(self.empty1) < 7:
                self.empty1.append(22)

            elif len(self.empty2) < 7:
                self.empty2.append(22)
            else:
                self.empty3.append(22)

        def twenty_3(self):
            if len(self.empty1) < 7:
                self.empty1.append(23)

            elif len(self.empty2) < 7:
                self.empty2.append(23)
            else:
                self.empty3.append(23)


        def twenty_4(self):
            if len(self.empty1) < 7:
                self.empty1.append(24)

            elif len(self.empty2) < 7:
                self.empty2.append(24)
            else:
                self.empty3.append(24)


        def twenty_5(self):
            if len(self.empty1) < 7:
                self.empty1.append(25)

            elif len(self.empty2) < 7:
                self.empty2.append(25)
            else:
                self.empty3.append(25)

        def twenty_6(self):
            if len(self.empty1) < 7:
                self.empty1.append(26)

            elif len(self.empty2) < 7:
                self.empty2.append(26)
            else:
                self.empty3.append(26)


        def twenty_7(self):
            if len(self.empty1) < 7:
                self.empty1.append(27)

            elif len(self.empty2) < 7:
                self.empty2.append(27)
            else:
                self.empty3.append(27)


        def twenty_8(self):
            if len(self.empty1) < 7:
                self.empty1.append(28)

            elif len(self.empty2) < 7:
                self.empty2.append(28)
            else:
                self.empty3.append(28)


        def twenty_9(self):
            if len(self.empty1) < 7:
                self.empty1.append(29)

            elif len(self.empty2) < 7:
                self.empty2.append(29)
            else:
                self.empty3.append(29)


        def thirty(self):
            if len(self.empty1) < 7:
                self.empty1.append(30)

            elif len(self.empty2) < 7:
                self.empty2.append(30)
            else:
                self.empty3.append(30)


        def thirty_1(self):
            if len(self.empty1) < 7:
                self.empty1.append(31)

            elif len(self.empty2) < 7:
                self.empty2.append(31)
            else:
                self.empty3.append(31)


        def thirty_2(self):
            if len(self.empty1) < 7:
                self.empty1.append(32)

            elif len(self.empty2) < 7:
                self.empty2.append(32)
            else:
                self.empty3.append(32)

        def thirty_3(self):
            if len(self.empty1) < 7:
                self.empty1.append(33)

            elif len(self.empty2) < 7:
                self.empty2.append(33)
            else:
                self.empty3.append(33)


        def thirty_4(self):
            if len(self.empty1) < 7:
                self.empty1.append(34)

            elif len(self.empty2) < 7:
                self.empty2.append(34)
            else:
                self.empty3.append(34)


        def thirty_5(self):
            if len(self.empty1) < 7:
                self.empty1.append(35)

            elif len(self.empty2) < 7:
                self.empty2.append(35)
            else:
                self.empty3.append(35)


        def thirty_6(self):
            if len(self.empty1) < 7:
                self.empty1.append(36)

            elif len(self.empty2) < 7:
                self.empty2.append(36)
            else:
                self.empty3.append(36)


        def thirty_7(self):
            if len(self.empty1) < 7:
                self.empty1.append(37)

            elif len(self.empty2) < 7:
                self.empty2.append(37)
            else:
                self.empty3.append(37)


        def thirty_8(self):
            if len(self.empty1) < 7:
                self.empty1.append(38)

            elif len(self.empty2) < 7:
                self.empty2.append(38)
            else:
                self.empty3.append(38)


        def thirty_9(self):
            if len(self.empty1) < 7:
                self.empty1.append(39)

            elif len(self.empty2) < 7:
                self.empty2.append(39)
            else:
                self.empty3.append(39)


        def fourty(self):
            if len(self.empty1) < 7:
                self.empty1.append(40)

            elif len(self.empty2) < 7:
                self.empty2.append(40)
            else:
                self.empty3.append(40)


        def fourty_1(self):
            if len(self.empty1) < 7:
                self.empty1.append(41)

            elif len(self.empty2) < 7:
                self.empty2.append(41)
            else:
                self.empty3.append(41)

        def fourty_2(self):
            if len(self.empty1) < 7:
                self.empty1.append(42)

            elif len(self.empty2) < 7:
                self.empty2.append(42)
            else:
                self.empty3.append(42)

        def fourty_3(self):
            if len(self.empty1) < 7:
                self.empty1.append(43)

            elif len(self.empty2) < 7:
                self.empty2.append(43)
            else:
                self.empty3.append(43)

        def fourty_4(self):
            if len(self.empty1) < 7:
                self.empty1.append(44)

            elif len(self.empty2) < 7:
                self.empty2.append(44)
            else:
                self.empty3.append(44)


        def fourty_5(self):
            if len(self.empty1) < 7:
                self.empty1.append(45)

            elif  len(self.empty2) < 7:
                self.empty2.append(45)
            else:
                self.empty3.append(45)

        def fourty_6(self):
            if len(self.empty1) < 7:
                self.empty1.append(46)

            elif len(self.empty2) < 7:
                self.empty2.append(46)
            else:
                self.empty3.append(46)


        def fourty_7(self):
            if len(self.empty1) < 7:
                self.empty1.append(47)

            elif len(self.empty2) < 7:
                self.empty2.append(47)
            else:
                self.empty3.append(47)


        def fourty_8(self):
            if len(self.empty1) < 7:
                self.empty1.append(48)

            elif len(self.empty1) < 7:

                self.empty2.append(48)
            else:
                self.empty3.append(48)


        def fourty_9(self):
            if len(self.empty1) < 7:

                self.empty1.append(49)

            elif len(self.empty1) < 7:
                self.empty2.append(49)
            else:
                self.empty3.append(49)



        #play function

        def play(self):

            if len(self.empty1) < 7:
                for i in self.game_numbers:
                    if i in self.empty1:
                        self.compare.append(i)

            elif len(self.empty2) < 7:
                for i in self.game_numbers:
                    if i in self.empty2:
                        self.compare.append(i)

            else:
                if len(self.empty3) < 7:
                    for i in self.game_numbers:
                        if i in self.empty3:
                            self.compare.append(i)

            self.num_entry1.insert(0,self.empty1)
            self.results_entry1.insert(0,self.compare)
            self.draw_entry1.insert(0,self.game_numbers)
            self.num_entry1.config(state='readonly')
            self.results_entry1.config(state='readonly')
            self.draw_entry1.config(state='readonly')

            if len(self.empty2) != 0:

                self.num_entry2.insert(0,self.empty2)
                self.results_entry2.insert(0,self.compare)
                self.draw_entry2.insert(0,self.game_numbers)
                self.num_entry2.config(state='readonly')
                self.results_entry2.config(state='readonly')
                self.draw_entry2.config(state='readonly')

            if len(self.empty3) != 0:

                self.num_entry3.insert(0,self.empty3)
                self.results_entry3.insert(0,self.compare)
                self.draw_entry3.insert(0,self.game_numbers)
                self.num_entry3.config(state='readonly')
                self.results_entry3.config(state='readonly')
                self.draw_entry3.config(state='readonly')




        def sort_random_list(self):
            for i in range (1,len(self.game_numbers)):
                j=i
                while self.game_numbers[j-1] > self.game_numbers[j] and j>0:
                    self.game_numbers[j-1], self.game_numbers[j]=self.game_numbers[j],self.game_numbers[j-1]
                    j-=1


            for i in range (1,len(self.g)):
                j=i
                while self.game_numbers[j-1] > self.game_numbers[j] and j>0:
                    self.game_numbers[j-1], self.game_numbers[j]=self.game_numbers[j],self.game_numbers[j-1]
                    j-=1












y=Lotto_machine(root)
root.mainloop()
