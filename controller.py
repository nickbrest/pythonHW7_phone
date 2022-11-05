import function
import menu


def button_click():
    while True:
        menu.show_menu()
        choice = menu.control_menu()
        if choice == 1:
            function.add_note()
        if choice == 2:
            function.delete_entry()
        if choice == 3:
            function.import_format_1()
        # if choice == 4:
        #      function.import_format_2()
        # if choice == 5:
        #     function.export_format_1()
        if choice == 6:
            function.export_format_2()
        if choice == 7:
            function.print_list()
        if choice == 8:
            function.search_surname()
        if choice == 0:
            function.exit_program()
            break
        function.goback_menu()

