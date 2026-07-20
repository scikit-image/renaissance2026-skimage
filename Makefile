SRC      := WORKPLAN.md
FILTER   := strip-prompts.lua
TEMPLATE := OS4LS Work Plan template.docx
OUT      := OS4LS-WorkPlan-vanderWalt.docx

.PHONY: all docx clean

all: docx

docx: $(OUT)

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

clean:
	rm -f "$(OUT)"
