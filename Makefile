LATEX_FILES := $(wildcard *.tex)
PDF_FILES := $(LATEX_FILES:.tex=.pdf)

# Define variables
PIPENV = pipenv
PYTHON = $(PIPENV) run python
RENDER_SCRIPT = render.py

all: render pdf

# Render the resume
render:
	$(PYTHON) $(RENDER_SCRIPT)

# Generate PDF files
pdf: $(PDF_FILES)

# Lint YAML files
yamllint:
	$(PIPENV) run yamllint resume_common.yaml

%.pdf: %.tex
	docker run --rm -v $(shell pwd):/data fbenz/pdflatex pdflatex -output-directory=/data $<
	mv $*.pdf "Marcell, Jason - Resume.pdf"
