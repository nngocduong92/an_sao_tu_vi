"""
Module Ngũ Hành - Hệ thống Kim Mộc Thủy Hỏa Thổ
Xử lý các quy tắc sinh khắc, tương sinh, tương khắc
"""

from typing import Dict, List
from .can_chi import THIEN_CAN, DIA_CHI


# Định nghĩa Ngũ hành
NGU_HANH = ["Kim", "Mộc", "Thủy", "Hỏa", "Thổ"]

# Ngũ hành của Thiên Can
CAN_NGU_HANH = {
    "Giáp": "Mộc",
    "Ất": "Mộc",
    "Bính": "Hỏa",
    "Đinh": "Hỏa",
    "Mậu": "Thổ",
    "Kỷ": "Thổ",
    "Canh": "Kim",
    "Tân": "Kim",
    "Nhâm": "Thủy",
    "Quý": "Thủy"
}

# Ngũ hành của Địa Chi
CHI_NGU_HANH = {
    "Tý": "Thủy",
    "Sửu": "Thổ",
    "Dần": "Mộc",
    "Mão": "Mộc",
    "Thìn": "Thổ",
    "Tỵ": "Hỏa",
    "Ngọ": "Hỏa",
    "Mùi": "Thổ",
    "Thân": "Kim",
    "Dậu": "Kim",
    "Tuất": "Thổ",
    "Hợi": "Thủy"
}

# Âm Dương của Thiên Can
CAN_AM_DUONG = {
    "Giáp": "Dương",
    "Ất": "Âm",
    "Bính": "Dương",
    "Đinh": "Âm",
    "Mậu": "Dương",
    "Kỷ": "Âm",
    "Canh": "Dương",
    "Tân": "Âm",
    "Nhâm": "Dương",
    "Quý": "Âm"
}

# Âm Dương của Địa Chi
CHI_AM_DUONG = {
    "Tý": "Dương",
    "Sửu": "Âm",
    "Dần": "Dương",
    "Mão": "Âm",
    "Thìn": "Dương",
    "Tỵ": "Âm",
    "Ngọ": "Dương",
    "Mùi": "Âm",
    "Thân": "Dương",
    "Dậu": "Âm",
    "Tuất": "Dương",
    "Hợi": "Âm"
}

# Quy tắc tương sinh: A sinh B (A tạo ra B)
# Mộc sinh Hỏa, Hỏa sinh Thổ, Thổ sinh Kim, Kim sinh Thủy, Thủy sinh Mộc
TUONG_SINH = {
    "Mộc": "Hỏa",
    "Hỏa": "Thổ",
    "Thổ": "Kim",
    "Kim": "Thủy",
    "Thủy": "Mộc"
}

# Quy tắc tương khắc: A khắc B (A chế ngự B)
# Mộc khắc Thổ, Thổ khắc Thủy, Thủy khắc Hỏa, Hỏa khắc Kim, Kim khắc Mộc
TUONG_KHAC = {
    "Mộc": "Thổ",
    "Thổ": "Thủy",
    "Thủy": "Hỏa",
    "Hỏa": "Kim",
    "Kim": "Mộc"
}


class NguHanh:
    """Class xử lý Ngũ hành và các quy tắc sinh khắc"""

    @staticmethod
    def get_ngu_hanh_can(can: str) -> str:
        """
        Lấy Ngũ hành của Thiên Can

        Args:
            can: Thiên Can

        Returns:
            Ngũ hành (Kim/Mộc/Thủy/Hỏa/Thổ)
        """
        return CAN_NGU_HANH.get(can, "")

    @staticmethod
    def get_ngu_hanh_chi(chi: str) -> str:
        """
        Lấy Ngũ hành của Địa Chi

        Args:
            chi: Địa Chi

        Returns:
            Ngũ hành (Kim/Mộc/Thủy/Hỏa/Thổ)
        """
        return CHI_NGU_HANH.get(chi, "")

    @staticmethod
    def get_ngu_hanh_can_chi(can: str, chi: str) -> str:
        """
        Lấy Ngũ hành chủ đạo của Can Chi (ưu tiên Can)

        Args:
            can: Thiên Can
            chi: Địa Chi

        Returns:
            Ngũ hành chủ đạo
        """
        return NguHanh.get_ngu_hanh_can(can)

    @staticmethod
    def get_am_duong_can(can: str) -> str:
        """
        Lấy Âm Dương của Thiên Can

        Args:
            can: Thiên Can

        Returns:
            "Âm" hoặc "Dương"
        """
        return CAN_AM_DUONG.get(can, "")

    @staticmethod
    def get_am_duong_chi(chi: str) -> str:
        """
        Lấy Âm Dương của Địa Chi

        Args:
            chi: Địa Chi

        Returns:
            "Âm" hoặc "Dương"
        """
        return CHI_AM_DUONG.get(chi, "")

    @staticmethod
    def sinh(hanh_1: str, hanh_2: str) -> bool:
        """
        Kiểm tra hành 1 có sinh hành 2 không

        Args:
            hanh_1: Ngũ hành thứ nhất
            hanh_2: Ngũ hành thứ hai

        Returns:
            True nếu hành 1 sinh hành 2
        """
        return TUONG_SINH.get(hanh_1, "") == hanh_2

    @staticmethod
    def khac(hanh_1: str, hanh_2: str) -> bool:
        """
        Kiểm tra hành 1 có khắc hành 2 không

        Args:
            hanh_1: Ngũ hành thứ nhất
            hanh_2: Ngũ hành thứ hai

        Returns:
            True nếu hành 1 khắc hành 2
        """
        return TUONG_KHAC.get(hanh_1, "") == hanh_2

    @staticmethod
    def bi_sinh(hanh: str) -> str:
        """
        Tìm hành nào sinh ra hành này

        Args:
            hanh: Ngũ hành

        Returns:
            Ngũ hành sinh ra hành này
        """
        for h, target in TUONG_SINH.items():
            if target == hanh:
                return h
        return ""

    @staticmethod
    def bi_khac(hanh: str) -> str:
        """
        Tìm hành nào khắc hành này

        Args:
            hanh: Ngũ hành

        Returns:
            Ngũ hành khắc hành này
        """
        for h, target in TUONG_KHAC.items():
            if target == hanh:
                return h
        return ""

    @staticmethod
    def quan_he(hanh_1: str, hanh_2: str) -> str:
        """
        Xác định quan hệ giữa 2 ngũ hành

        Args:
            hanh_1: Ngũ hành thứ nhất
            hanh_2: Ngũ hành thứ hai

        Returns:
            Mô tả quan hệ: "Sinh", "Khắc", "Bị sinh", "Bị khắc", "Hòa"
        """
        if hanh_1 == hanh_2:
            return "Hòa (cùng hành)"

        if NguHanh.sinh(hanh_1, hanh_2):
            return f"{hanh_1} sinh {hanh_2}"

        if NguHanh.khac(hanh_1, hanh_2):
            return f"{hanh_1} khắc {hanh_2}"

        if NguHanh.sinh(hanh_2, hanh_1):
            return f"{hanh_2} sinh {hanh_1}"

        if NguHanh.khac(hanh_2, hanh_1):
            return f"{hanh_2} khắc {hanh_1}"

        return "Trung hòa"

    @staticmethod
    def phan_tich_ngu_hanh(can: str, chi: str) -> Dict[str, str]:
        """
        Phân tích đầy đủ ngũ hành của can chi

        Args:
            can: Thiên Can
            chi: Địa Chi

        Returns:
            Dict chứa thông tin phân tích
        """
        can_hanh = NguHanh.get_ngu_hanh_can(can)
        chi_hanh = NguHanh.get_ngu_hanh_chi(chi)
        can_am_duong = NguHanh.get_am_duong_can(can)
        chi_am_duong = NguHanh.get_am_duong_chi(chi)

        return {
            "can": can,
            "chi": chi,
            "can_ngu_hanh": can_hanh,
            "chi_ngu_hanh": chi_hanh,
            "can_am_duong": can_am_duong,
            "chi_am_duong": chi_am_duong,
            "chu_hanh": can_hanh,  # Hành chủ đạo (theo Can)
            "quan_he_can_chi": NguHanh.quan_he(can_hanh, chi_hanh)
        }

    @staticmethod
    def tinh_luc_luong_ngu_hanh(danh_sach_can_chi: List[tuple]) -> Dict[str, int]:
        """
        Tính tổng lực lượng của từng ngũ hành trong danh sách Can Chi
        (Dùng để phân tích lá số: năm, tháng, ngày, giờ)

        Args:
            danh_sach_can_chi: List các tuple (can, chi)

        Returns:
            Dict với key là ngũ hành, value là số lần xuất hiện
        """
        dem = {"Kim": 0, "Mộc": 0, "Thủy": 0, "Hỏa": 0, "Thổ": 0}

        for can, chi in danh_sach_can_chi:
            can_hanh = NguHanh.get_ngu_hanh_can(can)
            chi_hanh = NguHanh.get_ngu_hanh_chi(chi)
            dem[can_hanh] += 1
            dem[chi_hanh] += 1

        return dem

    @staticmethod
    def phan_tich_can_bang_ngu_hanh(dem: Dict[str, int]) -> Dict[str, any]:
        """
        Phân tích cân bằng ngũ hành

        Args:
            dem: Dict số lượng từng ngũ hành

        Returns:
            Dict chứa phân tích
        """
        tong = sum(dem.values())
        hanh_manh = max(dem, key=dem.get)
        hanh_yeu = min(dem, key=dem.get)

        return {
            "tong": tong,
            "phan_bo": dem,
            "hanh_manh_nhat": hanh_manh,
            "so_luong_manh": dem[hanh_manh],
            "hanh_yeu_nhat": hanh_yeu,
            "so_luong_yeu": dem[hanh_yeu],
            "can_bang": "Cân bằng" if max(dem.values()) - min(dem.values()) <= 2 else "Mất cân bằng"
        }


if __name__ == "__main__":
    # Test module
    print("=== Test Module Ngũ Hành ===\n")

    # Test lấy ngũ hành
    can = "Canh"
    chi = "Ngọ"
    print(f"Can: {can} -> Ngũ hành: {NguHanh.get_ngu_hanh_can(can)}")
    print(f"Chi: {chi} -> Ngũ hành: {NguHanh.get_ngu_hanh_chi(chi)}")

    # Test phân tích
    phan_tich = NguHanh.phan_tich_ngu_hanh(can, chi)
    print(f"\nPhân tích {can} {chi}:")
    for key, value in phan_tich.items():
        print(f"  {key}: {value}")

    # Test sinh khắc
    print(f"\nKim sinh Thủy: {NguHanh.sinh('Kim', 'Thủy')}")
    print(f"Kim khắc Mộc: {NguHanh.khac('Kim', 'Mộc')}")
    print(f"Quan hệ Kim - Thủy: {NguHanh.quan_he('Kim', 'Thủy')}")
    print(f"Quan hệ Kim - Mộc: {NguHanh.quan_he('Kim', 'Mộc')}")

    # Test phân tích cân bằng (ví dụ 4 trụ)
    danh_sach = [("Canh", "Ngọ"), ("Tân", "Tỵ"), ("Nhâm", "Dần"), ("Giáp", "Thìn")]
    dem = NguHanh.tinh_luc_luong_ngu_hanh(danh_sach)
    can_bang = NguHanh.phan_tich_can_bang_ngu_hanh(dem)
    print(f"\nPhân tích cân bằng ngũ hành:")
    print(f"  Phân bố: {can_bang['phan_bo']}")
    print(f"  Hành mạnh nhất: {can_bang['hanh_manh_nhat']} ({can_bang['so_luong_manh']})")
    print(f"  Hành yếu nhất: {can_bang['hanh_yeu_nhat']} ({can_bang['so_luong_yeu']})")
    print(f"  Đánh giá: {can_bang['can_bang']}")
