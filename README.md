# Thuật Toán Mã Hóa Playfair

Bài tập 1 - An Toàn Thông Tin

## Mô tả

Cài đặt thuật toán mã hóa Playfair bằng Python. Chương trình thực hiện:
- Tạo ma trận Playfair 5×5 từ từ khóa
- Mã hóa bản rõ theo 3 quy tắc: cùng hàng, cùng cột, hình chữ nhật
- Giải mã bản mã

## Chạy chương trình

```bash
python playfair.py
```

## Ví dụ kiểm thử

- **Từ khóa:** MONARCHY
- **Bản rõ:** Do you like to study Cryptography course
- **Bản mã:** HRHNMUKEKLAPLZCBDMHQPRKNOSYBHMZMLI

## Quá trình thực hiện

### Bước 1: Tạo ma trận Playfair 5×5

Từ khóa: **MONARCHY**

Lấy các ký tự không trùng từ khóa: `M O N A R C H Y`, sau đó điền các chữ cái còn lại (bỏ J):

|   | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **0** | M | O | N | A | R |
| **1** | C | H | Y | B | D |
| **2** | E | F | G | I | K |
| **3** | L | P | Q | S | T |
| **4** | U | V | W | X | Z |

### Bước 2: Tiền xử lý bản rõ

- Bản rõ gốc: `Do you like to study Cryptography course`
- Chuyển hoa + loại khoảng trắng: `DOYOULIKETOSTUDYCRYPTOGRAPHYCOURSE`
- Tách thành các cặp 2 ký tự (nếu 2 ký tự giống nhau thì chèn X):

```
DO  YO  UL  IK  ET  OS  TU  DY  CR  YP  TO  GR  AP  HY  CO  UR  SE
```

### Bước 3: Mã hóa từng cặp

| STT | Cặp rõ | Vị trí 1 | Vị trí 2 | Quy tắc | Cặp mã |
|-----|--------|----------|----------|---------|--------|
| 1 | DO | (1,4) | (0,1) | Hình chữ nhật | **HR** |
| 2 | YO | (1,2) | (0,1) | Hình chữ nhật | **HN** |
| 3 | UL | (4,0) | (3,0) | Cùng cột → dịch xuống | **MU** |
| 4 | IK | (2,3) | (2,4) | Cùng hàng → dịch phải | **KE** |
| 5 | ET | (2,0) | (3,4) | Hình chữ nhật | **KL** |
| 6 | OS | (0,1) | (3,3) | Hình chữ nhật | **AP** |
| 7 | TU | (3,4) | (4,0) | Hình chữ nhật | **LZ** |
| 8 | DY | (1,4) | (1,2) | Cùng hàng → dịch phải | **CB** |
| 9 | CR | (1,0) | (0,4) | Hình chữ nhật | **DM** |
| 10 | YP | (1,2) | (3,1) | Hình chữ nhật | **HQ** |
| 11 | TO | (3,4) | (0,1) | Hình chữ nhật | **PR** |
| 12 | GR | (2,2) | (0,4) | Hình chữ nhật | **KN** |
| 13 | AP | (0,3) | (3,1) | Hình chữ nhật | **OS** |
| 14 | HY | (1,1) | (1,2) | Cùng hàng → dịch phải | **YB** |
| 15 | CO | (1,0) | (0,1) | Hình chữ nhật | **HM** |
| 16 | UR | (4,0) | (0,4) | Hình chữ nhật | **ZM** |
| 17 | SE | (3,3) | (2,0) | Hình chữ nhật | **LI** |

### Bước 4: Kết quả

```
Plaintext:  DO YO UL IK ET OS TU DY CR YP TO GR AP HY CO UR SE
Ciphertext: HR HN MU KE KL AP LZ CB DM HQ PR KN OS YB HM ZM LI
```

**Bản mã cuối cùng:** `HRHNMUKEKLAPLZCBDMHQPRKNOSYBHMZMLI`
