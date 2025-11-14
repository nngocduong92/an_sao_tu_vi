"""
Module Can Chi - Hệ thống Thiên Can, Địa Chi
Tính toán can chi của năm, tháng, ngày, giờ theo phương pháp truyền thống
"""

from typing import Tuple

# 10 Thiên Can
THIEN_CAN = [
    "Giáp", "Ất", "Bính", "Đinh", "Mậu",
    "Kỷ", "Canh", "Tân", "Nhâm", "Quý"
]

# 12 Địa Chi
DIA_CHI = [
    "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
    "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
]

# 12 Con giáp tương ứng với Địa Chi
CON_GIAP = [
    "Tý (Chuột)", "Sửu (Trâu)", "Dần (Hổ)", "Mão (Mèo)",
    "Thìn (Rồng)", "Tỵ (Rắn)", "Ngọ (Ngựa)", "Mùi (Dê)",
    "Thân (Khỉ)", "Dậu (Gà)", "Tuất (Chó)", "Hợi (Lợn)"
]


class CanChi:
    """Class xử lý các phép tính về Can Chi"""

    @staticmethod
    def get_can_chi_nam(nam: int) -> Tuple[str, str]:
        """
        Tính Can Chi của năm dương lịch

        Args:
            nam: Năm dương lịch (ví dụ: 1990)

        Returns:
            Tuple (Thiên Can, Địa Chi)
        """
        # Năm Giáp Tý là năm 1984 (chu kỳ 60 năm)
        # Can = (năm - 4) % 10
        # Chi = (năm - 4) % 12
        can_index = (nam - 4) % 10
        chi_index = (nam - 4) % 12

        return THIEN_CAN[can_index], DIA_CHI[chi_index]

    @staticmethod
    def get_can_chi_thang(nam: int, thang: int) -> Tuple[str, str]:
        """
        Tính Can Chi của tháng

        Quy tắc: Can của tháng được tính dựa vào Can của năm
        - Giáp/Kỷ năm: tháng 1 là Bính Dần
        - Ất/Canh năm: tháng 1 là Mậu Dần
        - Bính/Tân năm: tháng 1 là Canh Dần
        - Đinh/Nhâm năm: tháng 1 là Nhâm Dần
        - Mậu/Quý năm: tháng 1 là Giáp Dần

        Args:
            nam: Năm dương lịch
            thang: Tháng (1-12)

        Returns:
            Tuple (Thiên Can, Địa Chi)
        """
        can_nam, _ = CanChi.get_can_chi_nam(nam)
        can_nam_index = THIEN_CAN.index(can_nam)

        # Tháng 1 bắt đầu từ Dần (index 2 trong Địa Chi)
        chi_thang_index = (thang + 1) % 12

        # Tính Can của tháng 1 dựa vào Can của năm
        can_thang_1_map = {
            0: 2,  # Giáp năm -> Bính (index 2)
            1: 4,  # Ất năm -> Mậu (index 4)
            2: 6,  # Bính năm -> Canh (index 6)
            3: 8,  # Đinh năm -> Nhâm (index 8)
            4: 0,  # Mậu năm -> Giáp (index 0)
            5: 2,  # Kỷ năm -> Bính (index 2)
            6: 4,  # Canh năm -> Mậu (index 4)
            7: 6,  # Tân năm -> Canh (index 6)
            8: 8,  # Nhâm năm -> Nhâm (index 8)
            9: 0,  # Quý năm -> Giáp (index 0)
        }

        can_thang_1 = can_thang_1_map[can_nam_index]
        can_thang_index = (can_thang_1 + thang - 1) % 10

        return THIEN_CAN[can_thang_index], DIA_CHI[chi_thang_index]

    @staticmethod
    def get_can_chi_ngay(jd: int) -> Tuple[str, str]:
        """
        Tính Can Chi của ngày dựa trên Julian Day Number

        Args:
            jd: Julian Day Number

        Returns:
            Tuple (Thiên Can, Địa Chi)
        """
        # Ngày 01/01/1984 (Giáp Tý) có JD = 2445701
        # Can = (jd + 9) % 10
        # Chi = (jd + 1) % 12
        can_index = (jd + 9) % 10
        chi_index = (jd + 1) % 12

        return THIEN_CAN[can_index], DIA_CHI[chi_index]

    @staticmethod
    def get_can_chi_gio(gio: int, can_ngay: str) -> Tuple[str, str]:
        """
        Tính Can Chi của giờ

        Quy tắc tương tự tháng:
        - Giáp/Kỷ ngày: giờ Tý là Giáp Tý
        - Ất/Canh ngày: giờ Tý là Bính Tý
        - Bính/Tân ngày: giờ Tý là Mậu Tý
        - Đinh/Nhâm ngày: giờ Tý là Canh Tý
        - Mậu/Quý ngày: giờ Tý là Nhâm Tý

        Args:
            gio: Giờ trong ngày (0-23)
            can_ngay: Can của ngày

        Returns:
            Tuple (Thiên Can, Địa Chi)
        """
        # Chuyển giờ sang địa chi (mỗi giờ địa chi = 2 giờ đồng hồ)
        chi_gio_index = ((gio + 1) // 2) % 12

        can_ngay_index = THIEN_CAN.index(can_ngay)

        # Tính Can của giờ Tý (23h-1h) dựa vào Can của ngày
        can_gio_ty_map = {
            0: 0,  # Giáp ngày -> Giáp Tý
            1: 2,  # Ất ngày -> Bính Tý
            2: 4,  # Bính ngày -> Mậu Tý
            3: 6,  # Đinh ngày -> Canh Tý
            4: 8,  # Mậu ngày -> Nhâm Tý
            5: 0,  # Kỷ ngày -> Giáp Tý
            6: 2,  # Canh ngày -> Bính Tý
            7: 4,  # Tân ngày -> Mậu Tý
            8: 6,  # Nhâm ngày -> Canh Tý
            9: 8,  # Quý ngày -> Nhâm Tý
        }

        can_gio_ty = can_gio_ty_map[can_ngay_index]
        can_gio_index = (can_gio_ty + chi_gio_index) % 10

        return THIEN_CAN[can_gio_index], DIA_CHI[chi_gio_index]

    @staticmethod
    def get_gio_dia_chi(gio: int) -> str:
        """
        Chuyển giờ thành Địa Chi

        Args:
            gio: Giờ trong ngày (0-23)

        Returns:
            Tên Địa Chi của giờ
        """
        chi_index = ((gio + 1) // 2) % 12
        return DIA_CHI[chi_index]

    @staticmethod
    def get_con_giap(nam: int) -> str:
        """
        Lấy con giáp của năm

        Args:
            nam: Năm dương lịch

        Returns:
            Tên con giáp
        """
        _, chi = CanChi.get_can_chi_nam(nam)
        chi_index = DIA_CHI.index(chi)
        return CON_GIAP[chi_index]

    @staticmethod
    def get_can_chi_string(can: str, chi: str) -> str:
        """
        Ghép Can và Chi thành chuỗi đầy đủ

        Args:
            can: Thiên Can
            chi: Địa Chi

        Returns:
            Chuỗi Can Chi (ví dụ: "Giáp Tý")
        """
        return f"{can} {chi}"


def julian_day_number(ngay: int, thang: int, nam: int) -> int:
    """
    Tính Julian Day Number cho một ngày dương lịch

    Args:
        ngay: Ngày (1-31)
        thang: Tháng (1-12)
        nam: Năm dương lịch

    Returns:
        Julian Day Number
    """
    a = (14 - thang) // 12
    y = nam + 4800 - a
    m = thang + 12 * a - 3

    jd = ngay + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    return jd


if __name__ == "__main__":
    # Test module
    print("=== Test Module Can Chi ===\n")

    # Test năm
    nam = 1990
    can, chi = CanChi.get_can_chi_nam(nam)
    print(f"Năm {nam}: {can} {chi} - {CanChi.get_con_giap(nam)}")

    # Test tháng
    thang = 5
    can_t, chi_t = CanChi.get_can_chi_thang(nam, thang)
    print(f"Tháng {thang}/{nam}: {can_t} {chi_t}")

    # Test ngày
    jd = julian_day_number(15, 5, 1990)
    can_n, chi_n = CanChi.get_can_chi_ngay(jd)
    print(f"Ngày 15/5/1990 (JD={jd}): {can_n} {chi_n}")

    # Test giờ
    gio = 14
    can_g, chi_g = CanChi.get_can_chi_gio(gio, can_n)
    print(f"Giờ {gio}h (ngày {can_n} {chi_n}): {can_g} {chi_g}")
