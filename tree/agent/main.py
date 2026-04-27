import json

def load_tree():
    with open("../tree/reflection-tree.json", "r") as file:
        return json.load(file)

def find_node(tree, node_id):
    for node in tree["nodes"]:
        if node["id"] == node_id:
            return node
    return None

def run_reflection():
    tree = load_tree()
    current_id = "START"

    while True:
        node = find_node(tree, current_id)

        if not node:
            print("Error: Node not found.")
            break

        print("\n" + node["text"])

        if node["type"] == "question":
            for i, option in enumerate(node["options"], 1):
                print(f"{i}. {option['label']}")

            choice = int(input("Choose an option: "))
            current_id = node["options"][choice - 1]["next"]

        elif node["type"] == "reflection":
            current_id = node["next"]

        elif node["type"] == "end":
            break

        else:
            current_id = node["next"]

if __name__ == "__main__":
    run_reflection()
