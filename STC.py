from numpy import abs
from random import (randrange, choice)
import tkinter as tk
import os
import sys

class Game_Variables:
    monitor_on = False
    assembler_on = False
    mainframe_on = False
    refinery_on = False
    lifesupport_on = False
    reactor_on = False
    inventory_display = False
    ship_cargo = False
    implant_interface = False
    ship_status = False
    multitool_repair = False
    first_dialog = True
    player_row_vec = 1
    player_col_vec = 1
    player_row_pos = 45
    player_col_pos = 45    
    player_health = 9
    player_shield = 1
    player_armor = 7
    player_oxygen = 10
    player_water = 6
    player_food = 8
    player_sleep = 9
    player_energy = 10
    player_weight = 10
    player_xp = 4
    player_signal = 10
    player_ammo = 9
    game_delay = 97
    game_clock = 0 
    sub_clock = 0
    object_size = 40 
    board_size = 100
    view_size = 14 
    message_log_size = 100
    frame_width = 2*5 + view_size * object_size 
    frame_height = 2*5 + view_size * object_size + message_log_size
    current_player_tile = 'ground_grass_id'
    inventory_option_selected = 'microchip interface'
    ship_option_selected = 'monitor'
    cargo_option_selected = 'metal alloy'
    interface_option_selected = 'inventory'
    repair_option_selected = 'repair'
    player_inventory = {'microchip interface':1,'multitool':1,'phaser':1,'id_documents':1,'data_cube':1,
                        'phaser_charges':8}
    ship_storage = {'metal alloy':5, 'electronic components':3, 'radioactive isotopes': 6, 
                    'plastic polymers': 5}
    interface_option = {'inventory':1,'ship status':2,'phaser mode':3,'read id documents':4,
                        'read data_cube':5,'broadcast signal':6}
    ship_option = {'monitor': 22, 'assembler': 12, 'lifesupport': 8, 'reactor': 0, 'mainframe': 0, 
                   'hull' : 59, 'bed': 59, 'cargo container': 94}
    tile_nr_dict = {'ground_grass_id' : 0, 'player_id' : 1, 'world_border_id' : 40, 
                    'bush_wall_id' : 41, 'ship_floor_id' : 59, 'ship_monitor_id' : 60, 
                    'ship_storage_id': 61, 'ship_mainframe_id' : 62, 'ship_lifesupport_id' : 80, 
                    'ship_reactor_id' : 63, 'ship_refinery_id' : 64, 'ship_assembler_id' : 65,
                    'ship_bed_id' : 66, 'ship_blwallcorner_id' : 67, 'ship_tlwallcorner_id' : 68, 
                    'ship_brwallcorner_id' : 69, 'ship_trwallcorner_id' : 70, 'ship_enginemount_id' : 71, 
                    'ship_enginetipoff_id' : 72, 'ship_lasermount_id' : 73, 'ship_lasertip_id' : 74, 
                    'ship_wall_h_id' : 75, 'ship_wall_v_id' : 76, 'wood_tree_id' : 77,
                    'ship_dooropen_id' : 78, 'ship_doorclosed_id' : 79}
    
class Image_Fetch:
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    def fetching_img(self):
        self.img_dict = {
            'player_up_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_up.gif")),
            'player_down_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_down.gif")),
            'player_left_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_left.gif")),
            'player_right_src' : tk.PhotoImage(file=self.resource_path("img/human_fa_right.gif")),
            'world_border_src' : tk.PhotoImage(file=self.resource_path("img/border_stone.gif")),      
            'ground_grass_src' : tk.PhotoImage(file=self.resource_path("img/ground_grass.gif")),     
            'ship_dooropen_src' : tk.PhotoImage(file=self.resource_path("img/ship_dooropen.gif")),     
            'ship_doorclosed_src' : tk.PhotoImage(file=self.resource_path("img/ship_doorclosed.gif")),     
            'ship_floor_src' : tk.PhotoImage(file=self.resource_path("img/ship_floor.gif")),     
            'ship_monitoroff_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitoroff.gif")),     
            'ship_monitorona_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitorona.gif")),     
            'ship_monitoronb_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitoronb.gif")),     
            'ship_monitoronc_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitoronc.gif")),     
            'ship_monitorond_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitorond.gif")),     
            'ship_monitorone_src' : tk.PhotoImage(file=self.resource_path("img/ship_monitorone.gif")),     
            'ship_storage_src' : tk.PhotoImage(file=self.resource_path("img/ship_storage.gif")),     
            'ship_mainframeoff_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeoff.gif")),   
            'ship_mainframeona_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeona.gif")),   
            'ship_mainframeonb_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeonb.gif")),   
            'ship_mainframeonc_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeonc.gif")),   
            'ship_mainframeond_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeond.gif")),   
            'ship_mainframeone_src' : tk.PhotoImage(file=self.resource_path("img/ship_mainframeone.gif")),   
            'ship_lifesupportoff_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportoff.gif")), 
            'ship_lifesupportona_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportona.gif")), 
            'ship_lifesupportonb_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportonb.gif")), 
            'ship_lifesupportonc_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportonc.gif")), 
            'ship_lifesupportond_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportond.gif")), 
            'ship_lifesupportone_src' :tk.PhotoImage(file=self.resource_path("img/ship_lifesupportone.gif")), 
            'ship_reactoroff_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactoroff.gif")),       
            'ship_reactorona_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactorona.gif")),       
            'ship_reactoronb_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactoronb.gif")),       
            'ship_reactoronc_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactoronc.gif")),       
            'ship_reactorond_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactorond.gif")),       
            'ship_reactorone_src' : tk.PhotoImage(file=self.resource_path("img/ship_reactorone.gif")),      
            'ship_refineryoff_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryoff.gif")),   
            'ship_refineryona_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryona.gif")),   
            'ship_refineryonb_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryonb.gif")),   
            'ship_refineryonc_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryonc.gif")),   
            'ship_refineryond_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryond.gif")),   
            'ship_refineryone_src' : tk.PhotoImage(file=self.resource_path("img/ship_refineryone.gif")),     
            'ship_assembleroff_src' : tk.PhotoImage(file=self.resource_path("img/ship_assembleroff.gif")),   
            'ship_assemblerona_src' : tk.PhotoImage(file=self.resource_path("img/ship_assemblerona.gif")),   
            'ship_assembleronb_src' : tk.PhotoImage(file=self.resource_path("img/ship_assembleronb.gif")),   
            'ship_assembleronc_src' : tk.PhotoImage(file=self.resource_path("img/ship_assembleronc.gif")),   
            'ship_assemblerond_src' : tk.PhotoImage(file=self.resource_path("img/ship_assemblerond.gif")),   
            'ship_assemblerone_src' : tk.PhotoImage(file=self.resource_path("img/ship_assemblerone.gif")),   
            'ship_bed_src' : tk.PhotoImage(file=self.resource_path("img/ship_bed.gif")),      
            'ship_blwallcorner_src' : tk.PhotoImage(file=self.resource_path("img/ship_blwallcorner.gif")),   
            'ship_tlwallcorner_src' : tk.PhotoImage(file=self.resource_path("img/ship_tlwallcorner.gif")),   
            'ship_brwallcorner_src' : tk.PhotoImage(file=self.resource_path("img/ship_brwallcorner.gif")),   
            'ship_trwallcorner_src' : tk.PhotoImage(file=self.resource_path("img/ship_trwallcorner.gif")),   
            'ship_enginemount_src' : tk.PhotoImage(file=self.resource_path("img/ship_enginemount.gif")),     
            'ship_enginetipoff_src' : tk.PhotoImage(file=self.resource_path("img/ship_enginetipoff.gif")),   
            'ship_lasermount_src' : tk.PhotoImage(file=self.resource_path("img/ship_lasermount.gif")),     
            'ship_lasertip_src' : tk.PhotoImage(file=self.resource_path("img/ship_lasertip.gif")),     
            'ship_wall_h_src' : tk.PhotoImage(file=self.resource_path("img/ship_wall_h.gif")),     
            'ship_wall_v_src' : tk.PhotoImage(file=self.resource_path("img/ship_wall_v.gif")),     
            'wood_tree_src' : tk.PhotoImage(file=self.resource_path("img/wood_tree.gif")),                   
            'stat_dash_src' : tk.PhotoImage(file=self.resource_path("img/stat_dash.gif")),    
            'game_armor_src' : tk.PhotoImage(file=self.resource_path("img/game_armor.gif")),     
            'game_shield_src' : tk.PhotoImage(file=self.resource_path("img/game_shield.gif")),               
            'game_life_src' : tk.PhotoImage(file=self.resource_path("img/game_life.gif")),
            'game_oxygen_src' : tk.PhotoImage(file=self.resource_path("img/game_oxygen.gif")),     
            'game_food_src' : tk.PhotoImage(file=self.resource_path("img/game_food.gif")),                   
            'game_water_src' : tk.PhotoImage(file=self.resource_path("img/game_water.gif")),
            'game_energy_src' : tk.PhotoImage(file=self.resource_path("img/game_energy.gif")),     
            'game_sleep_src' : tk.PhotoImage(file=self.resource_path("img/game_sleep.gif")),    
            'game_ammo_src' : tk.PhotoImage(file=self.resource_path("img/game_ammo.gif")),     
            'game_sleep_src' : tk.PhotoImage(file=self.resource_path("img/game_sleep.gif")),    
            'game_signal_src' : tk.PhotoImage(file=self.resource_path("img/game_signal.gif")),  
            'game_xp_src' : tk.PhotoImage(file=self.resource_path("img/game_xp.gif")),              
            'game_weight_src' : tk.PhotoImage(file=self.resource_path("img/game_weight.gif")),
            'game_overlay_src' : tk.PhotoImage(file=self.resource_path("img/game_overlay.gif"))} 
        
class Game_Mechanics:
    def timer_clock(self): 
        self.tk_frame.delete(tk.ALL) 
        self.game_clock += 1
        if self.game_clock >= 10:
            self.game_clock = 0
            self.sub_clock += 1
        if self.sub_clock >= 10:
            self.sub_clock = 0
        self.write_view_frame()
        self.draw_view_frame()
        self.tk_frame.after(self.game_delay, self.timer_clock)
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
        self.view_h_size = 14
        self.view_w_size = 14
        for i in range(self.view_h_size):
            self.view_list += [self.grid_list[i+(self.player_row_pos+1-int(self.view_h_size/2))][self.player_col_pos+1-int(self.view_w_size/2):self.player_col_pos+1+int(self.view_w_size/2)]]
    def add_background(self, rect_left, rect_top):
        self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['ground_grass_src'])
    def custom_background(self, rect_left, rect_top):
        if self.current_player_tile == 'ground_grass_id':
            self.add_background(rect_left, rect_top)
        elif self.current_player_tile == 'ship_dooropen_id':
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['ship_dooropen_src'])
        elif self.current_player_tile == 'ship_floor_id':
            self.tk_frame.create_image(rect_left+10, rect_top+10, image=self.img_dict['ship_floor_src'])     
    
    def key_pressed(self, tk_command):
        self.tk_frame = tk_command.widget.tk_frame
        if tk_command.char == "p" and self.instance == 0:
            self.write_first_instance() 
        elif tk_command.keysym == "f":
            self.remove_overlays()
        elif self.inventory_display == False and self.implant_interface == False and self.ship_status == False and self.ship_cargo == False and self.first_dialog == False:
            if tk_command.keysym == "Up":
                self.move_player(-1, 0) 
            elif tk_command.keysym == "Down":
                self.move_player(+1, 0) 
            elif tk_command.keysym == "Left":
                self.move_player(0,-1) 
            elif tk_command.keysym == "Right":
                self.move_player(0,+1)
            elif tk_command.keysym == "e":
                self.ability_activate()
            elif tk_command.keysym == "i":
                self.inventory_toogle()
        elif self.inventory_display == True:
            if tk_command.keysym == "Up" and self.inv_key.index(self.inventory_option_selected) >= 1:
                self.inventory_option_selected = self.inv_key[self.inv_key.index(self.inventory_option_selected)-1]
            elif tk_command.keysym == "Down" and self.inv_key.index(self.inventory_option_selected) <= len(self.inv_key)-2:
                self.inventory_option_selected = self.inv_key[self.inv_key.index(self.inventory_option_selected)+1]
            elif tk_command.keysym == "c" and self.inventory_option_selected == 'microchip interface':
                self.remove_overlays()
                self.interface_toogle()
        elif self.implant_interface == True:
            if tk_command.keysym == "Up" and self.imp_key.index(self.interface_option_selected) >= 1:
                self.interface_option_selected = self.imp_key[self.imp_key.index(self.interface_option_selected)-1]
            elif tk_command.keysym == "Down" and self.imp_key.index(self.interface_option_selected) <= len(self.imp_key)-2:
                self.interface_option_selected = self.imp_key[self.imp_key.index(self.interface_option_selected)+1]
            elif tk_command.keysym == "c" and self.interface_option_selected == 'inventory':
                self.remove_overlays()
                self.inventory_toogle()
            elif tk_command.keysym == "c" and self.interface_option_selected == 'ship status':
                self.remove_overlays()
                self.ship_toogle()
        elif self.ship_status == True:
            if tk_command.keysym == "Up" and self.shp_key.index(self.ship_option_selected) >= 1:
                self.ship_option_selected = self.shp_key[self.shp_key.index(self.ship_option_selected)-1]
            elif tk_command.keysym == "Down" and self.shp_key.index(self.ship_option_selected) <= len(self.shp_key)-2:
                self.ship_option_selected = self.shp_key[self.shp_key.index(self.ship_option_selected)+1]
            elif tk_command.keysym == "c" and self.ship_option_selected == 'cargo container':
                self.remove_overlays()
                self.cargo_toogle()
        elif self.ship_cargo == True:
            if tk_command.keysym == "Up" and self.crg_key.index(self.cargo_option_selected) >= 1:
                self.cargo_option_selected = self.crg_key[self.crg_key.index(self.cargo_option_selected)-1]
            elif tk_command.keysym == "Down" and self.crg_key.index(self.cargo_option_selected) <= len(self.crg_key)-2:
                self.cargo_option_selected = self.crg_key[self.crg_key.index(self.cargo_option_selected)+1]
                
class Rendering_World:
    def draw_view_frame(self):
        for i_row in range(self.view_h_size): 
            for f_col in range(self.view_w_size):
                rect_left = 5 + f_col * self.object_size+ 12
                rect_right = rect_left + self.object_size + 12
                rect_top = 5 + i_row * self.object_size + 110
                rect_bottom = rect_top + self.object_size + 110
                if self.view_list[i_row][f_col] == self.tile_nr_dict['player_id']:
                    self.custom_background(rect_left, rect_top)
                    self.draw_player_frame(rect_left, rect_top)
                if self.view_list[i_row][f_col] == self.tile_nr_dict['world_border_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['world_border_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ground_grass_id']: 
                    self.add_background(rect_left, rect_top)
                if self.view_list[i_row][f_col] == self.tile_nr_dict['bush_wall_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['bush_wall_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_floor_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_floor_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_dooropen_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_dooropen_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_doorclosed_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_doorclosed_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_monitor_id']: 
                    if self.monitor_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10,
                                                       image=self.img_dict['ship_monitorona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_monitoronb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_monitoronc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_monitorond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_monitorone_src'])
                    elif self.monitor_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_monitoroff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_refinery_id']: 
                    if self.refinery_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_refineryona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_refineryonb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_refineryonc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_refineryond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_refineryone_src'])
                    elif self.refinery_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_refineryoff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_assembler_id']: 
                    if self.assembler_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_assemblerona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_assembleronb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_assembleronc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_assemblerond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10,
                                                       image=self.img_dict['ship_assemblerone_src'])
                    elif self.assembler_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_assembleroff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_lifesupport_id']: 
                    if self.lifesupport_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_lifesupportona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_lifesupportonb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_lifesupportonc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_lifesupportond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_lifesupportone_src'])
                    elif self.lifesupport_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_lifesupportoff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_mainframe_id']: 
                    if self.mainframe_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_mainframeona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_mainframeonb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_mainframeonc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_mainframeond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_mainframeone_src'])
                    elif self.mainframe_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_mainframeoff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_reactor_id']: 
                    if self.reactor_on == True:
                        if self.sub_clock <= 1: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_reactorona_src'])
                        elif self.sub_clock <= 3: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_reactoronb_src'])
                        elif self.sub_clock <= 5: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_reactoronc_src'])
                        elif self.sub_clock <= 7: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                       image=self.img_dict['ship_reactorond_src'])
                        elif self.sub_clock <= 9: 
                            self.tk_frame.create_image(rect_left+10, rect_top+10,
                                                       image=self.img_dict['ship_reactorone_src'])
                    elif self.reactor_on == False: 
                        self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                                   image=self.img_dict['ship_reactoroff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_storage_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_storage_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_bed_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_floor_src'])
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_bed_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_blwallcorner_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_blwallcorner_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_tlwallcorner_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_tlwallcorner_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_brwallcorner_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_brwallcorner_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_trwallcorner_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_trwallcorner_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_enginemount_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_enginemount_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_enginetipoff_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_enginetipoff_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_lasermount_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10,
                                               image=self.img_dict['ship_lasermount_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_lasertip_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_lasertip_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_wall_h_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10,
                                               image=self.img_dict['ship_wall_h_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['ship_wall_v_id']: 
                    self.tk_frame.create_image(rect_left+10, rect_top+10, 
                                               image=self.img_dict['ship_wall_v_src'])
                if self.view_list[i_row][f_col] == self.tile_nr_dict['wood_tree_id']: 
                    self.add_background(rect_left, rect_top)
                    self.tk_frame.create_image(rect_left+10, rect_top+10,
                                               image=self.img_dict['wood_tree_src'])
            self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2)-285,
                                       image=self.img_dict['stat_dash_src'])
            for i in range(self.player_health):
                self.tk_frame.create_image(33+i*13, 23, image=self.img_dict['game_life_src'])
            for i in range(self.player_armor):
                self.tk_frame.create_image(33+i*13, 40, image=self.img_dict['game_armor_src'])
            for i in range(self.player_shield):
                self.tk_frame.create_image(33+i*13, 59, image=self.img_dict['game_shield_src'])
            for i in range(self.player_oxygen):
                self.tk_frame.create_image(33+i*13, 79, image=self.img_dict['game_oxygen_src'])
            for i in range(self.player_energy):
                self.tk_frame.create_image(188+i*13, 23, image=self.img_dict['game_energy_src'])
            for i in range(self.player_water):
                self.tk_frame.create_image(188+i*13, 40, image=self.img_dict['game_water_src'])
            for i in range(self.player_food):
                self.tk_frame.create_image(188+i*13, 59, image=self.img_dict['game_food_src'])
            for i in range(self.player_sleep):
                self.tk_frame.create_image(188+i*13, 79, image=self.img_dict['game_sleep_src'])
            for i in range(self.player_weight):
                self.tk_frame.create_image(346+i*13, 23, image=self.img_dict['game_weight_src'])
            for i in range(self.player_xp):
                self.tk_frame.create_image(346+i*13, 40, image=self.img_dict['game_xp_src'])
            for i in range(self.player_signal):
                self.tk_frame.create_image(346+i*13, 59, image=self.img_dict['game_signal_src'])
            for i in range(self.player_ammo):
                self.tk_frame.create_image(346+i*13, 79, image=self.img_dict['game_ammo_src'])
            if self.ship_cargo == True:
                self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2),
                                           image=self.img_dict['game_overlay_src'])
                self.crg_key = []
                self.crg_var = []
                for i in self.ship_storage:
                    self.crg_key += [i]
                    self.crg_var += [self.ship_storage[i]]
                for i in range(len(self.crg_key)):
                    self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2+ i*20)-100,
                                              text=self.crg_key[i], fill="green", font=("Helvetica", 14))
                    self.tk_frame.create_text(self.frame_width/2-150, (self.frame_height/2+ i*20)-100,
                                              text=self.crg_var[i], fill="green", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2, 150, text='SPACESHIP CARGO', fill="blue",
                                          font=("Helvetica", 18))
                self.tk_frame.create_text(self.frame_width/2+100, 215, text=self.cargo_option_selected,
                                          fill="red", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-100, 215, text='Currently selected:',
                                          fill="red", font=("Helvetica", 14))
            if self.ship_status == True:
                self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2),
                                           image=self.img_dict['game_overlay_src'])
                self.shp_key = []
                self.shp_var = []
                for i in self.ship_option:
                    self.shp_key += [i]
                    self.shp_var += [self.ship_option[i]]
                for i in range(len(self.shp_key)):
                    self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2+ i*20)-100,
                                              text=self.shp_key[i], fill="green", font=("Helvetica", 14))
                    self.tk_frame.create_text(self.frame_width/2-150, (self.frame_height/2+ i*20)-100,
                                              text=self.shp_var[i], fill="green", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2, 150, text='SPACESHIP STATUS', fill="blue",
                                          font=("Helvetica", 18))
                self.tk_frame.create_text(self.frame_width/2+100, 215, text=self.ship_option_selected,
                                          fill="red", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-100, 215, text='Currently selected:',
                                          fill="red", font=("Helvetica", 14))
            elif self.implant_interface == True:
                self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2),
                                           image=self.img_dict['game_overlay_src'])
                self.imp_key = []
                self.imp_var = []
                for i in self.interface_option:
                    self.imp_key += [i]
                    self.imp_var += [self.interface_option[i]]
                for i in range(len(self.imp_key)):
                    self.tk_frame.create_text(self.frame_width/2, 
                                              (self.frame_height/2+ i*20)-100, text=self.imp_key[i],
                                              fill="green", font=("Helvetica", 14))
                    self.tk_frame.create_text(self.frame_width/2-150, 
                                              (self.frame_height/2+ i*20)-100, 
                                              text=self.imp_var[i], fill="green", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2, 150, 
                                          text='AVR INTERFACE', fill="blue", font=("Helvetica", 18))
                self.tk_frame.create_text(self.frame_width/2+100, 215, 
                                          text=self.interface_option_selected, fill="red", 
                                          font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-100, 215, 
                                          text='Currently selected:', fill="red", font=("Helvetica", 14))
            elif self.inventory_display == True:
                self.tk_frame.create_image(self.frame_width/2, 
                                           (self.frame_height/2), image=self.img_dict['game_overlay_src'])
                self.inv_key = []
                self.inv_var = []
                for i in self.player_inventory:
                    self.inv_key += [i]
                    self.inv_var += [self.player_inventory[i]]
                for i in range(len(self.inv_key)):
                    self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2+ i*20)-100, 
                                              text=self.inv_key[i], fill="green", font=("Helvetica", 14))
                    self.tk_frame.create_text(self.frame_width/2-150, (self.frame_height/2+ i*20)-100,
                                              text=self.inv_var[i], fill="green", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2, 150, 
                                          text='INVENTORY', fill="blue", font=("Helvetica", 18))
                self.tk_frame.create_text(self.frame_width/2+100, 215, 
                                          text=self.inventory_option_selected, fill="red",
                                          font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-100, 215, 
                                          text='Currently selected:', fill="red", font=("Helvetica", 14))
            elif self.first_dialog == True:
                self.tk_frame.create_image(self.frame_width/2, (self.frame_height/2), 
                                           image=self.img_dict['game_overlay_src'])
                self.tk_frame.create_text(self.frame_width/2, 150, text='TRANSMISSION', fill="blue", 
                                          font=("Helvetica", 18))
                self.tk_frame.create_text(self.frame_width/2-40, 225, text='AI: You seem awake! Jolly good.',
                                          fill="green", font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-40, 255, 
                                          text='You: WTF where are we, who is talking', fill="green",
                                          font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-40, 285, 
                                          text='AI: Your syncronized general purpose AI', fill="green",
                                          font=("Helvetica", 14))
                self.tk_frame.create_text(self.frame_width/2-40, 315, 
                                          text='AI: We crashed and you need to rebuild', fill="green", 
                                          font=("Helvetica", 14))
                
                
                
class Player_Method:
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
        self.player_row_dir_vec = dist_row
        self.player_col_dir_vec = dist_col
        if self.player_row_dir_vec == self.player_row_vec and self.player_col_dir_vec == self.player_col_vec:
            self.player_row_vec = dist_row
            self.player_col_vec = dist_col
            if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == self.tile_nr_dict['ground_grass_id']: 
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['{}'.format(self.current_player_tile)]
                self.player_row_pos = self.player_row_pos + dist_row
                self.player_col_pos = self.player_col_pos + dist_col
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['player_id']
                self.current_player_tile = 'ground_grass_id'
            elif self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == self.tile_nr_dict['ship_dooropen_id']: 
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['{}'.format(self.current_player_tile)]
                self.player_row_pos = self.player_row_pos + dist_row
                self.player_col_pos = self.player_col_pos + dist_col
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['player_id']
                self.current_player_tile = 'ship_dooropen_id'
            elif self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == self.tile_nr_dict['ship_floor_id']:
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['{}'.format(self.current_player_tile)]
                self.player_row_pos = self.player_row_pos + dist_row
                self.player_col_pos = self.player_col_pos + dist_col
                self.grid_list[self.player_row_pos][self.player_col_pos] = self.tile_nr_dict['player_id']
                self.current_player_tile = 'ship_floor_id'
        else:
            self.player_row_vec = dist_row
            self.player_col_vec = dist_col
    def ability_activate(self):
        if self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_doorclosed_id']:
            self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] = self.tile_nr_dict['ship_dooropen_id']
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_dooropen_id']:
            self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] = self.tile_nr_dict['ship_doorclosed_id']
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_monitor_id']:
            if self.reactor_on == True and self.mainframe_on == True:
                if self.monitor_on == True:
                    self.monitor_on = False
                else:
                    self.monitor_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_assembler_id']:
            if self.reactor_on == True and self.mainframe_on == True:
                if self.assembler_on == True:
                    self.assembler_on = False
                else:
                    self.assembler_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_refinery_id']:
            if self.reactor_on == True and self.mainframe_on == True:
                if self.refinery_on == True:
                    self.refinery_on = False
                else:
                    self.refinery_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_mainframe_id']:
            if self.reactor_on == True:
                if self.mainframe_on == True:
                    self.mainframe_on = False
                else:
                    self.mainframe_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_lifesupport_id']:
            if self.reactor_on == True and self.mainframe_on == True:
                if self.lifesupport_on == True:
                    self.lifesupport_on = False
                else:
                    self.lifesupport_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_reactor_id']:
            if self.reactor_on == True:
                self.reactor_on = False
            else:
                self.reactor_on = True
        elif self.grid_list[self.player_row_pos + self.player_row_vec][self.player_col_pos + self.player_col_vec] == self.tile_nr_dict['ship_monitor_id']:
            if self.monitor_on == True:
                self.monitor_on = False
            else:
                self.monitor_on = True
    def inventory_toogle(self):
        self.inventory_display = True
    def interface_toogle(self):
        self.implant_interface = True
    def ship_toogle(self):
        self.ship_status = True
    def cargo_toogle(self):
        self.ship_cargo = True
    def repair_toogle(self):
        self.multitool_repair = True
    def first_dialog(self):
        self.first_dialog = True
        
class Game_Instances:
    def remove_overlays(self):
        self.inventory_display = False
        self.ship_cargo = False
        self.implant_interface = False
        self.ship_status = False
        self.multitool_repair = False
        self.first_dialog = False
    def write_ui_instance(self): 
        self.instance = 0
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 250, 
                                  text="Stars Transcending Continuum", fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 200, 
                                  text='Press [P] to play', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 150, 
                                  text='Power up devices with [E]', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 100, 
                                  text='Lookup inventory with [I]', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2) - 50, 
                                  text='Interact with devices [C]', fill="black")
        self.tk_frame.create_text(self.frame_width/2, (self.frame_height/2), 
                                  text='Exit tab, return to game [F]', fill="black")
    def write_first_instance(self):
        self.instance = 1
        self.write_board() 
        for i in range(3):
            for f in range(5):
                self.grid_list[39+i][38+f] = self.tile_nr_dict['ship_floor_id']
        self.grid_list[40][37] = self.tile_nr_dict['ship_monitor_id']
        self.grid_list[40][36] = self.tile_nr_dict['ship_lasermount_id']
        self.grid_list[40][35] = self.tile_nr_dict['ship_lasertip_id']
        self.grid_list[38][37] = self.tile_nr_dict['ship_tlwallcorner_id']
        self.grid_list[39][36] = self.tile_nr_dict['ship_tlwallcorner_id']
        self.grid_list[42][37] = self.tile_nr_dict['ship_blwallcorner_id']
        self.grid_list[41][36] = self.tile_nr_dict['ship_blwallcorner_id']
        for i in range(5):
            self.grid_list[38][38+i] = self.tile_nr_dict['ship_wall_h_id']
            self.grid_list[42][38+i] = self.tile_nr_dict['ship_wall_h_id']
        self.grid_list[39][37] = self.tile_nr_dict['ship_wall_v_id']
        self.grid_list[41][37] = self.tile_nr_dict['ship_wall_v_id']
        self.grid_list[39][38] = self.tile_nr_dict['ship_lifesupport_id']
        self.grid_list[41][38] = self.tile_nr_dict['ship_refinery_id']
        self.grid_list[39][39] = self.tile_nr_dict['ship_storage_id']
        self.grid_list[41][39] = self.tile_nr_dict['ship_reactor_id']
        self.grid_list[42][40] = self.tile_nr_dict['ship_doorclosed_id']
        self.grid_list[41][41] = self.tile_nr_dict['ship_mainframe_id']
        self.grid_list[41][42] = self.tile_nr_dict['ship_assembler_id']
        self.grid_list[39][42] = self.tile_nr_dict['ship_bed_id']
        self.grid_list[38][43] = self.tile_nr_dict['ship_trwallcorner_id']
        self.grid_list[42][43] = self.tile_nr_dict['ship_brwallcorner_id']
        self.grid_list[39][43] = self.tile_nr_dict['ship_enginemount_id']
        self.grid_list[41][43] = self.tile_nr_dict['ship_enginemount_id']
        self.grid_list[39][44] = self.tile_nr_dict['ship_enginetipoff_id']
        self.grid_list[41][44] = self.tile_nr_dict['ship_enginetipoff_id']
        self.grid_list[40][43] = self.tile_nr_dict['ship_wall_v_id']
        for i in range(59):
            self.grid_list[21][21+i] = self.tile_nr_dict['wood_tree_id']
            self.grid_list[79][21+i] = self.tile_nr_dict['wood_tree_id']
        for i in range(57):
            self.grid_list[22+i][21] = self.tile_nr_dict['wood_tree_id']
            self.grid_list[22+i][79] = self.tile_nr_dict['wood_tree_id']
        self.move_player(1,1)
        self.timer_clock()
        
class Game_Init(tk.Tk, Image_Fetch, Rendering_World, Game_Mechanics, Game_Variables, Game_Instances, Player_Method):
    def __init__(self):
        super().__init__()
        self.bind("<Key>", self.key_pressed)
        self.tk_frame = tk.Canvas(self, width=self.frame_width, height=self.frame_height) 
        self.tk_frame.pack()
        self.fetching_img()
        self.write_ui_instance()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
init_grid = Game_Init()
init_grid.mainloop()