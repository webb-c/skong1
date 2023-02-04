from pcconfig import config
import pynecone as pc
from pynecone.base import Base

class Letter(Base):
    text: str
    date: str
class State(pc.State):
    #letter state
    msg: list[Letter] = []
    IsOpen = False
    buttonText = "Open"
    text = "test"
    def reading(self):
        if self.IsOpen :
            self.IsOpen = False
            self.buttonText = "Open"
            self.msg = []
        else :
            self.IsOpen = True
            self.buttonText = "Close"
            self.msg = [Letter(text=self.text, date="February 05, 2023 11:29 PM")]

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

def message(message):
    return pc.box(
        pc.vstack(
            pc.box(
                pc.text(message.text),
                font_size = "1.2rem",
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
        width="80%",
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
            ),
            pc.text(
                "About allo1001PD",
                as_="i",
                font_size="1.5em",
            ),
            pc.image(src="/data/243953504.jpg", width="25em"),
            pc.text("상세 정보", font_size="1.3em", as_="b"),
            pc.vstack(
                pc.box(
                    pc.markdown(
                        """
                        - 모델명 : allo1001PD
                        - 전지 종류 : 리튬폴리머 2차 전지
                        - 정격 용량 :
                            - 3.7VDC
                            - 10000mAh
                            - 37Wh
                        - 사이즈 : 145 X 68 X 16 mm
                        - 무게 : 225g
                        """
                    ),
                    width = "100%"
                ),
                pc.text("지원 기능", font_size="1.3em", as_="b"),
                pc.box(
                    pc.markdown(
                        """
                        - 3개의 출력 포트를 사용한 최대 3개의 기기 동시 충전 지원
                        - QC3.0/PD3.0 고속 충전 지원 (고속 충전시 LED 색상 변화)
                        - 과충전 방지 및 안정성 테스트 완료
                        """
                    ),
                    width="100%"
                ),
                spacing="20px"
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