from pcconfig import config
import pynecone as pc

'''
# Welcome to Pynecone! This file outlines the steps to create a basic app.
# 기본 예시 페이지 (주석처리)
docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
'''


class State(pc.State):
    total_clicks = 0

    def increase_clicks(self):
        self.total_clicks += 1

    def decrese_clicks(self):
        self.total_clicks -= 1


def index():
    return pc.center(
        pc.vstack(
            pc.hstack(
                pc.link(pc.text("HBD"), href="http://localhost:3000/"),
                pc.link(pc.text("GIFT"), href="http://localhost:3000/gift"),
                pc.link(pc.text("LETTER"), href="http://localhost:3000/letter"),
                pc.link(pc.text("TIMELINE"), href="http://localhost:3000/timeline"),
                spacing="50px"
            ),
            pc.heading(
                "Happy Birthday!",
                font_size="2em",
                margin_bottom=20,
            ),
            pc.text("cake img"),
        ),
        padding_top="3%",
        font_size="2em",
    )

# GIFT
def gift():
    return pc.center(pc.text("gift page"), padding_top="3%")
# LETTER
def letter():
    return pc.center(pc.text("letter page"), padding_top="3%")
# TIMELINE
def timeline():
    return pc.center(pc.text("timeline page"), padding_top="3%")

app = pc.App(state=State)
app.add_page(index)
app.add_page(gift)
app.add_page(letter)
app.add_page(timeline)
app.compile()

# HBD (home)