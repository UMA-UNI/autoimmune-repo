# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:32:08 2023

@author: Uma R
"""

import pandas as pd
from PIL import Image
import numpy as np
import pickle
import streamlit as st
loadmodel=pickle.load(open('C:/Users/Uma R/psofeat_modelpickle.sav', 'rb'))

def arthritis_prediction(inputs):    

    idp=np.asarray(inputs)
    
    idps=idp.reshape(1,-1)
    
    prediction=loadmodel.predict(idps)
    prediction_prob=loadmodel.predict_proba(idps)
    print(prediction)
    
    st.subheader('Prediction ')
    st.write(prediction)
    
    st.write(""" 
             **1** : Autoimmune Arthritis Disease: Present \n
             **0**: Autoimmune Arthritis Disease: Absent
             """)
    
    st.subheader('Prediction Probability')
    st.write(prediction_prob)
    
    if (prediction[0]==0):
        return 'The person has No Autoimmune Arthritis Disease'
    else:
        return 'The person has Autoimmune Arthritis Disease'
    
    
def main():
   
    image=Image.open('D:/API/aadimg.tif')
    st.image(image,use_column_width=True)

    st.title('AUTOIMMUNE ARTHRITIS DISEASE PREDICTION  ')
    
     
    # st.sidebar.header('Biomarkers ') 
    def clear_text():
        st.session_state['gen']=""
        st.session_state['tc']=""
        st.session_state['esin']=""
        st.session_state['esrh']=""
        st.session_state['esro']=""
        st.session_state['hb']=""
        st.session_state['rbc']=""
        st.session_state['abs']=""
        st.session_state['mcv']="" 
        st.session_state['mch']=""
        st.session_state['mchc']=""
        st.session_state['aso']=""
        st.session_state['rf']=""
        st.session_state['crp']=""
        st.session_state['rbs']=""
        st.session_state['cree']=""
    st.button("Clear Text Input", on_click=clear_text)  
    
    def user_input_features():
        col1,col2=st.columns(2)
        
        st.write('Enter the biomarker values:')
        # st.write('Gender:')
        Gender_M = col1.text_input('Gender: 0 for male, 1 for female', key='gen')
        Gender_M = int(Gender_M) if Gender_M.strip() and Gender_M.isnumeric() else 0
        
        TC = col1.text_input('Enter Total Blood Count', key='tc')
        TC = int(TC) if TC.strip() and TC.isnumeric() else 0
        
        E = col1.text_input('Esinophil', key='esin')
        E = int(E) if E.strip() and E.isnumeric() else 0
        
        ESRh = col1.text_input('ESR for half an hour', key='esrh')
        ESRh = int(ESRh) if ESRh.strip() and ESRh.isnumeric() else 0
        
        ESRo = col1.text_input('ESR for an hour', key='esro')
        ESRo = int(ESRo) if ESRo.strip() and ESRo.isnumeric() else 0
        
        Hb = col1.text_input('Haemoglobin', key='hb')
        Hb = float(Hb) if Hb.strip() and Hb.replace('.', '', 1).isdigit() else 0.0
        
        RBC = col1.text_input('RBC', key='rbc')
        RBC = float(RBC) if RBC.strip() and RBC.replace('.', '', 1).isdigit() else 0.0
        
        Abs = col1.text_input('Abs',key='abs')
        Abs = int(Abs) if Abs.strip() and Abs.isnumeric() else 0
        
        MCV = col2.text_input('MCV', key='mcv')
        MCV = int(MCV) if MCV.strip() and MCV.isnumeric() else 0
        
        MCH = col2.text_input('MCH', key='mch')
        MCH = int(MCH) if MCH.strip() and MCH.isnumeric() else 0
        
        MCHC = col2.text_input('MCHC',key='mchc')
        MCHC = int(MCHC) if MCHC.strip() and MCHC.isnumeric() else 0
        
        ASO = col2.text_input('ASO', key='aso')
        ASO = float(ASO) if ASO.strip() and ASO.replace('.', '', 1).isdigit() else 0.0
        
        RF = col2.text_input('RF',key='rf')
        RF = float(RF) if RF.strip() and RF.replace('.', '', 1).isdigit() else 0.0
        
        CRP = col2.text_input('CRP',key='crp')
        CRP = float(CRP) if CRP.strip() and CRP.replace('.', '', 1).isdigit() else 0.0
        
        RBS = col2.text_input('RBS',key='rbs')
        RBS = int(RBS) if RBS.strip() and RBS.isnumeric() else 0
        
        Creatinine = col2.text_input('Creatinine',key='cree')
        Creatinine = float(Creatinine) if Creatinine.strip() and Creatinine.replace('.', '', 1).isdigit() else 0.0
    
        data = {
            'Gender': int(Gender_M),
            'Total Blood Count': int(TC),
            'Esinophil': int(E),
            'ESR for half an hour': int(ESRh),
            'ESR for an hour': int(ESRo),
            'Haemoglobin': float(Hb),
            'RBC': float(RBC),
            'Abs': int(Abs),
            'MCV': int(MCV),
            'MCH': int(MCH),
            'MCHC': int(MCHC),
            'ASO': float(ASO),
            'RF': float(RF),
            'CRP': float(CRP),
            'RBS': int(RBS),
            'Creatinine': float(Creatinine)
        }
        
        features = pd.DataFrame(data, index=[0])
        return features
    
    
    df=user_input_features()


    Label=''
    if st.button('Autoimmune Arthritis Disease Prediction Result'):
        Label=arthritis_prediction(df)

    st.success(Label)    

   
if __name__=='__main__':
    main()






