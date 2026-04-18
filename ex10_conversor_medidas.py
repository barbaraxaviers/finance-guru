medida = float(input('Uma distância em metros:'))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
m = medida
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A medida de {medida} metros corresponde a {cm} cm e {mm} mm.')
print(f' A medida de {medida} metros corresponde a {dm} dm, {dam} dam, {hm} hm, {km} km.')
print('A medida de {} metros corresponde a {} cm e {} mm.'.format(medida, cm,mm))
print('A medida de {} metros corresponde a {} dm, {} dam, {} hm, {}km. '.format(medida,dm,dam,hm,km))
#mapa das unidades
#a base de tudo é o (m). A partir dele:
#km (quilometro) = metro /1000
#hm (hectômetro) = metro / 100
#dam (decâmetro) = metro / 10
#######m (metro) = ele mesmo
#dm(decimetro) = metro * 10
#cm (centimetro) = metro * 100
#mm (milimetro) = metro * 1000
