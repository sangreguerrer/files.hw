recipes=[]
with open("recipes.txt","rt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ing_count = int(file.readline().strip())
        ingredient_list = []
        for _ in range(ing_count):
            nqm = file.readline().strip().split('|')
            name, quantity, measure=nqm
            ingredient_list.append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish]=ingredient_list


        def get_shop_list_by_dishes(dishes, person_count:int):
            total_ingrs={}
            for dish in dishes:
                if dish in cook_book:
                    for spot in cook_book[dish]:
                        parameters={'quantity':int(spot['quantity'])*person_count,'measure':spot['measure']}
                        if spot['ingredient_name'] in total_ingrs:
                            total_ingrs[spot['ingredient_name']]['quantity']+=int(spot['quantity'])
                        else:
                            total_ingrs[spot['ingredient_name']]=parameters
                    
                else:
                    print(f"'Блюдо' {dish}'не найдено")
            print(total_ingrs)


news_dict={}
sort_list=[]
file_list=['1.txt','2.txt','3.txt']
for files in file_list:
    with open(files,'r',encoding="utf-8") as part:
        text=len(part.readlines())
        sort_list.append(text)
        news_dict=dict(zip(sort_list,file_list))
        sorted_dict = dict(sorted(news_dict.items()))
        with open('new_text.txt','w+',encoding="utf-8") as outfile:
            for key,value in sorted_dict.items():
                with open(value,'r',encoding="utf-8") as part1:
                    contain=f'{value}\n{key}\n{part1.read()}\n'
                    outfile.write(contain)


print(cook_book)
print()
get_shop_list_by_dishes(['Омлет','Оливье'],7)