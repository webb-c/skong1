from pcconfig import config
import pynecone as pc

class State(pc.State):
    total_clicks = 0
    def increase_clicks(self):
        self.total_clicks += 1
    def decrese_clicks(self):
        self.total_clicks -= 1

def topBar():
    return pc.hstack(
                pc.link(pc.text("HBD"), href="http://localhost:3000/"),
                pc.link(pc.text("GIFT"), href="http://localhost:3000/gift"),
                pc.link(pc.text("LETTER"), href="http://localhost:3000/letter"),
                pc.link(pc.text("TIMELINE"), href="http://localhost:3000/timeline"),
                spacing="150px",
                font_size="1em",
                margin_bottom="5%"
            )

def bottom():
    return pc.hstack(
        pc.link(
            pc.tooltip(
                pc.image(src="/data/github-mark.png", width="2em"),
                label="More detail"
            ),
            href ="https://github.com/webb-c/skong1",
        ),
        pc.link(
            pc.tooltip(
                pc.image(src="/data/gmail.png", width="2em"),
                label="Send Thanks!"
            ),
            href = "mailto:jwst0210@gmail.com",
        ),
        spacing="50px"
    )

# HBD (home)
def index():
    return pc.center(
        pc.vstack(
            topBar(),
            pc.heading(
                "Happy Birthday!",
                font_size="2em",
                margin_bottom=20,
            ),
            pc.image(src="/data/cake.png", width="30em", margin_bottom=20),
            bottom(),
            spacing="20px"
        ),
        padding_top="3%",
    )

# GIFT
def gift():
    return pc.center(
        pc.vstack(
            topBar(),
            pc.heading(
                "Gift",
                font_size="2em",
                margin_bottom=20,
            ),
            bottom(),
            spacing="20px"
        ),
        padding_top="3%",
    )
# LETTER
def letter():
    return pc.center(
        pc.vstack(
            topBar(),
            pc.heading(
                "Dear...",
                font_size="2em",
                margin_bottom=20,
            ),
            pc.text("상세한 편지 내용", margin_bottom=20),
            bottom(),
            spacing="20px"
        ),
        padding_top="3%",
    )
# TIMELINE
def timeline():
    return pc.center(
        pc.vstack(
            topBar(),
            pc.heading(
                "Timeline",
                font_size="2em",
                margin_bottom=20,
            ),
            bottom(),
            spacing="20px"
        ),
        padding_top="3%",
    )

app = pc.App(state=State)
app.add_page(index)
app.add_page(gift)
app.add_page(letter)
app.add_page(timeline)
app.compile()