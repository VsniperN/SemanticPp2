from rdflib import Graph, Namespace, Literal, RDF
from rdflib.namespace import DC

# Створюємо граф
g = Graph()

# Простори імен
EX = Namespace("http://example.org/schema/")
WIKI = Namespace("https://uk.wikipedia.org/wiki/S.T.A.L.K.E.R._2:_Серце_Чорнобиля#")
g.bind("dc", DC)
g.bind("ex", EX)

# Опис ресурсу "Стаття"
g.add((WIKI.STALKER2, RDF.type, EX.Article))
g.add((WIKI.STALKER2, DC.title, Literal("S.T.A.L.K.E.R. 2: Серце Чорнобиля")))
g.add((WIKI.STALKER2, DC.creator, Literal("Wikipedia Contributors")))
g.add((WIKI.STALKER2, DC.date, Literal("2024-12-25")))
g.add((WIKI.STALKER2, DC.description, Literal("Майбутня відеогра в жанрі шутер від першої особи.")))
g.add((WIKI.STALKER2, EX.hasSection, EX.Section1))

# Опис секції "Геймплей"
g.add((EX.Section1, RDF.type, EX.Section))
g.add((EX.Section1, EX.title, Literal("Геймплей")))
g.add((EX.Section1, EX.hasParagraph, EX.Paragraph1))

# Опис параграфа
g.add((EX.Paragraph1, RDF.type, EX.Paragraph))
g.add((EX.Paragraph1, EX.content, Literal("Гравці досліджують зону відчуження, збирають артефакти та борються з аномаліями.")))

# Опис розробника "GSC Game World"
g.add((EX.GSCGameWorld, RDF.type, EX.Developer))
g.add((EX.GSCGameWorld, DC.title, Literal("GSC Game World")))
g.add((EX.GSCGameWorld, DC.description, Literal("Українська студія, що розробляє S.T.A.L.K.E.R. 2.")))
g.add((WIKI.STALKER2, EX.developedBy, EX.GSCGameWorld))

# Опис платформи "Steam"
g.add((EX.Steam, RDF.type, EX.Platform))
g.add((EX.Steam, DC.title, Literal("Steam")))
g.add((EX.Steam, DC.description, Literal("Популярна онлайн-платформа для розповсюдження ігор.")))
g.add((WIKI.STALKER2, EX.availableOn, EX.Steam))

# Опис ігрового предмета "Детектор"
g.add((EX.Detector, RDF.type, EX.GameItem))
g.add((EX.Detector, EX.name, Literal("Детектор")))
g.add((EX.Detector, EX.description, Literal("Інструмент для виявлення аномалій у зоні відчуження.")))
g.add((EX.Detector, EX.usedIn, WIKI.STALKER2))

# Опис персонажа "Майор Дегтярьов"
g.add((EX.Character1, RDF.type, EX.GameCharacter))
g.add((EX.Character1, EX.name, Literal("Майор Дегтярьов")))
g.add((EX.Character1, EX.role, Literal("Протагоніст")))
g.add((EX.Character1, EX.appearsIn, WIKI.STALKER2))

# Опис мапи "Зона відчуження"
g.add((EX.GameMap, RDF.type, EX.GameMap))
g.add((EX.GameMap, EX.name, Literal("Зона відчуження")))
g.add((EX.GameMap, EX.size, Literal("5km x 5km")))
g.add((EX.GameMap, EX.usedIn, WIKI.STALKER2))

# Збереження RDF-документа у файл
with open("stalker2_resources.rdf", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

print("RDF-документ створено як 'stalker2_resources.rdf'")
