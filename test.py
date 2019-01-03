import lua

print(lua.globals())
print("-----")

lua.execute(r"""
print(require("rapidjson"))
print(require("pb"))
""")

lua = None

import gc

gc.collect()
