"""
Thuật toán mã hóa Playfair
Bài tập 1 - An Toàn Thông Tin
"""


def tao_ma_tran(khoa):
    """Tạo ma trận Playfair 5x5 từ từ khóa."""
    khoa = khoa.upper().replace("J", "I")
    # Loại bỏ ký tự trùng, giữ thứ tự
    da_dung = []
    for ch in khoa:
        if ch.isalpha() and ch not in da_dung:
            da_dung.append(ch)
    # Thêm các chữ cái còn lại (bỏ J)
    for i in range(26):
        ch = chr(65 + i)
        if ch != "J" and ch not in da_dung:
            da_dung.append(ch)
    # Chuyển thành ma trận 5x5
    ma_tran = []
    for i in range(5):
        ma_tran.append(da_dung[i * 5 : i * 5 + 5])
    return ma_tran


def in_ma_tran(ma_tran):
    """In ma trận 5x5 ra màn hình."""
    print("\nMa trận Playfair 5x5:")
    print("+" + "----+" * 5)
    for hang in ma_tran:
        print("|", end="")
        for ch in hang:
            print(f" {ch}  |", end="")
        print()
        print("+" + "----+" * 5)


def tim_vi_tri(ma_tran, ky_tu):
    """Tìm vị trí (hàng, cột) của ký tự trong ma trận."""
    if ky_tu == "J":
        ky_tu = "I"
    for r in range(5):
        for c in range(5):
            if ma_tran[r][c] == ky_tu:
                return (r, c)
    return None


def tach_cap(van_ban):
    """Tiền xử lý: tách văn bản thành các cặp 2 ký tự."""
    van_ban = van_ban.upper().replace("J", "I")
    van_ban = "".join([ch for ch in van_ban if ch.isalpha()])

    cac_cap = []
    i = 0
    while i < len(van_ban):
        a = van_ban[i]
        if i + 1 >= len(van_ban):
            cac_cap.append((a, "X"))
            i += 1
        elif van_ban[i] == van_ban[i + 1]:
            cac_cap.append((a, "X"))
            i += 1
        else:
            cac_cap.append((a, van_ban[i + 1]))
            i += 2
    return cac_cap


def ma_hoa_cap(ma_tran, a, b):
    """Mã hóa một cặp ký tự theo 3 quy tắc Playfair."""
    r1, c1 = tim_vi_tri(ma_tran, a)
    r2, c2 = tim_vi_tri(ma_tran, b)

    if r1 == r2:  # Cùng hàng -> dịch phải
        quy_tac = "Cùng hàng"
        return ma_tran[r1][(c1 + 1) % 5], ma_tran[r2][(c2 + 1) % 5], quy_tac
    elif c1 == c2:  # Cùng cột -> dịch xuống
        quy_tac = "Cùng cột"
        return ma_tran[(r1 + 1) % 5][c1], ma_tran[(r2 + 1) % 5][c2], quy_tac
    else:  # Hình chữ nhật -> đổi cột
        quy_tac = "Hình chữ nhật"
        return ma_tran[r1][c2], ma_tran[r2][c1], quy_tac


def giai_ma_cap(ma_tran, a, b):
    """Giải mã một cặp ký tự (ngược lại mã hóa)."""
    r1, c1 = tim_vi_tri(ma_tran, a)
    r2, c2 = tim_vi_tri(ma_tran, b)

    if r1 == r2:  # Cùng hàng -> dịch trái
        quy_tac = "Cùng hàng"
        return ma_tran[r1][(c1 - 1) % 5], ma_tran[r2][(c2 - 1) % 5], quy_tac
    elif c1 == c2:  # Cùng cột -> dịch lên
        quy_tac = "Cùng cột"
        return ma_tran[(r1 - 1) % 5][c1], ma_tran[(r2 - 1) % 5][c2], quy_tac
    else:  # Hình chữ nhật -> đổi cột
        quy_tac = "Hình chữ nhật"
        return ma_tran[r1][c2], ma_tran[r2][c1], quy_tac


def ma_hoa(ma_tran, ban_ro):
    """Mã hóa toàn bộ bản rõ."""
    cac_cap = tach_cap(ban_ro)
    print(f"\nBản rõ gốc:    {ban_ro.upper()}")
    print(f"Sau tách cặp:  {' '.join([a+b for a,b in cac_cap])}")
    print(f"\nChi tiết từng bước:")
    print("-" * 50)

    ket_qua = ""
    for i, (a, b) in enumerate(cac_cap):
        x, y, quy_tac = ma_hoa_cap(ma_tran, a, b)
        pos1 = tim_vi_tri(ma_tran, a)
        pos2 = tim_vi_tri(ma_tran, b)
        print(f"  Bước {i+1}: {a}{b} ({pos1}) ({pos2}) -> {x}{y}  [{quy_tac}]")
        ket_qua += x + y

    print("-" * 50)
    print(f"Bản mã:        {ket_qua}")
    return ket_qua


def giai_ma(ma_tran, ban_ma):
    """Giải mã toàn bộ bản mã."""
    ban_ma = ban_ma.upper().replace("J", "I")
    ban_ma = "".join([ch for ch in ban_ma if ch.isalpha()])
    cac_cap = [(ban_ma[i], ban_ma[i + 1]) for i in range(0, len(ban_ma) - 1, 2)]

    print(f"\nBản mã gốc:    {ban_ma}")
    print(f"Các cặp:       {' '.join([a+b for a,b in cac_cap])}")
    print(f"\nChi tiết từng bước:")
    print("-" * 50)

    ket_qua = ""
    for i, (a, b) in enumerate(cac_cap):
        x, y, quy_tac = giai_ma_cap(ma_tran, a, b)
        pos1 = tim_vi_tri(ma_tran, a)
        pos2 = tim_vi_tri(ma_tran, b)
        print(f"  Bước {i+1}: {a}{b} ({pos1}) ({pos2}) -> {x}{y}  [{quy_tac}]")
        ket_qua += x + y

    print("-" * 50)
    print(f"Bản rõ:        {ket_qua}")
    return ket_qua


# ================ KIỂM THỬ ================
if __name__ == "__main__":
    print("=" * 50)
    print("  THUẬT TOÁN MÃ HÓA PLAYFAIR")
    print("  Bài tập 1 - An Toàn Thông Tin")
    print("=" * 50)

    # Ví dụ trong bài giảng: khóa MONARCHY
    khoa = "MONARCHY"
    ban_ro = "INSTRUMENTS"

    print(f"\nTừ khóa: {khoa}")

    # Tạo và in ma trận
    ma_tran = tao_ma_tran(khoa)
    in_ma_tran(ma_tran)

    # Mã hóa
    print("\n" + "=" * 50)
    print("  MÃ HÓA")
    print("=" * 50)
    ban_ma = ma_hoa(ma_tran, ban_ro)

    # Giải mã để kiểm chứng
    print("\n" + "=" * 50)
    print("  GIẢI MÃ (kiểm chứng)")
    print("=" * 50)
    ket_qua = giai_ma(ma_tran, ban_ma)

    print("\n" + "=" * 50)
    print("  KẾT LUẬN")
    print("=" * 50)
    print(f"  Bản rõ ban đầu:  {ban_ro.upper()}")
    print(f"  Sau mã hóa:      {ban_ma}")
    print(f"  Sau giải mã:     {ket_qua}")
    print(f"  Khớp: {'✓ ĐÚNG' if ban_ro.upper().replace('J','I') in ket_qua or ket_qua.startswith(ban_ro.upper().replace('J','I')) else '✗ SAI'}")
    print("=" * 50)
