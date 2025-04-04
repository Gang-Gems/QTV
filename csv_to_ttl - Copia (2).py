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

df = pd.read_csv("new_final_dataset_comma.csv", dtype=str).fillna("")

for index, row in df.iterrows():
    # 2a) Build a Character individual
    char_name = row["Character Name"].strip()
    character_uri = LGBTQPortrayal[f"Character_{char_name.replace(' ', '_')}"]
    g.add((character_uri, RDF.type, LGBTQPortrayal.Character))
    g.add((character_uri, RDFS.label, Literal(char_name, datatype=XSD.string)))
    
    # Gender of the character
    if row["Gender of the character"] == "Female":
        g.add((character_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Female))
    elif row["Gender of the character"] == "Male":
        g.add((character_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Male))
    elif row["Gender of the character"] == "Non-binary":
        g.add((character_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.NonBinary))
    else:
        # fallback
        g.add((character_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Gender))

    # Transgender Character?  # <-- IMPORTANT: attach to the character, not the Gender class
    if row["Transgender Character"].strip().lower() == "yes":
        g.add((character_uri, LGBTQPortrayal.isTransgender, Literal(True, datatype=XSD.boolean)))
    else:
        g.add((character_uri, LGBTQPortrayal.isTransgender, Literal(False, datatype=XSD.boolean)))

    # Sexual orientation
    # Map each possible value to a known URI in your ontology
    orientation_map = {
        "Bisexual": LGBTQPortrayal.Bisexual,
        "Gay": LGBTQPortrayal.Gay,
        "Lesbian": LGBTQPortrayal.Lesbian,
        "Questioning": LGBTQPortrayal.Questioning,
        "Pansexual": LGBTQPortrayal.Pansexual,
        "Queer": LGBTQPortrayal.Queer,
        "Not specified": LGBTQPortrayal.NotSpecified
    }
    char_orientation_uri = orientation_map.get(row["Sex Orientation of character"], LGBTQPortrayal.SexOrientation)
    g.add((character_uri, LGBTQPortrayal.hasSexOrientation, char_orientation_uri))

    # 2b) Performer
    performer_name = row["Performer"].strip()
    performer_uri = LGBTQPortrayal[f"Performer_{performer_name.replace(' ', '_')}"]
    g.add((performer_uri, RDF.type, LGBTQPortrayal.Performer))
    g.add((performer_uri, RDFS.label, Literal(performer_name, datatype=XSD.string)))

    # Link character to performer (usually you'd do show -> actor -> performer, but let's follow your code)
    g.add((character_uri, schema.actor, performer_uri))

    # Gender of performer
    performer_gender = row["Gender of performer"].strip()
    if performer_gender == "Female":
        g.add((performer_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Female))
    elif performer_gender == "Male":
        g.add((performer_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Male))
    elif performer_gender == "Non-binary":
        g.add((performer_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.NonBinary))
    else:
        g.add((performer_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Gender))

    # Transgender performer
    perf_is_trans = (row["Transgender Performer"].strip().lower() == "yes")
    g.add((performer_uri, LGBTQPortrayal.isTransgender, Literal(perf_is_trans, datatype=XSD.boolean)))

    # Performer’s sexual orientation
    perf_orientation_uri = orientation_map.get(row["Sex orientation of performer"], LGBTQPortrayal.SexOrientation)
    g.add((performer_uri, LGBTQPortrayal.hasSexOrientation, perf_orientation_uri))

    # 2c) Creator
    creator_name = row["Creator"].strip()
    creator_uri = LGBTQPortrayal[f"Creator_{creator_name.replace(' ', '_')}"]
    g.add((creator_uri, RDF.type, LGBTQPortrayal.Creator))
    g.add((creator_uri, RDFS.label, Literal(creator_name, datatype=XSD.string)))

    # Gender of creator
    creator_gender = row["Gender of creator"].strip()
    if creator_gender == "Female":
        g.add((creator_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Female))
    elif creator_gender == "Male":
        g.add((creator_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Male))
    elif creator_gender == "Non-binary":
        g.add((creator_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.NonBinary))
    else:
        g.add((creator_uri, LGBTQPortrayal.hasGender, LGBTQPortrayal.Gender))

    # Transgender creator
    creator_is_trans = (row["Transgender creator"].strip().lower() == "yes")
    g.add((creator_uri, LGBTQPortrayal.isTransgender, Literal(creator_is_trans, datatype=XSD.boolean)))

    # Creator’s sexual orientation
    creator_orientation_uri = orientation_map.get(row["Sex orientation of creator"], LGBTQPortrayal.SexOrientation)
    g.add((creator_uri, LGBTQPortrayal.hasSexOrientation, creator_orientation_uri))

    # 2d) TV Show
    show_title = row["Show Title"].strip()
    tvshow_uri = LGBTQPortrayal[f"TvShow_{show_title.replace(' ', '_').replace('""', '').replace(',', '')}"]
    g.add((tvshow_uri, RDF.type, LGBTQPortrayal.TvShow))
    g.add((tvshow_uri, RDFS.label, Literal(show_title, datatype=XSD.string)))

    # Usually you'd do tvshow -> schema:character -> character
    g.add((tvshow_uri, schema.character, character_uri))

    # Usually you'd do tvshow -> schema:creator -> creator
    g.add((tvshow_uri, schema.creator, creator_uri))

    # Year
    g.add((tvshow_uri, schema.datePublished, Literal(str(row["Year"]), datatype=XSD.gYear)))

    # Place of publication -> country
    country_label = row["Place of publication"].strip()
    if country_label:
        country_uri = LGBTQPortrayal[f"Country_{country_label.replace(' ', '_')}"]
        g.add((country_uri, RDF.type, schema.Country))
        g.add((country_uri, RDFS.label, Literal(country_label, datatype=XSD.string)))
        g.add((tvshow_uri, schema.countryOfOrigin, country_uri))

    # Genre
    genre_label = row["Genre of the tv-series"].strip()
    if genre_label:
        genre_uri = LGBTQPortrayal[f"Genre_{genre_label.replace(' ', '_').replace('""', '').replace(',', '')}"]
        g.add((genre_uri, RDF.type, LGBTQPortrayal.Genre))
        g.add((genre_uri, RDFS.label, Literal(genre_label, datatype=XSD.string)))
        g.add((tvshow_uri, schema.genre, genre_uri))

    # Production company
    production_label = row["Production company"].strip()
    if production_label:
        production_uri = LGBTQPortrayal[f"Production_{production_label.replace(' ', '_')}"]
        g.add((production_uri, RDF.type, LGBTQPortrayal.ProductionAndIndustryFactory))
        g.add((production_uri, RDFS.label, Literal(production_label, datatype=XSD.string)))
        # IMPORTANT: use schema.productionCompany (or your own property) instead of the class
        g.add((tvshow_uri, schema.productionCompany, production_uri))

    # 2e) Portrayal instance
    portrayal_uri = LGBTQPortrayal[f"Portrayal_{char_name.replace(' ', '_')}"]
    g.add((portrayal_uri, RDF.type, LGBTQPortrayal.PortrayalofLgbtqCharacter))

    # Link character -> hasPortrayal -> portrayal
    g.add((character_uri, LGBTQPortrayal.hasPortrayal, portrayal_uri))

    # Representation type: Fair or Unfair
    rep_type = row["Representation Type"].strip().lower()
    if rep_type == "fair":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.FairRepresentation))
        # Possibly link to PositiveRoleModel
        g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, LGBTQPortrayal.PositiveRoleModel))
    elif rep_type == "unfair":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.UnfairRepresentation))
        # Possibly link to NegativeRoleModel
        g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, LGBTQPortrayal.NegativeRoleModel))
    else:
        # fallback
        pass

    # Justification
    justification_text = row["Justification for Classification"].strip()
    if justification_text:
        g.add((portrayal_uri, RDFS.comment, Literal(justification_text, datatype=XSD.string)))

    # Authenticity
    if row["Authenticity"].strip().lower() == "yes":
        # Typically you do RDF.type, not rdfs:subClassOf
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.Authenticity))

    # Affirmation of Identity
    if row["Affirmation of Identity"].strip().lower() == "yes":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.AffirmationOfIdentity))

    # Normalization of Relationship
    if row["Normalization of Relationship"].strip().lower() == "yes":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.NormalizationOfRelationship))

    # Gay Best Friend
    if row["Gay Best Friend"].strip().lower() == "yes":
        gbf_uri = LGBTQPortrayal[f"GayBestFriend_{char_name.replace(' ', '_')}"]
        g.add((gbf_uri, RDF.type, LGBTQPortrayal.GayBestFriend))

    # Tragic Trope
    if row["Tragic Trope"].strip().lower() == "yes":
        tragic_uri = LGBTQPortrayal[f"TragicTrope_{char_name.replace(' ', '_')}"]
        g.add((tragic_uri, RDF.type, LGBTQPortrayal.TragicTrope))

    # 2f) Depth of portrayal
    depth_value = row["Portrayal"].strip().lower()
    if depth_value == "detailed":
        # up to you if you define separate classes Detailed / Superficial
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.Detailed))
    elif depth_value == "superficial":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.Superficial))

    g.add((LGBTQPortrayal.Detailed, RDF.type, LGBTQPortrayal.CharacterDepth))
    g.add((LGBTQPortrayal.Detailed, RDFS.subClassOf, LGBTQPortrayal.CharacterDepth))

    g.add((LGBTQPortrayal.Superficial, RDF.type, LGBTQPortrayal.CharacterDepth))
    g.add((LGBTQPortrayal.Superficial, RDFS.subClassOf, LGBTQPortrayal.CharacterDepth))


    # 2g) Impact on LGBTQ Community
    impact_value = row["LGBTQ Community Impact"].strip().lower()
    impact_justif = row["LGBTQ Community Impact Justification"].strip()
    if impact_value in ("positive", "negative"):
        # Create an instance for the "impact" if you wish
        impact_uri = LGBTQPortrayal[f"Impact_{char_name.replace(' ', '_')}"]
        g.add((impact_uri, RDF.type, LGBTQPortrayal.LGBTQCommunityImpact))
        g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, impact_uri))
        if impact_justif:
            g.add((impact_uri, RDFS.comment, Literal(impact_justif, datatype=XSD.string)))
        if impact_value == "positive":
            g.add((impact_uri, RDF.type, LGBTQPortrayal.PositiveRoleModel))
        else:
            g.add((impact_uri, RDF.type, LGBTQPortrayal.NegativeRoleModel))

    # 2h) Character Type (e.g. "Authentic Representation", "Token Character", etc.)
    ctype = row["Character Type"].strip()
    char_type_map = {
        "Authentic Representation": LGBTQPortrayal.AuthenticRepresentation,
        "Comic Sidekick": LGBTQPortrayal.ComicSidekick,
        "Token Character": LGBTQPortrayal.TokenCharacter,
        "Queerprotagonist Lead Role": LGBTQPortrayal.QueerProtagonistLeadRole
    }
    ctype_uri = char_type_map.get(ctype, LGBTQPortrayal.CharacterType)
    g.add((character_uri, RDF.type, ctype_uri))
    # Le istanze della classe CharacterType
# Dichiarare esplicitamente le istanze come NamedIndividual
# Dichiarare le entità come istanze di CharacterType
g.add((LGBTQPortrayal.AuthenticRepresentation, RDF.type, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.ComicSidekick, RDF.type, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.TokenCharacter, RDF.type, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.QueerProtagonistLeadRole, RDF.type, LGBTQPortrayal.CharacterType))

# Dichiarare le stesse entità anche come classi (subclassi di CharacterType)
g.add((LGBTQPortrayal.AuthenticRepresentation, RDFS.subClassOf, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.ComicSidekick, RDFS.subClassOf, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.TokenCharacter, RDFS.subClassOf, LGBTQPortrayal.CharacterType))
g.add((LGBTQPortrayal.QueerProtagonistLeadRole, RDFS.subClassOf, LGBTQPortrayal.CharacterType))



# ------------------------------------------------------------------------------
# 3) Finally, serialize your graph
# ------------------------------------------------------------------------------
g.serialize("LGBTQPortrayal_with_data.ttl1", format="turtle")
print("RDF data written to LGBTQPortrayal_with_data.ttl1")

