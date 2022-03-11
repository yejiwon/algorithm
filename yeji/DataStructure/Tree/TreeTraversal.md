### Tree Traversal

---

트리를 각 노드를 한번씩만 체계적으로 순회하는 방법<br/>
노드 방문 순서에 따라 아래처럼 나눠짐<br>

- preorder(전위)
- inorder(중위)
- postorder(후위)
- level-order

### Preorder Traversal

> 전위 순회 or 깊이 우선 순회

#### 순회 방법

1. 노드를 방문
2. 왼쪽 서브트리를 전위 순회
3. 오른쪽 서브트리 전위 순회

즉, 노드를 먼저 방문하고 왼쪽 끝까지 내려간 다음 오른쪽으로 이동해 다시 시작하거나 순회를 계속

```
preorder(node)
    print node.value // node.value: 노드의 값
    if node.left != null then preorder(node.left) // node.left: 왼쪽 자식 node
    if node.right != null then preorder(node.right) // node.right: 오른쪽 자식 노드
```

### Inorder Traversal

> 중위 순회 or 대칭 순회

#### 순회 방법

1. 왼쪽 서브트리를 중위 순회
2. 노드 방문
3. 오른쪽 서브트리를 중위 순회

즉, 왼쪽 끝까지 내려간 후 노드를 방문하고 오른쪽 자식 노드로 이동해 순회를 계속

```
inorder(node)
    if node.left != null then inorder(node.left)
    print node.value
    if node.right != null then inorder(node.right)
```

### Postorder Traversal

> 후위 순회

#### 순회 방법

1. 왼쪽 서브트리 후위 순회
2. 오른쪽 서브트리 후위 순회
3. 노드 방문

```
postorder(node)
    if node.left  != null then postorder(node.left)
    if node.right != null then postorder(node.right)
    print node.value
```

### Levelorder Traversal

> 레벨 순서 순회 or 너비 우선 순회

#### 순회 방법

모든 노드를 낮은 레벨부터 차례대로 순회

큐 사용하여 구현 가능

```
levelorder(root)
    q = empty queue
    q.enqueu(root)
    while not q.empty do
        node := q.dequeue()
        visit(node)
        if node.left not null:
            q.enqueue(node.left)
        if node.right not null:
            q.enqueue(node.right)
```
