from scanner.capture import TradeZeroCapture
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QTableWidget,
    QTableWidgetItem,
    QStatusBar,
    QHeaderView,
    QFrame
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def check_tradezero(self):

        if self.capture.find_tradezero():

            self.tradezero_status.setText(
                f"🟢 {self.capture.get_title()}"
            )

        else:

            self.tradezero_status.setText(
                "🔴 TradeZero : Not Connected"
            )

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ScannerApp Pro v2")
        self.resize(1300, 800)

        self.setup_ui()
        self.capture = TradeZeroCapture()

        self.timer = QTimer()

        self.timer.timeout.connect(self.check_tradezero)

        self.timer.start(1000)
        
    def setup_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)

        ###################################
        # LEFT PANEL
        ###################################

        left = QVBoxLayout()

        self.tradezero_status = QLabel("🔴 TradeZero : Not Connected")
        self.tradezero_status.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
            color:#ff5555;
            padding:10px;
        """)

        left.addWidget(self.tradezero_status)

        self.btn_add = QPushButton("Add Scanner")
        self.btn_remove = QPushButton("Remove Scanner")
        self.btn_edit = QPushButton("Edit Layout")
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")

        buttons = [
            self.btn_add,
            self.btn_remove,
            self.btn_edit,
            self.btn_start,
            self.btn_stop
        ]

        for b in buttons:
            b.setMinimumHeight(40)
            left.addWidget(b)

        left.addSpacing(15)

        lbl = QLabel("Scanners")
        lbl.setStyleSheet("font-size:16px;font-weight:bold;")
        left.addWidget(lbl)

        self.scanner_list = QListWidget()
        left.addWidget(self.scanner_list)

        left.setStretchFactor(self.scanner_list, 1)

        ###################################
        # RIGHT PANEL
        ###################################

        right = QVBoxLayout()

        title = QLabel("Live Scanner Results")
        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            padding:5px;
        """)

        right.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Ticker",
            "Pops",
            "Latest Time",
            "Scanner"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.table.verticalHeader().hide()

        right.addWidget(self.table)

        ###################################
        # LAYOUT
        ###################################

        left_frame = QFrame()
        left_frame.setLayout(left)
        left_frame.setMaximumWidth(300)

        root.addWidget(left_frame)
        root.addLayout(right)

        ###################################
        # STATUS BAR
        ###################################

        self.status = QStatusBar()

        self.status.showMessage("Ready")

        self.setStatusBar(self.status)

        ###################################
        # DARK THEME
        ###################################

        self.setStyleSheet("""

        QMainWindow{
            background:#202124;
        }

        QWidget{
            background:#202124;
            color:white;
            font-size:13px;
        }

        QPushButton{

            background:#2d89ef;
            border:none;
            border-radius:6px;
            padding:8px;

        }

        QPushButton:hover{

            background:#3b97ff;

        }

        QListWidget{

            background:#2c2c2c;
            border:1px solid #444;

        }

        QTableWidget{

            background:#2c2c2c;
            gridline-color:#444;

        }

        QHeaderView::section{

            background:#1e1e1e;
            padding:8px;
            border:1px solid #444;

        }

        QStatusBar{

            background:#181818;

        }

        """)