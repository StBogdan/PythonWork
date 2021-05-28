from typing import Dict, List, Mapping

# Method store dict w/ _dirs and _files fiels, subdirs are sub dictionaries, file content as key of dict
# Time: O(m+n) where m is len(path) and n depth of filepath (for file r/w or mkdir)
# Space: O(trie(paths) + n)


class FileSystem:
    def __init__(self):
        self.file_syst_paths = {"_dirs": dict(), "_files": dict()}

    def ls(self, path: str) -> List[str]:
        elems = path.split("/")[1:]
        cwd = self.file_syst_paths

        if not elems[0]:
            print(f"Badabing on {path} w/ {cwd}")
            return self._dir_to_str(cwd)

        for i, path_elem in enumerate(elems):
            # print(f'Looking at {path_elem} in {cwd}')
            if path_elem not in cwd["_dirs"]:
                if i < len(elems) - 1:
                    # Not a dir and not the last
                    raise Exception(
                        f"Could not find directory {path_elem} of path {path}, part {i} of {len(elems)}"
                    )
                else:
                    return [path_elem]
            cwd = cwd["_dirs"][path_elem]

        # print(f"At cwd {cwd}")
        return self._dir_to_str(cwd)

    @staticmethod
    def _dir_to_str(directory: Dict[str, dict]) -> str:
        return sorted(
            list(directory["_files"].keys()) + list(directory["_dirs"].keys())
        )

    def mkdir(self, path: str) -> None:
        elems = path.split("/")[1:]
        cwd = self.file_syst_paths
        for dir in elems:
            if dir not in cwd["_dirs"]:
                cwd["_dirs"][dir] = {"_dirs": dict(), "_files": dict()}
            cwd = cwd["_dirs"][dir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        _, filename = filePath.rsplit("/", 1)
        cwd = self._get_file_dir(filePath)

        if filename not in cwd["_files"]:
            cwd["_files"][filename] = ""
        cwd["_files"][filename] += content

    def _get_file_dir(self, filePath: str) -> dict:
        elems = filePath.split("/")[1:]

        cwd = self.file_syst_paths
        for dir in elems[:-1]:
            cwd = cwd["_dirs"][dir]

        return cwd

    def readContentFromFile(self, filePath: str) -> str:
        _, filename = filePath.rsplit("/", 1)
        cwd = self._get_file_dir(filePath)
        return cwd["_files"][filename]


if __name__ == "__main__":
    fs = FileSystem()
    # ops = ["ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
    # ops_args = [["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

    ops = [
        "FileSystem",
        "mkdir",
        "ls",
        "mkdir",
        "ls",
        "ls",
        "ls",
        "addContentToFile",
        "ls",
        "ls",
        "ls",
    ]
    ops_args = [
        [],
        ["/m"],
        ["/m"],
        ["/w"],
        ["/"],
        ["/w"],
        ["/"],
        ["/dycete", "emer"],
        ["/w"],
        ["/"],
        ["/dycete"],
    ]

    for i in range(1, len(ops)):
        op = ops[i]
        args = ops_args[i]

        print(f"Calling op {op} and args {args}")
        res = fs.__getattribute__(op)(*args)
        print(f"Calling op {op} and args {args}, result: {res}")
