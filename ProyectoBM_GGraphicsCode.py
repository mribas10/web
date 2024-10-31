# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:34:33 2024

@author: Alumne_mati1
"""
#IMPORT------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import os

#WINDOW1: LOGIN----------------------------------------------------------------
if 'w1' not in st.session_state:
    st.session_state['w1'] = False
    st.session_state['w2'] = False
    st.session_state['w3'] = False

if not st.session_state['w1']:
    st.title("GGràfics: Generador de Gràfiques per a Professionals i Estudiants")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if  username == "BGMolina" and password == "bgm":
            st.success("Login successful!")
            st.session_state['w1'] = True
            st.session_state['w2'] = True

            
        else:
            st.error("Invalid username or password")
#WINDOW2:TIPO CARACTERIZACION--------------------------------------------------            

if st.session_state['w2']:
    st.title("GGràfics")
    caracterizations = ['','FT-IR', 'TGA', 'DSC', 'UV-VIS', 'WCA', 'Perfilometry', 'Cyclic Voltammetry']
    selecCar = st.selectbox('Select the characterization technique', list(caracterizations))
    if selecCar == 'FT-IR':
        typeIR = ['Absorbance', 'Transmittance']
        selecCarIR = st.selectbox('Select the FT-IR technique', list(typeIR))
    else:
        print('Working on it!')

    sname = st.text_input('Sample name')
    dataD = st.text_input('Data document (.csv)') #buscar otra manera
   
    
    if st.button('Next'):
        st.session_state['w2'] = True
        st.session_state['w3'] = True

#V3:GRAFICO -------------------------------------------------------------------

if st.session_state['w3']:
    colum1, colum2 = st.columns([1, 2], gap = "large") 
    with colum1:
        #V3c1:Graph FORMAT PARAMETERS -----------------------------------------
        st.title("Format")
        axisX = st.text_input('Axis x range (From,To)')
        axisY = st.text_input('Axis y range (From,To)')
        fonts = {'Times New Roman': 'Times New Roman', 'Arial': 'Arial', 'Calibri': 'Calibri', 'Verdana': 'Verdana'}
        selected_font = st.selectbox('Select font', list(fonts.keys()))
        slider_val = st.slider("Font size", min_value=10, max_value=40, value=10)
        checkbox_val = st.checkbox('Show Legend', value=True)
        checkbox_title = st.checkbox('Show Title', value=True)
        lcolor = {'black': 'black', 'red': 'red', 'blue': 'blue', 'green': 'green'}
        colors = st.selectbox('Select line color', list(lcolor.keys()))
   
    with colum2:
        #V3c2:Graph -----------------------------------------------------------
        st.title("Graph")
        
        fig, ax = plt.subplots()
        dataD1 = pd.read_csv(dataD, header=0, sep=";")
        ax.plot(dataD1['label x'], dataD1['label y'], color=lcolor[colors], label=sname)
        ax = plt.gca()
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)
        
        ax.tick_params(direction='out', length=10, width=2)
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(slider_val-4)
            label.set_fontname(selected_font)
            label.set_fontweight('bold')   
        
        try:
            x_min, x_max = map(float, axisX.split(','))
            ax.set_xlim(x_min, x_max)
            y_min, y_max = map(float, axisY.split(','))
            ax.set_ylim(y_min, y_max)
        except ValueError:
                st.error("Invalid axis range input.")
        
        if checkbox_val:
            ax.legend(fontsize=slider_val,loc='best',frameon=False,
                      prop={'family': selected_font,'size': slider_val,
                            'weight': 'bold'})
        if checkbox_title:
            ax.set_title(sname, fontsize=slider_val, fontname=selected_font, fontweight='bold')
        
   
        #V3c2:Graph FT-IT -----------------------------------------------------
        if selecCar == 'FT-IR':
            ax.set_xlabel('Wavenumber (cm-1)', fontsize=slider_val, fontname=selected_font, fontweight='bold')
            if selecCarIR == 'Absorbance':
                ax.set_ylabel('Absorbance (a.u.)', fontsize=slider_val, fontname=selected_font, fontweight='bold') 
            else :
                ax.set_ylabel('Transmittance (a.u.)', fontsize=slider_val, fontname=selected_font, fontweight='bold') 
        
        #V3c2:VIEW AND SAVE --------------------------------------------------
        if st.button('GGGràfics'):
            st.pyplot(fig)

        user_directory = st.text_input('Enter the folder directory')
        if st.button('Save'):
            if user_directory:
                if not os.path.exists(user_directory):
                    os.makedirs(user_directory)
                # File name and save
                #file_path = os.path.join(user_directory, f"{sname}.png")
                st.pyplot(fig)
                plt.savefig(file_path, dpi=300, bbox_inches='tight')
                st.success(f"Saved as: {sname}.png in {user_directory}.")
                plt.clf()  # Clear the figure
            else:
                st.error("Please specify a directory to save the plot.") 

#FIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            
            
            



        



        

                  
        
        
       
       
         

    
    

            
        


