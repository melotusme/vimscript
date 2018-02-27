import snake
import re

@snake.visual_key_map("<leader>c")
def f(selected):
    s = selected.split("\n")
    rst = [re.sub(r'(=\s{0,}\d{0,})', "= {}".format(i+1), l) for i,l in enumerate(s)]
    return "\n".join(rst)

