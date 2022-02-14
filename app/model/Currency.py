class Currency:

    def __init__(self, short_name):
        self.short_name = short_name

    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        self._short_name = short_name

    def __str__(self):
        return f"{{ \"short_name\" : \"{self.short_name}\" }}"

