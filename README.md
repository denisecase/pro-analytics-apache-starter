# pro-analytics-apache-starter

Apache Spark development environment for macOS, Linux, and **Windows (on WSL)**.

---

## 0. Windows Users: Set up WSL First

Follow the [WSL installation instructions](01-setup/windows-users-install-wsl.md), then run all commands in WSL.

Open WSL by opening a PowerShell terminal and running wsl.

```powershell
wsl
```

## 1. Install Java (JDK 17)

### 1a. Mac Users

1. Download Temurin 17 from Adoptium: <https://adoptium.net/installation/>
2. Install the `.pkg` file for Java 17

### 1a. WSL/Linux

Open your WSL/Linux terminal and run:

```shell
sudo apt update
sudo apt install openjdk-17-jdk -y
```

### 1b: Verify (should show 17.x.x)

```shell
java --version
```

## 2. Get the Code

1. Log in to GitHub. 
2. Go to: <https://github.com/denisecase/pro-analytics-apache-starter>. 
3. Click "Use this template" to get a copy in your GitHub account.
4. In your shell ($ prompt) terminal (Windows users: inside WSL), go to your `Repos` folder, clone **your new repository URL**, and change directory into it:

```shell
cd ~/Repos
git clone https://github.com/YOUR_ACCOUNT/pro-analytics-apache-starter
cd pro-analytics-apache-starter
```

## 3. Create Python Virtual Environment

Run the following commands in your shell ($ prompt) terminal. Windows users use WSL.

```shell
git pull origin main
uv python pin 3.12
uv venv
source .venv/bin/activate
uv sync --extra dev --extra docs --upgrade
uv run pre-commit install
```

## 4. Run Example

```shell
uv run python src/analytics_project/test-pyspark.py
```

## 5. After Modifications

Change your commit message to explain what was done, e.g. "add new .py file".

```shell
git add .
git commit -m "your change in quotes"
git push -u origin main 

---

## Troubleshooting

### JDK Versions

If you have multiple JDK versions installed (either 17 or 21 should work), you can select which one is active using:

```shell
sudo update-alternatives --config java
```

### Spark Error (`/opt/spark`)

If you see: 

```text
FileNotFoundError: [Errno 2] No such file or directory: '/opt/spark/./bin/spark-submit'
FAIL: Exception during test. See logs above.
```

```shell
# Check what's set
echo $SPARK_HOME
# Probably shows /opt/spark

# Temporarily unset it
unset SPARK_HOME

# Test again
uv run python src/analytics_project/test-pyspark.py
```
