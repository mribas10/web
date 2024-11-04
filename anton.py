# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:34:29 2024

"""

# Import streamlit Library
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# importing subprocess module 
#import subprocess
import os

# =============================================================================
# # #------ Declaration of Definition -------
# =============================================================================

# def my_pass():
    
#     text = " The analysis of the requeriment shown a complied achievement the requeriment by the WTG"  
    
#     text_input = st.text_input("Enter Conclusion of the Test 👇")
#     if text_input:
#         write_box =  st.write("You have entered: ", text_input)
            
#     return write_box

# def nopassed():
    
#     text = " The analysis of the requeriment shown a failure of the device to achievement the tast"
#     text_input = st.text_input("Enter Conclusion of the Test 👇")
#     if text_input:
#         write_box = st.write("You have entered: ", text_input)
        
#     return write_box

# def triangle_of_power (parameter_active_power, parameter_reactive_power):
    
#     apparent_power = math.sqrt(parameter_active_power**2 + parameter_reactive_power**2)
    
#     return apparent_power

# #def cosphi (parameter_active_power, parameter_reactive_power):
#     #cosphi_tang = math.atan(parameter_reactive_power/parameter_active_power)
# #    cosphi_tang = math.tan(parameter_reactive_power/parameter_active_power)
    
# #    return cosphi_tang

# def active_power_output (parameter_voltage, parameter_current,tang_phi):
    
#     #angle_phi = math.atan(tang_phi)
#     angle_degree = math.degrees(tang_phi)
#     cos_phi      = math.cos(math.radians(angle_degree))
#     sinus_phi    = math.sin(math.radians(angle_degree))
#     print(angle_degree)
#     #print(cos_phi)
#     #print(sinus_phi)
#     print("bring Values")
   
#     print ("Inside def Voltage",parameter_voltage)
#     print ("Inside def Current",parameter_current)
    
#     calculated_active_power = math.sqrt(3)*parameter_voltage*parameter_current*cos_phi
#     calculated_reactive_power = math.sqrt(3)*parameter_voltage*parameter_current*sinus_phi
        
#     return calculated_active_power,calculated_reactive_power

@st.cache_data
def csv (df_WTG_File, WTGs_analysis, WTGs_LVRT_HVRT):
    
	return df_WTG_File,WTGs_analysis, WTGs_LVRT_HVRT



# =============================================================================
# # #------- Variables -------
# =============================================================================
# apparent_power = 0 
# #cosphi_tang    = 0
# calculated_active_power   = 0
# calculated_reactive_power = 0
# tang_phi       = 0.434 # Angle is similar than 25 degree
taula_images = {''}
# var_iloc_P     = []
# var_iloc_Q     = []
# var_iloc_time  = []
        
# =============================================================================
# #-----------------Upload CSV file and read it ----------------------------------
# =============================================================================




df_WTG_File = pd.read_csv("WTG_Step_4_25ms.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

#mere df_WTG_File.to_excel (r'WTG_Step_25ms.xlsx', index = None, header=True)

#mere WTGs_analysis = pd.read_excel(r"WTG_Step_25ms.xlsx", skiprows=2) # r is used before absolute file path 

WTGs_analysis = df_WTG_File.drop(0)

#mere WTGs_LVRT_HVRT = pd.read_excel(r"LVRT_HVRT.xlsx", skiprows=2)#Fault Ride-though Analysis
WTGs_LVRT_HVRT = pd.read_excel(r"LVRT_HVRT.xlsx")
csv(df_WTG_File,WTGs_analysis,WTGs_LVRT_HVRT)


# =============================================================================
# introduce Pag Title (aligned) and intro Web page for reference
# =============================================================================
#st.title("Instantaneous Performance of Wind Turbines")  # add a title

st.markdown("<h1 style='text-align: center; color: grey;'>Instantaneous Performance of Wind Turbines</h1>", unsafe_allow_html=True)

st.header("Analysis of Grid Compliance Tests based in the IEC International Standard")# add a Header fro Title


# link the pag with a website

url = "https://webstore.iec.ch/en/publication/29528"
st.write("check the Standard with this [link] (%s)" % url,unsafe_allow_html=True)
#st.markdown("check the Standard in with this [link](%s)" % url,unsafe_allow_html=True)

# =============================================================================
# #--------------Sidebar---------------
# =============================================================================
is_wind = st.sidebar.selectbox(
    "International Standard: Wind turbines –Part 21",
    ("Active Power", "Reactive Power", "FRT for LVRT", "FRT for HVRT", "PQ capability","Tolerance Band")
)

# Using "with" notation (this should be linked with the analysis of the plots)
with st.sidebar:
    add_radio = st.radio(
        "Final Decision of the Test:",
        ("Passed", "No Passed")
    )    
# =============================================================================
# SECOND STEP SPLIT SCREEN IN TWO PARTS
# =============================================================================

# =============================================================================
# # #---------Split Screen into 2 Columns Comparation ----------

col_Req_1, col_Data_2 = st.columns(2)

with col_Req_1:

#--------------Import png file----------
# Adding Requeriment Images and create a Table
#   I can sellect the image
    try: 

        taula_images = { "Active Power"  :"ActiveSet_Point.png", 
                     "Reactive Power":"Reactive_set_point.png",
                     "FRT for LVRT"  :"LVRT.png", 
                     "FRT for HVRT"  :"HVRT.jpg",
                     "PQ capability" :"PQ_Capability.png",
                     "Tolerance Band":"Tole_band.png"}
                 
#--- I select the image from the folder using the Sidebar Selector (above)
   
        image_name = "./img/"+ taula_images[is_wind]
        st.subheader("Requeriment Selected:"  + is_wind)
        st.image(image_name, caption= is_wind, width=350)

# =============================================================================
# # TEXT TO BE INTRODUCE BELOW each Rqueriment
# =============================================================================

        if is_wind == "Active Power":
            text_P = st.write('''The ability of the wind turbine to operate in active power control mode shall be characterized
                       for various reference values given by the control interface. The aim of this test is to determine
                       the response of the WT to reference commands regarding the static error, the rise time and
                       the settling time of active power, for both steady-state conditions and under dynamic
                        response conditions.''')
                                    
        elif is_wind == "Reactive Power":
            
            text_Q = st.write(''' The aim of this test is to determine the response of the WT to reference commands regarding
                                  the static error, the rise time and the settling time of reactive power using either reactive
                                   power, voltage or cos φ reference values, depending on the wind turbine control system as
                                   specified by the manufacturer''')

        elif  is_wind == "FRT for LVRT":
            text_LVRT = st.write('''The ability of a wind turbine or wind power plant to stay connected during voltage dips.
                                 The test is intended to verify the wind turbine response to undervoltage 
                                 The test is intended to verify the wind turbine response to undervoltage
                                 events (due to e.g. grid faults, switching operations) and providing a basis for wind turbine
                                 numerical simulation model validation. ''')

        elif  is_wind == "FRT for HVRT":
            text_HVRT = st.write('''The ability of a wind turbine or wind power plant to stay connected during voltage dips.
                                 The test is intended to verify the wind turbine response to undervoltage 
                                 The test is intended to verify the wind turbine response to undervoltage
                                 events (due to e.g. grid faults, switching operations) and providing a basis for wind turbine
                                 numerical simulation model validation. ''')
             
        elif  is_wind == "PQ capability":
            text_PQ = st.write(''' The ability of a wind turbine or wind power plant to stay connected during voltage dips.
                                 The test is intended to verify the wind turbine response to undervoltage 
                                 The test is intended to verify the wind turbine response to undervoltage
                                 events (due to e.g. grid faults, switching operations) and providing a basis for wind turbine
                                 numerical simulation model validation. ''')

        elif  is_wind == "Tolerance Band":
            text_PQ = st.write(''' The maximum permissible tolerance is calculated  ± 5 %. ''')

# If there is any issue the program should give this erro 
    except Exception as e:
         st.error(" No he pogut carregar la imatge" + image_name)
         print (e)

# =============================================================================
# #--------------Column 2
# =============================================================================
with col_Data_2:
         ####-- Header and Subheader
    st.subheader("Requeriment Analysed:"  + is_wind)
    if is_wind == "Active Power":
                
####--Create a Figure to be add data

        plt.figure(constrained_layout=True, figsize =(7, 7))

        plt.title('Active Power Set-Point',fontweight ="bold",size=18)
        #plt.suptitle('Figure')
        plt.xlabel('"Time in seconds"',size=12)
        plt.ylabel('Active Power (MW)',size=12)

        # Adding a grid to the Figure
        plt.grid()
        plt.legend(['Active Power'],loc='upper right')

        # Showing the plot with the data 
        var_time  = WTGs_analysis.iloc[2:,0]
        var_P     = WTGs_analysis.iloc[2:,1]
        plt.plot(var_time ,var_P)
        plt.savefig("Active Power Set-Point.png")

#--- I select the image from the folder using the Sidebar Selector (above)
        #image_Pdata = "./Final_Project/"
        st.image("Active Power Set-Point.png", caption= is_wind) 
                
        # =============================================================================
        #         Enter Input text for final decision of Test
        
        if add_radio == "Passed":
            text = " The analysis of test shown a complied achievement the requeriment by the WTG"  
        
            text_input = st.text_input("Enter Conclusion of the Test 👇")
            if text_input:
                st.write("You have entered: " +  text)
                st.write(text_input)
        # elif add_radio == No Passed:
        #     text = " The analysis of the requeriment shown a failure of the device to achievement the tast."
        #     text_input = st.text_input("Enter Conclusion of the Test 👇")
        #     if text_input:
        #         st.write("You have entered: "+ text + text_input)
                
            
        # my_pass()
         
        # nopassed()

            
    elif is_wind == "Reactive Power":
        
        ####--Create a Figure to be add data
        plt.figure(constrained_layout=True, figsize =(7, 7))

        plt.title('Reactive Power Set-Point',fontweight ="bold",size=18)
        #plt.suptitle('Figure')
        plt.xlabel('"Time in seconds"',size=12)
        plt.ylabel('Reactive Power (Mvar)',size=12)

    # Adding a grid to the Figure
        plt.grid()
        plt.legend(['Reactive Power'],loc='upper right')

      # Showing the plot with the data 
        var_time  = WTGs_analysis.iloc[2:,0]
        var_Q     = WTGs_analysis.iloc[2:,9]
        plt.plot(var_time ,var_Q)
        plt.savefig("Reactive Power Set-Point.png")

        #--- I select the image from the folder using the Sidebar Selector (above)
                #image_Pdata = "./Final_Project/"
        st.image("Reactive Power Set-Point.png", caption= is_wind) 
        # =============================================================================
        #         Enter Input text for final decision
        if add_radio == "Passed":
            text = " The analysis of test shown a complied achievement the requeriment by the WTG"  
        
            text_input = st.text_input("Enter Conclusion of the Test 👇")
            if text_input:
                st.write("You have entered: " +  text)
                st.write(text_input)

    elif is_wind == "FRT for LVRT":
        
        ####--Create a Figure to be add data
        plt.figure(constrained_layout=True, figsize =(7, 7))

        plt.title('LVRT Analysis',fontweight ="bold",size=18)
        #plt.suptitle('Figure')
        plt.xlabel('"Time in seconds"',size=12)
        plt.ylabel('Voltage (kV)',size=12)

    # Adding a grid to the Figure
        plt.grid()
        plt.legend(['Reactive Power'],loc='upper right')

      # Showing the plot with the data 
        var_time  = WTGs_LVRT_HVRT.iloc[2:,0]
        var_Q     = WTGs_LVRT_HVRT.iloc[2:,1]
        plt.plot(var_time ,var_Q)
        plt.savefig("LVRT.png")

        #--- I select the image from the folder using the Sidebar Selector (above)
                #image_Pdata = "./Final_Project/"
        st.image("LVRT.png", caption= is_wind)
       # st.markdown(""Write Conslusion: ", st.text_input("")

    elif is_wind == "FRT for HVRT":
        
        ####--Create a Figure to be add data
        plt.figure(constrained_layout=True, figsize =(7, 7))

        plt.title('HVRT Analysis',fontweight ="bold",size=18)
        #plt.suptitle('Figure')
        plt.xlabel('"Time in seconds"',size=12)
        plt.ylabel('Voltage (kV)',size=12)

    # Adding a grid to the Figure
        plt.grid()
        plt.legend(['Reactive Power'],loc='upper right')

      # Showing the plot with the data 
        var_time  = WTGs_LVRT_HVRT.iloc[2:,0]
        var_Q     = WTGs_LVRT_HVRT.iloc[2:,5]
        plt.plot(var_time ,var_Q)
        plt.savefig("HVRT.png")

        #--- I select the image from the folder using the Sidebar Selector (above)
                #image_Pdata = "./Final_Project/"
        st.image("HVRT.png", caption= is_wind)

        # =============================================================================
        #         Enter Input text for final decision
        if add_radio == "Passed":
            text = " The analysis of test shown a complied achievement the requeriment by the WTG"  
        
            text_input = st.text_input("Enter Conclusion of the Test 👇")
            if text_input:
                st.write("You have entered: " +  text)
                st.write(text_input)

    elif is_wind == "PQ capability":
        # =============================================================================
        #         # opening file_1.py and reading it with read() and executing if with exec()
        # =============================================================================
        print("removed code")
        #subprocess.run(["python", "Ideal_Data_CSV_PQ_Capability_Plots.py"])
        # running other file using run()
        
        
        #os.system("Ideal_Data_CSV_PQ_Capability_Plots.py")
         
        #plt.savefig("PQ_Capability.png")
        

# =============================================================================
#         # opening file_1.py and reading it with read() and executing if with exec()
# =============================================================================
        # with open("Ideal_Data_CSV_PQ_Capability_Plots.py") as file:
        #     exec(file.read())
        # running other file using run() 

        # =============================================================================
#         var_columns = WTGs_LVRT_HVRT.groupby.iloc[2:,1]
#         print (var_columns)
#         ####--Create a Figure to be add data
#         plt.figure(constrained_layout=True, figsize =(7, 7))
# 
#         plt.title('PQ Capability Analysis',fontweight ="bold",size=18)
#         #plt.suptitle('Figure')
#         plt.xlabel('"Reactive Power"',size=12)
# #         plt.ylabel('Active Power (kV)',size=12)
#     # Adding a grid to the Figure
#         plt.grid()
#         plt.legend(['Reactive Power'],loc='upper right')

#       # Showing the plot with the data 
#       # Selectiong Rows for do Mean Value for Active Power WTG 1.1
       
#         var_time  = WTGs_analysis.iloc[2:,0]
#         var_Q     = WTGs_analysis.iloc[2:,1]
#         plt.plot(var_time ,var_Q)
#         plt.savefig("PQ_Capability.png")
        
# =============================================================================

        # =============================================================================
        #         Enter Input text for final decision
        if add_radio == "Passed":
            text = " The analysis of test shown a complied achievement the requeriment by the WTG"  
        
            text_input = st.text_input("Enter Conclusion of the Test 👇")
            if text_input:
                st.write("You have entered: " +  text)
                st.write(text_input)

        #--- I select the image from the folder using the Sidebar Selector (above)
                #image_Pdata = "./Final_Project/"
#         st.image("HVRT.png", caption= is_wind)
                 

