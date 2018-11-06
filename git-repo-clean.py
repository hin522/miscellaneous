import os
import subprocess
import shutil

def get_folders_recursively():
  return os.popen('find . -type d').readlines()

def get_folders():
  return os.popen('ls -d */').readlines()

def find_folder_end_with(folders, pattern):
  return list(filter(lambda f: (f.endswith(pattern+"\n") and f.count(pattern) == 1), folders))

def remove_folder_recursively(name):
  print("Removing " + name[:-1])
  shutil.rmtree(name[:-1])

def find_and_remove_folders_recursively(suffix):
  all_folders = get_folders_recursively()
  folders_to_remove = find_folder_end_with(all_folders, suffix)
  for r in folders_to_remove:
    remove_folder_recursively(r)

######################################
all_git_repo_folders = get_folders()

for git_repo in all_git_repo_folders:
  git_repo=git_repo[:-2]
  os.chdir(git_repo)
  print("Go to " + os.getcwd())

  find_and_remove_folders_recursively("/node_modules")
  find_and_remove_folders_recursively("/build")
  find_and_remove_folders_recursively("/.git")
  find_and_remove_folders_recursively("/.idea")
  find_and_remove_folders_recursively("/gradle")
  find_and_remove_folders_recursively("/.gradle")
  find_and_remove_folders_recursively("/.metadata")
  find_and_remove_folders_recursively("/target")
  find_and_remove_folders_recursively("/classes")
  find_and_remove_folders_recursively("/generated")
  find_and_remove_folders_recursively("/out")
  find_and_remove_folders_recursively("/.settings")
  find_and_remove_folders_recursively("/coverage")
  find_and_remove_folders_recursively("/ci")
  find_and_remove_folders_recursively("/logs")

  os.chdir("..")