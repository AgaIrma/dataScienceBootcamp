from optparse import Values


print('Lista zakupów');
shopping_dict = {
    "Piekarnia":     ["Chleb","Pączek","Bułka"],
    "Warzywniak":    ["Marchew", "Seler", "Ziemniaki"]
    }

shopping_items = []
for shopping_dict_key in shopping_dict:
    shopping_dict_values = shopping_dict.get(shopping_dict_key)
    print(f"Ide do {shopping_dict_key}, kupuję tu następujące rzeczy: {shopping_dict_values}")
    shopping_items = shopping_items + shopping_dict_values
print(f"W sumie kupuję { len(shopping_items)}  produktów");
