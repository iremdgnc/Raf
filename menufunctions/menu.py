from userproducts import add, delete, edit, list, savecsv


def user_menu():
    while True:
        selection = input("- Ürün Eklemek İçin 1'e Basın. \n- Ürün Silmek İçin 2'ye Basın. "
                          "\n- Ürün Bilgisi Düzenlemek İçin 3'e Basın. \n- Ürünleri Listelemek İçin 4'e Basın. \n- "
                          "Dosyayı 'csv' Formatında Kaydetmek İçin 5'e Basın. \n")
        if selection == '1':
            add.user_add_product()
        elif selection == '2':
            delete.user_delete_product()
        elif selection == '3':
            edit.user_edit_product()
        elif selection == '4':
            list.user_list_product()
        elif selection == '5':
            savecsv.user_save_csv()
        break

# user inputtan gelen verileri class ile al