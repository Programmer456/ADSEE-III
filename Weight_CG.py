import numpy as np
import matplotlib.pyplot as plt
import Reference_Parameters as ref




def mtom_pie_chart():
    MTOM = ref.MTOW
    OEM = ref.OEW
    MFM = ref.MTOW - OEM - ref.MPW
    MPM = ref.MPW

    labels = 'OEM', 'MFM', 'MPLM'
    masses = [OEM, MFM, MPM]

    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(masses, labels=labels, autopct='%1.1f%%',
           shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
    plt.show()


mtom_pie_chart()
