import traceback
from ui.MainWinDowFAHASAUI import Ui_mainWindow
from utils.tinhtien import tinh_tong_tien_sinhvien, tinh_tong_tien_khac


class MainWindowFAHASAUIExt(Ui_mainWindow):
    so_kh_sv=0
    so_kh_khac=0

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlots()
    def show(self):
        self.MainWindow.show()

    def setupSignalAndSlots(self):
        self.pushButton.clicked.connect(self.process_mua)
        self.pushButton_2.clicked.connect(self.process_tiep)
        self.pushButton_3.clicked.connect(self.MainWindow.close) #có thể dùng trực tiếp SignalAndSlots trong QtDesigner
    def process_mua(self):
        try:
            soluong=int(self.soluongmua.text())
            loaikh="SV"
            if self.lasinhvien.isChecked():
                self.so_kh_sv+=soluong
            if self.khongphailasinhvien.isChecked():
                loaikh="KH_KHAC"
                self.so_kh_khac+=soluong
            tien_sv = round(tinh_tong_tien_sinhvien(self.so_kh_sv),2)
            tien_khac = round(tinh_tong_tien_khac(self.so_kh_khac),2)

            self.sokhsinhvien.setText(str(self.so_kh_sv)) #vì số kh sinh viên định dạng ban đầu là số nên phảo có str (string) để đổi số thành chuỗi
            self.tienkhsinhvien.setText(str(tien_sv))
            self.sokhkhac.setText(str(self.so_kh_khac))
            self.tienkhkhac.setText(str(tien_khac))
            self.tongsoluong.setText(f"{self.so_kh_sv+self.so_kh_khac}")
            self.tongtien.setText(f"{tien_sv+tien_khac}")
        except:
            traceback.print_exc()
            self.label_12.setText("NHẬP SỐ! NHẬP SỐ! NHẬP SỐ!")
            self.soluongmua.selectAll()
            self.soluongmua.setFocus()
    def process_tiep(self):
        self.soluongmua.setText("")
        self.soluongmua.setFocus()