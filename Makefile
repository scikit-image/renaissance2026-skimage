SRC      := WORKPLAN.md
FILTER   := strip-prompts.lua
TEMPLATE := OS4LS Work Plan template.docx
OUT      := OS4LS-WorkPlan-vanderWalt.docx
BIO      := OPTIONAL_UPLOAD.md
BIO_OUT  := OPTIONAL_UPLOAD.pdf

.PHONY: all docx optional clean

all: docx optional

docx: $(OUT)

optional: $(BIO_OUT)

# We produce text for the work plan here, but to preserve styling of
# the template it still has to be cut and paste. If we had a bit more
# time, we could have made a template with the right styles; next
# time.

$(OUT): $(SRC) $(FILTER)
	pandoc "$(SRC)" \
	  --reference-doc="$(TEMPLATE)" \
	  --lua-filter="$(FILTER)" \
	  -o "$(OUT)"
	@echo "Wrote $(OUT)"

# Optional supporting document (bio) -> PDF. Sans-serif font and page
# geometry come from the YAML header in $(BIO); needs a LaTeX engine
# (pandoc's default, pdflatex).
$(BIO_OUT): $(BIO)
	pandoc "$(BIO)" \
	  -o "$(BIO_OUT)"
	@echo "Wrote $(BIO_OUT)"

clean:
	rm -f "$(OUT)" "$(BIO_OUT)"
