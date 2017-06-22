from batship_search import *

sa = SearchArea(100,200)

sa.mark_loc(5,5)
sa.mark_loc(80,200)


print sa.get_loc_context(4,7)
print sa.get_loc_context(100,200)