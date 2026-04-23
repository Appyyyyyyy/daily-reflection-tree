import csv

# Load tree
def load_tree(file_path):
    nodes = {}
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            nodes[row['id']] = row
    return nodes

# Parse decision logic
def parse_decision(options_str):
    rules = []
    if not options_str:
        return rules
    parts = options_str.split(';')
    for part in parts:
        cond, target = part.split(':')
        answers = cond.replace('answer=', '').split('|')
        rules.append((answers, target))
    return rules

# State tracking
state = {
    "answers": {},
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0, "neutral": 0},
    "axis3": {"self": 0, "team": 0, "wide": 0}
}

def update_signal(signal):
    if not signal:
        return
    axis, val = signal.split(':')
    if axis in state and val in state[axis]:
        state[axis][val] += 1

def get_dominant(axis):
    return max(state[axis], key=state[axis].get)

# Run agent
def run(tree):
    current = "START"

    while True:
        node = tree[current]
        ntype = node["type"]
        text = node["text"]

        # Replace placeholders
        for k, v in state["answers"].items():
            text = text.replace(f"{{{k}.answer}}", v)

        print("\n" + text)

        if ntype == "end":
            break

        if ntype == "question":
            options = node["options"].split('|')
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")

            choice = int(input("Choose: ")) - 1
            answer = options[choice]
            state["answers"][node["id"]] = answer

            update_signal(node["signal"])

            # Move to next (child or decision)
            # Find next node with this parent
            next_node = None
            for n in tree.values():
                if n["parentId"] == node["id"]:
                    next_node = n["id"]
                    break
            current = next_node

        elif ntype == "decision":
            prev_answer = list(state["answers"].values())[-1]
            rules = parse_decision(node["options"])
            for answers, target in rules:
                if prev_answer in answers:
                    current = target
                    break

        elif ntype in ["reflection", "bridge"]:
            update_signal(node["signal"])
            input("\n(Press Enter to continue)")
            # go to child
            for n in tree.values():
                if n["parentId"] == node["id"]:
                    current = n["id"]
                    break

        elif ntype == "summary":
            a1 = get_dominant("axis1")
            a2 = get_dominant("axis2")
            a3 = get_dominant("axis3")

            text = text.replace("{axis1.dominant}", a1)
            text = text.replace("{axis2.dominant}", a2)
            text = text.replace("{axis3.dominant}", a3)

            print("\n" + text)
            input("\n(Press Enter to continue)")

            for n in tree.values():
                if n["parentId"] == node["id"]:
                    current = n["id"]
                    break

        else:  # start
            for n in tree.values():
                if n["parentId"] == node["id"]:
                    current = n["id"]
                    break


if __name__ == "__main__":
    tree = load_tree("../tree/reflection-tree.tsv")
    run(tree)
