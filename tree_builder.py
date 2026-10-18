class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        is_initial_call = current_node is None
        if current_node is None:
            current_node = self.root

        if current_node is None:
            print("Error: The tree is empty.")
            return False

        if current_node.name == manager_name:
            if side not in ("left", "right"):
                print("Error: Side must be 'left' or 'right'.")
                return False

            if getattr(current_node, side) is not None:
                print(f"Error: The {side} side is already occupied.")
                return False

            setattr(current_node, side, EmployeeNode(employee_name))
            return True

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        if is_initial_call:
            print(f"Error: Manager '{manager_name}' does not exist.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here
company_directory = TeamTree()
company_directory.root = EmployeeNode("Jordan")

company_directory.insert("Jordan", "Taylor", "right")
company_directory.insert("Jordan", "Riley", "left")
company_directory.insert("Riley", "Dana", "right")
company_directory.insert("Riley", "Morgan", "left")

company_directory.print_tree()








# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


# Design Memo
# Recursive insertion begins at the root and compares each visited node's name
# with the requested manager's name. When it finds the manager, it checks
# whether the requested side is either "left" or "right" and whether that child
# position is empty. If the position is available, it creates an EmployeeNode
# for the new employee and attaches it there. If the current node is not the
# manager, insert() searches the left subtree and then the right subtree. Its
# return value tells earlier recursive calls whether insertion succeeded, so
# the search can stop as soon as the employee is added. If the manager cannot
# be found, or the tree is empty, the method prints an error instead.
# One challenge was searching for a manager who might be several levels below
# the root. Checking only the root would work for the team lead, but would not
# find other managers. Recursion makes it possible to apply the same search to
# each child subtree. Another challenge was preventing an employee from
# replacing a child that already exists. Checking the requested side before
# assignment protects the existing tree structure. The method also needs to
# distinguish a successful insertion from an unsuccessful search, which is
# why it returns True after adding the employee and False when it cannot.
# Trees are useful when the data has a hierarchy or parent-child relationships.
# A company directory is one example: managers can have employees beneath
# them, and those employees may manage teams of their own. Trees are also a
# natural fit for file and folder structures, organization charts, and some
# search indexes. Compared with a list, a tree can represent how items relate
# to one another instead of storing them only in a sequence. This structure
# can make hierarchical relationships easier to understand and navigate.