from datetime import datetime

class Rekord1P:

    def __init__(self, criteria):
        self.pei = 0
        self.criteria = criteria
        self.status = criteria.state
        self.process = criteria.process
        self.filter = criteria.filter
        self.new_account = False
        self.zmiana_urzadzen = False
        self.AdresInstalacyjny = ""

    def get_action(self, actions, action):
        for e in actions:
            if action in e:
                return e
        return ""

    def create_from_db(self, p):
        self.pei = p.get("pei")
        self.status = p.get("status")

    def __str__(self):
        return f"({self.pei}, " \
               f"{self.status}, "


class Uwaga:

    def __init__(self):
        self.canRemove = True
        self.id = 0
        self.message = ""
        self.createDate = "2021-03-16 10:33:58"
        self.creator = ""
        self.location_data1 = 0
        self.location_author1 = 0
        self.location_entry1 = 0
        self.location_data2 = 0
        self.location_author2 = 0
        self.location_entry2 = 0
        self.location_ending = 0

    def convert2textAPI(self, uwagi):
        section1 = "["
        section2 = ", "
        section3 = "]"
        ret = section1

        for i, u in enumerate(uwagi):
            ret += "{"
            ret += f"\"canRemove\":false,\"id\":{i},\"message\":\"{u.message}\",\"createDate\":\"{u.createDate}\",\"creator\":\"{u.creator}\""
            ret += "}"
            if i < len(uwagi) - 1:
                ret += section2

        ret += section3
        return ret

    def convert2textDB(self, uwaga):
        ret = ""
        for i, u in enumerate(uwaga):
            ret += f"{i}, Data utworzenia: {u.createDate}, Twórca: {u.creator}, Treść: {u.message} \n"
        return ret

    def convert2uwaga(self, textDB):
        ret = []
        for r in textDB.split("\n"):
            if 'Data utworzenia: ' in r and 'Twórca: ' in r and 'Treść: ' in r:
                u = Uwaga()
                u.location_data1 = r.index('Data utworzenia: ') + len('Data utworzenia: ')
                u.location_data2 = r.index('Twórca: ') - 2
                u.location_author1 = r.index('Twórca: ') + len('Twórca: ')
                u.location_author2 = r.index('Treść: ') - 2
                u.location_entry1 = r.index('Treść: ') + len('Treść: ')
                u.location_entry2 = len(r) - 1
                u.location_ending = len(r)
                u.createDate = r[u.location_data1:u.location_data2]
                u.creator = r[u.location_author1:u.location_author2]
                u.message = r[u.location_entry1:u.location_entry2]
                ret.append(u)
        return ret


    def __repr__(self):
        return " ( " + str(self.createDate) + ", " + str(self.creator) + ", " + str(self.message) + " )"

    pass


if __name__ == "__main__":
    u = Uwaga()
    response = "2, Data utworzenia: 2021-03-16 10:33:58, Twórca: Joanna Jankowska-Mikułowicz, Treść: Wpis testowy nr 1, oraz nr 2. \n3, Data utworzenia: 2021-03-16 10:33:58, Twórca: Joanna Jankowska-Mikułowicz, Treść: Wpis testowy nr 3, oraz nr 4. \n"
    t = u.convert2uwaga(response)
    print(t)
    pass