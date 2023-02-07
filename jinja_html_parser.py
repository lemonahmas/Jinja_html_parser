import jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader("E:\VSCPython\Jinja_html_parser"))
temp = env.get_template('./test.html')

# https://jinja.palletsprojects.com/en/3.1.x/templates/# Check this out XD.

navigation = [{"href":"email1","caption":"1"},{"href":"email2","caption":"2"},{"href":"email3","caption":"3"}]
a_variable = "Damn this is ez."

out = temp.render({"navigation":navigation,"a_variable":a_variable})
with open("./out.html","w") as f:
    f.writelines(out)
    f.close()