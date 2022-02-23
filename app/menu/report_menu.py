from app.model.Report import Report
from app.utils import json_report_util
from app.menu.menu import clearscreen, choose_menu, back, back_no_confirmation, CoinMenu, CurrencyMenu


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
            CreateReportMenu.start()
        elif choice == 3:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.report_details_menu.report_edition_menu.start_create()


class ReportDetailMenu:

    def __init__(self):
        self.report_edition_menu = ReportEditionMenu()

    def start(self):
        clearscreen()
        reports = json_report_util.get_all_reports()
        print("--  MES RAPPORTS --\n")
        if len(reports):
            for idx, report in enumerate(reports):
                print(f'{idx}. {report.name}')
            idx = choose_menu("Rapport", len(reports))
            self.show_report_details(reports[idx])
            self.report_detail_menu(idx)
        else:
            print("Aucun rapport disponible.")
            back_no_confirmation()

    @staticmethod
    def show_report_details(report):
        clearscreen()
        print(f'\nRapport : {report.name}')
        print("Les cryptomonnaies : ", [f'{coin.name},' for coin in report.coins])
        print("Les monnaies de comparaisons : ", [f'{curr.short_name},' for curr in report.currencies])

    def report_detail_menu(self, idx):
        menu_text = "\n1.Modifier le rapport\n2.Supprimer le rapport\n3.Quitter\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.report_edition_menu.start_edit(idx)
        elif choice == 2:
            json_report_util.delete_report(idx)
            back_no_confirmation()
            return
        elif choice == 3:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.report_detail_menu(idx)


class ReportEditionMenu:

    def start_edit(self, idx):
        clearscreen()
        report = json_report_util.get_report_by_idx(idx)
        ReportDetailMenu.show_report_details(report)
        menu_text = "\n1.Renommer le rapport\n2.Ajouter une cryptomonnaie\n3.Retirer une cryptomonnaie\n4.Ajouter une " \
                    "monnaie\n5.Retirer une monnaie\n6.Sauvegarder et Quitter\n7.Annuler et quitter\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            report.name = 'nouveau'
            json_report_util.edit_report(idx, report)

        elif choice == 2:
            return
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start_edit(report)

    def start_create(self):
        pass

    def rename(self):
        pass

    def edit_coins(self):
        pass

    def edit_currencies(self):
        pass


class CreateReportMenu:

    @staticmethod
    def start():
        name = input("Nom du rapport : (Rapport) ") or "Rapport"
        coins = CreateReportMenu.coin_menu()
        currencies = CreateReportMenu.currency_menu()
        json_report_util.append_report(Report(name, coins, currencies))

    @staticmethod
    def coin_menu():
        coins = []
        print("-- Les cryptomonnaies --")
        adding = True
        while adding:
            print("Ajouter une cryptomonnaie au rapport : ")
            coins.append(CoinMenu.choose_coin())
            adding = input("Ajouter une autre cryptomonnaie ? (O/n) ") != "n"
        return coins

    @staticmethod
    def currency_menu():
        currencies = []
        print("-- Les monnaies --")
        adding = True
        while adding:
            currencies.append(CurrencyMenu.choose_currency())
            adding = input("Ajouter une autre monnaie ? (O/n) ") != "n"
        return currencies
