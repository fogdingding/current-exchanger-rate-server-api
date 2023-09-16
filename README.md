# Current Exchanger Rate Server API

本專案為 Current Exchanger Rate 的 Server API，提供各個 Endpoint 進行操作，是以 Async 架構為主的 FastAPI 為框架來開發。

## API 文件

* **FastAPI 官方文件**：<https://fastapi.tiangolo.com/>

## 建置 Model 設定檔

使用者在啟用服務前，須先至 src/app/model/config.py 中，填入 model 相關設定
備註：已複製題目資料；無須建制。

```python
class ExchangeRateConfig(BaseSettings):
    exchange_rate_table: dict = {
        "currencies": { ... }
}
```

## 使用方式

##### 安裝 Python3 套件

請在目錄中，輸入以下的指令，本專案需確保 Python 版本 >= 3.9.12 ，其中 3.9.12 版本為本專案運行成功之版本。

```shell
$ python3 -m pip install -r requirements.txt
```

##### 啟動服務

在專案目錄中，輸入以下的指令，就會在 Localhost 啟動 API Server 服務，如果需要自訂 HOST:PORT，可以藉由使用 --host 及 --port 來設置。

```shell
$ uvicorn src.app.main:app --proxy-headers --forwarded-allow-ips='*'
```

當啟動本地端預設服務時，使用者可以在 <http://127.0.0.1:8000/docs> 中看到 Swagger API 文件。當作業系統為 Linux 時，如在 localhost 設置服務且用 Docker 設置運行，此時 Host 需設定成 172.17.0.1。

##### 啟動服務

在專案目錄中，輸入以下的指令，就會在 Localhost 啟動進行單元測試。需確保已經安裝過 httpx 和 pytest ，如步驟「安裝 Python3 套件 」。

```shell
$ pytest
```

## Docker 建置（容器運行）

進入 src 資料夾後，輸入以下指令來建立 Docker Image。

```shell
$ docker build -t current-exchanger-rate-server-api . --no-cache
```

之後回到專案目錄下執行指令（退出 src 資料夾）<http://127.0.0.1:8002/docs>。可以在 docker-compose.yml 中調整參數以及 docker 中對應出來的 PORT，最後利用 docker-compose up 啟動服務。

```shell
$ docker-compose up -d --build
```

當然也可以在容器內進行 pytest ，但是要注意 pytest 的快取資料夾需要額外刪除（如果有先執行 Localhost 的單元測試）

```shell
$ pytest
```
