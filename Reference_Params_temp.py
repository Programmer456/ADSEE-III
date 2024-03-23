import numpy as np
import matplotlib.pyplot as plt

class Reference_Params:
    'NOTES'
    # ENGINE OPTION: R-R Tay Mk 620-15

    'UNIT CONVERSIONS'
    inch = 0.0254   # [m]
    foot = 0.3048   # [m]

    'FUSELAGE GEOMETRY'
    l_fus = 32.5             # [m]
    l_cabin = 21.19          # [m]
    l_seating_area = 18.8    # [m]
    seat_pitch = 32*inch     # [m]
    d_fus = 3.3              # [m]

    'MASSES'
    MTOM = 43090    # [Kg], FROM: http://www.fokker-aircraft.info/f100general.htm
    OEM = 24272     # [Kg], FROM: http://www.fokker-aircraft.info/f100general.htm
    MZFM = 35835    # [Kg], FROM: http://www.fokker-aircraft.info/f100general.htm
    MFM = 10293     # [Kg], full tanks
    MLM = 38780     # [kg], FROM: http://www.fokker-aircraft.info/f100general.htm
    MPM = 11242     # [Kg], FROM: http://www.fokker-aircraft.info/f100general.htm

    M_wing = 0.1477*MTOM            # [Kg]
    M_htail = 0.0137 * MTOM         # [Kg]
    M_vtail = 0.95/100 * MTOM       # [Kg]
    M_fus = 0.1929 * MTOM           # [Kg]
    M_nose_gear = 0.47/100 * MTOM   # [Kg]
    M_main_gear = 2.71/100 * MTOM   # [Kg]
    M_nacelle = 1.83/100 * MTOM     # [Kg]
    M_prop = 9.12/100 * MTOM        # [Kg]

    'PROPULSION GROUP'
    d_fan = 44*inch         # [m]
    d_nacelle =
    x_cg_engine = 23607/1000 # [m], wrt nose, FROM: Towards a Stall Model for the Fokker 100

    'WING GEOMETRY'
    cw_r = 5.28 # [m]
    cw_t = 1.26 # [m]
    bw = 28.08 # [m]
    Aw = 8.4 # [-]
    Sw = 93.5               # [m^2]
    x_w_r =
    sweep_le_w =
    sweep_quarter_chord_w = 17.45*np.pi/180 # [rad]
    taper_rat_w =
    S_net_w =
    x_40percent_MAC = 17330/1000 # [m], wrt nose, FROM: Towards a Stall Model for the Fokker 100
    x_lemac = 15799/1000 # [m], wrt nose, FROM: Towards a Stall Model for the Fokker 100
    x_ac_w = # from wierd graph
    x_main_gear = 17649 # [m], wrt nose, FROM: Towards a Stall Model for the Fokker 100

    'HSTAB GEOMETRY'
    ch_r =
    ch_t =
    bh = 10.04 # [m]
    Ah =
    Sh = 17.76          # [m^2]
    sweep_le_h =
    taper_rat_h =
    Vh_V = 1
    x_half_chord_h = 32801/1000 # [m], wrt nose, FROM: Towards a Stall Model for the Fokker 100

    'FLIGHT PERFORMANCE'

    def calculate_MAC(self):
        return

    def calculate_sweep_angle(self, chord_ratio: float):
        return

    def calculate_CLah(self, Mach: float,):
        return

    def calculate_CLa_w(self, Mach: float, ):
        return

    def calculate_CLa_Aminush(self):
        return

    def calculate_downwash_grad(self):
        return

    def calculate_xac_wf(self):
        return



length_total = 35.53 # meters ( maybe includes tail)
height_total = 8.51 # meters
length_fuselage = 32.5 #meters
height_fuselage = 3.3 #meters
b = 28.08 #meters
mac = 0 #TO BE FOUND ADSEE II SLIDES FORMULAS
mac_h =  0
chord_root = 5.28 #meters
chord_tip = 1.26 #meters
Ar = 8.4 #meters
b_h = 10.04 #meters
wheelbase = 14.01 #meters
wheeltrack = 5.04 #meters
lenght_seatingarea = 18.8 #meters
lenght_cabin = 21.19 #meters excluding flight deck
Sh = 17.76 #m^2
S = 93.5 #m^2
'weight [c]'
OEW = 24747 #Kg
MZFW = 36740 #Kg
MRW = 46040 #Kg
MTOW = 45810 #Kg
MLW = 39915 #Kg
MPW = 11993 #Kg
V_app_max = 241*3.6 #m/s
Vh_V = 1 # T- Tail vh/v








