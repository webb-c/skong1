import TLdetail
import pynecone as pc
from pynecone.base import Base
from datetime import datetime, timedelta

# for time
pre = datetime(2015, 3, 2)
now = datetime.now()
class Letter(Base):
    text: list[str]
    date: str

class State(pc.State):
    #letter state
    msg: list[Letter] = []
    IsOpen = False
    buttonText = "Open"
    text = TLdetail.letter22
    def reading(self):
        if self.IsOpen :
            self.IsOpen = False
            self.buttonText = "Open"
            self.msg = []
        else :
            self.IsOpen = True
            self.buttonText = "Close"
            self.msg = [Letter(text=self.text.split("\n"), date="February 05, 2023 11:29 PM")]

    #timeline state
    value: int = 0
    # default_value: int = 100
    value_date: str = "2015. 03. 02"
    gap = (now-pre).days
    time: list[TLdetail.Time] = TLdetail.time

    def set_val(self, value):
        self.value = value
    @pc.var
    def set_time(self):
        dt = pre + timedelta(days=self.value * self.gap // 100)
        return str(dt.year)+". "+str(dt.month)+". "+str(dt.day)

def topBar():
    return pc.hstack(
                pc.link(pc.text("HBD"), href="http://localhost:3000/"),
                pc.link(pc.text("GIFT"), href="http://localhost:3000/gift"),
                pc.link(pc.text("LETTER"), href="http://localhost:3000/letter"),
                pc.link(pc.text("TIMELINE"), href="http://localhost:3000/timeline"),
                spacing="120px",
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
        spacing="50px",
        padding_top = "5%",
        padding_bottom="5%",
    )

def timetransfer(time):
    return pc.accordion(
            pc.accordion_item(
                pc.accordion_button(
                    pc.text(time.cls, font_size="1.1em", as_="b"),
                    pc.accordion_icon(),
                ),
                pc.accordion_panel(
                    pc.vstack(
                        pc.text(time.detail),
                        pc.image(src=time.pic, width="15em")
                    )
                ),
            )
    )
def message(message):
    return pc.box(
        pc.vstack(
            pc.box(
                element="iframe",
                src="https://www.youtube.com/embed/BRs0GGCT4bU?autoplay=1&mute=0",
                width="50em",
            ),
            pc.box(
                pc.foreach(message.text, pc.text),
                font_size = "1.1rem",
                bg = "#FFFFFF",
                padding = "1rem",
                border_radius = "3px",
                width = "100%"
            ),
            pc.box(
                pc.text(message.date),
                display="flex",
                font_size="0.8rem",
                color="#666"
            ),
            spacing="1rem",
        ),
        bg="#f0f8ff",
        width="100%",
        padding="1.5rem",
        border_radius="5px",
    )

# HBD (home)
def index():
    return pc.center(
        pc.vstack(
            topBar(),
            pc.heading(
                "Happy Birthday!",
                font_size="2em"
            ),
            pc.image(src="/data/cake.png", width="27em"),
            pc.vstack(
                pc.text("??? ???????????? ???????????? 22?????? ????????? ???????????? ????????? ????????? ??? ????????? ?????????.", font_size="1.1em"),
                pc.text("????????? ????????? ????????? ?????? ????????? ????????? ????????? ?????? ?????? ????????? ???????????? ????????????", font_size="1.1em"),
                pc.text("?????? ???????????? ???????????? ??? ????????? ??????????????? ????????????.", font_size="1.1em"),
                spacing="5px",
            ),
            pc.box(padding_top="3%"),
            pc.image(src="/data/arrow.png", width="5em"),
            pc.box(padding_top="3%"),
            pc.text(
                "????????? ??????",
                as_="i",
                font_size="1.3em",
            ),
            pc.box(padding_top="3%"),
            TLdetail.gallery(), # ???????????? ?????? ??????
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
            ),
            pc.text(
                "About allo1001PD",
                as_="i",
                font_size="1.5em",
            ),
            pc.image(src="/data/243953504.jpg", width="25em"),
            pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(
                        pc.text("?????? ??????", font_size="1.3em", as_="b"),
                        pc.accordion_icon(),
                    ),
                    pc.accordion_panel(
                        pc.markdown(
                            """
                            - ????????? : allo1001PD
                            - ?????? ?????? : ??????????????? 2??? ??????
                            - ?????? ?????? :
                                - 3.7VDC
                                - 10000mAh
                                - 37Wh
                            - ????????? : 145 X 68 X 16 mm
                            - ?????? : 225g
                            """
                        ),
                    ),
                ),
                width="100%"
            ),
            pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(
                        pc.text("?????? ??????", font_size="1.3em", as_="b"),
                        pc.accordion_icon(),
                    ),
                    pc.accordion_panel(
                        pc.markdown(
                            """
                            - 3?????? ?????? ????????? ????????? ?????? 3?????? ?????? ?????? ?????? ??????
                            - QC3.0/PD3.0 ?????? ?????? ?????? (?????? ????????? LED ?????? ??????)
                            - ????????? ?????? ??? ????????? ????????? ??????
                            """
                        ),
                    ),
                ),
                width="100%"
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
            ),
            pc.image(src="/data/letter4.gif", width="23em"),
            pc.foreach(State.msg, message),
            pc.box(),
            pc.button(
                State.buttonText,
                bg="rgb(51 128 255)",
                color="white",
                size="lg",
                on_click=State.reading,
            ),
            bottom(),
            spacing="15px"
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
            pc.text(
                "Our history",
                as_="i",
                font_size="1.1em",
            ),
            pc.box(),
            pc.heading(State.set_time, font_size="1.2em", color="rgb(60 135 240)"),
            pc.container(
                pc.slider(default_value=0, on_change=State.set_value),
                bg="#f0f8ff",
                center_content=True,
                border_radius="0.5em",
                padding="0.8em"
            ),
            pc.box(),
            pc.hstack(
                pc.foreach(State.time, timetransfer),
                spacing="10px",
                align_items="left"
            ),
            bottom(),
            spacing="20px"
        ),
        padding_top="3%",
    )

app = pc.App(state=State)
app.add_page(index, title="HBD App", image="/favicon.ico")
app.add_page(gift, title="Gift", image="/favicon.ico")
app.add_page(letter, title="Letter", image="/favicon.ico")
app.add_page(timeline, title="Timeline", image="/favicon.ico")
app.compile()