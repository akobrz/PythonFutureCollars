from projekt.portals import portal_olx

def start():
    p = portal_olx.Portal_Olx()
    p.load_page(1)
    p.load_page(2)


if __name__ == "__main__":
    start()
