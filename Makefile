pdf:
	latexmk -pdf 00main.tex
diff:
	git latexdiff HEAD~2 HEAD --latexmk --latexopt -pdf --main 00main.tex
check:
	find . -name "*.tex" -exec aspell --lang=en --mode=tex check "{}" \;
