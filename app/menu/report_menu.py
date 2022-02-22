import json

import config
from app.menu.menu import clearscreen, choose_menu, back
from app.parser import parse_reports


class ReportMenu:

    def __init__(self):
        self.report_details_menu = ReportDetailMenu()

    def start(self):
        clearscreen()
        menu_text = "\n1.Tous mes rapports\n2.Nouveau rapport\n3.Retour\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.report_details_menu.start()
            self.start()
        elif choice == 2:
            # self.new_report()
            self.start()
            # TODO : Créer un fichier rapport Json
        elif choice == 3:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start()


class ReportDetailMenu:

    def __init__(self):
        self.report_file = config.REPORT_FILE_NAME
        self.report_edition_menu = ReportEditionMenu()

    def start(self):
        clearscreen()
        reports = self.get_all_reports()
        print("Tous mes rapports\n")
        for idx, report in enumerate(reports):
            print(f'{idx}. {report.name}')
        choice = choose_menu("Rapport", len(reports))
        self.show_report_details(reports[choice])
        self.report_detail_menu(reports[choice])

    def get_all_reports(self):
        with open(self.report_file) as f:
            val = json.load(f)
            return parse_reports(val)

    @staticmethod
    def show_report_details(report):
        clearscreen()
        print(f'\nRapport : {report.name}')
        print("Les cryptomonnaies : ", [f'{coin.name},' for coin in report.coins])
        print("Les monnaies de comparaisons : ", [f'{curr.short_name},' for curr in report.currencies])

    def report_detail_menu(self, report):
        menu_text = "\n1.Modifier le rapport\n2.Quitter\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.report_edition_menu.start_edit(report)
        elif choice == 2:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.report_detail_menu(report)


class ReportEditionMenu:

    def start_edit(self, report):
        clearscreen()
        ReportDetailMenu.show_report_details(report)
        back()

    def start_create(self):
        pass

    def rename(self):
        pass

    def edit_coins(self):
        pass

    def edit_currencies(self):
        pass
