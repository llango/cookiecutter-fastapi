# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## 安装依赖

- Python3.8.2
- Pip
- Poetry 

### M.L 模型环境

```sh
MODEL_PATH={{cookiecutter.machine_learn_model_path}}
MODEL_NAME={{cookiecutter.machine_learn_model_name}}
```

### 更新 `/predict`

若要更新机器学习模型，请 [在这里](app/api/routes/predictor.py#L13) `predictor.py` 中 添加 `load` 和 `method`。

## 安装

```sh
python -m venv venv
source venv/bin/activate
make install
```

## 本机运行 

`make run`

## 部署应用

`make deploy`

## 运行测试

`make test`

## 运行彩蛋

`make easter`

## 访问 Swagger 文档 

> <http://localhost:8080/docs>

## 访问 Redocs 文档 

> <http://localhost:8080/redoc>

## 项目结构

与应用相关的文件在`app`或者 `tests`目录。 应用部分为： 

    app
    ├── api              - 网络相关的东西。
    │   └── routes       - 路由
    ├── core             - 应用程序配置、启动事件、日志记录。
    ├── models           - pydantic 模型
    ├── services         - 不仅仅是与 crud 相关的逻辑。
    └── main.py          - FastAPI 应用创建和配置。
    ├──
    tests                - pytest。
