#!/usr/bin/env python3
"""
Main Entry Point - Ứng dụng An Sao Tử Vi
Phần mềm tính toán và phân tích lá số tử vi theo phương pháp truyền thống Việt Nam
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from src.ui.console import ConsoleUI


def main():
    """Hàm main chạy ứng dụng"""
    try:
        app = ConsoleUI()
        app.chay()
    except KeyboardInterrupt:
        print("\n\nỨng dụng bị ngắt bởi người dùng. Tạm biệt!")
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
        print("Vui lòng báo cáo lỗi này để được hỗ trợ.")


if __name__ == "__main__":
    main()
