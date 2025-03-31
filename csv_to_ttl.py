import pandas as pd
import os
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import XSD, OWL, RDF, RDFS, FOAF

# Definition of Namespaces
persp = Namespace("http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")
LGBTQPortrayal = Namespace("http://www.semanticweb.org/LGBTQPortrayal#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
schema = Namespace("https://schema.org/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")


# Create a new RDFLib graph
g = Graph()

# Bind namespaces 
g.bind("persp", persp)
g.bind("LGBTQPortrayal", LGBTQPortrayal)
g.bind("RDFS", RDFS)
g.bind("schema", schema)


# Carica SOLO la tua ontologia locale con le importazioni già fatte in Protégé
# Carica l'ontologia locale
g.parse("LGBTQPortrayal.oww", format="xml")

# aggiungere le classi e proprietà nuove
g.add((LGBTQPortrayal.SexOrientation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Gender, RDF.type, OWL.Class))
g.add((FOAF.Person, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Performer, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Performer, RDFS.subClassOf, LGBTQPortrayal.Person))
g.add((LGBTQPortrayal.Creator, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Creator, RDFS.subClassOf, LGBTQPortrayal.Person))
g.add((schema.Country, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TvShow, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Character, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Genre, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.ProductionAndIndustryFactory, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Stereotypes, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TragicTrope, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TragicTrope, RDFS.subClassOf, persp.Stereotypes))
g.add((LGBTQPortrayal.GayBestFriend, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.GayBestFriend, RDFS.subClassOf, persp.Stereotypes))
g.add((LGBTQPortrayal.LGBTQCommunityImpact, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NegativeRoleModel, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NegativeRoleModel, RDFS.subClassOf, persp.LGBTQCommunityImpact))
g.add((LGBTQPortrayal.PositiveRoleModel, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PositiveRoleModel, RDFS.subClassOf, persp.LGBTQCommunityImpact))



#Eventuality
g.add((LGBTQPortrayal.PortrayalofLgbtqCharacter, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PortrayalofLgbtqCharacter, RDFS.subClassOf, persp.Eventuality))
g.add((LGBTQPortrayal.RepresentationType, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.RepresentationType, RDFS.subClassOf, persp.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.CharacterDepth, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CharacterDepth, RDFS.subClassOf, persp.RepresentationType))
g.add((LGBTQPortrayal.FairRepresentation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.FairRepresentation, RDFS.subClassOf, persp.RepresentationType))
g.add((LGBTQPortrayal.UnfairRepresentation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.UnfairRepresentation, RDFS.subClassOf, persp.RepresentationType))
g.add((LGBTQPortrayal.PlotResolution, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PlotResolution, RDFS.subClassOf, persp.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.NormalizationOfRelationship, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NormalizationOfRelationship, RDFS.subClassOf, persp.PlotResolution))
g.add((LGBTQPortrayal.AffirmationOfIdentity, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.AffirmationOfIdentity, RDFS.subClassOf, persp.PlotResolution))
g.add((LGBTQPortrayal.Authenticity, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Authenticity, RDFS.subClassOf, persp.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.SignificanceInPlot, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.SignificanceInPlot, RDFS.subClassOf, persp.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.NarrativeRole, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NarrativeRole, RDFS.subClassOf, persp.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.CharacterTransformation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CharacterTransformation, RDFS.subClassOf, persp.NarrativeRole)) #see what they say
g.add((LGBTQPortrayal.Dynamic, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Dynamic, RDFS.subClassOf, persp.NarrativeRole)) #see what they say
g.add((LGBTQPortrayal.Static, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Static, RDFS.subClassOf, persp.NarrativeRole)) #see what they say


#Lens
g.add((LGBTQPortrayal.ProfitDrivenLens, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.ProfitDrivenLens, RDFS.subClassOf, persp.Lens))
g.add((LGBTQPortrayal.SocialImpactLens, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.SocialImpactLens, RDFS.subClassOf, persp.Lens))

#Attitude
g.add((LGBTQPortrayal.MarketFriendly, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.MarketFriendly, RDFS.subClassOf, persp.Attitude))
g.add((LGBTQPortrayal.Tokenization, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Tokenization, RDFS.subClassOf, persp.Attitude))
g.add((LGBTQPortrayal.Queerbaiting, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Queerbaiting, RDFS.subClassOf, persp.Attitude))
g.add((LGBTQPortrayal.EmpowermentRepresentation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.EmpowermentRepresentation, RDFS.subClassOf, persp.Attitude))
g.add((LGBTQPortrayal.ChallengingStereotypes, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.ChallengingStereotypes, RDFS.subClassOf, persp.Attitude))

#Background
g.add((LGBTQPortrayal.StreamingPolicies, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.StreamingPolicies, RDFS.subClassOf, persp.Background))
g.add((LGBTQPortrayal.CensorshipLaws, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CensorshipLaws, RDFS.subClassOf, persp.Background))
g.add((LGBTQPortrayal.FinancialRisk, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.FinancialRisk, RDFS.subClassOf, persp.Background))
g.add((LGBTQPortrayal.QueerTheory, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.QueerTheory, RDFS.subClassOf, persp.Background))
g.add((LGBTQPortrayal.HistoricalTrends, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.HistoricalTrends, RDFS.subClassOf, persp.Background))
g.add((LGBTQPortrayal.AudienceDemand, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.AudienceDemand, RDFS.subClassOf, persp.Background))

#Cut
g.add((LGBTQPortrayal.CharacterType, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CharacterType, RDFS.subClassOf, persp.Cut))

#properties 
#properties from schema
hasOccupation = schema.hasOccupation
g.add((hasOccupation, RDF.type, OWL.ObjectProperty))

countryOfOrigin = schema.countryOfOrigin
g.add((countryOfOrigin, RDF.type, OWL.ObjectProperty))

creator = schema.creator
g.add((creator, RDF.type, OWL.ObjectProperty))

actor = schema.actor
g.add((actor, RDF.type, OWL.ObjectProperty))

character = schema.character
g.add((character, RDF.type, OWL.ObjectProperty))

genre = schema.genre
g.add((genre, RDF.type, OWL.ObjectProperty))

productionCompany = schema.productionCompany
g.add((productionCompany, RDF.type, OWL.ObjectProperty))


#properties from LGBTQPortrayal
hasGender = LGBTQPortrayal.hasGender
g.add((hasGender, RDF.type, OWL.ObjectProperty))

hasSexOrientation = LGBTQPortrayal.hasSexOrientation
g.add((hasSexOrientation, RDF.type, OWL.ObjectProperty))

hasCharacterDepth = LGBTQPortrayal.hasCharacterDepth
g.add((hasCharacterDepth, RDF.type, OWL.ObjectProperty))

hasPortrayal = LGBTQPortrayal.hasPortrayal
g.add((hasPortrayal, RDF.type, OWL.ObjectProperty))

hasImpactOn = LGBTQPortrayal.hasImpactOn
g.add((hasImpactOn, RDF.type, OWL.ObjectProperty))

hasNarrativeFunction = LGBTQPortrayal.hasNarrativeFunction
g.add((hasNarrativeFunction, RDF.type, OWL.ObjectProperty))

impactsCommunity = LGBTQPortrayal.impactsCommunity
g.add((impactsCommunity, RDF.type, OWL.ObjectProperty))

hasStereotype = LGBTQPortrayal.hasStereotype
g.add((hasStereotype, RDF.type, OWL.ObjectProperty))

associatedWith = LGBTQPortrayal.associatedWith
g.add((associatedWith, RDF.type, OWL.ObjectProperty))

viewedThroughLens  = LGBTQPortrayal.viewedThroughLens 
g.add((viewedThroughLens, RDF.type, OWL.ObjectProperty))

hasAttitude  = LGBTQPortrayal.hasAttitude 
g.add((hasAttitude, RDF.type, OWL.ObjectProperty))

affectsPortrayal  = LGBTQPortrayal.affectsPortrayal 
g.add((affectsPortrayal, RDF.type, OWL.ObjectProperty))

shapedByLens  = LGBTQPortrayal.shapedByLens 
g.add((shapedByLens, RDF.type, OWL.ObjectProperty))

emergesFrom  = LGBTQPortrayal.emergesFrom 
g.add((emergesFrom, RDF.type, OWL.ObjectProperty))

shapedByAttitude  = LGBTQPortrayal.shapedByAttitude  
g.add((shapedByAttitude, RDF.type, OWL.ObjectProperty))

providesContextFor  = LGBTQPortrayal.providesContextFor  
g.add((providesContextFor, RDF.type, OWL.ObjectProperty))

informedByBackground  = LGBTQPortrayal.informedByBackground   
g.add((informedByBackground, RDF.type, OWL.ObjectProperty))

# Define data properties
g.add((LGBTQPortrayal.isTransgender, RDF.type, OWL.DatatypeProperty))
g.add((LGBTQPortrayal.hasTitle, RDF.type, OWL.DatatypeProperty))
g.add((schema.datePublished, RDF.type, OWL.DatatypeProperty))
g.add((RDFS.label, RDF.type, OWL.DatatypeProperty))


# Load the data from our CSV file as pandas DataFrame
#url = "C:/Users/vdant/Documents/DIGITAL HUMANITIES BOLOGONA/KNOWLEDGE REPRESENTATION AND EXTRACTION/LGBTQ-Rep/final_dataset.csv"
#df = pd.read_csv(url,dtype=str).fillna("")


# Percorso del file
file_path = r"C:\Users\vdant\Documents\DIGITAL HUMANITIES BOLOGONA\KNOWLEDGE REPRESENTATION AND EXTRACTION\LGBTQ-Rep\final_dataset.csv"

# Proviamo con diversi separatori per capire il formato corretto
try:
    df = pd.read_csv(file_path, sep=",", encoding="utf-8")  # Prova con virgola
    if df.shape[1] == 1:  # Se c'è solo una colonna, forse il separatore è ";"
        df = pd.read_csv(file_path, sep=";", encoding="utf-8")
        
    print("✅ File caricato con successo!")
    print(df.head())  # Mostra le prime righe
except Exception as e:
    print(f"❌ Errore durante il caricamento del file: {e}")



# Iterate over the DataFrame rows
#for index, row in df.iterrows():
 #  character_uri = LGBTQPortrayal[f"Character_{index}"]  # Crea un URI univoco per ogni istanza
  # g.add((character_uri, RDF.type, LGBTQPortrayal.PortrayalofLgbtqCharacter))
   #g.add((character_uri, schema.name, Literal(row["Name"], datatype=XSD.string)))

