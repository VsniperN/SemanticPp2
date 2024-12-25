from rdflib import Graph

# Шлях до RDF-документа
rdf_file = "stalker2_resources.rdf"

# Завантаження графа
g = Graph()
g.parse(rdf_file, format="turtle")

# --- Перевірка валідності ---
try:
    print(f"Документ '{rdf_file}' успішно завантажено.")
except Exception as e:
    print(f"Помилка завантаження RDF-документа: {e}")
    exit()

# --- Виведення всіх тріплетів ---
print("\nВсі тріплети у форматі 'суб'єкт-предикат-об'єкт':")
for subj, pred, obj in g:
    print(f"Суб'єкт: {subj}, Предикат: {pred}, Об'єкт: {obj}")

# --- Підрахунок тріплетів ---
triplet_count = len(g)
print(f"\nЗагальна кількість тріплетів у RDF-документі: {triplet_count}")
