from tkinter import Tk,Frame,Canvas,Entry,SUNKEN,Button,END

from hangWords001c_120 import long_list as word_content
from tkinter.simpledialog import askstring
import shelve, os, logging,re

from tkinter.messagebox import showinfo, askokcancel

class Tk_Hangman(Frame):
    """
    This is a spelling game .
    Each puzzle starts with 1500 points, wrong answers -250.
    Enter one character in the entry
    widget you can use either submit button or return (keyboard Enter).
    When the starts you have a row of empty boxes and the
    alphabet under it to keep track of your guesses.
    Saving the stats with a flat text file
    and the shelve module. 

    """
    def __init__(self, parent=None):
        self.parent= parent
        self.parent.title('HangMan')
        Frame.__init__(self, self.parent)
        self.pack(expand='yes',fill='both')
        self.canvas= Canvas(self)
        self.canvas.config(width= 1500, height= 900, bg='gray90')
        self.canvas.pack(expand='yes', fill='both')
        self.point_total= int
        self.xxx= 0
        self.guess= []
        fieldname= ('wins','losses','points')
        self.hangMan= [self.make_head, self.make_neck,  self.make_body, self.make_l_arm, 
                       self.make_r_arm, self.make_r_leg,  self.make_l_leg,]
                      
        self.picked_letters= []
        self.game_Count= int
        self.gamecount= int
        self.points= int
        self.wins= int
        self.losses= int
        self.pointz= int
        self.point_total= int
        self.shelve_name= 'hangman_001c'
        self.text_flat= 'hangman_001c.txt'
        self.letters= ['a','b','c','d','e','f','g','h',
                       'i','j','k','l','m','n',
                      'o','p','q','r','s','t','u','v',
                       'w','x','y','z',]
        self.build_puzzle()
    
    def setup_file(self):
        if os.path.exists(self.text_flat):
            self.read_game_count()
            self.read_stats()
        else:
            self.game_Count= 0
            self.gamecount= 0
            self.wins= 0
            self.losses= 0
            self.pointz= 0
            self.shelve_setup()
    def read_stats(self):
        db= shelve.open(self.shelve_name, 'r')
        self.gamecount= db['stats']['gamecount']
        self.wins= db['stats']['wins']
        self.losses= db['stats']['losses']
        self.pointz= db['stats']['points']
        db.close()
        return self.gamecount, self.wins, self.losses

    def shelve_setup(self):
        stats= {'gamecount':0,'wins':0,'losses':0,'points':0}
        db= shelve.open(self.shelve_name, 'n')
        db['stats']= stats
        db.close()
    def points_total(self):
        db= shelve.open(self.shelve_name, writeback=True)
        copy= db['stats']['points']
        db['stats']['points']= self.points + copy
        db.close()
        return self.points
    def win_update(self):
        logging.debug('start in wins %d gamecount %d points %d'% (self.wins,
                                                                 self.gamecount,
                                                                 self.points))
        db= shelve.open(self.shelve_name, writeback=True)
        db['stats']['wins']= self.wins + 1
        db['stats']['gamecount']= self.gamecount + 1
        db.close()
        self.points_total()
        return self.gamecount, self.wins
    def loss_update(self):
        self.points_total()
        db= shelve.open(self.shelve_name, writeback=True)
        db['stats']['losses']= self.losses + 1
        db['stats']['gamecount']= self.gamecount + 1
        db.close
        return self.losses, self.gamecount
    def read_game_count(self):
        f= open(self.text_flat)        
        self.game_Count = int(f.read())
        return self.game_Count
    def write_game_count(self):
        f= open(self.text_flat, 'w+')
        f.write(str(self.game_Count))
        f.close()  
   
    def make_head(self):
        head= [(217.5, 181.5), (197.5, 191.5), (185.5, 226.5),
               (183.5, 257.5), (195.5, 298.5), (216.5, 317.5),
               (235.5, 344.5), (256.5, 369.5), (300.5, 366.5),
               (319.5, 338.5), (321.5, 309.5), (317.5, 270.5),
               (309.5, 240.5), (294.5, 218.5), (271.5, 197.5),
               (246.5, 181.5)]
        
        self.canvas.create_polygon(head,fill= 'red', tag='head')
                               
        self.points -= 250        
        self.show_points()
    def make_neck(self):
        neck= [(196.5, 312.5), (204.5, 351.5), (205.5, 383.5),
               (195.5, 410.5), (198.5, 422.5), (234.5, 452.5),
               (271.5, 470.5), (308.5, 458.5), (326.5, 433.5),
               (326.5, 412.5), (297.5, 411.5), (290.5, 427.5),
               (276.5, 380.5), (254.5, 382.5), (231.5, 351.5),
               (212.5, 324.5)]
        
        self.canvas.create_polygon(neck, fill='black',tag='neck')
                                 
        self.points -= 250        
        self.show_points()
    def make_l_arm(self):
        left= [(79.5, 491.5), (147.5, 509.5), (144.5, 545.5),
               (149.5, 591.5), (138.5, 616.5), (140.5, 640.5),
               (157.5, 666.5), (143.5, 679.5), (101.5, 685.5),
               (69.5, 677.5), (65.5, 661.5), (81.5, 648.5),
               (90.5, 627.5), (85.5, 593.5), (73.5, 533.5)]
        
        
        self.canvas.create_polygon(left, fill='black', tag='l_arm')
                                
        self.points -= 250        
        self.show_points()
    def make_r_arm(self):
        r_arm= [(356.5, 511.5), (361.5, 532.5), (374.5, 564.5),
                (379.5, 598.5), (382.5, 635.5), (391.5, 652.5),
                (386.5, 671.5), (403.5, 675.5), (435.5, 673.5),
                (460.5, 653.5), (445.5, 629.5), (435.5, 622.5),
                (422.5, 612.5), (422.5, 574.5), (416.5, 539.5),
                (414.5, 508.5), (408.5, 483.5)]
        
        self.canvas.create_polygon(r_arm, fill='black',tag='r_arm')
                                 
        self.points -= 250        
        self.show_points()
    def make_body(self):
        body= [(335.5, 412.5), (368.5, 414.5), (399.5, 441.5),
               (407.5, 475.5), (363.5, 503.5), (363.5, 503.5),
               (348.5, 510.5), (341.5, 491.5), (339.5, 566.5),
               (344.5, 626.5), (277.5, 626.5), (215.5, 623.5),
               (184.5, 619.5), (163.5, 480.5), (149.5, 502.5),
               (79.5, 485.5), (76.5, 441.5), (92.5, 412.5),
               (152.5, 399.5), (190.5, 397.5), (189.5, 416.5),
               (194.5, 429.5), (231.5, 460.5), (272.5, 480.5),
               (311.5, 466.5), (332.5, 436.5)]
        
        self.canvas.create_polygon(body, fill='black',tag='body')
                                
        self.points -= 250        
        self.show_points()
    def make_l_leg(self):
        left_leg= [(184.5, 630.5), (217.5, 636.5), (261.5, 633.5),
               (261.5, 633.5), (273.5, 706.5), (255.5, 761.5),
               (241.5, 804.5), (234.5, 841.5), (225.5, 879.5),
               (213.5, 887.5), (167.5, 888.5), (118.5, 889.5),
               (83.5, 885.5), (69.5, 856.5), (84.5, 838.5),
               (116.5, 838.5), (132.5, 844.5), (162.5, 814.5),
               (169.5, 766.5), (188.5, 675.5)]
        
        self.canvas.create_polygon(left_leg, fill='black', tag='l_leg')
        self.points -= 250        
        self.show_points()
    def make_r_leg(self):
        r_leg= [(267.5, 637.5), (278.5, 712.5), (325.5, 768.5),
                (342.5, 791.5), (359.5, 835.5), (364.5, 874.5),
                (368.5, 897.5), (428.5, 893.5), (463.5, 886.5),
                (485.5, 876.5), (480.5, 824.5), (442.5, 837.5),
                (412.5, 843.5), (387.5, 773.5), (361.5, 722.5),
                (344.5, 691.5), (344.5, 636.5)]
        
        self.canvas.create_polygon(r_leg,  fill='black', tag='r_leg')
                                
        self.points -= 250        
        self.show_points()
            
    def show_values(self):
        x=20
        y=130
        for l in self.letters:
            self.canvas.create_text(x,y, text=l, fill='black',
                                    font=('times',16,'bold'),
                                    tag='value%s'%l)
            x += 25
        return self.puzzle_number(x,y)

    def start_points(self):
        self.points= 1500
        return self.show_points()
    

    def show_points(self):
        self.delete_points()
        x=1100
        y=500
        txt= 'Total game points: %d'% self.points
        tally= self.canvas.create_text(x,y, text= txt, fill='black',
                                      font=('ms',16,'bold'), tag='tgps')
        return self.points
    def delete_points(self):
        return self.canvas.delete('tgps')
        
        

    def puzzle_number(self,x,y):
        self.widget= Entry(root, relief= SUNKEN,)
        
        self.widget.place(x= 960, y= 225)
        self.widget.focus()
        self.widget.bind('<Return>', (lambda event:self.ask_for_letter()))
        self.btn= Button(root, text='Submit', command= self.ask_for_letter)
        x += 370
        self.btn.place(x= 1200, y= 225)
        the_num= 'The puzzle number: %d'% self.game_Count
        self.canvas.create_text(x+100,y, text=the_num, fill='black',
                                font=('ms', 18, 'bold'), tag='game_num')
        the_wins= 'The total wins: %d' % self.wins
        self.canvas.create_text(x+100,y+60, text= the_wins, fill='black',
                                font=('ms', 18, 'bold'), tag='t_wins')
        the_loss= 'Total number of losses: %d'% self.losses
        self.canvas.create_text(x+100, y+160, text= the_loss, fill='black',
                                font=('ms',18,'bold'), tag='t_loss')
        the_gme= 'Total shelve game count: %d' % self.gamecount
        self.canvas.create_text(x+100, y+230, text= the_gme, fill='black',
                                font=('ms',18,'bold'),tag='shelve_c')
        the_pointz= 'Total points: %d'% self.pointz
        self.canvas.create_text(x+100, y+300, text=the_pointz, fill='purple',
                                font=('ms',18,'bold'), tag='points')
    def get_word(self,p):    
        self.res= []
        num= self.game_Count
        self.picked_word= p[num]
        for i in self.picked_word:
            self.res.append(i)    
        return self.picked_word, self.res
    
    def build_puzzle(self):
        logging.debug('Building the puzzle')
        self.start_points()
        self.setup_file()
        self.show_values()
        self.get_word(word_content)
        x= 10   
        x1= 10
        y= 60
        y1= 60
        for j in self.picked_word:
            self.canvas.create_rectangle(x,x1,y,y1, fill='white', width=2,
                                         tag='puzzle%s'%j)
            x+= 50
            y+= 50
        logging.debug('tiles made, x: %d y: %d'%(x,y))
        

    def next_puzzle(self):
        self.canvas.delete('all')
        self.build_puzzle()

    def new_game(self):    
        self.xxx= 0
        self.guess= []
        self.picked_letters= []
        new_g= askokcancel('New Game','Play again?')
        self.game_Count += 1
        if new_g:
            if self.game_Count > len(word_content)-1:
                self.game_Count= 0
                self.write_game_count()
                self.shelve_setup()
                self.next_puzzle()
            else:
                self.write_game_count()
                self.next_puzzle()                   
        else:
            if self.game_Count > len(word_content)-1:
                self.game_Count= 0
                self.write_game_count()
                self.shelve_setup()
                root.destroy()
            else:
                self.write_game_count()
                root.destroy()                

    def ask_for_letter(self):              
        findletter= self.widget.get()
        
        if findletter:
            self.widget.delete(0,END)
            if len(findletter) >1 or findletter in self.picked_letters:
                showinfo('Error', 'Pick again one letter or already picked')
                self.ask_for_letter()
            else:
                if re.findall(findletter, self.picked_word):
                    tagGuess= 'puzzle'+ findletter
                    t_g= self.canvas.find_withtag(tagGuess)
                    for i in list(t_g):
                        pos= self.canvas.coords(i)
                        x1= (pos[0] + pos[2])/2
                        y1= (pos[1] + pos[3])/2
                        self.canvas.create_text(x1,y1, text= findletter, fill= 'red',
                                                font=('arial', 25, 'bold'), tag='guess')
                        self.guess.append(findletter)
                    val_d= 'value'+ (findletter)
                    self.canvas.delete(val_d)
                    self.picked_letters.append(findletter)
                    if len(self.res) == len(self.guess):
                        self.win_update()
                        self.canvas.create_text(750,650, text='Win', fill='yellow',
                                           font=('times', 50, 'bold'), tag='win')
                        self.canvas.create_text(800,800,text=self.picked_word, fill='green',
                                                font=('times',50,'bold'), tag='word')
                    
                        self.new_game()             
             
                else:
                    if self.xxx == 6:
                        self.hangMan[self.xxx]()
                        self.canvas.create_text(750,650, text='Loss', fill='orange',
                                                font=('times', 50, 'bold'), tag='loss')
                        self.loss_update()
                        logging.debug('The puzzle word:  %s'% self.picked_word)
                        self.canvas.create_text(800,800,text=self.picked_word, fill='green',
                                                font=('times',50,'bold'), tag='word')
                        self.new_game()
                    else:
                        self.hangMan[self.xxx]()
                        d_val= 'value'+ (findletter)
                        self.canvas.delete(d_val)
                        self.picked_letters.append(findletter)
                        self.xxx+=1
                        

if __name__ == '__main__':
    root= Tk()    
    root.title('Hangman_11b')
    Tk_Hangman(root)
    root.mainloop()

