from datastack import datastack
from varname.helpers import exec_code

ds = datastack(main=True)

ds.subheader("DataStack click counter app")

count = 0


def inc_count():
    global count
    count += 1


ds.button("Click", on_click=inc_count)
ds.write("counts: " + str(count))

code = "ds.button('dynamic text')"
exec_code(code)
