"""
Module Phụ Diệu - Các sao phụ trong Tử Vi
Bao gồm: Văn tinh, Tả Hữu, Thiên Khôi Việt, Lộc Tồn, Tứ Hóa, v.v.
"""

from typing import Dict, List


# Các nhóm sao phụ
VAN_TINH = ["Văn Xương", "Văn Khúc"]
TA_HUU = ["Tả Phụ", "Hữu Bật"]
KHOI_VIET = ["Thiên Khôi", "Thiên Việt"]
LOC_TON = ["Lộc Tồn", "Thiên Mã"]
TU_HOA = ["Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Hóa Kỵ"]
LONG_PHUONG = ["Long Trì", "Phượng Các"]
TAM_DAI = ["Thiên Quan", "Thiên Phúc", "Thiên Không"]

# Ý nghĩa sao phụ
PHU_DIEU_Y_NGHIA = {
    "Văn Xương": "Văn chương, học vấn, thi cử, tài năng",
    "Văn Khúc": "Nghệ thuật, âm nhạc, sáng tạo",
    "Tả Phụ": "Quý nhân bên trái, hỗ trợ nam giới",
    "Hữu Bật": "Quý nhân bên phải, hỗ trợ nữ giới",
    "Thiên Khôi": "Quý nhân thiên thời, may mắn",
    "Thiên Việt": "Quý nhân địa lợi, thuận lợi",
    "Lộc Tồn": "Tài lộc, của cải, tích trữ",
    "Thiên Mã": "Vận động, di chuyển, năng động",
    "Hóa Lộc": "Tài lộc, sung túc, may mắn",
    "Hóa Quyền": "Quyền lực, uy tín, nắm quyền",
    "Hóa Khoa": "Công danh, thi cử, danh tiếng",
    "Hóa Kỵ": "Trở ngại, thất bại, điều không tốt",
    "Long Trì": "Danh vọng nam, cao quý",
    "Phượng Các": "Danh vọng nữ, tú nhã",
    "Thiên Quan": "Tước vị, chức vị quan",
    "Thiên Phúc": "Phúc lộc, hạnh phúc",
    "Thiên Không": "Trống rỗng, tâm linh, hư vô"
}


class PhuDieu:
    """Class xử lý các sao phụ diệu"""

    @staticmethod
    def an_van_tinh(gio_sinh_index: int, nam_sinh_am: int) -> Dict[str, int]:
        """
        An Văn Xương và Văn Khúc

        Quy tắc:
        - Văn Xương: dựa vào giờ sinh
        - Văn Khúc: dựa vào năm sinh

        Args:
            gio_sinh_index: Index giờ sinh (0-11)
            nam_sinh_am: Năm sinh âm lịch

        Returns:
            Dict với key là tên sao, value là vị trí
        """
        result = {}

        # Văn Xương: khởi Tý thuận đếm theo giờ
        van_xuong_map = {
            0: 0,   # Tý -> Tý
            1: 1,   # Sửu -> Sửu
            2: 2,   # Dần -> Dần
            3: 3,   # Mão -> Mão
            4: 4,   # Thìn -> Thìn
            5: 5,   # Tỵ -> Tỵ
            6: 10,  # Ngọ -> Tuất
            7: 9,   # Mùi -> Dậu
            8: 8,   # Thân -> Thân
            9: 7,   # Dậu -> Mùi
            10: 6,  # Tuất -> Ngọ
            11: 11  # Hợi -> Hợi
        }

        result["Văn Xương"] = van_xuong_map[gio_sinh_index]

        # Văn Khúc: dựa vào năm sinh (Can năm)
        # Đơn giản hóa: theo năm % 10
        can_nam_index = (nam_sinh_am - 4) % 10
        van_khuc_map = {
            0: 4,   # Giáp -> Thìn
            1: 6,   # Ất -> Ngọ
            2: 8,   # Bính -> Thân
            3: 10,  # Đinh -> Tuất
            4: 10,  # Mậu -> Tuất
            5: 0,   # Kỷ -> Tý
            6: 2,   # Canh -> Dần
            7: 4,   # Tân -> Thìn
            8: 6,   # Nhâm -> Ngọ
            9: 8    # Quý -> Thân
        }

        result["Văn Khúc"] = van_khuc_map[can_nam_index]

        return result

    @staticmethod
    def an_ta_huu(thang_am: int, gio_sinh_index: int) -> Dict[str, int]:
        """
        An Tả Phụ và Hữu Bật

        Quy tắc:
        - Tả Phụ: dựa vào tháng sinh
        - Hữu Bật: dựa vào giờ sinh

        Args:
            thang_am: Tháng sinh âm lịch (1-12)
            gio_sinh_index: Index giờ sinh (0-11)

        Returns:
            Dict với key là tên sao, value là vị trí
        """
        result = {}

        # Tả Phụ: tháng 1 tại Thìn, thuận
        ta_phu_pos = (4 + thang_am - 1) % 12
        result["Tả Phụ"] = ta_phu_pos

        # Hữu Bật: giờ Tý tại Tuất, nghịch
        huu_bat_pos = (10 - gio_sinh_index) % 12
        result["Hữu Bật"] = huu_bat_pos

        return result

    @staticmethod
    def an_khoi_viet(nam_sinh_am: int) -> Dict[str, int]:
        """
        An Thiên Khôi và Thiên Việt

        Dựa vào Can của năm sinh

        Args:
            nam_sinh_am: Năm sinh âm lịch

        Returns:
            Dict với key là tên sao, value là vị trí
        """
        result = {}

        can_nam_index = (nam_sinh_am - 4) % 10

        # Thiên Khôi
        khoi_map = {
            0: 1,   # Giáp -> Sửu
            1: 0,   # Ất -> Tý
            2: 11,  # Bính -> Hợi
            3: 11,  # Đinh -> Hợi
            4: 1,   # Mậu -> Sửu
            5: 0,   # Kỷ -> Tý
            6: 1,   # Canh -> Sửu
            7: 6,   # Tân -> Ngọ
            8: 3,   # Nhâm -> Mão
            9: 3    # Quý -> Mão
        }

        # Thiên Việt
        viet_map = {
            0: 7,   # Giáp -> Mùi
            1: 8,   # Ất -> Thân
            2: 9,   # Bính -> Dậu
            3: 9,   # Đinh -> Dậu
            4: 7,   # Mậu -> Mùi
            5: 8,   # Kỷ -> Thân
            6: 7,   # Canh -> Mùi
            7: 2,   # Tân -> Dần
            8: 5,   # Nhâm -> Tỵ
            9: 5    # Quý -> Tỵ
        }

        result["Thiên Khôi"] = khoi_map[can_nam_index]
        result["Thiên Việt"] = viet_map[can_nam_index]

        return result

    @staticmethod
    def an_loc_ton(nam_sinh_am: int) -> Dict[str, int]:
        """
        An Lộc Tồn

        Dựa vào Can của năm sinh

        Args:
            nam_sinh_am: Năm sinh âm lịch

        Returns:
            Dict với key là "Lộc Tồn", value là vị trí
        """
        can_nam_index = (nam_sinh_am - 4) % 10

        loc_ton_map = {
            0: 2,   # Giáp -> Dần
            1: 3,   # Ất -> Mão
            2: 5,   # Bính -> Tỵ
            3: 6,   # Đinh -> Ngọ
            4: 5,   # Mậu -> Tỵ
            5: 6,   # Kỷ -> Ngọ
            6: 8,   # Canh -> Thân
            7: 9,   # Tân -> Dậu
            8: 11,  # Nhâm -> Hợi
            9: 0    # Quý -> Tý
        }

        return {"Lộc Tồn": loc_ton_map[can_nam_index]}

    @staticmethod
    def an_thien_ma(nam_sinh_chi_index: int) -> Dict[str, int]:
        """
        An Thiên Mã

        Dựa vào Chi của năm sinh (Tam hợp)

        Args:
            nam_sinh_chi_index: Index Chi của năm sinh

        Returns:
            Dict với key là "Thiên Mã", value là vị trí
        """
        # Tam hợp:
        # Dần Ngọ Tuất -> Thân
        # Thân Tý Thìn -> Dần
        # Tỵ Dậu Sửu -> Hợi
        # Hợi Mão Mùi -> Tỵ

        thien_ma_map = {
            0: 2,   # Tý -> Dần
            1: 11,  # Sửu -> Hợi
            2: 8,   # Dần -> Thân
            3: 5,   # Mão -> Tỵ
            4: 2,   # Thìn -> Dần
            5: 11,  # Tỵ -> Hợi
            6: 8,   # Ngọ -> Thân
            7: 5,   # Mùi -> Tỵ
            8: 2,   # Thân -> Dần
            9: 11,  # Dậu -> Hợi
            10: 8,  # Tuất -> Thân
            11: 5   # Hợi -> Tỵ
        }

        return {"Thiên Mã": thien_ma_map[nam_sinh_chi_index]}

    @staticmethod
    def an_tu_hoa(nam_sinh_am: int) -> Dict[str, str]:
        """
        An Tứ Hóa (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ)

        Tứ Hóa là 4 sao biến hóa của năm, gắn với các sao chính

        Args:
            nam_sinh_am: Năm sinh âm lịch

        Returns:
            Dict với key là tên Hóa, value là tên sao bị hóa
        """
        can_nam_index = (nam_sinh_am - 4) % 10

        # Map: Can năm -> (Lộc, Quyền, Khoa, Kỵ)
        tu_hoa_map = {
            0: ("Liêm Trinh", "Phá Quân", "Vũ Khúc", "Thái Dương"),      # Giáp
            1: ("Thiên Cơ", "Thiên Lương", "Tử Vi", "Thái Âm"),          # Ất
            2: ("Thiên Đồng", "Thiên Cơ", "Văn Xương", "Liêm Trinh"),    # Bính
            3: ("Thái Âm", "Thiên Đồng", "Thiên Cơ", "Cự Môn"),          # Đinh
            4: ("Tham Lang", "Thái Âm", "Hữu Bật", "Thiên Cơ"),          # Mậu
            5: ("Vũ Khúc", "Tham Lang", "Thiên Lương", "Văn Khúc"),      # Kỷ
            6: ("Thái Dương", "Vũ Khúc", "Thiên Phủ", "Thái Âm"),        # Canh
            7: ("Cự Môn", "Thái Dương", "Văn Khúc", "Văn Xương"),        # Tân
            8: ("Thiên Lương", "Tử Vi", "Tả Phụ", "Vũ Khúc"),            # Nhâm
            9: ("Phá Quân", "Cự Môn", "Thái Âm", "Tham Lang")            # Quý
        }

        hoa_tuple = tu_hoa_map[can_nam_index]

        return {
            "Hóa Lộc": hoa_tuple[0],
            "Hóa Quyền": hoa_tuple[1],
            "Hóa Khoa": hoa_tuple[2],
            "Hóa Kỵ": hoa_tuple[3]
        }

    @staticmethod
    def an_tat_ca_phu_dieu(ngay_am: int, thang_am: int, nam_am: int,
                           gio_sinh_index: int) -> Dict[str, any]:
        """
        An tất cả các sao phụ diệu

        Args:
            ngay_am: Ngày sinh âm lịch
            thang_am: Tháng sinh âm lịch
            nam_am: Năm sinh âm lịch
            gio_sinh_index: Index giờ sinh

        Returns:
            Dict chứa tất cả sao phụ (vị trí và hóa)
        """
        result = {}

        # An các sao có vị trí cụ thể
        result.update(PhuDieu.an_van_tinh(gio_sinh_index, nam_am))
        result.update(PhuDieu.an_ta_huu(thang_am, gio_sinh_index))
        result.update(PhuDieu.an_khoi_viet(nam_am))
        result.update(PhuDieu.an_loc_ton(nam_am))

        # Chi năm sinh
        chi_nam_index = (nam_am - 4) % 12
        result.update(PhuDieu.an_thien_ma(chi_nam_index))

        # Tứ Hóa (không có vị trí cụ thể, gắn với sao chính)
        tu_hoa = PhuDieu.an_tu_hoa(nam_am)
        result["tu_hoa"] = tu_hoa

        return result

    @staticmethod
    def lay_thong_tin_sao_phu(ten_sao: str) -> Dict[str, str]:
        """
        Lấy thông tin chi tiết của sao phụ

        Args:
            ten_sao: Tên sao phụ

        Returns:
            Dict chứa thông tin
        """
        return {
            "ten": ten_sao,
            "y_nghia": PHU_DIEU_Y_NGHIA.get(ten_sao, "")
        }


if __name__ == "__main__":
    # Test module
    print("=== Test Module Phụ Diệu ===\n")

    ngay = 15
    thang = 4
    nam = 1990
    gio_idx = 6  # Ngọ

    print(f"Ngày {ngay}/{thang}/{nam} âm, giờ {gio_idx}\n")

    # An tất cả sao phụ
    sao_phu_map = PhuDieu.an_tat_ca_phu_dieu(ngay, thang, nam, gio_idx)

    print("Các sao phụ diệu:")
    for sao, info in sao_phu_map.items():
        if sao == "tu_hoa":
            print("\nTứ Hóa:")
            for hoa, sao_bi_hoa in info.items():
                print(f"  {hoa:12s} -> {sao_bi_hoa}")
        else:
            from ..core.can_chi import DIA_CHI
            print(f"  {sao:15s} -> {DIA_CHI[info]}")

    # Test thông tin sao
    print("\nThông tin sao Văn Xương:")
    info = PhuDieu.lay_thong_tin_sao_phu("Văn Xương")
    for key, value in info.items():
        print(f"  {key}: {value}")
