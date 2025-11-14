"""
Module Chính Diệu - 14 Sao chính trong Tử Vi
Bao gồm: Bắc Đẩu, Nam Đẩu, Trung Thiên các sao
"""

from typing import Dict, List, Tuple


# 14 Sao Chính Diệu
CHINH_DIEU = [
    "Tử Vi",      # Sao Đế vương
    "Thiên Cơ",   # Sao Trí tuệ
    "Thái Dương",  # Sao Ánh sáng
    "Vũ Khúc",    # Sao Tài lộc
    "Thiên Đồng", # Sao Phúc đức
    "Liêm Trinh", # Sao Công danh
    "Thiên Phủ",  # Sao Tài chính
    "Thái Âm",    # Sao Nữ tính
    "Tham Lang",  # Sao Ham muốn
    "Cú Môn",     # Sao Tranh tụng
    "Thiên Tướng", # Sao Hỗ trợ
    "Thiên Lương", # Sao Y dược
    "Thất Sát",   # Sao Quyền lực
    "Phá Quân"    # Sao Biến động
]

# Phân loại sao
NHOM_SAO = {
    "Bắc Đẩu": ["Tham Lang", "Cự Môn", "Lộc Tồn", "Văn Khúc", "Liêm Trinh", "Vũ Khúc", "Phá Quân"],
    "Nam Đẩu": ["Thiên Phủ", "Thiên Tướng", "Thiên Lương", "Thiên Đồng", "Thất Sát", "Thiên Cơ"],
    "Trung Thiên": ["Tử Vi", "Thái Dương", "Thái Âm"]
}

# Thuộc tính ngũ hành của các sao
SAO_NGU_HANH = {
    "Tử Vi": "Thổ",
    "Thiên Cơ": "Mộc",
    "Thái Dương": "Hỏa",
    "Vũ Khúc": "Kim",
    "Thiên Đồng": "Thủy",
    "Liêm Trinh": "Hỏa",
    "Thiên Phủ": "Thổ",
    "Thái Âm": "Thủy",
    "Tham Lang": "Thủy/Mộc",
    "Cự Môn": "Thủy",
    "Thiên Tướng": "Thủy",
    "Thiên Lương": "Thổ",
    "Thất Sát": "Kim",
    "Phá Quân": "Thủy"
}

# Âm dương của sao
SAO_AM_DUONG = {
    "Tử Vi": "Dương",
    "Thiên Cơ": "Dương",
    "Thái Dương": "Dương",
    "Vũ Khúc": "Âm",
    "Thiên Đồng": "Dương",
    "Liêm Trinh": "Âm",
    "Thiên Phủ": "Dương",
    "Thái Âm": "Âm",
    "Tham Lang": "Dương",
    "Cự Môn": "Âm",
    "Thiên Tướng": "Dương",
    "Thiên Lương": "Dương",
    "Thất Sát": "Âm",
    "Phá Quân": "Âm"
}

# Ý nghĩa cơ bản của sao
SAO_Y_NGHIA = {
    "Tử Vi": "Đế vương, quyền quý, địa vị cao, tự tin, lãnh đạo",
    "Thiên Cơ": "Trí tuệ, mưu lược, nhanh nhạy, đa mưu, thông minh",
    "Thái Dương": "Ánh sáng, nam tính, danh tiếng, quang minh chính đại",
    "Vũ Khúc": "Tài chính, kim khí, cương trực, quyết đoán",
    "Thiên Đồng": "Phúc đức, an nhàn, hưởng thụ, hiền hòa",
    "Liêm Trinh": "Công danh, văn chương, lễ nghĩa, thanh cao",
    "Thiên Phủ": "Tài lộc, giàu có, bao dung, hậu đậm",
    "Thái Âm": "Nữ tính, thanh tú, tinh tế, nội tâm",
    "Tham Lang": "Ham muốn, tham vọng, đa tài, giao thiếp",
    "Cự Môn": "Tranh tụng, khẩu thiệt, nghi ngờ, cẩn thận",
    "Thiên Tướng": "Hỗ trợ, phụ tá, trung thành, có tổ chức",
    "Thiên Lương": "Y dược, giải ách, cao niên, đạo đức",
    "Thất Sát": "Quyền uy, cô độc, dũng mãnh, mạo hiểm",
    "Phá Quân": "Biến động, phá cách, cải cách, không ổn định"
}


class ChinhDieu:
    """Class xử lý các sao chính diệu"""

    @staticmethod
    def tinh_tu_vi(ngay_am: int, thang_am: int, gio_sinh_index: int) -> int:
        """
        Tính vị trí sao Tử Vi

        Công thức: Tử Vi = (Số cục + Ngày sinh) % 12
        Số cục phụ thuộc vào tháng sinh và giờ sinh

        Args:
            ngay_am: Ngày âm lịch (1-30)
            thang_am: Tháng âm lịch (1-12)
            gio_sinh_index: Index giờ sinh (0-11)

        Returns:
            Index vị trí sao Tử Vi (0-11)
        """
        # Bảng số cục theo tháng sinh (1-12) và giờ sinh
        # Đơn giản hóa: Số cục từ 2 đến 5
        so_cuc_map = {
            1: 5, 2: 5, 3: 2, 4: 2, 5: 5, 6: 5,
            7: 2, 8: 2, 9: 5, 10: 5, 11: 2, 12: 2
        }

        so_cuc = so_cuc_map.get(thang_am, 5)

        # Tính Tử Vi
        vi_tri = (so_cuc + ngay_am - 1) % 12

        return vi_tri

    @staticmethod
    def an_tu_vi_he(ngay_am: int, thang_am: int, gio_sinh_index: int) -> Dict[str, int]:
        """
        An sao Tử Vi và các sao trong hệ Tử Vi
        Hệ Tử Vi: Tử Vi, Thiên Cơ, Thái Dương, Vũ Khúc, Thiên Đồng, Liêm Trinh

        Args:
            ngay_am: Ngày âm lịch
            thang_am: Tháng âm lịch
            gio_sinh_index: Index giờ sinh

        Returns:
            Dict với key là tên sao, value là vị trí (0-11)
        """
        result = {}

        # An Tử Vi
        tu_vi_pos = ChinhDieu.tinh_tu_vi(ngay_am, thang_am, gio_sinh_index)
        result["Tử Vi"] = tu_vi_pos

        # An các sao khác trong hệ (theo thứ tự thuận)
        result["Thiên Cơ"] = (tu_vi_pos + 1) % 12
        result["Thái Dương"] = (tu_vi_pos + 2) % 12
        result["Vũ Khúc"] = (tu_vi_pos + 3) % 12
        result["Thiên Đồng"] = (tu_vi_pos + 4) % 12
        result["Liêm Trinh"] = (tu_vi_pos + 5) % 12

        return result

    @staticmethod
    def an_thien_phu_he(thang_am: int, gio_sinh_index: int) -> Dict[str, int]:
        """
        An sao Thiên Phủ và các sao trong hệ Thiên Phủ
        Hệ Thiên Phủ: Thiên Phủ, Thái Âm, Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân

        Args:
            thang_am: Tháng âm lịch
            gio_sinh_index: Index giờ sinh

        Returns:
            Dict với key là tên sao, value là vị trí
        """
        result = {}

        # An Thiên Phủ (dựa vào tháng sinh)
        # Tháng 1 (Giêng) tại Tý, đếm thuận
        thien_phu_pos = (thang_am - 1) % 12
        result["Thiên Phủ"] = thien_phu_pos

        # An các sao khác (thuận/nghịch tùy theo quy luật)
        result["Thái Âm"] = (thien_phu_pos + 1) % 12
        result["Tham Lang"] = (thien_phu_pos + 2) % 12
        result["Cự Môn"] = (thien_phu_pos + 3) % 12
        result["Thiên Tướng"] = (thien_phu_pos + 4) % 12
        result["Thiên Lương"] = (thien_phu_pos + 5) % 12
        result["Thất Sát"] = (thien_phu_pos + 6) % 12
        result["Phá Quân"] = (thien_phu_pos + 8) % 12  # Cách 2 cung

        return result

    @staticmethod
    def an_14_chinh_sao(ngay_am: int, thang_am: int, gio_sinh_index: int) -> Dict[str, int]:
        """
        An toàn bộ 14 sao chính diệu

        Args:
            ngay_am: Ngày âm lịch
            thang_am: Tháng âm lịch
            gio_sinh_index: Index giờ sinh

        Returns:
            Dict với key là tên sao, value là vị trí
        """
        result = {}

        # An hệ Tử Vi
        tu_vi_he = ChinhDieu.an_tu_vi_he(ngay_am, thang_am, gio_sinh_index)
        result.update(tu_vi_he)

        # An hệ Thiên Phủ
        thien_phu_he = ChinhDieu.an_thien_phu_he(thang_am, gio_sinh_index)
        result.update(thien_phu_he)

        return result

    @staticmethod
    def lay_thong_tin_sao(ten_sao: str) -> Dict[str, str]:
        """
        Lấy thông tin chi tiết của sao

        Args:
            ten_sao: Tên sao

        Returns:
            Dict chứa thông tin sao
        """
        # Xác định nhóm sao
        nhom = ""
        for key, value in NHOM_SAO.items():
            if ten_sao in value:
                nhom = key
                break

        if not nhom:
            if ten_sao in NHOM_SAO["Trung Thiên"]:
                nhom = "Trung Thiên"

        return {
            "ten": ten_sao,
            "nhom": nhom,
            "ngu_hanh": SAO_NGU_HANH.get(ten_sao, ""),
            "am_duong": SAO_AM_DUONG.get(ten_sao, ""),
            "y_nghia": SAO_Y_NGHIA.get(ten_sao, "")
        }

    @staticmethod
    def hien_thi_sao_trong_cung(sao_map: Dict[str, int], chi_index: int) -> List[str]:
        """
        Hiển thị các sao ở một cung cụ thể

        Args:
            sao_map: Dict mapping tên sao -> vị trí
            chi_index: Index của cung (0-11)

        Returns:
            List tên các sao trong cung
        """
        result = []
        for ten_sao, vi_tri in sao_map.items():
            if vi_tri == chi_index:
                result.append(ten_sao)
        return result

    @staticmethod
    def phan_tich_tuong_tac_sao(sao_1: str, sao_2: str) -> str:
        """
        Phân tích tương tác khi 2 sao đồng cung

        Args:
            sao_1: Tên sao thứ nhất
            sao_2: Tên sao thứ hai

        Returns:
            Mô tả tương tác
        """
        # Một số cặp sao tốt
        cap_tot = [
            ("Tử Vi", "Thiên Phủ"),
            ("Tử Vi", "Thiên Tướng"),
            ("Thiên Cơ", "Thái Âm"),
            ("Thiên Lương", "Thái Dương"),
        ]

        # Cặp sao xấu
        cap_xau = [
            ("Liêm Trinh", "Thất Sát"),
            ("Cự Môn", "Thái Dương"),
            ("Phá Quân", "Tham Lang"),
        ]

        cap = (sao_1, sao_2)
        cap_nguoc = (sao_2, sao_1)

        if cap in cap_tot or cap_nguoc in cap_tot:
            return "Tốt - Hai sao tương sinh, hỗ trợ lẫn nhau"
        elif cap in cap_xau or cap_nguoc in cap_xau:
            return "Xấu - Hai sao xung khắc, gây bất lợi"
        else:
            return "Trung bình - Hai sao có tác động bình thường"


if __name__ == "__main__":
    # Test module
    print("=== Test Module Chính Diệu ===\n")

    # Test an sao
    ngay = 15
    thang = 4
    gio_idx = 6  # Ngọ

    print(f"Ngày {ngay}/{thang} âm, giờ {gio_idx}\n")

    # An 14 sao chính
    sao_map = ChinhDieu.an_14_chinh_sao(ngay, thang, gio_idx)
    print("14 Sao Chính Diệu:")
    for sao, vi_tri in sorted(sao_map.items(), key=lambda x: x[1]):
        from ..core.can_chi import DIA_CHI
        print(f"  {sao:15s} -> {DIA_CHI[vi_tri]}")

    # Test thông tin sao
    print("\nThông tin sao Tử Vi:")
    info = ChinhDieu.lay_thong_tin_sao("Tử Vi")
    for key, value in info.items():
        print(f"  {key}: {value}")

    # Test hiển thị sao trong cung
    print(f"\nCác sao tại cung Tý:")
    sao_tai_cung = ChinhDieu.hien_thi_sao_trong_cung(sao_map, 0)
    print(f"  {', '.join(sao_tai_cung) if sao_tai_cung else '(Không có sao)'}")
