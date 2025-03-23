import csv
import pandas as pd
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, OWL, XSD
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

def create_graph_persp(csv_file, endpoint):

    # Define Namespaces
    PERSPECT = Namespace("http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")
    #OWL = Namespace("http://www.w3.org/2002/07/owl#")

    # Create a new RDF graph
    g = Graph()

    # Bind prefixes- namespace vengono associati al grafo
    g.bind("persp", PERSPECT)

     # Lettura del CSV
    df = pd.read_csv(csv_file, delimiter=",")
    endpoint = endpoint + "sparql"

    # Definizione classi RDF
    #Attitude
    Attitude = URIRef(PERSPECT.Attitude)
    g.add((Attitude, RDF.type, OWL.Class))

    # Attitude Sub-classes: ProfitDriven
    ProfitDriven = URIRef(PERSPECT.ProfitDriven)
    g.add((ProfitDriven, RDF.type, OWL.Class))
    g.add((ProfitDriven, RDFS.subClassOf, PERSPECT.Attitude))

    # Attitude Sub-classes: SocialImpact
    SocialImpact = URIRef(PERSPECT.SocialImpact)
    g.add((SocialImpact, RDF.type, OWL.Class))
    g.add((SocialImpact, RDFS.subClassOf, PERSPECT.Attitude))

    #Background
    Background = URIRef(PERSPECT.Background)
    g.add((Background, RDF.type, OWL.Class))

    # Background Sub-classes: AudienceEngagement
    AudienceEngagement = URIRef(PERSPECT.AudienceEngagement)
    g.add((AudienceEngagement, RDF.type, OWL.Class))
    g.add((AudienceEngagement, RDFS.subClassOf, PERSPECT.Background))

    # Background Sub-classes: Conceptualizer
    Conceptualizer = URIRef(PERSPECT.Conceptualizer)
    g.add((Conceptualizer, RDF.type, OWL.Class))
    g.add((Conceptualizer, RDFS.subClassOf, PERSPECT.Background))

    # Background Sub-classes: Year
    Year = URIRef(PERSPECT.Year)
    g.add((Year, RDF.type, OWL.Class))
    g.add((Year, RDFS.subClassOf, PERSPECT.Background))

    #Cut
    Cut = URIRef(PERSPECT.Cut)
    g.add((Cut, RDF.type, OWL.Class))

    # Cut Sub-classes: RepresentationType
    RepresentationType = URIRef(PERSPECT.RepresentationType)
    g.add((RepresentationType, RDF.type, OWL.Class))
    g.add((RepresentationType, RDFS.subClassOf, PERSPECT.Cut))

    #Eventuality
    Eventuality = URIRef(PERSPECT.Eventuality)
    g.add((Eventuality, RDF.type, OWL.Class))

    #Eventuality Sub-classes: AuthenticCharacterization
    AuthenticCharacterization = URIRef(PERSPECT.AuthenticCharacterization)
    g.add((AuthenticCharacterization, RDF.type, OWL.Class))
    g.add((AuthenticCharacterization, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: CharacterTransformation
    CharacterTransformation = URIRef(PERSPECT.CharacterTransformation)
    g.add((CharacterTransformation, RDF.type, OWL.Class))
    g.add((CharacterTransformation, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: DetailedPortrayal
    DetailedPortrayal = URIRef(PERSPECT.DetailedPortrayal)
    g.add((DetailedPortrayal, RDF.type, OWL.Class))
    g.add((DetailedPortrayal, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: DynamicRole
    DynamicRole = URIRef(PERSPECT.DynamicRole)
    g.add((DynamicRole, RDF.type, OWL.Class))
    g.add((DynamicRole, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: FairRepresentation
    FairRepresentation = URIRef(PERSPECT.FairRepresentation)
    g.add((FairRepresentation, RDF.type, OWL.Class))
    g.add((FairRepresentation, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: PlotResolution
    PlotResolution = URIRef(PERSPECT.PlotResolution)
    g.add((PlotResolution, RDF.type, OWL.Class))
    g.add((PlotResolution, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: StaticRole
    StaticRole = URIRef(PERSPECT.StaticRole)
    g.add((StaticRole, RDF.type, OWL.Class))
    g.add((StaticRole, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: StereotypicalCharacterization
    StereotypicalCharacterization = URIRef(PERSPECT.StereotypicalCharacterization)
    g.add((StereotypicalCharacterization, RDF.type, OWL.Class))
    g.add((StereotypicalCharacterization, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: SuperficialPortrayal
    SuperficialPortrayal = URIRef(PERSPECT.SuperficialPortrayal)
    g.add((SuperficialPortrayal, RDF.type, OWL.Class))
    g.add((SuperficialPortrayal, RDFS.subClassOf, PERSPECT.Eventuality))

    #Eventuality Sub-classes: UnfairRepresentation
    UnfairRepresentation = URIRef(PERSPECT.UnfairRepresentation)
    g.add((UnfairRepresentation, RDF.type, OWL.Class))
    g.add((UnfairRepresentation, RDFS.subClassOf, PERSPECT.Eventuality))

    #Lens
    Lens = URIRef(PERSPECT.Lens)
    g.add((Lens, RDF.type, OWL.Class))

    #Lens Sub-classes: IdeologicalChallenge
    IdeologicalChallenge = URIRef(PERSPECT.IdeologicalChallenge)
    g.add((IdeologicalChallenge, RDF.type, OWL.Class))
    g.add((IdeologicalChallenge, RDFS.subClassOf, PERSPECT.Lens))

    #Lens Sub-classes: ProfitAndMassAppeal
    ProfitAndMassAppeal = URIRef(PERSPECT.ProfitAndMassAppeal)
    g.add((ProfitAndMassAppeal, RDF.type, OWL.Class))
    g.add((ProfitAndMassAppeal, RDFS.subClassOf, PERSPECT.Lens))

    # Aggiungere dati dal CSV
    for _, row in df.iterrows():
        entity_uri = URIRef(PERSPECT[row["ID"]])
        g.add((entity_uri, RDF.type, PERSPECT[row["Type"]]))
        g.add((entity_uri, RDFS.label, Literal(row["Label"], lang="en")))

    # Salvataggio o caricamento nel triplestore
    if endpoint:
        g.commit()
    else:
        g.serialize(destination="output.ttl", format="turtle")