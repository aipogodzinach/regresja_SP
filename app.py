import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

X_d = {0:"Kobieta",1:"Mężczyzna"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy SP będzie dobry?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	with overview:
		st.title("Przewidywanie (ocena SP)")

	with left:
		P1_slider = st.slider("Stopień, w jakim SP dostosowuje swoją komunikację niewerbalną do sytuacji", value=3, min_value=1, max_value=7)
		P2_slider = st.slider("Stopień, w jakim zrozumiały i poprawny gramatycznie jest tok wypowiedzi SP", value=3, min_value=1, max_value=7)
		P3_slider = st.slider("Stopień, w jakim SP realizuje przewidziany scenariusz zajęć", value=3, min_value=1, max_value=7)

	with right:
		P4_slider = st.slider("Stopień w jakim SP okazuje emocje związane z rozmową", value=3, min_value=1, max_value=7)
		P5_slider = st.slider("Stopień w jakim SP reaguje adekwatnie do zachowania studenta", value=3, min_value=1, max_value=7)
		P6_slider = st.slider("Jeżeli pytasz się SP o informację zwrotną, to oceń sposób, w jaki SP udziela informacji zwrotnej po zakończeniu zajęć (merytorycznie oraz technicznie)", value=3, min_value=1, max_value=7)

	data = [[P1_slider, P2_slider,  P3_slider, P4_slider, P5_slider, P6_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy SP będzie dobry? {0}".format("Tak" if survival[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga