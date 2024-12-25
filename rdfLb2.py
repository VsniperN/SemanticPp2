from rdflib import Graph, Literal, Namespace, RDF
from rdflib.namespace import DC

# Створюємо граф
g = Graph()

# Простори імен
EX = Namespace("http://example.org/schema/")
WIKI = Namespace("https://uk.wikipedia.org/wiki/S.T.A.L.K.E.R._2:_Серце_Чорнобиля#")
g.bind("dc", DC)
g.bind("ex", EX)

# Опис статті
g.add((WIKI.STALKER2, RDF.type, EX.Article))
g.add((WIKI.STALKER2, DC.title, Literal("S.T.A.L.K.E.R. 2: Серце Чорнобиля")))
g.add((WIKI.STALKER2, DC.creator, Literal("Wikipedia Contributors")))
g.add((WIKI.STALKER2, DC.date, Literal("2024-12-25")))
g.add((WIKI.STALKER2, DC.description, Literal("S.T.A.L.K.E.R. 2 — це майбутня відеогра в жанрі шутер від першої особи.")))
g.add((WIKI.STALKER2, DC.subject, Literal("Відеогра, Шутер, Survival, Постапокаліпсис")))
g.add((WIKI.STALKER2, EX.hasSection, EX.Section1))

# Опис секції "Геймплей"
g.add((EX.Section1, RDF.type, EX.Section))
g.add((EX.Section1, EX.title, Literal("Геймплей")))
g.add((EX.Section1, EX.hasParagraph, EX.Paragraph1))

# Опис параграфа в секції
g.add((EX.Paragraph1, RDF.type, EX.Paragraph))
g.add((EX.Paragraph1, EX.content, Literal("Гравці досліджують Зону відчуження, борються з аномаліями і збирають артефакти.")))

# Опис розробника "GSC Game World"
g.add((EX.GSCGameWorld, RDF.type, EX.Developer))
g.add((EX.GSCGameWorld, DC.title, Literal("GSC Game World")))
g.add((EX.GSCGameWorld, DC.description, Literal("Українська студія, розробник серії S.T.A.L.K.E.R.")))

# Опис платформи "Steam"
g.add((EX.Steam, RDF.type, EX.Platform))
g.add((EX.Steam, DC.title, Literal("Steam")))
g.add((EX.Steam, DC.description, Literal("Онлайн-платформа для розповсюдження ігор.")))

# Опис жанру "Survival"
g.add((EX.Survival, RDF.type, EX.Genre))
g.add((EX.Survival, DC.title, Literal("Survival")))
g.add((EX.Survival, DC.description, Literal("Жанр відеоігор, зосереджений на виживанні персонажів.")))

# Опис режиму "Singleplayer"
g.add((EX.Singleplayer, RDF.type, EX.GameMode))
g.add((EX.Singleplayer, DC.title, Literal("Singleplayer")))
g.add((EX.Singleplayer, DC.description, Literal("Режим гри для одного гравця.")))

# Збереження RDF-документа у файл
with open("stalker2.rdf", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

print("RDF-документ створено як 'stalker2.rdf'")
