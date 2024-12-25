from rdflib import Graph, Namespace, Literal, RDF, RDFS
from rdflib.namespace import DC

# Створюємо граф
g = Graph()

# Простори імен
EX = Namespace("http://example.org/schema/")
WIKI = Namespace("https://uk.wikipedia.org/wiki/S.T.A.L.K.E.R._2:_Серце_Чорнобиля#")
g.bind("dc", DC)
g.bind("ex", EX)

# Опис статті "S.T.A.L.K.E.R. 2"
g.add((WIKI.STALKER2, RDF.type, EX.Article))
g.add((WIKI.STALKER2, DC.title, Literal("S.T.A.L.K.E.R. 2: Серце Чорнобиля")))
g.add((WIKI.STALKER2, DC.creator, Literal("Wikipedia Contributors")))
g.add((WIKI.STALKER2, DC.date, Literal("2024-12-25")))
g.add((WIKI.STALKER2, DC.description, Literal("Майбутня відеогра в жанрі шутер від першої особи.")))
g.add((WIKI.STALKER2, DC.subject, Literal("Відеогра, Шутер, Постапокаліпсис")))
g.add((WIKI.STALKER2, EX.hasSection, EX.Section1))

# Опис секції "Геймплей"
g.add((EX.Section1, RDF.type, EX.Section))
g.add((EX.Section1, EX.title, Literal("Геймплей")))
g.add((EX.Section1, EX.hasParagraph, EX.Paragraph1))

# Опис параграфа в секції
g.add((EX.Paragraph1, RDF.type, EX.Paragraph))
g.add((EX.Paragraph1, EX.content, Literal("Гравці досліджують зону відчуження, борються з аномаліями, збирають артефакти.")))

# Опис розробника "GSC Game World"
g.add((EX.GSCGameWorld, RDF.type, EX.Developer))
g.add((EX.GSCGameWorld, DC.title, Literal("GSC Game World")))
g.add((EX.GSCGameWorld, DC.description, Literal("Розробник відеоігор серії S.T.A.L.K.E.R.")))

# Опис платформи "Steam"
g.add((EX.Steam, RDF.type, EX.Platform))
g.add((EX.Steam, DC.title, Literal("Steam")))
g.add((EX.Steam, DC.description, Literal("Онлайн-платформа для розповсюдження ігор.")))

# Опис жанру "Survival"
g.add((EX.Survival, RDF.type, EX.Genre))
g.add((EX.Survival, DC.title, Literal("Survival")))
g.add((EX.Survival, DC.description, Literal("Жанр відеоігор, зосереджений на виживанні.")))

# Опис режиму "Singleplayer"
g.add((EX.Singleplayer, RDF.type, EX.GameMode))
g.add((EX.Singleplayer, DC.title, Literal("Singleplayer")))
g.add((EX.Singleplayer, DC.description, Literal("Режим гри для одного гравця.")))

# Опис ресурсу "S.T.A.L.K.E.R. 2 Artifact"
g.add((EX.Artifact, RDF.type, EX.GameItem))
g.add((EX.Artifact, EX.name, Literal("Артефакт")))
g.add((EX.Artifact, EX.description, Literal("Унікальний об'єкт, який можна знайти в зоні відчуження.")))
g.add((EX.Artifact, EX.usedIn, WIKI.STALKER2))

# Опис персонажа "Майор Дегтярьов"
g.add((EX.Character1, RDF.type, EX.GameCharacter))
g.add((EX.Character1, EX.name, Literal("Майор Дегтярьов")))
g.add((EX.Character1, EX.role, Literal("Протагоніст")))
g.add((EX.Character1, EX.appearsIn, WIKI.STALKER2))

# Опис мапи "Зона Відчуження"
g.add((EX.GameMap, RDF.type, EX.GameMap))
g.add((EX.GameMap, EX.name, Literal("Зона Відчуження")))
g.add((EX.GameMap, EX.size, Literal("5km x 5km")))
g.add((EX.GameMap, EX.usedIn, WIKI.STALKER2))

# Опис класа "Tool" як підкласу "GameItem"
g.add((EX.Tool, RDF.type, RDFS.Class))
g.add((EX.Tool, RDFS.subClassOf, EX.GameItem))
g.add((EX.Tool, DC.title, Literal("Tool")))
g.add((EX.Tool, DC.description, Literal("Інструмент, використовуваний у грі для різних завдань.")))

# Приклад ресурсу підкласу Tool
g.add((EX.Detector, RDF.type, EX.Tool))
g.add((EX.Detector, EX.name, Literal("Детектор")))
g.add((EX.Detector, EX.description, Literal("Пристрій для виявлення аномалій.")))
g.add((EX.Detector, EX.usedIn, WIKI.STALKER2))

# Збереження RDF-документа у файл
with open("stalker2_detailed.rdf", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

print("RDF-документ створено як 'stalker2_detailed.rdf'")
