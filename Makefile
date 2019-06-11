stats:
	python3 statistics.py
graph:
	python3 graph.py
commit:
	git commit -am "update $(date)" && git push origin master
