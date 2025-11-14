"""
Module Âm Lịch - Chuyển đổi giữa Âm lịch và Dương lịch
Sử dụng cho tính toán tử vi theo âm lịch Việt Nam
Dựa trên thuật toán của Hồ Ngọc Đức
"""

import math
from datetime import datetime, timedelta
from typing import Tuple


class AmLich:
    """Class chuyển đổi giữa Âm lịch và Dương lịch"""

    @staticmethod
    def jd_from_date(dd: int, mm: int, yy: int) -> int:
        """
        Tính Julian Day Number từ ngày dương lịch

        Args:
            dd: Ngày (1-31)
            mm: Tháng (1-12)
            yy: Năm

        Returns:
            Julian Day Number
        """
        a = (14 - mm) // 12
        y = yy + 4800 - a
        m = mm + 12 * a - 3
        jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
        return jd

    @staticmethod
    def jd_to_date(jd: int) -> Tuple[int, int, int]:
        """
        Chuyển Julian Day Number về ngày dương lịch

        Args:
            jd: Julian Day Number

        Returns:
            Tuple (ngày, tháng, năm)
        """
        a = jd + 32044
        b = (4 * a + 3) // 146097
        c = a - (b * 146097) // 4
        d = (4 * c + 3) // 1461
        e = c - (1461 * d) // 4
        m = (5 * e + 2) // 153
        day = e - (153 * m + 2) // 5 + 1
        month = m + 3 - 12 * (m // 10)
        year = b * 100 + d - 4800 + m // 10
        return day, month, year

    @staticmethod
    def new_moon(k: int) -> float:
        """
        Tính thời điểm sóc (trăng mới) thứ k kể từ điểm đầu năm 2000
        Sử dụng công thức của Jean Meeus

        Args:
            k: Số thứ tự của sóc

        Returns:
            Julian Day Number của thời điểm sóc
        """
        T = k / 1236.85  # Thời gian tính theo thế kỷ Julius từ 1/1/2000
        T2 = T * T
        T3 = T2 * T
        dr = math.pi / 180

        # Độ dài trung bình của trăng
        Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
        Jd1 = Jd1 + 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)

        # Bổ chính do quỹ đạo trái đất
        M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
        Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
        F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3

        C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
        C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
        C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
        C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
        C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
        C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) - 0.0006 * math.sin(dr * (2 * F + Mpr))
        C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) + 0.0005 * math.sin(dr * (2 * Mpr + M))

        delta_t = 0
        if T < -11:
            delta_t = 0.001 + 0.000839 * T + 0.0002261 * T2 - 0.00000845 * T3 - 0.000000081 * T * T3
        else:
            delta_t = -0.000278 + 0.000265 * T + 0.000262 * T2

        JdNew = Jd1 + C1 - delta_t

        return JdNew

    @staticmethod
    def sun_longitude(jdn: float) -> float:
        """
        Tính kinh độ mặt trời tại thời điểm jdn
        Kết quả tính bằng radian

        Args:
            jdn: Julian Day Number

        Returns:
            Kinh độ mặt trời (0 đến 2π radian)
        """
        T = (jdn - 2451545.0) / 36525  # Thời gian tính theo thế kỷ Julius từ 1/1/2000
        T2 = T * T
        dr = math.pi / 180

        # Kinh độ trung bình (mean anomaly)
        M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2

        # Kinh độ trung bình (mean longitude)
        L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2

        # Độ lệch tâm (equation of center)
        DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
        DL = DL + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)

        # Kinh độ thực (true longitude) tính bằng độ
        L = L0 + DL

        # Chuyển sang radian
        L = L * dr

        # Chuẩn hóa về khoảng (0, 2π)
        L = L - math.pi * 2 * (int(L / (math.pi * 2)))

        return L

    @staticmethod
    def get_sun_longitude_segment(jdn: float, time_zone: int = 7) -> int:
        """
        Lấy chỉ số tiết khí (0-11) tương ứng với kinh độ mặt trời
        0: Xuân phân (0°), 1: Thanh minh (15°), ...

        Args:
            jdn: Julian Day Number
            time_zone: Múi giờ (mặc định 7)

        Returns:
            Chỉ số tiết khí (0-11 tương ứng 12 tháng)
        """
        # Tính kinh độ mặt trời tại nửa đêm theo múi giờ
        # sun_longitude trả về radian (0 đến 2π)
        # Chia cho π rồi nhân 6 để ra 12 tiết khí (0-11)
        return int(AmLich.sun_longitude(jdn - 0.5 - time_zone / 24.0) / math.pi * 6)

    @staticmethod
    def get_new_moon_day(k: int, time_zone: int = 7) -> int:
        """
        Tính ngày sóc (trăng non) thứ k theo múi giờ

        Args:
            k: Số thứ tự của sóc
            time_zone: Múi giờ (mặc định 7 cho Việt Nam)

        Returns:
            Julian Day Number của ngày sóc
        """
        jd = AmLich.new_moon(k)
        return int(jd + 0.5 + time_zone / 24.0)

    @staticmethod
    def get_lunar_month_11(yy: int, time_zone: int = 7) -> Tuple[int, int]:
        """
        Tìm tháng 11 âm lịch (tháng có chứa Đông chí)

        Args:
            yy: Năm dương lịch
            time_zone: Múi giờ

        Returns:
            Tuple (off, k) - off là JD của ngày 1 tháng 11 âm, k là số thứ tự sóc
        """
        off = AmLich.jd_from_date(31, 12, yy) - 2415021
        k = int(off / 29.530588853)
        nm = AmLich.get_new_moon_day(k, time_zone)
        sun_long = AmLich.get_sun_longitude_segment(nm, time_zone)

        if sun_long >= 9:
            nm = AmLich.get_new_moon_day(k - 1, time_zone)

        return nm, k

    @staticmethod
    def get_leap_month_offset(a11: int, time_zone: int = 7) -> int:
        """
        Tìm tháng nhuận trong năm âm lịch

        Args:
            a11: JD của ngày 1 tháng 11 năm trước
            time_zone: Múi giờ

        Returns:
            Số thứ tự tháng nhuận (0 nếu không có tháng nhuận)
        """
        k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
        last = 0
        i = 1
        arc = AmLich.get_sun_longitude_segment(AmLich.get_new_moon_day(k + i, time_zone), time_zone)

        while True:
            last = arc
            i += 1
            arc = AmLich.get_sun_longitude_segment(AmLich.get_new_moon_day(k + i, time_zone), time_zone)
            if not (arc != last and i < 14):
                break

        return i - 1

    @staticmethod
    def duong_to_am(dd: int, mm: int, yy: int, time_zone: int = 7) -> Tuple[int, int, int, bool]:
        """
        Chuyển đổi từ dương lịch sang âm lịch

        Args:
            dd: Ngày dương lịch (1-31)
            mm: Tháng dương lịch (1-12)
            yy: Năm dương lịch
            time_zone: Múi giờ (mặc định 7)

        Returns:
            Tuple (ngày âm, tháng âm, năm âm, có phải tháng nhuận không)
        """
        # Tính Julian Day Number của ngày dương lịch
        day_number = AmLich.jd_from_date(dd, mm, yy)

        # Tìm sóc (new moon) gần nhất trước hoặc vào ngày này
        k = int((day_number - 2415021.076998695) / 29.530588853)
        month_start = AmLich.get_new_moon_day(k + 1, time_zone)

        if month_start > day_number:
            month_start = AmLich.get_new_moon_day(k, time_zone)

        # Lấy tháng 11 âm lịch của năm dương lịch
        a11, _ = AmLich.get_lunar_month_11(yy, time_zone)
        b11 = a11

        # Xác định năm âm lịch
        if a11 >= month_start:
            lunar_year = yy
            a11, _ = AmLich.get_lunar_month_11(yy - 1, time_zone)
        else:
            lunar_year = yy + 1
            b11, _ = AmLich.get_lunar_month_11(yy + 1, time_zone)

        # Tính ngày âm lịch
        lunar_day = day_number - month_start + 1

        # Tính số tháng từ tháng 11
        diff = int((month_start - a11) / 29)
        lunar_leap = False
        lunar_month = diff + 11

        # Kiểm tra năm nhuận
        if b11 - a11 > 365:
            leap_month_diff = AmLich.get_leap_month_offset(a11, time_zone)
            if diff >= leap_month_diff:
                lunar_month = diff + 10
            if diff == leap_month_diff:
                lunar_leap = True

        # Điều chỉnh tháng về khoảng 1-12
        if lunar_month > 12:
            lunar_month -= 12

        # Điều chỉnh năm nếu tháng >= 11 và diff < 4
        if lunar_month >= 11 and diff < 4:
            lunar_year -= 1

        return int(lunar_day), int(lunar_month), int(lunar_year), lunar_leap

    @staticmethod
    def am_to_duong(dd: int, mm: int, yy: int, leap: bool = False, time_zone: int = 7) -> Tuple[int, int, int]:
        """
        Chuyển đổi từ âm lịch sang dương lịch

        Args:
            dd: Ngày âm lịch (1-30)
            mm: Tháng âm lịch (1-12)
            yy: Năm âm lịch
            leap: Có phải tháng nhuận không
            time_zone: Múi giờ

        Returns:
            Tuple (ngày dương, tháng dương, năm dương)
        """
        # Xác định cặp tháng 11 (a11, b11) dựa vào tháng âm lịch
        if mm < 11:
            # Tháng 1-10: dùng tháng 11 năm trước và năm hiện tại
            a11, _ = AmLich.get_lunar_month_11(yy - 1, time_zone)
            b11, _ = AmLich.get_lunar_month_11(yy, time_zone)
        else:
            # Tháng 11-12: dùng tháng 11 năm hiện tại và năm sau
            a11, _ = AmLich.get_lunar_month_11(yy, time_zone)
            b11, _ = AmLich.get_lunar_month_11(yy + 1, time_zone)

        # Tính k - số thứ tự sóc kể từ 1/1/1900
        k = int(0.5 + (a11 - 2415021.076998695) / 29.530588853)

        # Tính offset từ tháng 11
        off = mm - 11
        if off < 0:
            off += 12

        # Kiểm tra năm nhuận (có 13 tháng)
        if b11 - a11 > 365:
            # Có tháng nhuận - tìm vị trí tháng nhuận
            leap_off = AmLich.get_leap_month_offset(a11, time_zone)
            leap_month = leap_off - 2
            if leap_month < 0:
                leap_month += 12

            # Kiểm tra tính hợp lệ của tháng nhuận
            if leap and mm != leap_month:
                # Yêu cầu tháng nhuận nhưng tháng không phải tháng nhuận
                raise ValueError(f"Tháng {mm} năm {yy} không phải là tháng nhuận")

            # Điều chỉnh offset nếu cần
            if leap or off >= leap_off:
                off += 1

        # Tính JD của ngày đầu tháng
        month_start = AmLich.get_new_moon_day(k + off, time_zone)

        # Tính JD của ngày cần tìm
        jd = month_start + dd - 1
        return AmLich.jd_to_date(jd)


if __name__ == "__main__":
    # Test module
    print("=== Test Module Âm Lịch ===\n")

    # Test chuyển dương sang âm
    dd, mm, yy = 27, 1, 1992
    ngay_am, thang_am, nam_am, nhuan = AmLich.duong_to_am(dd, mm, yy)
    print(f"Dương lịch: {dd:02d}/{mm:02d}/{yy}")
    print(f"Âm lịch: {ngay_am:02d}/{thang_am:02d}/{nam_am}" + (" (nhuận)" if nhuan else ""))

    # Test chuyển âm sang dương
    dd_am, mm_am, yy_am = 23, 12, 1991
    ngay_dl, thang_dl, nam_dl = AmLich.am_to_duong(dd_am, mm_am, yy_am)
    print(f"\nÂm lịch: {dd_am:02d}/{mm_am:02d}/{yy_am}")
    print(f"Dương lịch: {ngay_dl:02d}/{thang_dl:02d}/{nam_dl}")
