class TreeNode:  
    def __init__(self, value):  
        self.value = value  
        self.left = None  
        self.right = None  

def build_tree(nodes):  
    if not nodes or nodes[0] == -1:  
        return None  

    root = TreeNode(nodes[0])  
    queue = [root]  
    i = 1  

    while i < len(nodes):  
        current = queue.pop(0)  

        # ساخت گره چپ اگر موجود باشد  
        if i < len(nodes) and nodes[i] != -1:  
            current.left = TreeNode(nodes[i])  
            queue.append(current.left)  
        i += 1  

        # ساخت گره راست اگر موجود باشد  
        if i < len(nodes) and nodes[i] != -1:  
            current.right = TreeNode(nodes[i])  
            queue.append(current.right)  
        i += 1  

    return root  

def invert_tree(node):  
    if not node:  
        return  
    # معکوس کردن گره‌ها  
    node.left, node.right = node.right, node.left  
    invert_tree(node.left)  
    invert_tree(node.right)  

def inorder_traversal(node):  
    if node is None:  
        return []  
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)  

if __name__ == "__main__":  
    input_data = input("Enter the tree nodes: ")  
    nodes = list(map(int, input_data.split()))  

    tree_root = build_tree(nodes)  
    invert_tree(tree_root)  
    result = inorder_traversal(tree_root)  

    print(' '.join(map(str, result)))