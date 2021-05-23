import re

msj = "Puedes marcarme mañana a uno de los siguientes números de telefono: 515-555-4242,555-1234,212-347-5672"

phoneRegex = re.compile(r'((\d{3}.\d{3}.\d{4}).*)')
mo = phoneRegex.search(msj)
print(mo.group())