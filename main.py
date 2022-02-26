# coding: utf-8

from app.App import App
from app.template_editor.editor import generate_template
from app.mail import send_mail
from app.api.request_manager import request_manager


def main():
    app = App()
    app.start()


if __name__ == '__main__':
    main()