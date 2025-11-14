"""
Module Console - Giao diện console cho ứng dụng Tử Vi
Cung cấp menu và tương tác với người dùng
"""

import os
import sys
from datetime import datetime

# Add parent directory to path để import được các module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.analysis.la_so import LaSo
from src.core.am_lich import AmLich


class ConsoleUI:
    """Class quản lý giao diện console"""

    def __init__(self):
        """Khởi tạo console UI"""
        self.la_so = None

    def clear_screen(self):
        """Xóa màn hình console"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def hien_thi_banner(self):
        """Hiển thị banner chào mừng"""
        print("=" * 80)
        print(" " * 25 + "ỨNG DỤNG TỬ VI AN SAO")
        print(" " * 22 + "Phương pháp truyền thống Việt Nam")
        print("=" * 80)
        print()

    def hien_thi_menu_chinh(self):
        """Hiển thị menu chính"""
        print("\nMENU CHÍNH:")
        print("-" * 80)
        print("  1. Tạo lá số tử vi mới")
        print("  2. Hiển thị lá số hiện tại")
        print("  3. Phân tích cung Mệnh")
        print("  4. Xem thông tin các cung")
        print("  5. Chuyển đổi Âm Dương lịch")
        print("  6. Lưu lá số ra file")
        print("  0. Thoát")
        print("-" * 80)

    def nhap_thong_tin_sinh(self) -> dict:
        """
        Nhập thông tin ngày giờ sinh từ người dùng

        Returns:
            Dict chứa thông tin sinh
        """
        print("\nNHẬP THÔNG TIN NGÀY GIỜ SINH:")
        print("-" * 80)

        try:
            # Chọn loại lịch
            print("\nChọn loại lịch:")
            print("  1. Dương lịch")
            print("  2. Âm lịch")
            loai_lich = input("Lựa chọn (1/2): ").strip()

            if loai_lich == "2":
                # Nhập âm lịch
                ngay_am = int(input("Ngày sinh (âm lịch) [1-30]: "))
                thang_am = int(input("Tháng sinh (âm lịch) [1-12]: "))
                nam_am = int(input("Năm sinh (âm lịch): "))
                nhuan = input("Tháng nhuận không? (c/k) [k]: ").strip().lower() == 'c'

                # Chuyển sang dương lịch
                ngay_dl, thang_dl, nam_dl = AmLich.am_to_duong(
                    ngay_am, thang_am, nam_am, nhuan
                )
                print(f"\n→ Dương lịch tương ứng: {ngay_dl:02d}/{thang_dl:02d}/{nam_dl}")
            else:
                # Nhập dương lịch
                ngay_dl = int(input("Ngày sinh (dương lịch) [1-31]: "))
                thang_dl = int(input("Tháng sinh (dương lịch) [1-12]: "))
                nam_dl = int(input("Năm sinh (dương lịch): "))

            # Nhập giờ sinh
            print("\nGiờ sinh:")
            print("  Nhập giờ (0-23) hoặc nhấn Enter để dùng giờ hiện tại")
            gio_input = input("Giờ sinh: ").strip()
            if gio_input:
                gio = int(gio_input)
            else:
                gio = datetime.now().hour
                print(f"  → Sử dụng giờ hiện tại: {gio}h")

            # Giới tính
            gioi_tinh = input("\nGiới tính (Nam/Nữ) [Nam]: ").strip() or "Nam"

            return {
                "ngay": ngay_dl,
                "thang": thang_dl,
                "nam": nam_dl,
                "gio": gio,
                "gioi_tinh": gioi_tinh
            }

        except ValueError as e:
            print(f"\n❌ Lỗi: Dữ liệu nhập không hợp lệ! ({e})")
            return None
        except Exception as e:
            print(f"\n❌ Lỗi: {e}")
            return None

    def tao_la_so_moi(self):
        """Tạo lá số tử vi mới"""
        self.clear_screen()
        self.hien_thi_banner()

        thong_tin = self.nhap_thong_tin_sinh()
        if thong_tin:
            try:
                print("\n⏳ Đang tính toán lá số...")
                self.la_so = LaSo(
                    ngay_dl=thong_tin["ngay"],
                    thang_dl=thong_tin["thang"],
                    nam_dl=thong_tin["nam"],
                    gio=thong_tin["gio"],
                    gioi_tinh=thong_tin["gioi_tinh"]
                )
                print("✓ Tạo lá số thành công!")
                input("\nNhấn Enter để tiếp tục...")
            except Exception as e:
                print(f"\n❌ Lỗi khi tạo lá số: {e}")
                input("\nNhấn Enter để tiếp tục...")

    def hien_thi_la_so(self):
        """Hiển thị lá số đầy đủ"""
        if not self.la_so:
            print("\n❌ Chưa có lá số nào! Vui lòng tạo lá số trước.")
            input("\nNhấn Enter để tiếp tục...")
            return

        self.clear_screen()
        print(self.la_so.hien_thi_la_so_day_du())
        input("\nNhấn Enter để tiếp tục...")

    def phan_tich_cung_menh(self):
        """Phân tích cung Mệnh"""
        if not self.la_so:
            print("\n❌ Chưa có lá số nào! Vui lòng tạo lá số trước.")
            input("\nNhấn Enter để tiếp tục...")
            return

        self.clear_screen()
        print("=" * 80)
        print(" " * 28 + "PHÂN TÍCH CUNG MỆNH")
        print("=" * 80)

        phan_tich = self.la_so.phan_tich_cung_menh()

        print(f"\nVị trí Cung Mệnh: {phan_tich['vi_tri']}")
        print(f"\nSao chính trong Mệnh:")
        if phan_tich['sao_chinh']:
            for sao in phan_tich['sao_chinh']:
                print(f"  • {sao}")
        else:
            print("  (Không có)")

        print(f"\nSao phụ trong Mệnh:")
        if phan_tich['sao_phu']:
            for sao in phan_tich['sao_phu']:
                print(f"  • {sao}")
        else:
            print("  (Không có)")

        if phan_tich['tu_hoa']:
            print(f"\nTứ Hóa:")
            for hoa in phan_tich['tu_hoa']:
                print(f"  • {hoa}")

        print(f"\nNgũ hành Cung Mệnh: {phan_tich['ngu_hanh']['chu_hanh']}")
        print(f"\nĐánh giá: {phan_tich['danh_gia']}")

        input("\nNhấn Enter để tiếp tục...")

    def xem_thong_tin_cung(self):
        """Xem thông tin các cung"""
        if not self.la_so:
            print("\n❌ Chưa có lá số nào! Vui lòng tạo lá số trước.")
            input("\nNhấn Enter để tiếp tục...")
            return

        self.clear_screen()
        print("=" * 80)
        print(" " * 28 + "THÔNG TIN CÁC CUNG")
        print("=" * 80)

        cung_names = [
            "Mệnh", "Phụ Mẫu", "Phúc Đức", "Điền Trạch",
            "Quan Lộc", "Nô Bộc", "Thiên Di", "Tật Ách",
            "Tài Bạch", "Tử Tức", "Phu Thê", "Huynh Đệ"
        ]

        print("\nChọn cung cần xem:")
        for i, cung in enumerate(cung_names, 1):
            print(f"  {i:2d}. {cung}")

        try:
            chon = int(input("\nLựa chọn [1-12]: "))
            if 1 <= chon <= 12:
                ten_cung = cung_names[chon - 1]
                sao = self.la_so.lay_sao_trong_cung(ten_cung)

                print(f"\n{'=' * 80}")
                print(f"CUNG {ten_cung.upper()}")
                print(f"{'=' * 80}")

                print(f"\nSao chính:")
                if sao['chinh_dieu']:
                    for s in sao['chinh_dieu']:
                        print(f"  • {s}")
                else:
                    print("  (Không có)")

                print(f"\nSao phụ:")
                if sao['phu_dieu']:
                    for s in sao['phu_dieu']:
                        print(f"  • {s}")
                else:
                    print("  (Không có)")

                if sao['tu_hoa']:
                    print(f"\nTứ Hóa:")
                    for h in sao['tu_hoa']:
                        print(f"  • {h}")
            else:
                print("\n❌ Lựa chọn không hợp lệ!")

        except ValueError:
            print("\n❌ Vui lòng nhập số!")

        input("\nNhấn Enter để tiếp tục...")

    def chuyen_doi_lich(self):
        """Chuyển đổi Âm Dương lịch"""
        self.clear_screen()
        print("=" * 80)
        print(" " * 26 + "CHUYỂN ĐỔI ÂM DƯƠNG LỊCH")
        print("=" * 80)

        print("\nChọn hướng chuyển đổi:")
        print("  1. Dương lịch → Âm lịch")
        print("  2. Âm lịch → Dương lịch")

        try:
            chon = input("Lựa chọn (1/2): ").strip()

            if chon == "1":
                ngay = int(input("\nNgày (dương lịch) [1-31]: "))
                thang = int(input("Tháng (dương lịch) [1-12]: "))
                nam = int(input("Năm (dương lịch): "))

                ngay_am, thang_am, nam_am, nhuan = AmLich.duong_to_am(ngay, thang, nam)

                print(f"\n→ Kết quả:")
                print(f"  Dương lịch: {ngay:02d}/{thang:02d}/{nam}")
                print(f"  Âm lịch:    {ngay_am:02d}/{thang_am:02d}/{nam_am}" +
                     (" (nhuận)" if nhuan else ""))

            elif chon == "2":
                ngay_am = int(input("\nNgày (âm lịch) [1-30]: "))
                thang_am = int(input("Tháng (âm lịch) [1-12]: "))
                nam_am = int(input("Năm (âm lịch): "))
                nhuan = input("Tháng nhuận? (c/k) [k]: ").strip().lower() == 'c'

                ngay, thang, nam = AmLich.am_to_duong(ngay_am, thang_am, nam_am, nhuan)

                print(f"\n→ Kết quả:")
                print(f"  Âm lịch:    {ngay_am:02d}/{thang_am:02d}/{nam_am}" +
                     (" (nhuận)" if nhuan else ""))
                print(f"  Dương lịch: {ngay:02d}/{thang:02d}/{nam}")

        except Exception as e:
            print(f"\n❌ Lỗi: {e}")

        input("\nNhấn Enter để tiếp tục...")

    def luu_la_so(self):
        """Lưu lá số ra file"""
        if not self.la_so:
            print("\n❌ Chưa có lá số nào! Vui lòng tạo lá số trước.")
            input("\nNhấn Enter để tiếp tục...")
            return

        try:
            file_name = input("\nNhập tên file (mặc định: la_so.txt): ").strip()
            if not file_name:
                file_name = "la_so.txt"

            if not file_name.endswith('.txt'):
                file_name += '.txt'

            self.la_so.luu_la_so_txt(file_name)
            print(f"\n✓ Đã lưu lá số vào file: {file_name}")

        except Exception as e:
            print(f"\n❌ Lỗi khi lưu file: {e}")

        input("\nNhấn Enter để tiếp tục...")

    def chay(self):
        """Chạy ứng dụng console"""
        while True:
            self.clear_screen()
            self.hien_thi_banner()
            self.hien_thi_menu_chinh()

            lua_chon = input("\nLựa chọn của bạn: ").strip()

            if lua_chon == "1":
                self.tao_la_so_moi()
            elif lua_chon == "2":
                self.hien_thi_la_so()
            elif lua_chon == "3":
                self.phan_tich_cung_menh()
            elif lua_chon == "4":
                self.xem_thong_tin_cung()
            elif lua_chon == "5":
                self.chuyen_doi_lich()
            elif lua_chon == "6":
                self.luu_la_so()
            elif lua_chon == "0":
                print("\nCảm ơn bạn đã sử dụng ứng dụng! Hẹn gặp lại!")
                break
            else:
                print("\n❌ Lựa chọn không hợp lệ!")
                input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    app = ConsoleUI()
    app.chay()
