from pathlib import Path
import filecmp

newFiles = []
missingFiles = []
notComparableFiles = []
mismatchFiles = []
errorsMisMatch = []

def compare_dir_trees(inputDir, baselineDir):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param inputDir: directory path which need to be validate
    @param baselineDir: baseline path

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(inputDir, baselineDir)

    newFiles.append(dirs_cmp.left_only) if dirs_cmp.left_only else newFiles
    missingFiles.append(dirs_cmp.right_only) if dirs_cmp.right_only else missingFiles
    notComparableFiles.append(dirs_cmp.funny_files) if dirs_cmp.funny_files else notComparableFiles
        
    (_, mismatch, errors) =  filecmp.cmpfiles(
        inputDir, baselineDir, dirs_cmp.common_files, shallow=False)

    mismatchFiles.append(mismatch) if mismatch else mismatchFiles
    errorsMisMatch.append(errors) if errors else mismatchFiles

    for common_dir in dirs_cmp.common_dirs:
        source_subdir = Path(inputDir)/common_dir
        target_subdir = Path(baselineDir)/common_dir
        compare_dir_trees(source_subdir, target_subdir)
    return


if __name__ == "__main__":
    sourcePath = "D://tmp/openrefine/"
    targetPath = "D://tmp/openrefineV2"
    if Path(sourcePath).exists and Path(targetPath).exists:
        compare_dir_trees(sourcePath, targetPath)
        print("new files: " + str(newFiles))
        print("missing files: " + str(missingFiles))
        print("not comparable files: " + str(notComparableFiles))
        print("mismatch files: " + str(mismatchFiles))
        print("errors: " + str(errorsMisMatch))
        
    else:
        print("Dir not exists. Please check the input.")
