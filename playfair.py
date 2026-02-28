def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used_chars = set()
    
    # Thêm ký tự của key vào ma trận
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)
            
    # Thêm các ký tự còn lại của bảng chữ cái
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
            
    # Chuyển list 25 ký tự thành ma trận 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def prepare_text(text):
    text = "".join([c.upper() for c in text if c.isalpha()]).replace('J', 'I')
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                prepared += a + 'X'
                i += 1
            else:
                prepared += a + b
                i += 2
        else:
            prepared += a + 'X'
            i += 1
    return prepared

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return -1, -1

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])
        
        if r1 == r2: # Cùng hàng: Dịch phải
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2: # Cùng cột: Dịch xuống
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else: # Khác hàng, khác cột: Hình chữ nhật
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
            
    return ciphertext, text

# ================= KẾT QUẢ KIỂM THỬ =================
if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "Do you like to study Cryptography course"
    
    ciphertext, prepared_text = encrypt_playfair(plaintext, key)
    
    print(f"Key: {key}")
    print(f"Plaintext gốc: {plaintext}")
    print(f"Plaintext đã xử lý: {prepared_text}")
    print(f"Ciphertext: {ciphertext}")