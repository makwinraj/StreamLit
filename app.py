import streamlit as st
import json
import requests
import pandas as pd


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    login="https://deverp.primeassetsource.com/api/method/library_management.signin.login"
    st.write(login)
    datas={
    "usr":"sales@gmail.com",
    "pwd":"Prime@123"
    }
    loginres=requests.post(login,json=datas)
    dic=(loginres.text)
    J=json.loads(dic)
    api_k=(str(J["message"]["api_key"]))
    api_s=(str(J["message"]["api_secret"]))
    api_ks="token "+api_k+":"+api_s
    st.write(api_ks)
    item_c=dataframe["Item Code "]
    qty=dataframe["Qty "]
    item_n=dataframe["Item Name (Items)"]
    basic_r=dataframe["Basic Rate (as per Stock UOM) (Items)"]
    item_g=dataframe["Item Group (Items)"]
    #supplier_w=dataframe["Supplier warranty"]
    #serialnum=dataframe["Serial Number"]

    
    url="https://deverp.primeassetsource.com/api/resource/Stock Entry"
    header={"Content-Type":"application/json","Authorization":api_ks}
    for (Item_c,Qty,Item_n,Basic_r,Item_g)  in zip(item_c,qty,item_n,basic_r,item_g):
        body= {
        
       
        "stock_entry_type": "Material Receipt",
        "company": "Prime Asset Source",
          #"supplier_warranty": Supplier_w,
          #"serial_number":Serial_n,
    
      
        "items": [
            {
                
            
                "t_warehouse": "YESHWANTPUR - PAS",
                "item_code": Item_c,
                "item_name":Item_n,
                "item_group":Item_g,
                "qty": Qty,
                "basic_rate":Basic_r,
              
                
            
            }   
                
            ]
        }

        st.write(body)

   
    
   
        x=requests.post(url, json=body,headers=header)
        st.write(x)            
        #print("response--->",x)
  
