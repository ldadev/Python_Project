import pandas as pd

#fields_date = ['fecha_nacimiento','fecha_afiliacion','fecha_aplicacion_cambio_estado',
      #         'fecha_estao_corte','fecha_corte']
#df = pd.read_csv('afiliados.csv')
#df.columns
#for field in fields_date:
	#df[field] = pd.to_datetime(df[field])
#df = df.set_index('afiliado_id')
#mask = (df['fecha_afiliacion']>'2020-03-25') & (df['fecha_afiliacion'] < '2020-03-26')
#filtered_df=df.loc[mask]
#df.to_csv('/home/david/Programacion/Datacience/Servsalud/datacleaning/Usuarios/afiliadolimpio.csv')


df = pd.read_csv('recovered.csv')
df = df.set_index('cod')
df.columns
print(df.mean(axis = 2))

