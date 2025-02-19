from rdflib import Graph
from ia_ontoAgro.src.terms import readable_terms

class OntologyQuery:
    def __init__(self, ontology_file: str):
        self.graph = Graph()
        self.graph.parse(ontology_file, format="xml")

    def query(self, command: str) -> str:
        # Example SPARQL query based on the command
        # sparql_query = """
        # SELECT ?subject ?predicate ?object
        # WHERE {
        #     ?subject ?predicate ?object.
        # }
        # """

        words = command.split()
        filter_conditions = []
        for word in words:
            filter_conditions.append(f"regex(?subject, '{word}', 'i')")
            filter_conditions.append(f"regex(?predicate, '{word}', 'i')")
            filter_conditions.append(f"regex(?object, '{word}', 'i')")

        filter_expression = " || ".join(filter_conditions)

        sparql_query = f"""
        SELECT ?subject ?predicate ?object
        WHERE {{
            ?subject ?predicate ?object.
            FILTER ({filter_expression})
        }}
        """



        results = self.graph.query(sparql_query)
        response = "\n".join([f"{row.subject} {row.predicate} {row.object}" for row in results])

        for i, line in enumerate(response.split('\n')):
            for uri, term in readable_terms.items():
                line = line.replace(uri, term)
            response = response.replace(response.split('\n')[i], line) # Atualiza a linha com os termos legíveis.







        # print(f'RESPOSTA: <<<<{response}>>>>>')
        return response