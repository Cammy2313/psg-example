habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}
print(habitats)

habitats.update({
    "sabana": {"especies": {"león", "elefante"}},
    "océano": {"especies": {"tiburón", "tortuga marina"}}
})
print("Habitats actualizados con dos especies mas:", habitats)

existe = "amazonas" in habitats
print ("¿Existe amazonas en los habitats?",existe)

habitats["amazonas"]["especies"].add("anaconda")
print ("Se añadio la especie anaconda a amazonas :",habitats)