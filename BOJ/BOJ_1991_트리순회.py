n = int(input())

tree = {}

for _ in range(n):
  p, left, right = input().split()
  tree[p] = [left, right]

# print(tree)

def preorder(node):
  if node == '.':
    return
  
  print(node, end='')
  
  preorder(tree[node][0])
  preorder(tree[node][1])


def inorder(node):
  if node == '.':
    return

  inorder(tree[node][0])
  print(node, end='')
  inorder(tree[node][1])

def postorder(node):
  if node == '.':
    return 

  postorder(tree[node][0])
  postorder(tree[node][1])
  print(node, end='')

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')