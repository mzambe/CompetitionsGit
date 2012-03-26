all : probl1 probl2 probl3 probl4 probl7

probl1 : probl1.ml
	ocamlopt probl1.ml -o probl1

probl2 : probl2.ml
	ocamlopt probl2.ml -o probl2

probl3 : probl3.py
	chmod +x probl3.py

probl4 : probl4.py
	chmod +x probl4.py

probl7 : probl7.py
	chmod +x probl7.py

clean :
	rm probl1 probl2
