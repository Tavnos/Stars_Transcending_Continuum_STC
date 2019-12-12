from numpy import abs
from random import (randrange, choice)
import tkinter as tk
import os
import sys


class Game_Init(tk.Tk):
    game_delay = 71 
    game_clock = 0 
    object_size = 40
    board_size = 100
    view_size = 14 # should be int(h+w/2)
    message_log_size = 100
    frame_width = 2*5 + view_size * object_size 
    frame_height = 2*5 + view_size * object_size + message_log_size
    tile_nr_dict = {'ground_grass_id' : 0, 'player_id' : 1, 'world_border_id' : 40, 'bush_wall_id' : 41}
    player_row_pos = 45
    player_col_pos = 45
    def __init__(self):
        super().__init__()
        self.bind("<Key>", self.key_pressed)
        self.tk_frame = tk.Canvas(self, width=self.frame_width, height=self.frame_height) 
        self.tk_frame.pack()
        
        self.img_dict = {
            'player_up_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_up.gif")),
            'player_down_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_down.gif")),
            'player_left_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_left.gif")),
            'player_right_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_right.gif")),
            'world_border_src' : tk.PhotoImage(file=self.resource_path("img/border_stone.gif")),      
            'ground_grass_src' : tk.PhotoImage(file=self.resource_path("img/ground_grass.gif")),                    
            'stat_dash_src' : tk.PhotoImage(file=self.resource_path("img/stat_dash.gif"))}
        
        self.write_ui_instance()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def timer_clock(self): 
        self.tk_frame.delete(tk.ALL) 
        self.game_clock += 1
        if self.game_clock >= 10:
            self.game_clock = 0
        self.write_view_frame()
        self.draw_view_frame()
        self.tk_frame.after(self.game_delay, self.timer_clock)
        
    def key_pressed(self, tk_command):
        self.tk_frame = tk_command.widget.tk_frame
        if (tk_command.char == "p") and (self.instance == 0):
            self.write_first_instance() 
        if tk_command.keysym == "Up": 
            self.move_player(-1, 0) 
        if tk_command.keysym == "Down":
            self.move_player(+1, 0) 
        if tk_command.keysym == "Left":
            self.move_player(0,-1) 
        if tk_command.keysym == "Right":
            self.move_player(0,+1)
            
    def write_board(self):
        self.grid_list = []
        for row in range(self.board_size): 
            self.grid_list += [[0] * self.board_size] 
        for row in range(self.board_size-40): 
            self.grid_list[20][row+20] = 40
            self.grid_list[self.board_size-20][row+20] = 40  
        for col in range(self.board_size-39):
            self.grid_list[col+20][20] = 40
            self.grid_list[col+20][self.board_size-20] = 40 
    def write_view_frame(self):
        self.view_list = []
        self.view_h_size = 12
        self.view_w_size = 14
        for i in range(self.view_h_size):
            self.view_list += [self.grid_list[i+(self.player_row_pos+1-int(self.view_h_size/2))][self.player_col_pos+1-int(self.view_w_size/2):self.player_col_pos+1+int(self.view_w_size/2)]]
    def draw_view_frame(self):
        for i_row in range(self.view_h_size): 
            for f_col in range(self.view_w_size):
                rect_left = 5 + f_col * self.object_size+ 12
                rect_right = rect_left + self.object_size + 12
                rect_top = 5 + i_row * self.object_size + 110
                rect_bottom = rect_top + self.object_size + 110
                if self.view_list[i_row][f_col] == self.tile_nr_dict['player_id']:
                    self.add_background(rect_left, rect_top)
                    self.draw_player_frame(rect_left, rect_top)
                if self.view_list[i_row][f_col] == self.tile_nr_dict['world_border_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['world_border_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ground_grass_id']: 
                    self.add_background(rect_left, rect_top)
                if self.view_list[i_row][f_col] == self.tile_nr_dict['bush_wall_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['bush_wall_src'])
                self.tk_frame.create_text(50,200, text=self.game_clock, fill="black")
                self.tk_frame.create_image((self.view_h_size/2)*40, 10, image=self.img_dict['stat_dash_src'])
    def add_background(self, rect_left, rect_top):
        self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['ground_grass_src'])
    def write_first_instance(self):
        self.write_board() 
        self.move_player(0,0)
        self.timer_clock()
    def write_ui_instance(self): 
        self.instance = 0
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 250, 
                                  text='x v.x', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 200, 
                                  text='Press P to play', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 150, 
                                  text='x', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 100, 
                                  text='x', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 50, 
                                  text='x', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2), 
                                  text='x)', fill="black")
    def draw_player_frame(self, rect_left, rect_top):
        if self.player_row_vec == -1 and self.player_col_vec == 0:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['player_up_src'])
        elif self.player_row_vec == 1 and self.player_col_vec == 0:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['player_down_src'])
        elif self.player_row_vec == 0 and self.player_col_vec == -1:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['player_left_src'])
        elif self.player_row_vec == 0 and self.player_col_vec == 1:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['player_right_src'])
        else:
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['player_down_src'])      
    def move_player(self, dist_row, dist_col):
        self.player_row_vec = dist_row
        self.player_col_vec = dist_col
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 0: 
            self.grid_list[self.player_row_pos][self.player_col_pos] = 0
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
init_grid = Game_Init()
init_grid.mainloop()