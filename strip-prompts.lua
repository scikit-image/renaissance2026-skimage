-- Remove the template's italic guidance-prompt paragraphs.
-- A paragraph consisting solely of emphasized (italic) text is treated
-- as instructional boilerplate and dropped.
function Para(el)
  if #el.content == 1 and el.content[1].t == "Emph" then
    return {}
  end
  return nil
end
