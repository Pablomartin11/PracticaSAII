from SPARQLWrapper import SPARQLWrapper, JSON

# Establecer la URL del punto SPARQL
endpoint_url = "http://datos.gob.es/virtuoso/sparql" 

# Crear un objeto SPARQLWrapper para el punto SPARQL
sparql = SPARQLWrapper(endpoint_url)

# Escribir tu consulta SPARQL
query = """
    select ?dataset where {
    ?dataset a <http://www.w3.org/ns/dcat#Dataset> .
    ?dataset <http://purl.org/dc/terms/title> "Climatología en Asturias: temperaturas, precipitaciones y horas de sol"@es .
    }
"""

# Otro ejemplo de como sacarlo
# PREFIX dct: <http://purl.org/dc/terms/>
# select distinct ?dataset ?valor where
# {
#  ?dataset <http://purl.org/dc/terms/publisher> ?publicador .
#  ?publicador <http://www.w3.org/2004/02/skos/core#notation> "A03002951".
#  ?dataset dct:title "Climatología en Asturias: temperaturas, precipitaciones y horas de sol"@es
# }


# Establecer la consulta SPARQL en el objeto SPARQLWrapper
sparql.setQuery(query)

# Especificar que los resultados deben ser devueltos en formato JSON
sparql.setReturnFormat(JSON)

# Enviar la consulta al punto SPARQL y procesar los resultados
try:
    # Realizar la consulta SPARQL
    results = sparql.query().convert()
    # Iterar sobre los resultados e imprimirlos
    for result in results["results"]["bindings"]:
        print(result["dataset"]["value"])

except Exception as e:
    print(f"Error occurred: {e}")
