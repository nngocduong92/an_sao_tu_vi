"""
Module An Sao - Tổng hợp thuật toán an sao vào lá số tử vi
Kết hợp sao chính và sao phụ
"""

from typing import Dict, List
from .chinh_dieu import ChinhDieu
from .phu_dieu import PhuDieu


class AnSao:
    """Class tổng hợp an tất cả các sao vào lá số"""

    @staticmethod
    def an_toan_bo_sao(ngay_am: int, thang_am: int, nam_am: int,
                       gio_sinh_index: int) -> Dict[str, any]:
        """
        An toàn bộ sao chính và phụ vào lá số

        Args:
            ngay_am: Ngày sinh âm lịch
            thang_am: Tháng sinh âm lịch
            nam_am: Năm sinh âm lịch
            gio_sinh_index: Index giờ sinh (0-11)

        Returns:
            Dict chứa:
            - 'chinh_dieu': Dict các sao chính (tên -> vị trí)
            - 'phu_dieu': Dict các sao phụ (tên -> vị trí)
            - 'tu_hoa': Dict tứ hóa (tên hóa -> sao bị hóa)
        """
        # An 14 sao chính diệu
        sao_chinh = ChinhDieu.an_14_chinh_sao(ngay_am, thang_am, gio_sinh_index)

        # An các sao phụ diệu
        sao_phu_full = PhuDieu.an_tat_ca_phu_dieu(ngay_am, thang_am, nam_am, gio_sinh_index)

        # Tách tứ hóa ra
        tu_hoa = sao_phu_full.pop("tu_hoa", {})
        sao_phu = sao_phu_full

        return {
            "chinh_dieu": sao_chinh,
            "phu_dieu": sao_phu,
            "tu_hoa": tu_hoa
        }

    @staticmethod
    def lay_sao_tai_cung(sao_data: Dict[str, any], chi_index: int) -> Dict[str, List[str]]:
        """
        Lấy tất cả các sao tại một cung cụ thể

        Args:
            sao_data: Dict từ an_toan_bo_sao()
            chi_index: Index cung (0-11)

        Returns:
            Dict với key là loại sao, value là list tên sao
        """
        result = {
            "chinh_dieu": [],
            "phu_dieu": [],
            "tu_hoa": []
        }

        # Sao chính
        for ten_sao, vi_tri in sao_data["chinh_dieu"].items():
            if vi_tri == chi_index:
                result["chinh_dieu"].append(ten_sao)

        # Sao phụ
        for ten_sao, vi_tri in sao_data["phu_dieu"].items():
            if vi_tri == chi_index:
                result["phu_dieu"].append(ten_sao)

        # Tứ hóa (kiểm tra sao nào bị hóa ở cung này)
        for hoa, sao_bi_hoa in sao_data["tu_hoa"].items():
            # Tìm vị trí của sao bị hóa
            if sao_bi_hoa in sao_data["chinh_dieu"]:
                vi_tri_sao = sao_data["chinh_dieu"][sao_bi_hoa]
                if vi_tri_sao == chi_index:
                    result["tu_hoa"].append(f"{sao_bi_hoa} {hoa}")
            elif sao_bi_hoa in sao_data["phu_dieu"]:
                vi_tri_sao = sao_data["phu_dieu"][sao_bi_hoa]
                if vi_tri_sao == chi_index:
                    result["tu_hoa"].append(f"{sao_bi_hoa} {hoa}")

        return result

    @staticmethod
    def dem_sao_theo_loai(sao_data: Dict[str, any]) -> Dict[str, int]:
        """
        Đếm số lượng sao theo từng loại

        Args:
            sao_data: Dict từ an_toan_bo_sao()

        Returns:
            Dict với số lượng từng loại sao
        """
        return {
            "tong_chinh_dieu": len(sao_data["chinh_dieu"]),
            "tong_phu_dieu": len(sao_data["phu_dieu"]),
            "tong_tu_hoa": len(sao_data["tu_hoa"])
        }

    @staticmethod
    def tim_sao_dong_cung(sao_data: Dict[str, any]) -> Dict[int, List[str]]:
        """
        Tìm các cung có nhiều sao đồng cung

        Args:
            sao_data: Dict từ an_toan_bo_sao()

        Returns:
            Dict với key là index cung, value là list tên sao trong cung
        """
        dong_cung = {}

        for i in range(12):
            sao_tai_cung = AnSao.lay_sao_tai_cung(sao_data, i)

            # Ghép tất cả sao lại
            tat_ca_sao = (sao_tai_cung["chinh_dieu"] +
                         sao_tai_cung["phu_dieu"] +
                         sao_tai_cung["tu_hoa"])

            if len(tat_ca_sao) >= 2:  # Chỉ lấy cung có từ 2 sao trở lên
                dong_cung[i] = tat_ca_sao

        return dong_cung

    @staticmethod
    def phan_tich_sao_tot_xau(sao_data: Dict[str, any]) -> Dict[str, List[str]]:
        """
        Phân tích các sao tốt và xấu trong lá số

        Args:
            sao_data: Dict từ an_toan_bo_sao()

        Returns:
            Dict phân loại sao tốt/xấu
        """
        sao_tot = [
            "Tử Vi", "Thiên Phủ", "Thái Dương", "Thái Âm",
            "Thiên Đồng", "Thiên Lương", "Văn Xương", "Văn Khúc",
            "Tả Phụ", "Hữu Bật", "Thiên Khôi", "Thiên Việt",
            "Lộc Tồn", "Hóa Lộc", "Hóa Quyền", "Hóa Khoa"
        ]

        sao_xau = [
            "Thất Sát", "Phá Quân", "Liêm Trinh", "Tham Lang",
            "Hóa Kỵ"
        ]

        result = {
            "tot": [],
            "xau": [],
            "trung_binh": []
        }

        # Kiểm tra sao chính
        for ten_sao in sao_data["chinh_dieu"].keys():
            if ten_sao in sao_tot:
                result["tot"].append(ten_sao)
            elif ten_sao in sao_xau:
                result["xau"].append(ten_sao)
            else:
                result["trung_binh"].append(ten_sao)

        # Kiểm tra sao phụ
        for ten_sao in sao_data["phu_dieu"].keys():
            if ten_sao in sao_tot:
                result["tot"].append(ten_sao)
            elif ten_sao in sao_xau:
                result["xau"].append(ten_sao)

        # Kiểm tra tứ hóa
        for hoa, sao_bi_hoa in sao_data["tu_hoa"].items():
            sao_hoa_day_du = f"{sao_bi_hoa} {hoa}"
            if hoa in sao_tot:
                result["tot"].append(sao_hoa_day_du)
            elif hoa in sao_xau:
                result["xau"].append(sao_hoa_day_du)

        return result

    @staticmethod
    def hien_thi_tat_ca_sao(sao_data: Dict[str, any]) -> str:
        """
        Hiển thị tất cả các sao theo format dễ đọc

        Args:
            sao_data: Dict từ an_toan_bo_sao()

        Returns:
            String hiển thị
        """
        from ..core.can_chi import DIA_CHI

        lines = []
        lines.append("=" * 70)
        lines.append("TẤT CẢ CÁC SAO TRONG LÁ SỐ")
        lines.append("=" * 70)

        # Hiển thị sao chính
        lines.append("\n14 SAO CHÍNH DIỆU:")
        lines.append("-" * 70)
        for ten_sao, vi_tri in sorted(sao_data["chinh_dieu"].items(), key=lambda x: x[1]):
            lines.append(f"  {ten_sao:15s} -> {DIA_CHI[vi_tri]:5s} (cung {vi_tri + 1})")

        # Hiển thị sao phụ
        lines.append("\nCÁC SAO PHỤ DIỆU:")
        lines.append("-" * 70)
        for ten_sao, vi_tri in sorted(sao_data["phu_dieu"].items(), key=lambda x: x[1]):
            lines.append(f"  {ten_sao:15s} -> {DIA_CHI[vi_tri]:5s} (cung {vi_tri + 1})")

        # Hiển thị tứ hóa
        lines.append("\nTỨ HÓA:")
        lines.append("-" * 70)
        for hoa, sao_bi_hoa in sao_data["tu_hoa"].items():
            lines.append(f"  {hoa:12s} -> {sao_bi_hoa}")

        lines.append("=" * 70)

        return "\n".join(lines)


if __name__ == "__main__":
    # Test module
    print("=== Test Module An Sao ===\n")

    ngay = 15
    thang = 4
    nam = 1990
    gio_idx = 6  # Ngọ

    print(f"Ngày {ngay}/{thang}/{nam} âm, giờ {gio_idx}\n")

    # An toàn bộ sao
    sao_data = AnSao.an_toan_bo_sao(ngay, thang, nam, gio_idx)

    # Hiển thị tất cả sao
    print(AnSao.hien_thi_tat_ca_sao(sao_data))

    # Thống kê
    dem = AnSao.dem_sao_theo_loai(sao_data)
    print(f"\nThống kê:")
    for key, value in dem.items():
        print(f"  {key}: {value}")

    # Sao đồng cung
    dong_cung = AnSao.tim_sao_dong_cung(sao_data)
    print(f"\nCác cung có nhiều sao đồng cung:")
    from ..core.can_chi import DIA_CHI
    for chi_idx, sao_list in sorted(dong_cung.items()):
        print(f"  {DIA_CHI[chi_idx]:5s}: {', '.join(sao_list)}")

    # Phân tích tốt xấu
    phan_tich = AnSao.phan_tich_sao_tot_xau(sao_data)
    print(f"\nPhân tích sao:")
    print(f"  Sao tốt ({len(phan_tich['tot'])}): {', '.join(phan_tich['tot'][:5])}...")
    print(f"  Sao xấu ({len(phan_tich['xau'])}): {', '.join(phan_tich['xau'])}")
