import numpy as np
from matplotlib.patches import ConnectionPatch

def conn_lines(Te1, Te2, Tc, Ps, Pc, Pm, Ne, Nb, Rc, Be, df, df_t, x_ptl, multi_cept, ax, ax1t, x, ax2t, ax3t, lwidth, connector_color):
    # ====================================== FIND INTERSECTIONS

    Te1_idx = np.argwhere(np.diff(np.sign(Te1 - [float(df_t[df['Engine Output (%)'] == x_ptl]['Te1']) for i in range (len(Te1))]))).flatten()
    Te2_idx = np.argwhere(np.diff(np.sign(Te2 - [float(df_t[df['Engine Output (%)'] == x_ptl]['Te2']) for i in range (len(Te2))]))).flatten()
    Tc_idx = np.argwhere(np.diff(np.sign(Tc - [float(df_t[df['Engine Output (%)'] == x_ptl]['Tc']) for i in range (len(Tc))]))).flatten()
    Ps_idx = np.argwhere(np.diff(np.sign(Ps - [float(df_t[df['Engine Output (%)'] == x_ptl]['Ps']) for i in range (len(Ps))]))).flatten()
    Pc_idx = np.argwhere(np.diff(np.sign(Pc - [float(df_t[df['Engine Output (%)'] == x_ptl]['Pc']) for i in range (len(Pc))]))).flatten()
    Pm_idx = np.argwhere(np.diff(np.sign(Pm - [float(df_t[df['Engine Output (%)'] == x_ptl]['Pm']) for i in range (len(Pm))]))).flatten()
    Ne_idx = np.argwhere(np.diff(np.sign(Ne - [float(df_t[df['Engine Output (%)'] == x_ptl]['Ne']) for i in range (len(Ne))]))).flatten()
    Nb_idx = np.argwhere(np.diff(np.sign(Nb - [float(df_t[df['Engine Output (%)'] == x_ptl]['Nb']) for i in range (len(Nb))]))).flatten()
    Rc_idx = np.argwhere(np.diff(np.sign(Rc - [float(df_t[df['Engine Output (%)'] == x_ptl]['Rc']) for i in range (len(Rc))]))).flatten()
    Be_idx = np.argwhere(np.diff(np.sign(Be - [float(df_t[df['Engine Output (%)'] == x_ptl]['Be']) for i in range (len(Be))]))).flatten()

    # =================================== Penanganan jika ada nilai yang tidak memiliki x-intersection

    Te1_idx_ = Te1_idx if len(Te1_idx) > 0 else (x_ptl-50)*10-1
    Te2_idx_ = Te2_idx if len(Te2_idx) > 0 else (x_ptl-50)*10-1
    Tc_idx_ = Tc_idx if len(Tc_idx) > 0 else (x_ptl-50)*10-1
    Ps_idx_ = Ps_idx if len(Ps_idx) > 0 else (x_ptl-50)*10-1
    Pc_idx_ = Pc_idx if len(Pc_idx) > 0 else (x_ptl-50)*10-1
    Pm_idx_ = Pm_idx if len(Pm_idx) > 0 else (x_ptl-50)*10-1
    print(Pm_idx, Pm_idx_, x_ptl)
    Ne_idx_ = Ne_idx if len(Ne_idx) > 0 else (x_ptl-50)*10-1
    Nb_idx_ = Nb_idx if len(Nb_idx) > 0 else (x_ptl-50)*10-1
    Rc_idx_ = Rc_idx if len(Rc_idx) > 0 else (x_ptl-50)*10-1
    Be_idx_ = Be_idx if len(Be_idx) > 0 else (x_ptl-50)*10-1

    # ================================== Penanganan jika ada nilai yang memiliki 2 intercept

    Te1_idx = multi_cept(Te1_idx_, x_ptl)
    Te2_idx = multi_cept(Te2_idx_, x_ptl)
    Tc_idx = multi_cept(Tc_idx_, x_ptl)
    Ps_idx = multi_cept(Ps_idx_, x_ptl)
    Pc_idx = multi_cept(Pc_idx_, x_ptl)
    Pm_idx = multi_cept(Pm_idx_, x_ptl)
    Ne_idx = multi_cept(Ne_idx_, x_ptl)
    Nb_idx = multi_cept(Nb_idx_, x_ptl)
    Rc_idx = multi_cept(Rc_idx_, x_ptl)
    Be_idx = multi_cept(Be_idx_, x_ptl)

    # ==================================== Penanganan jika ada nilai -1
    Te1_idx_ = 0 if Te1_idx == -1 else Te1_idx
    Te2_idx_ = 0 if Te2_idx == -1 else Te2_idx
    Tc_idx_ = 0 if Tc_idx == -1 else Tc_idx
    Ps_idx_ = 0 if Ps_idx == -1 else Ps_idx
    Pc_idx_ = 0 if Pc_idx == -1 else Pc_idx
    Pm_idx_ = 0 if Pm_idx == -1 else Pm_idx
    Ne_idx_ = 0 if Ne_idx == -1 else Ne_idx
    Nb_idx_ = 0 if Nb_idx == -1 else Nb_idx
    Rc_idx_ = 0 if Rc_idx == -1 else Rc_idx
    Be_idx_ = 0 if Be_idx == -1 else Be_idx
    
            
    # ==================================== Scatter Plot Intersection

    # ax[0].plot(x[Te1_idx], Te1[Te1_idx], 'ro')
    # ax[0].plot(x[Tc_idx], Tc[Tc_idx], 'ro')
    # ax[0].plot(x[Te2_idx], Te2[Te2_idx], 'ro')

    ax[0].scatter(x_ptl, Te1[Te1_idx_], marker = '*', color = 'magenta', s = 100)
    ax[0].scatter(x_ptl, Tc[Tc_idx_], marker = '*', color = 'magenta', s = 100)
    ax[0].scatter(x_ptl, Te2[Te2_idx_], marker = '*', color = 'magenta', s = 100)

    ax1t.plot(x[Pc_idx_], Pc[Pc_idx_], 'ro')
    ax[1].plot(x[Ps_idx_], Ps[Ps_idx_], 'ro')
    ax1t.plot(x[Pm_idx_], Pm[Pm_idx_], 'ro')
    ax[2].plot(x[Ne_idx_], Ne[Ne_idx_], 'ro')
    ax2t.plot(x[Nb_idx_], Nb[Nb_idx_], 'ro')
    ax[3].plot(x[Be_idx_], Be[Be_idx_], 'ro')
    ax3t.plot(x[Rc_idx_], Rc[Rc_idx_], 'ro')

    # =================================== Menghubungkan titik2

    # -------------------------- Koneksi Te1, Tc, & Te2
    ax[0].plot([x_ptl, x_ptl, x_ptl], [Te1[Te1_idx_], 
                Tc[Tc_idx_], Te2[Te2_idx_]],
                linewidth = lwidth,
                color = 'magenta')

    # -------------------------- Koneksi Pm -> Pc
    ax1t.plot([x[Pm_idx_], x[Pc_idx_]], [Pm[Pm_idx_], Pc[Pc_idx_]],
                linewidth = lwidth,
                color = 'magenta')

    # -------------------------- Koneksi Pc -> Ps
    Pc_Ps = ConnectionPatch(xyA=(x[Pc_idx_], Pc[Pc_idx_]), 
                            xyB=(x[Ps_idx_], Ps[Ps_idx_]), 
                            coordsA="data", 
                            coordsB="data", 
                            axesA = ax1t, 
                            axesB = ax[1], 
                            linewidth = lwidth,
                            color = connector_color )
    ax1t.add_artist(Pc_Ps)

    # -------------------------- Koneksi Ps -> Nb
    Ps_Nb = ConnectionPatch(xyA=(x[Ps_idx_], Ps[Ps_idx_]), 
                            xyB=(x[Nb_idx_], Nb[Nb_idx_]), 
                            coordsA="data", 
                            coordsB="data", 
                            axesA = ax[1], 
                            axesB = ax2t, 
                            linewidth = lwidth,
                            color = connector_color )
    ax2t.add_artist(Ps_Nb)

    # -------------------------- Koneksi Nb -> Ne
    Nb_Ne = ConnectionPatch(xyA=(x[Nb_idx_], Nb[Nb_idx_]), 
                            xyB=(x[Ne_idx_], Ne[Ne_idx_]), 
                            coordsA="data", 
                            coordsB="data", 
                            axesA = ax2t, 
                            axesB = ax[2], 
                            linewidth = lwidth,
                            color = connector_color )
    ax2t.add_artist(Nb_Ne)

    # -------------------------- Koneksi Ne -> Rc
    Ne_Rc = ConnectionPatch(xyA=(x[Ne_idx_], Ne[Ne_idx_]), 
                            xyB=(x[Rc_idx_], Rc[Rc_idx_]), 
                            coordsA="data", 
                            coordsB="data", 
                            axesA = ax[2], 
                            axesB = ax3t, 
                            linewidth = lwidth,
                            color = connector_color )
    ax3t.add_artist(Ne_Rc)

    # -------------------------- Koneksi Rc -> Be
    Rc_Be = ConnectionPatch(xyA=(x[Rc_idx_], Rc[Rc_idx_]), 
                            xyB=(x[Be_idx_], Be[Be_idx_]), 
                            coordsA="data", 
                            coordsB="data", 
                            axesA = ax3t, 
                            axesB = ax[3], 
                            linewidth = lwidth,
                            color = connector_color )
    ax3t.add_artist(Rc_Be)
