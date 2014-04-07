install:
	make skeleton
	python setup.py install
	make clean

uninstall:
	python setup.py uninstall

reinstall:
	make uninstall
	make install

clean:
	rm -Rf build Cactus.egg-info dist

test:
	nosetests -s

shelltest:
	tests/test.sh

alltests:
	make clean
	make skeleton
	make uninstall
	make install
	make test
	make shelltest

skeleton:
	rm -Rf skeleton.tar.gz
	rm -f cactus/skeleton.py
	cd skeleton; tar -cz --exclude='.[^/]*' -f ../skeleton.tar.gz . 
	echo 'data = """' > cactus/skeleton.py
	cat skeleton.tar.gz | base64 | fold -sw 60 >> cactus/skeleton.py
	echo '"""' >> cactus/skeleton.py
	rm -Rf skeleton.tar.gz

submit:
	python setup.py register

.PHONY: test skeleton
