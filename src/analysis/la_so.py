"""
Module Lá Số - Class chính để tạo và phân tích lá số tử vi
Tổng hợp tất cả các thành phần: Can Chi, Cung, Sao, Ngũ hành
"""

from typing import Dict, List, Optional
from datetime import datetime

from ..core.am_lich import AmLich
from ..core.can_chi import CanChi, DIA_CHI, julian_day_number
from ..core.cung_menh import CungMenh
from ..core.ngu_hanh import NguHanh
from ..stars.an_sao import AnSao


class LaSo:
    """Class chính để tạo và quản lý lá số tử vi"""

    def __init__(self, ngay_dl: int, thang_dl: int, nam_dl: int,
                 gio: int, gioi_tinh: str = "Nam", time_zone: int = 7):
        """
        Khởi tạo lá số tử vi

        Args:
            ngay_dl: Ngày sinh dương lịch (1-31)
            thang_dl: Tháng sinh dương lịch (1-12)
            nam_dl: Năm sinh dương lịch
            gio: Giờ sinh (0-23)
            gioi_tinh: "Nam" hoặc "Nữ"
            time_zone: Múi giờ (mặc định 7 cho VN)
        """
        # Thông tin cơ bản
        self.ngay_duong = ngay_dl
        self.thang_duong = thang_dl
        self.nam_duong = nam_dl
        self.gio = gio
        self.gioi_tinh = gioi_tinh
        self.time_zone = time_zone

        # Chuyển sang âm lịch
        ngay_am, thang_am, nam_am, nhuan = AmLich.duong_to_am(
            ngay_dl, thang_dl, nam_dl, time_zone
        )
        self.ngay_am = ngay_am
        self.thang_am = thang_am
        self.nam_am = nam_am
        self.thang_nhuan = nhuan

        # Tính Can Chi
        jd = julian_day_number(ngay_dl, thang_dl, nam_dl)
        self.can_nam, self.chi_nam = CanChi.get_can_chi_nam(nam_dl)
        self.can_thang, self.chi_thang = CanChi.get_can_chi_thang(nam_dl, thang_dl)
        self.can_ngay, self.chi_ngay = CanChi.get_can_chi_ngay(jd)
        self.chi_gio = CanChi.get_gio_dia_chi(gio)
        self.can_gio, _ = CanChi.get_can_chi_gio(gio, self.can_ngay)

        # Index giờ sinh
        self.gio_sinh_index = DIA_CHI.index(self.chi_gio)

        # Tính Ngũ hành
        self.ngu_hanh_menh = NguHanh.get_ngu_hanh_can(self.can_nam)

        # Xây dựng 12 cung
        self.cung_map = CungMenh.xay_dung_12_cung(self.thang_am, self.chi_gio)
        self.cung_menh_index = CungMenh.lay_vi_tri_cung(self.cung_map, "Mệnh")
        self.cung_than_index = CungMenh.lay_vi_tri_cung(self.cung_map, "Thân")

        # An sao
        self.sao_data = AnSao.an_toan_bo_sao(
            self.ngay_am, self.thang_am, self.nam_am, self.gio_sinh_index
        )

    def lay_thong_tin_co_ban(self) -> Dict[str, any]:
        """
        Lấy thông tin cơ bản của lá số

        Returns:
            Dict chứa thông tin
        """
        return {
            "duong_lich": f"{self.ngay_duong:02d}/{self.thang_duong:02d}/{self.nam_duong}",
            "am_lich": f"{self.ngay_am:02d}/{self.thang_am:02d}/{self.nam_am}" +
                      (" (nhuận)" if self.thang_nhuan else ""),
            "gio_sinh": f"{self.gio:02d}:00 ({self.chi_gio})",
            "gioi_tinh": self.gioi_tinh,
            "can_chi_nam": f"{self.can_nam} {self.chi_nam}",
            "can_chi_thang": f"{self.can_thang} {self.chi_thang}",
            "can_chi_ngay": f"{self.can_ngay} {self.chi_ngay}",
            "can_chi_gio": f"{self.can_gio} {self.chi_gio}",
            "ngu_hanh_menh": self.ngu_hanh_menh,
            "cung_menh": f"{DIA_CHI[self.cung_menh_index]} ({self.cung_menh_index + 1})",
            "cung_than": f"{DIA_CHI[self.cung_than_index]} ({self.cung_than_index + 1})"
        }

    def lay_sao_trong_cung(self, ten_cung: str) -> Dict[str, List[str]]:
        """
        Lấy các sao trong một cung cụ thể

        Args:
            ten_cung: Tên cung

        Returns:
            Dict chứa các sao trong cung
        """
        vi_tri_cung = CungMenh.lay_vi_tri_cung(self.cung_map, ten_cung)
        if vi_tri_cung == -1:
            return {"chinh_dieu": [], "phu_dieu": [], "tu_hoa": []}

        return AnSao.lay_sao_tai_cung(self.sao_data, vi_tri_cung)

    def hien_thi_la_so_day_du(self) -> str:
        """
        Hiển thị lá số đầy đủ dạng text

        Returns:
            String hiển thị lá số
        """
        lines = []
        lines.append("=" * 80)
        lines.append(" " * 30 + "LÁ SỐ TỬ VI")
        lines.append("=" * 80)

        # Thông tin cơ bản
        info = self.lay_thong_tin_co_ban()
        lines.append("\nTHÔNG TIN CƠ BẢN:")
        lines.append("-" * 80)
        lines.append(f"  Dương lịch: {info['duong_lich']:20s} Giới tính: {info['gioi_tinh']}")
        lines.append(f"  Âm lịch:    {info['am_lich']:20s} Giờ sinh:  {info['gio_sinh']}")
        lines.append(f"\n  Tứ trụ (4 cột mốc thời gian):")
        lines.append(f"    Năm:  {info['can_chi_nam']}")
        lines.append(f"    Tháng: {info['can_chi_thang']}")
        lines.append(f"    Ngày: {info['can_chi_ngay']}")
        lines.append(f"    Giờ:  {info['can_chi_gio']}")
        lines.append(f"\n  Ngũ hành mệnh: {info['ngu_hanh_menh']}")
        lines.append(f"  Cung Mệnh: {info['cung_menh']}")
        lines.append(f"  Cung Thân:  {info['cung_than']}")

        # Hiển thị 12 cung với các sao
        lines.append("\n12 CUNG VÀ CÁC SAO:")
        lines.append("=" * 80)

        for i in range(12):
            chi = DIA_CHI[i]
            cung_name = self.cung_map.get(i, "")
            sao_trong_cung = AnSao.lay_sao_tai_cung(self.sao_data, i)

            # Header cung
            lines.append(f"\n{chi:5s} (Cung {i+1:2d}) - {cung_name:12s}")
            lines.append("-" * 80)

            # Sao chính
            if sao_trong_cung["chinh_dieu"]:
                lines.append(f"  Sao chính: {', '.join(sao_trong_cung['chinh_dieu'])}")

            # Sao phụ
            if sao_trong_cung["phu_dieu"]:
                lines.append(f"  Sao phụ:   {', '.join(sao_trong_cung['phu_dieu'])}")

            # Tứ hóa
            if sao_trong_cung["tu_hoa"]:
                lines.append(f"  Tứ hóa:    {', '.join(sao_trong_cung['tu_hoa'])}")

            # Nếu không có sao nào
            if (not sao_trong_cung["chinh_dieu"] and
                not sao_trong_cung["phu_dieu"] and
                not sao_trong_cung["tu_hoa"]):
                lines.append("  (Không có sao)")

        lines.append("\n" + "=" * 80)

        return "\n".join(lines)

    def phan_tich_cung_menh(self) -> Dict[str, any]:
        """
        Phân tích cung Mệnh chi tiết

        Returns:
            Dict chứa phân tích
        """
        sao_menh = self.lay_sao_trong_cung("Mệnh")

        # Phân tích ngũ hành
        can_menh = CanChi.THIEN_CAN[(self.cung_menh_index + (self.nam_duong - 4)) % 10]
        chi_menh = DIA_CHI[self.cung_menh_index]
        ngu_hanh_info = NguHanh.phan_tich_ngu_hanh(can_menh, chi_menh)

        return {
            "vi_tri": f"{DIA_CHI[self.cung_menh_index]} (Cung {self.cung_menh_index + 1})",
            "sao_chinh": sao_menh["chinh_dieu"],
            "sao_phu": sao_menh["phu_dieu"],
            "tu_hoa": sao_menh["tu_hoa"],
            "ngu_hanh": ngu_hanh_info,
            "danh_gia": self._danh_gia_cung_menh(sao_menh)
        }

    def _danh_gia_cung_menh(self, sao_menh: Dict[str, List[str]]) -> str:
        """
        Đánh giá sơ bộ cung Mệnh

        Args:
            sao_menh: Các sao trong cung Mệnh

        Returns:
            Chuỗi đánh giá
        """
        sao_tot = ["Tử Vi", "Thiên Phủ", "Thái Dương", "Thái Âm", "Thiên Đồng"]
        sao_xau = ["Thất Sát", "Phá Quân", "Hóa Kỵ"]

        co_sao_tot = any(s in sao_menh["chinh_dieu"] for s in sao_tot)
        co_sao_xau = any(s in sao_menh["chinh_dieu"] or
                        "Hóa Kỵ" in str(sao_menh["tu_hoa"]) for s in sao_xau)

        if co_sao_tot and not co_sao_xau:
            return "Tốt - Cung Mệnh có sao tốt, vận mệnh hanh thông"
        elif co_sao_xau and not co_sao_tot:
            return "Khó - Cung Mệnh gặp sao xấu, cần cẩn trọng"
        elif co_sao_tot and co_sao_xau:
            return "Trung bình - Có cả sao tốt và xấu, vận có lên xuống"
        else:
            return "Bình thường - Không có sao đặc biệt nổi bật"

    def luu_la_so_txt(self, file_path: str):
        """
        Lưu lá số ra file text

        Args:
            file_path: Đường dẫn file
        """
        content = self.hien_thi_la_so_day_du()
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def to_dict(self) -> Dict[str, any]:
        """
        Chuyển lá số thành dict để lưu trữ hoặc export

        Returns:
            Dict chứa toàn bộ thông tin lá số
        """
        return {
            "thong_tin_co_ban": self.lay_thong_tin_co_ban(),
            "cung_map": self.cung_map,
            "sao_data": self.sao_data,
            "cung_menh_index": self.cung_menh_index,
            "cung_than_index": self.cung_than_index
        }


if __name__ == "__main__":
    # Test module
    print("=== Test Module Lá Số ===\n")

    # Tạo lá số mẫu
    la_so = LaSo(
        ngay_dl=15,
        thang_dl=5,
        nam_dl=1990,
        gio=14,
        gioi_tinh="Nam"
    )

    # Hiển thị lá số đầy đủ
    print(la_so.hien_thi_la_so_day_du())

    # Phân tích cung Mệnh
    print("\n\nPHÂN TÍCH CUNG MỆNH:")
    print("=" * 80)
    phan_tich = la_so.phan_tich_cung_menh()
    print(f"Vị trí: {phan_tich['vi_tri']}")
    print(f"Sao chính: {', '.join(phan_tich['sao_chinh']) if phan_tich['sao_chinh'] else 'Không có'}")
    print(f"Sao phụ: {', '.join(phan_tich['sao_phu']) if phan_tich['sao_phu'] else 'Không có'}")
    print(f"Đánh giá: {phan_tich['danh_gia']}")
