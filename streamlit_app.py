import streamlit as st 
mylist = ("km/h zu mp/h", "mp/h zu km/h", "Fibonacci-Folge", "Primzahl (Ja/Nein)")


with st.container():
    st.title("MATHEMAX")
    st.write("---")
    st.subheader("Hi, ich bin Max :wave:")
    st.write("Meine Passion ist die Königin der Disziplinen, DIE MATHEMATIK!")
    st.write("Mit dieser Seite helfe ich dir MEHRERE mathematische Berechnungen zu berechnen!")


with st.container():
    st.write("---")
    st.subheader("Wähle aus, was ich für dich berechnen soll!")
    st.write("---")
    st.subheader("[1. Berechnung km/h UND mp/h](http://tpcg.io/_HZXOUP)")
    st.subheader("[2. Berechnung der Fibonacci-Folge](http://tpcg.io/_2RD629)")
    st.subheader("[3. Ist es eine Primzahl?](http://tpcg.io/_97AZOJ)")
    st.subheader("[4. Berechnung von geometrischen Körpern](http://tpcg.io/_DN3Q48)")
