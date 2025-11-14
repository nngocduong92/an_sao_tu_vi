"""
Module Cung Mệnh - Tính toán 12 cung trong lá số tử vi
Bao gồm: Mệnh, Phụ Mẫu, Phúc Đức, Điền Trạch, Quan Lộc, Nô Bộc,
         Thiên Di, Tật Ách, Tài Bạch, Tử Tức, Phu Thê, Huynh Đệ
"""

from typing import Dict, List, Tuple
from .can_chi import DIA_CHI


# Danh sách 12 cung theo thứ tự
CUNG_NAMES = [
    "Mệnh",      # 0
    "Phụ Mẫu",   # 1
    "Phúc Đức",  # 2
    "Điền Trạch", # 3
    "Quan Lộc",  # 4
    "Nô Bộc",    # 5
    "Thiên Di",  # 6
    "Tật Ách",   # 7
    "Tài Bạch",  # 8
    "Tử Tức",    # 9
    "Phu Thê",   # 10
    "Huynh Đệ"   # 11
]

# Mô tả ý nghĩa từng cung
CUNG_DESCRIPTIONS = {
    "Mệnh": "Cung chính, thể hiện tính cách, vận mệnh chung",
    "Phụ Mẫu": "Quan hệ với cha mẹ, phúc đức tổ tiên",
    "Phúc Đức": "Tinh thần, tâm trí, hưởng thụ",
    "Điền Trạch": "Tài sản, nhà cửa, đất đai",
    "Quan Lộc": "Sự nghiệp, công danh, địa vị xã hội",
    "Nô Bộc": "Quan hệ với bạn bè, đồng nghiệp, người giúp đỡ",
    "Thiên Di": "Xuất ngoại, di chuyển, đi xa",
    "Tật Ách": "Sức khỏe, bệnh tật",
    "Tài Bạch": "Tài chính, tiền bạc, thu nhập",
    "Tử Tức": "Con cái, dòng dõi",
    "Phu Thê": "Vợ chồng, tình duyên, hôn nhân",
    "Huynh Đệ": "Anh chị em, bạn bè thân thiết"
}


class CungMenh:
    """Class xử lý 12 cung tử vi"""

    @staticmethod
    def tinh_cung_menh(thang_sinh_am: int, gio_sinh: str) -> int:
        """
        Tính vị trí cung Mệnh dựa trên tháng sinh âm lịch và giờ sinh

        Quy tắc: Khởi Dần cung tháng sinh, thuận đếm đến giờ sinh
        - Tháng Giêng (1) tại cung Dần
        - Đếm thuận (Dần->Mão->Thìn...) đến tháng sinh
        - Từ tháng sinh, đếm ngược (Dần->Sửu->Tý...) đến giờ sinh

        Args:
            thang_sinh_am: Tháng sinh âm lịch (1-12)
            gio_sinh: Giờ sinh (Địa Chi)

        Returns:
            Index của cung Mệnh (0-11 tương ứng Tý->Hợi)
        """
        # Tháng 1 (Giêng) ở cung Dần (index 2)
        # Đếm thuận đến tháng sinh
        vi_tri_thang = (2 + thang_sinh_am - 1) % 12

        # Từ vị trí tháng, đếm ngược đến giờ sinh
        gio_index = DIA_CHI.index(gio_sinh)

        # Khoảng cách từ giờ sinh đến Dần (index 2)
        # Đếm ngược từ vị trí tháng
        khoang_cach = (gio_index - 2) % 12
        cung_menh_index = (vi_tri_thang - khoang_cach) % 12

        return cung_menh_index

    @staticmethod
    def tinh_cung_than(cung_menh_index: int) -> int:
        """
        Tính vị trí cung Thân (đối cung với Mệnh)

        Args:
            cung_menh_index: Vị trí cung Mệnh

        Returns:
            Index của cung Thân
        """
        return (cung_menh_index + 6) % 12

    @staticmethod
    def xay_dung_12_cung(thang_sinh_am: int, gio_sinh: str) -> Dict[int, str]:
        """
        Xây dựng toàn bộ 12 cung với vị trí tương ứng

        Args:
            thang_sinh_am: Tháng sinh âm lịch
            gio_sinh: Giờ sinh (Địa Chi)

        Returns:
            Dict với key là index Địa Chi (0-11), value là tên cung
        """
        cung_menh_index = CungMenh.tinh_cung_menh(thang_sinh_am, gio_sinh)

        # Xây dựng map: từ vị trí Địa Chi -> Tên cung
        cung_map = {}

        # Đặt cung Mệnh
        cung_map[cung_menh_index] = "Mệnh"

        # Các cung khác đi theo chiều thuận từ Mệnh
        for i in range(1, 12):
            cung_index = (cung_menh_index + i) % 12
            cung_map[cung_index] = CUNG_NAMES[i]

        return cung_map

    @staticmethod
    def lay_cung_tai_vi_tri(cung_map: Dict[int, str], chi_index: int) -> str:
        """
        Lấy tên cung tại vị trí Địa Chi

        Args:
            cung_map: Map cung đã xây dựng
            chi_index: Index của Địa Chi (0-11)

        Returns:
            Tên cung
        """
        return cung_map.get(chi_index, "")

    @staticmethod
    def lay_vi_tri_cung(cung_map: Dict[int, str], ten_cung: str) -> int:
        """
        Lấy vị trí Địa Chi của một cung

        Args:
            cung_map: Map cung đã xây dựng
            ten_cung: Tên cung cần tìm

        Returns:
            Index Địa Chi của cung (-1 nếu không tìm thấy)
        """
        for chi_index, cung_name in cung_map.items():
            if cung_name == ten_cung:
                return chi_index
        return -1

    @staticmethod
    def hien_thi_12_cung(cung_map: Dict[int, str]) -> str:
        """
        Hiển thị 12 cung theo format dễ đọc

        Args:
            cung_map: Map cung đã xây dựng

        Returns:
            String hiển thị 12 cung
        """
        result = []
        result.append("=" * 60)
        result.append("12 CUNG TỬ VI")
        result.append("=" * 60)

        for i in range(12):
            chi = DIA_CHI[i]
            cung_name = cung_map.get(i, "")
            desc = CUNG_DESCRIPTIONS.get(cung_name, "")
            result.append(f"{chi:5s} ({i+1:2d}) -> {cung_name:12s} | {desc}")

        result.append("=" * 60)
        return "\n".join(result)

    @staticmethod
    def phan_tich_cung(ten_cung: str) -> Dict[str, str]:
        """
        Phân tích thông tin của một cung

        Args:
            ten_cung: Tên cung

        Returns:
            Dict chứa thông tin phân tích
        """
        return {
            "ten_cung": ten_cung,
            "mo_ta": CUNG_DESCRIPTIONS.get(ten_cung, ""),
            "loai": "Chính cung" if ten_cung in ["Mệnh", "Thân"] else "Phụ cung"
        }

    @staticmethod
    def lay_cung_tam_hop(cung_map: Dict[int, str], ten_cung: str) -> List[str]:
        """
        Lấy 3 cung tam hợp với cung cho trước
        Tam hợp: cách nhau 4 cung (120 độ)

        Args:
            cung_map: Map cung đã xây dựng
            ten_cung: Tên cung gốc

        Returns:
            List 3 tên cung tam hợp (bao gồm cả cung gốc)
        """
        vi_tri = CungMenh.lay_vi_tri_cung(cung_map, ten_cung)
        if vi_tri == -1:
            return []

        cung_tam_hop = []
        for i in [0, 4, 8]:  # Cách nhau 4 cung
            vi_tri_tam_hop = (vi_tri + i) % 12
            cung_tam_hop.append(cung_map[vi_tri_tam_hop])

        return cung_tam_hop

    @staticmethod
    def lay_cung_luc_hop(cung_map: Dict[int, str], ten_cung: str) -> List[str]:
        """
        Lấy 6 cung lục hợp với cung cho trước
        Lục hợp: Tý-Sửu, Dần-Hợi, Mão-Tuất, Thìn-Dậu, Tỵ-Thân, Ngọ-Mùi

        Args:
            cung_map: Map cung đã xây dựng
            ten_cung: Tên cung gốc

        Returns:
            List 2 tên cung lục hợp
        """
        luc_hop_pairs = [
            (0, 1),   # Tý-Sửu
            (2, 11),  # Dần-Hợi
            (3, 10),  # Mão-Tuất
            (4, 9),   # Thìn-Dậu
            (5, 8),   # Tỵ-Thân
            (6, 7)    # Ngọ-Mùi
        ]

        vi_tri = CungMenh.lay_vi_tri_cung(cung_map, ten_cung)
        if vi_tri == -1:
            return []

        # Tìm cặp lục hợp
        for pair in luc_hop_pairs:
            if vi_tri == pair[0]:
                return [cung_map[pair[0]], cung_map[pair[1]]]
            elif vi_tri == pair[1]:
                return [cung_map[pair[1]], cung_map[pair[0]]]

        return []

    @staticmethod
    def lay_doi_cung(cung_map: Dict[int, str], ten_cung: str) -> str:
        """
        Lấy đối cung (cách 6 cung - 180 độ)

        Args:
            cung_map: Map cung đã xây dựng
            ten_cung: Tên cung gốc

        Returns:
            Tên đối cung
        """
        vi_tri = CungMenh.lay_vi_tri_cung(cung_map, ten_cung)
        if vi_tri == -1:
            return ""

        doi_vi_tri = (vi_tri + 6) % 12
        return cung_map[doi_vi_tri]


if __name__ == "__main__":
    # Test module
    print("=== Test Module Cung Mệnh ===\n")

    # Test tính cung Mệnh
    thang_am = 4
    gio = "Ngọ"
    cung_menh_idx = CungMenh.tinh_cung_menh(thang_am, gio)
    print(f"Tháng {thang_am} âm, giờ {gio}")
    print(f"Cung Mệnh tại: {DIA_CHI[cung_menh_idx]}\n")

    # Xây dựng 12 cung
    cung_map = CungMenh.xay_dung_12_cung(thang_am, gio)
    print(CungMenh.hien_thi_12_cung(cung_map))

    # Test các quan hệ cung
    print(f"\nĐối cung của Mệnh: {CungMenh.lay_doi_cung(cung_map, 'Mệnh')}")
    print(f"Tam hợp của Mệnh: {CungMenh.lay_cung_tam_hop(cung_map, 'Mệnh')}")
    print(f"Lục hợp của Mệnh: {CungMenh.lay_cung_luc_hop(cung_map, 'Mệnh')}")

    # Phân tích cung
    phan_tich = CungMenh.phan_tich_cung("Mệnh")
    print(f"\nPhân tích cung Mệnh:")
    for key, value in phan_tich.items():
        print(f"  {key}: {value}")
