
#Identificadores de campos>cedula,date_1,date_2,estamento
#Obtener objeto por cada identificador de campo>self.request.GET.get(input)
#Guardar cada objeto relacionadolo por su campo
#De acuerdo al campo obtenido, aplicar el filtro y retornar los objetos filtrados


strs = {'numeros':{'cedula':''},'dates':{'date_1':'01/01/2020','date_2':'01/01/1991'},'selects':{'estamento':'Todos'}}

nan = ['cedula','date_1','date_2','estamento']
