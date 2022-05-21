Started by user Ankit Asthana
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/JenkinsfileCD
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Preparation)
[Pipeline] sh
+ python3 --version
Python 3.7.10
[Pipeline] sh
+ python3 -m pip -V
pip 22.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
[Pipeline] echo
All
[Pipeline] echo
2
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Git Clone)
[Pipeline] git
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/JenkinsfileCD/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/ankitasthana-hu/mg-proj.git # timeout=10
Fetching upstream changes from https://github.com/ankitasthana-hu/mg-proj.git
 > git --version # timeout=10
 > git --version # 'git version 2.32.0'
 > git fetch --tags --force --progress -- https://github.com/ankitasthana-hu/mg-proj.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 32923a2a194e91496472db9d1857ae6fffcd5f44 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 32923a2a194e91496472db9d1857ae6fffcd5f44 # timeout=10
 > git branch -a -v --no-abbrev # timeout=10
 > git branch -D main # timeout=10
 > git checkout -b main 32923a2a194e91496472db9d1857ae6fffcd5f44 # timeout=10
Commit message: "Update fetchrecord.py"
 > git rev-list --no-walk 32923a2a194e91496472db9d1857ae6fffcd5f44 # timeout=10
[Pipeline] sh
+ ls -lrta
total 16
drwxr-xr-x 6 jenkins jenkins   98 May 21 14:04 ..
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 version.txt
-rw-r--r-- 1 jenkins jenkins 1131 May 21 14:05 test_fetchrecord.py
-rw-r--r-- 1 jenkins jenkins   47 May 21 14:05 requirements.txt
-rw-r--r-- 1 jenkins jenkins   18 May 21 14:05 README.md
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCI
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCD
drwxr-xr-x 3 jenkins jenkins   70 May 21 14:05 .pytest_cache
-rw-r--r-- 1 jenkins jenkins 3059 May 21 14:16 fetchrecord.py
drwxr-xr-x 5 jenkins jenkins  209 May 21 14:16 .
drwxr-xr-x 2 jenkins jenkins   92 May 21 14:16 __pycache__
drwxr-xr-x 8 jenkins jenkins  181 May 21 14:18 .git
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Unit/Integration Test)
[Pipeline] sh
+ cd /var/lib/jenkins/workspace/JenkinsfileCD
+ ls -lrta
total 16
drwxr-xr-x 6 jenkins jenkins   98 May 21 14:04 ..
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 version.txt
-rw-r--r-- 1 jenkins jenkins 1131 May 21 14:05 test_fetchrecord.py
-rw-r--r-- 1 jenkins jenkins   47 May 21 14:05 requirements.txt
-rw-r--r-- 1 jenkins jenkins   18 May 21 14:05 README.md
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCI
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCD
drwxr-xr-x 3 jenkins jenkins   70 May 21 14:05 .pytest_cache
-rw-r--r-- 1 jenkins jenkins 3059 May 21 14:16 fetchrecord.py
drwxr-xr-x 5 jenkins jenkins  209 May 21 14:16 .
drwxr-xr-x 2 jenkins jenkins   92 May 21 14:16 __pycache__
drwxr-xr-x 8 jenkins jenkins  181 May 21 14:18 .git
+ python3 -m pip install -r requirements.txt
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests==2.27.1 in /usr/local/lib/python3.7/site-packages (from -r requirements.txt (line 1)) (2.27.1)
Requirement already satisfied: urllib3==1.26.8 in /usr/local/lib/python3.7/site-packages (from -r requirements.txt (line 2)) (1.26.8)
Requirement already satisfied: pytest==7.1.2 in /usr/local/lib/python3.7/site-packages (from -r requirements.txt (line 3)) (7.1.2)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/site-packages (from requests==2.27.1->-r requirements.txt (line 1)) (2022.5.18.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.7/site-packages (from requests==2.27.1->-r requirements.txt (line 1)) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.7/site-packages (from requests==2.27.1->-r requirements.txt (line 1)) (3.3)
Requirement already satisfied: tomli>=1.0.0 in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (2.0.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (1.0.0)
Requirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (21.4.0)
Requirement already satisfied: iniconfig in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (1.1.1)
Requirement already satisfied: importlib-metadata>=0.12 in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (4.11.3)
Requirement already satisfied: py>=1.8.2 in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (1.11.0)
Requirement already satisfied: packaging in /usr/local/lib/python3.7/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (21.3)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest==7.1.2->-r requirements.txt (line 3)) (3.8.0)
Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/site-packages (from importlib-metadata>=0.12->pytest==7.1.2->-r requirements.txt (line 3)) (4.2.0)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/site-packages (from packaging->pytest==7.1.2->-r requirements.txt (line 3)) (3.0.9)
WARNING: There was an error checking the latest version of pip.
+ python3 -m pip show pytest
Name: pytest
Version: 7.1.2
Summary: pytest: simple powerful testing with Python
Home-page: https://docs.pytest.org/en/latest/
Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt, Floris Bruynooghe, Brianna Laugher, Florian Bruhin and others
Author-email: 
License: MIT
Location: /usr/local/lib/python3.7/site-packages
Requires: attrs, importlib-metadata, iniconfig, packaging, pluggy, py, tomli
Required-by: 
+ pytest -v test_fetchrecord.py
============================= test session starts ==============================
platform linux -- Python 3.7.10, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /var/lib/jenkins/workspace/JenkinsfileCD
collecting ... collected 5 items

test_fetchrecord.py::test_APIconnectivity PASSED                         [ 20%]
test_fetchrecord.py::test_dryrun_fetchdata PASSED                        [ 40%]
test_fetchrecord.py::test_APIcall PASSED                                 [ 60%]
test_fetchrecord.py::test_nodata_check PASSED                            [ 80%]
test_fetchrecord.py::test_comparedata_validity PASSED                    [100%]

=============================== warnings summary ===============================
../../../../../usr/lib64/python3.7/site-packages/simplejson/compat.py:23
  /usr/lib64/python3.7/site-packages/simplejson/compat.py:23: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
    from imp import reload as reload_module

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================= 5 passed, 1 warning in 0.23s =========================
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy Script to fetch data)
[Pipeline] script
[Pipeline] {
[Pipeline] sh
+ rm -rf 'out*'
[Pipeline] }
[Pipeline] // script
[Pipeline] sh
+ cd /var/lib/jenkins/workspace/JenkinsfileCD
+ python3 fetchrecord.py All 2
200
[[7, 'michael.lawson@reqres.in', 'Michael', 'Lawson', 'https://reqres.in/img/faces/7-image.jpg'], [8, 'lindsay.ferguson@reqres.in', 'Lindsay', 'Ferguson', 'https://reqres.in/img/faces/8-image.jpg'], [9, 'tobias.funke@reqres.in', 'Tobias', 'Funke', 'https://reqres.in/img/faces/9-image.jpg'], [10, 'byron.fields@reqres.in', 'Byron', 'Fields', 'https://reqres.in/img/faces/10-image.jpg'], [11, 'george.edwards@reqres.in', 'George', 'Edwards', 'https://reqres.in/img/faces/11-image.jpg'], [12, 'rachel.howell@reqres.in', 'Rachel', 'Howell', 'https://reqres.in/img/faces/12-image.jpg']]
User selected operation:  All
done
+ ls -lrta
total 20
drwxr-xr-x 6 jenkins jenkins   98 May 21 14:04 ..
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 version.txt
-rw-r--r-- 1 jenkins jenkins 1131 May 21 14:05 test_fetchrecord.py
-rw-r--r-- 1 jenkins jenkins   47 May 21 14:05 requirements.txt
-rw-r--r-- 1 jenkins jenkins   18 May 21 14:05 README.md
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCI
-rw-r--r-- 1 jenkins jenkins    0 May 21 14:05 JenkinsfileCD
drwxr-xr-x 3 jenkins jenkins   70 May 21 14:05 .pytest_cache
-rw-r--r-- 1 jenkins jenkins 3059 May 21 14:16 fetchrecord.py
drwxr-xr-x 2 jenkins jenkins   92 May 21 14:16 __pycache__
drwxr-xr-x 8 jenkins jenkins  181 May 21 14:18 .git
-rw-r--r-- 1 jenkins jenkins  536 May 21 14:18 out_allusers.csv
drwxr-xr-x 5 jenkins jenkins  233 May 21 14:18 .
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS


