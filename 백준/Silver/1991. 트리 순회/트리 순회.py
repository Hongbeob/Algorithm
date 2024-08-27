def preorder(node):
    if str(node).isalpha():
        node = Tree.index(node)
    if not node:
        return
    print(Tree[node],end="")
    preorder(left[node])
    preorder(right[node])

def inorder(node):
    if str(node).isalpha():
        node = Tree.index(node)
    if not node:
        return
    inorder(left[node])
    print(Tree[node],end='')
    inorder(right[node])

def postorder(node):
    if str(node).isalpha():
        node = Tree.index(node)
    if not node:
        return
    postorder(left[node])
    postorder(right[node])
    print(Tree[node],end='')

N=int(input())
lst=[list(input().split()) for _ in range(N)]
Tree=[0]*(N+1)
left=[0]*(N+1)
right=[0]*(N+1)
for i in range(N):
    Tree[i+1]=lst[i][0]
    if lst[i][1] != '.':
        left[i+1]=lst[i][1]

    if lst[i][2] != '.':
        right[i+1] = lst[i][2]

preorder(1)
print()
inorder(1)
print()
postorder(1)