import streamlit as st

#st.title est emploiye pour ecrire le titre de l'application
st.title("IMC")

#st.number_input est utilise pour entrer une valeur de type nombre

poids = st.number_input("veuiller donner le poids du patient:")
taille = st.number_input("veuiller donner la taille du patient:")

#calcul à faire

if st.button("calcul") :

    imc = poids/(taille**2)
    st.write(imc)

    if imc < 18.5:
   
        st.warning("maigre")

    elif 18.5<imc25 :
    
        st.success("poids normal")

    elif 25 < imc <30:
    
        st.warning (" surpoids ")

    elif imc >= 30 :
        st.warning ("obese")
else :
    st.info("Ceci n'est pas un nombre")

        
        

        


