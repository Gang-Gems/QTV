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

# Carica l'ontologia locale
g.parse("LGBTQPortrayal.owx", format="xml")

# aggiungere le classi e proprietà nuove
g.add((LGBTQPortrayal.SexOrientation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Gender, RDF.type, OWL.Class))
g.add((FOAF.Person, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Performer, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Performer, RDFS.subClassOf, FOAF.Person))
g.add((LGBTQPortrayal.Creator, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Creator, RDFS.subClassOf, FOAF.Person))
g.add((schema.Country, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TvShow, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Character, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Genre, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.ProductionAndIndustryFactory, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Stereotype, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TragicTrope, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.TragicTrope, RDFS.subClassOf, LGBTQPortrayal.Stereotype))
g.add((LGBTQPortrayal.GayBestFriend, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.GayBestFriend, RDFS.subClassOf, LGBTQPortrayal.Stereotype))
g.add((LGBTQPortrayal.LGBTQCommunityImpact, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NegativeRoleModel, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NegativeRoleModel, RDFS.subClassOf, LGBTQPortrayal.LGBTQCommunityImpact))
g.add((LGBTQPortrayal.PositiveRoleModel, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PositiveRoleModel, RDFS.subClassOf, LGBTQPortrayal.LGBTQCommunityImpact))


#Eventuality
g.add((LGBTQPortrayal.PortrayalofLgbtqCharacter, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PortrayalofLgbtqCharacter, RDFS.subClassOf, persp.Eventuality))
g.add((LGBTQPortrayal.RepresentationType, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.RepresentationType, RDFS.subClassOf, LGBTQPortrayal.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.CharacterDepth, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CharacterDepth, RDFS.subClassOf, LGBTQPortrayal.RepresentationType))
g.add((LGBTQPortrayal.FairRepresentation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.FairRepresentation, RDFS.subClassOf, LGBTQPortrayal.RepresentationType))
g.add((LGBTQPortrayal.UnfairRepresentation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.UnfairRepresentation, RDFS.subClassOf, LGBTQPortrayal.RepresentationType))
g.add((LGBTQPortrayal.PlotResolution, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.PlotResolution, RDFS.subClassOf, LGBTQPortrayal.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.NormalizationOfRelationship, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NormalizationOfRelationship, RDFS.subClassOf, LGBTQPortrayal.PlotResolution))
g.add((LGBTQPortrayal.AffirmationOfIdentity, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.AffirmationOfIdentity, RDFS.subClassOf, LGBTQPortrayal.PlotResolution))
g.add((LGBTQPortrayal.Authenticity, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Authenticity, RDFS.subClassOf, LGBTQPortrayal.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.SignificanceInPlot, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.SignificanceInPlot, RDFS.subClassOf, LGBTQPortrayal.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.NarrativeRole, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.NarrativeRole, RDFS.subClassOf, LGBTQPortrayal.PortrayalofLgbtqCharacter))
g.add((LGBTQPortrayal.CharacterTransformation, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.CharacterTransformation, RDFS.subClassOf, LGBTQPortrayal.NarrativeRole)) #see what they say
g.add((LGBTQPortrayal.Dynamic, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Dynamic, RDFS.subClassOf, LGBTQPortrayal.NarrativeRole)) #see what they say
g.add((LGBTQPortrayal.Static, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.Static, RDFS.subClassOf, LGBTQPortrayal.NarrativeRole)) #see what they say


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
g.add((LGBTQPortrayal.ChallengingStereotype, RDF.type, OWL.Class))
g.add((LGBTQPortrayal.ChallengingStereotype, RDFS.subClassOf, persp.Attitude))

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
df = pd.read_csv("new_final_dataset_comma.csv",dtype=str).fillna("")

# Iterate over the DataFrame rows
for index, row in df.iterrows():
  character_uri = LGBTQPortrayal[f"Character_{row['Character Name'].replace(' ', '_')}"] #Estrae il nome del personaggio dalla riga del dataset--> http://www.semanticweb.org/LGBTQPortrayal#Character_Jules_Vaughn
  g.add((character_uri, RDF.type, LGBTQPortrayal.Character)) #aggiunge un triplo RDF al grafo, affermando che il personaggio (character_uri) è un'istanza della classe Character nell'ontologia -->classificato come character
  g.add((character_uri, RDFS.label, Literal(row["Character Name"], datatype=XSD.string))) #crea un valore testuale per il nome del personaggio-->'etichetta leggibile per facilitarne l'interpretazione.

  # GENDER OF THE CHARACTER
  if row["Gender of the character"] == "Female":
    gender_uri = LGBTQPortrayal.Female
  elif row["Gender of the character"] == "Male":
    gender_uri = LGBTQPortrayal.Male
  elif row["Gender of the character"] == "Non-binary":
    gender_uri = LGBTQPortrayal.NonBinary
  else:
    gender_uri = LGBTQPortrayal.Gender  # Fallback generico

  g.add((character_uri, LGBTQPortrayal.hasGender, gender_uri))

# TRANSGENDER CHARACTER (Yes/No)
  if row["Transgender Character"].strip().lower() == "yes":
    g.add((gender_uri, LGBTQPortrayal.isTransgender, Literal(True, datatype=XSD.boolean)))
  elif row["Transgender Character"].strip().lower() == "no":
    g.add((gender_uri, LGBTQPortrayal.isTransgender, Literal(False, datatype=XSD.boolean)))

# SEX ORIENTATION OF CHARACTER
  sex_orientation_map = {
    "Bisexual": LGBTQPortrayal.Bisexual,
    "Gay": LGBTQPortrayal.Gay,
    "Lesbian": LGBTQPortrayal.Lesbian,
    "Questioning": LGBTQPortrayal.Questioning,
    "Pansexual": LGBTQPortrayal.Pansexual,
    "Queer": LGBTQPortrayal.Queer,
    "Not specified": LGBTQPortrayal.NotSpecified
    }

  sex_orientation_uri = sex_orientation_map.get(row["Sex Orientation of character"], LGBTQPortrayal.SexOrientation)

  g.add((character_uri, LGBTQPortrayal.hasSexOrientation, sex_orientation_uri))

  # Creiamo un URI per il performer basato sul nome
  performer_uri = LGBTQPortrayal[f"Performer_{row['Performer'].replace(' ', '_')}"]
  g.add((performer_uri, RDF.type, LGBTQPortrayal.Performer))
  g.add((performer_uri, RDFS.label, Literal(row["Performer"], datatype=XSD.string)))
  g.add((LGBTQPortrayal.Performer, RDFS.subClassOf, FOAF.Person))

  g.add((character_uri, schema.actor, performer_uri))

# Mappiamo il gender del performer
  gender_map = {
    "Female": LGBTQPortrayal.Female,
    "Male": LGBTQPortrayal.Male,
    "Non-binary": LGBTQPortrayal.NonBinary
}
  gender_uri = gender_map.get(row["Gender of performer"], LGBTQPortrayal.Gender)
  g.add((performer_uri, LGBTQPortrayal.hasGender, gender_uri))

# Mappiamo se il performer è transgender
  is_trans = row["Transgender Performer"].strip().lower() == "yes"
  g.add((performer_uri, LGBTQPortrayal.isTransgender, Literal(is_trans, datatype=XSD.boolean)))

# Mappiamo l'orientamento sessuale del performer
  sex_orientation_map = {
    "Bisexual": LGBTQPortrayal.Bisexual,
    "Gay": LGBTQPortrayal.Gay,
    "Lesbian": LGBTQPortrayal.Lesbian,
    "Questioning": LGBTQPortrayal.Questioning,
    "Pansexual": LGBTQPortrayal.Pansexual,
    "Queer": LGBTQPortrayal.Queer,
    "Not specified": LGBTQPortrayal.NotSpecified
}
  sex_orientation_uri = sex_orientation_map.get(row["Sex orientation of performer"], LGBTQPortrayal.SexOrientation)
  g.add((performer_uri, LGBTQPortrayal.hasSexOrientation, sex_orientation_uri))

  # Creiamo un URI per il CREATOR basato sul nome
  creator_uri = LGBTQPortrayal[f"Creator_{row['Creator'].replace(' ', '_')}"]
  g.add((creator_uri, RDF.type, LGBTQPortrayal.Creator))
  g.add((creator_uri, RDFS.label, Literal(row["Creator"], datatype=XSD.string)))
  g.add((LGBTQPortrayal.Creator, RDFS.subClassOf, FOAF.Person))


# Mappiamo il gender del performer
  gender_map = {
    "Female": LGBTQPortrayal.Female,
    "Male": LGBTQPortrayal.Male,
    "Non-binary": LGBTQPortrayal.NonBinary
    }
  gender_uri = gender_map.get(row["Gender of creator"], LGBTQPortrayal.Gender)

# Mappiamo se il performer è transgender
  is_trans = row["Transgender creator"].strip().lower() == "yes"
  g.add((creator_uri, LGBTQPortrayal.isTransgender, Literal(is_trans, datatype=XSD.boolean)))

# Mappiamo l'orientamento sessuale del performer
  sex_orientation_map = {
    "Bisexual": LGBTQPortrayal.Bisexual,
    "Gay": LGBTQPortrayal.Gay,
    "Lesbian": LGBTQPortrayal.Lesbian,
    "Questioning": LGBTQPortrayal.Questioning,
    "Pansexual": LGBTQPortrayal.Pansexual,
    "Queer": LGBTQPortrayal.Queer,
    "Not specified": LGBTQPortrayal.NotSpecified
    }
  sex_orientation_uri = sex_orientation_map.get(row["Sex orientation of creator"], LGBTQPortrayal.SexOrientation)
  g.add((creator_uri, LGBTQPortrayal.hasSexOrientation, sex_orientation_uri))


  tvshow_uri = LGBTQPortrayal[f"TvShow_{row['Show Title'].replace(' ', '_')}"] #f"Show_{...}" → Aggiunge un prefisso per distinguere gli URI (es. "Show_Euphoria")-->http://www.semanticweb.org/LGBTQPortrayal#Show_Euphoria
  g.add((tvshow_uri, RDF.type, LGBTQPortrayal.TvShow)) # Qui diciamo che lo show è un'istanza della classe TvShow.
  g.add((tvshow_uri, RDFS.label, Literal(row["Show Title"], datatype=XSD.string)))
  g.add((character_uri, schema.character, tvshow_uri))
  g.add((creator_uri, schema.creator, tvshow_uri))


  g.add((tvshow_uri, schema.datePublished, Literal(str(row["Year"]), datatype=XSD.gYear)))

  # Creiamo un URI per il Paese
  country_uri = LGBTQPortrayal[f"Country_{row['Place of publication'].replace(' ', '_')}"]
  g.add((country_uri, RDF.type, schema.Country))
  g.add((country_uri, RDFS.label, Literal(row["Place of publication"], datatype=XSD.string)))

  g.add((tvshow_uri, schema.countryOfOrigin, country_uri))

  # Creiamo un URI per il genere
  genre_uri = LGBTQPortrayal[f"Genre_{row['Genre of the tv-series'].replace(' ', '_')}"]
  g.add((genre_uri, RDF.type, LGBTQPortrayal.Genre))
  g.add((genre_uri, RDFS.label, Literal(row["Genre of the tv-series"], datatype=XSD.string)))

  g.add((tvshow_uri, schema.genre, genre_uri))

# Creiamo un URI per la casa di produzione
  production_uri = LGBTQPortrayal[f"Production_{row['Production company'].replace(' ', '_')}"]

# Definiamo la casa di produzione come istanza di schema:Organization
  g.add((production_uri, RDF.type, LGBTQPortrayal.ProductionAndIndustryFactory))
  g.add((production_uri, RDFS.label, Literal(row["Production company"], datatype=XSD.string)))

# Colleghiamo il TvShow alla casa di produzione
  g.add((tvshow_uri, LGBTQPortrayal.ProductionAndIndustryFactory, production_uri))

  # Creiamo un'istanza per la Portrayal associata al character   -->è giusto??
  portrayal_uri = LGBTQPortrayal[f"Portrayal_{row['Character Name'].replace(' ', '_')}"]
  g.add((portrayal_uri, RDF.type, LGBTQPortrayal.PortrayalofLgbtqCharacter))

  # Colleghiamo il character alla sua portrayal
  g.add((character_uri, hasPortrayal, portrayal_uri))

  # Determina la classe di Representation Type corretta
  if row["Representation Type"] == "Fair":
    representation_type_uri = LGBTQPortrayal.FairRepresentation
    g.add((representation_type_uri, LGBTQPortrayal.associatedWith, LGBTQPortrayal.PositiveRoleModel))
  
  elif row["Representation Type"] == "Unfair":
    representation_type_uri = LGBTQPortrayal.UnfairRepresentation
    g.add((representation_type_uri, LGBTQPortrayal.associatedWith, LGBTQPortrayal.NegativeRoleModel))
  
    # Creiamo un'istanza dello Stereotype associato
    stereotype_uri = LGBTQPortrayal[f"Stereotype_{row['Character Name'].replace(' ', '_')}"]
    g.add((stereotype_uri, RDF.type, LGBTQPortrayal.Stereotype))
    # Collegare UnfairRepresentation a Stereotype
    g.add((representation_type_uri, LGBTQPortrayal.hasStereotype, stereotype_uri))
    # Collegare Stereotype a RepresentationType
    g.add((stereotype_uri, LGBTQPortrayal.hasImpactOn, LGBTQPortrayal.RepresentationType))

  else:
    representation_type_uri = LGBTQPortrayal.RepresentationType  # Fallback

  # Colleghiamo la portrayal alla Representation Type corretta
  g.add((portrayal_uri, RDF.type, representation_type_uri))

  # Aggiungiamo il Justification for Classification come rdfs:comment
  justification_text = row["Justification for Classification"].strip()
  if justification_text:  # Controlliamo che non sia vuoto
    g.add((portrayal_uri, RDFS.comment, Literal(justification_text, datatype=XSD.string)))

  # AUTHENTICITY (sottoclasse di PortrayalofLgbtqCharacter)
  if row["Authenticity"] == "Yes":
    authenticity_uri = LGBTQPortrayal[f"Authenticity_{row['Character Name'].replace(' ', '_')}"]
    g.add((authenticity_uri, RDF.type, LGBTQPortrayal.Authenticity))

  # PLOT RESOLUTION (Affirmation of Identity e Normalization of Relationship)
  if row["Affirmation of Identity"] == "Yes":
    affirmation_uri = LGBTQPortrayal[f"Affirmation_{row['Character Name'].replace(' ', '_')}"]
    g.add((affirmation_uri, RDF.type, LGBTQPortrayal.AffirmationOfIdentity))

  if row["Normalization of Relationship"] == "Yes":
    normalization_uri = LGBTQPortrayal[f"Normalization_{row['Character Name'].replace(' ', '_')}"]
    g.add((normalization_uri, RDF.type, LGBTQPortrayal.NormalizationOfRelationship))

  # NARRATIVE ROLE (Dynamic o Static)
  if row["Dynamic Role"] == "Yes":
    dynamic_uri = LGBTQPortrayal[f"DynamicRole_{row['Character Name'].replace(' ', '_')}"]
    g.add((dynamic_uri, RDF.type, LGBTQPortrayal.Dynamic))

  if row["Static Role"] == "Yes":
    static_uri = LGBTQPortrayal[f"StaticRole_{row['Character Name'].replace(' ', '_')}"]
    g.add((static_uri, RDF.type, LGBTQPortrayal.Static))

  # CHARACTER TRANSFORMATION (se ha una giustificazione)
  if row["Character Transformation"].strip():  # Se non è vuoto
    transformation_uri = LGBTQPortrayal[f"CharacterTransformation_{row['Character Name'].replace(' ', '_')}"]
    g.add((transformation_uri, RDF.type, LGBTQPortrayal.CharacterTransformation))
    
    # Aggiungiamo la giustificazione come commento
    g.add((transformation_uri, RDFS.comment, Literal(row["Character Transformation"], datatype=XSD.string)))

    # PLOT RESOLUTION (se ha una giustificazione)
  if row["Plot Resolution"].strip():  # Se non è vuoto
    plot_resolution_uri = LGBTQPortrayal[f"PlotResolution_{row['Character Name'].replace(' ', '_')}"]
    g.add((plot_resolution_uri, RDF.type, LGBTQPortrayal.PlotResolution))
    
    # Aggiungiamo la giustificazione come commento
    g.add((plot_resolution_uri, RDFS.comment, Literal(row["Plot Resolution"], datatype=XSD.string)))

    # LENS ORIENTATION
  if row["Lens Orientation"] == "Social Impact Lens":
    lens_uri = LGBTQPortrayal.SocialImpactLens
  elif row["Lens Orientation"] == "Profit Driven Lens":
    lens_uri = LGBTQPortrayal.ProfitDrivenLens
  else:
    lens_uri = LGBTQPortrayal.Lens  # Fallback generico

  # Colleghiamo la portrayal alla Lens corretta
  g.add((portrayal_uri, LGBTQPortrayal.viewedThroughLens, lens_uri))


  # STEREOTYPE
  if row["Stereotypical Characterization"] == "Yes":
    stereotype_uri = LGBTQPortrayal[f"Stereotype_{row['Character Name'].replace(' ', '_')}"]
    g.add((stereotype_uri, RDF.type, LGBTQPortrayal.Stereotype))
    g.add((portrayal_uri, LGBTQPortrayal.hasStereotype, stereotype_uri))

  if row["Gay Best Friend"] == "Yes":
    gbf_uri = LGBTQPortrayal[f"GayBestFriend_{row['Character Name'].replace(' ', '_')}"]
    g.add((gbf_uri, RDF.type, LGBTQPortrayal.GayBestFriend))
    g.add((portrayal_uri, LGBTQPortrayal.hasStereotype, gbf_uri))

  if row["Tragic Trope"] == "Yes":
    tragic_trope_uri = LGBTQPortrayal[f"TragicTrope_{row['Character Name'].replace(' ', '_')}"]
    g.add((tragic_trope_uri, RDF.type, LGBTQPortrayal.TragicTrope))
    g.add((portrayal_uri, LGBTQPortrayal.hasStereotype, tragic_trope_uri))

  # ATTITUDE (Tokenization)
  if row["Tokenization"] == "Yes":
    tokenization_uri = LGBTQPortrayal[f"Tokenization_{row['Character Name'].replace(' ', '_')}"]
    g.add((tokenization_uri, RDF.type, LGBTQPortrayal.Tokenization))
    g.add((tokenization_uri, LGBTQPortrayal.affectsPortrayal, portrayal_uri))

  # Creiamo un'istanza di CharacterDepth per il personaggio
  character_depth_uri = LGBTQPortrayal[f"CharacterDepth_{row['Character Name'].replace(' ', '_')}"]
  g.add((character_depth_uri, RDF.type, LGBTQPortrayal.CharacterDepth))

  # Determiniamo se è Detailed o Superficial
  depth_value = row["Portrayal"].strip()
  if depth_value.lower() == "Detailed":
    g.add((character_depth_uri, RDF.type, LGBTQPortrayal.Detailed))
  elif depth_value.lower() == "Superficial":
    g.add((character_depth_uri, RDF.type, LGBTQPortrayal.Superficial))

  g.add((character_uri, LGBTQPortrayal.hasCharacterDepth, character_depth_uri))
  
  # Creiamo un'istanza per l'impatto sulla comunità LGBTQ+
  community_impact_uri = LGBTQPortrayal[f"Impact_{row['Character Name'].replace(' ', '_')}"]
  g.add((community_impact_uri, RDF.type, LGBTQPortrayal.LGBTQCommunityImpact))

  # Estrarre l'impatto (Positive/Negative) e la giustificazione
  impact_value = row["LGBTQ Community Impact"].strip()
  impact_justification = row["LGBTQ Community Impact Justification"].strip()

  # Determinare la sottoclasse corrispondente
  if impact_value.lower() == "positive":
    g.add((community_impact_uri, RDF.type, LGBTQPortrayal.PositiveRoleModel))
  elif impact_value.lower() == "negative":
    g.add((community_impact_uri, RDF.type, LGBTQPortrayal.NegativeRoleModel))

  # Collegare la portrayal all'impatto sulla comunità
  g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, community_impact_uri))

  # Aggiungere la giustificazione come rdfs:comment
  if impact_justification:
    g.add((community_impact_uri, RDFS.comment, Literal(impact_justification, datatype=XSD.string)))

    # Mappa per i Character Type
  character_type_map = {
    "Authentic Representation": LGBTQPortrayal.AuthenticRepresentation,
    "Comic Sidekick": LGBTQPortrayal.ComicSidekick,
    "Token Character": LGBTQPortrayal.TokenCharacter,
    "Queerprotagonist Lead Role": LGBTQPortrayal.QueerProtagonistLeadRole
}

# Recuperiamo il Character Type dal dataset
  character_type_uri = character_type_map.get(row["Character Type"], LGBTQPortrayal.CharacterType)

# Assegniamo il Character Type al Character
  g.add((character_uri, RDF.type, character_type_uri))
  g.add((LGBTQPortrayal.CharacterType, RDFS.subClassOf, persp.Cut))

  g.add((LGBTQPortrayal.AuthenticRepresentation, RDF.type, LGBTQPortrayal.CharacterType))
  g.add((LGBTQPortrayal.ComicSidekick, RDF.type, LGBTQPortrayal.CharacterType))
  g.add((LGBTQPortrayal.TokenCharacter, RDF.type, LGBTQPortrayal.CharacterType))
  g.add((LGBTQPortrayal.QueerProtagonistLeadRole, RDF.type, LGBTQPortrayal.CharacterType))

  
# Salva il grafo RDF in un file
g.serialize("LGBTQPortrayal_with_data.ttl1", format="turtle")




  


  





 
  



