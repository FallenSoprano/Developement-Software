
class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:

                self.left = TreeNode(value)

            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return f"The number {value} is not in the tree"
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return f"The number {value} is not in the tree"
            else:
                return self.right.find(value)

        else:
            return f"The number {value} is in the tree"

    def remove(self, value):
        if value < self.value:
            if self.left is None:
                return self, f"The number {value} is not in the tree"
            self.left, message = self.left.remove(value)
            return self, message
        elif value > self.value:
            if self.right is None:
                return self, f"The number {value} is not in the tree"
            self.right, message = self.right.remove(value)
            return self, message
        else:
            # Node to delete found
            # Case 1: No children
            if self.left is None and self.right is None:
                return None, f"Successfully deleted {value}"
            # Case 2: One child
            elif self.left is None:
                return self.right, f"Successfully deleted {value}"
            elif self.right is None:
                return self.left, f"Successfully deleted {value}"
            # Case 3: Two children
            else:
                # Find minimum value in right subtree
                min_node = self.right
                while min_node.left:
                    min_node = min_node.left
                self.value = min_node.value
                self.right, message = self.right.remove(min_node.value)
                return self, f"Successfully deleted {value}"

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)
        if self.right:
            self.right.inorder_traversal()


m = 0
numbers = [50, 30, 70, 20, 40, 60, 80]
tree = TreeNode(numbers[0])

for num in numbers[1:]:
    tree.insert(num)

while m == 0:


    print("....Menu....")
    print(" ")
    print("1. Search for a specific number")
    print("2. Delete a specific number")
    print("3. Print the tree in in-order traversal")
    print("4. End program")


    try:
        option = int(input("\nEnter your choice: "))

        if option == 1:
            print(" ")
            to_find = int(input("Enter the number: "))
            print(" ")
            print(tree.find(to_find))

        elif option == 2:
            print(" ")
            to_delete = int(input("Enter the number: "))
            print(" ")
            print(tree.remove(to_delete))
            print(" ")
            tree.inorder_traversal()
            print(" ")

        elif option == 3:
            print(" ")
            tree.inorder_traversal()
            print(" ")

        elif option == 4:
            print(" ")
            print("Closing the program...")
            print("Thank you for using this program")
            print(" ")
            m += 1

        else:
            print("Please enter a valid option")


    except ValueError:
        print(" ")
        print("Value error: Please enter what is asked\n\n")
        print(" ")

