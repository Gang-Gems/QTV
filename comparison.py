# 2e) Portrayal instance
    portrayal_uri = LGBTQPortrayal[f"Portrayal_{char_name.replace(' ', '_')}"]
    g.add((portrayal_uri, RDF.type, LGBTQPortrayal.PortrayalofLgbtqCharacter))

    # Link character -> hasPortrayal -> portrayal
    g.add((character_uri, LGBTQPortrayal.hasPortrayal, portrayal_uri))

    # Representation type: Fair or Unfair
    rep_type = row["Representation Type"].strip().lower()
    if rep_type == "Fair Representation":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.FairRepresentation))
        # Possibly link to PositiveRoleModel
        g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, LGBTQPortrayal.PositiveRoleModel))
    elif rep_type == "Unfair Representation":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.UnfairRepresentation))
        # Possibly link to NegativeRoleModel
        g.add((portrayal_uri, LGBTQPortrayal.impactsCommunity, LGBTQPortrayal.NegativeRoleModel))
    else:
        # fallback
        pass
    g.add((LGBTQPortrayal.FairRepresentation, RDFS.subClassOf, LGBTQPortrayal.RepresentationType))

    g.add((LGBTQPortrayal.UnfairRepresentation, RDFS.subClassOf, LGBTQPortrayal.RepresentationType))

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

    # Dynamic Role
    if row["Dynamic Role"].strip().lower() == "yes":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.Dynamic))

# Static Role
    if row["Static Role"].strip().lower() == "yes":
        g.add((portrayal_uri, RDF.type, LGBTQPortrayal.Static))

# Character Transformation
    transformation_justif = row["Character Transformation"].strip()
    if transformation_justif:
        transf_uri = LGBTQPortrayal[f"CharacterTransformation_{char_name.replace(' ', '_')}"]
    g.add((transf_uri, RDF.type, LGBTQPortrayal.CharacterTransformation))
    g.add((portrayal_uri, LGBTQPortrayal.hasNarrativeFunction, transf_uri))
    g.add((transf_uri, RDFS.comment, Literal(transformation_justif, datatype=XSD.string)))

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
