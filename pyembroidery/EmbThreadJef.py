from .EmbThread import EmbThread






def get_thread_set():
    return [
        EmbThreadJef(0x000000, "Placeholder", "000"),
        EmbThreadJef(0x000000, "Black", "002"),
        EmbThreadJef(0xffffff, "White", "001"),
        EmbThreadJef(0xffff17, "Yellow", "204"),
        EmbThreadJef(0xff6600, "Orange", "203"),
        EmbThreadJef(0x2f5933, "Olive Green", "219"),
        EmbThreadJef(0x237336, "Green", "226"),
        EmbThreadJef(0x65c2c8, "Sky", "217"),
        EmbThreadJef(0xab5a96, "Purple", "208"),
        EmbThreadJef(0xf669a0, "Pink", "201"),
        EmbThreadJef(0xff0000, "Red", "225"),
        EmbThreadJef(0xb1704e, "Brown", "214"),
        EmbThreadJef(0x0b2f84, "Blue", "207"),
        EmbThreadJef(0xe4c35d, "Gold", "003"),
        EmbThreadJef(0x481a05, "Dark Brown", "205"),
        EmbThreadJef(0xac9cc7, "Pale Violet", "209"),
        EmbThreadJef(0xfcf294, "Pale Yellow", "210"),
        EmbThreadJef(0xf999b7, "Pale Pink", "211"),
        EmbThreadJef(0xfab381, "Peach", "212"),
        EmbThreadJef(0xc9a480, "Beige", "213"),
        EmbThreadJef(0x970533, "Wine Red", "215"),
        EmbThreadJef(0xa0b8cc, "Pale Sky", "216"),
        EmbThreadJef(0x7fc21c, "Yellow Green", "218"),
        EmbThreadJef(0xe5e5e5, "Silver Gray", "220"),
        EmbThreadJef(0x889b9b, "Gray", "221"),
        EmbThreadJef(0x98d6bd, "Pale Aqua", "227"),
        EmbThreadJef(0xb2e1e3, "Baby Blue", "228"),
        EmbThreadJef(0x368ba0, "Powder Blue", "229"),
        EmbThreadJef(0x4f83ab, "Bright Blue", "230"),
        EmbThreadJef(0x386a91, "Slate Blue", "231"),
        EmbThreadJef(0x071650, "Navy Blue", "232"),
        EmbThreadJef(0xf999a2, "Salmon Pink", "233"),
        EmbThreadJef(0xf9676b, "Coral", "234"),
        EmbThreadJef(0xe3311f, "Burnt Orange", "235"),
        EmbThreadJef(0xe2a188, "Cinnamon", "236"),
        EmbThreadJef(0xb59474, "Umber", "237"),
        EmbThreadJef(0xe4cf99, "Blond", "238"),
        EmbThreadJef(0xffcb00, "Sunflower", "239"),
        EmbThreadJef(0xe1add4, "Orchid Pink", "240"),
        EmbThreadJef(0xc3007e, "Peony Purple", "241"),
        EmbThreadJef(0x80004b, "Burgundy", "242"),
        EmbThreadJef(0x540571, "Royal Purple", "243"),
        EmbThreadJef(0xb10525, "Cardinal Red", "244"),
        EmbThreadJef(0xcae0c0, "Opal Green", "245"),
        EmbThreadJef(0x899856, "Moss Green", "246"),
        EmbThreadJef(0x5c941a, "Meadow Green", "247"),
        EmbThreadJef(0x003114, "Dark Green", "248"),
        EmbThreadJef(0x5dae94, "Aquamarine", "249"),
        EmbThreadJef(0x4cbf8f, "Emerald Green", "250"),
        EmbThreadJef(0x007772, "Peacock Green", "251"),
        EmbThreadJef(0x595b61, "Dark Gray", "252"),
        EmbThreadJef(0xfffff2, "Ivory White", "253"),
        EmbThreadJef(0xb15818, "Hazel", "254"),
        EmbThreadJef(0xcb8a07, "Toast", "255"),
        EmbThreadJef(0x986c80, "Salmon", "256"),
        EmbThreadJef(0x98692d, "Cocoa Brown", "257"),
        EmbThreadJef(0x4d3419, "Sienna", "258"),
        EmbThreadJef(0x4c330b, "Sepia", "259"),
        EmbThreadJef(0x33200a, "Dark Sepia", "260"),
        EmbThreadJef(0x523a97, "Violet Blue", "261"),
        EmbThreadJef(0x0d217e, "Blue Ink", "262"),
        EmbThreadJef(0x1e77ac, "Sola Blue", "263"),
        EmbThreadJef(0xb2dd53, "Green Dust", "264"),
        EmbThreadJef(0xf33689, "Crimson", "265"),
        EmbThreadJef(0xde649e, "Floral Pink", "266"),
        EmbThreadJef(0x984161, "Wine", "267"),
        EmbThreadJef(0x4c5612, "Olive Drab", "268"),
        EmbThreadJef(0x4c881f, "Meadow", "269"),
        EmbThreadJef(0xe4de79, "Mustard", "270"),
        EmbThreadJef(0xcb8a1a, "Yellow Ocher", "271"),
        EmbThreadJef(0xcba21c, "Old Gold", "272"),
        EmbThreadJef(0xff9805, "Honey Dew", "273"),
        EmbThreadJef(0xfcb257, "Tangerine", "274"),
    ]


class EmbThreadJef(EmbThread):
    def __init__(self, color, description, catalog_number):
        EmbThread.__init__(self)
        self.color = color
        self.description = description
        self.catalog_number = catalog_number
        self.brand = "Jef"
        self.chart = "Jef"
