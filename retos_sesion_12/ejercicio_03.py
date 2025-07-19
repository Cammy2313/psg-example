jhon_autos = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
jess_autos = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
print("Autos a escala de Jhon:", jhon_autos)
print("Autos a escala de Jess:", jess_autos)
if jhon_autos.isdisjoint(jess_autos):
    print ("No tienen autos en común")
else:
    print ("Autos en común:")
    print (jhon_autos.intersection(jess_autos))