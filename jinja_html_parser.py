import jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
temp = env.get_template('./test.html')

# https://jinja.palletsprojects.com/en/3.1.x/templates/# Check this out XD.

navigation = [{"href":"email1","caption":"1"},{"href":"email2","caption":"2"},{"href":"email3","caption":"3"}]
a_variable = "Damn this is ez."

out = temp.render({"navigation":navigation,"a_variable":a_variable})
with open("./out.html","w") as f:
    f.writelines(out)
    f.close()

with open("./test.html") as f:
    template = jinja2.Template(source=f.read())

template.render({"navigation":navigation,"a_variable":a_variable})
with open("./out2.html","w") as f:
    f.writelines(out)
    f.close()