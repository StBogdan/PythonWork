from typing import List


class Node:
    children = {}

    def __init__(self, value, is_leaf, full_path):
        self.value = value
        self.full_path = full_path
        self.is_leaf = is_leaf
        self.children = {}

    def __str__(self):
        return f"Val:{self.value} + Path:{self.full_path} + Children:{self.children} + IsLeaf:{self.is_leaf}"


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        known_folder = Node("", False, "")
        non_subdirs = []
        for folder_str in folder:
            fe = folder_str.split("/")[1:]
            # print(fe)
            cur_node = known_folder
            for indiv in fe:
                # print(f"{indiv} cn: {cur_node}")
                if cur_node.is_leaf:
                    # print("oof")
                    break
                if indiv in cur_node.children:
                    cur_node = cur_node.children[indiv]
                else:
                    cur_node.children[indiv] = Node(
                        indiv, False, cur_node.full_path + "/" + indiv
                    )
                    cur_node = cur_node.children[indiv]
            cur_node.is_leaf = True

        to_explore = [known_folder]
        value = known_folder.value
        while to_explore:
            cur_elem = to_explore.pop()
            # print(f"Aaaaaaaaa {cur_elem}")

            if cur_elem.is_leaf:
                non_subdirs.append(cur_elem.full_path)
            else:
                for val in cur_elem.children.values():
                    to_explore.append(val)

        return non_subdirs


if __name__ == "__main__":
    folder = ["/a/b", "/a/b/c", "/a/b/ca", "/a/b/d"]
    sol = Solution()
    print(f"Ans: {sol.removeSubfolders(folder)}")
