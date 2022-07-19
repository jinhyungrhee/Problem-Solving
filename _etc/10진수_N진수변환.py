# N진수 -> 10진수 : int() 메서드 사용
print(int('101', 2)) # 5
print(int('202', 3)) # 20
print(int('303', 4)) # 51
print(int('404', 5)) # 104
print(int('505', 6)) # 185
print(int('707', 8)) # 455
print(int('ACF', 16)) # 2767

# 10진수 -> N진수 : 
def decimal_to_n_ary(n, q): # n : 10진수 , q : 변환할 진법
  rev_base = ''

  while n > 0:
    n, mod = divmod(n, q) # 몫, 나머지
    rev_base += str(mod) # 나머지만 string에 저장

  # 저장된 나머지들을 역순으로 변환
  return rev_base[::-1]
print(decimal_to_n_ary(20, 3)) # 202

# 10진수 -> 2진수, 8진수, 16진수 : bin(), oct(), hex()
print(bin(5)) # 0b101 (str)
print(oct(455)) # 0o707 (str)
print(hex(2767)) # 0xacf (str)
