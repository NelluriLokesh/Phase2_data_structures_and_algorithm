"""
 JAVA BAVA...................
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) return null;
        TreeNode root = null;
        while(head!=null){
            root = insert(root,head.val);
            head = head.next;
        }
        return root;
    }
    TreeNode insert(TreeNode root,int data){
        // BST
        if(root == null)
            return new TreeNode(data);
        if(root.val < data)
            root.right = insert(root.right,data);
        else if(root.val > data)
            root.left = insert(root.left,data);

        int balance = balanceFactor(root);

        if(balance < -1 && data > root.right.val)
            return leftRotate(root);
        if(balance > 1 && data < root.left.val)
            return rightRotate(root);
        if(balance > 1 && data > root.left.val){
            root.left = leftRotate(root.left);
            return rightRotate(root.right);
        }
        if(balance < -1 && data < root.right.val){
            root.right = rightRotate(root.right);
            return leftRotate(root.left);
        }
        return root;
    }
    // left rotate
    TreeNode leftRotate(TreeNode node){
        TreeNode temp = node.right;
        TreeNode t2 = temp.left;
        temp.left = node;
        node.right = t2;
        return temp;
    }
    // right Rotate
    TreeNode rightRotate(TreeNode node){
        TreeNode temp = node.left;
        TreeNode t2 = temp.right;
        temp.right = node;
        node.left = t2;
        return temp;
    }
    // balance factor
    int balanceFactor(TreeNode root){
        if(root == null) return 0;
        return height(root.left) - height(root.right);
    }
    int height(TreeNode root){
        if(root == null)
            return 0;
        return 1 + Math.max(height(root.left),height(root.right));
    }
}
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insertBst(root,data):
    if root == None:
        return Node(data)
    elif root.data < data :
        root.right = insertBst(root.right,data)
    elif root.data > data :
        root.left = insertBst(root.left,data)
    b = balanceFactor(root)
    if b < -1 and data > root.right.data:
        return leftRotation(root)
    if b > 1 and data < root.left.data:
        return rightRotation(root)
    if b > 1 and data > root.left.data:
        root.left = leftRotation(root.left)
        return rightRotation(root)
    if b <  -1 and data < root.right.data:
        root.right = rightRotation(root.right)
        return leftRotation(root)   
    return root
def leftRotation(root):
    temp = root.right
    t2 = temp.left
    temp.left = root
    root.right = t2
    return temp
def rightRotation(root):
    temp = root.left
    t2 = temp.right
    temp.right = root
    root.left = t2
    return temp
def balanceFactor(root):
    if root == None: return 0
    return height(root.left) - height(root.right)
def height(root):
    if root == None : return 0
    return 1 + max(height(root.left),height(root.right))
def Inorder(root): # Do Leetcode Problems 
    if root == None:
        return
    Inorder(root.left)
    print(root.data,end = ' ')
    Inorder(root.right)
root = None
root = insertBst(root,7)
root = insertBst(root,4)
root = insertBst(root,9)
root = insertBst(root,-4)
root = insertBst(root,2)
root = insertBst(root,0)
Inorder(root)