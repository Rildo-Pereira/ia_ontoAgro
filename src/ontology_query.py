from rdflib import Graph

class OntologyQuery:
    def __init__(self, ontology_file: str):
        self.graph = Graph()
        self.graph.parse(ontology_file, format="xml")

    def query(self, command: str) -> str:
        # Example SPARQL query based on the command
        sparql_query = """
        SELECT ?subject ?predicate ?object
        WHERE {
            ?subject ?predicate ?object.
        }
        LIMIT 10
        """
        results = self.graph.query(sparql_query)
        response = "\n".join([f"{row.subject} {row.predicate} {row.object}" for row in results])
        print(f'RESPOSTA: {response}')
        return response