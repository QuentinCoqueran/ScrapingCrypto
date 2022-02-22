import json

import config
from app.parser import parse_reports
# TODO : penser a une refactor avec des décorateurs

FILE_PATH = config.REPORT_FILE_NAME


def get_json():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)


def get_all_reports():
    json_data = get_json()
    return parse_reports(json_data)


def save_all_reports(reports):
    with open(FILE_PATH, 'w') as outfile:
        json_data = json.dumps([dict(report) for report in reports])
        print(json_data)
        #json.dump(json_data, outfile)


def get_report_by_idx(idx):
    reports = get_all_reports()
    return reports[idx]


def append_report(report):
    reports = get_all_reports()
    reports.append(report)
    save_all_reports(reports)


def edit_report(idx, report_updated):
    reports = get_all_reports()
    reports[idx] = report_updated
    save_all_reports(reports)


def delete_report(idx):
    reports = get_all_reports()
    reports.pop(idx)
    save_all_reports(reports)
