import json

import config
from app.menu.menu import clearscreen, choose_menu
from app.parser import parse_reports

class ReportMenu:

    def __init__(self):
        self.report_details_menu = ReportDetailMenu()

    def start(self):
        clearscreen()
        menu_text = "\n1.Tous mes rapports\n2.Nouveau rapport\n3.Retour\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.report_details_menu.all_reports()
            self.start()
        elif choice == 2:
            self.new_report()
            self.start()
            # TODO : Créer un fichier rapport Json
        elif choice == 3:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start()

    @staticmethod
    def my_reports():
        print("\nTous mes rapports")

    @staticmethod
    def new_report():
        print("-- Création d'un rapport --")


class ReportDetailMenu:

    def __init__(self):
        self.report_file = config.REPORT_FILE_NAME

    def all_reports(self):
        reports = self.get_all_reports()
        for idx, report in enumerate(reports):
            print(f'{idx}. {report.name}')
        choose_menu("Rapport", len(reports))

    def get_all_reports(self):
        with open(self.report_file) as f:
            val = json.load(f)
            return parse_reports(val)


class ReportGenerationMenu:
    pass